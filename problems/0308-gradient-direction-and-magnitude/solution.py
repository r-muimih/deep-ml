import math


def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.

    Args:
        gradient: A list representing the gradient vector

    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    if len(gradient) == 0:
        raise ValueError("gradient must be non-empty")

    g = [float(v) for v in gradient]
    magnitude = math.hypot(*g)          # L2 norm, safe against overflow

    # Edge case: zero gradient -> no well-defined direction
    if magnitude == 0.0:
        zeros = [0.0] * len(g)
        return {
            "magnitude": 0.0,
            "direction": zeros,
            "descent_direction": list(zeros),
        }

    direction = [v / magnitude for v in g]
    return {
        "magnitude": round(magnitude, 4),
        # "+ 0.0" turns any -0.0 into 0.0
        "direction": [round(v, 4) + 0.0 for v in direction],
        "descent_direction": [round(-v, 4) + 0.0 for v in direction],
    }


def clip_by_norm(g: list, max_norm: float) -> list:
    """Rescale g so that its norm is at most max_norm (direction unchanged)."""
    norm = math.hypot(*g)
    scale = min(1.0, max_norm / norm) if norm > 0 else 1.0
    return [round(v * scale, 4) + 0.0 for v in g]

