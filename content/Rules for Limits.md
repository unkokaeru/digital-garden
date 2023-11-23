# Rules for Limits

## Overview

In calculus, limits are fundamental in understanding the behaviour of functions as they approach a specific point. Limits help in defining derivatives and integrals, which are core concepts in calculus. This note will cover the basic rules for calculating limits, which are essential for understanding more complex calculus topics.

## Basic Rules

1. **Constant Rule**: If $f(x) = c$, a constant, then $\lim_{x \to a} f(x) = c$.
2. **Identity Rule**: For $f(x) = x$, $\lim_{x \to a} f(x) = a$.
3. **Sum Rule**: $\lim_{x \to a} [f(x) + g(x)] = \lim_{x \to a} f(x) + \lim_{x \to a} g(x)$.
4. **Difference Rule**: $\lim_{x \to a} [f(x) - g(x)] = \lim_{x \to a} f(x) - \lim_{x \to a} g(x)$.
5. **Product Rule**: $\lim_{x \to a} [f(x) \cdot g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)$.
6. **Quotient Rule**: If $\lim_{x \to a} g(x) \neq 0$, then $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}$.
7. **Power Rule**: $\lim_{x \to a} [f(x)]^n = [\lim_{x \to a} f(x)]^n$, where $n$ is a positive integer.

## Historical Context

The concept of limits was formalized in the late 17th century by Sir Isaac Newton and Gottfried Wilhelm Leibniz while developing calculus. This was a significant advancement over the previous methods of infinitesimals, providing a more rigorous foundation for calculus.

## Application in Calculus

- **Derivatives**: The derivative of a function at a point is defined as the limit of the function's average rate of change at that point.
- **Integrals**: The integral of a function is found using the limit of summing infinitely many infinitesimally small quantities.

## Examples

1. **Constant Rule Example**: $\lim_{x \to 4} 7 = 7$.
2. **Sum Rule Example**: $\lim_{x \to 3} (x^2 + 2x) = \lim_{x \to 3} x^2 + \lim_{x \to 3} 2x = 9 + 6 = 15$.

## Test Questions

1. Calculate $\lim_{x \to 2} (3x + 4)$ using the Sum and Constant rules.
2. Find $\lim_{x \to 5} x^3$ using the Power rule.
3. Determine $\lim_{x \to 0} \frac{x^2 - 1}{x - 1}$ using the Quotient rule.