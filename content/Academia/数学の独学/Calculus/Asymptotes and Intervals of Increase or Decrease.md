# Intervals of Increase or Decrease in Functions

## Overview
In calculus, understanding the intervals of increase or decrease of a function is essential for analysing its behaviour. These intervals refer to the sections of the function's domain where its output either consistently rises (increases) or falls (decreases).

## Defining Intervals
- **Interval of Increase**: A function $f(x)$ is increasing on an interval if, for any two numbers $a$ and $b$ in that interval, $a < b$ implies $f(a) < f(b)$.
- **Interval of Decrease**: Conversely, $f(x)$ is decreasing on an interval if, for any two numbers $a$ and $b$ in that interval, $a < b$ implies $f(a) > f(b)$.

## Determining Intervals
To find these intervals, we typically use the first derivative $f'(x)$ of the function:
1. **Find the Derivative**: Calculate $f'(x)$, the first derivative of $f(x)$.
2. **Identify Critical Points**: Solve $f'(x) = 0$ and $f'(x)$ undefined to find critical points.
3. **Test Intervals**: Pick test points in the intervals created by the critical points and plug them into $f'(x)$. 
   - If $f'(x) > 0$ in an interval, $f(x)$ is increasing there.
   - If $f'(x) < 0$, $f(x)$ is decreasing.

## Historical Context
The concept of intervals of increase and decrease has been integral in calculus since its formalization by Isaac Newton and Gottfried Wilhelm Leibniz in the late 17th century. It is foundational in understanding the behaviour of functions and forms the basis for more advanced concepts like local maxima and minima.

## Example
Consider the function $f(x) = x^3 - 3x^2 - 9x + 10$.
1. Derivative: $f'(x) = 3x^2 - 6x - 9$.
2. Critical Points: Solve $3x^2 - 6x - 9 = 0$ to find the critical points.
3. Test Intervals: Choose test points in the intervals divided by the critical points and determine the sign of $f'(x)$.

## Test Questions
1. For the function $g(x) = x^2 - 4x + 3$, find the intervals where the function is increasing or decreasing.
2. Explain how the first derivative test helps in identifying the intervals of increase or decrease.
3. Determine the intervals of increase and decrease for $h(x) = \sin(x)$ in the interval $[0, 2\pi]$.