## Remainder, Factor Theorems, Ruffini’s Rule, and Polynomial Algebra

---

### Remainder Theorem:

1. **Definition**: When a polynomial $P(x)$ is divided by a linear divisor $x - a$, the remainder is equal to $P(a)$.

### Factor Theorem:

1. **Definition**: For a polynomial $P(x)$, if $P(a) = 0$, then $x - a$ is a factor of $P(x)$.

2. **Connection with Remainder Theorem**: The Factor Theorem is essentially a special case of the Remainder Theorem. If the remainder when $P(x)$ is divided by $x - a$ is zero, then $x - a$ is a factor of $P(x)$.

### Ruffini's Rule:
Ruffini's Rule, also known as Ruffini's Horner's method, is a quick polynomial division technique when dividing a polynomial by a linear divisor of the form $x - c$. It's especially useful for synthetic division.

Let's go step-by-step:

**Ruffini's Rule Procedure**

1. **Setup**: 
    - Write down the polynomial you want to divide. Let's call this polynomial $P(x)$.
    - Identify the divisor. It should be in the form $x - c$ or $x + c$.
    - List the coefficients of $P(x)$ in descending order of the degree of each term.

2. **Initialize the table**:
    - Draw a horizontal line and a vertical line to create a small 'L' shape.
    - Above the horizontal line and to the left of the vertical line, write the value of $c$.
    - Next to $c$ and above the horizontal line, write down the coefficients of $P(x)$ in order, starting from the highest degree. If a degree is missing, place a 0 for that coefficient. This creates the first row of numbers.

3. **First Entry**:
    - Bring down the leading coefficient (the leftmost number of the first row) as it is. Write it below the horizontal line to start a new row.

4. **Multiplication and Addition**:
    - Multiply the number you just wrote below the line by $c$ (the value you placed at the corner of the 'L' shape). Write the result below the next coefficient in the first row.
    - Add the coefficient from the first row and the result you just obtained. Write this sum below the line, creating the next entry in the second row.
    - Continue this process of multiplying, then adding, for all the coefficients in the first row.

5. **Result**:
    - Once you've gone through all the coefficients, the numbers in the second row represent the coefficients of the quotient polynomial in descending order.
    - The rightmost number in the second row represents the remainder.
  
6. **Interpret the Answer**:
    - The coefficients obtained in the second row (except for the last number) represent the quotient polynomial.
    - If the remainder is 0, it means $P(x)$ is completely divisible by $x - c$. If the remainder is not 0, then it's the remainder when $P(x)$ is divided by $x - c$.

**Example**: Let's illustrate with an example.

Let's say we are dividing $P(x) = x^3 - 6x^2 + 11x - 6$ by $x - 1$:

1. We set up our polynomial and identify our divisor as $x - 1$. So, $c = 1$.
2. We write 1 at the corner of our 'L' shape and list our coefficients as 1, -6, 11, and -6.
3. The leading coefficient, 1, is brought straight down.
4. We multiply this 1 by $c$, which gives 1. We then add this to the next coefficient, -6, giving -5.
5. We continue this process. Multiplying -5 by 1 gives -5, which when added to 11 gives 6. Then, multiplying 6 by 1 and adding to -6 gives 0.
6. Our final row is 1, -5, 6, and 0. This means our quotient polynomial is $x^2 - 5x + 6$ and our remainder is 0.

The procedure described above may sound a bit lengthy due to the verbose nature of the explanation, but in practice, Ruffini's Rule is a quick and efficient method to perform polynomial division by a linear divisor.

**Tabular Example**
The table is set up as shown below

| (2) | 3   | 0   | -6  | 2   |
| --- | --- | --- | --- | --- |
|     | 0    |     |     |     |
|     | 3    |     |     |     |
Then slowly we apply the procedure as described above.

| (2) | 3   | 0   | -6  | 2   |
| --- | --- | --- | --- | --- |
|     | 0   | 6   | 12  | 12  |
|     | 3   | 6   | 6   | 14  | 
Thus $q(x)=3x^2+6x+6$, $r(x) = \frac{14}{x-2}$.
### Application to Factorising $x^n \pm a^n$:

1. **Factorisation of $x^n - a^n$**:
   $x^n - a^n$ can be factored as $(x-a)(x^{n-1} + x^{n-2}a + x^{n-3}a^2 + \dots + xa^{n-2} + a^{n-1})$

2. **Factorisation of $x^n + a^n$** for odd $n$:
   $x^n + a^n$ can be factored using similar principles as $x^n - a^n$, but the signs within the factors will alternate.

$$
p(x)=x^3+2x^2-x-3=a_1(x-2)^3+a_2(x-2)^2+a_3(x-2)+a_4
$$
$$
p(x)=(x-2)q(x)+a_4
$$
$$
\text{for }q(x)=a_1(x-2)^2+a_2(x-2)+a_3
$$
We can continue this, slowly decomposing the polynomial $p(x)$. This proves how we can find the coefficients (if continued).
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