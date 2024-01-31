### Biquadratic Polynomials

Biquadratic polynomials are fourth-degree polynomials characterized by the highest power of the variable being four, and they are in the general form $ax^4 + bx^2 + c$ with the condition that $a \neq 0$. The absence of the $x^3$ and $x$ terms simplifies the solving process, as one can often factor these polynomials into products of quadratic factors.

#### Example Expansion:
Consider the biquadratic polynomial $x^4 - 6x^2 + 9$. We aim to find its roots by factoring. Notice that the polynomial resembles a quadratic in form, with $x^2$ taking the place of $x$. This observation allows us to factor it as if it were a quadratic:

$$
(x^2 - 3)^2 = 0
$$

By setting each factor equal to zero, we find that:

$$
x^2 - 3 = 0 \implies x^2 = 3 \implies x = \pm \sqrt{3}
$$

Thus, the roots of the original biquadratic polynomial are $\pm \sqrt{3}$.

### Self-Reciprocal Polynomials

A self-reciprocal polynomial has a fascinating property: if one substitutes $x$ with $\frac{1}{x}$, the form of the polynomial remains unchanged. Mathematically, this is expressed as $P(x) = x^nP(\frac{1}{x})$.

#### Example Clarification:
For the polynomial $x^2 + 2x + 1$, let's test for self-reciprocity. Replacing $x$ with $\frac{1}{x}$, we get:

$$
1 + 2 + x^2 \neq x^2 + 2x + 1
$$

This result is not the same as the original polynomial, thus $x^2 + 2x + 1$ is not self-reciprocal.

#### Solving Self-Reciprocal Polynomials:
The solving process for self-reciprocal polynomials involves manipulation to take advantage of their structure. Given a polynomial:

$$
ax^4+bx^3+cx^2+bx+a=0
$$

Divide through by $x^2$ to get:

$$
a\left(x^2+\frac{1}{x^2}\right)+b\left(x+\frac{1}{x}\right)+c=0
$$

Next, recognize that $x^2 + \frac{1}{x^2}$ can be rewritten using the identity $x + \frac{1}{x}$, giving us a transformed quadratic equation:

$$
a\left(x+\frac{1}{x}\right)^2+b\left(x+\frac{1}{x}\right)+(c-2a)=0
$$

Solving for $x+\frac{1}{x}$ yields:

$$
x+\frac{1}{x}=\frac{-b\pm\sqrt{b^2-4a(c-2a)}}{2a}=k
$$

We simplify the quadratic formula to reach a constant $k$, and solve the new quadratic equation:

$$
x^2-kx+1=0
$$

Hence:

$$
x=\frac{k\pm\sqrt{k^2-4}}{2}
$$

With $k$ derived from the earlier step as:

$$
k=\frac{-b\pm\sqrt{b^2-4a(c-2a)}}{2a}
$$

### Square Roots of Complex Numbers

To find the square root of a complex number $a + bi$, we use the following formula:

$$
\sqrt{a + bi} = \pm \left( \sqrt{\frac{a + \sqrt{a^2 + b^2}}{2}} + i\sqrt{\frac{-a + \sqrt{a^2 + b^2}}{2}} \right)
$$

#### Example Elaboration:
To find $\sqrt{1 + i}$:

$$
\sqrt{1 + i} = \sqrt{\frac{1 + \sqrt{2}}{2}} + i\sqrt{\frac{-1 + \sqrt{2}}{2}}
$$

This provides the square root of the complex number in its algebraic form.

### Relations Between Roots and Coefficients of a Quadratic Polynomial

For any quadratic polynomial $ax^2 + bx + c$, if $\alpha$ and $\beta$ are its roots, they relate to the coefficients as follows:

- The sum of the roots $\alpha + \beta$ equals the negation of the coefficient of $x$ divided by the coefficient of $x^2$: $\alpha +

 \beta = -\frac{b}{a}$.
- The product of the roots $\alpha \beta$ equals the constant term divided by the coefficient of $x^2$: $\alpha \beta = \frac{c}{a}$.

### Symmetric Systems

A symmetric system of equations is one in which interchanging the variables does not alter the system. It is often represented in matrix form, and a key property of a symmetric matrix is that it is equal to its transpose $A = A^T$.

#### Example Illustration:
Consider the matrix:

$$
\begin{pmatrix}
  1 & 2 \\
  2 & 1
\end{pmatrix}
$$

This matrix is symmetric because it remains the same when flipped over its main diagonal. The transpose of the matrix, where the rows become columns and vice versa, is identical to the original matrix, confirming its symmetry.