# Irreducible Polynomials

## Definition

An **irreducible polynomial** is a non-constant polynomial that cannot be expressed as the product of two non-constant polynomials. It's the polynomial equivalent of a prime number in the integers.

In mathematical terms, a polynomial $p(x)$ over a field $F$ is said to be irreducible over $F$ if it cannot be written as the product of two non-constant polynomials from $F[x]$ ([note](note-for-irreducible-polynomials.md)). If such a decomposition is possible, we say $p(x)$ is **reducible**.

*Note: constant polynomials are neither reducible nor irreducible (by convention), whilst polynomials of degree 1 are always irreducible, trivially.*

It is of course also important to note which field the irreducibility is being tested, for example $x^2 + 1$ is irreducible in the real numbers, but reducible to $(x+i)(x-i)$ in the complex numbers.

## Importance

Irreducibility is a central concept in polynomial factorization, algebraic number theory, and several areas of algebra. It helps us understand the structure and properties of polynomials and their roots.

## Test for Irreducibility

There are several methods to test for irreducibility:

**Quadratic Polynomials:** Given an order 2 polynomial
$$
p(x)=ax^2+bx+c
$$
with integer coefficients, the polynomial is reducible precisely when $b^2-4ac$ is a square in $F$.

**Rational Root Theorem:** Given a polynomial 
$$ p(x) = a_nx^n + a_{n-1}x^{n-1} + \dots + a_2x^2 + a_1x + a_0 $$
with integer coefficients, if the polynomial has a rational root $\frac{p}{q}$, then $p$ divides $a_0$ and $q$ divides $a_n$.

## Example

Consider the polynomial $p(x) = x^2 - 2$.

Using the Rational Root Theorem, the only potential rational roots are ±1 and ±2. Evaluating the polynomial at these values, we see that none of them are roots. Thus, $p(x) = x^2 - 2$ doesn't have any rational roots. It also turns out to be irreducible over the rational numbers, but its roots are $\sqrt{2}$ and $-\sqrt{2}$, which are irrational.

This can be checked by using the discriminant :
$$b^2-4ac\implies 0-4\cdot1\cdot(-2)\implies8\gt0\therefore\text{no rational roots.}$$

## Exercise

Check if the polynomial $q(x) = x^3 - 3x + 2$ is reducible over the rationals.

## Conclusion

Irreducible polynomials play a fundamental role in understanding the structure of polynomial equations. Being able to determine whether a polynomial is irreducible is an important skill in higher-level mathematics. Always remember to test for potential roots using tools like the Rational Root Theorem, but also be aware that this is just one step in determining irreducibility.