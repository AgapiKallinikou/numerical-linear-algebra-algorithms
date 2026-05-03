# QR Factorization via Householder Reflections

This directory contains the implementation of the QR Factorization using **Householder Reflections**. This method is heavily preferred in numerical computing due to its exceptional numerical stability compared to Gram-Schmidt orthogonalization.

## 🧮 Matrix Structures & Complexity

The algorithm dynamically adapts to the dimensions of the input matrix $A \in \mathbb{R}^{m \times n}$. The transformations $H_k$ are applied iteratively to annihilate sub-diagonal elements. The total number of steps is $s = \min(n, m - 1)$.

### Case 1: Tall Matrix ($m > n$)
* **Elimination Steps:** The algorithm performs exactly $s = n$ steps.
* **Structure:** The resulting matrix $R$ is strictly upper triangular in its first $n$ rows ($R_1 \in \mathbb{R}^{n \times n}$), while the remaining $m - n$ rows are completely zeroed out.
* **Computational Complexity (Flops):**
  $$Flops \approx n^2 \left(m - \frac{n}{3}\right)$$

### Case 2: Wide or Square Matrix ($m \leq n$)
* **Elimination Steps:** The algorithm stops early at $s = m - 1$, as there are no sub-diagonal elements left to annihilate in the final row.
* **Structure:** The resulting matrix $R$ contains an upper triangular block $R_1 \in \mathbb{R}^{m \times m}$ on the left, and a dense block $S \in \mathbb{R}^{m \times (n-m)}$ on the right.
* **Computational Complexity (Flops):**
  $$Flops \approx m^2 \left(n - \frac{m}{3}\right)$$

## 🚀 Application
By utilizing implicit Householder vectors ($v$), this implementation strictly avoids the explicit construction of the $H$ matrices, favoring computationally efficient vector outer products instead.
