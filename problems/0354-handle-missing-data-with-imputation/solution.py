import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.

    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'

    Returns:
        2D numpy array with missing values imputed
    """
    if strategy not in ('mean', 'median', 'mode'):
        raise ValueError("strategy must be 'mean', 'median' or 'mode'")

    result = np.array(data, dtype=float)          # copy: the input is not modified
    for j in range(result.shape[1]):
        col = result[:, j]                        # a view into `result`
        mask = np.isnan(col)
        observed = col[~mask]
        if observed.size == 0:                    # nothing to learn from: leave as NaN
            continue

        if strategy == 'mean':
            fill = observed.mean()
        elif strategy == 'median':
            fill = np.median(observed)
        else:                                     # mode
            values, counts = np.unique(observed, return_counts=True)
            fill = values[np.argmax(counts)]      # ties -> smallest value

        col[mask] = fill
    return result