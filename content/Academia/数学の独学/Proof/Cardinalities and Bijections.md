# Cardinalities and Bijections

## Introduction

The concept of **cardinality** refers to the mathematical notion of the "size" of a set, which allows for the comparison and quantification of sets that may not be finite. In essence, cardinality provides a way to describe the number of elements in a set, extending the familiar notion of countability from finite sets to infinite ones.

**Bijections**, or bijective functions, are crucial in the analysis of cardinalities. A function $f: A \to B$ is called bijective if it is both injective (no two elements of $A$ map to the same element of $B$) and surjective (every element of $B$ is mapped to by some element of $A$). When such a bijection exists between two sets, they are said to have the same cardinality.

## Cardinalities

- **Finite Sets:** The cardinality of a finite set is simply the number of elements in the set. For example, the set $\{1, 2, 3\}$ has a cardinality of 3.
- **Infinite Sets:** Infinite sets can be more complex. They are primarily classified into:
  - **Countably Infinite Sets:** These are sets whose elements can be listed in a sequence (e.g., the set of all natural numbers $\mathbb{N}$). Such sets have the same cardinality as $\mathbb{N}$.
  - **Uncountably Infinite Sets:** These are sets that cannot be listed in a sequence, even an infinite one (e.g., the set of all real numbers $\mathbb{R}$). Their cardinality is strictly greater than that of $\mathbb{N}$.

## Bijections and Cardinality

The existence of a bijection between two sets is a powerful concept that equates their sizes, even for infinite sets. For example, the set of even numbers is countably infinite, just like the set of all integers, because we can construct a bijection between them (e.g., by mapping each integer $n$ to $2n$).

### Explicit Bijections

- **Between $\mathbb{N}$ and $\mathbb{Z}$:** A simple bijection can be constructed by alternating between positive and negative integers, starting from zero. This demonstrates that the set of all integers $\mathbb{Z}$ is countably infinite.
- **Between $\mathbb{N}$ and $\mathbb{Q}$:** Constructing a bijection between the natural numbers and the rational numbers involves creating a sequence that includes all possible fractions, illustrating that $\mathbb{Q}$ is countably infinite.

### Countable Sets

A set is countable if it is finite or countably infinite. The concept of countability is vital in understanding the structure of sets within mathematics, particularly in analysis and number theory.

## Examples

1. **The set of prime numbers** is countably infinite, as it can be ordered in an increasing sequence, demonstrating a bijection with $\mathbb{N}$.
2. **The set of algebraic numbers** is also countably infinite, as each algebraic number is a root of a polynomial with integer coefficients, and these polynomials can be listed in a sequence.

## Conclusion

Analyzing cardinalities and constructing explicit bijections provide profound insights into the nature and size of sets, bridging the gap between the intuitive notion of quantity and its mathematical formalization. This exploration reveals the surprising result that some infinite sets can be matched with others in a one-to-one correspondence, highlighting the nuanced hierarchy of infinities.

## Test Questions

1. **[Basic]** Question: What is a bijection? Back: A bijection is a function that is both injective and surjective, meaning each element of the first set is paired with a unique element of the second set, and every element of the second set is paired with some element of the first set.
2. **[Basic]** Question: How can one show that the set of all natural numbers $\mathbb{N}$ and the set of all integers $\mathbb{Z}$ have the same cardinality? Back: One can show this by constructing a bijection between the two sets, such as mapping each natural number to an integer by alternating between positive and negative values.
3. **[Basic]** Question: Explain why the set of all real numbers $\mathbb{R}$ is uncountably infinite. Back: The set of all real numbers $\mathbb{R}$ is uncountably infinite because there is no way to list all real numbers in a sequence that includes every real number, as proven by Cantor's diagonal argument.