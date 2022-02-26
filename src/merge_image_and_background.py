import numpy as np


def merge_image_and_background(wb_image, clear_background):
    return np.minimum(np.dstack((wb_image, wb_image, wb_image)), clear_background)
