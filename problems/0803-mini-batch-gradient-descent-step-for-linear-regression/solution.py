import numpy as np


def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float,
                       batch_indices: list, lr: float, decimals=4) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    (Rounded to `decimals`; pass decimals=None for the unrounded values.)
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)
    w = np.asarray(weights, dtype=float).reshape(-1)

    idx = np.asarray(batch_indices, dtype=int)
    if idx.size == 0:
        raise ValueError("batch_indices must be non-empty")

    Xb, yb = X[idx], y[idx]                     # the mini-batch
    B = len(yb)

    errors = Xb @ w + bias - yb                 # e_i = x_i^T w + b - y_i
    grad_w = (2.0 / B) * (Xb.T @ errors)        # (2/B) X_B^T e
    grad_b = (2.0 / B) * errors.sum()           # (2/B) sum e_i

    # Both gradients were computed from the old w and b
    new_params = np.concatenate([w - lr * grad_w, [bias - lr * grad_b]])

    if decimals is not None:
        new_params = np.round(new_params, decimals) + 0.0   # "+ 0.0" removes any -0.0
    return new_params

