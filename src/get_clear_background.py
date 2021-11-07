
import cv2
import numpy as np


def get_clear_background(image, wb_simplified):
    # TODO
    mask = 255 - wb_simplified
    kernel = np.zeros((9, 9), dtype=np.uint8)
    cv2.circle(kernel, (4, 4), 4, (255, 255, 255), thickness=-1)
    mask = cv2.dilate(mask, kernel)
    new_image = cv2.inpaint(image, mask, 10, None)
    return new_image
