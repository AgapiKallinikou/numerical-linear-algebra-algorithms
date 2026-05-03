import numpy as np
import time

def det_gep(matrix):
    """Υπολογισμός ορίζουσας με Απαλοιφή Gauss και Μερική Οδήγηση O(n^3)."""
    A = np.copy(matrix).astype(float)
    n = len(A)
    det = 1.0
    sign = 1

    for k in range(n - 1):
        # Εύρεση μέγιστου στοιχείου (Μερική Οδήγηση)
        pivot_row = k
        max_val = abs(A[k, k])
        for i in range(k + 1, n):
            if abs(A[i, k]) > max_val:
                max_val = abs(A[i, k])
                pivot_row = i
                
        if max_val == 0:
            return 0.0
            
        # Εναλλαγή γραμμών αν χρειάζεται
        if pivot_row != k:
            A[[k, pivot_row]] = A[[pivot_row, k]]
            sign *= -1
            
        # Απαλοιφή στοιχείων κάτω από τον οδηγό
        for i in range(k + 1, n):
            m_ik = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] -= m_ik * A[k, j]
                
    # Υπολογισμός τελικής ορίζουσας από τη διαγώνιο
    for k in range(n):
        det *= A[k, k]
        
    return sign * det

def det_laplace(A):
    """Υπολογισμός ορίζουσας με Αναδρομικό Ανάπτυγμα Laplace O(n!)."""
    n = len(A)
    if n == 1:
        return A[0][0]
        
    det = 0.0
    sign = 1
    
    for j in range(n):
        # Δημιουργία υποπίνακα (διαγραφή 1ης γραμμής και j-στήλης)
        submatrix = [row[:j] + row[j+1:] for row in A[1:]]
        cofactor = sign * det_laplace(submatrix)
        det += A[0][j] * cofactor
        sign *= -1
        
    return det

# ==========================================
# EXPERIMENT: Benchmark GEP vs Laplace
# ==========================================
if __name__ == "__main__":
    print(f"{'n':<4} | {'DetGEP Time (s)':<17} | {'DetLaplace Time (s)':<19} | {'Match?':<6}")
    print("-" * 55)
    
    # We test up to n=10 because Laplace becomes dangerously slow after 11.
    for n in range(2, 11):
        # Create a random n x n matrix
        np.random.seed(42)
        A = np.random.rand(n, n) * 10
        A_list = A.tolist() # List format for Laplace to avoid numpy overhead in recursion
        
        # Benchmark GEP
        start_time = time.time()
        res_gep = det_gep(A)
        time_gep = time.time() - start_time
        
        # Benchmark Laplace
        start_time = time.time()
        res_lap = det_laplace(A_list)
        time_lap = time.time() - start_time
        
        # Check if results match
        match = np.isclose(res_gep, res_lap)
        
        print(f"{n:<4} | {time_gep:<17.6f} | {time_lap:<19.6f} | {str(match):<6}")
