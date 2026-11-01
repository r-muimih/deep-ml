import numpy as np


def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.

    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation

    Returns:
        tuple: (numerical_grad, relative_error)
    """
    x = np.array(x, dtype=float)                        # private float copy; caller's x is untouched
    analytical_grad = np.asarray(analytical_grad, dtype=float)

    numerical_grad = np.zeros_like(x)
    flat_x = x.reshape(-1)                              # views, so any array shape works
    flat_g = numerical_grad.reshape(-1)

    for i in range(flat_x.size):
        original = flat_x[i]

        flat_x[i] = original + epsilon
        f_plus = f(x)                                   # f(x + eps * e_i)

        flat_x[i] = original - epsilon
        f_minus = f(x)                                  # f(x - eps * e_i)

        flat_x[i] = original                            # restore before the next coordinate
        flat_g[i] = (f_plus - f_minus) / (2 * epsilon)

    diff = np.linalg.norm((numerical_grad - analytical_grad).reshape(-1))
    denom = (np.linalg.norm(numerical_grad.reshape(-1))
             + np.linalg.norm(analytical_grad.reshape(-1)))

    # If both gradients are exactly zero they agree perfectly
    relative_error = 0.0 if denom == 0 else float(diff / denom)

    return numerical_grad, relative_error


def interpret(relative_error):
    """Map a relative error to the verdicts in the table above."""
    if relative_error < 1e-7:
        return "likely correct"
    if relative_error < 1e-3:
        return "investigate"
    return "likely a bug"

