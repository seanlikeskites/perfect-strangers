# MOLS Matching
[Transversal designs](./block_designs#transversal-designs) $\left(\mathrm{TD}\text{s}\right)$ are closely related to
[mutually orthogonal Latin squares](./mols) $\left(\mathrm{MOLS}\right)$. Given a set of $\mathrm{MOLS}$ or $\mathrm{MOLR}$
there are a number of methods one can construct an $\mathrm{RTD}$ or $\mathrm{RTD}$-like design (i.e. a design in which each
block contains exactly one point from each group and a number of parallel classes can be constructed from the blocks).

## One Round per Latin Square / Rectangle
For perfect stranger matching with $\beta \leq \alpha$, one can construct $n + 1$ rounds of participant groupings from $n$
$\mathrm{MOLS}$ of order $\alpha$ all on the same set of symbols. Denote these Latin squares $\mathbf{L}^{0},
\mathbf{L}^{1}, \dots, \mathbf{L}^{n - 1}$.

Begin by creating the first round's grouping matrix $\mathbf{G}^{0}$, assigning participants to groups using any method.
For each Latin square $\mathbf{L}^{m}$ an additional round of the experiment can be constructed. The symbol in the $i$^th^
row and $j$^th^ column of $\mathbf{L}^{m}$ identifies the group that the participant in the $i$^th^ row and $j$^th^ column of
$\mathbf{G}^{0}$ will be in in this round.

Where the Latin squares are on the set of symbols $\mathbb{Z}_{\alpha}$ and $\mathbf{A}(i, j)$ denotes the element at the
$i$^th^ row and $j$^th^ column of the matrix $\mathbf{A}$ (with indices starting at 0), the elements of the grouping matrices
are as follows.

$$
    \mathbf{G}^{m + 1}(i, j) = \mathbf{G}^{0}\left(\mathbf{L}^{m}(i, j), j\right) \; \text{for} \;
    0 \leq m < n \; \text{and} \; 0 \leq i < \alpha \; \text{and} \; 0 \leq j < \beta
$$

A complete set of $\alpha - 1$ $\mathrm{MOLS}$ would yield a full $\mathrm{RTD}\left(\beta, \alpha\right)$: an optimal
solution for typed perfect stranger matching with more than one type of participant.

### Using Latin Rectangles
When $\beta < \alpha$ only the first $\beta$ columns of each Latin square are used in the above construction. This is
equivalent to using using a set of transposed $\mathrm{MOLR}$ to construct the rounds.

Given that is it possible for more $\mathrm{MOLR}$ of size $k{\times}n$ to exist than $\mathrm{MOLS}$ of order $n$, we may
be able to construct more rounds by using Latin rectangles instead of squares. The construction is the same as given above, but
using a transposed Latin rectangle from a set of $\mathrm{MOLR}$ of size $\beta{\times}\alpha$ for each round.


## TD -- MOLS Equivalence

The existence of a $\mathrm{TD}(k, n)$ is equivalent to the existence of a set of $k - 2$  $\mathrm{MOLS}$ or order $n$. Since
an $\mathrm{RTD}(k, n)$ can be attained by removing a group from a $\mathrm{TD}(k + 1, n)$, its existence is equivalent to
the existance of $k - 1$ $\mathrm{MOLS}$ or order $n$.

### RTD Construction
An $\mathrm{RTD}(k, n)$ can be constructed from $k - 1$ $\mathrm{MOLS}$ or order $n$ as follows.

#### Latin Squares
Construct $k - 1$ mutually orthogonal Latin squares of order $n$ on the set of symbols $\mathbb{Z_{n}}$. Denote these
$\mathbf{L}^{0},\mathbf{L}^{1},\dots,\mathbf{L}^{k - 2}$ and let $\mathbf{L}^{m}_{i,j}$ denote the symbol at in the $i$^th^
row and $j$^th^ column of the $m$^th^ Latin square (with indices starting at 0).

#### Transversal Design
From the Latin squares construct a $\mathrm{TD}(k + 1, n)$ on the point set $\mathbb{Z}_{k + 1} \times \mathbb{Z}_{n}$.  The
$n^{2}$ blocks of this design are given by the following sets:

$$
    \left\{(0, i), (1, j)\right\} \cup
    \bigcup_{m = 0}^{k - 2} \left\{\left(m + 2, \mathbf{L}^{m}_{i,j}\right)\right\} \;
    \text{for} \; i,j = 0,1,\dots,n - 1 \\[10pt]
$$

#### Removing a Group
For each $\theta \in \mathbb{Z}_{n}$ we can create a parallel class of an $\mathrm{RTD}(k, n)$. The blocks of the parallel
class are formed by finding every block of the above $\mathrm{TD}(k + 1, n)$ which contains the point $(k, \theta)$ and
removing that point from them. This yields $n$ blocks of size $k$.

#### Grouping Matrices
Associate each experiment participant with a point $(a, b)$ in the set $\mathbb{Z}_{k} \times \mathbb{Z}_{n}$. The above
parallel classes then give the rows of the grouping matrices for the experiment. Participants with equal $a$ values will
belong to the same group of the transversal design (participants of the same type in typed perfect stranger matching)
