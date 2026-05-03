# Givens Rotations: Right Matrix Multiplication

This directory demonstrates the highly optimized implementation of right-multiplying a dense matrix $A \in \mathbb{R}^{m \times n}$ by a Givens rotation matrix $J(i, j, \theta)$.

## 🚀 Algorithmic Optimization

A naive implementation of the multiplication $A \cdot J$ would require explicitly constructing the $n \times n$ matrix $J$ and performing standard matrix multiplication, resulting in computationally heavy overhead ($\mathcal{O}(m n^2)$ flops).

However, a right Givens rotation acts exclusively on the column space of $A$. Specifically, it updates only the $i$-th and $j$-th columns via a linear combination, leaving all other columns unchanged:

$$
A'_{:,i} = c \cdot A_{:,i} - s \cdot A_{:,j}
$$

$$
A'_{:,j} = s \cdot A_{:,i} + c \cdot A_{:,j}
$$

where $c = \cos(\theta)$ and $s = \sin(\theta)$.

## 🧮 Complexity Analysis

By isolating the update to just the affected columns, the algorithm scales linearly with the number of rows $m$. For each of the $m$ rows, the algorithm performs exactly:
* 4 multiplications
* 2 additions/subtractions

**Total Flops:** $\approx 4m$

This reduces the asymptotic computational complexity strictly to **$\mathcal{O}(m)$**, making it highly suitable for large-scale Scientific Computing applications where explicit matrix formation is avoided to conserve memory and CPU cycles.
