import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    r = 0
    for r in range(len(A)):
        B = [[row[i] for row in A] for i in range(len(A[r]))]
        r +=1
    return np.array(B)
