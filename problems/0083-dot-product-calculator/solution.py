import numpy as np

def calculate_dot_product(vec1, vec2):
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The dot product of the two vectors.
	"""
	vec1 = np.asarray(vec1)
	vec2 = np.asarray(vec2)

	if vec1.ndim != 1 or vec2.ndim != 1:
		raise ValueError("Both inputs must be 1D vectors.")
	if vec1.shape != vec2.shape:
		raise ValueError(
			f"Vectors must have equal length, got {vec1.shape[0]} and {vec2.shape[0]}."
		)

	return np.dot(vec1, vec2)


# Test
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(calculate_dot_product(a, b))  # 32