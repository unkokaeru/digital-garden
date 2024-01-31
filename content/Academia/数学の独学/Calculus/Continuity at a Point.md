# Continuity at a Point

## Definition
Continuity at a point in the realm of mathematics, particularly in calculus, is a fundamental concept that describes the behaviour of functions at specific points. A function $f(x)$ is said to be continuous at a point $x = a$ if the following three conditions are met:
1. The function $f(x)$ is defined at $x = a$; that is, $f(a)$ exists.
2. The limit of $f(x)$ as $x$ approaches $a$ exists.
3. The limit of $f(x)$ as $x$ approaches $a$ is equal to the function value at $a$; mathematically, $\lim_{x \to a} f(x) = f(a)$.

## Intuitive Understanding
Imagine drawing the graph of a function without lifting your pen off the paper. If you can do this through a point $a$, the function is continuous at that point. This imagery helps understand continuity as a smooth, uninterrupted path.

## Historical Context
The concept of continuity has evolved over centuries. Early mathematicians like Newton and Leibniz, founders of calculus, used intuitive notions of continuity. Rigorous definitions, similar to the one used today, were developed in the 19th century by mathematicians like Augustin-Louis Cauchy and Karl Weierstrass. This period marked a shift from intuitive understandings to precise mathematical definitions.

## Examples
1. **Polynomial Functions**: Consider $f(x) = x^2$. This function is continuous at every point because it meets all three conditions for any value of $x$.
2. **Rational Functions**: The function $g(x) = \frac{1}{x}$ is continuous at every point except $x = 0$, where it is undefined.
3. **Piecewise Functions**: Consider $$h(x) = \begin{cases} 
x^2, & \text{if } x < 2 \\
5, & \text{if } x = 2 \\
x + 3, & \text{if } x > 2 
\end{cases}$$. Here, $h(x)$ is continuous at $x = 2$ because $\lim_{x \to 2} h(x) = h(2) = 5$.

## Test Questions
1. Is the function $f(x) = \frac{x^2 - 1}{x - 1}$ continuous at $x = 1$? Why or why not?
2. If $\lim_{x \to 3} g(x) = 6$ and $g(3) = 6$, is $g(x)$ continuous at $x = 3$?
3. For the function $h(x) = |x|$, identify a point where $h$ is not continuous. Explain your reasoning.