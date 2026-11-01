import numpy as np


def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray,
               learning_rate: float, n_iter: int, decimals=4) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list
    (rounded to `decimals`; pass decimals=None for the unrounded values).
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)
    w = np.asarray(weights, dtype=float).copy()
    n = X.shape[0]

    for t in range(n_iter):
        i = t % n                                  # i_t = t mod n
        xi, yi = X[i], y[i]
        w = w - 2.0 * learning_rate * (xi @ w - yi) * xi   # w - eta * grad of l_i

    if decimals is not None:
        w = np.round(w, decimals) + 0.0            # "+ 0.0" removes any -0.0
    return w.tolist()


# Tests (values from the worked examples)
X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
y = np.array([2, 3, 4, 5])
w0 = np.zeros(2)

