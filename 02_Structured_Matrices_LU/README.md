# LU Factorization for Structured Matrices

Standard Gaussian Elimination is an $\mathcal{O}(N^3)$ operation, making it computationally expensive for large systems. However, many real-world applications (such as discretizing differential equations or Markov Chains) produce highly structured, sparse matrices. 

This directory contains highly optimized $\mathcal{O}(N)$ and $\mathcal{O}(N^2)$ LU factorizations that exploit these structural properties.

## 🚀 Implemented Algorithms & Complexity

### 1. Tridiagonal Matrix Factorization (Thomas Algorithm approach)
* **Structure:** Non-zero elements exist only on the main diagonal, one super-diagonal, and one sub-diagonal.
* **Optimization:** Instead of passing an $N \times N$ matrix, the algorithm utilizes three 1D arrays (vectors). This drops spatial complexity to $\mathcal{O}(N)$.
* **Time Complexity:** Drastically reduced from $\mathcal{O}(N^3)$ to **$\mathcal{O}(N)$**. Requires only one elimination step per column.
* **Symmetric Variant:** For symmetric tridiagonal matrices, memory footprint is further reduced as the sub-diagonal equals the super-diagonal.

### 2. Upper Hessenberg Matrix Factorization
* **Structure:** Zeros everywhere below the first sub-diagonal ($a_{ij} = 0 \quad \forall i > j+1$).
* **Optimization:** Since there is only one non-zero element below the pivot in each column, the algorithm strictly zeroes out exactly one element per step, while vectorized operations update the rest of the row.
* **Time Complexity:** Reduced to **$\mathcal{O}(N^2)$**.

## 🧠 Why this matters
Exploiting matrix sparsity and structure is crucial in large-scale Machine Learning and Scientific Computing. By avoiding operations on known zeros, these algorithms prevent unnecessary floating-point operations and memory overhead, showcasing a fundamental principle of High-Performance Computing (HPC).
