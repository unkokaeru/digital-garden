- **Determining Linear Independence**:
  1. Check if the vectors can be written as a linear combination: $\lambda_1u + \lambda_2v = 0$.
  2. Write the system of equations and solve for $\lambda_1, \lambda_2$.
  3. If the only solution is $\lambda_1 = \lambda_2 = 0$, the vectors are linearly independent.

- **Linear Dependence of Vectors**:
  1. Assume the vectors are linearly dependent, so they can be written as: $\lambda_1u + \lambda_2v = 0$ with not all $\lambda$'s being zero.
  2. Check that this system of equations has a non-trivial solution using row operations.

- **Finding Span of Vectors**:
  1. Form a matrix with the given vectors.
  2. Reduce the matrix to its row-echelon form.
  3. The span of the vectors is the set of all possible linear combinations of the vectors.

- **Scalar Calculation for Linear Independence**:
  1. Assume linear dependence.
  2. Set up the linear combination equation for $\lambda$'s.
  3. Choose a value for the parameter for which the vectors become dependent/independent.

- **Determining Linear Combination in Subspace**:
  1. Write down the equation $\lambda_1u + \lambda_2v = u$ for scalar $\lambda_1, \lambda_2$.
  2. Solve the system of equations to find the scalar values.

- **Finding Span of Vectors in $\mathbb{R}^3$**:
  1. Form a matrix with the given vectors.
  2. Find its row-echelon form to determine the span.
  3. Span is all the vectors that can be obtained by scaling and adding the given vectors.

- **Dot Product, Length, and Angle Between Vectors**:
  1. Compute the dot product: $u\cdot v = u_1v_1 + u_2v_2 + \dots$.
  2. Find the lengths of the vectors using $\|u\| = \sqrt{u\cdot u}$.
  3. Calculate the angle between the vectors using $\cos\theta = \frac{u\cdot v}{\|u\|\|v\|}$.

- **Row Echelon Form Solutions**:
  1. Use Gaussian elimination to reduce the matrix to row-echelon form.
  2. Interpret the solutions in terms of the variables.
  3. For each non-pivot column, assign a free variable.

- **Gauss-Jordan Elimination for Solutions**:
  1. Bring the matrix to row-echelon form.
  2. Write the system of equations corresponding to the matrix.
  3. Use back-substitution to solve for the variables.

- **Determining Linear Dependence Using Gaussian Elimination**:
  1. Create an augmented matrix.
  2. Reduce the matrix to row-echelon form.
  3. If a row with all zeros appears, the vectors are linearly dependent.

- **Invertibility Conditions**:
  1. Use the determinant to check invertibility.
  2. If $\det A \neq 0$, matrix A is invertible.
  3. If $\det AB = 0$, then $B$ must be the zero matrix.

- **Cramer's Rule for Linear Systems**:
  1. Form the augmented matrix from the system of equations.
  2. Compute the determinants corresponding to each variable to find the solutions.

- **Vector Subspace Determination**:
  1. Check if the set is closed under vector addition and scalar multiplication.
  2. Verify that the set contains the zero vector.
  3. Confirm that the set follows all vector space properties.

- **Determining Basis of Vector Subspace**:
  1. Use Gaussian elimination to find linearly independent vectors.
  2. Form a basis set from the linearly independent vectors found.

- **Calculating Matrix Rank**:
  1. Reduce the matrix to row-echelon form.
  2. Rank is the number of non-zero rows in row-echelon form.
  3. Nullity is the number of free variables in the system.

- **Matrix Inversion**:
  1. For a $2\times 2$ matrix, use the standard formula for inversion.
  2. Compute the determinant and apply it to find the inverse.

- **Eigenvalues and Eigenvectors Computation**:
  1. Find the characteristic equation by solving $\det(A - \lambda I) = 0$.
  2. Solve for eigenvalues and then find the corresponding eigenvectors by solving $(A - \lambda I)v = 0$.

- **Proving Properties of Matrices**:
  1. Use matrix properties to simplify the expressions.
  2. Verify that the determinant of the given matrices satisfies the properties.

- **Using Cramer's Rule for Solutions**:
  1. Compute determinants for different part of the system.
  2. Use Cramer's Rule to find the values of the variables.

- **Proof of Vector Subspace and Correction of False Propositions**:
  1. Show closure under vector addition and scalar multiplication.
  2. Verify that other vector space properties are satisfied.

- **Rank and Invertibility**:
  1. Understand the relationship between rank and invertibility for matrices.
  2. Use the concept of invertibility to identify traits of the system.