# Finite Affine Plane Matching

## Finite Affine Planes
A finite affine plane of order $n$ is a geometric system which consists of:

  * A set of $n^{2}$ points.
  * A set of $n^{2} + n$ lines such that:
    - Each line contains $n$ points.
    - Each point is on $n + 1$ lines.
    - Each distinct pair of point appears on exactly one line.
    - Given a line $l$ and a point $p$ not on $l$, there is exactly one other line $l'$ which contains $p$ and is parallel to $l$
      (i.e. $l$ and $l'$ do not intersect).
    - There exist 4 points such that no three of them sit on the same line.

Below is a diagram of a finite affine plane of order 3:

![Finite Affine Plane](../diagrams/finite_planes/finite_affine_plane.svg)
/// caption
Finite Affine Plane of order 3. Each set of coloured lines represents a set of parallel lines which cover every point in the
plane.
///

### Construction
If the finite field $\mathbb{F}_{q}$ exists, we can construct a finite affine plane of order $q$ by defining points with
coordinates $(x, y)$ for $x,y \in \mathbb{F}_{q}$.

For each gradient $m \in \mathbb{F}_{q}$ we can define a set of parallel lines, each line joining all the points with
coordinates satisfying the standard equation of a straight line.

$$
    y = mx + c
$$

Each set contains $q$ lines, one for each $y$-intercept $c \in \mathbb{F}_{q}$. This gives us a total of $q^{2}$ lines in
$q$ sets.

The final set of parallel lines are the vertical lines (those with infinite gradient). For each $x \in \mathbb{F}_{q}$ a
line is constructed though the points $(x, y)$ for every $y \in \mathbb{F}_{q}$.

Given that $\mathbb{F}_{q}$ only exists when $q$ is a positive integer power of a prime, this construction only works under
those conditions.

## Perfect Stranger Matching with Finite Affine Planes
The geometry of finite affine planes proves useful in solutions to the problem of perfect stranger matching. Given the
following properties of perfect stranger matching:

  * Each round should include every participant.
  * Participants should never meet more than once.

There are mirrored by the properties of finite affine planes:

  * Each set of parallel lines covers every point in the plane.
  * Any two lines in the plane intersect at no more than one point.

### Square Matrices
When $\alpha = \beta$ and $\alpha$ is a positive integer power of a prime, the finite affine plane of order $\alpha$ can be
used to construct a sequence of grouping matrices.

Associate each participant with a point in the plane. Each set of parallel lines in the plane then gives the grouping matrix
for one round, the lines in the set defining the rows of the matrix.

Under this construction we get grouping matrices for $\alpha + 1$ rounds, equal to the [trivial upper
bound](./overview.md#trivial-upper-bound).

### Truncating Lines
When $\beta < \alpha$ and $\alpha$ is a positive integer power of a prime, we can truncate the lines of the finite affine
plane of order $\alpha$ to construct grouping matrices.

Associate each participant with a point in the plane $(x, y)$ where $x$ is taken from the first $\beta$ elements of
$\mathbb{F}_{\alpha}$ and $y \in \mathbb{F}_{\alpha}$. $\alpha$ grouping matrices can then be constructed from the sets of lines
satisfying the equation $y = mx + c$ by taking the first $\beta$ points from each line for each row.

Because this method only uses the first $\beta$ elements of $\mathbb{F}_{\alpha}$ for $x$ coordinates, it cannot readily use the
vertical lines of the plane. Only $\beta$ vertical lines from the plane use this subset of $x$ coordinates which is
insufficient for a full grouping matrix.

#### Using the Vertical Lines
Where $\alpha$ is an integer multiple of $\beta$ we can partition the vertical lines of the plane in such a way as to
generate additional grouping matrices. The columns of the grouping matrices constructed through truncation of lines in the
finite affine plane correspond to the first $\beta$ vertical lines in that plane. As such, [submatrix
transposition](submatrix_transposition) serves as a method of partitioning these vertical lines.

Given that construction of the finite affine plane requires $\alpha$ be a prime power $p^{k}$, the divisibility of $\alpha$
by $\beta$ implies that $\beta$, and the block size $b$ and number of blocks $N = \frac{\alpha}{b}$ in the [submatrix
transposition sequence](submatrix_transposition#multiple-sets-of-submatrices), are also powers of the same prime. At steps
for which $N \geq \beta$ the finite affine plane of order $N$ can be used to rearrange the vertical lines of
$\mathbb{F}_{\alpha}$ to generate additional rounds after transposition.

Construct $b$ matrices of size $N{\times}\beta$ by taking rows at the same position from each of the blocks used in
submatrix transposition, e.g. the first of these matrices is formed by combining the first row of each block.
The lines of $\mathbb{F}_{N}$ can then be applied to each of these matrices to define additional groups for subsequent
rounds in our sequence of grouping matrices: a complete round being compiled from the groups constructed from each
$N{\times}\beta$ matrix and the same set of parallel lines from $\mathbb{F}_{N}$.
