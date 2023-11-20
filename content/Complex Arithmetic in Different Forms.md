# Complex Arithmetic in Different Forms

## Introduction

Complex numbers, a fundamental concept in mathematics, extend the idea of the one-dimensional number line to a two-dimensional complex plane. This note delves into complex arithmetic in various forms, primarily focusing on the rectangular (a + bi) and polar (r(cos θ + i sin θ)) forms.

## Rectangular Form

In the rectangular form, a complex number is expressed as $a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit with the property $i^2 = -1$.

### Operations:

1. **Addition/Subtraction**: Add or subtract corresponding real and imaginary parts.
   - $(a + bi) \pm (c + di) = (a \pm c) + (b \pm d)i$

2. **Multiplication**: Use distributive law and simplify using $i^2 = -1$.
   - $(a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i$

3. **Division**: Multiply numerator and denominator by the conjugate of the denominator.
   - $\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}$

## Polar Form

A complex number in polar form is represented as $r(\cos \theta + i \sin \theta)$, where $r$ is the magnitude and $\theta$ is the angle with the positive real axis.

### Operations:

1. **Multiplication**: Multiply the magnitudes and add the angles.
   - $r_1(\cos \theta_1 + i \sin \theta_1) \cdot r_2(\cos \theta_2 + i \sin \theta_2) = r_1r_2(\cos(\theta_1 + \theta_2) + i \sin(\theta_1 + \theta_2))$

2. **Division**: Divide the magnitudes and subtract the angles.
   - $\frac{r_1(\cos \theta_1 + i \sin \theta_1)}{r_2(\cos \theta_2 + i \sin \theta_2)} = \frac{r_1}{r_2}(\cos(\theta_1 - \theta_2) + i \sin(\theta_1 - \theta_2))$

3. **De Moivre's Theorem**: Useful for raising a complex number to a power.
   - $[r(\cos \theta + i \sin \theta)]^n = r^n(\cos(n\theta) + i \sin(n\theta))$

## Historical Context

The concept of complex numbers emerged in the 16th century, primarily in the works of Gerolamo Cardano and Rafael Bombelli. They were initially met with skepticism but gradually became essential in various fields of mathematics and physics.

## Examples

1. **Addition in Rectangular Form**: $(3 + 4i) + (1 - 2i) = 4 + 2i$
2. **Multiplication in Polar Form**: $2(\cos 45^\circ + i \sin 45^\circ) \cdot 3(\cos 30^\circ + i \sin 30^\circ)$

## Test Questions

1. STARTI [Basic] Question: Simplify $(2 + 3i) \cdot (1 - 4i)$. Back: $14 + 5i$. ENDI
2. STARTI [Basic] Question: Express $1 + i$ in polar form. Back: $\sqrt{2}(\cos 45^\circ + i \sin 45^\circ)$. ENDI
3. STARTI [Basic] Question: Use De Moivre's Theorem to find $(1 + i)^4$. Back: $-4$. ENDI

---

For further exploration, consider creating notes on related topics such as [[Euler's Formula]] and [[Applications of Complex Numbers in Engineering]].
