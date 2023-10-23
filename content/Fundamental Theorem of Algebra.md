# Fundamental Theorem of Algebra
*(Argand, 1806)*

The **Fundamental Theorem of Algebra** is a foundational result in the field of complex analysis, but it has wide-reaching implications for polynomial equations in general. The theorem essentially guarantees that every non-constant polynomial has at least one root in the complex number system.

## Statement

For every non-constant polynomial $p(z)$ with complex coefficients, there exists a complex number $c$ such that $p(c) = 0$.

In other words, every polynomial of degree $n \geq 1$ has at least one complex root. Moreover, with multiplicity considered, it has exactly $n$ complex roots.

## Proof

The formal proof of the Fundamental Theorem of Algebra is beyond the scope of a simple introduction due to its reliance on advanced concepts from complex analysis. However, a general sketch can be provided.

### Proof Sketch:

1. **Boundedness of \( p \)**: For a non-constant polynomial, it can be shown that there exists some radius $R$ such that $|p(z)| \rightarrow \infty$ as $|z| \rightarrow \infty$, for all $|z| > R$. This means that the polynomial's magnitude grows without bound outside of some large circle in the complex plane.

2. **Achievement of Minimum Magnitude**: The function $|p(z)|$ achieves its minimum value over the closed disc of radius $R$ (due to compactness). If this minimum value is zero, we have found a root. If not...

3. **Rolle's Theorem for Complex Polynomials**: If $p(z)$ doesn't have a root in the disc of radius $R$, then neither does its derivative. This contradicts the fact that the derivative is of lower degree and, by induction, should have a root. Thus, $p(z)$ must have had a root in the disc.

Through a combination of these elements, we can establish the Fundamental Theorem of Algebra.

## Implications

1. **Complex Roots Come in Pairs**: If a polynomial has real coefficients and one non-real complex root, then its complex conjugate is also a root.

2. **Degree of Polynomial**: A polynomial of degree $n$ will have exactly $n$ roots in the complex numbers, considering multiplicity.

3. **Roots and Factors**: If $c$ is a root of $p(z)$, then $(z - c)$ is a factor of $p(z)$. Using synthetic division or polynomial long division, we can express $p(z)$ as $p(z) = (z-c)q(z)$ where $q(z)$ is a polynomial of degree $n-1$.

## Practice Problems

1. Show that the polynomial $p(z) = z^2 + 1$ has no real roots but has two complex roots.
2. Find all roots, real or complex, of the polynomial $p(z) = z^3 - 6z^2 + 11z - 6$.

For those interested in a deeper dive, books on complex analysis or advanced algebra will provide rigorous proofs and further discussion on the Fundamental Theorem of Algebra.

Note that this also links with [[Galois Theory]], and how it can prove that no formulae exist for polynomials above order 4.