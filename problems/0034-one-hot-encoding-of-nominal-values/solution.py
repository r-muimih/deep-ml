import numpy as np

def to_categorical(x, n_col=None):
    """
    One-hot encode an array of integer labels.

    Args:
        x: 1D array-like of integer labels in {0, ..., n_col - 1}
        n_col: number of categories (default: max(x) + 1)

    Returns:
        Array of shape (len(x), n_col) with a single 1 per row.
    """
    x = np.asarray(x, dtype=int)
    if x.size and x.min() < 0:
        raise ValueError("labels must be non-negative integers")

    if n_col is None:
        n_col = int(np.max(x)) + 1
    if x.size and x.max() >= n_col:
        raise ValueError("n_col must be greater than the largest label")

    one_hot = np.zeros((x.shape[0], n_col))
    one_hot[np.arange(x.shape[0]), x] = 1
    return one_hot