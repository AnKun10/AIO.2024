import numpy as np


def cs(x, y):
    cos_sim = (x @ y) / (np.linalg.norm(x) * np.linalg.norm(y))
    return cos_sim