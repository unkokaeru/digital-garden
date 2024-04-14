# Gaussian Elimination

Gaussian elimination is a fundamental algorithm in linear algebra used to solve systems of linear equations and find the solutions to such systems. It is named after Carl Friedrich Gauss, a German mathematician who contributed significantly to the field of mathematics in the late 18th and early 19th centuries.

## Introduction

In Gaussian elimination, the goal is to transform a system of linear equations into row-echelon form (or reduced row-echelon form) through a series of elementary row operations. These operations include swapping rows, multiplying a row by a nonzero scalar, and adding a multiple of one row to another row. The process continues until the system is simplified enough to easily read off the solution.

## Steps of Gaussian Elimination

1. **Formulation of Augmented Matrix**: The system of linear equations is first written in an augmented matrix form, with the coefficients of the variables on the left side and the constants on the right side.

2. **Row Operations**: Through a series of row operations (such as row switching, scaling, and row addition), the augmented matrix is transformed into row-echelon form.

3. **Back Substitution**: Once the matrix is in row-echelon form, the variables can be solved for by working backward from the bottom equation to the top equation.

## Example

Consider the following system of linear equations:

$$\begin{align*}
2x+ y&= 5\\
4x- 2y&=-6\end{align*}$$

This system can be represented in augmented matrix form as:

$$\begin{bmatrix}
2& 1&|& 5\\
4&-2&|&-6\end{bmatrix}$$

Applying Gaussian elimination, we can transform this matrix into row-echelon form and solve for the values of $x$ and $y$.

## Historical Context

Gaussian elimination was introduced by Carl Friedrich Gauss in the early 19th century and has since become a cornerstone of computational mathematics. Gauss made significant contributions to various fields of mathematics, including number theory, statistics, and differential equations.

## Real-life Example

A real-life application of Gaussian elimination can be observed in engineering, where it is used to solve systems of linear equations that arise in circuit analysis, structural analysis, and signal processing. Engineers use Gaussian elimination to determine currents flowing in electrical circuits, forces acting on structural components, and filter coefficients in signal processing algorithms.

## Exam Questions

1. Solve the following system of linear equations using Gaussian elimination:
$$\begin{align*}
3x+ 2y&= 7\\
6x- 4y&=-2\end{align*}$$

2. Describe the three elementary row operations used in Gaussian elimination. Provide an example for each operation.

3. Explain the significance of Gaussian elimination in the context of computational mathematics and its impact on various fields.