# First Principles and Formal Definition of Integration

## Introduction
Integration is a fundamental concept in calculus, central to many areas of mathematics, physics, engineering, and other sciences. It extends the concept of summing up infinitely many small quantities, offering a way to calculate areas, volumes, and other quantities that require accumulation.

## Historical Context
The concept of integration can be traced back to ancient mathematicians like Archimedes, who used methods resembling integration to calculate areas and volumes. The formal development of calculus in the 17th century by Newton and Leibniz provided a more rigorous foundation for integration, framing it as the inverse process of differentiation.

## First Principles of Integration
### Riemann Sums
At the heart of understanding integration from first principles is the concept of a Riemann sum. It involves dividing the region to be integrated (under a curve, for example) into small segments, approximating the area of each segment, and then summing these areas. The process can be expressed as:

1. Divide the interval $[a, b]$ into $n$ subintervals.
2. In each subinterval, choose a point $x_i$.
3. The area of each rectangle is $f(x_i) \Delta x$, where $\Delta x = \frac{b-a}{n}$.
4. The Riemann sum is $\sum_{i=1}^{n} f(x_i) \Delta x$.

As $n$ approaches infinity, the Riemann sum approaches the exact area, leading to the concept of the definite integral.

### Formal Definition
The formal definition of the definite integral of a function $f$ from $a$ to $b$ is given by:

$$\int_{a}^{b} f(x) \,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \Delta x$$

This expression is read as "the integral from $a$ to $b$ of $f(x)$ with respect to $x$" and represents the limit of the Riemann sums as the number of subintervals goes to infinity.

## Applications
Integration is used extensively in various fields:
- In physics, for calculating quantities like work, energy, and electric potential.
- In engineering, for design and analysis in multiple domains.
- In economics, to model growth and accumulation.
- In probability, to find distributions and expectations.

## Test Questions
1. STARTI [Basic] Question: What is the primary difference between a Riemann sum and a definite integral? Back: A Riemann sum is an approximation made by summing the areas of rectangles under a curve, while a definite integral is the exact area, obtained by taking the limit of the Riemann sum as the number of rectangles approaches infinity. ENDI
2. STARTI [Basic] Question: How would you express the integral of a function $f(x)$ from 0 to 2 using the formal definition? Back: $\int_{0}^{2} f(x) \,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \frac{2}{n}$, where $x_i$ is a sample point in each subinterval. ENDI
3. STARTI [Basic] Question: In what situations is it impossible to use Riemann sums to define an integral? Back: Riemann sums and the corresponding definite integrals cannot be used when the function $f(x)$ is not defined or is discontinuous in the interval $[a, b]$. ENDI

---
Feel free to add more content or adjust existing content to suit the specific needs of your Obsidian vault. Hyperlinks can be integrated for related topics like "calculus", "Riemann sums", or specific mathematicians for a richer learning experience.