# Submatrix Transposition
Several matching methods assign groups in such a way that participants in the same column of any of the grouping matrices
are never matched together. This means that for certain shapes of matrix we can employ transposition to generate grouping
matrices for additional rounds.

## Square Matrices
For square matrices (i.e $\alpha = \beta$) transposing $\mathbf{G}^{0}$ gives an additional grouping matrix for the
sequence. 

## Transposing Submatrices
When $\alpha$ is an integer multiple of $\beta$ we can transpose submatrices of $\mathbf{G}^{0}$ to generate a new matrix
in the sequence. For example, consider the following $6{\times}3$ matrix:

<div style="display: flex; justify-content: center;">
  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Before Transposition" src="../diagrams/submatrix_transposition/submatrix_before.svg"></p>
      <figcaption>Before Transposition</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="After Transpiosition" src="../diagrams/submatrix_transposition/submatrix_after.svg"></p>
      <figcaption>After Transposition</figcaption>
    </figure>
  </div>
</div>

## Multiple Sets of Submatrices
When $\alpha$ is divisible by $\beta^{p}$ for some integer power $p$, we can generate a new sequence of $p$ grouping
matrices through the transposition of submatrices.

To produce each grouping matrix in this sequence, first we define a block size $b = \beta$. The sequence is then
constructed iteratively with the following steps: 

  1. Split $\mathbf{G}^{0}$ vertically into $\frac{\alpha}{b}$ blocks of size $b{\times}\beta$.
  2. Split each block into $\frac{b}{\beta}$ submatrices of size $\beta{\times}\beta$ by taking rows spaced
     $\frac{b}{\beta}$ apart.
  3. Transpose each of these $\beta{\times}\beta$ submatrices and place their rows back in the block in the rows the matrix
     was constructed from.
  4. Update $b$ as $b := b\beta$.
  5. If $\alpha$ is divisible by the new value of $b$, return to step 1.

An example sequence for a $4{\times}2$ matrix is shown below. Elements which make up the submatrices being transposed are
boxed in the same colour.

<div style="display: flex; justify-content: center;">
  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Before Transposition" src="../diagrams/submatrix_transposition/submatrix_zero.svg"></p>
      <figcaption>Before Transposition</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="First Transpiosition" src="../diagrams/submatrix_transposition/submatrix_one.svg"></p>
      <figcaption>First Transposition </br> $b = 2$</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Second Transpiosition" src="../diagrams/submatrix_transposition/submatrix_two.svg"></p>
      <figcaption>Second Transposition </br> $b = 4$</figcaption>
    </figure>
  </div>
</div>
