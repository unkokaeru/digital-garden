# Tests for Continuity

## Introduction
Continuity of a function is a fundamental concept in calculus and mathematical analysis. It describes the behaviour of functions as they approach a particular point. A function is continuous at a point if there is no sudden change in its value at that point. Understanding continuity is crucial in studying limits, derivatives, and integrals.

## Definition
A function $f(x)$ is said to be continuous at a point $a$ if the following three conditions are met:
1. **Existence of $f(a)$**: The function $f(x)$ is defined at $a$.
2. **Limit Exists**: The limit of $f(x)$ as $x$ approaches $a$ exists.
3. **Limit Equals Function Value**: The limit of $f(x)$ as $x$ approaches $a$ is equal to $f(a)$.

Formally, $f(x)$ is continuous at $a$ if and only if 
$$\lim_{x \to a} f(x) = f(a)$$

## Types of Continuity
1. **Continuous at a Point**: If a function meets the above criteria at a particular point.
2. **Continuous on an Interval**: If a function is continuous at every point in a given interval.
3. **Uniform Continuity**: A stronger form of continuity that holds when the function's rate of change is bounded throughout its domain.

## Tests for Continuity
To determine whether a function is continuous at a point or over an interval, follow these steps:

1. **Check for Existence**: Ensure the function is defined at the point or throughout the interval.
2. **Evaluate the Limit**: Find the limit of the function as it approaches the point from both directions (left and right).
3. **Compare Limit and Function Value**: Ensure that the limit equals the function's value at the point.

### Special Cases
- **Piecewise Functions**: Check continuity at each segment and at the points where the function changes definition.
- **Rational Functions**: Check points where the denominator is zero.
- **Trigonometric Functions**: Pay attention to points where these functions are not defined.

## Historical Context
The concept of continuity has evolved significantly over time. Early notions by mathematicians like Newton and Leibniz were more intuitive. The rigorous definition, as given by Weierstrass in the 19th century, laid the groundwork for modern analysis.

## Examples
1. **Polynomials**: Polynomials are continuous everywhere.
2. **Rational Functions**: Rational functions are continuous wherever they are defined (i.e., where the denominator is non-zero).
3. **Trigonometric Functions**: Functions like sin(x) and cos(x) are continuous everywhere, but functions like tan(x) are not continuous where cos(x) = 0.

## Conclusion
Understanding continuity is essential for delving deeper into calculus. It's a concept that bridges the gap between intuitive and rigorous mathematical thinking.

## Test Questions
1. Is the function $f(x) = \frac{1}{x}$ continuous at $x = 0$? Why or why not?
2. Determine if the function $$g(x) = \left\{
   \begin{array}{ll}
   x^2 & \text{if } x < 1 \\
   x+1 & \text{if } x \geq 1
   \end{array}
\right.$$ is continuous at $x = 1$.
3. Prove that the function $h(x) = x^3 - 2x + 1$ is continuous for all values of $x$.