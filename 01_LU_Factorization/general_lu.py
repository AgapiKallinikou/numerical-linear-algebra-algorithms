import numpy as np

def general_lu_factorization(A):
    """
    Computes the LU factorization of a general M x N matrix without pivoting.
    Handles rectangular matrices and early stopping for rank-deficient matrices.
    
    Parameters:
    A (numpy.ndarray): Input matrix of shape (M, N).
    
    Returns:
    L (numpy.ndarray): Lower triangular matrix of shape (M, M) with ones on the diagonal.
    U (numpy.ndarray): Upper triangular/trapezoidal matrix of shape (M, N).
    rank (int): The estimated rank of the matrix based on non-zero pivots.
    """
    # Convert input to float to avoid integer truncation issues
    U = np.copy(A).astype(float)
    m, n = U.shape
    
    # Initialize L as an M x M identity matrix
    L = np.eye(m)
    
    # The elimination can proceed up to min(m, n) steps
    limit = min(m, n)
    rank = 0
    
    for k in range(limit):
        pivot = U[k, k]
        
        # Check for zero pivot (Rank deficiency / Early stopping)
        if np.abs(pivot) < 1e-12:
            print(f"Zero pivot encountered at step {k+1}. Matrix is rank deficient.")
            break
            
        rank += 1
        
        # Eliminate entries below the pivot in column k
        for i in range(k + 1, m):
            multiplier = U[i, k] / pivot
            L[i, k] = multiplier
            
            # Vectorized update of the remaining elements in row i
            U[i, k:] = U[i, k:] - multiplier * U[k, k:]
            
    return L, U, rank

# --- Experimental Test ---
if __name__ == "__main__":
    # Test Case: m > n, Rank deficient (Case 3 from theory)
    A_test = np.array([
        [1, 2],
        [2, 4],
        [3, 6]
    ])
    
    print("Original Matrix A:\n", A_test)
    L, U, estimated_rank = general_lu_factorization(A_test)
    
    print(f"\nEstimated Rank: {estimated_rank}")
    print("Lower Matrix L:\n", np.round(L, 4))
    print("Upper Matrix U:\n", np.round(U, 4))
    
    # Verification
    print("\nVerification (L @ U):\n", np.round(L @ U, 4))
