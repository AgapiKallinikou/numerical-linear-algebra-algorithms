import numpy as np
import time

def givens_right_mult_loop(A, i, j, c, s):
    """
    Applies a Givens rotation to matrix A from the right: A * J(i, j, theta).
    Uses a standard for-loop (translating the mathematical pseudo-code).
    Updates the matrix in-place to save memory.
    """
    m, n = A.shape
    for k in range(m):
        t1 = A[k, i]
        t2 = A[k, j]
        A[k, i] = c * t1 - s * t2
        A[k, j] = s * t1 + c * t2
    return A

def givens_right_mult_vectorized(A, i, j, c, s):
    """
    Vectorized NumPy implementation of the right Givens rotation.
    Avoids Python's slow for-loops, achieving the same O(m) complexity
    but much faster wall-clock execution time.
    """
    t1 = A[:, i].copy()
    t2 = A[:, j].copy()
    A[:, i] = c * t1 - s * t2
    A[:, j] = s * t1 + c * t2
    return A

# --- Experimental Test ---
if __name__ == "__main__":
    # Create a random 5x4 matrix
    np.random.seed(42)
    A_original = np.random.rand(5, 4)
    
    # Define Givens parameters (e.g., theta = pi/4)
    theta = np.pi / 4
    c = np.cos(theta)
    s = np.sin(theta)
    i, j = 1, 3 # Columns to update (0-indexed: 2nd and 4th columns)
    
    print("--- Original Matrix A ---")
    print(np.round(A_original, 4))
    
    # Test the vectorized algorithm
    A_vectorized = np.copy(A_original)
    givens_right_mult_vectorized(A_vectorized, i, j, c, s)
    
    print(f"\n--- Matrix after Givens Right Multiplication (Columns {i} and {j} updated) ---")
    print(np.round(A_vectorized, 4))
