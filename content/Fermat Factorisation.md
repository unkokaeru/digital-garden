# Fermat Factorization

## Introduction
Fermat Factorization is a method in number theory for finding the factors of an odd integer. Named after Pierre de Fermat, a 17th-century mathematician, this method is particularly efficient for numbers that are a product of two primes close to each other.

## Principle
The basic idea behind Fermat's Factorization is to express an odd integer $N$ as the difference of two squares:

$$N = a^2 - b^2$$

This can be further factored into:

$$N = (a + b)(a - b)$$

Here, $N$ is the number to be factored, and $a$ and $b$ are integers.

## Method
1. Start with a value of $a$ that is the ceiling square root of $N$ ($a = \lceil \sqrt{N} \rceil$).
2. Compute $b^2 = a^2 - N$.
3. If $b^2$ is a square number, then $N = (a + b)(a - b)$; $a + b$ and $a - b$ are the factors.
4. If $b^2$ is not a square, increment $a$ and repeat step 2.

This method is efficient when $N$ is a product of two primes that are close together. For larger differences, the method can be less efficient than modern algorithms like the General Number Field Sieve.

## Example
Consider finding factors of N = 5959. 

1. Start with $a = \lceil \sqrt{5959} \rceil = 78$.
2. Compute $b^2 = 78^2 - 5959 = 49$.
3. Since 49 is a square number ($7^2$), the factors are $78 + 7$ and $78 - 7$, which are $85$ and $71$.

Therefore, $5959 = 85 \cdot 71$.

## Historical Context
Fermat's Factorization method, though simple, was a significant step in number theory. Pierre de Fermat was instrumental in the development of modern number theory, and his work laid the groundwork for future mathematicians.

## Test Questions
1. STARTI [Basic] Question: What is the basic principle behind Fermat's Factorization method? Back: It involves expressing an odd integer as the difference of two squares. ENDI
2. STARTI [Basic] Question: In Fermat's Factorization method, if N = 2021, what is the starting value of a? Back: The starting value of a is the ceiling of the square root of 2021, which is 45. ENDI
3. STARTI [Basic] Question: For N = 437, apply Fermat's Factorization method and find the factors. Back: The factors are 23 and 19. (Start with a = \lceil \sqrt{437} \rceil = 21, then find b^2 = 21^2 - 437, and so on until you find that b^2 is a square number). ENDI