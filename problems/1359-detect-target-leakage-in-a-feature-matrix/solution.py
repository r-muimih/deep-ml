import numpy as np


def find_leaky_features(X: np.ndarray, y: np.ndarray, threshold: float) -> list:
    """Column indices whose |correlation| with y is >= threshold.

    Args:
        X (np.ndarray): (n, p) feature matrix.
        y (np.ndarray): (n,) target.
        threshold (float): absolute-correlation cutoff.

    Returns:
        list[int]: ascending column indices.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).ravel()
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    if X.shape[0] != y.shape[0]:
        raise ValueError("X and y must have the same number of rows")

    yc = y - y.mean()
    y_norm = np.sqrt(np.sum(yc ** 2))
    y_const = np.ptp(y) == 0

    flagged = []
    for j in range(X.shape[1]):
        col = X[:, j]
        if y_const or np.ptp(col) == 0:            # zero variance: correlation undefined -> 0
            continue
        cc = col - col.mean()
        corr = float(cc @ yc / (np.sqrt(np.sum(cc ** 2)) * y_norm))
        if abs(corr) >= threshold - 1e-12:         # tolerance for float rounding
            flagged.append(j)
    return flagged


def is_affine_function_of(col: np.ndarray, y: np.ndarray) -> bool:
    """True when col == a + b * y to within a residual of 1e-9."""
    col = np.asarray(col, dtype=float).ravel()
    y = np.asarray(y, dtype=float).ravel()
    if col.shape != y.shape:
        raise ValueError("col and y must have the same length")

    A = np.column_stack([np.ones_like(y), y])             # design matrix [1, y]
    coef, *_ = np.linalg.lstsq(A, col, rcond=None)         # least-squares a, b
    rss = float(np.sum((col - A @ coef) ** 2))            # residual sum of squares
    return rss < 1e-9