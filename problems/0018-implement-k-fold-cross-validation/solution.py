import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.

    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)

    Returns:
        List of (train_indices, test_indices) tuples
    """
    if k < 2 or k > n_samples:
        raise ValueError("k must satisfy 2 <= k <= n_samples")

    indices = np.arange(n_samples)                  # step 1
    if shuffle:                                     # step 2
        np.random.shuffle(indices)

    base, extra = divmod(n_samples, k)              # step 3
    sizes = [base + 1 if i < extra else base for i in range(k)]

    folds, start = [], 0
    for size in sizes:
        folds.append(indices[start:start + size])
        start += size

    splits = []                                     # step 4
    for i in range(k):
        test_idx = folds[i]
        train_idx = np.concatenate([folds[j] for j in range(k) if j != i])
        splits.append((train_idx.tolist(), test_idx.tolist()))
    return splits                                   # step 5