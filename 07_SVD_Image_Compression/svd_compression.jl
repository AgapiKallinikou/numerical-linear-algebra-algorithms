using Images, LinearAlgebra, Plots

# Load the high-resolution RGB image
img = load("Vistula_Original.jpg")
img_float = float.(img)
channels = channelview(img_float)

# Core Low-Rank Approximation Function using SVD
function rank_approx(F::SVD, k)
    U, S, V = F
    k = min(k, size(U, 2), size(V, 2))
    M = U[:, 1:k] * Diagonal(S[1:k]) * V[:, 1:k]'
    clamp01!(M)
    return M
end

# Compute SVD for each color channel (Red, Green, Blue) independently
svdfactors = svd.(eachslice(channels, dims=1))

# Generate compressed images for different rank (k) values
ks = [5, 20, 50, 120]
imgs = map(ks) do k
    colorview(RGB, rank_approx.(svdfactors, k)...)
end

# Save the original and compressed versions side-by-side as a mosaic
save("Vistula_Compressed_Mosaic.jpg", mosaicview(img, imgs..., nrow=1, npad=10))
