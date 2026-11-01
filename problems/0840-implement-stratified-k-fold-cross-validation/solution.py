import numpy as np

def stratified_kfold_indices(y, n_splits):
    """
    Generate train/test indices for stratified K-fold cross-validation.

    Args:
        y: 1D array-like of integer class labels
        n_splits: number of folds

    Returns:
        A list of [train_indices, test_indices] pairs, one per fold.
    """
    y = np.asarray(y)
    n = len(y)
    if n_splits < 2:
        raise ValueError("n_splits must be at least 2")

    test_folds = [[] for _ in range(n_splits)]
    for c in np.unique(y):                               # step 1: group by class
        idx = np.where(y == c)[0]
        base, extra = divmod(len(idx), n_splits)         # step 2: k contiguous groups,
        start = 0                                        #   first `extra` get +1
        for i in range(n_splits):
            size = base + 1 if i < extra else base
            test_folds[i].extend(idx[start:start + size].tolist())
            start += size

    splits = []                                          # step 3: form folds
    for i in range(n_splits):
        test_idx = sorted(test_folds[i])                 # union over classes
        test_set = set(test_idx)
        train_idx = [j for j in range(n) if j not in test_set]   # complement
        splits.append([train_idx, test_idx])
    return splits