import cv2
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

BINS = 256


def get_ink_border(image_data):
    border = 0
    border_score = image_data.size ** 2
    x = np.arange(BINS)
    indexes, counts = np.unique(image_data.reshape((-1,)), return_counts=True)
    cnts = np.zeros((BINS,))
    cnts[indexes] = counts
    for i in range(1, BINS):
        if cnts[:i].sum() > image_data.size * 0.001 and cnts[i:].sum() > image_data.size * 0.001:
            mu_ink = (x * cnts)[:i].sum() / cnts[:i].sum()
            mu_paper = (x * cnts)[i:].sum() / cnts[i:].sum()
            score = np.sum((ss.norm.pdf(x[:i], mu_ink, (i - mu_ink) / 2.5) * cnts[:i].sum() - cnts[:i]) ** 2) \
                    / (cnts[:i] ** 2).sum() + \
                    np.sum((ss.norm.pdf(x[i:], mu_paper, (mu_paper - i) / 2.5) * cnts[i:].sum() - cnts[i:]) ** 2) \
                    / (cnts[i:] ** 2).sum()
            if score < border_score:
                border = i
                border_score = score
    mu_paper = (x * cnts)[border:].sum() / cnts[border:].sum()
    plt.plot(cnts)
    mu_ink = (x * cnts)[:border].sum() / cnts[:border].sum()
    plt.plot(x, ss.norm.pdf(x, mu_ink, (border - mu_ink) / 2.5) * cnts[:border].sum())
    plt.plot(x, ss.norm.pdf(x, mu_paper, (mu_paper - border) / 2.5) * cnts[border:].sum())
    plt.axvline(x=border + (mu_paper - border) / 2, c='red')
    plt.show()
    return border + (mu_paper - border) / 2


def get_background(image):
    image_data = image.min(axis=-1)
    border = get_ink_border(image_data)
    mask = ((image_data < border) * 255).astype(np.uint8)
    kernel = np.zeros((9, 9), dtype=np.uint8)
    cv2.circle(kernel, (4, 4), 4, (255, 255, 255), thickness=-1)
    mask_dilate = cv2.dilate(mask, kernel)
    return cv2.inpaint(image, mask_dilate, 10, None)


def get_clear_background(image):
    new_image = get_background(image)
    return new_image
