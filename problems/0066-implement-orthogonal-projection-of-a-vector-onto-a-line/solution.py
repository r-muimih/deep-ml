import math


def dot(a, b):
    """Dot product of two equal-length vectors."""
    if len(a) != len(b):
        raise ValueError("vectors must have the same length")
    return sum(x * y for x, y in zip(a, b))


def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
    :param L: The line vector defining the direction of projection
    :return: List representing the projection of v onto L
    """
    LL = dot(L, L)
    if LL == 0:
        raise ValueError("L must be a non-zero vector")
    scale = dot(v, L) / LL
    return [scale * c for c in L]


def scalar_projection(v, L):
    """Signed length of the projection of v onto L (v . L_hat)."""
    norm = math.sqrt(dot(L, L))
    if norm == 0:
        raise ValueError("L must be a non-zero vector")
    return dot(v, L) / norm


# Tests (values from the worked examples)
def close(a, b, tol=1e-12):
    return all(abs(x - y) < tol for x, y in zip(a, b))