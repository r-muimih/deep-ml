import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.

    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i

    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    f = np.array(f_coeffs, dtype=float)
    g = np.array(g_coeffs, dtype=float)

    def derivative(p):
        # d/dx of sum(p[i] * x^i) = sum(i * p[i] * x^(i-1))
        if len(p) <= 1:
            return np.array([0.0])
        return p[1:] * np.arange(1, len(p))

    f_prime = derivative(f)
    g_prime = derivative(g)

    # Product rule: f'g + fg'
    # np.convolve multiplies polynomials stored lowest-degree first
    term1 = np.convolve(f_prime, g)
    term2 = np.convolve(f, g_prime)

    # Pad to equal length and add
    n = max(len(term1), len(term2))
    result = np.zeros(n)
    result[:len(term1)] += term1
    result[:len(term2)] += term2

    result = np.round(result, 4)

    # Strip trailing zeros
    while len(result) > 1 and result[-1] == 0:
        result = result[:-1]

    # Zero polynomial
    if len(result) == 0 or np.all(result == 0):
        return [0.0]

    # Normalize -0.0 to 0.0
    return [float(c) + 0.0 for c in result]