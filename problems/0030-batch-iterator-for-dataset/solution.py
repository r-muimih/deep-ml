import numpy as np
def batch_iterator(X, y=None, batch_size=64):
    if y is not None and len(X) != len(y):
        raise ValueError("X and y must have the same number of samples")
    if batch_size < 1:
        raise ValueError("batch_size must be a positive integer")

    n = len(X)
    for start in range(0, n, batch_size):
        end = start + batch_size
        if y is None:
            yield X[start:end]
        else:
            yield [X[start:end], y[start:end]]