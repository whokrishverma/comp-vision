import numpy as np

COLOR_MAP = {

    "red": (
        np.array([0, 120, 70]),
        np.array([10, 255, 255]),
        np.array([170, 120, 70]),
        np.array([179, 255, 255])
    ),

    "green": (
        np.array([35, 70, 70]),
        np.array([85, 255, 255])
    ),

    "blue": (
        np.array([100, 150, 70]),
        np.array([130, 255, 255])
    ),

    "yellow": (
        np.array([20, 100, 100]),
        np.array([35, 255, 255])
    ),

    "orange": (
        np.array([10, 100, 100]),
        np.array([20, 255, 255])
    ),

    "purple": (
        np.array([130, 80, 80]),
        np.array([160, 255, 255])
    ),

    "cyan": (
        np.array([80, 100, 100]),
        np.array([100, 255, 255])
    ),

    "white": (
        np.array([0, 0, 180]),
        np.array([179, 40, 255])
    ),

    "black": (
        np.array([0, 0, 0]),
        np.array([179, 255, 40])
    )
}


def get_limits(color):

    color = color.lower()

    if color not in COLOR_MAP:
        raise ValueError(f"'{color}' is not a supported color.")

    return COLOR_MAP[color]