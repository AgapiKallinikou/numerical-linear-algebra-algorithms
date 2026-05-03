# Numerical Linear Algebra & Algorithmic Complexity

A comprehensive collection of Numerical Linear Algebra algorithms implemented from scratch in Python. This repository bridges the gap between pure mathematical theory and High-Performance Computing (HPC), focusing on algorithmic complexity, memory optimization, matrix factorizations, and numerical stability.

## 📌 Key Highlights
* **Algorithmic Efficiency:** Empirical benchmarks and theoretical proofs comparing polynomial **O(n³)** vs factorial **O(n!)** time complexities.
* **Exploiting Matrix Structure:** Highly optimized **O(N)** and **O(N²)** implementations for Tridiagonal and Hessenberg matrices.
* **Orthogonal Transformations:** Detailed computational cost comparisons between Householder Reflections and Givens Rotations.
* **Robust Edge-Case Handling:** Dynamic shape adaptation and early-stopping mechanisms for non-square and rank-deficient matrices.

---

## 📂 Repository Structure

### Part 1: LU Factorizations & Linear Systems
* **`01_LU_Factorization/`**
  Implementation of Gaussian Elimination without pivoting that dynamically handles rectangular inputs (M × N). Features an **early-stopping mechanism** for rank-deficient matrices, reducing complexity to **O(rmn)**.
* **`02_Structured_Matrices_LU/`**
  Exploits matrix sparsity to bypass standard **O(N³)** costs. Includes the Thomas Algorithm for Tridiagonal matrices (**O(N)**) and optimizations for Upper Hessenberg matrices (**O(N²)**).
* **`03_Crout_Factorization/`**
  Direct algebraic substitution approach (where the upper matrix U has unit diagonals), heavily optimized using vectorized inner products (dot products) to minimize interpreter overhead.

### Part 2: QR Factorizations & Orthogonalizations
* **`04_QR_Factorization/`**
  QR Factorization using Householder Reflections for exceptional numerical stability. Includes theoretical proofs on why explicitly forming the orthogonal matrix Q adds a massive **(2/3)n³** flop overhead, and why implicit calculation is preferred.
* **`05_Givens_Rotations/`**
  Implementation of right-side matrix multiplication and full QR factorization using Givens Rotations. Features a complexity analysis demonstrating why Givens is ideal for sparse matrices but costs strictly twice as much as Householder for dense systems.

### Part 3: Computational Complexity
* **`06_Determinant_Complexity/`**
  A deep dive into the computational costs of determinant calculations. Includes a Python benchmark comparing Gaussian Elimination with Partial Pivoting (**O(n³)**) against the recursive Laplace Expansion (**O(n!)**). 
  * *Fun Fact derived from the analysis: For a 100x100 matrix, the Laplace method would take ≈ 9.32 × 10¹⁵² seconds (vastly exceeding the age of the universe), while GEP finishes in ≈ 3.33 seconds.*

---

## 🛠️ Tech Stack & Methodologies
* **Language:** Python 3.x
* **Libraries:** NumPy (Vectorized operations, BLAS-style computing)
* **Concepts:** Big-O Complexity, Flop Counting, Vectorization, Numerical Stability, Memory Footprint Optimization.

---

## 🎓 Academic Context & Author

This project was developed as part of the coursework at the **National and Kapodistrian University of Athens (NKUA)**.

* **Author:** Agapi Kallinikou
* **Academic Year:** 2025 - 2026
