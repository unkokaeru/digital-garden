# Euclidean Algorithm

## Introduction
The **[[Euclidean algorithm]]** is a time-honored technique for finding the greatest common divisor (GCD) of two integers. Named after the ancient Greek mathematician Euclid, it's one of the oldest algorithms still in common use today. 

## Core Concept
The algorithm is based on the principle that the GCD of two numbers also divides their difference. It uses a series of divisions to reduce the problem to increasingly smaller pairs of numbers until the GCD is found. 

## Process
Given two integers $a$ and $b$, the Euclidean algorithm follows these steps:
1. Divide $a$ by $b$, and find the quotient $q$ and remainder $r$, so $a = bq + r$.
2. Replace $a$ with $b$ and $b$ with $r$.
3. Repeat the process until $b$ becomes 0. The non-zero remainder at this step is the GCD of $a$ and $b$.

## Example
Let's consider finding the GCD of 48 and 18:
- Step 1: 48 divided by 18 gives a remainder of 12. So, replace 48 with 18, and 18 with 12.
- Step 2: 18 divided by 12 gives a remainder of 6. So, replace 18 with 12, and 12 with 6.
- Step 3: 12 divided by 6 gives a remainder of 0. So, the GCD is 6.

## Historical Context
Euclid's original formulation of the algorithm is found in his work "Elements", which is a cornerstone in the history of mathematics. The algorithm was likely known to mathematicians before Euclid, but his work is the earliest surviving detailed account.

## Applications
The Euclidean algorithm is not only used for finding GCDs but also has applications in number theory, cryptography, and even in algorithms for solving linear Diophantine equations.

## Test Questions
1. STARTI [Basic] Question: How does the Euclidean algorithm determine the GCD of two integers? Back: It repeatedly replaces the larger number by the remainder of dividing the larger number by the smaller one, until the remainder is zero. The last non-zero remainder is the GCD. ENDI
2. STARTI [Basic] Question: What is the GCD of 56 and 98 according to the Euclidean algorithm? Back: 14. ENDI
3. STARTI [Basic] Question: Explain how the Euclidean algorithm is used in cryptography. Back: It's used in algorithms like RSA for computing modular inverses, a key step in the encryption and decryption processes. ENDI

---

This note provides a foundational understanding of the **[[Euclidean algorithm]]**. Its iterative, division-based process exemplifies a simple yet powerful approach to problem-solving in mathematics.