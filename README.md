# Numerical Linear Algebra Algorithms

This repository contains Python implementations and experimental analyses of core numerical linear algebra algorithms. The project bridges the gap between theoretical mathematical concepts and practical scientific computing, focusing on numerical stability, computational efficiency, and algorithmic complexity.

## Features & Algorithms

### 1. Matrix Decompositions
* **LU Decomposition**: Implementation of general LU factorization.
* **Cholesky Factorization**: Optimal decomposition for Symmetric Positive Definite (SPD) matrices.
* **SPD Checking**: Algorithmic verification of positive definiteness using Sylvester's criterion and pivot analysis.

### 2. QR Decomposition
* **Householder Transformations**: Efficient, stable QR factorization for dense matrices.
* **Givens Rotations**: Alternative QR factorization, optimal for zeroing out specific elements or sparse matrices.
* **Performance Analysis**: Direct benchmarking between Householder and Givens approaches.

### 3. Determinant Computation
* **Gaussian Elimination (DetGEP)**: Efficient determinant calculation $O(n^3)$ using LU-based elimination.
* **Laplace Expansion (Recursive)**: Naive determinant computation to demonstrate combinatorial explosion ($O(n!)$) and highlight why recursive methods fail for large systems.

## Repository Structure

```text
numerical-linear-algebra-algorithms/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── qr/                     # Householder & Givens implementations
│   ├── determinant/            # DetGEP and Laplace implementations
│   └── decompositions/         # LU, Cholesky, and SPD checks
│
├── experiments/                # Python scripts for benchmarking & timing
│
├── notebooks/                  # Jupyter notebooks with detailed analyses
│
└── results/
    └── plots/                  # Visualizations of complexity & execution time

```

## Academic Context & Author

This project was developed as part of the **"Matrix Calculus"** course at the **National and Kapodistrian University of Athens (NKUA)**, Department of Mathematics.

* **Author:** Agapi Kallinikou
* **Academic Year:** 2025 - 2026
