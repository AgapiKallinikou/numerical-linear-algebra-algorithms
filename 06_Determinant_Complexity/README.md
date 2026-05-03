# Determinant Calculation: Algorithmic Complexity

This section investigates the computational complexity of different algorithms for calculating the determinant of a non-singular matrix $A \in \mathbb{R}^{n \times n}$. We compare the highly efficient Gaussian Elimination approach with the mathematically intuitive but computationally explosive Laplace expansion.

---

## 1. Gaussian Elimination with Partial Pivoting (DetGEP)

The `DetGEP` algorithm computes the determinant by transforming the matrix into an upper triangular form using Gaussian elimination. The determinant of an upper triangular matrix is simply the product of its main diagonal elements. 

Since row swaps (partial pivoting) flip the sign of the determinant, we track the number of permutations to adjust the final sign.

### 🧮 Complexity Analysis
The most demanding part of the algorithm consists of three nested loops during the elimination phase.
* The outer loop for pivots runs $n - 1$ times.
* The row loop runs $n - k$ times.
* The inner column loop runs $n - k + 1$ times.

The inner operation $A[i,j] \leftarrow A[i,j] - m_{ik} \times A[k,j]$ costs 1 flop. The total number of floating-point operations (flops) is:

$$
\text{Flops} \approx \sum_{k=1}^{n-1} \sum_{i=k+1}^{n} \sum_{j=k}^{n} 1 \approx \sum_{k=1}^{n-1} (n - k)^2
$$

By setting $m = n - k$, we sum the squares of the first $n - 1$ integers:

$$
\sum_{m=1}^{n-1} m^2 = \frac{(n - 1)n(2n - 1)}{6} = \frac{2n^3 - 3n^2 + n}{6}
$$

For large $n$, the dominant term determines the complexity:

$$
\text{Flops} \approx \frac{n^3}{3}
$$

Thus, the asymptotic time complexity of `DetGEP` is strictly **$\mathcal{O}(n^3)$**.

---

## 2. Laplace Expansion (DetLaplace)

The `DetLaplace` algorithm computes the determinant using a recursive mathematical definition. To find the determinant of an $n \times n$ matrix, it requires calculating the determinants of $n$ submatrices of size $(n-1) \times (n-1)$, continuing down to $1 \times 1$ matrices.

### 🧮 Complexity Analysis
Let $T(n)$ be the total flops required. The recursive step requires $n$ calls to submatrices, $n$ multiplications, and $n - 1$ additions:

$$
T(n) = n \cdot T(n - 1) + 2n - 1
$$

Unrolling this inequality $T(n) > n \cdot T(n - 1)$ yields:

$$
T(n) > n \cdot (n - 1) \cdot (n - 2) \cdots 2 \cdot 1 \cdot T(1)
$$

Since $n \cdot (n - 1) \cdots 1 = n!$, the computational complexity of the Laplace expansion is strictly **$\mathcal{O}(n!)$**.

---

## 3. Execution Time Benchmarks (Theory vs Reality)

To understand the practical implications of $\mathcal{O}(n^3)$ vs $\mathcal{O}(n!)$, assume a computer that executes 1 flop in $10^{-5}$ seconds. 
Using Stirling's approximation for large factorials: $n! \approx \sqrt{2\pi n} (n/e)^n$.

### ⚡ DetGEP ($\mathcal{O}(n^3)$)
* **$n = 100$:** $\approx 3.33$ seconds
* **$n = 1000$:** $\approx 55.5$ minutes
* **$n = 5000$:** $\approx 4.8$ days

### 🐢 DetLaplace ($\mathcal{O}(n!)$)
* **$n = 12$:** $\approx 1.33$ hours
* **$n = 13$:** $\approx 17.3$ hours
* **$n = 100$:** $\approx 9.32 \times 10^{152}$ seconds *(Vastly exceeds the age of the universe, which is $\approx 4.3 \times 10^{17}$ seconds)*.

**Conclusion:** The mathematical elegance of Laplace expansion makes it a terrible algorithmic choice. It is realistically applicable only for very small matrices ($n \le 11$). For all practical engineering applications, factorization methods like GEP are mandatory.
