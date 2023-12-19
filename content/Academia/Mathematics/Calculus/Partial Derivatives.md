# Partial Derivatives

## Introduction
Partial derivatives are fundamental in the field of multivariable calculus. They represent the rate at which a function changes as one of its variables is varied, while keeping other variables constant. This concept is crucial in physics, engineering, economics, and various other disciplines where functions depend on more than one variable.

## Basic Concepts
Consider a function $f(x, y)$ of two variables, $x$ and $y$. The partial derivative of $f$ with respect to $x$ is denoted as $\frac{\partial f}{\partial x}$ and represents the rate of change of $f$ as $x$ changes, while $y$ is held constant. Similarly, $\frac{\partial f}{\partial y}$ denotes the rate of change of $f$ with respect to $y$, keeping $x$ constant.

### Calculation
To compute $\frac{\partial f}{\partial x}$, treat $y$ as a constant and differentiate $f$ with respect to $x$ using the standard rules of differentiation. Apply the same process to find $\frac{\partial f}{\partial y}$, treating $x$ as a constant.

### Example
For $f(x, y) = x^2y + 3xy^3$:
- $\frac{\partial f}{\partial x} = 2xy + 3y^3$
- $\frac{\partial f}{\partial y} = x^2 + 9xy^2$

## Higher-Order Partial Derivatives
You can also take partial derivatives of partial derivatives. For example, the second-order partial derivatives of $f$ are:
- $\frac{\partial^2 f}{\partial x^2}$, $\frac{\partial^2 f}{\partial y^2}$: The second partial derivatives with respect to $x$ and $y$ respectively.
- $\frac{\partial^2 f}{\partial x \partial y}$, $\frac{\partial^2 f}{\partial y \partial x}$: The mixed partial derivatives.

### Clairaut's Theorem
Clairaut's Theorem states that if $f$ is continuously differentiable, then the mixed partial derivatives are equal: $\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$.

## Applications
Partial derivatives are used in various fields:
- **Physics**: Describing systems with multiple variables (e.g., temperature gradients).
- **Engineering**: Optimization problems, fluid dynamics.
- **Economics**: Modeling how different factors affect economic indicators.

## Conclusion and Test Questions
Understanding partial derivatives is essential for any field that deals with functions of multiple variables. They form the foundation for more complex concepts in multivariable calculus, like gradients and Jacobians.

### Test Questions
1. Compute the partial derivatives $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ for $f(x, y) = \ln(x) + e^{xy}$.
2. Explain the significance of Clairaut's Theorem in the context of partial derivatives.
3. How would you use partial derivatives to find the maximum and minimum values of a function of two variables?