def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization with MSE loss.

    ...
    Returns:
        Optimized weights at full float precision.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)
    w = np.asarray(weights, dtype=float).copy()
    m = X.shape[0]

    if method == 'batch':
        b = m
    elif method == 'stochastic':
        b = 1
    elif method == 'mini_batch':
        if batch_size < 1:
            raise ValueError("batch_size must be >= 1")
        b = int(batch_size)
    else:
        raise ValueError(f"unknown method: {method!r}")

    for _ in range(n_epochs):
        for start in range(0, m, b):
            Xb = X[start:start + b]
            yb = y[start:start + b]
            grad = (2.0 / len(yb)) * Xb.T @ (Xb @ w - yb)
            w = w - learning_rate * grad

    return w + 0.0   # <-- was: np.round(w, 4) + 0.0