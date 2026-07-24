# Kirkman Triple Matching
A Kirkman Triple System is a <a style="text-decoration: none;"
href="./block_designs#balanced-incomplete-block-designs">$\left(v, 3, 1\right)$-$\mathrm{RBIBD}$ </a> named for [Kirkman's
schoolgirl problem](https://en.wikipedia.org/wiki/Kirkman%27s_schoolgirl_problem): a special case of perfect stranger
matching where $\alpha = 5$ and $\beta = 3$. It was shown by [Ray-Chaudhuri and Wilson
(1971)](https://doi.org/10.1090%2Fpspum%2F019%2F9959) that such systems are constructible where the total number of elements
is an odd multiple of 3. This is equivalent to saying that $l_{\max}(\alpha, 3)$ is equal to the [trivial upper
bound](./overview.md#trivial-upper-bound) when $\alpha$ is odd.

## Constructions
Ray-Chaudhuri and Wilson (1971) detail several theorems which can be used to construct Kirkman triple systems for different
cases. Those described here are the ones which are currently implemented as part of the perfect-strangers package (hopefully
one day I'll get round to implementing them all).

### Composition Theorems
Theorems 3 and 4 from Ray-Chaudhuri and Wilson (1971) provide constructions for Kirkman triple systems base on the
composition of [balanced incomplete block designs](./block_designs#balanced-incomplete-block-designs) of smaller sizes and
[resolvable orthogonal arrays](./orthogonal_arrays).

#### Theorem 4
Theorem 4 is the technique used for <a style="text-decoration: none;" href="./sub_bibd">$\mathrm{Sub}$-$\mathrm{RBIBD}$
matching</a>.

### Finite Field Arithmetic
Let $q$ be a prime power of the form $6t + 1$, where $t$ is an integer. Theorems 5 and 6 from Ray-Chaudhuri and Wilson
(1971) give constructions for Kirkman triple systems of order $3q$ and $2q + 1$. These constructions are based on arithmetic
in $\mathbb{F}_{q}$, the finite field of order $q$. In addition, let $g$ be a primitive element of $\mathbb{F}_{q}$.
Depending on the total number of participants, $\alpha\beta$, we use a different theorem to construct our grouping matrices.

  * When $\alpha\beta = 3q$: [Theorem 5](#theorem-5)
  * When $\alpha\beta = 2q + 1$: [Theorem 6](#theorem-6)

#### Theorem 5
When $\alpha\beta = 3q$ each participant can be uniquely identified by a label of the form $(x, y)$ where $x$ is an element
from $\mathbb{F}_{q}$ and $y$ is in integer in the set $\{1, 2, 3\}$. To construct grouping matrices we define the following
families of triples, where $a$ is any element of $\mathbb{F}_{q}$:

$$
    A_{0}(a) = \left\{\left(a, 1\right), \left(a, 2\right), \left(a, 3\right)\right\} \\[10pt]
    B_{j}^{i}(a) = \left\{\left(g^{i} + a, j\right), \left(g^{i + 2t} + a, j\right), \left(g^{i + 4t} + a, j\right)\right\} \;
        \text{for} \; i = 0,1,\dots,t - 1 \; \text{and} \; j = 1,2,3 \\[10pt]
    A^{i}(a) = \left\{\left(g^{i} + a, 1\right), \left(g^{i + 2t} + a, 2\right), \left(g^{i + 4t} + a, 3\right)\right\} \;
        \text{for} \; i = 0,1,\dots,6t - 1
$$

The first $q$ grouping matrices in our sequence are each constructed using a different element $a$ from $\mathbb{F}_{q}$.
The rows of each matrix are the triples: 

  * $A_{0}(a)$
  * $B_{j}^{i}(a)$ for all values of $i$ and $j$
  * $A_{i}(a)$ where $\left\lfloor i/t \right\rfloor$ is odd.

An additional $3t$ grouping matrices can be constructed for each $i$ for which $\left\lfloor i/t \right\rfloor$ is even. The
rows of each matrix are the triples $A_{i}(a)$ for all values of $a$ from $\mathbb{F}_{q}$.

This gives a total of $q + 3t = 9t + 1$ grouping matrices under perfect stranger matching conditions. In such an experiment
$\alpha = q$ and $\beta = 3$, so the trivial upper bound for number of rounds would be:

$$
	l_{\max}(\alpha, \beta) = \left\lfloor\frac{3q - 1}{3 - 1}\right\rfloor = \left\lfloor\frac{18t + 2}{2}\right\rfloor =
    9t + 1
$$

Hence this method gives a number of rounds equal to the trivial upper bound.

#### Theorem 6
When $\alpha\beta = 2q + 1$ the first $2q$ participants are identified by a label of the form $(x, y)$ where $x$ is an
element of $\mathbb{F}_{q}$ and $y$ is an integer from the set $\{1, 2\}$. The final participant is given the label
$\infty$. Grouping matrices are constructed from the following families of triples, where $m$ is a value such that $2g^{m} =
g^{t} + 1$:

$$
    A_{0}(a) = \left\{\left(a, 1\right), \left(a, 2\right), \infty)\right\} \\[10pt]
    B_{j}^{i}(a) = \left\{\left(g^{i + 2jt} + a, 1\right), \left(g^{i + 2jt + t} + a, 1\right), \left(g^{i + 2jt + m} + a, 2\right)\right\} \;
        \text{for} \; i = 0,1,\dots,t - 1 \; \text{and} \; j = 0,1,2 \\[10pt]
    A^{i}(a) = \left\{\left(g^{i + m + t} + a, 2\right), \left(g^{i + m + 3t} + a, 2\right), \left(g^{i + m + 5t} + a, 2\right)\right\} \;
        \text{for} \; i = 0,1,\dots,t - 1
$$

$q$ grouping matrices can be constructed, one for each element of $a$ of $\mathbb{F}_{q}$. The rows of each matrix are all
triples: $A_{0}(a)$, $B_{j}^{i}(a)$, $A^{i}(a)$, for the given value $a$.

Under these conditions, $\alpha = 4t + 1$ and $\beta = 3$. The trivial upper bound for number of rounds is therefore:

$$
    l_{\max}(\alpha, \beta) = \left\lfloor\frac{3(4t + 1) - 1}{3 - 1}\right\rfloor = \left\lfloor\frac{12t + 2}{2}\right\rfloor
    = 6t + 1 = q
$$

This method also provides a number of rounds equal to the trivial upper bound.
