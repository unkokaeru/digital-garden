- Find divisors of $n$ using a Hasse diagram.
	- Create a Hasse diagram representing the divisibility relations among the divisors of $n$. Start by identifying the prime factors of $n$, then build the diagram by connecting each divisor with its immediate larger divisor that divides $n$.

- Use the Euclidean algorithm to find a greatest common divisor between two numbers or polynomials.
	- Apply the Euclidean algorithm by repeatedly dividing the larger number by the smaller number, then replacing the larger number with the remainder, until the remainder is zero. The last non-zero remainder is the greatest common divisor.

- Find all integer solutions of a linear combination using Bézout's Lemma and the Extended Euclidean algorithm.
	- Use the Extended Euclidean algorithm to express the greatest common divisor of the given numbers as a linear combination of these numbers. This representation will give the integer solutions.

- Converting real numbers from base $n$ to decimal notation.
	- Multiply each digit of the base $n$ number by $n$ raised to the power of its position index (counting from right to left, starting at zero), and sum these products to get the decimal value.

- Convert a recurring decimal into a fraction.
	- Let $x$ be the recurring decimal. Multiply $x$ by a power of 10 that moves the recurring part to the left of the decimal point. Set up an equation and solve for $x$ to express it as a fraction.

- Convert decimal numbers into base $n$.
	 - Divide the decimal number by $n$, record the remainder, then divide the quotient by $n$. Repeat until the quotient is zero. The base $n$ number is the recorded remainders read in reverse order.

- Calculate the sum of a geometric or arithmetic progression.
	- For a geometric progression, use the formula $S_n = a(1 - r^n)/(1 - r)$. For an arithmetic progression, use $S_n = n/2(2a + (n-1)d)$, where $a$ is the first term, $n$ is the number of terms, $r$ is the common ratio (geometric), and $d$ is the common difference (arithmetic).

- Use Ruffini's Rule to divide polynomials, as well as using it to write a polynomial in powers of $(x-a)$, where $a\in\mathbb{Z}$.
	- Apply Ruffini's Rule for polynomial division by using a synthetic division table. For writing a polynomial in powers of $(x-a)$, factor the polynomial using Ruffini’s rule iteratively.

- Find a unique polynomial using polynomial interpolation (from multiple points).
	- Use Lagrange interpolation or Newton's divided difference to construct a polynomial that passes through the given points. Each method involves calculating coefficients based on the given data points.

- Factorise a polynomial into irreducible factors under any field.
	- Use algorithms like Kronecker's method, Berlekamp's algorithm, or Cantor–Zassenhaus algorithm, depending on the field. For example, in the field of real numbers, factorise by finding roots and using synthetic division.

- Test irreducibility under a given field.
	- Apply Eisenstein's criterion for rational roots or utilize reduction modulo a prime number followed by checking for irreducibility in the reduced polynomial over the finite field.

- Solve a self-reciprocal polynomial.
	- Recognise that if $x$ is a root, then $1/x$ is also a root. Solve for the roots as usual, and then verify the self-reciprocal property.

- Find solutions to a symmetric system.
	- Utilise the symmetry in the equations to reduce the complexity. Sometimes, it involves introducing new variables that simplify the symmetric relations.

- Use roots of polynomials to compute expressions such as $\alpha^{2} + \beta^{2} + \gamma^{2}$.
	- Apply Vieta’s formulas to express the sum of squares of roots in terms of the coefficients of the polynomial. This often involves algebraic manipulation of the polynomial's coefficients.

- Solve a system of congruences.
	- Use the Chinese Remainder Theorem if the moduli are coprime, or apply successive substitution and simplification if the moduli are not coprime.

- Write a multiplication table for a congruence class, then use it to check invertibility and find inverses.
	- Create a table of multiplication for the elements in the congruence class. Invertibility is checked by identifying elements that multiply to 1 modulo $n$. The corresponding element is the inverse.

- Use theory to prove a given congruence class is invertible under a field, and find its inverse.
	- Prove invertibility by showing that the element and the modulus are coprime (using, for example, the Euclidean algorithm). Then, find the inverse either using the Extended Euclidean algorithm or modular arithmetic techniques.
Here are the methods for each of these topics:

- Compute the right-most decimal digit of a given high power, e.g. $7^{1234567}$.
	- Utilise the pattern in the last digit of powers of 7, which repeat every 4 cycles (7, 9, 3, 1). Find the remainder when the exponent (1234567) is divided by 4, and use this to determine the corresponding last digit.

- Compute negative powers using congruence classes.
	- First, find the multiplicative inverse of the base in the given modulus, then compute the positive power of this inverse. This is equivalent to the negative power of the original base.

- Test whether or not certain integers are multiples of other integers, e.g. multiple of 9, 11, as well as others.
	- Use divisibility tests. For 9, check if the sum of the digits is divisible by 9. For 11, calculate the alternating sum of the digits and check if it's divisible by 11. Similar tests exist for other integers.

- Find the last two decimal digits of a given high power.
	- The last two digits of a number in base 10 are its remainder upon division by 100. Use modular exponentiation to compute the power modulo 100.

- Find the decryption map for an affine map, then decrypt a message.
	- In an affine cipher, if the encryption is $E(x) = (ax + b) \mod m$, the decryption is $D(x) = a^{-1}(x - b) \mod m$, where $a^{-1}$ is the multiplicative inverse of $a$ modulo $m$. Find $a^{-1}$ using the Extended Euclidean algorithm and apply the decryption formula.

- Apply the Factor factorisation trick to find two primes that multiply to give a given integer.
	- This typically involves using methods like trial division, Fermat's factorisation method, or Pollard's rho algorithm, particularly useful if the number is a product of two primes that are close together.

- Find the encrypting and decrypting transformations for a very long string of cipher text, given that we know the two most common characters in the string.
	- For a monoalphabetic substitution cipher, use frequency analysis. Match the most common characters in the ciphertext with the known most common characters in the language. This gives clues about the substitution pattern. Use further analysis to determine the complete transformation.