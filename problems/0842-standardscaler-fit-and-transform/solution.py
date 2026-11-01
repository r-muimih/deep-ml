import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    X_train = np.asarray(X_train, dtype=float)
    X_test = np.asarray(X_test, dtype=float)

    # fit: statistics from the training data only, per column
    mean = X_train.mean(axis=0)
    std = X_train.std(axis=0)                  # population std (ddof=0)
    std = np.where(std == 0, 1.0, std)         # constant feature safeguard

    # transform: apply the TRAIN statistics to the test data
    return (X_test - mean) / std