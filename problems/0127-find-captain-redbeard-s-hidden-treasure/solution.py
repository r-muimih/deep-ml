def find_treasure(start_x: float) -> float:
    """
    Find the x-coordinate where f(x) = x^4 - 3x^3 + 2 is minimized.

    Returns:
        float: The x-coordinate of the minimum point.
    """
    def grad(x):
        return 4 * x**3 - 9 * x**2   # f'(x) = x^2 (4x - 9)

    # f' < 0 for all x < 2.25 (x != 0) and f' > 0 for x > 2.25,
    # so the sign change at the minimizer can be bracketed and bisected.
    lo = min(float(start_x), 0.0) - 1.0   # always <= -1, so grad(lo) < 0
    hi = max(float(start_x), 3.0) + 1.0   # always >= 4,  so grad(hi) > 0

    for _ in range(200):
        mid = (lo + hi) / 2
        if grad(mid) < 0:
            lo = mid
        else:
            hi = mid

    return (lo + hi) / 2