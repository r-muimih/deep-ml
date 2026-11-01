import numpy as np

def convert_range(values: np.ndarray, c: float, d: float) -> np.ndarray:
    """
    Shift and scale values from their original range [min, max] to a target [c, d] range.
    """
    values = np.asarray(values, dtype=float)
    a, b = values.min(), values.max()          # range of the whole array

    if a == b:                                 # constant input: avoid division by zero
        return np.full_like(values, float(c))

    return c + (d - c) / (b - a) * (values - a)