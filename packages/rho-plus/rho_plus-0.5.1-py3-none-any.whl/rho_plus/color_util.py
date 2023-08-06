import numpy as np
import hsluv
import matplotlib as mpl


def to_rgb(c):
    """Converts any matplotlib color to RGB."""
    return np.array(mpl.colors.to_rgb(c))


def to_hsluv(rgb):
    return np.array(hsluv.rgb_to_hsluv(rgb))


def lightness(c):
    """Returns lightness from 0-1"""
    return to_hsluv(to_rgb(c))[..., 2] / 100


def color_is_dark(c):
    return lightness(c) <= 0.5


def contrast_with(fg, bg, ratio=4.5):
    """Lightens/darkens fg to contrast with bg by the given WCAG ratio. 4.5:1 is good for most text."""

    fg_hsl = to_hsluv(to_rgb(fg))
    bg_l = lightness(bg)

    # ratio is (L1 + 0.05) / (L2 + 0.05)
    # solving for L2, we get L2 = (1 + 20L1 - r) / 20r
    # solving for L1, we get L1 = (20 * r * L2 + r - 1) / 20
    r = ratio
    if color_is_dark(bg):
        # text will be L1
        l2 = bg_l
        l1 = (20 * r * l2 + r - 1) / 20
        new_l = l1
    else:
        l1 = bg_l
        l2 = (1 + 20 * l1 - r) / (20 * r)
        new_l = l2

    fg_hsl[2] = np.clip(new_l * 100, 0, 100)

    return np.array(hsluv.hsluv_to_rgb(fg_hsl))
