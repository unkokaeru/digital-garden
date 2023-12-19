# Differentiability of Functions

## Introduction
In calculus, differentiability is a fundamental concept that deals with the existence and nature of derivatives of functions. A function is said to be differentiable at a point if it has a derivative at that point. This concept is closely related to continuity but is a stronger condition.

## Understanding Differentiability

### Definition
A function $f: \mathbb{R} \rightarrow \mathbb{R}$ is differentiable at a point $a$ if the following limit exists:
$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$
This limit, if it exists, is known as the derivative of $f$ at $a$.

### Relationship with Continuity
For a function to be differentiable at a point, it must be continuous at that point. However, the converse is not true; a function can be continuous at a point but not differentiable there. A classic example is the absolute value function, which is continuous everywhere but not differentiable at $x = 0$.

## Examples of Differentiable Functions

1. **Linear Functions**: Any linear function $f(x) = mx + b$ is differentiable everywhere, and its derivative is the constant $m$.
2. **Polynomials**: Polynomials are differentiable everywhere. For example, the derivative of $f(x) = x^2$ is $f'(x) = 2x$.
3. **Trigonometric Functions**: Functions like $\sin(x)$ and $\cos(x)$ are differentiable everywhere, with their derivatives being $\cos(x)$ and $-\sin(x)$ respectively.

## Non-Examples
- **The Absolute Value Function**: As mentioned, $f(x) = |x|$ is not differentiable at $x = 0$ because the function makes a sharp turn there.
- **Step Functions**: Functions that have jumps or discontinuities, like the Heaviside step function, are not differentiable at those points of discontinuity.

## Historical Context
The concept of differentiability was formalized in the 17th century, primarily through the work of Isaac Newton and Gottfried Wilhelm Leibniz. Their development of calculus introduced the fundamental principles of differentiation, which have since become essential in mathematics, physics, and engineering.

## Test Questions
1. Is the function $f(x) = x^3$ differentiable at $x = 2$? What is its derivative at this point?
2. Give an example of a function that is continuous everywhere but not differentiable at exactly one point.
3. Explain why a function that has a corner or a cusp at a point is not differentiable at that point.

[[Calculus]] | [[Derivatives]] | [[Continuity]]