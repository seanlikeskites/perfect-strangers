# Kirkman Triple Matching
A Kirkman Triple System is a <a style="text-decoration: none;"
href="./block_designs#balanced-incomplete-block-designs">$\left(v, 3, 1\right)$-$\mathrm{RBIBD}$ </a> named for [Kirkman's
schoolgirl problem](https://en.wikipedia.org/wiki/Kirkman%27s_schoolgirl_problem): a special case of perfect stranger
matching where $\alpha = 5$ and $\beta = 3$. It was shown by Ray-Chaudhuri and Wilson (1971)[^1] that such systems are
constructible where the total number of elements is an odd multiple of 3. This is equivalent to saying that
$l_{\max}(\alpha, 3)$ is equal to the [trivial upper bound](./overview.md#trivial-upper-bound) when $\alpha$ is odd.

## Constructions
Ray-Chaudhuri and Wilson (1971) detail several theorems which can be used to construct Kirkman triple systems for different
cases. Those described here are the ones which are currently implemented as part of the perfect-strangers package (hopefully
one day I'll get round to implementing them all).

### Composition Theorems
Theorems 3 and 4 from Ray-Chaudhuri and Wilson (1971) provide constructions for Kirkman triple systems based on the
composition of [balanced incomplete block designs](./block_designs#balanced-incomplete-block-designs) of smaller sizes and
[resolvable orthogonal arrays](./orthogonal_arrays).

#### Theorem 4
Theorem 4 is the technique used for <a style="text-decoration: none;" href="./sub_bibd">$\mathrm{Sub}$-$\mathrm{RBIBD}$
matching</a>.

### Primitive Element Theorems
Theorems 5 and 6 from Ray-Chaudhuri and Wilson (1971) are instances of [primitive element
constructions](./primitive_element).


[^1]: Ray-Chaudhuri, D.K. and Wilson, R.M., 1971. Solution of Kirkman’s schoolgirl problem. In Proc. symp. pure Math (Vol.
  19, pp. 187-203). DOI: [10.1090/pspum/019/9959](https://doi.org/10.1090/pspum/019/9959)
