import numpy as np


def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]
