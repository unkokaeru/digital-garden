> MTH1004 Linear Algebra Cheat Sheet by William Fayers :)

### Linear Algebra Exam Cheat Sheet

#### Eigenvalues and Eigenvectors

- **Characteristic Equation**: $\det(A - \lambda I) = 0$
- **Eigenvector**: Non-zero vector $v$ such that $Av = \lambda v$, where $\lambda$ is an eigenvalue. To solve, first re-arrange to $(A-\lambda I)v=0$, simplify the left matrix, then solve that equation with Gauss-Jordan Elimination. However, it's pretty sensible to check the solution in the original formula form, too (especially if you don't find all the values for a vector, you can assume the missing ones are $1$ and then check it).

#### Diagonalisation

- **Condition**: A matrix $A$ is diagonalisable if it has $n$ linearly independent eigenvectors.
- **Process**:
  1. Find eigenvalues ($\lambda$) using the characteristic equation.
  2. For each $\lambda$, find $(A - \lambda I)v = 0$.
  3. Form $P$ from eigenvectors and $D$ (the result) with eigenvalues on the diagonal.
  4. $P^{-1}AP = D$.
- **Goal**: Form an equivalent matrix with the the eigenvalues on the diagonal.

#### Solving Linear Systems

- **Gauss-Jordan Elimination**: Process for putting a matrix into Reduced Row Echelon Form (RREF).
- **Homogeneous Systems**: $Ax = 0$, solution is vector subspace.
- **Null Space**: Set of all solutions to $Ax = 0$; basis found during RREF.

#### Matrix Inverse and Gauss-Jordan

- **Finding $A^{-1}$**: Augment $A$ with $I$, apply Gauss-Jordan to transform $A$ into $I$, resulting matrix next to $I$ is $A^{-1}$.
- **Condition for Invertibility**: $A$ is invertible if and only if $\det(A) \neq 0$.

#### Basis and Dimension

- **Basis of Vector Space**: Linearly independent set that spans the space.
- **To Prove Basis**: Show set is linearly independent and spans vector space.
- **Dimension**: Number of vectors in a basis for the space.

$\mathbf{u}, \mathbf{v}\in \mathbb{R}^{2}$ are linearly independent if, for $c_{1},c_{2}\in \mathbb{R}$:
$$
c_{1}\mathbf{u}+c_{2}\mathbf{v}=0\implies c_{1}=c_{2}=0
$$

#### Cramer's Rule

Suppose you have a system of $n$ linear equations with $n$ unknowns, represented as:

$$
\begin{align*}
a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \ldots + a_{2n}x_n &= b_2 \\
\vdots \\
a_{n1}x_1 + a_{n2}x_2 + \ldots + a_{nn}x_n &= b_n \\
\end{align*}
$$

This system can be written in matrix form as $AX = B$, where:
- $A$ is the coefficient matrix,
- $X$ is the column matrix of variables $(x_1, x_2, \ldots, x_n)^T$,
- $B$ is the column matrix of constants $(b_1, b_2, \ldots, b_n)^T$.
- 
Cramer's rule states that the solution for each variable $x_i$ is given by:
$$
x_i = \frac{\det(A_i)}{\det(A)}
$$
where $\det(A)$ is the determinant of the coefficient matrix $A$, and $\det(A_i)$ is the determinant of the matrix formed by replacing the $i$-th column of $A$ with the column matrix $B$.

#### Additional Tips

- **Determinant Properties**:
  - $\det(AB) = \det(A)\det(B)$
  - $\det(A^{-1}) = 1/\det(A)$
  - $\det(P^{-1}AP) = \det(A)$
- **Rank Theorem**: $\text{Rank}(A) + \text{Nullity}(A) = n$, where $n$ is the number of columns in $A$, $\text{Rank}(A)$ is the number of pivots in row-echelon form, $\text{Nullity}(A)$ is the dimension of $\text{Null}(A)$.
- **Multiplicities**: An algebraic multiplicity is the number of times an eigenvalue appears as a root of the characteristic equation of a matrix, whilst a geometric multiplicity is the dimension of the eigenspace corresponding to an eigenvalue.
- **Column Space**: $\text{Col}(A)$ is the set of all possible linear combinations of its column vectors, given that they're all independent.
- **Multiplying Matrices**: For a 3x3 matrix $A$ and a 3x1 vector $\mathbf{v}$,
  $$A \mathbf{v}=\begin{pmatrix} a_{11}v_{1} + a_{12}v_{2} + a_{13}v_{3} \\ a_{21}v_{1} + a_{22}v_{2} + a_{23}v_{3} \\ a_{31}v_{1} + a_{32}v_{2} + a_{33}v_{3} \end{pmatrix}$$


---

### Strategy Tips

- **Before the Exam**: Understand each concept, not just memorize formulas.
- **During the Exam**: 
  - Read each question carefully.
  - Plan your approach before writing.
  - Check if an answer makes sense in the context of the question.

#### Problem-Solving Approach

1. **Identify**: Determine what the problem is asking.
2. **Plan**: Choose which formulas or concepts apply.
3. **Execute**: Carry out your plan methodically.
4. **Review**: Check your work for errors or oversights.

___

![[sudoku 1.png]]