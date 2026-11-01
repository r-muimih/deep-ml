import numpy as np

def stratified_train_test_split(X, y, test_size, random_seed=None):
    """
    Split data into train and test sets while maintaining class proportions.

    Args:
        X: Feature matrix of shape (n_samples, n_features)
        y: Label vector of shape (n_samples,)
        test_size: Proportion of data for test set (0 < test_size < 1)
        random_seed: Random seed for reproducibility

    Returns:
        X_train, X_test, y_train, y_test
    """
    X, y = np.asarray(X), np.asarray(y)
    if len(X) != len(y):
        raise ValueError("X and y must have the same number of samples")
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1")

    np.random.seed(random_seed)

    train_idx, test_idx = [], []
    for c in np.unique(y):                       # each class (sorted order)
        idx = np.where(y == c)[0]                # step 1: I_c
        np.random.shuffle(idx)                   # step 3: shuffle I_c
        n_test = int(len(idx) * test_size)       # step 2: floor(|I_c| * test_size)
        test_idx.extend(idx[:n_test])
        train_idx.extend(idx[n_test:])

    train_idx, test_idx = np.array(train_idx), np.array(test_idx)
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
