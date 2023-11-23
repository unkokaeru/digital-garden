# Types of Discontinuity

**Introduction**
In mathematics, particularly in calculus and real analysis, the concept of discontinuity plays a crucial role in understanding the behaviour of functions. Discontinuity refers to points at which a function is not continuous. Understanding different types of discontinuities helps in analysing functions and their properties. This note delves into the main types of discontinuities you'll encounter.

## Types of Discontinuities

### 1. Jump Discontinuity
A **jump discontinuity** occurs when the function has two distinct limit values as it approaches from the left and the right of a certain point. In other words, the function 'jumps' from one value to another.

- **Example:** Consider the function $$f(x) = \left\{
   \begin{array}{ll}
   x + 1 & \mbox{if } x < 0 \\
   x - 1 & \mbox{if } x \geq 0
   \end{array}
\right.$$- This function has a jump discontinuity at $x = 0$.

### 2. Infinite Discontinuity
An **infinite discontinuity** occurs when the function approaches infinity as it nears a certain point.

- **Example:** The function $g(x) = \frac{1}{x}$ has an infinite discontinuity at $x = 0$.

### 3. Removable Discontinuity
A **removable discontinuity** is present when a function is not defined at a point, but the limit exists and is the same from both sides. By redefining the function at that point, the discontinuity can be 'removed.'

- **Example:** The function $h(x) = \frac{{x^2 - 1}}{{x - 1}}$ can be simplified to $h(x) = x + 1$ for $x \neq 1$. It has a removable discontinuity at $x = 1$.

### 4. Oscillating Discontinuity
An **oscillating discontinuity** occurs when the function oscillates between different values as it approaches the discontinuous point.

- **Example:** The function $k(x) = \sin\left(\frac{1}{x}\right)$ oscillates between -1 and 1 as $x$ approaches 0.

## Historical Context
The concept of continuity and discontinuity in mathematics dates back to the 19th century. Bernhard Riemann, a German mathematician, was among the pioneers in formalizing the definition of a continuous function. His work paved the way for rigorous mathematical analysis and a deeper understanding of function behaviour.

## Test Questions
1. **Identify the Discontinuity:** For the function $f(x) = \frac{x^2 - 4}{x - 2}$, determine the type of discontinuity at $x = 2$.
2. **True or False:** Every infinite discontinuity is also a jump discontinuity.
3. **Application:** Describe the behaviour of the function $g(x) = \tan(x)$ near $x = \frac{\pi}{2}$ and classify the type of discontinuity.