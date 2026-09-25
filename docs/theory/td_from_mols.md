# MOLS Matching
A <a style="text-decoration: none;" href="./block_designs#transversal-designs">$\mathrm{TD}(k, n)$</a> can be constructed
from a set of $k - 2$  <a style="text-decoration: none;" href="./mols">$\mathrm{MOLS}$</a> or order $n$. Since an
$\mathrm{RTD}(k, n)$ can be attained by removing a group from a $\mathrm{TD}(k + 1, n)$, one can be constructed from a set
of $k - 1$ $\mathrm{MOLS}$.

## Construction

### Latin Squares
Construct $k - 1$ mutually orthogonal Latin squares of order $n$ on the set of symbols $\mathbb{Z_{n}}$. Denote these
$\mathbf{L}^{0},\mathbf{L}^{1},\dots,\mathbf{L}^{k - 2}$ and let $\mathbf{L}^{m}_{i,j}$ denote the symbol at in the $i$^th^
row and $j$^th^ column of the $m$^th^ Latin square (with indices starting at 0).


### Transversal Design
From the Latin squares construct a $\mathrm{TD}(k + 1, n)$ on the point set $\mathbb{Z}_{k + 1} \times \mathbb{Z}_{n}$.  The
$n^{2}$ blocks of this design are given by the following sets:

$$
    \left\{(0, i), (1, j)\right\} \cup
    \bigcup_{m = 0}^{k - 2} \left\{\left(m + 2, \mathbf{L}^{m}_{i,j}\right)\right\} \;
    \text{for} \; i,j = 0,1,\dots,n - 1 \\[10pt]
$$

### Removing a Group
For each $\theta \in \mathbb{Z}_{n}$ we can create a parallel class of an $\mathrm{RTD}(k, n)$. The blocks of the parallel
class are formed by finding every block of the above $\mathrm{TD}(k + 1, n)$ which contains the point $(k, \theta)$ and
removing that point from them. This yields $n$ blocks of size $k$.


Associate each participants with a point $(a, b)$ in the set $\mathbb{Z}_{k} \times \mathbb{Z}_{n}$. The above parallel
classes then give the rows of the grouping matrices for the experiment. Participants with equal $a$ values will belong to
the same group of the transversal design (participants of the same type in [typed perfect stranger
matching](./overview#typed-perfect-stranger-matching)).

