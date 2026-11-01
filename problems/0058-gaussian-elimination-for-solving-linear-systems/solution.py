import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.

	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	A = np.array(A, dtype=float)   # copies, so inputs aren't modified
	b = np.array(b, dtype=float)
	n = len(b)

	# Forward elimination
	for k in range(n - 1):
		# Partial pivoting: row with the largest |entry| in column k
		p = k + np.argmax(np.abs(A[k:, k]))
		if abs(A[p, k]) < 1e-12:
			raise ValueError("Matrix is singular: no unique solution.")
		if p != k:
			A[[k, p]] = A[[p, k]]
			b[[k, p]] = b[[p, k]]

		for i in range(k + 1, n):
			m = A[i, k] / A[k, k]
			A[i, k:] -= m * A[k, k:]
			b[i] -= m * b[k]

	if abs(A[n - 1, n - 1]) < 1e-12:
		raise ValueError("Matrix is singular: no unique solution.")

	# Back substitution
	x = np.zeros(n)
	for k in range(n - 1, -1, -1):
		x[k] = (b[k] - A[k, k + 1:] @ x[k + 1:]) / A[k, k]
	return x


