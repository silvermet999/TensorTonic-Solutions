import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    sigma = 1/(1+np.exp(np.negative(x)))
    return sigma

