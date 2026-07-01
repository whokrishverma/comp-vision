import numpy as np
import cv2

def get_limits(color):

    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]

    # Red wraps around the HSV hue scale
    if hue < 10:
        lower1 = np.array([0, 100, 100], dtype=np.uint8)
        upper1 = np.array([hue + 10, 255, 255], dtype=np.uint8)

        lower2 = np.array([180 - (10 - hue), 100, 100], dtype=np.uint8)
        upper2 = np.array([180, 255, 255], dtype=np.uint8)

        return (lower1, upper1), (lower2, upper2)

    lower = np.array([hue - 10, 100, 100], dtype=np.uint8)
    upper = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lower, upper