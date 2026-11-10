import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.

    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative

    Returns:
        The derivative value f'(x)
    """
    g = np.polyval(g_coeffs, x)
    h = np.polyval(h_coeffs, x)

    # np.polyder returns [] for some constant inputs in older versions,
    # and polyval of an empty array gives 0, but guard explicitly anyway
    g_prime_coeffs = np.polyder(g_coeffs) if len(g_coeffs) > 1 else [0.0]
    h_prime_coeffs = np.polyder(h_coeffs) if len(h_coeffs) > 1 else [0.0]

    g_prime = np.polyval(g_prime_coeffs, x)
    h_prime = np.polyval(h_prime_coeffs, x)

    return float((g_prime * h - g * h_prime) / (h ** 2))