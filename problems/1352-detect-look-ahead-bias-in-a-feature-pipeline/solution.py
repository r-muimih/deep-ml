import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


def causal_zscore(x: np.ndarray, window: int) -> np.ndarray:
    """Rolling z-score using only the trailing `window` values at each point.

    Args:
        x (np.ndarray): 1-D input series.
        window (int): lookback length, inclusive of the current point.

    Returns:
        np.ndarray: same length as x; the first window-1 entries are np.nan.
    """
    x = np.asarray(x, dtype=float).ravel()
    if window < 1:
        raise ValueError("window must be a positive integer")

    out = np.full(x.shape[0], np.nan)
    if x.shape[0] < window:
        return out                                   # no full window anywhere

    windows = sliding_window_view(x, window)         # row i = x[i : i + window]
    mu = windows.mean(axis=1)
    sd = windows.std(axis=1)                         # population std (ddof=0)
    current = x[window - 1:]                         # x_t for t = window-1 .. n-1

    safe = np.where(sd == 0, 1.0, sd)                # constant window: avoid 0/0
    out[window - 1:] = np.where(sd == 0, 0.0, (current - mu) / safe)
    return out


def has_lookahead(feature_fn, x: np.ndarray) -> bool:
    """Return True if feature_fn uses information from the future."""
    x = np.asarray(x, dtype=float)
    base = np.asarray(feature_fn(x.copy()), dtype=float)    # copy: never mutate the caller's x

    perturbed = x.copy()
    perturbed[-1] += 1000.0                                  # change ONLY the last value
    new = np.asarray(feature_fn(perturbed), dtype=float)

    return not np.allclose(base[:-1], new[:-1], equal_nan=True)