import numpy as np

def lu_decomposition(A: list) -> tuple:
	"""
	Perform LU decomposition on a square matrix using Doolittle's method.

	Args:
		A: Square matrix as a list of lists

	Returns:
		tuple: (L, U) where L is lower triangular with 1s on diagonal,
		       U is upper triangular, and A = L @ U
	"""
	A = np.array(A, dtype=float)
	n = A.shape[0]
	if A.ndim != 2 or A.shape[1] != n:
		raise ValueError("A must be a square matrix.")

	L = np.eye(n)
	U = np.zeros((n, n))

	for i in range(n):
		# Row i of U
		for j in range(i, n):
			U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))

		if abs(U[i, i]) < 1e-12:
			raise ValueError("Zero pivot encountered: pivoting is required.")

		# Column i of L (below the diagonal)
		for j in range(i + 1, n):
			L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

	return L, U
