# Gaussian Elimination

Gaussian Elimination is a fundamental algorithm in linear algebra for solving systems of linear equations, finding the rank of a matrix, and determining the invertibility of square matrices. It systematically transforms a given matrix into a row echelon form (REF) or reduced row echelon form (RREF) through a series of row operations. These operations are row swapping, row multiplication, and row addition, all aimed at creating zeros below the leading entries in each column to simplify the system.

## Historical Context

The method is named after Carl Friedrich Gauss, a German mathematician and physicist who made significant contributions across many fields of mathematics and science in the late 18th and early 19th centuries. However, methods similar to Gaussian Elimination were known to ancient civilizations, including the Chinese, who used it in the Nine Chapters on the Mathematical Art over 2000 years ago.

## Process

The Gaussian Elimination process involves three main steps:

1. **Forward Elimination**: The goal is to transform the original matrix into an upper triangular form or row echelon form. Starting from the first row, we make the elements below the pivot (the first non-zero element from the left in a row) zero by subtracting a suitable multiple of the pivot row from the rows below it.

2. **Back Substitution**: Once the matrix is in upper triangular form, we solve for the variables starting from the bottom row, where the last variable can be directly solved. We then substitute this value into the above rows to find the other variables successively.

3. **(Optional) Row Reduction**: To achieve the reduced row echelon form (RREF), additional steps are taken to make the pivot elements 1 (if they are not already) and to ensure that the pivot is the only non-zero entry in its column by eliminating above the pivot.

## Applications

Gaussian Elimination is used in various fields of science and engineering for solving linear systems, which is crucial for modeling and solving real-world problems. It is also a foundational algorithm for more complex numerical methods and linear algebra operations, such as matrix inversion and determinant calculation.

## Example

Consider the system of linear equations:

$$
\begin{align*}
2x + 3y - z &= 5 \\
4x + 4y - 3z &= 3 \\
-2x + 3y - 2z &= -1
\end{align*}
$$

The goal is to apply Gaussian Elimination to solve for $x$, $y$, and $z$.

### Test Questions

1. What are the row operations used in Gaussian Elimination?
2. Explain the difference between row echelon form (REF) and reduced row echelon form (RREF).
3. Solve the following system of equations using Gaussian Elimination:
   $$
   \begin{align*}
   x + 2y - z &= 2 \\
   3x - y + 2z &= 1 \\
   2x + y + z &= 3
   \end{align*}
   $$

