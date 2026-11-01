import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.

    Returns [train, validation, test].
    """
    if train_frac < 0 or validation_frac < 0 or train_frac + validation_frac > 1:
        raise ValueError("fractions must be non-negative and sum to at most 1")

    rng = np.random.default_rng(seed)
    shuffled = data[rng.permutation(len(data))]   # shuffles rows, returns a copy

    n = len(shuffled)
    train_end = int(n * train_frac)
    val_end = train_end + int(n * validation_frac)

    return [shuffled[:train_end], shuffled[train_end:val_end], shuffled[val_end:]]