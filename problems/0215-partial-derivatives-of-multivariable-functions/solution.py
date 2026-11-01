import math


def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
    """
    Compute partial derivatives of multivariable functions.

    Args:
        func_name: Function identifier
            'poly2d': f(x,y) = x²y + xy²
            'exp_sum': f(x,y) = e^(x+y)
            'product_sin': f(x,y) = x·sin(y)
            'poly3d': f(x,y,z) = x²y + yz²
            'squared_error': f(x,y) = (x-y)²
        point: Point (x, y) or (x, y, z) at which to evaluate

    Returns:
        Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point,
        rounded to 4 decimals
    """
    def unpack(k):
        if len(point) != k:
            raise ValueError(f"{func_name!r} needs {k} coordinates, got {len(point)}")
        return point

    if func_name == "poly2d":
        x, y = unpack(2)
        grad = (2 * x * y + y ** 2, x ** 2 + 2 * x * y)
    elif func_name == "exp_sum":
        x, y = unpack(2)
        e = math.exp(x + y)
        grad = (e, e)
    elif func_name == "product_sin":
        x, y = unpack(2)
        grad = (math.sin(y), x * math.cos(y))
    elif func_name == "poly3d":
        x, y, z = unpack(3)
        grad = (2 * x * y, x ** 2 + z ** 2, 2 * y * z)
    elif func_name == "squared_error":
        x, y = unpack(2)
        grad = (2 * (x - y), -2 * (x - y))
    else:
        raise ValueError(f"unknown function: {func_name!r}")

    # "+ 0.0" turns any -0.0 into 0.0
    return tuple(round(g, 4) + 0.0 for g in grad)

