# Step Functions and their Limits

Step functions are a type of piecewise constant function, commonly used in mathematical analysis and applications. They are defined by partitioning a domain into a finite number of intervals and assigning a constant value to each interval. This creates a function that jumps from one value to another, resembling steps, hence the name.

## Definition and Examples

A step function, $f$, on an interval $[a, b]$ can be written as:

$$f(x) = \begin{cases} 
c_1 & \text{if } x \in [a_1, b_1) \\
c_2 & \text{if } x \in [a_2, b_2) \\
\vdots \\
c_n & \text{if } x \in [a_n, b_n]
\end{cases}$$

where $c_1, c_2, \ldots, c_n$ are constants, and the intervals $[a_i, b_i)$ cover $[a, b]$ without overlapping.

**Example:** The function defined by $f(x) = 1$ for $x \in [0, 1)$ and $f(x) = 2$ for $x \in [1, 2]$ is a simple step function.

## Properties

- **Discontinuities:** Step functions are discontinuous at the points where the function jumps from one value to another.
- **Integrability:** They are Riemann integrable on any interval over which they are defined.

## Limits of Step Functions

The concept of limits applies to step functions, particularly at points of discontinuity. The limit of a step function as $x$ approaches a point of discontinuity can be different from the function's value at that point.

### Left-Hand and Right-Hand Limits

- **Left-Hand Limit (LHL):** The limit of $f(x)$ as $x$ approaches a point $c$ from the left.
- **Right-Hand Limit (RHL):** The limit of $f(x)$ as $x$ approaches $c$ from the right.

In many cases, the LHL and RHL at a point of discontinuity of a step function are equal to the values of the function on the intervals immediately to the left and right of the point, respectively.

## Historical Context

Step functions have been essential in the development of integration theory, serving as a simple form of a function that is easy to integrate. They are also used in probability theory (e.g., in defining cumulative distribution functions) and in signal processing.

## Applications

- **Signal Processing:** Step functions model signals that change abruptly at certain points in time.
- **Economics:** They can represent tax brackets where the tax rate changes at specific income levels.

## Test Questions

1. **Question:** Provide an example of a step function defined on the interval $[0, 3]$.
   
   **Back:** One example could be: $f(x) = 1$ for $x \in [0, 1)$, $f(x) = 2$ for $x \in [1, 2)$, and $f(x) = 3$ for $x \in [2, 3]$.

2. **Question:** Explain why step functions are Riemann integrable.

   **Back:** Step functions are Riemann integrable because they are bounded and only have a finite number of discontinuities in any bounded interval.

3. **Question:** What is the left-hand limit of the step function $f(x)$ at $x = 2$ if $f(x) = 3$ for $x \in [1, 2)$ and $f(x) = 5$ for $x \in [2, 3]$?

   **Back:** The left-hand limit of $f(x)$ at $x = 2$ is 3, as it is the value of the function on the interval immediately to the left of 2.