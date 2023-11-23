# Linearisation and Quadratic Approximations

## Introduction

Linearisation and quadratic approximations are powerful mathematical techniques used in calculus and applied mathematics. They are used to approximate complex functions using simpler linear or quadratic functions, making them easier to analyse and work with.

## Linearisation

Linearisation is the process of approximating a function near a point using a linear function. The linear approximation of a function $f(x)$ at a point $a$ is given by the tangent line at that point. The formula for the linear approximation of $f(x)$ at $a$ is:

$$L(x) = f(a) + f'(a)(x - a)$$

### Example
Consider the function $f(x) = \sin(x)$. The linear approximation of $f(x)$ at $a = 0$ is:
$$L(x) = \sin(0) + \cos(0)(x - 0) = x$$

## Quadratic Approximations

Quadratic approximation takes this a step further by using a second-degree polynomial to approximate the function. The formula for the quadratic approximation of $f(x)$ at $a$ is:

$$Q(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2}(x - a)^2$$

### Example
For $f(x) = e^x$, the quadratic approximation at $a = 0$ is:
$$Q(x) = e^0 + e^0(x - 0) + \frac{e^0}{2}(x - 0)^2 = 1 + x + \frac{x^2}{2}$$

## Applications

- **Engineering**: Used in control systems and optimizations.
- **Economics**: Applied in marginal analysis.
- **Physics**: Helps simplify complex equations.

## Test Questions

1. STARTI [Basic] Question: What is the linear approximation of $f(x) = \ln(x)$ at $a = 1$? Back: $L(x) = x - 1$. ENDI
2. STARTI [Basic] Question: How do you find the quadratic approximation of a function at a given point? Back: Evaluate the function and its first and second derivatives at the point, and substitute these into the quadratic approximation formula. ENDI
3. STARTI [Basic] Question: If $f(x) = \cos(x)$, what is the quadratic approximation of $f$ at $a = \frac{\pi}{4}$? Back: $Q(x) = \frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}(x - \frac{\pi}{4}) - \frac{\sqrt{2}}{4}(x - \frac{\pi}{4})^2$. ENDI

---

*For further exploration, consider how linearisation and quadratic approximations could be applied to real-world scenarios in your field of interest.*