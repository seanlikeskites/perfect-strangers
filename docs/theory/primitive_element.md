# Primitive Element Matching
Several [$\mathrm{RBIBD}$](./block_designs#balanced-incomplete-block-designs) construction methods from the literature
utilise a primitive element of a finite field in defining blocks. We refer to any such construction as a primitive element
construction.

## Constructions
Primitive element constructions make use of the following elements:

  * $\mathbb{F}_{q}$: the finite field of some order $q$.
  * $g$: a primitive element of that finite field.
  * $\mathbb{Z}_{n}$: the additive group of integers modulo $n$.

Depending on the experiment parameters $\left(\alpha \; \text{and} \; \beta\right)$ we use a different primitive element
construction.

### When $\beta = 3$
Let $q$ be a prime power of the form $6t + 1$, for some integer $t$. Theorems 5 and 6 from Ray-Chaudhuri and Wilson
(1971)[^1] give primitive element constructions for $\left(\alpha\beta, 3, 1\right)$-$\mathrm{RBIBD}$s when $\alpha\beta =
3q$ and $\alpha\beta = 2q + 1$ respectively.

#### Ray-Chaudhuri and Wilson Theorem 5
When $\alpha\beta = 3q$ each participant can be uniquely identified by an element of the set $\mathbb{F}_{q} \times
\mathbb{Z}_{3}$.  To construct grouping matrices we define the following families of triples, where $a$ is any element of
$\mathbb{F}_{q}$:

$$
    A_{0}(a) = \left\{\left(a, 0\right), \left(a, 1\right), \left(a, 2\right)\right\} \\[10pt]
    B_{j}^{i}(a) = \left\{\left(g^{i} + a, j\right), \left(g^{i + 2t} + a, j\right), \left(g^{i + 4t} + a, j\right)\right\} \;
        \text{for} \; i = 0,1,\dots,t - 1 \; \text{and} \; j = 0,1,2 \\[10pt]
    A^{i}(a) = \left\{\left(g^{i} + a, 0\right), \left(g^{i + 2t} + a, 1\right), \left(g^{i + 4t} + a, 2\right)\right\} \;
        \text{for} \; i = 0,1,\dots,6t - 1
$$

The first $q$ grouping matrices in our sequence are each constructed using a different element $a$ from $\mathbb{F}_{q}$.
The rows of each matrix are the triples: 

  * $A_{0}(a)$
  * $B_{j}^{i}(a)$ for all values of $i$ and $j$
  * $A^{i}(a)$ where $\left\lfloor i/t \right\rfloor$ is odd.

An additional $3t$ grouping matrices can be constructed for each $i$ for which $\left\lfloor i/t \right\rfloor$ is even. The
rows of each matrix are the triples $A^{i}(a)$ for all values of $a$ from $\mathbb{F}_{q}$.

This gives a total of $q + 3t = 9t + 1$ grouping matrices under perfect stranger matching conditions.

#### Ray-Chaudhuri and Wilson Theorem 6
When $\alpha\beta = 2q + 1$ the first $2q$ participants are identified by an element of the set $\mathbb{F}_{q} \times
\mathbb{Z}_{2}$. The final participant is given the label $\infty$. Grouping matrices are constructed from the following
families of triples, where $m$ is a value such that $2g^{m} = g^{t} + 1$:

$$
    A_{0}(a) = \left\{\left(a, 0\right), \left(a, 1\right), \infty)\right\} \\[10pt]
    B_{j}^{i}(a) = \left\{\left(g^{i + 2jt} + a, 0\right), \left(g^{i + 2jt + t} + a, 0\right), \left(g^{i + 2jt + m} + a, 1\right)\right\} \;
        \text{for} \; i = 0,1,\dots,t - 1 \; \text{and} \; j = 0,1,2 \\[10pt]
    A^{i}(a) = \left\{\left(g^{i + m + t} + a, 1\right), \left(g^{i + m + 3t} + a, 1\right), \left(g^{i + m + 5t} + a, 1\right)\right\} \;
        \text{for} \; i = 0,1,\dots,t - 1
$$

$q$ grouping matrices can be constructed, one for each element of $a$ of $\mathbb{F}_{q}$. The rows of each matrix are all
triples: $A_{0}(a)$, $B_{j}^{i}(a)$, $A^{i}(a)$, for the given value $a$.

### When $\beta = 4$
#### Hanani et al. Lemma 3
Let $q$ be a prime power of the form $4t + 1$, for some integer $t$. Lemma 3 from Hanani et al.  (1972)[^2] provides a
primitive element construction for a $\left(3q + 1, 4, 1\right)$-$\mathrm{RBIBD}$.

Associate the first $3q$ participants with an element in the set $\mathbb{F}_{q} \times \mathbb{Z}_{3}$ and label the final
participant $\infty$. Grouping matrices are constructed from the following families of quadruples:

$$
    A(a) = \left\{\left(a, 0\right), \left(a, 1\right), \left(a, 2\right), \infty)\right\} \\[10pt]
    B_{j}^{i}(a) = \left\{
      \left(g^{i} + a, j\right),
      \left(g^{i + 2t} + a, j\right),
      \left(g^{i + t} + a, j + 1\right),
      \left(g^{i + 3t} + a, j + 1\right)
    \right\} \; \text{for} \; i = 0,1,\dots,t - 1 \; \text{and} \; j \in \mathbb{Z}_{3}
$$

The rows of each grouping matrix are all the quadruples: $A(a)$, $B_{j}^{i}(a)$, for a given value of $a \in \mathbb{F}_{q}$.

[^1]: Ray-Chaudhuri, D.K. and Wilson, R.M., 1971. Solution of Kirkman’s schoolgirl problem. In Proc. symp. pure Math (Vol.
  19, pp. 187-203). DOI: [10.1090/pspum/019/9959](https://doi.org/10.1090/pspum/019/9959)
[^2]: Hanani, H., Ray-Chaudhuri, D.K. and Wilson, R.M., 1972. On resolvable designs. Discrete Mathematics, 3(4), pp.343-357.
  DOI: [10.1016/0012-365X(72)90091-X](https://doi.org/10.1016/0012-365X(72)90091-X)
