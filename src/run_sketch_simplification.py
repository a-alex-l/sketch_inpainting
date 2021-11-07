import cv2
import numpy as np


def run_sketch_simplification(image):
    # TODO
    mask = np.ones(image.shape[:2], dtype=np.uint8) * 255
    cv2.circle(mask, (100, 100), 50, (0, 0, 0), thickness=6)
    return mask
