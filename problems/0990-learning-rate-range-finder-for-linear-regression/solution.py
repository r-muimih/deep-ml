import numpy as np


def lr_range_finder(X, y, w0, a, b, n_steps, decimals=4):
    """
    Sweep learning rate from 10**a to 10**b over n_steps full-batch GD updates
    on a linear regression model (no bias). Return the list of MSE losses after
    each update (rounded to `decimals`; pass decimals=None for the raw values).
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)
    w = np.asarray(w0, dtype=float).copy()          # do not modify the caller's w0
    n = X.shape[0]

    losses = []
    with np.errstate(over="ignore", invalid="ignore"):   # diverging runs may overflow to inf/nan
        for k in range(n_steps):
            exponent = a if n_steps == 1 else a + (b - a) * k / (n_steps - 1)
            lr = 10.0 ** exponent

            grad = (2.0 / n) * X.T @ (X @ w - y)         # (2/n) X^T (Xw - y)
            w = w - lr * grad                            # update with this step's lr

            errors = X @ w - y
            losses.append(float(np.mean(errors ** 2)))   # loss AFTER the update

    if decimals is not None:
        losses = [round(v, decimals) if np.isfinite(v) else v for v in losses]
    return losses


def suggest_lr(a, b, n_steps, losses):
    """Two common heuristics: steepest downhill slope, and 1/10 of the min-loss LR."""
    log_lr = np.array([a if n_steps == 1 else a + (b - a) * k / (n_steps - 1)
                       for k in range(n_steps)])
    losses = np.asarray(losses, dtype=float)
    finite = np.isfinite(losses)

    i_min = int(np.argmin(np.where(finite, losses, np.inf)))
    slopes = np.gradient(np.where(finite, losses, np.nan), log_lr)   # d loss / d log10(lr)
    i_steep = int(np.nanargmin(slopes[: i_min + 1]))                 # most negative slope before the minimum

    return {"steepest_lr": 10.0 ** log_lr[i_steep],
            "min_loss_lr": 10.0 ** log_lr[i_min],
            "min_loss_lr_over_10": 10.0 ** log_lr[i_min] / 10}


