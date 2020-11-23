import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


def custom_colormap(cmap_name: str, img_data: np.uint8):
    cmap = plt.get_cmap(cmap_name)
    sm = plt.cm.ScalarMappable(cmap=cmap)
    color_range = sm.to_rgba(np.linspace(0, 1, 256))[:, 0:3]
    color_range = (color_range*255).astype(np.uint8)
    channels = [cv.LUT(img_data, color_range[:, i]) for i in range(3)]
    return np.dstack(channels)


def float_range(start: float or int, end: float or int, step: float):
    i = len(str(str(step)[str(step).index(".") + 1:]))
    while round(start, i) < round(end, i):
        yield float(start)
        start = round(step + start, i)
