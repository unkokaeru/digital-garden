# Converting between Cartesian and Polar Coordinates

## Introduction
In mathematics, two common coordinate systems are used to specify the position of a point in a plane: Cartesian and polar coordinates. Cartesian coordinates are denoted in the form (x, y), representing points in terms of their horizontal (x) and vertical (y) distances. In contrast, polar coordinates use the form (r, $\theta$), where 'r' is the radius (distance from the origin) and '$\theta$' (theta) is the angle from the positive x-axis.

Understanding how to convert between these two systems is crucial in various fields like physics, engineering, and computer graphics.

## Cartesian to Polar Conversion
To convert Cartesian coordinates (x, y) to polar coordinates (r, $\theta$):

1. **Radius (r):** The radius is the distance of the point from the origin (0, 0). It is calculated using the Pythagorean theorem:
   
   $$r = \sqrt{x^2 + y^2}$$

2. **Angle ($\theta$):** The angle is measured from the positive x-axis to the line segment that joins the point to the origin. It is calculated using the arctan function, but remember to consider the quadrant in which the point lies:

   $$\theta = \arctan\left(\frac{y}{x}\right)$$
   
   Adjust $\theta$ based on the quadrant:
   - In the 2nd and 3rd quadrants, add π to $\theta$.
   - In the 4th quadrant, add 2π to $\theta$ if you need a positive angle.

## Polar to Cartesian Conversion
To convert polar coordinates (r, $\theta$) to Cartesian coordinates (x, y):

1. **X-coordinate:** It's the horizontal distance, calculated as:

   $$x = r \cos(\theta)$$

2. **Y-coordinate:** It's the vertical distance, calculated as:

   $$y = r \sin(\theta)$$

## Example
Consider a point P with Cartesian coordinates (3, 4). To convert it to polar coordinates:

1. Radius: $r = \sqrt{3^2 + 4^2} = 5$
2. Angle: $\theta = \arctan\left(\frac{4}{3}\right) \approx 53.13^\circ$ or $\approx 0.93$ radians.

Thus, the polar coordinates are approximately (5, 0.93).

## Conclusion and Test Questions
Understanding the conversion between Cartesian and Polar Coordinates is vital in many mathematical and practical applications. It allows us to approach problems from different perspectives and apply various mathematical tools.

### Test Questions
1. Convert the Cartesian coordinates (-3, 3) to polar coordinates.
2. Convert the polar coordinates (4, π/4) to Cartesian coordinates.
3. If a point in polar coordinates is given as (6, π/3), what are its Cartesian coordinates?