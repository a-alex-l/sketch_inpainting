import cv2
import numpy as np
from get_clear_background import get_background


def erase_shadow(image):
    shadow_background = get_background(image)
    shadow = cv2.GaussianBlur(shadow_background, (9, 9), cv2.BORDER_REFLECT)
    ink_prob = (np.abs(image.astype(float) - shadow).astype(float) / 255)
    ink_prob /= ink_prob.max()
    new_image = (1 - ink_prob) * (image.astype(float) - shadow + shadow.mean()) + ink_prob * image
    new_image[new_image < 0] = 0
    new_image[new_image > 255] = 255
    return new_image.astype(np.uint8)
