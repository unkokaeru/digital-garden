# Gauss-Jordan Elimination

Gauss-Jordan Elimination is an extension of the Gaussian Elimination method for solving systems of linear equations. It further simplifies the matrix obtained from Gaussian Elimination into a reduced row echelon form (RREF), making the solution to the system of equations more straightforward to interpret. This method not only facilitates the solving of linear equations but also aids in finding the inverse of matrices and the rank of a matrix.

## Historical Context

The Gauss-Jordan Elimination method is named after Carl Friedrich Gauss and Wilhelm Jordan. Gauss was a prolific German mathematician whose work in the early 19th century laid the foundation for much of modern mathematics and physics. Wilhelm Jordan later refined Gauss's methods in the late 19th century, contributing to the development of the technique now known as Gauss-Jordan Elimination.

## Process

The Gauss-Jordan Elimination process consists of the following steps:

1. **Forward Elimination**: Similar to Gaussian Elimination, the matrix is first converted into an upper triangular form or row echelon form (REF) by applying row operations that eliminate the elements below the leading entry in each column.

2. **Pivot Normalization**: Each leading entry in a row (pivot) is normalized to 1, if it is not already, by dividing the entire row by the value of the pivot.

3. **Backward Elimination**: Unlike Gaussian Elimination, Gauss-Jordan Elimination also eliminates the elements above each leading entry, thus achieving a reduced row echelon form (RREF). This is done by subtracting suitable multiples of each row from the rows above it to create zeros above the pivot elements as well.

#### Example

Solve the following system:

$$
\begin{cases}
x_{1}+2x_{2}-3x_{3}+x_{4}=2 \\
2x_{1}+4x_{2}-4x_{3}+6x_{4}=10 \\
3x_{1}+6x_{2}-6x_{3}+9x_{4}=13
\end{cases}
$$

$$
\iff
\begin{bmatrix}
1 & 2 & -3 & 1 & | & 2 \\
2 & 4 & -4 & 6 & | & 10 \\ 
3 & 6 & -6 & 9 & | & 13
\end{bmatrix}
$$

$$
\iff
\begin{bmatrix}
1 & 2 & -3 & 1 & | & 2 \\ 
0 & 0 & 1 & 2 & | & 3 \\ 
0 & 0 & 3 & 6 & | & 7 \\ 
\end{bmatrix}
$$

$$
\iff
\begin{bmatrix}
1 & 2 & -3 & 1 & | & 2 \\ 
0 & 0 & 1 & 2 & | & 3 \\ 
0 & 0 & 0 & 0 & | & -2 \\ 
\end{bmatrix}
$$

...no solutions due to the third equation. Ensure actual working contains the row transformations, in the form like $R_{3}=R_{3}-3R_{2}$, for example.

## Applications

Gauss-Jordan Elimination is widely used in linear algebra for various purposes, including:
- Solving systems of linear equations
- Determining the inverse of matrices
- Computing the rank of a matrix
- Solving linear optimization problems

Its ability to reduce matrices to RREF makes it particularly useful for computational applications where a clear and direct solution is advantageous.

## Example

Consider the system of linear equations:

$$
\begin{align*}
x + 2y - z &= 8 \\
2x - y + 3z &= 1 \\
4x + y + z &= 2
\end{align*}
$$

Applying Gauss-Jordan Elimination will simplify this system into a form where the solution for $x$, $y$, and $z$ can be directly read off from the matrix.

### Test Questions

1. Describe the difference between Gaussian Elimination and Gauss-Jordan Elimination.
2. What are the advantages of reducing a matrix to reduced row echelon form (RREF)?
3. Apply Gauss-Jordan Elimination to solve the following system of equations:
   $$
   \begin{align*}
   x + y + z &= 6 \\
   2x + 3y + 2z &= 14 \\
   4x + 7y + 3z &= 24
   \end{align*}
   $$

This note format, when used within Obsidian, enables effective organization and review of mathematical concepts, particularly suited for academic study in fields requiring a deep understanding of linear algebra techniques. Coupled with the creation of flashcards, this approach reinforces learning through active recall and spaced repetition.