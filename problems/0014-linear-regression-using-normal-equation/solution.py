import numpy as np


def linear_regression_normal_equation(
    X: list[list[float]],
    y: list[float],
    add_intercept: bool = False,
    decimals: int = 4,
) -> list[float]:
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)

    if X.ndim == 1:                      # single raw feature
        X = X.reshape(-1, 1)
    if add_intercept:                    # prepend a column of ones
        X = np.column_stack([np.ones(X.shape[0]), X])

    try:
        # Solve X^T X theta = X^T y (more stable than forming the inverse)
        theta = np.linalg.solve(X.T @ X, X.T @ y)
    except np.linalg.LinAlgError:
        # Singular X^T X: fall back to the pseudoinverse (min-norm solution)
        theta = np.linalg.pinv(X) @ y

    # Round, and "+ 0.0" turns any -0.0 into 0.0
    return [float(t) + 0.0 for t in np.round(theta, decimals)]