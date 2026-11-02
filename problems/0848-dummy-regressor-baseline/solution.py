import numpy as np

def dummy_regressor(y_train, n_test, strategy='mean', constant=None, quantile=None):
    """
    Baseline regressor that predicts a constant value derived from y_train.

    Args:
        y_train: 1D array-like of training target values.
        n_test: number of test predictions to return (int >= 0).
        strategy: one of 'mean', 'median', 'quantile', 'constant'.
        constant: required when strategy='constant'.
        quantile: required when strategy='quantile', must be in [0, 1].

    Returns:
        List[float] of length n_test, all equal to the chosen summary value.
    """
    if n_test < 0:
        raise ValueError("n_test must be non-negative")

    if strategy == 'constant':
        if constant is None:
            raise ValueError("strategy='constant' requires a constant value")
        return [float(constant)] * n_test
    if strategy not in ('mean', 'median', 'quantile'):
        raise ValueError(f"unknown strategy: {strategy!r}")

    y = np.asarray(y_train, dtype=float).ravel()
    if y.size == 0:
        raise ValueError("y_train must not be empty")

    if strategy == 'mean':
        value = y.mean()
    elif strategy == 'median':
        value = np.median(y)
    else:  # quantile
        if quantile is None or not 0 <= quantile <= 1:
            raise ValueError("strategy='quantile' requires quantile in [0, 1]")
        value = np.quantile(y, quantile)

    return [float(value)] * n_test
