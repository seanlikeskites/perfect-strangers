# Column Shift Matching
The column shift matching algorithm used in the perfect-strangers package starts with an initial grouping matrix,
$\mathbf{G}^{(0)}$, for the first round. Grouping matrices for subsequent rounds are constructed by applying circular column
shifts and transpositions to this initial matrix.


## Column Shifts
For all setting of the experiment parameters ($\alpha$ and $\beta$) we can construct an initial sequence of grouping
matrices by applying circular shifts to the columns. For the $n^{\text{th}}$ matrix in this sequence the $j^{\text{th}}$
column of $\mathbf{G}^{(0)}$ is circularly shifted $nj$ positions. **N.B. We are defying mathematical convention here by
indexing the columns of the matrix starting at 0.**

To illustrate, consider the following initial grouping matrix:

![Grouping Matrix](../../diagrams/column_shift/initial.svg)
/// caption
$\mathbf{G}^{(0)}$
///

The next two matrices in the sequence are as follows. Note that between each matrix in the sequence the column at index 1 is
shifted 1 position and that at position 2 is shifted 2 positions.

<div style="display: flex; justify-content: center;">
  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="One Shift" src="../../diagrams/column_shift/one_shift.svg"></p>
      <figcaption>$\mathbf{G}^{(1)}$</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Two Shifts" src="../../diagrams/column_shift/two_shifts.svg"></p>
      <figcaption>$\mathbf{G}^{(2)}$</figcaption>
    </figure>
  </div>
</div>

At a minimum we can continue generating new matrices in this way until the element which started at the top of the final
column would circle back round to the top when undergoing another shift. The minimum number of shifts we can apply is given
by $\left\lceil\frac{\alpha}{\beta - 1}\right\rceil - 1$. Including $\mathbf{G}^{(0)}$ this gives a total of
$\left\lceil\frac{\alpha}{\beta - 1}\right\rceil$ matrices in the sequence.

### Additional Shifts
Under certain conditions we can allow the top element of the final column to circle back to the top. If all the integers
between 0 and $\beta - 1$ are coprime with $\alpha$ (i.e. $\beta$ is less than or equal to the least prime factor of $\alpha$)
we can continue applying shifts until we get back to $\mathbf{G}^{(0)}$. This allows for a total sequence length of $\alpha$
after applying all shifts.

In our example $\alpha = 5$ and $\beta = 3$, which are coprime. We can therefore continue shifting to generate 2 more valid
grouping matrices.

<div style="display: flex; justify-content: center;">
  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Three Shifts" src="../../diagrams/column_shift/three_shifts.svg"></p>
      <figcaption>$\mathbf{G}^{(3)}$</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Four Shifts" src="../../diagrams/column_shift/four_shifts.svg"></p>
      <figcaption>$\mathbf{G}^{(4)}$</figcaption>
    </figure>
  </div>
</div>

## Transpositions
For certain shapes of matrix we can also employ transposition to generate new matrices in the sequence.

### Square Matrices
For square matrices (i.e $\alpha = \beta$) transposing $\mathbf{G}^{(0)}$ gives an additional grouping matrix for the
sequence. 

### Transposing Submatrices
When $\alpha$ is an integer multiple of $\beta$ we can transpose submatrices of $\mathbf{G}^{(0)}$ to generate a new matrix
in the sequence. For example, consider the following $6{\times}3$ matrix:

<div style="display: flex; justify-content: center;">
  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Before Transposition" src="../../diagrams/column_shift/submatrix_before.svg"></p>
      <figcaption>Before Transposition</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="After Transpiosition" src="../../diagrams/column_shift/submatrix_after.svg"></p>
      <figcaption>After Transposition</figcaption>
    </figure>
  </div>
</div>

### Multiple Sets of Submatrices
When $\alpha$ is divisible by $\beta^{p}$ for some integer power $p$, we can generate a new sequence of $p$ grouping
matrices through the transposition of submatrices.

To produce each grouping matrix in this sequence, first we define a block size $b = \beta$. The sequence is then
constructed iteratively with the following steps: 

  1. Split $\mathbf{G}^{(0)}$ vertically into $\frac{\alpha}{b}$ blocks of size $b{\times}\beta$.
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
      <p><img alt="Before Transposition" src="../../diagrams/column_shift/submatrix_zero.svg"></p>
      <figcaption>Before Transposition</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="First Transpiosition" src="../../diagrams/column_shift/submatrix_one.svg"></p>
      <figcaption>First Transposition </br> $b = 2$</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Second Transpiosition" src="../../diagrams/column_shift/submatrix_two.svg"></p>
      <figcaption>Second Transposition </br> $b = 4$</figcaption>
    </figure>
  </div>
</div>

### Column Shifts After Transposition
At steps of the submatrix transposition sequence for which $\frac{\alpha}{b} \geq \beta$ we can apply circular column
shifting to generate an additional sequence of grouping matrices. These shifts are done between the blocks used to construct
the sub matrices. For the $n^{\text{th}}$ matrix in this sequence the $j^{\text{th}}$ column of the transposed matrix is
circularly shifted $njb$ positions.

For the first transposition step illustrated above (when $b = 2$) the second column of the matrix can be circularly shifted
2 positions to generate a new grouping matrix.

![Grouping Matrix](../../diagrams/column_shift/transpose_and_shift.svg)
/// caption
///

The number of column shifts which can be applied to each transposed matrix depends on the number of blocks the matrix has
been split into, $N = \frac{\alpha}{b}$, and the number of participants per group, $\beta$. The minimum number of shifts we can apply is given
by $\left\lceil\frac{N}{\beta - 1}\right\rceil - 1$. If $\beta$ is less than or equal to the least prime factor of $N$ we
can apply $N - 1$ shifts.

### Optimal Cases
Combining the various steps of column shifting and submatrix transposition described above, when $\beta$ is prime and
$\alpha = \beta^{p}$ for some integer power $p$ the maximum sequence length $l_{\max}(\alpha, \beta)$ is  equal to the
[trivial upper bound](./overview.md#trivial-upper-bound). In these cases every participant will appear in a group with every
other participant exactly once.
