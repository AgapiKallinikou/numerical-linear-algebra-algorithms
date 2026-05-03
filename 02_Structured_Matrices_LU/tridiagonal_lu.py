import numpy as np

def tridiagonal_lu(d, e, c):
    """
    Computes the LU factorization of a Tridiagonal matrix using 1D arrays.
    Complexity: O(N) Time, O(N) Space.
    
    Parameters:
    d (numpy.ndarray): Main diagonal of length n
    e (numpy.ndarray): Super-diagonal of length n-1
    c (numpy.ndarray): Sub-diagonal of length n-1
    
    Returns:
    l (numpy.ndarray): Sub-diagonal of L (length n-1)
    u (numpy.ndarray): Main diagonal of U (length n)
    """
    n = len(d)
    u = np.zeros(n)
    l = np.zeros(n-1)
    
    u[0] = d[0]
    for k in range(n - 1):
        if np.abs(u[k]) < 1e-12:
            raise ValueError(f"Zero pivot at index {k}. Factorization fails.")
            
        l[k] = c[k] / u[k]
        u[k+1] = d[k+1] - l[k] * e[k]
        
    return l, u

def symmetric_tridiagonal_lu(d, e):
    """
    Computes the LU factorization of a Symmetric Tridiagonal matrix.
    Since it's symmetric, sub-diagonal equals super-diagonal (c = e).
    """
    return tridiagonal_lu(d, e, e)

def hessenberg_lu(A):
    """
    Computes the LU factorization of an Upper Hessenberg matrix.
    Complexity: O(N^2) Time.
    
    Parameters:
    A (numpy.ndarray): Upper Hessenberg matrix (zeros below the first sub-diagonal).
    """
    n = A.shape[0]
    U = np.copy(A).astype(float)
    L = np.eye(n)
    
    for k in range(n - 1):
        if np.abs(U[k, k]) < 1e-12:
            raise ValueError(f"Zero pivot at index {k}.")
            
        # Only one element to eliminate per column!
        L[k+1, k] = U[k+1, k] / U[k, k]
        
        # Vectorized update only for the necessary row and columns
        U[k+1, k:] = U[k+1, k:] - L[k+1, k] * U[k, k:]
        
        # Enforce exact numerical zero below the diagonal
        U[k+1, k] = 0.0
        
    return L, U

# --- Experimental Test ---
if __name__ == "__main__":
    print("--- Tridiagonal LU Test ---")
    d = np.array([2.0, 2.0, 2.0])
    e = np.array([-1.0, -1.0])
    c = np.array([-1.0, -1.0])
    
    l, u = tridiagonal_lu(d, e, c)
    print("Sub-diagonal of L:", l)
    print("Main diagonal of U:", u)
    
    print("\n--- Upper Hessenberg LU Test ---")
    H = np.array([
        [2, 3, 1, 4],
        [1, 4, 2, 1],
        [0, 2, 5, 2],
        [0, 0, 1, 3]
    ])
    L_hess, U_hess = hessenberg_lu(H)
    print("L matrix:\n", np.round(L_hess, 4))
    print("U matrix:\n", np.round(U_hess, 4))
