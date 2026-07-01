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
