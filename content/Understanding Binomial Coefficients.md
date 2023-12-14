# Understanding Binomial Coefficients

## Introduction
Binomial coefficients are fundamental elements in combinatorics, often denoted as $\binom{n}{k}$ or $C(n, k)$. They represent the number of ways to choose $k$ items from a set of $n$ items without regard to the order in which they are chosen. 

## Definition
The binomial coefficient $\binom{n}{k}$ is defined as:

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

where $n!$ denotes the factorial of $n$, which is the product of all positive integers less than or equal to $n$.

## Properties
1. **Symmetry**: $\binom{n}{k} = \binom{n}{n-k}$. This property reflects the fact that choosing $k$ items out of $n$ is equivalent to leaving out $n-k$ items.
2. **Pascal's Triangle**: Each entry in Pascal's Triangle is a binomial coefficient, and each is the sum of the two directly above it: $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$.
3. **Summation**: The sum of the binomial coefficients for a given $n$ is $2^n$, representing the subsets of a set of size $n$.

## Applications
- **Combinatorial Problems**: Binomial coefficients are used in problems involving combinations, such as how many different ways you can choose a committee from a group.
- **Binomial Theorem**: They play a key role in the expansion of $(x + y)^n$.
- **Probability Theory**: Useful in calculating probabilities in a binomial distribution.

## Historical Context
The study of binomial coefficients can be traced back to ancient India, where they were used in the study of combinatorial mathematics. Blaise Pascal, a French mathematician, made significant contributions in the 17th century, especially in the development of Pascal's Triangle.

## Examples
1. **Choosing Committees**: How many ways can you choose 3 members from a group of 10? Use $\binom{10}{3}$.
2. **Binomial Expansion**: Expand $(x + y)^3$ using binomial coefficients.

## Test Questions
1. Calculate $\binom{7}{3}$.
2. Using Pascal's Triangle, find $\binom{5}{2}$.
3. If a coin is flipped 5 times, how many outcomes contain exactly 3 heads?
