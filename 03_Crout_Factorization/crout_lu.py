import numpy as np

def crout_factorization(A):
    """
    Computes the Crout LU Factorization of a square matrix A.
    In Crout, L is a lower triangular matrix and U is a unit upper triangular matrix.
    
    Parameters:
    A (numpy.ndarray): Square non-singular matrix of size (N, N).
    
    Returns:
    L (numpy.ndarray): Lower triangular matrix.
    U (numpy.ndarray): Unit upper triangular matrix.
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.eye(n)  # U has 1s on the main diagonal
    
    for j in range(n):
        # Step 1: Compute column j for matrix L
        for i in range(j, n):
            # Using np.dot for fast inner product instead of a loop
            sum_Lk_Ukj = np.dot(L[i, :j], U[:j, j])
            L[i, j] = A[i, j] - sum_Lk_Ukj
            
        # Step 2: Compute row j for matrix U
        if j < n - 1:
            if np.abs(L[j, j]) < 1e-12:
                raise ValueError(f"Zero pivot encountered at L[{j},{j}]. Crout fails without pivoting.")
            
            for i in range(j + 1, n):
                sum_Ljk_Uki = np.dot(L[j, :j], U[:j, i])
                U[j, i] = (A[j, i] - sum_Ljk_Uki) / L[j, j]
                
    return L, U

# --- Experimental Test ---
if __name__ == "__main__":
    print("--- 3x3 Matrix Test ---")
    A_test = np.array([
        [2, 1, 1],
        [4, 3, 3],
        [8, 7, 9]
    ], dtype=float)
    
    print("Original Matrix A:\n", A_test)
    
    L_crout, U_crout = crout_factorization(A_test)
    
    print("\nLower Matrix L (Crout):\n", np.round(L_crout, 4))
    print("Upper Matrix U (Crout):\n", np.round(U_crout, 4))
    
    print("\nVerification (L @ U):\n", np.round(L_crout @ U_crout, 4))
