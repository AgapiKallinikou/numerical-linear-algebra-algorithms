# Givens Rotations

This directory explores the applications and computational complexity of **Givens Rotations** in Numerical Linear Algebra. It contains highly optimized implementations for applying rotations to matrices and computing the full QR factorization.

---

## 1. Right Matrix Multiplication (`givens_right_mult.py`)

This section demonstrates the highly optimized implementation of right-multiplying a dense matrix $A \in \mathbb{R}^{m \times n}$ by a Givens rotation matrix $J(i, j, \theta)$.

### 🚀 Algorithmic Optimization
A naive implementation of the multiplication $A \cdot J$ would require explicitly constructing the $n \times n$ matrix $J$ and performing standard matrix multiplication, resulting in computationally heavy overhead ($\mathcal{O}(m n^2)$ flops).

However, a right Givens rotation acts exclusively on the column space of $A$. Specifically, it updates only the $i$-th and $j$-th columns via a linear combination, leaving all other columns unchanged:

$$
A'_{:,i} = c \cdot A_{:,i} - s \cdot A_{:,j}
$$

$$
A'_{:,j} = s \cdot A_{:,i} + c \cdot A_{:,j}
$$

where $c = \cos(\theta)$ and $s = \sin(\theta)$.

### 🧮 Complexity Analysis
By isolating the update to just the affected columns, the algorithm scales linearly with the number of rows $m$. For each of the $m$ rows, the algorithm performs exactly:
* 4 multiplications
* 2 additions/subtractions

**Total Flops:** $\approx 4m$

This reduces the asymptotic computational complexity strictly to **$\mathcal{O}(m)$**, making it highly suitable for large-scale Scientific Computing applications where explicit matrix formation is avoided to conserve memory and CPU cycles.

---

## 2. Full QR Factorization (`givens_qr.py`)

This section implements the full QR factorization of a matrix $A \in \mathbb{R}^{m \times n}$ using Givens Rotations. The algorithm iterates through the columns from left to right, and zeroes out the sub-diagonal elements from bottom to top by applying rotations to adjacent rows.

### 🧮 Complexity Proof

To annihilate an element at position $(i, j)$, a Givens rotation is applied to rows $i-1$ and $i$, affecting columns $j$ through $n$. Updating each pair of elements requires 4 multiplications. Thus, the cost per annihilation is roughly $4(n-j)$ flops.

Summing over all rows ($i$ from $j+1$ to $m$) and all columns ($j$ from 1 to $n$), the total computational cost is:

$$
\text{Flops} \approx \sum_{j=1}^{n} 4(m - j)(n - j)
$$

Expanding and using asymptotic approximations for large matrices ($\sum j \approx \frac{n^2}{2}$ and $\sum j^2 \approx \frac{n^3}{3}$):

$$
\text{Flops} \approx 4 \left( mn(n) - \frac{(m + n)n^2}{2} + \frac{n^3}{3} \right)
$$

$$
\text{Flops} \approx 2n^2 \left( m - \frac{n}{3} \right)
$$

### ⚖️ Comparison with Householder Method
The standard Householder QR factorization requires $n^2(m - n/3)$ operations (counting multiply-add pairs as a single unit). 
The Givens approach requires **strictly twice the computational effort** for dense matrices. This makes Givens rotations less efficient for general dense matrices, though they remain highly valuable for parallel computing architectures or sparse/banded matrices where operations can be selectively applied to specific elements.

### ⚠️ The Cost of Explicitly Computing Q

If the explicit construction of the orthogonal matrix $Q \in \mathbb{R}^{m \times m}$ is required, all rotations must be accumulated into an identity matrix $I_m$. 

The total number of applied Givens rotations is approximately $mn - \frac{n^2}{2}$.
Applying a single rotation to two full columns of length $m$ requires $4m$ operations. Therefore, the extra complexity to form $Q$ is:

$$
\text{Extra Flops} \approx 4m \left( mn - \frac{n^2}{2} \right) = 4m^2n - 2mn^2
$$

*(For a square matrix where $m = n$, this adds an enormous $2n^3$ flops to the total runtime).*