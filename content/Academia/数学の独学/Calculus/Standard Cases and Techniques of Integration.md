# Standard Cases and Techniques of Integration

Integration is a crucial concept in calculus, used in areas like physics, engineering, and mathematics. It helps in calculating areas, solving differential equations, and more. This note explores standard cases, techniques of integration, and includes reduction formulas.

## Basic Definitions

**Integral:** A mathematical representation of the area under a curve over an interval.

- **Indefinite Integral:** Represents a family of functions without specified limits, including a constant of integration $C$.
- **Definite Integral:** An integral with specific upper and lower limits, providing a numerical value for the area under the curve.

## Standard Techniques of Integration

1. **Direct Integration:** Applying known integral formulas.
   - Example: $\int x^2 \, dx = \frac{x^3}{3} + C$

2. **Integration by Substitution:** Simplifying the integral through variable change.
   - Example: $\int 2x \cdot e^{x^2} \, dx$, set $u = x^2$.

3. **Integration by Parts:** Based on differentiation's product rule, for integrals involving products of functions.
   - Formula: $\int u \, dv = uv - \int v \, du$
   - Example: $\int x \cdot e^x \, dx$

4. **Partial Fraction Decomposition:** For rational functions, splitting the fraction into simpler parts.
   - Example: $\int \frac{1}{x^2 - 1} \, dx$

5. **Trigonometric Substitution:** For integrals involving square roots of trigonometric expressions.
   - Example: $\int \sqrt{1 - x^2} \, dx$

6. **Integration of Trigonometric Functions:** Specific techniques for trigonometric integrals.
   - Example: $\int \sin(x) \cos(x) \, dx$

7. **Improper Integrals:** For integrals with infinite limits or discontinuous integrands.
   - Example: $\int_1^\infty \frac{1}{x^2} \, dx$

## Reduction Formulas

Reduction formulas are recursive relations that reduce the power of the function being integrated. They are particularly useful in integrating powers of trigonometric functions.

- **Sine Reduction Formula:** 
  $$\int \sin^n(x) \, dx = -\frac{\sin^{n-1}(x) \cos(x)}{n} + \frac{n-1}{n} \int \sin^{n-2}(x) \, dx$$

- **Cosine Reduction Formula:** 
  $$\int \cos^n(x) \, dx = \frac{\cos^{n-1}(x) \sin(x)}{n} + \frac{n-1}{n} \int \cos^{n-2}(x) \, dx$$

- **Tangent Reduction Formula:** 
  $$\int \tan^n(x) \, dx = \frac{\tan^{n-1}(x)}{n-1} - \int \tan^{n-2}(x) \, dx$$

## Historical Context

Integration's roots trace back to the 17th century with significant contributions from Isaac Newton and Gottfried Wilhelm Leibniz. Their groundbreaking work in calculus laid the groundwork for its extensive modern applications.

## Test Questions

1. **STARTI [Basic] Question:** Calculate $\int 3x^2 \, dx$. **Back:** The integral of $3x^2$ is $x^3 + C$. **ENDI**
2. **STARTI [Intermediate] Question:** Apply integration by parts to $\int x \cdot e^x \, dx$. **Back:** Set $u = x$ and $dv = e^x dx$, leading to $xe^x - \int e^x \, dx = xe^x - e^x + C$. **ENDI**
3. **STARTI [Advanced] Question:** Solve $\int \sin^3(x) \, dx$ using the sine reduction formula. **Back:** Applying the formula, $\int \sin^3(x) \, dx = -\frac{\sin^2(x) \cos(x)}{3} + \frac{2}{3} \int \sin(x) \, dx$. **ENDI**

Incorporating these techniques and formulas in your studies will enhance your understanding and ability to tackle complex integrals. Consider creating flashcards on specific integration techniques or practicing more complex examples to deepen your understanding.