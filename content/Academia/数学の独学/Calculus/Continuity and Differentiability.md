# Continuity and Differentiability

Continuity and differentiability are fundamental concepts in calculus, which form the backbone of mathematical analysis, particularly in the study of functions. Understanding these concepts is crucial for anyone studying undergraduate mathematics.

## Continuity

### Definition
A function $f(x)$ is said to be continuous at a point $x = a$ if the following three conditions are met:
1. $f(a)$ is defined.
2. The limit of $f(x)$ as $x$ approaches $a$ exists.
3. The limit of $f(x)$ as $x$ approaches $a$ is equal to $f(a)$.

In simpler terms, a function is continuous at a point if there is no interruption in its graph at that point. 

### Types of Continuity
- **Continuous on an Interval:** If a function is continuous at every point in an interval, it is said to be continuous on that interval.
- **Uniform Continuity:** A stronger form where the way the function behaves does not depend on the choice of the point in its domain.

## Differentiability

### Definition
A function $f(x)$ is differentiable at a point $x = a$ if the derivative of $f(x)$ at that point exists. This derivative is given by the limit:
$$f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$$

If this limit exists, the function is differentiable at $x = a$. Differentiability implies a function's graph has a tangent at that point and is not sharply turning.

### Relationship with Continuity
A crucial aspect to remember is that if a function is differentiable at a point, then it must be continuous at that point. However, the converse is not necessarily true: a continuous function may not be differentiable at all points.

## Examples and Historical Context

1. **The Function $f(x) = |x|$:** This function is continuous everywhere but not differentiable at $x = 0$ because of the sharp point at the origin.
2. **The Discovery of Calculus:** The concepts of continuity and differentiability were central to the development of calculus by Newton and Leibniz in the 17th century.

## Test Questions

1. Is the function $f(x) = \frac{1}{x}$ continuous at $x = 0$? Why or why not?
2. Give an example of a function that is continuous at every point but not differentiable at exactly one point.
3. Show that the function $f(x) = x^2$ is differentiable at $x = 1$ and find its derivative at that point.