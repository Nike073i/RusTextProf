import numpy as np


epsilon = 1e-8

def triangular_weights(distances, max_distance=None):
    if max_distance is None:
        max_distance = np.max(distances)
    if max_distance < epsilon:
        return np.ones_like(distances)
    return np.maximum(1 - distances / max_distance, 0)

def gaussian_weights(distances, sigma=1.0):
    return np.exp(-(distances**2) / (2 * sigma**2))

def quadratic_weights(distances):
    return 1 / (distances**2 + epsilon)
