# Limits at Infinity

## Introduction
In mathematics, particularly in calculus, the concept of limits at infinity is crucial for understanding the behaviour of functions as they approach infinitely large (or small) values. This concept helps in analysing and understanding the asymptotic behaviour of functions.

## Definition
The limit of a function $f(x)$ as $x$ approaches infinity, denoted as $\lim_{x \to \infty} f(x)$, is the value that $f(x)$ gets closer to as $x$ becomes arbitrarily large. Similarly, the limit of $f(x)$ as $x$ approaches negative infinity, denoted as $\lim_{x \to -\infty} f(x)$, is the value that $f(x)$ approaches as $x$ becomes arbitrarily large in the negative direction.

## Formal Definition
1. **Positive Infinity**: We say $\lim_{x \to \infty} f(x) = L$ if for every $\epsilon > 0$, there exists a $M$ such that if $x > M$, then $|f(x) - L| < \epsilon$.
2. **Negative Infinity**: We say $\lim_{x \to -\infty} f(x) = L$ if for every $\epsilon > 0$, there exists a $N$ such that if $x < N$, then $|f(x) - L| < \epsilon$.

## Examples
1. **Polynomial Functions**: For any polynomial function $p(x)$, $\lim_{x \to \infty} p(x)$ is either $\infty$, $-\infty$, or undefined, depending on the leading term.
2. **Rational Functions**: For a rational function $\frac{p(x)}{q(x)}$, where $p(x)$ and $q(x)$ are polynomials, the limit at infinity depends on the degrees of $p(x)$ and $q(x)$.

## Applications
- **Asymptotic behaviour**: Understanding how a function behaves as it approaches infinity is crucial in many areas of mathematics, including calculus and analysis.
- **Curve Sketching**: Limits at infinity are used to determine horizontal asymptotes of functions, which are essential in sketching graphs.

## Conclusion
The concept of limits at infinity is fundamental in calculus and helps in understanding the behaviour of functions over large scales. It's a critical tool for evaluating the long-term behaviour of various mathematical models.

---

## Test Questions
1. Calculate $\lim_{x \to \infty} \frac{2x^3 - 1}{x^3 + 5}$.
2. Determine if $\lim_{x \to -\infty} \sqrt{x^2 + 1}$ exists, and if so, find its value.
3. Evaluate $\lim_{x \to \infty} e^{-x}$ and explain why it approaches its limit.