# Combinatorial Probability

Combinatorial probability is a branch of mathematics that deals with the likelihood of the occurrence of events where the outcomes are distinctly defined and countable. It's a crucial concept in statistics and plays a significant role in various fields such as computer science, finance, and game theory.

## Key Concepts

### 1. Sample Space
The sample space in combinatorial probability is the set of all possible outcomes. For example, in a dice roll, the sample space is {1, 2, 3, 4, 5, 6}.

### 2. Events
An event is a subset of the sample space. For instance, rolling an even number is an event within the sample space of a dice roll.

### 3. Counting Techniques
Counting techniques are vital in determining the size of the sample space and the number of favorable outcomes. The most common methods are:
- **Factorials**: Used in arrangements where order matters. For example, the number of ways to arrange 'n' distinct objects is $n!$ (n factorial).
- **Permutations**: Order-specific arrangements of a subset of items.
- **Combinations**: Order-independent selections of a subset of items.

### 4. Probability Formula
The probability of an event is given by $P(E) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}}$.

## Applications
Combinatorial probability is used in analyzing games of chance, in cryptographic algorithms, and in predicting outcomes in genetic inheritance.

## Historical Context
The foundation of combinatorial probability was laid in the 17th century, with significant contributions from mathematicians like Blaise Pascal and Pierre de Fermat. Their correspondence on problems related to gambling laid the groundwork for the theory of probability.

## Examples in Real Life
1. **Lotteries**: Calculating the odds of winning.
2. **Poker**: Determining the probability of specific hand combinations.
3. **Genetics**: Predicting the likelihood of inheriting specific traits.

---

## Test Questions

1. STARTI [Basic] Question: What is the probability of rolling a 4 with a fair six-sided die? Back: $P(4) = \frac{1}{6}$. ENDI
2. STARTI [Basic] Question: How many ways can you arrange 5 distinct books on a shelf? Back: There are $5! = 120$ ways. ENDI
3. STARTI [Basic] Question: In a lottery where you choose 6 numbers out of 49, what is the probability of choosing exactly 3 correct numbers if the order of selection doesn't matter? Back: $P(\text{3 correct}) = \frac{\binom{6}{3} \times \binom{43}{3}}{\binom{49}{6}}$. ENDI