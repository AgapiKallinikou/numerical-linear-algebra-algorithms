import numpy as np

def givens_qr(A, compute_Q=False):
    """
    Computes the QR factorization of a matrix A using Givens rotations.
    
    Parameters:
    A (numpy.ndarray): Input matrix of shape (m, n).
    compute_Q (bool): If True, explicitly forms and returns the orthogonal matrix Q.
    
    Returns:
    Q (numpy.ndarray or None): The orthogonal matrix of shape (m, m), or None if compute_Q is False.
    R (numpy.ndarray): The upper triangular matrix of shape (m, n).
    """
    m, n = A.shape
    R = np.copy(A).astype(float)
    
    # Initialize Q as an identity matrix if we need to explicitly compute it
    Q = np.eye(m) if compute_Q else None
    
    # Iterate over columns (from left to right)
    for j in range(min(n, m)):
        # Iterate over rows in the current column (from bottom to top)
        for i in range(m - 1, j, -1):
            
            a = R[i - 1, j]
            b = R[i, j]
            
            # Skip if the element is already zero
            if np.abs(b) < 1e-12:
                continue
                
            # Safely compute cos(theta) and sin(theta) avoiding overflow
            r = np.hypot(a, b)
            c = a / r
            s = -b / r
            
            # Apply the rotation to rows i-1 and i, from column j to the end
            # (Vectorized equivalent of the inner loop k)
            R_i_minus_1 = c * R[i - 1, j:] - s * R[i, j:]
            R_i         = s * R[i - 1, j:] + c * R[i, j:]
            
            R[i - 1, j:] = R_i_minus_1
            R[i, j:]     = R_i
            
            # If Q is requested, accumulate the rotations
            if compute_Q:
                Q_i_minus_1 = c * Q[:, i - 1] - s * Q[:, i]
                Q_i         = s * Q[:, i - 1] + c * Q[:, i]
                Q[:, i - 1] = Q_i_minus_1
                Q[:, i]     = Q_i
                
    # Force exact numerical zeros below the main diagonal
    for i in range(1, m):
        for j in range(min(i, n)):
            R[i, j] = 0.0
            
    return Q, R

# --- Experimental Test ---
if __name__ == "__main__":
    A_test = np.array([
        [0.8147, 0.0975, 0.1576],
        [0.9058, 0.2785, 0.9706],
        [0.1270, 0.5469, 0.9572],
        [0.9134, 0.9575, 0.4854]
    ])
    
    print("--- Original Matrix A ---")
    print(A_test)
    
    Q, R = givens_qr(A_test, compute_Q=True)
    
    print("\n--- Matrix R (Upper Triangular) ---")
    print(np.round(R, 4))
    
    print("\n--- Matrix Q (Orthogonal) ---")
    print(np.round(Q, 4))
    
    print("\n--- Verification (Q @ R) ---")
    print(np.round(Q @ R, 4))