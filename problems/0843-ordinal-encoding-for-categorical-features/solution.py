import numpy as np

def ordinal_encode(X, categories):
    """
    Encode categorical features as integer codes using a provided ordering.

    Args:
        X: 2D list/array of shape (n_samples, n_features) with string values.
        categories: list of length n_features; categories[j] is an ordered
                    list of valid categories for column j.

    Returns:
        np.ndarray of shape (n_samples, n_features), dtype int.
        Unknown categories are encoded as -1.
    """
    n_samples = len(X)
    n_features = len(categories)
    Z = np.full((n_samples, n_features), -1, dtype=int)      # unknown by default

    for j, cats in enumerate(categories):
        mapping = {c: k for k, c in enumerate(cats)}          # rank lookup for column j
        for i in range(n_samples):
            Z[i, j] = mapping.get(X[i][j], -1)
    return Z
