import numpy as np

def generator(z, W, b):
    """
    Returns: np.ndarray of shape (batch, output_dim) with tanh-activated values rounded to 4 decimals
    """
    # x = np.ndarray(z, output_dim)
    g = np.tanh(np.dot(z, W)+b)
    return g

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html
# output_dim = np.array([14, 14])
z = np.ndarray(shape=(14, 100))
W = np.random.randn(100, 14) * 0.1
b = np.zeros(14)
G = generator(z, W, b)

# tanh function search
# https://numpy.org/doc/stable/reference/generated/numpy.sinh.html
# https://numpy.org/doc/stable/reference/generated/numpy.tanh.html


