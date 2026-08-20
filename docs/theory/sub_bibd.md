# Sub-RBIBD Matching
Theorem 4 from [Ray-Chaudhuri and Wilson (1971)](https://doi.org/10.1090%2Fpspum%2F019%2F9959) states that an $\left(m(v_{1}
- 1) + v_{2}, k, 1\right)$-$\mathrm{RBIBD}$ can be constructed from the following elements:

  * A <a style="text-decoration: none;" href="./block_designs#balanced-incomplete-block-designs">$(v_{1}, k, 1)$-$\mathrm{RBIBD}$</a>
  * An $(m(k - 1) + v_{2}, k, 1)$-$\mathrm{RBIBD}$ with a <a style="text-decoration: none;"
    href="./block_designs#sub-rbibds">$(v_{2}, k, 1)$-$\mathrm{sub}$-$\mathrm{RBIBD}$</a> $\left(\text{or }v_{2} = 1\right)$.
  * An <a style="text-decoration: none;" href="./orthogonal_arrays#resolvable-orthogonal-arrays">$\mathrm{ROA}\left(m^{2}, k, m, 2\right)$</a>[^1]

[^1]: Ray-Chaudhuri and Wilson use different notation for resolvable orthogonal arrays: referring to an
  $\mathrm{ROA}\left(N, k, v, t\right)$ as an $(m, n, d, \lambda)$-resolvable orthogonal array, where $m = k$, $n = N$, $d =
  t$, and $\lambda = N/v^{t}$.

## Construction
### Point Set
The end result of this construction is an $\mathrm{RBIBD}$ on the set of points $X^{*}$. The points of this set are defined
from the points of three other sets:

  * $X$: a set of $v_{1}$ points.
  * $Y$: a set of $v_{2}$ points.
  * $\mathbb{Z}_{m}$: the set of integers from 0 to $m - 1$.

First we define $\theta$ to be a fixed point from $X$. Removing this point from $X$ yields the set $X'$, i.e.  $X' = X -
\{\theta\}$. The full set of points for the $\mathrm{RBIBD}$ under construction is then:

$$
  X^{*} = X' \times \mathbb{Z}_{m} \cup Y
$$

This set has $m(v_{1} - 1) + v_{2}$ elements, hence the $\mathrm{RBIBD}$ under construction is an $\left(m(v_{1} - 1) +
v_{2}, k, 1\right)$-$\mathrm{RBIBD}$.

For perfect stranger matching we associate each of the experiment participants with a point in the set $X^{*}$.

### Construction Elements
#### • $(v_{1}, k, 1)$-$\mathrm{RBIBD}$ 
Construct $\left(X, \mathcal{B}\right)$, a $(v_{1}, k, 1)$-$\mathrm{RBIBD}$ on the point set $X$ with the set of blocks $\mathcal{B}$. This
$\mathrm{RBIBD}$ has $r_{1} = \frac{v_{1} - 1}{k - 1}$ parallel classes, denoted
$\mathcal{B}_{0},\mathcal{B}_{1},\dots,\mathcal{B}_{r_{1} - 1}$.

Let $B_{i}$ denote the block from the parallel class $\mathcal{B}_{i}$ which contains the fixed point $\theta$. Then let
$B_{i}'$ denote this block with $\theta$ removed, i.e. $B_{i}' = B_{i} - \{\theta\}$.

#### • $(m(k - 1) + v{2}, k, 1)$-$\mathrm{RBIBD}$
For each of the blocks $B_{i}'$ from the parallel classes of $\left(X, \mathcal{B}\right)$, define the point set ${Q^{i} =
B_{i}' \times \mathbb{Z}_{m} + Y}$. Construct $\left(Q^{i}, \mathcal{S}^{i}\right)$, an ${(m(k - 1) + v_{2}, k, 1)}$-$\mathrm{RBIBD}$
on this point set, with the set of blocks $\mathcal{S}^{i}$. Each of these $\mathrm{RBIBD}$s has $r_{2} + m$ parallel
classes, where $r_{2} = \frac{v_{2} - 1}{k - 1}$. We denote these parallel classes
$\mathcal{S}^{i}_{0},\mathcal{S}^{i}_{1},\dots,\mathcal{S}^{i}_{r_{2} + m - 1}$.

#### • $(v_{2}, k, 1)$-$\mathrm{sub}$-$\mathrm{RBIBD}$ 
When $v_{2} > 1$ the construction requires that each of the $\mathrm{RBIBD}$s, $\left(Q^{i}, \mathcal{S}^{i}\right)$, have a $(v_{2}, k,
1)$-$\mathrm{sub}$-$\mathrm{RBIBD}$ on the set of points $Y$. Since $Y \subset Q^{i}$ this is the same
$\mathrm{sub}$-$\mathrm{RBIBD}$ for all $i = 0,1,\dots,r_{2} + m - 1$. Denote this $\mathrm{sub}$-$\mathrm{RBIBD}$ $\left(Y,
\mathcal{S}'\right)$ and denote its $r_{2}$ parallel classes $\mathcal{S}_{0}',\mathcal{S}_{1}',\dots,\mathcal{S}_{r_{2} -
1}'$, where ${\mathcal{S}_{j}' \subset \mathcal{S}^{i}_{j}}$.

Further, let $\mathcal{V}^{i}_{j}$ be the set of blocks from $\mathcal{S}^{i}_{j}$ which are not in $\mathcal{S}_{j}'$. That
is:

$$
  \mathcal{V}^{i}_{j} = \mathcal{S}^{i}_{j} - \mathcal{S}_{j}' \quad \text{for} \; j = 0,1,\dots,r_{2} - 1
$$

The remaining $S^{i}_{j}$ for $j = r_{2},r_{2} + 1,\dots,r_{2} + m - 1$ are the parallel classes from $\left(Q^{i},
\mathcal{S}^{i}\right)$ which are not supersets of a parallel class from $\left(Y, \mathcal{S}'\right)$. For convenience we
will denote these parallel classes $\mathcal{W}^{i}_{j}$, where:

$$
  \mathcal{W}^{i}_{j} = S^{i}_{j + r_{2}} \quad \text{for} \; j = 0,1,\dots,m - 1
$$

#### • $\mathrm{ROA}\left(m^{2}, k, m, 2\right)$
Construct an orthogonal array of type $\left(m^{2}, k, m, 2\right)$ with elements taken from the set $\mathbb{Z}_{m}$ which can be
resolved into $m$ orthogonal arrays of type $(m, k, m, 1)$. Denote these smaller orthogonal arrays
$\mathbf{P}^{0},\mathbf{P}^{1},\dots,\mathbf{P}^{m - 1}$.

Further, for a given block of $k$ points, $B$, let $\mathcal{P}_j(B)$ denote the set of blocks constructed from the rows of
$\mathbf{P}^{j}$ and the points in $B$ as follows. Each $\mathcal{P}_j(B)$ contains $m$ blocks, the blocks being given by:

$$
  \left\{\left( b_{n}, \mathbf{P}^{j}_{i,n} \right) \Big| \; n \in \mathbb{Z} \land 0 \leq n < k \right\} \quad
    \text{for} \; i = 0,1,\dots,m - 1
$$

Where $\mathbf{P}^{j}_{i,n}$ is the element in the $i^{\text{th}}$ row and $n^{\text{th}}$ column of $\mathbf{P}^{j}$ (with
indices starting at 0), and $b_{n}$ is the $n^{\text{th}}$ element of $B$.

### Grouping Matrices
The above components can be used to construct the $mr_{1} + r_{2}$ parallel classes of blocks for an $(m(v_{1} - 1) + v_{2},
k, 1)$-$\mathrm{RBIBD}$ on the point set $X'$. These parallel classes give the grouping matrices for the experiment
participants. Parallel classes are constrcuted using two different methods.

#### From Sub-RBIBD
The first $r_{2}$ parallel classes are constructed from the parallel classes of the $\mathrm{sub}$-$\mathrm{RBIBD}$
$\left(Y, \mathcal{S}'\right)$ and the sets of blocks $\mathcal{V}^{i}_{j}$ as follows:

$$
  \mathcal{E}_{j} = \mathcal{S}_{j}' \cup \bigcup_{i = 0}^{r_{1} - 1} \mathcal{V}^{i}_{j} \quad \text{for} \; j =
  0,1,\dots,r_{2} - 1
$$

#### From Orthogonal Array
The remaining $mr_{1}$ parallel classes are constructed from the orthogonal arrays and parallel classes
$\mathcal{S}^{i}_{j}$ as follows:

$$
  \mathcal{H}_{j}^{i} = \mathcal{W}^{i}_{j} \cup \bigcup_{B \in \mathcal{B}_{i}, B \neq B_{i}} \mathcal{P}_{j}(B) \quad \text{for}
      \; j = 0,1,\dots,m - 1 \; \text{and} \; i = 0,1,\dots,r_{1} - 1
$$

### Sub-RBIBDs
$\mathrm{RBIBD}$s constructed using this method contain $\mathrm{sub}$-$\mathrm{RBIBDS}$ on different sets of points.

#### On the Set of Points $Y$
Parallel classes of a $(v_{2}, k, 1)$-$\mathrm{sub}$-$\mathrm{RBIBD}$ on the set of points $Y$ are given by the sets of
blocks:

$$
  \mathcal{S}_{j}' \quad \text{for} \; j = 0,1,\dots,r_{2} - 1
$$

#### On the Set of points $Q^{i}$
For any given $i$ from 0 to $r_{1} - 1$, parallel classes of a $(m(k - 1) + v_{2}, k, 1)$-$\mathrm{sub}$-$\mathrm{RBIBD}$ on
the set of points $Q^{i}$ are given by the sets of blocks:

$$
  \mathcal{S}^{i}_{j} \quad \text{for} \; j = 0,1,\dots,r_{2} + m - 1
$$
