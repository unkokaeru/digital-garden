# Polynomial Roots and Factorisation

## Unique Factorisation Theorem

Every non-constant polynomial over a field $F$ is a product of irreducible polynomials, in an essentially (meaning the factorisation is only unique up to permuting factors and multiplying them by non-zero constants) unique way.

**Example:** $2x^2+10x+12$
$$
\implies2(x+2)(x+3)\implies(2x+4)(x+3)\implies(x+2)(2x+6)\implies(3x+6)(\frac{2}{3}x+2), \ldots
$$

## Maximum Polynomial Roots

**Theorem:** A polynomial of degree $n \ge 0$ can have at most $n$ distinct roots in a field $F$.

**Clarification:** A polynomial of degree 0 has no roots. This is because any expression of the form $x^0$ is equal to 1, which means the polynomial does not intersect the x-axis, and therefore, has no roots.

**Proof (informal):**
A formal proof would follow the same argument, but by induction.

1. Suppose $f(x)$ is a polynomial with a root $\alpha$. According to the Factor Theorem, we can express $f(x)$ as $f(x) = (x - \alpha) \cdot g(x)$, where $g(x)$ is a polynomial of degree $n-1$.
  
2. Now, let's assume $f(x)$ has another distinct root $\beta$ such that $\beta \ne \alpha$. This means $f(\beta) = 0$. Plugging $\beta$ into our expression, we get $0 = (\beta - \alpha) \cdot g(\beta)$. Since $\beta - \alpha$ is non-zero (because $\beta$ and $\alpha$ are distinct), it must be the case that $g(\beta) = 0$. This implies that $\beta$ is also a root of $g(x)$.
   
3. Again using the Factor Theorem, we can express $g(x)$ as $g(x) = (x - \beta) \cdot h(x)$, where $h(x)$ is a polynomial of degree $n-2$.
   
4. Continuing this process, we can express $f(x)$ in terms of its roots. But this method will allow us to find at most $n$ distinct roots for the polynomial. $\blacksquare$

**Note:** The process might terminate before identifying $n$ distinct roots. This could occur if a root is repeated multiple times or if a factor of $f$ does not have any roots in field $F$.

An interesting corollary of this theorem is that a polynomial can be uniquely determined by $n+1$ points on the curve, where $n$ is the order of the polynomial.
## Interpolation Theorem

**Theorem:** Let $b_1,\ldots, b_n$ be distinct elements of a field $F$ and $c_1,\ldots,c_n$ be arbitrary elements of the same field. There exists a unique polynomial $f(x) \in F[x]$ of degree at most $n-1$ that satisfies:
$$
f(b_1) = c_1, \quad f(b_2) = c_2, \quad \ldots, \quad f(b_n) = c_n.
$$
*This theorem is foundational for various modelling techniques.*

Using the theorem is trivial, just substitute in the values, then create a system of equations, then solve that system.

For a polynomial of degree 0 or 1, the theorem is straightforward. For polynomials of higher degrees, the proof can be articulated as follows:
### Proof:

**Existence:** 

For each $i$ in $\{1, 2, ..., n\}$, define the **Lagrange basis polynomial** $L_i(x)$ as:
$$L_i(x) = \prod_{1 \leq j \leq n, j \neq i} \frac{x - b_j}{b_i - b_j}$$

Observe that:

1. $L_i(b_i) = 1$
2. $L_i(b_j) = 0$ for $j \neq i$

Now, let's define our interpolating polynomial $f(x)$ as:
$$f(x) = \sum_{i=1}^{n} c_i L_i(x)$$

Using properties of $L_i(x)$, it's clear that for every $i$, we have:
$$f(b_i) = \sum_{j=1}^{n} c_j L_j(b_i) = c_i$$

This is because $L_j(b_i)$ will be 0 for all $j \neq i$ and $L_i(b_i)$ will be 1. 

Thus, $f(x)$ satisfies the given conditions for interpolation.

**Uniqueness:** 

Assume there exists another polynomial $g(x)$ of degree $< n$ that satisfies the given conditions. Then consider the polynomial $h(x) = f(x) - g(x)$. $h(x)$ is also a polynomial of degree $< n$.

Since both $f(x)$ and $g(x)$ satisfy the conditions:
$$h(b_i) = f(b_i) - g(b_i) = c_i - c_i = 0$$

for all $i = 1, ..., n$.

Thus, $h(x)$ is a polynomial of degree $< n$ with at least $n$ roots. This is a contradiction, unless $h(x)$ is identically zero. Hence, $f(x) = g(x)$, and the interpolating polynomial is unique.

### Conclusion:

Using Lagrange interpolation, we have demonstrated that a unique polynomial $f(x)$ exists such that it satisfies the given interpolation conditions.