import numpy as np
import torch
from models.model_simplification import model_simplification


def run_sketch_simplification(image):
    model = model_simplification.copy()
    model.load_state_dict(torch.load("../models/model_gan.pth"))
    model.eval()
    data = (image - np.mean(image)) / np.std(image)
    simplified_data = model.forward(data)
    simplified_image = (simplified_data * np.std(image)) + np.mean(image)
    return simplified_image
