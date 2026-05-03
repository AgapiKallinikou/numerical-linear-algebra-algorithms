import numpy as np

def householder_qr(A):
    """
    Computes the QR factorization of a rectangular matrix A using Householder reflections.
    Handles both Tall (m > n) and Wide/Square (m <= n) matrices.
    
    Parameters:
    A (numpy.ndarray): Matrix of shape (m, n).
    
    Returns:
    Q (numpy.ndarray): Orthogonal matrix of shape (m, m).
    R (numpy.ndarray): Upper triangular/trapezoidal matrix of shape (m, n).
    """
    m, n = A.shape
    R = np.copy(A).astype(float)
    Q = np.eye(m)
    
    # Determine the number of steps s = min(n, m - 1)
    s = min(n, m - 1) if m > 1 else 0
    
    for k in range(s):
        x = R[k:m, k]
        norm_x = np.linalg.norm(x)
        
        # Skip if the column below the diagonal is already zeroed out
        if norm_x < 1e-12:
            continue
            
        # Create the Householder vector v
        v = np.copy(x)
        sign = 1 if x[0] >= 0 else -1
        v[0] += sign * norm_x
        
        # Normalize the Householder vector
        v = v / np.linalg.norm(v)
        
        # Apply the reflection to R: R = H * R = (I - 2*v*v.T) * R
        R[k:m, k:] -= 2 * np.outer(v, np.dot(v, R[k:m, k:]))
        
        # Accumulate the orthogonal matrix Q: Q = Q * H
        Q[:, k:m] -= 2 * np.outer(np.dot(Q[:, k:m], v), v)
        
    # Force exact numerical zeros below the main diagonal for a clean R matrix
    for i in range(1, m):
        for j in range(min(i, n)):
            R[i, j] = 0.0
            
    return Q, R

# --- Experimental Test ---
if __name__ == "__main__":
    print("--- Case 1: Tall Matrix (m > n) ---")
    A_tall = np.array([
        [1, -1,  4],
        [1,  4, -2],
        [1,  4,  2],
        [1, -1,  0]
    ], dtype=float)
    
    Q1, R1 = householder_qr(A_tall)
    print("Matrix R (Notice the bottom row is all zeros):\n", np.round(R1, 4))
    print("Verification (Q @ R):\n", np.round(Q1 @ R1, 4))
    
    print("\n--- Case 2: Wide Matrix (m <= n) ---")
    A_wide = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ], dtype=float)
    
    Q2, R2 = householder_qr(A_wide)
    print("Matrix R (Notice the R1 and S block structure):\n", np.round(R2, 4))
    print("Verification (Q @ R):\n", np.round(Q2 @ R2, 4))
