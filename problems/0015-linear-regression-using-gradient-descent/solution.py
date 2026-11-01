import numpy as np


def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations

    Returns:
        Learned weights as a 1D array of shape (n,), rounded to 4 decimals
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)

    m, n = X.shape
    y = y.reshape(-1, 1)          # Ensure y is a column vector
    theta = np.zeros((n, 1))      # Initialize weights to zeros

    for _ in range(iterations):
        predictions = X @ theta               # y_hat = X theta
        errors = predictions - y              # e = y_hat - y
        gradient = (X.T @ errors) / m         # g = (1/m) X^T e
        theta = theta - alpha * gradient      # theta = theta - alpha * g

    # "+ 0.0" turns any -0.0 into 0.0
    return np.round(theta.flatten(), 4) + 0.0
