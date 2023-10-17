## Remainder, Factor Theorems, Ruffini’s Rule, and Polynomial Algebra

---

### Remainder Theorem:

1. **Definition**: When a polynomial $P(x)$ is divided by a linear divisor $x - a$, the remainder is equal to $P(a)$.

### Factor Theorem:

1. **Definition**: For a polynomial $P(x)$, if $P(a) = 0$, then $x - a$ is a factor of $P(x)$.

2. **Connection with Remainder Theorem**: The Factor Theorem is essentially a special case of the Remainder Theorem. If the remainder when $P(x)$ is divided by $x - a$ is zero, then $x - a$ is a factor of $P(x)$.

### Ruffini's Rule:

1. **Definition**: Ruffini's Rule is a synthetic division method used to divide a polynomial by a linear factor of the form $x - a$. It provides a quick method to obtain the quotient and the remainder.
   
2. **Procedure**:
   - Arrange the polynomial and the divisor.
   - Write down the coefficients of the polynomial.
   - Carry out the synthetic division process.

### Application to Factorising $x^n \pm a^n$:

1. **Factorisation of $x^n - a^n$**:
   $x^n - a^n$ can be factored as $(x-a)(x^{n-1} + x^{n-2}a + x^{n-3}a^2 + \dots + xa^{n-2} + a^{n-1})$

2. **Factorisation of $x^n + a^n$** for odd $n$:
   $x^n + a^n$ can be factored using similar principles as $x^n - a^n$, but the signs within the factors will alternate.

### Expanding a Polynomial in Terms of $x - a$:

Given a polynomial $P(x)$, its expansion in terms of $x - a$ will result in a polynomial in which every term will be of the form $c_k(x - a)^k$, where $c_k$ are coefficients determined by the polynomial and the value of $a$.

### GCD for Polynomials:

1. **Definition**: The greatest common divisor (GCD) of two polynomials is the highest-degree polynomial that divides both of the given polynomials without leaving a remainder.
   
2. **Procedure**: The GCD of polynomials can be found using the polynomial division method or the extended Euclidean algorithm.

### The Extended Euclidean Algorithm for Polynomials:

1. **Definition**: This algorithm is a polynomial version of the extended Euclidean algorithm for integers. It helps find the GCD of two polynomials and represents the GCD as a linear combination of the two polynomials.

2. **Procedure**: The method involves repeated polynomial division, just as the standard extended Euclidean algorithm does with integers.

### Bézout’s Lemma for Polynomials:

1. **Definition**: For polynomials $P(x)$ and $Q(x)$ with a GCD $D(x)$, there exist polynomials $U(x)$ and $V(x)$ such that:
   $$ P(x)U(x) + Q(x)V(x) = D(x) $$

---

## Historical Context:

1. **Remainder and Factor Theorems**: These theorems, foundational to polynomial algebra, have been known since ancient times and have played a pivotal role in algebraic computations and problem-solving.
   
2. **Ruffini's Rule**: Named after Paolo Ruffini, an Italian mathematician who made significant contributions to algebra.
   
3. **Bézout's Lemma**: Named after Étienne Bézout, a French mathematician who first stated and proved this lemma for integers. Its adaptation to polynomials has been instrumental in algebraic computations.

---

## Sample Exam Questions:

1. **Remainder Theorem**: Given the polynomial $P(x) = 2x^3 - 3x^2 + 4x - 5$, determine the remainder when $P(x)$ is divided by $x - 2$.

2. **Factor Theorem**: Using the Factor Theorem, determine whether $x - 3$ is a factor of $Q(x) = x^3 - 6x^2 + 11x - 6$.

3. **Ruffini's Rule**: Use Ruffini's Rule to divide $P(x) = x^3 - 2x^2 - 4x + 8$ by $x + 1$.

4. **Polynomial Expansion**: Expand the polynomial $f(x) = (x - 2)(x - 3)(x - 4)$ in terms of $x - 2$.

5. **Extended Euclidean Algorithm**: Use the extended Euclidean algorithm to find the GCD of the polynomials $A(x) = x^4 - 1$ and $B(x) = x^3 + x^2 + x + 1$.

6. **Conceptual Question**: Describe the importance of Bézout's Lemma in polynomial algebra and its connection to the extended Euclidean algorithm.