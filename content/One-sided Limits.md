# One-sided Limits

## Introduction
One-sided limits are an essential concept in calculus, particularly when studying functions that behave differently as they approach a certain point from different directions. Understanding one-sided limits is crucial for grasping the overall concept of limits, which forms the foundation for derivatives and integrals.

## Definition
A **one-sided limit** refers to the value that a function approaches as the input approaches a particular point from one side - either from the left or the right.

### Left-hand Limit
The **left-hand limit** of a function $f(x)$ as $x$ approaches a point $a$ is denoted as $\lim_{{x \to a^-}} f(x)$. It describes the behaviour of $f(x)$ as $x$ approaches $a$ from the left (i.e., from values less than $a$).

### Right-hand Limit
Conversely, the **right-hand limit** of $f(x)$ as $x$ approaches $a$ is denoted as $\lim_{{x \to a^+}} f(x)$. This limit explains what happens to $f(x)$ as $x$ approaches $a$ from the right (i.e., from values greater than $a$).

## Importance
One-sided limits are particularly important for understanding functions that are not continuous at certain points. They help in determining the behaviour of a function near points of discontinuity.

## Examples
1. **Step Function:** Consider the Heaviside step function $H(x)$, which is 0 for $x < 0$ and 1 for $x \geq 0$. The left-hand limit as $x$ approaches 0 is 0, while the right-hand limit is 1.

2. **Piecewise Functions:** Functions defined differently on different intervals often have distinct left-hand and right-hand limits at the points where the definition changes.

## Historical Context
The concept of limits, including one-sided limits, was formalized in the 19th century, though mathematicians like Newton and Leibniz used limit-like concepts in developing calculus in the 17th century.

## Conclusion
One-sided limits play a critical role in understanding the behaviour of functions, especially near points of discontinuity. They are fundamental in the study of calculus and are a stepping stone to more advanced concepts.

---

## Test Questions
1. Calculate the left-hand and right-hand limits of the function $f(x) = \frac{x}{|x|}$ as $x$ approaches 0.
2. For the function $$g(x) = \begin{cases} 
      x^2 & \text{if } x \leq 1 \\
      2x + 1 & \text{if } x > 1 
   \end{cases}$$, find $\lim_{{x \to 1^-}} g(x)$ and $\lim_{{x \to 1^+}} g(x)$.
3. Explain why the left-hand and right-hand limits are important for determining the continuity of a function at a point.