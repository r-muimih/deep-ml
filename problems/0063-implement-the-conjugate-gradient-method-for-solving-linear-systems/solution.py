import numpy as np

def conjugate_gradient(A, b, n, x0=None, tol=1e-8):
	"""
	Solve the system Ax = b using the Conjugate Gradient method.

	:param A: Symmetric positive-definite matrix
	:param b: Right-hand side vector
	:param n: Maximum number of iterations
	:param x0: Initial guess for solution (default is zero vector)
	:param tol: Convergence tolerance
	:return: Solution vector x
	"""
	A = np.array(A, dtype=float)
	b = np.array(b, dtype=float)
	x = np.zeros_like(b) if x0 is None else np.array(x0, dtype=float)

	# Initial residual and search direction
	r = b - A @ x
	p = r.copy()
	rs_old = r @ r

	if np.sqrt(rs_old) < tol:
		return x

	for _ in range(n):
		Ap = A @ p
		alpha = rs_old / (p @ Ap)
		x = x + alpha * p
		r = r - alpha * Ap

		rs_new = r @ r
		if np.sqrt(rs_new) < tol:
			break

		beta = rs_new / rs_old
		p = r + beta * p
		rs_old = rs_new

	return x


# Tests
A = [[4, 1], [1, 3]]
b = [6, 6]
x = conjugate_gradient(A, b, n=100)
print(x)                                     # [1.09090909 1.63636364]
print(np.allclose(np.dot(A, x), b))          # True
print(np.allclose(x, np.linalg.solve(A, b))) # True

# 3x3 SPD system
A3 = [[4, 1, 0], [1, 3, 1], [0, 1, 2]]
b3 = [1, 2, 3]
print(np.allclose(conjugate_gradient(A3, b3, 100), np.linalg.solve(A3, b3)))  # True

# With an iimport numpy as np

def conjugate_gradient(A, b, n, x0=None, tol=1e-8):
	"""
	Solve the system Ax = b using the Conjugate Gradient method.

	:param A: Symmetric positive-definite matrix
	:param b: Right-hand side vector
	:param n: Maximum number of iterations
	:param x0: Initial guess for solution (default is zero vector)
	:param tol: Convergence tolerance
	:return: Solution vector x
	"""
	A = np.array(A, dtype=float)
	b = np.array(b, dtype=float)
	x = np.zeros_like(b) if x0 is None else np.array(x0, dtype=float)

	# Initial residual and search direction
	r = b - A @ x
	p = r.copy()
	rs_old = r @ r

	if np.sqrt(rs_old) < tol:
		return x

	for _ in range(n):
		Ap = A @ p
		alpha = rs_old / (p @ Ap)
		x = x + alpha * p
		r = r - alpha * Ap

		rs_new = r @ r
		if np.sqrt(rs_new) < tol:
			break

		beta = rs_new / rs_old
		p = r + beta * p
		rs_old = rs_new

	return x
