import numpy as np

def bias_variance_decomp(predictions, y_true):
    """
    Compute the empirical bias-variance decomposition from bootstrap predictions.

    Args:
        predictions: array-like of shape (B, M) - predictions from B models at M test points
        y_true: array-like of shape (M,) - true target values

    Returns:
        dict with keys 'bias_squared', 'variance', 'mse'
    """
    predictions = np.asarray(predictions, dtype=float)
    y_true = np.asarray(y_true, dtype=float)

    # Mean prediction at each test point, averaged across the B bootstrap models
    mean_prediction = predictions.mean(axis=0)  # shape (M,)

    # Squared bias at each test point, then averaged across test points
    bias_squared = np.mean((mean_prediction - y_true) ** 2)

    # Variance at each test point: average squared deviation of each model's
    # prediction from the mean prediction, then averaged across test points
    variance = np.mean((predictions - mean_prediction) ** 2)

    # MSE at each test point: average squared deviation of each model's
    # prediction from the true value, then averaged across test points
    mse = np.mean((predictions - y_true) ** 2)

    return {
        'bias_squared': float(bias_squared),
        'variance': float(variance),
        'mse': float(mse),
    }