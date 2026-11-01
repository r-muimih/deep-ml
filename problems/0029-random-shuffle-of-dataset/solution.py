import numpy as np

def shuffle_data(X, y, seed=None):
    X, y = np.asarray(X), np.asarray(y)
    if len(X) != len(y):
        raise ValueError("X and y must have the same number of samples")
    rng = np.random.RandomState(seed)
    idx = rng.permutation(len(X))
    return X[idx], y[idx]