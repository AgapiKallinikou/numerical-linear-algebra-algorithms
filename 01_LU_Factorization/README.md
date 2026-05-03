# General LU Factorization (Non-Square & Rank-Deficient Matrices)

This directory contains the implementation of the generalized LU Factorization using Gaussian Elimination (without pivoting). Unlike standard implementations that assume an $N \times N$ full-rank matrix, this algorithm dynamically handles rectangular inputs ($M \times N$) and detects rank deficiencies.

## 🧮 Theoretical & Computational Analysis

The algorithm adapts its behavior based on the shape and rank of the input matrix $A$. The computational complexity (Flops) has been theoretically derived for all four edge cases:

### Case 1: Tall Matrix, Full Column Rank ($m > n$, rank = $n$)
* The algorithm eliminates elements for exactly $n$ steps.
* **Complexity:** $\approx mn^2 - \frac{n^3}{3}$ flops.

### Case 2: Wide Matrix, Full Row Rank ($m < n$, rank = $m$)
* The algorithm runs out of rows before columns, terminating at step $m$.
* **Complexity:** $\approx nm^2 - \frac{m^3}{3}$ flops.

### Cases 3 & 4: Rank Deficient Matrices (rank = $r < \min(m,n)$)
* The algorithm utilizes **Early Stopping**. Upon encountering a zero pivot at step $r$, it halts elimination, realizing the remaining rows are linearly dependent (already zeroed out).
* **Complexity:** $\approx O(rmn)$ flops. 

## 🚀 Key Takeaways
1. **Dynamic Shape Handling:** The resulting $L$ matrix is always strictly $m \times m$ (identity trace), while $U$ preserves the $m \times n$ shape.
2. **Computational Efficiency:** Early stopping drastically reduces the number of Flops for highly dependent data structures.
3. **Vectorization:** The provided Python implementation utilizes NumPy's vectorization to update entire matrix rows simultaneously, avoiding slow nested `for` loops.
