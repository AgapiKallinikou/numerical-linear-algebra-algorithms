# Crout LU Factorization

This directory contains the implementation of the **Crout Factorization** algorithm. Unlike Doolittle's method (where the lower matrix $L$ has unit diagonals), Crout's method decomposes a non-singular matrix $A$ into a lower triangular matrix $L$ and a **unit upper triangular matrix $U$** ($u_{ii} = 1$).

## 🧮 Algorithm Dynamics & Complexity

Instead of viewing the factorization through the lens of Gaussian row operations (multipliers), the Crout method approaches the problem via direct algebraic substitution. The elements of $L$ and $U$ are derived directly from the matrix multiplication definition $A = LU$.

* **Column-Row Alternation:** The algorithm computes the $j$-th column of $L$ and immediately follows it by computing the $j$-th row of $U$.
* **Dot Products:** The core of the computation relies heavily on inner products (dot products) of previously computed rows and columns.
* **Complexity:** The asymptotic complexity remains **$\mathcal{O}(N^3)$**, requiring roughly $\frac{2N^3}{3}$ floating-point operations (flops), matching standard Gaussian elimination.

## 🚀 Implementation Highlights
The provided Python implementation optimizes the nested summation loops found in the standard pseudocode by utilizing NumPy's highly optimized `np.dot()` function. This vectorization reduces interpreter overhead, making the code both faster and more aligned with modern numerical libraries (BLAS-style operations).
