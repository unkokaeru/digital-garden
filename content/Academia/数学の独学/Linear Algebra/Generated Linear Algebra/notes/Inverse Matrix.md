# Inverse Matrix

## Definition

Given a square matrix $A$, the inverse of $A$, denoted as $A^{-1}$, is a matrix such that when $A$ is multiplied by $A^{-1}$, it results in the identity matrix $I$. 

In other words, if $A$ is an $n\times n$ matrix, and $A^{-1}$ is also an $n\times n$ matrix, then $A\cdot A^{-1}= A^{-1}\cdot A= I$, where $I$ is the identity matrix of size $n\times n$.


## Existence of Inverse

Not all square matrices have inverses. For a matrix to have an inverse, it must be a non-singular matrix, which means its determinant is non-zero. If the determinant of a square matrix $A$ is zero, then it is a singular matrix and does not have an inverse.

## Computing the Inverse

The inverse of a square matrix $A$ can be computed using various techniques, such as Gaussian elimination, adjoint method, or using matrix algebra. One common method to find the inverse of a matrix is by using the formula:

$$ A^{-1}=\frac{1}{\text{det}(A)}\text{adj}(A)$$

where $\text{adj}(A)$ is the adjugate matrix of $A$, and $\text{det}(A)$ is the determinant of $A$.

## Properties of Inverse Matrix

- If $A$ has an inverse, then $(A^{-1})^{-1}= A$.
- If $A$ and $B$ are invertible matrices of the same size, then $AB$ is also invertible, and $(AB)^{-1}= B^{-1}A^{-1}$.
- If $A$ is an invertible matrix, then $A^T$ (transpose of $A$) is also invertible, and $(A^T)^{-1}=(A^{-1})^T$.

## Historical Context

The concept of the inverse of a matrix has been pivotal in the development of various areas of mathematics, especially in linear algebra. The foundational work on matrices and their inverses dates back to the 19th century and has played a crucial role in the development of modern algebra.

## Real-Life Example

Consider a system of linear equations representing a network of roads. The coefficients of the equations can be represented as a matrix. If we have the inverse of this matrix, we can efficiently solve for the transportation flow on each road, which can aid in traffic optimization and city planning.

## Exam Questions

1. Define the inverse of a matrix and explain why not all matrices have inverses.
2. Compute the inverse of the following $2\times 2$ matrix: $A=\begin{bmatrix} 2& 1\\ 1& 3\end{bmatrix}$.
3. Prove that if $A$ is an invertible matrix, then $kA$ is also invertible for any $k\neq 0$, and find an expression for $(kA)^{-1}$ in terms of $A^{-1}$ and $k$.