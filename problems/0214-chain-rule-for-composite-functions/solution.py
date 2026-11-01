import numpy as np

# Each entry: (function, derivative)
_FUNCS = {
    'square': (lambda u: u ** 2, lambda u: 2 * u),
    'sin':    (np.sin,           np.cos),
    'exp':    (np.exp,           np.exp),
    'log':    (np.log,           lambda u: 1 / u),
}

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    """
    Compute derivative of composite functions using chain rule.

    Args:
        functions: List of function names (applied right to left)
                   Available: 'square', 'sin', 'exp', 'log'
        x: Point at which to evaluate derivative

    Returns:
        Derivative value at x

    Example:
        ['sin', 'square'] represents sin(x²)
        ['exp', 'sin', 'square'] represents exp(sin(x²))
    """
    for name in functions:
        if name not in _FUNCS:
            raise ValueError(f"Unknown function '{name}'. Available: {list(_FUNCS)}")

    # The list is outermost-first, so reverse it to get f1 (innermost) first
    ordered = list(reversed(functions))

    # Forward pass: u0 = x, u_i = f_i(u_{i-1})
    inputs = []          # inputs[i] = u_{i-1}, the point where f_i' is evaluated
    u = float(x)
    for name in ordered:
        inputs.append(u)
        u = _FUNCS[name][0](u)

    # Backward pass: dh/dx = product of f_i'(u_{i-1})
    grad = 1.0
    for name, u_in in zip(ordered, inputs):
        grad *= _FUNCS[name][1](u_in)

    return float(grad)

