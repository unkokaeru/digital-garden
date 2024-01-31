# Polynomial Interpolation

**Introduction**

Polynomial interpolation is a method of estimating values between known data points. In mathematics, if we have a set of points $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$, polynomial interpolation involves finding a polynomial $P(x)$ of degree at most $n-1$ that passes through all these points. This technique is widely used in numerical analysis and computer science.

**Basic Concepts**

1. **Definition**: Polynomial interpolation creates a polynomial function $P(x)$ such that $P(x_i) = y_i$ for each $i = 1, 2, \ldots, n$.
2. **Uniqueness**: For a given set of distinct points, there exists a unique polynomial of degree at most $n-1$ that passes through all the points.
3. **Applications**: Commonly used in data fitting, numerical differentiation and integration, and in graphical applications.

**Methods of Polynomial Interpolation**

1. **Lagrange Interpolation**: Utilizes the concept of Lagrange polynomials, where the interpolating polynomial is expressed as a linear combination of these polynomials.
2. **Newton Interpolation**: Builds the polynomial incrementally, using divided differences to calculate the coefficients.
3. **Hermite Interpolation**: Extends polynomial interpolation by not only matching the values but also the derivatives at given points.

**Formulation with LaTeX**

- Lagrange Polynomial:
  $$
  P(x) = \sum_{j=1}^n y_j \prod_{\substack{i=1 \\ i \neq j}}^n \frac{x - x_i}{x_j - x_i}
  $$

- Newton Polynomial:
  $$
  P(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + \ldots
  $$

**Historical Context**

Polynomial interpolation dates back to the times of Newton and Lagrange, who were among the first to formalize this method. Over the centuries, it has evolved with contributions from mathematicians like Hermite, improving its accuracy and efficiency.

**Examples**

1. **Simple Example**: For points (1,2), (2,3), and (3,5), find the interpolating polynomial.
2. **Lagrange Example**: Use Lagrange interpolation to estimate the value at $x = 4$ given points (1,1), (2,4), (3,9).

**Test Questions**

1. STARTI [Basic] Question: What is the degree of the polynomial that can interpolate four distinct points? Back: The degree of the polynomial is 3 (one less than the number of points). ENDI
2. STARTI [Basic] Question: Explain why polynomial interpolation is not always the best method for data fitting. Back: Polynomial interpolation can lead to oscillations near the endpoints (Runge's phenomenon), especially with high-degree polynomials and unevenly spaced data points. ENDI
3. STARTI [Basic] Question: In the context of polynomial interpolation, what is meant by 'divided differences'? Back: Divided differences are used in Newton's method of polynomial interpolation and refer to a recursively calculated sequence of numbers that are used to determine the coefficients of the interpolating polynomial. ENDI

**Further Reading**

- [[Numerical Analysis]]
- [[Lagrange and Newton Interpolation Methods]]
- [[Runge's Phenomenon]]

This note provides a foundational understanding of polynomial interpolation, suitable for undergraduate mathematics. For further exploration, refer to the provided hyperlinks.