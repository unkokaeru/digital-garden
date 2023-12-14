# The Binomial Theorem

## Introduction

The Binomial Theorem is a fundamental theorem in algebra that describes the algebraic expansion of powers of a binomial. Historically, the theorem was first described by the 11th-century mathematician, Al-Karaji, and later developed by Isaac Newton in the 17th century.

## Definition

The Binomial Theorem states that for any positive integer $n$, the expansion of $(a + b)^n$ can be expressed as:

$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

where $\binom{n}{k}$ is a binomial coefficient, calculated as:

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

Here, $n!$ denotes the factorial of $n$.

## Applications

The Binomial Theorem has applications in probability, statistics, and various areas of mathematics including combinatorics and calculus.

## Example

Consider the expansion of $(x + y)^3$. Using the Binomial Theorem:

$$(x + y)^3 = \binom{3}{0}x^3y^0 + \binom{3}{1}x^2y^1 + \binom{3}{2}x^1y^2 + \binom{3}{3}x^0y^3$$
$$= 1x^3 + 3x^2y + 3xy^2 + 1y^3$$
$$= x^3 + 3x^2y + 3xy^2 + y^3$$

---

## Test Questions

1. STARTI [Basic] Question: What is the binomial expansion of $(a + b)^2$? Back: The binomial expansion of $(a + b)^2$ is $a^2 + 2ab + b^2$. ENDI
2. STARTI [Basic] Question: Calculate the coefficient of $x^2y$ in the expansion of $(x + y)^3$. Back: The coefficient of $x^2y$ in the expansion of $(x + y)^3$ is 3. ENDI
3. STARTI [Basic] Question: Explain how the Binomial Theorem applies to the calculation of probabilities in a binomial distribution. Back: In a binomial distribution, the probabilities of outcomes can be calculated using the Binomial Theorem, as the distribution represents the probabilities of obtaining a certain number of successes in a fixed number of independent experiments, each with two possible outcomes (success or failure). ENDI