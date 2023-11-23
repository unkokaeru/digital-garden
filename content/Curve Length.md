# Curve Length

Curve length, also known as arc length, is a fundamental concept in mathematics, particularly in calculus and geometry. It refers to the distance along a curved line or the length of a curve.

## Definition

The length of a curve $C$ from a point $A$ to a point $B$ is defined as the limit of the sum of line segment lengths that approximate the curve as the number of segments approaches infinity. Mathematically, for a curve defined by a function $y = f(x)$ from $x = a$ to $x = b$, the curve length $L$ is given by:

$$L = \int_{a}^{b} \sqrt{1 + \left( \frac{dy}{dx} \right)^2} \, dx$$

For a parametrically defined curve $x = g(t)$, $y = h(t)$, the formula becomes:

$$L = \int_{a}^{b} \sqrt{\left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2} \, dt$$

### Derivation

This derived with Pythagoras and the idea that the length of a curve at an infinitesimally small length $\Delta s=\sqrt{(\Delta x)^2+(\Delta y)^2}$, which can then be divided by $(\Delta x)^2$ in the square root and then balanced by multiplying $\Delta x$ outside of the square root, giving the required result.

The derivation is similar for a parametrically defined curve.

## Historical Context

The concept of curve length dates back to ancient Greece, where mathematicians like Archimedes began exploring the lengths of curves. The development of calculus by Newton and Leibniz in the 17th century provided the necessary tools for a more rigorous and general approach to determining curve lengths.

## Applications

- **Physics**: Calculating the length of a trajectory.
- **Engineering**: Determining the material needed for curved structures.
- **Computer Graphics**: In rendering curves and computing their properties.

## Examples

1. **Circle Arc**: For a circle of radius $r$, the length of an arc with angle $\theta$ (in radians) is $L = r\theta$.
2. **Parabola**: Finding the length of a segment of a parabola involves integrating the square root of a quadratic expression.

## Test Questions

1. Calculate the length of the curve $y = x^2$ from $x = 0$ to $x = 1$.
2. For a circle of radius 5, what is the length of an arc subtending a $\frac{\pi}{2}$ angle at the center?
3. Determine the length of the curve defined by $x = \cos(t)$, $y = \sin(t)$ from $t = 0$ to $t = \frac{\pi}{2}$.

---

This note aims to provide a foundational understanding of curve length, integrating historical perspectives and practical examples. For a deeper exploration, consider investigating more complex curves and their properties.