# Note on Intermediate Value Theorem

## Introduction
The Intermediate Value Theorem (IVT) is a fundamental theorem in calculus, specifically in the field of real analysis. It's an essential tool for understanding the behaviour of continuous functions on real number intervals. 

## Definition
The theorem states that if $f$ is a continuous function on the interval $[a, b]$ and $N$ is any number between $f(a)$ and $f(b)$, then there exists at least one number $c$ in the interval $[a, b]$ such that $f(c) = N$. 

Mathematically, it's expressed as:
- Let $f: [a, b] \rightarrow \mathbb{R}$ be a continuous function.
- If $N$ is any number between $f(a)$ and $f(b)$,
- Then there exists a $c$ in $[a, b]$ such that $f(c) = N$.

## Historical Context
The IVT has its roots in the early development of calculus. It was implicitly used by mathematicians like Bolzano in the 19th century, but the formal and rigorous definition was established as part of the foundations of real analysis.

## Applications and Examples
### Finding Roots
The IVT is often used to show that a function has a root (a point where the function equals zero) within an interval. For example, if a continuous function has values of opposite signs at the ends of an interval, the IVT assures us that there is at least one root within that interval.

### Ensuring Continuity
The theorem also serves as a test for continuity. If a function fails to satisfy the conditions of the IVT on an interval, it's not continuous on that interval.

### Example
Consider the function $f(x) = x^2 - 2$ on the interval $[0, 2]$. We have $f(0) = -2$ and $f(2) = 2$. Since 0 lies between -2 and 2, by the IVT, there exists a $c$ in $[0, 2]$ such that $f(c) = 0$. This is the root of the equation $x^2 - 2 = 0$, which is $\sqrt{2}$.

## Conclusion and Test Questions
Understanding the Intermediate Value Theorem is crucial for analysing the behaviour of continuous functions. It's not only a theoretical tool but also has practical applications in finding roots and ensuring the continuity of functions.

### Test Questions
1. If $f(x)$ is a continuous function on the interval $[-1, 3]$ and $f(-1) = -4$ and $f(3) = 6$, show that there exists a $c$ such that $f(c) = 0$.
2. Provide an example of a function that does not satisfy the conditions of the IVT on a given interval.
3. Explain why the IVT cannot be applied to functions that are not continuous. 

---

For more related concepts, explore:
- [[Continuity in Calculus]]
- [[Root-Finding Algorithms]]
- [[Bolzano's Theorem]]