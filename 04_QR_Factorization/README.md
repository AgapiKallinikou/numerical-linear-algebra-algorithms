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

## ⚠️ The Cost of Explicitly Forming Q

In practical High-Performance Computing (HPC) applications, explicitly forming the orthogonal matrix $Q$ is often avoided. $Q$ is implicitly defined as the product of Householder transformations:

$$Q = H_1 H_2 \dots H_{n-1}$$

Our implementation explicitly accumulates $Q$ for demonstration and verification purposes. However, it is mathematically proven that if the explicit construction of $Q$ is required, the most efficient method is backward accumulation ($Q_k = H_k Q_{k+1}$). 

Applying the transformation $H_k = I - 2v_kv_k^T$ to the trailing submatrix requires approximately $2(n - k)^2$ operations. Summing this over all $n$ steps yields the asymptotic extra cost:

$$\text{Extra Flops} \approx \sum_{k=1}^{n} 2(n - k)^2 = 2 \sum_{j=1}^{n} j^2 \approx \frac{2}{3}n^3$$

**Conclusion:** Explicitly forming $Q$ adds a massive $\frac{2}{3}n^3$ flops to the computational overhead. In memory-constrained or performance-critical environments (like solving Least Squares problems), it is significantly more efficient to store only the normalized Householder vectors $v_k$ and apply them dynamically when multiplying $Q$ with another vector or matrix.

## ⚖️ Householder vs. Givens Rotations: A Complexity Comparison

When computing the QR factorization, an alternative to Householder reflections is the use of **Givens Rotations**. However, Householder transformations are generally preferred for dense matrices due to computational efficiency. 

To introduce zeros into a vector $x \in \mathbb{R}^n$ such that it becomes a multiple of $e_1$, the complexity differs significantly:

### 1. Householder Reflections
A Householder transformation is defined as $H = I - 2vv^T$. Applying $H$ to a generic vector $y \in \mathbb{R}^n$:
$$Hy = y - 2v(v^T y)$$
* Inner product $v^T y$: $n$ multiplications.
* Scalar multiplication $2(v^T y)v$: $n$ multiplications.
* **Total Cost:** $\approx 2n$ flops.

### 2. Givens Rotations
To zero out $n-1$ elements iteratively, we must apply $n-1$ individual Givens rotation matrices. Each rotation modifies two components of the vector ($y_i, y_j$):
$$
\begin{bmatrix} y'_i \\ y'_j \end{bmatrix} = \begin{bmatrix} c & s \\ -s & c \end{bmatrix} \begin{bmatrix} y_i \\ y_j \end{bmatrix}
$$
* Each rotation requires 4 multiplications.
* Applying $n-1$ rotations requires $4(n-1)$ multiplications.
* **Total Cost:** $\approx 4n$ flops.

**Conclusion:** Utilizing Givens rotations to annihilate elements in a dense column requires strictly **twice as many multiplications** as Householder reflections ($\approx 4n$ vs $\approx 2n$). Givens rotations are typically reserved for highly sparse or specifically structured matrices (like banded matrices) where they can target individual elements without disturbing existing zeros.
