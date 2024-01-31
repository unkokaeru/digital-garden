# Stationary Points of Functions with Two Variables

## Introduction
In mathematics, particularly in multivariable calculus, the concept of stationary points is crucial for understanding the behavior of functions with two variables. A stationary point of a function is a point at which the gradient (or the first derivative) of the function is zero. These points are significant because they potentially represent local maxima, local minima, or saddle points in the function's graph.

## Definition
Consider a function $f(x, y)$ of two variables. A point $(x_0, y_0)$ is called a **stationary point** of $f$ if both partial derivatives of $f$ are zero at that point, i.e.,

$$\frac{\partial f}{\partial x}(x_0, y_0) = 0 \quad \text{and} \quad \frac{\partial f}{\partial y}(x_0, y_0) = 0.$$

## Types of Stationary Points
1. **Local Maximum**: At $(x_0, y_0)$, $f(x, y)$ is greater than its immediate surroundings.
2. **Local Minimum**: At $(x_0, y_0)$, $f(x, y)$ is less than its immediate surroundings.
3. **Saddle Point**: At $(x_0, y_0)$, $f(x, y)$ is neither a local maximum nor a minimum but has a flat tangent plane.

## Finding Stationary Points
To find the stationary points of $f(x, y)$, follow these steps:
1. Find the first partial derivatives $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$.
2. Solve the simultaneous equations $\frac{\partial f}{\partial x} = 0$ and $\frac{\partial f}{\partial y} = 0$ to find the coordinates $(x_0, y_0)$ of the stationary points.

## Determining the Nature of Stationary Points
Once the stationary points are found, use the second derivative test to determine their nature:
1. Compute the second-order partial derivatives: $\frac{\partial^2 f}{\partial x^2}$, $\frac{\partial^2 f}{\partial y^2}$, and the mixed derivative $\frac{\partial^2 f}{\partial x \partial y}$.
2. Evaluate the second-order derivatives at the stationary point $(x_0, y_0)$.
3. Calculate the determinant of the [[Hessian matrix]] $D$ at $(x_0, y_0)$:

   $$D = \left( \frac{\partial^2 f}{\partial x^2} \right)\left( \frac{\partial^2 f}{\partial y^2} \right) - \left( \frac{\partial^2 f}{\partial x \partial y} \right)^2$$

4. Interpretation:
   - If $D > 0$ and $\frac{\partial^2 f}{\partial x^2} > 0$, then $(x_0, y_0)$ is a local minimum.
   - If $D > 0$ and $\frac{\partial^2 f}{\partial x^2} < 0$, then $(x_0, y_0)$ is a local maximum.
   - If $D < 0$, then $(x_0, y_0)$ is a saddle point.
   - If $D = 0$, the test is inconclusive.

## Examples
1. Consider $f(x, y) = x^2 + y^2$. The stationary point at $(0, 0)$ is a local minimum.
2. For $f(x, y) = x^2 - y^2$, the point $(0, 0)$ is a saddle point.

## Test Questions
1. Find the stationary points of $f(x, y) = x^3 - 3xy + y^3$ and classify them.
2. If $f(x, y) = x^2 + 2xy + y^2 + 3$, determine the nature of its stationary point(s).
3. Explain why saddle points are important in the study of functions with two variables.

---

This note provides a fundamental understanding of stationary points in functions of two variables, crucial for fields like optimization, economics, and engineering. Understanding and visualizing these concepts enhance the comprehension of the landscape of multivariable functions.