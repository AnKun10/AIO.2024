import numpy as np


def compute_mean(X):
    return np.mean(X)


def compute_median(X):
    size = len(X)
    X = np.sort(X)
    if (size % 2) == 0:
        return (X[int((size - 1) / 2)] + X[int(size / 2)]) / 2
    else:
        return X[int((size - 1) / 2)]


def compute_std(X):
    mean = compute_mean(X)
    size = len(X)
    var = np.sum((X - mean) ** 2)/size
    return np.sqrt(var)


def compute_correlation_coefficient(X, Y):
    N = X.shape[0]
    numerator = N*(X@Y)-np.sum(X)*np.sum(Y)
    denominator = np.sqrt(N*np.sum(X**2)-np.sum(X)**2)*np.sqrt(N*np.sum(Y**2)-np.sum(Y)**2)
    return np.round(numerator / denominator, 2)
