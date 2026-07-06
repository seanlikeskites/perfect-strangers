# Column Shift Matching
The column shift matching algorithm used in the perfect-strangers package starts with an initial grouping matrix,
$\mathbf{G}^{(0)}$, for the first round. Grouping matrices for subsequent rounds are constructed by applying circular column
shifts and transpositions to this initial matrix.


## Column Shifts
For all setting of the experiment parameters ($\alpha$ and $\beta$) we can construct an initial sequence of grouping
matrices by applying circular shifts to the columns. For the $n^{\text{th}}$ matrix in this sequence the $j^{\text{th}}$
column of $\mathbf{G}^{(0)}$ is circularly shifted $nj$ positions. **N.B. For mathematical convenience we are defying
mathematical convention here by indexing the columns of the matrix starting at 0.**

To illustrate, consider the following initial grouping matrix:

![Grouping Matrix](../diagrams/column_shift/initial.svg)
/// caption
$\mathbf{G}^{(0)}$
///

The next two matrices in the sequence are as follows. Note that between each matrix in the sequence the column at index 1 is
shifted 1 position and that at position 2 is shifted 2 positions.

<div style="display: flex; justify-content: center;">
  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="One Shift" src="../diagrams/column_shift/one_shift.svg"></p>
      <figcaption>$\mathbf{G}^{(1)}$</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Two Shifts" src="../diagrams/column_shift/two_shifts.svg"></p>
      <figcaption>$\mathbf{G}^{(2)}$</figcaption>
    </figure>
  </div>
</div>

At a minimum we can continue generating new matrices in this way until the element which started at the top of the rightmost
column with index not coprime with $\alpha$ would circle back round to the top when undergoing another shift. The minimum
number of shifts we can apply is given by $\left\lceil\frac{\alpha}{j}\right\rceil - 1$ where $j$ is the index of the
rightmost column for which $\gcd(j, \alpha) > 1$. Including $\mathbf{G}^{(0)}$ this gives a total of
$\left\lceil\frac{\alpha}{j}\right\rceil$ matrices in the sequence.

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
      <p><img alt="Three Shifts" src="../diagrams/column_shift/three_shifts.svg"></p>
      <figcaption>$\mathbf{G}^{(3)}$</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Four Shifts" src="../diagrams/column_shift/four_shifts.svg"></p>
      <figcaption>$\mathbf{G}^{(4)}$</figcaption>
    </figure>
  </div>
</div>

## Transpositions
Where $\alpha$ is divisible by $\beta$ we can apply [submatrix transpotion](submatrix_transposition) to generate additional
rounds.

### Column Shifts After Transposition
At steps of the [submatrix transposition sequence](submatrix_transposition#multiple-sets-of-submatrices) for which
$\frac{\alpha}{b} \geq \beta$ we can apply circular column shifting to generate an additional sequence of grouping matrices.
These shifts are done between the blocks used to construct the submatrices. For the $n^{\text{th}}$ matrix in this sequence
the $j^{\text{th}}$ column of the transposed matrix is circularly shifted $njb$ positions.

Taking the $4{\times}2$ example given in the description of submatrix transposition, an additional grouping matrix can be
constructed by shifting columns of the matrix created by transposition with a block size of 2.

<div style="display: flex; justify-content: center;">
  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Before Transposition" src="../diagrams/submatrix_transposition/submatrix_zero.svg"></p>
      <figcaption>Before Transposition</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Transpiosition" src="../diagrams/column_shift/submatrix_one.svg"></p>
      <figcaption>Transposition </br> $b = 2$</figcaption>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Second Transpiosition" src="../diagrams/column_shift/transpose_and_shift.svg"></p>
      <figcaption>Shifting Between Blocks</figcaption>
    </figure>
  </div>
</div>

The number of column shifts which can be applied to each transposed matrix depends on the number of blocks the matrix has
been split into, $N = \frac{\alpha}{b}$, and the number of participants per group, $\beta$. The minimum number of shifts we
can apply is given by $\left\lceil\frac{N}{j}\right\rceil - 1$ where $j$ is the index of the rightmost column for which
$\gcd(j, \alpha) > 1$. If $\beta$ is less than or equal to the least prime factor of $N$ we can apply $N - 1$ shifts.

## Optimal Cases
Combining the various steps of column shifting and submatrix transposition described above, when $\beta$ is prime and
$\alpha = \beta^{p}$ for some integer power $p$ the maximum sequence length $l_{\max}(\alpha, \beta)$ is  equal to the
[trivial upper bound](./overview.md#trivial-upper-bound). In these cases every participant will appear in a group with every
other participant exactly once.

## Relationship to Finite Affine Planes
When $\alpha$ is a prime, this column shifting method is exactly equivalent to the construction using [finite affine
planes](finite_planes). This is because the circular column shifts are implemented modulo $\alpha$ and when $\alpha$ is
prime the integers modulo $\alpha$ form a field which is isomorphic to the finite field of order $\alpha$.

Whether to use the finite affine plane construction or the column shift approach depends on the number of groups per round,
$\alpha$:

  * When $\alpha$ is prime the two methods are equivalent, as stated above.
  * When $\alpha$ is  positive integer power of a prime $p^{k}$ and $k > 1$ the finite affine plane construction will always
    yield and equal or greater number of rounds.
  * For other values no finite affine planes of order $\alpha$ are known. The column shift approach can still be used in
    these situations to construct a number of rounds as detailed above.
    
