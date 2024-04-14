# Eigenvalue Equation

In linear algebra, the **eigenvalue equation** plays a fundamental role in the study of linear transformations and matrices. Given a square matrix $A$, an eigenvalue $\lambda$ for $A$ is a scalar such that there exists a non-zero vector $\mathbf{v}$ satisfying the equation:

$$ A\mathbf{v}=\lambda\mathbf{v}$$

Here, $\mathbf{v}$ is called an **eigenvector** corresponding to the eigenvalue $\lambda$. This relationship can be rewritten as:

$$(A-\lambda I)\mathbf{v}=\mathbf{0}$$

where $I$ is the identity matrix of the same size as $A$.

Eigenvalues and eigenvectors have numerous applications in mathematics and various scientific fields. They are used in solving systems of linear differential equations, analyzing structures in engineering, and studying quantum mechanics.

## Properties of Eigenvalue Equation:

- Eigenvalues can be complex numbers.
- The sum of all eigenvalues of a matrix is equal to the trace of the matrix.
- The product of all eigenvalues of a matrix is equal to the determinant of the matrix.

## Example:

Consider the matrix

$$ A=\begin{bmatrix} 3& 1\\ 1& 3\end{bmatrix}$$

To find the eigenvalues of $A$, we need to solve the characteristic equation:

$$\text{det}(A-\lambda I)= 0$$

Substitute $A$ into the equation, we get:

$$\text{det}\begin{pmatrix} 3-\lambda& 1\\ 1& 3-\lambda\end{pmatrix}= 0$$

Solving this equation gives us the eigenvalues $\lambda= 2, 4$.

## Historical Context:

The concept of eigenvalues and eigenvectors was introduced by the German mathematician David Hilbert in the early 20th century. Eigenvalues have since become a central tool in many areas of mathematics, physics, and engineering.

## Real-Life Example:

In physics, when studying the vibrational modes of a system, eigenvalues and eigenvectors can help determine the frequencies at which the system oscillates naturally. This information is crucial in understanding the stability and behavior of the system under different conditions.

---

## Exam Questions:

1. Given the matrix $B=\begin{pmatrix} 1& 0\\ 0&-2\end{pmatrix}$, find the eigenvalues and corresponding eigenvectors.
   
2. Prove that the sum of the eigenvalues of a $3\times 3$ matrix is equal to the sum of its diagonal elements.

3. Discuss a real-life application where eigenvalues and eigenvectors are used in solving practical problems.