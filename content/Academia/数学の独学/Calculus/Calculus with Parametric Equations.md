# Calculus with Parametric Equations

## Introduction
Calculus with Parametric Equations offers a powerful way to analyse curves that cannot be defined as functions of a single variable. These curves, described by parametric equations, allow us to explore more complex geometries and motions.

### What Are Parametric Equations?
Parametric equations involve a set of equations where the coordinates of points on a curve (x and y) are defined as functions of a third variable, typically denoted as 't'. This 't' is a parameter, often representing time, allowing for the description of motion and change in geometry.

### Example:
The simple circular motion can be expressed parametrically as:
$$x(t) = r \cos(t), \quad y(t) = r \sin(t)$$
where $r$ is the radius of the circle and $t$ represents the angle from the positive x-axis.

## Calculus with Parametric Equations

### Differentiation
To find the slope of the tangent to a parametric curve, we differentiate both x and y with respect to t:
$$\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}$$

### Integration
To find the area under a parametric curve, we integrate with respect to the parameter:
$$A = \int y(t) \, dx = \int y(t) \frac{dx}{dt} \, dt$$

### Length of a Parametric Curve
The formula for the length of a parametric curve from $t = a$ to $t = b$ is:
$$L = \int_{a}^{b} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$

## Applications
1. **Physics and Engineering**: Modelling trajectories and movements.
2. **Computer Graphics**: Animating paths and shapes.
3. **Economics**: Analysing dynamic systems over time.

## Historical Context
The concept of parametric equations dates back to the 17th century, with notable contributions from Pierre de Fermat and René Descartes. Their work laid the foundation for modern calculus and analytical geometry.

## Example Problems

### Test Questions
1. STARTI [Basic] Question: If a particle moves along the curve given by x(t) = 3t^2 and y(t) = 2t^3, what is the slope of the tangent line at t = 1? Back: The slope at t = 1 is given by dy/dx = (dy/dt) / (dx/dt). Here, dy/dt = 6t^2 and dx/dt = 6t. So, at t = 1, the slope is 6/6 = 1. ENDI
2. STARTI [Basic] Question: How do you find the length of a parametric curve? Back: The length of a parametric curve from t = a to t = b is given by the integral L = ∫ from a to b of sqrt((dx/dt)^2 + (dy/dt)^2) dt. ENDI
3. STARTI [Basic] Question: For the parametric equations x = sin(t) and y = cos(t), what is the length of the curve from t = 0 to t = π/2? Back: The length is given by the integral ∫ from 0 to π/2 of sqrt((-sin(t))^2 + (-cos(t))^2) dt, which simplifies to π/2. ENDI