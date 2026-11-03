import numpy as np


def learning_curve(X_train, y_train, X_val, y_val, train_sizes, degree,
                    bias_threshold=0.5, variance_threshold=0.5):
    """
    Generate a learning curve and diagnose bias vs variance.

    Args:
        X_train: training features, shape (n_train,) or (n_train, 1)
        y_train: training targets, shape (n_train,)
        X_val:   validation features, shape (n_val,) or (n_val, 1)
        y_val:   validation targets, shape (n_val,)
        train_sizes: iterable of training-set sizes to evaluate
        degree: degree of the polynomial model to fit
        bias_threshold: final training error above which the model is high-bias
        variance_threshold: train/val gap above which the model is high-variance

    Returns:
        dict with 'train_errors', 'val_errors', 'diagnosis'
        ('high_bias', 'high_variance', or 'good_fit')
    """
    X_train = np.asarray(X_train).ravel()
    y_train = np.asarray(y_train).ravel()
    X_val = np.asarray(X_val).ravel()
    y_val = np.asarray(y_val).ravel()

    train_errors = []
    val_errors = []

    for size in train_sizes:
        if size < degree + 1:
            train_errors.append(float('nan'))
            val_errors.append(float('nan'))
            continue

        X_sub = X_train[:size]
        y_sub = y_train[:size]

        coeffs = np.polyfit(X_sub, y_sub, degree)
        model = np.poly1d(coeffs)

        train_mse = np.mean((y_sub - model(X_sub)) ** 2)
        val_mse = np.mean((y_val - model(X_val)) ** 2)

        # Round and cast to native float: keeps output JSON/repr-friendly
        # and avoids np.float64(...) showing up in comparisons/printing.
        train_errors.append(round(float(train_mse), 4))
        val_errors.append(round(float(val_mse), 4))

    final_train = next((e for e in reversed(train_errors) if not np.isnan(e)), None)
    final_val = next((e for e in reversed(val_errors) if not np.isnan(e)), None)

    if final_train is None or final_val is None:
        diagnosis = "insufficient_data"
    else:
        gap = final_val - final_train

        if final_train > bias_threshold:
            # Model can't even fit the training data well -> underfitting,
            # regardless of how the validation error looks.
            diagnosis = "high_bias"
        elif gap > variance_threshold:
            diagnosis = "high_variance"
        else:
            diagnosis = "good_fit"

    return {
        "train_errors": train_errors,
        "val_errors": val_errors,
        "diagnosis": diagnosis,
    }