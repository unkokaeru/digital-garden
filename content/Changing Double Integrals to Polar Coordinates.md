# Changing Double Integrals to Polar Coordinates

## Overview
Changing double integrals to polar coordinates is a technique used in multivariable calculus. This approach is particularly useful when evaluating integrals over circular or annular regions. The transformation simplifies the computation by aligning the integration region with the geometry of the polar coordinate system.

## Polar Coordinates
In polar coordinates, a point in the plane is represented by a radius $r$ and an angle $\theta$. The relationships between polar coordinates $(r, \theta)$ and Cartesian coordinates $(x, y)$ are:

- $x = r \cos(\theta)$
- $y = r \sin(\theta)$

## Transforming Double Integrals
When transforming a double integral from Cartesian to polar coordinates, the differential area element changes. In Cartesian coordinates, the area element is $dx \, dy$. In polar coordinates, it becomes $r \, dr \, d\theta$.

### The Jacobian
The Jacobian of the transformation is the determinant of the matrix of partial derivatives of $x$ and $y$ with respect to $r$ and $\theta$. For the polar coordinate transformation, the Jacobian is $r$. 

### The Integral
A double integral in Cartesian coordinates:

$$\int \int_R f(x,y) \, dx \, dy$$

transforms into polar coordinates as:

$$\int \int_R f(r\cos(\theta), r\sin(\theta)) \, r \, dr \, d\theta$$

## Examples
### Example 1: Circular Region
Consider a circle of radius $a$. The integral over this region can be transformed into polar coordinates where $r$ ranges from 0 to $a$ and $\theta$ ranges from 0 to $2\pi$.

### Example 2: Annular Region
For an annular region with inner radius $a$ and outer radius $b$, $r$ varies from $a$ to $b$ and $\theta$ from 0 to $2\pi$.

## Conclusion
Converting double integrals to polar coordinates simplifies the computation for circular or annular regions. This method leverages the natural symmetry of these regions in polar coordinates.

## Test Questions
1. What is the Jacobian in the transformation from Cartesian to polar coordinates?
2. How does the area element $dx \, dy$ in Cartesian coordinates change when transformed to polar coordinates?
3. For a double integral over a circle of radius $a$, what are the limits of integration for $r$ and $\theta$ in polar coordinates?