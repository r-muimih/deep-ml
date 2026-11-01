import numpy as np
from collections import Counter

def descriptive_statistics(data) -> dict:
    """
    Calculate descriptive statistics for a dataset.
    
    Args:
        data: list or NumPy array of numerical values
    
    Returns:
        dict containing mean, median, mode, variance, standard_deviation,
        25th/50th/75th percentiles, and interquartile_range
    """
    arr = np.array(data, dtype=float)

    mean = np.mean(arr)
    median = np.median(arr)

    # Mode: most frequent value; ties broken by smallest value (Counter.most_common
    # order isn't guaranteed on ties, so resolve explicitly)
    counts = Counter(arr.tolist())
    max_freq = max(counts.values())
    mode = min(v for v, c in counts.items() if c == max_freq)

    variance = np.var(arr)  # population variance (ddof=0, divides by N)
    std_dev = np.sqrt(variance)

    q25 = np.percentile(arr, 25)
    q50 = np.percentile(arr, 50)
    q75 = np.percentile(arr, 75)
    iqr = q75 - q25

    return {
        "mean": float(mean),
        "median": float(median),
        "mode": float(mode),
        "variance": float(variance),
        "standard_deviation": float(std_dev),
        "25th_percentile": float(q25),
        "50th_percentile": float(q50),
        "75th_percentile": float(q75),
        "interquartile_range": float(iqr),
    }