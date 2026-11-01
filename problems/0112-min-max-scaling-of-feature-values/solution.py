def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].

    Args:
        x: A list of numerical values

    Returns:
        A new list with values normalized to [0, 1]
    """
    if not x:
        return []

    x_min, x_max = min(x), max(x)
    if x_max == x_min:                      # special case: identical values
        return [0.0] * len(x)

    span = x_max - x_min
    return [round((v - x_min) / span, 4) for v in x]