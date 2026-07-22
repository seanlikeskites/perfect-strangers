# Block Designs
## Introduction
Solutions to the perfect stranger matching problem take the form of block designs. These are combinatorial structures made
up of a set of "points" $X$ and a collection of subsets of $X$ called "blocks" which satisfy some constraints. In their
application to perfect stranger matching $X$ would be the set of all participants and the blocks the groups these
participants are placed in. In the following discussion the following terms refer to these elements of an experiment:

  * Points -> Participants
  * Blocks -> Groups of participants
  * Block Size -> Number of participants in a group, $\beta$

Under perfect stranger matching conditions, the following principles determine what types of block designs can be used:

  * Any pair of participants appear in the same group together at most once.
  * Every participant should participate in every round.

The first of these can be ensured by choosing block designs where any two blocks intersect at at most one point. To ensure
the second, the block design must be resolvable.

### Resolvable Block Designs
A resolvable block design is one in which the blocks can be partitioned into "parallel classes" where each parallel class
contains every point in $X$ exactly once. In such a design the blocks of a given parallel class give the groups for a single
round of the experiment:

  * Parallel Class -> Round

Designing an experiment with the largest number of rounds is then equivalent to finding a block design with the greatest
number of parallel classes.

## Balanced Incomplete Block Designs
A balanced incomplete block design $\left(\mathrm{BIBD}\right)$ has parameters: $v$, $k$, and $\lambda$. Given a set $X$ of
$v$ points, the design consists of blocks of $k$ points such that each unordered pair of points from $X$ appears in exactly
$\lambda$ blocks. The design is balanced in that each unordered pair of points occurs the same number of times, and
incomplete in that the blocks do not constitute every possible set of $k$ points from $X$. A $\mathrm{BIBD}$ for a given set
of parameters is referred to as a $\left(v, k, \lambda\right)$-$\mathrm{BIBD}$.  If the design is resolvable it is a
$\left(v, k, \lambda\right)$-$\mathrm{RBIBD}$.

For perfect stranger matching applications we consider $\left(v, k, \lambda\right)$-$\mathrm{RBIBD}$s for which:

  * $v = \alpha\beta$
  * $k = \beta$
  * $\lambda = 1$

Setting $\lambda = 1$ ensures perfect stranger matching. If an $\left(\alpha\beta, \beta, 1\right)$-$\mathrm{RBIBD}$ exists
for the given experiment parameters, every participant will meet every other participant exactly once if all possible rounds
are conducted. The maximum number of rounds is therefore equal to the [trivial upper bound](overview#trivial-upper-bound).

For a $\left(v, k, 1\right)$-$\mathrm{RBIBD}$ to exist, $v$ must be divisible by $k$ and $v - 1$ must be divisible by $k -
1$. In terms of experiment parameters that means that $\frac{\alpha\beta - 1}{\beta - 1}$ must be an integer. This does not
guarantee existence of the design however, for example a (36, 6, 1)-$\mathrm{RBIBD}$ does not exist.

A class of easily constructible $\mathrm{RBIBD}$s are the [finite affine planes](finite_planes). A $\left(k^{2}, k,
1\right)$-$\mathrm{RBIBD}$ exists whenever the finite affine plane of order $k$ exists.

### Sub-BIBDs
Given a $\left(v, k, \lambda\right)$-$\mathrm{BIBD}$ with points from the set $X$ and blocks from the set $\mathcal{B}$, a
$\left(v', k, \lambda\right)$-$\mathrm{sub}$-$\mathrm{BIBD}$ is a set of blocks $\mathcal{B}'$ such that:

  * $\mathcal{B}' \subseteq \mathcal{B}$
  * $\mathcal{B}'$ forms a $\mathrm{BIBD}$ on the set of $v'$ points, $X'$.
  * $X' \subseteq X$

If the points from $X$ and blocks from $\mathcal{B}$ form a $\left(v, k, \lambda\right)$-$\mathrm{RBIBD}$ with parallel
classes given by the set of blocks $\mathcal{B}_{0},\mathcal{B}_{1},\dots,\mathcal{B}_{r - 1}$, a $\left(v', k,
\lambda\right)$-$\mathrm{sub}$-$\mathrm{RBIBD}$ is a set of blocks $\mathcal{B}'$ where:

  * $\mathcal{B}'$ forms an $\mathrm{RBIBD}$ on the set of $v'$ points, $X'$.
  * $X' \subseteq X$
  * $\mathcal{B}'$ can be partitioned into parallel classes $\mathcal{B}_{0}',\mathcal{B}_{1}',\dots,\mathcal{B}_{r' - 1}'$.
  * $\mathcal{B}_{i}' \subseteq \mathcal{B}_{i}$ for $0 \leq i < r'$

## Group Divisible Designs
Another type of block design is the Group Divisible Design $\left(\mathrm{GDD}\right)$. A $\mathrm{GDD}$ with parameters
$v$, $J$, $K$, and $\lambda$ is a triple $\left(X, \mathcal{G}, \mathcal{B}\right)$ with the following properties:

  * $X$ is set of $v$ points.
  * $\mathcal{G}$ is a partition of $X$ into subsets called "groups" where $|G| \in J$ for all $G \in \mathcal{G}$.
  * $\mathcal{B}$ is a collection of subsets of $X$ called "blocks" where $|B| \in K$ for all $B \in \mathcal{B}$ and every
    unordered pair of points from different groups occurs in exactly $\lambda$ blocks.
  * Any pair of a group and block intersects at at most one point.

The groups of a $\mathrm{GDD}$ are distinct from the groups of participants in an experiment. To avoid confusion in the rest
of this discussion we will refer to the groups of a $\mathrm{GDD}$ as groups, and groups of participants as participant
groupings. As with $\mathrm{RBIBD}$s above, it is the blocks of the design which correspond to participant groupings.

It is common to refer to a $\mathrm{GDD}$ with certain parameters as a $\left(K, \lambda\right)$-$\mathrm{GDD}$ of a certain
type, where the type defines the number of groups of different sizes. Superscript notation is used to define the type:
$g_{1}^{n_{1}},g_{2}^{n_{2}},\dots,g_{N}^{n_{N}}$ denoting a $\mathrm{GDD}$ with $n_{1}$ groups of size $g_{1}$, $n_{2}$
groups of size $g_{2}$, etc. The total number of points $v$ is therefore equal to the sum $\sum_{i=1}^{N} n_{i}g_{i}$.

A resolvable $\mathrm{GDD}$ $\left(\mathrm{RGDD}\right)$ is one in which the blocks can be partitioned into parallel
classes. For the purposes of perfect stranger matching we will only consider $\mathrm{RGDD}$s for which:

  * All groups are of the same size.
  * All blocks are of the same size.
  * $\lambda = 1$

We refer to such an $\mathrm{RGDD}$ as a $\left(k, 1\right)$-$\mathrm{RGDD}$ of type $g^{n}$: an $\mathrm{RGDD}$ with $n$
groups of size $g$ and blocks of size $k$. 

A $\left(v, k, 1\right)$-$\mathrm{RBIBD}$ can be considered a $\left(k, 1\right)$-$\mathrm{RGDD}$ of type $k^{v/k}$. One of
the parallel classes of the $\mathrm{RBIBD}$ form the groups of the $\mathrm{RGDD}$.

$\mathrm{RGDD}$s can be useful in situations where the number of participants and participant grouping size do not allow a
participant to meet all other participants over the course of an experiment. Take the [social golfer
problem](https://en.wikipedia.org/wiki/Social_golfer_problem) as an example. This is a special case of perfect stranger
matching where $\alpha = 8$ and $\beta = 4$. With 32 total participants this means there are 31 others each individual could
be matched with. 10 rounds are possible in which each individual will match with 3 other participants they have not met
before. This means each individual will match with 30 others over the course of the experiment and never meet the final
participant. A (4, 1)-$\mathrm{RGDD}$ of type 2^16^ provides a [solution to the social golfer
problem](https://www.mathpuzzle.com/MAA/54-Golf%20Tournaments/socgolf1.pdf), the groups of size 2 giving the pairs of
participants who never meet.  **N.B. this construction is yet to be implemented in the perfect-strangers package.**

## Transversal Designs
A transversal design $\left(\mathrm{TD}\right)$ is a type of $\mathrm{GDD}$ with additional properties:

  * All groups are of the same size.
  * All blocks are of the same size.
  * Any pair of a group and block intersects at _exactly_ one point.

A transversal design with groups of size $n$ and blocks of size $k$ is typically written $\mathrm{TD}_{\lambda}(k, n)$. This
is a $\left(k, \lambda\right)$-$\mathrm{GDD}$ of type $n^{k}$ with the additional property that every block intersect every
group at exactly one point.

As with other block designs, a resolvable $\mathrm{TD}$ $\left(\mathrm{RTD}\right)$ is one in which the blocks can be
partitioned into parallel classes. For perfect stranger matching we consider resolvable transversal designs
$\mathrm{RTD}_{1}(\beta, \alpha)$.

$\mathrm{RTD}$s are particularly useful in experiments where we need perfect stranger matching and each participant grouping
should contain one participant from each of a set of classes (these classes may represent different demographic categories for
instance). In such an experiment, the participant classes and groupings would correspond to the groups and blocks of the
$\mathrm{RTD}$ respectively.

The method of [truncating lines of a finite affine plane](finite_planes#truncating-lines), before any submatrix
transposition, provides a way of constructing $\mathrm{RTD}$s. Using this method, the groups of the $\mathrm{RTD}$ are given
by the vertical lines of the finite affine plane.
