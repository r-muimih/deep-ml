def poly_term_derivative(c: float, x: float, n: float) -> float:
    """Derivative of c * x**n evaluated at x, rounded to 4 decimals."""
    # Edge case: n = 0 -> the term is constant, derivative is 0
    if n == 0:
        return 0.0

    # Cases where the derivative is undefined / not real
    if x == 0 and n < 1:
        raise ValueError("derivative undefined at x = 0 for n < 1")
    if x < 0 and n != int(n):
        raise ValueError("x**n is not real for negative x and non-integer n")

    # Power rule: d/dx (c x^n) = c * n * x^(n-1)
    # "+ 0.0" turns any -0.0 into 0.0
    return round(c * n * x ** (n - 1), 4) + 0.0
