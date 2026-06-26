
# Image Compression via Singular Value Decomposition (SVD)

This project demonstrates the practical application of **Singular Value Decomposition (SVD)** in digital image processing using **Julia**. By computing low-rank matrix approximations on a high-resolution, high-contrast RGB image, the algorithm achieves significant file size reduction while evaluating the mathematical and visual trade-offs between lossy compression and image fidelity.

---

## 📐 Mathematical Framework

Any digital image channel can be represented as an $m \times n$ matrix $A$. Through SVD, a matrix of rank $r$ is factored into three distinct matrices:

$$A = U \Sigma V^T$$

Where:
* $U$ is an $m \times m$ orthogonal matrix containing the left singular vectors.
* $\Sigma$ is an $m \times n$ diagonal matrix containing the singular values ($\sigma_i$) sorted in descending order.
* $V^T$ is the transpose of an $n \times n$ orthogonal matrix containing the right singular vectors.

To compress the image, we construct a **rank-$k$ approximation** ($A_k$) by keeping only the top $k$ largest singular values and truncating the rest:

$$A_k = \sum_{i=1}^{k} \sigma_i u_i v_i^T = \sigma_1 u_1 v_1^T + \dots + \sigma_k u_k v_k^T$$

---

## 📊 Memory Allocation & Compression Rates

### Theoretical Formulae
For a color RGB image (which consists of three independent color channels: Red, Green, Blue), the memory storage shifts dramatically after SVD truncation:
* **Original Memory Size:** $3 \times m \times n$ pixels
* **Compressed SVD Memory Size:** $3 \times k(m + n + 1)$ pixels
* **Compression Rate Ratio:** $$\text{Compression Rate} = \left( \frac{k(m + n + 1)}{m \times n} \right) \times 100\%$$

Notice that the factor of 3 cancels out, proving that SVD compression yields the exact same file size reduction efficiency regardless of whether the image is grayscale or RGB.

### Experimental Benchmark ($1733 \times 1300$ Vistula Image)

| Rank ($k$) | Original Memory (pixels) | Compressed Memory (pixels) | Compression Rate (%) | Visual Analysis & Fidelity |
| :---: | :---: | :---: | :---: | :--- |
| **$k = 5$** | 6,758,700 | 45,510 | **0.67%** | Highly blurred; retains only macro-lighting/luminescence info. |
| **$k = 20$** | 6,758,700 | 182,040 | **2.69%** | Noticeable improvement. Horizon and large castle structures are recognizable. |
| **$k = 50$** | 6,758,700 | 455,100 | **6.73%** | Highly sharp for casual viewing; saves **93.27%** of original space. |
| **$k = 120$** | 6,758,700 | 1,092,240 | **16.16%** | Visually lossless; fine architectural details are fully recovered. |

### 📈 Dimensional Scalability Analysis
Assuming a square image matrix ($m \approx n$), the compression rate can be approximated by $\frac{2k}{m}$. Because the dimensions grow quadratically in the denominator, **the SVD compression method becomes exponentially more efficient as the input resolution increases.**

This is empirically verified by comparing two datasets at $k = 50$:
* **Smaller Image (Cats - $640 \times 597$):** Yields a compression rate of **16.19%**.
* **Larger Image (Vistula - $1733 \times 1300$):** Yields a compression rate of just **6.73%**.

---

## 💻 Julia Source Code

The pipeline utilizes Julia's native high-performance linear algebra stack (`LinearAlgebra.jl`) and vectorized broadcasts to process color channels independently.
