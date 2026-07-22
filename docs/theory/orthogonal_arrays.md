# Orthogonal Arrays
## Definition
An orthogonal array with parameters $N$, $k$, $v$, $t$, and $\lambda$ is an $N{\times}k$ matrix with the following
properties:

  * Each element is taken from a set of $v$ points, $X$.
  * In any subset of $t$ columns, the rows produce every $t$-tuple of points from $X$ exactly $\lambda$ times.

Below is an example of an orthogonal array where: $N = 9$, $k = 3$, $X = \{0, 1, 2\}$, $t = 2$, and ${\lambda = 1}$. For any
two columns of this matrix, every ordered pair of points from $X$ appears as exactly one row.

$$
    \begin{bmatrix}
        0 & 0 & 0 \\
        0 & 1 & 1 \\
        0 & 2 & 2 \\
        1 & 0 & 1 \\
        1 & 1 & 2 \\
        1 & 2 & 0 \\
        2 & 0 & 2 \\
        2 & 1 & 0 \\
        2 & 2 & 1 \\
    \end{bmatrix}
$$

Given there are $v^{t}$ possible $t$-tuples of points taken from a set of size $v$, and each of these must appear in
$\lambda$ rows, the number of rows in an orthogonal array is given by $N = \lambda v^{t}$.


## Notation
A common notation for orthogonal arrays of a given set of parameters is $\mathrm{OA}(N, k, v, t)$. This may also be referred
to as an orthogonal array of type $(N, k, v, t)$. The $\lambda$ parameter is excluded from the notation as it can be easily
calculated from the other parameters: $\lambda = v^{t}/N$. The example array above would be an $\mathrm{OA}$(9, 3, 3, 2).

## Resolvable Orthogonal Arrays
An orthogonal array is said to be resolvable if its rows can be partitioned into smaller orthogonal arrays with a lower $t$
value. For example, the $\mathrm{OA}(9, 3, 3, 2)$ from above can be partitioned into the following three orthogonal arrays
of type (3, 3, 3, 1):


$$
    \begin{bmatrix}
        0 & 0 & 0\\
        1 & 1 & 2\\
        2 & 2 & 1\\
    \end{bmatrix} \qquad \begin{bmatrix}
        0 & 1 & 1\\
        1 & 2 & 0\\
        2 & 0 & 2\\
    \end{bmatrix} \qquad \begin{bmatrix}
        0 & 2 & 2\\
        1 & 0 & 1\\
        2 & 1 & 0\\
    \end{bmatrix}
$$

For perfect stranger matching we are interested in orthogonal arrays of type $\left(v^{2}, k, v, 2\right)$ which can be
resolved into $v$ orthogonal arrays of type $\left(v, k, v, 1\right)$. These are used in the <a style="text-decoration:
none;" href="./sub_bibd">Sub-$\mathrm{BIBD}$</a> construction method. For the purposes of this documentation we will refer
to such a resolvable orthogonal array as an $\mathrm{ROA}\left(v^{2}, k, v, 2\right)$.
