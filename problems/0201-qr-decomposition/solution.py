import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
	"""
	Perform QR decomposition using Gram-Schmidt process.

	Args:
		A: An m x n matrix represented as list of lists

	Returns:
		Tuple of (Q, R) where Q is orthogonal and R is upper triangular
	"""
	A = np.array(A, dtype=float)
	if A.ndim != 2:
		raise ValueError("A must be a 2D matrix.")
	m, n = A.shape
	if m < n:
		raise ValueError("Requires m >= n (at least as many rows as columns).")

	Q = np.zeros((m, n))
	R = np.zeros((n, n))

	for j in range(n):
		v = A[:, j].copy()

		# Subtract projections onto the previous orthonormal vectors
		for i in range(j):
			R[i, j] = Q[:, i] @ A[:, j]
			v -= R[i, j] * Q[:, i]

		# Normalize
		R[j, j] = np.linalg.norm(v)
		if R[j, j] < 1e-12:
			raise ValueError("Columns are linearly dependent: QR via Gram-Schmidt fails.")
		Q[:, j] = v / R[j, j]

	return Q.tolist(), R.tolist()
