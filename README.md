# Numerical Linear Algebra Algorithms

A collection of efficient implementations and theoretical analyses of core Numerical Linear Algebra algorithms. This repository focuses on the bridge between mathematical foundations and computational efficiency, specifically targeting matrix factorizations and algorithmic complexity.

## 📌 Project Highlights

* **Algorithmic Efficiency:** Detailed comparison between polynomial $O(n³)$ and factorial $O(n!)$ approaches for determinant calculation.
* **Matrix Factorizations:** Implementation of orthogonal transformations using Givens Rotations.
* **Numerical Stability:** Emphasis on methods that maintain precision in floating-point environments.

---

## 📂 Repository Structure

### [05_Givens_Rotations](./05_Givens_Rotations)
Focuses on orthogonal transformations using Givens Rotations.
* **`givens_right_mult.py`**: Efficient implementation of right-side matrix multiplication with a Givens rotation.
* **`givens_qr.py`**: QR factorization of a matrix $A \in \mathbb{R}^{m \times n}$ using a sequence of rotations to zero out sub-diagonal elements.

### [06_Determinant_Complexity](./06_Determinant_Complexity)
A deep dive into the computational costs of determinant calculations, showcasing why mathematical elegance doesn't always translate to algorithmic performance.
* **`determinant_benchmarks.py`**: A Python script benchmarking Gaussian Elimination with Partial Pivoting (GEP) against the recursive Laplace Expansion.
* **Theoretical Proofs**: Detailed analysis in the subdirectory's README proving the $O(n³)$ vs $O(n!)$ complexity.
* **Key Finding:** Demonstrates that for $n=100$, the Laplace method would take longer than the age of the universe to compute, while GEP finishes in seconds.

---

## 🛠 Tech Stack

* **Language:** Python 3.x
* **Libraries:** NumPy (Vectorized operations and matrix manipulations)
* **Analysis:** Big O Notation, Computational Complexity Analysis

---

