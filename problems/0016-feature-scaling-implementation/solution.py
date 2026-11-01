import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    """
    Scale each column (feature) of `data` two ways.

    Returns:
        standardized_data: (x - mean) / std, per column (mean 0, std 1)
        normalized_data:   (x - min) / (max - min), per column, in [0, 1]
    """
    data = np.asarray(data, dtype=float)

    mean = data.mean(axis=0)
    std = data.std(axis=0)                       # population std (ddof=0)
    data_min = data.min(axis=0)
    data_range = data.max(axis=0) - data_min

    # constant columns: avoid dividing by zero (result becomes all 0)
    safe_std = np.where(std == 0, 1.0, std)
    safe_range = np.where(data_range == 0, 1.0, data_range)

    standardized_data = (data - mean) / safe_std
    normalized_data = (data - data_min) / safe_range
    return standardized_data, normalized_data