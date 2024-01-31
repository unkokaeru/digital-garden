*Note: update these notes with the notes from my MD notebook, also include the idea that everything depends on the field it's defined in*
## Rational Root Test

The Rational Root Test is a technique to identify potential rational roots of a polynomial with integer coefficients. Given a polynomial

$$ P(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0 $$

where $a_n, a_{n-1}, \ldots, a_0$ are integers, the Rational Root Test tells us that any rational root, when expressed in its lowest terms $\frac{p}{q}$, must satisfy:

1. $p$ is a factor of the constant term $a_0$
2. $q$ is a factor of the leading coefficient $a_n$

To use the Rational Root Test, list all possible values of $\frac{p}{q}$ and then check each one to see if it's a root of the polynomial. 

Formally, to find all rational roots of $f(x)$:
$$
f\left(\frac{r}{s}\right)=0 : (r,s) = 1\implies r|a_0,s|a_n
$$
$$
\implies\frac{r}{s}=\frac{D(a_0)}{D(a_n)}
$$
This is then often followed by a few tricks, like if all values of $a$ are positive then so will the roots. If they instead alternate polarity, the roots will be negative, and so on.

This can also be applied to proving irrationality in a number, e.g. proving $\sqrt{3}$ is irrational by proving that $x^2-3=0$ has no rational roots.

### Example

Given $P(x) = 2x^3 - 4x^2 + 3x - 6$, the possible rational roots are:

$$ \pm \frac{\text{Factors of 6}}{\text{Factors of 2}} = \pm \frac{1, 2, 3, 6}{1, 2} $$

## Irreducibility and Roots in Quadratic and Cubic Polynomials

A polynomial is called "irreducible" if it cannot be factored into polynomials of lower degree with coefficients in the same domain. For quadratic and cubic polynomials with rational coefficients, irreducibility has a simple implication: it won't have any rational roots.

### Quadratics

A quadratic equation $ax^2 + bx + c = 0$ is irreducible over the rationals if its discriminant, $b^2 - 4ac$, is not a perfect square.

If the discriminant is not a perfect square, the quadratic is irreducible over the rationals.

### Cubics

For cubic equations $ax^3 + bx^2 + cx + d = 0$, irreducibility is a bit more involved. However, one simple test is to use the Rational Root Test. If the cubic has no rational roots, it's often—but not always—an indicator that it's irreducible over the rationals.

## Conclusion

The Rational Root Test is an effective way to find potential rational roots in polynomial equations. It's particularly useful for checking irreducibility in quadratics and cubics, although other methods might be required for a definitive proof of irreducibility.