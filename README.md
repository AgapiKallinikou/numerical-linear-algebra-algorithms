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
## Key Insights & Experiments

The experiments/ and notebooks/ directories contain benchmarking tools that evaluate:
1. The execution time and scaling behavior of the implemented algorithms.
2. The computational trade-offs between Householder reflections and Givens rotations.
3. The catastrophic performance degradation of Laplace expansion compared to Gaussian elimination for matrix determinants.

## Installation & Usage

To run this project locally, execute the following commands in your terminal:

```bash
# 1. Clone the repository
git clone [https://github.com/AgapiKallinikou/numerical-linear-algebra-algorithms.git](https://github.com/AgapiKallinikou/numerical-linear-algebra-algorithms.git)
cd numerical-linear-algebra-algorithms
```
# 2. Install the required dependencies
```bash
pip install -r requirements.txt
```

# 3. Run a benchmark experiment
```bash
python experiments/qr_benchmark.py
```    
## Purpose

This project was developed to demonstrate a practical understanding of numerical linear algebra. It showcases the ability to translate rigorous mathematical proofs and matrix theory into efficient, benchmarked code, with an emphasis on real-world applicability in scientific computing and machine learning.


    
## Academic Context & Author

This project was developed as part of the **"Matrix Calculus"** course at the **National and Kapodistrian University of Athens (NKUA)**, Department of Mathematics.

* **Author:** Agapi Kallinikou
* **Academic Year:** 2025 - 2026
