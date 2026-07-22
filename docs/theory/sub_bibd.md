# Sub-BIBD Matching
Theorem 4 from [Ray-Chaudhuri and Wilson (1971)](https://doi.org/10.1090%2Fpspum%2F019%2F9959) states that an $\left(m(v_{1}
- 1) + v_{2}, k, 1\right)$-$\mathrm{RBIBD}$ can be constructed from the following elements:

  * A <a style="text-decoration: none;" href="./block_designs#balanced-incomplete-block-designs">$(v_{1}, k, 1)$-$\mathrm{RBIBD}$</a>
  * An $(m(k - 1) + v_{2}, k, 1)$-$\mathrm{RBIBD}$ with a <a style="text-decoration: none;"
    href="./block_designs#sub-rbibds">$(v_{2}, k, 1)$-$\mathrm{sub}$-$\mathrm{RBIBD}$</a> $\left(\text{or }v_{2} = 1\right)$.
  * An <a style="text-decoration: none;" href="./orthogonal_arrays#resolvable-orthogonal-arrays">$\mathrm{ROA}\left(m^{2}, k, m, 2\right)$</a>[^1]

[^1]: Ray-Chaudhuri use different notation for resolvable orthogonal arrays: referring to an $\mathrm{ROA}\left(N, k, v,
  t\right)$ as an $(m, n, d, \lambda)$-resolvable orthogonal array, where $m = k$, $n = N$, $d = t$, and $\lambda = N/v^{t}$.

## Construction
### Point Set
The end result of this construction is an $\mathrm{RBIBD}$ on the set of points $X^{*}$. The points of this set are defined
from the points of three other sets:

  * $X$: a set of $v_{1}$ points.
  * $Y$: a set of $v_{2}$ points.
  * $I_m$: the set of integers from 1 to $m$.

First we define $\theta$ to be one of the points from $X$. Removing this point from $X$ yields the set $X'$, i.e.  $X' = X -
\{\theta\}$. The full set of points for the $\mathrm{RBIBD}$ being constructed is then:

$$
  X^{*} = X' \times I_{m} \cup Y
$$

This set has $m(v_{1} - 1) + v_{2}$ elements, hence the $\mathrm{RBIBD}$ under construction is an $\left(m(v_{1} - 1) +
v_{2}, k, 1\right)$-$\mathrm{RBIBD}$.

For perfect stranger matching we associate each of the experiment participants with a point in the set $X^{*}$.

### RBIBDS

