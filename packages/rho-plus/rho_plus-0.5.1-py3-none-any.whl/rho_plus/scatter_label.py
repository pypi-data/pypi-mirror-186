#!/usr/bin/env python3
"""The (relatively involved) algorithm for automatically labeling a scatterplot."""

import numpy as np
import textwrap
import matplotlib as mpl
import matplotlib.pyplot as plt

from functools import lru_cache

from .color_util import contrast_with


def compute_bbox(text, ax, **kwargs) -> mpl.transforms.Bbox:
    """
    Compute the bounding box without forcing a draw.

    Will error unless ax.figure.draw() has been called.
    """
    t = ax.text(0.5, 0.5, text, transform=ax.transAxes, **kwargs)
    bb = t.get_window_extent()
    t.remove()
    return bb


def draw_bbox(bbox, ax):
    bl, tl, br, tr = bbox.transformed(ax.transAxes.inverted()).corners()
    xy = np.vstack([bl, tl, tr, br, bl])
    ax.plot(*xy.T, transform=ax.transAxes, lw=0.5)


def in_bbox(pts, bbox):
    return (
        (pts[:, 0] >= bbox.xmin)
        & (pts[:, 0] <= bbox.xmax)
        & (pts[:, 1] >= bbox.ymin)
        & (pts[:, 1] <= bbox.ymax)
    )


def intersects(pts, xc, yc, ww, hh):
    xx = np.array(xc).reshape(-1, 1)
    yy = np.array(yc).reshape(-1, 1)

    xmin, xmax = xx - ww / 2, xx + ww / 2
    ymin, ymax = yy - hh / 2, yy + hh / 2

    return np.any(
        (pts[:, 0] >= xmin)
        & (pts[:, 0] <= xmax)
        & (pts[:, 1] >= ymin)
        & (pts[:, 1] <= ymax),
        axis=1,
    ).flatten()


@lru_cache(None)
def get_pts(ax):
    out = ax.figure.canvas.buffer_rgba().tolist()

    bgcolor = np.array(mpl.colors.to_rgba(plt.rcParams["figure.facecolor"])) * 255

    mask = np.not_equal(out, bgcolor).any(axis=2)
    # plt.imshow(mask)

    ii, jj = np.vstack(np.nonzero(mask))
    img_h, img_w = mask.shape
    # convert from image coordinates to (x, y)
    pts = np.vstack([jj, img_h - 1 - ii]).T

    # pad to make sure that the x and y axes are included
    ax_bb = ax.patch.get_extents().padded(3)

    # only consider points within the axis bounds
    return pts[in_bbox(pts, ax_bb)]


def compute_possible_locs(ax_bb, ND=20):
    if ax_bb is None:
        return ([], [])

    xspace = np.linspace(ax_bb.xmin, ax_bb.xmax, ND)
    yspace = np.linspace(ax_bb.ymin, ax_bb.ymax, ND)

    xx, yy = np.meshgrid(xspace, yspace)

    return (xx.flatten(), yy.flatten())


def compute_valid_locs(bb, ax_bb, pts, ND=20, other_bboxes=()):
    xx, yy = compute_possible_locs(ax_bb, ND=ND)

    xy = np.vstack([xx, yy]).T
    for bbox in other_bboxes:
        # pad so new label text wouldn't overlap
        # not just the center
        padded = bbox.expanded(
            1 + (bb.width / 1) / bbox.width, 1 + (bb.height / 1) / bbox.height
        )
        xy = xy[~in_bbox(xy, padded)]

    xx, yy = xy.T

    valid = ~intersects(pts, xx, yy, bb.width, bb.height)
    valid_xx = xx[valid].flatten()
    valid_yy = yy[valid].flatten()
    return np.vstack([valid_xx, valid_yy]).T


def best_loc(bb, ax_bb, pts, x, y, data_xy_fig, dpi, nd=40, other_bboxes=()):
    locs = compute_valid_locs(bb, ax_bb, pts, nd, other_bboxes)

    if len(locs) == 0:
        # no valid placement
        return None

    dist = np.sqrt((locs[:, 0] - x) ** 2 + (locs[:, 1] - y) ** 2)
    dist /= dpi

    arr = np.abs(locs.reshape(-1, 1, 2) - data_xy_fig.reshape(1, -1, 2))
    arr[:, 0] = arr[:, 0] - bb.width / 2
    arr[:, 1] = arr[:, 1] - bb.height / 2
    arr /= dpi
    arr = arr.clip(0, np.inf)
    forces = np.linalg.norm(arr, axis=-1)

    def normpdf(x, sigma):
        return np.exp(-0.5 * (x / sigma) ** 2) / (sigma * np.sqrt(np.pi * 2))

    def max1_normpdf(x, sigma):
        return normpdf(x, sigma) / normpdf(0, sigma)

    sigma = 4
    repulsion = np.mean(max1_normpdf(forces, sigma), axis=1)

    attraction = max1_normpdf(dist, 1)

    return locs[np.argmin(repulsion - 0.7 * attraction)]


def scatter_labels(
    labels, colors=None, ax=None, MIN_ARROW_LEN=0.2, MAX_ANNOT_DIST=1, **kwargs
):
    if ax is None:
        ax = plt.gca()

    # set the renderer so each call to compute_bbox doesn't have to
    ax.figure.canvas.draw()

    dpi = ax.figure.get_dpi()

    for c in ax.get_children():
        if isinstance(c, mpl.collections.PathCollection):
            xydata = c.get_offsets().filled()
            if len(xydata) > 0:
                data_xy = xydata
                break
    else:
        raise ValueError("Couldn't find scatterplot data")

    data_x, data_y = data_xy.T
    if colors is None:
        colors = c.get_facecolor()
    else:
        colors = np.broadcast_to(np.array(colors), data_x.shape)

    labels = np.array(labels)

    data_pts = (ax.transData - ax.transAxes).transform(data_xy)

    dists = np.linalg.norm(data_pts - 0.5, ord=2, axis=1)

    xy_fig = ax.transData.transform(data_xy)

    ax_bb = ax.patch.get_extents()

    max_annot_dist_fig = MAX_ANNOT_DIST * ax.figure.get_dpi()

    # start from the outside and work inwards
    label_texts = []
    label_xy = []
    label_locs = []
    do_draw_arrow = []
    label_bboxes = []
    label_colors = []

    for i in np.argsort(dists)[::-1]:
        for width in (1000, 30, 15):
            label = "\n".join(textwrap.wrap(labels[i], width=width))
            x = data_x[i]
            y = data_y[i]
            bb = compute_bbox(label, ax, **kwargs).padded(dpi * 2 / 72)
            data_bbox = mpl.transforms.Bbox.from_bounds(
                *xy_fig[i] - max_annot_dist_fig / 2,
                max_annot_dist_fig,
                max_annot_dist_fig,
            )
            # shrink to give room for label
            ax_bb_padded = ax_bb.expanded(
                1 - bb.width / ax_bb.width, 1 - bb.height / ax_bb.height
            )
            data_bbox = mpl.transforms.Bbox.intersection(data_bbox, ax_bb_padded)
            # draw_bbox(data_bbox, ax)

            # loc_fig = closest_loc(bb, data_bbox, get_pts(ax), *ax.transData.transform([x, y]), 4, bboxes)
            loc_fig = best_loc(
                bb,
                data_bbox,
                get_pts(ax),
                *ax.transData.transform([x, y]),
                xy_fig,
                dpi,
                4,
                label_bboxes,
            )
            if loc_fig is not None:
                annot_dist = np.sqrt(np.sum(np.square(xy_fig[i] - loc_fig))) / dpi

                loc_data = ax.transData.inverted().transform(loc_fig)
                # place at best location
                label_texts.append(label)
                label_xy.append((x, y))
                label_locs.append(loc_data)

                do_draw_arrow.append(annot_dist > MIN_ARROW_LEN)
                label_bboxes.append(
                    bb.translated(
                        loc_fig[0] - (bb.xmin + bb.xmax) / 2,
                        loc_fig[1] - (bb.ymin + bb.ymax) / 2,
                    )
                )

                for j in np.linspace(0, 1, 6):
                    arrow_x, arrow_y = loc_fig + (xy_fig[i] - loc_fig) * j
                    arrow_size = 0.01 * dpi
                    label_bboxes.append(
                        mpl.transforms.Bbox.from_bounds(
                            arrow_x - arrow_size / 2,
                            arrow_y - arrow_size / 2,
                            arrow_size,
                            arrow_size,
                        )
                    )

                label_colors.append(colors[i])

                # no need to check other widths
                break


    for label, xy_loc, loc, draw_arrow, color in zip(
        label_texts, label_xy, label_locs, do_draw_arrow, label_colors
    ):
        ax.annotate(
            label,
            xy_loc,
            loc,
            ha="center",
            va="center",
            arrowprops=dict(arrowstyle="-", color=color) if draw_arrow else None,
            color=contrast_with(color, ax.get_facecolor()),
            **kwargs,
        )

        # if draw_arrow:
        #     ax.arrow(*loc, *(xy_loc - loc), head_length=0, color=color, zorder=1)

    # for bbox in label_bboxes:
    #     draw_bbox(bbox, ax)
    return ax
