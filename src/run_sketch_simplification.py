import numpy as np
import torch
import cv2
from models.model_simplification import model_simplification


def run_sketch_simplification(image):
    model = model_simplification
    model.load_state_dict(torch.load("../models/model_gan.pth"))
    model.eval()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    p0 = (-(gray_image.shape[0] % 8)) % 8
    if p0 > 0:
        gray_image = cv2.copyMakeBorder(gray_image, 0, p0, 0, 0, cv2.BORDER_CONSTANT)
    p1 = (-(gray_image.shape[1] % 8)) % 8
    if p1 > 0:
        gray_image = cv2.copyMakeBorder(gray_image, 0, 0, 0, p1, cv2.BORDER_CONSTANT)
    data = torch.FloatTensor((gray_image - np.mean(gray_image)) / np.std(gray_image))
    data = data.unsqueeze(0).unsqueeze(0)
    simplified_data = model.forward(data)
    simplified_image = (simplified_data.detach().numpy()[0, 0, :, :] * 255).astype(int)
    simplified_image[simplified_image > 255] = 255
    simplified_image[simplified_image < 0] = 0
    if p0:
        simplified_image = simplified_image[0:-p0, :]
    if p1:
        simplified_image = simplified_image[:, 0:-p1]
    return simplified_image.astype(np.uint8)
