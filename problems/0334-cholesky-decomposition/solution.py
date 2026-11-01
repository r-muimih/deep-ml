
import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix.

    Args:
        A: A symmetric positive-definite matrix (2D list or numpy array)

    Returns:
        L: Lower triangular matrix such that A = L @ L.T as a 2D list,
           or -1 if decomposition is not possible
    """
    A = np.array(A, dtype=float)

    # Must be square and symmetric
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return -1
    if not np.allclose(A, A.T):
        return -1

    n = A.shape[0]
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i, k] * L[j, k] for k in range(j))
            if i == j:
                d = A[i, i] - s
                if d <= 1e-12:        # not positive-definite
                    return -1
                L[i, j] = np.sqrt(d)
            else:
                L[i, j] = (A[i, j] - s) / L[j, j]

    return L.tolist()
