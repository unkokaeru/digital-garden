### EIGENVALUES AND EIGENVECTORS OF A MATRIX

**Key Concepts:**
- **Eigenvalues** ($\lambda$) are scalars such that when multiplied by a vector ($v$), it is equivalent to the linear transformation of $v$ by matrix $A$, i.e., $Av = \lambda v$.
- **Eigenvectors** ($v$) are non-zero vectors that change by only a scalar factor when that linear transformation is applied.
- **Characteristic Equation:** $det(A - \lambda I) = 0$, where $I$ is the identity matrix of the same dimension as $A$. Solving this gives the eigenvalues.
- For each eigenvalue, find the eigenvector(s) by solving $(A - \lambda I)v = 0$.

**Diagonalisation:**
- A matrix $A$ is diagonalisable if there exists a diagonal matrix $D$ and an invertible matrix $P$ such that $A = PDP^{-1}$.
- Conditions: 
  - $A$ must have $n$ linearly independent eigenvectors.
  - If $A$ is $n \times n$, there must be $n$ eigenvalues (counting multiplicities).

### SOLVING LINEAR SYSTEMS (HOMOGENEOUS)

**Key Concepts:**
- A system is **homogeneous** if it can be written as $Ax = 0$.
- **Null Space (Null(A)):** The set of all vectors $x$ that satisfy $Ax = 0$. It's a vector subspace.
- **Basis of Null Space:** The set of linearly independent vectors that span the Null Space.

**Gauss-Jordan Elimination:**
- A method to solve linear systems, find the rank, and determine the inverse of a matrix.
- Perform row operations to transform the matrix into reduced row echelon form (RREF).
- For $Ax = 0$, RREF reveals the free variables, which help express the solution set.

### INVERSE OF A MATRIX

**Key Concepts:**
- The **inverse** of an $n \times n$ matrix $A$ is a matrix $A^{-1}$ such that $AA^{-1} = A^{-1}A = I$.
- A matrix is **invertible** (non-singular) if it has an inverse, which occurs iff |A| (determinant of $A$) $\neq 0$.

**Finding the Inverse:**
- **Method 1: Gauss-Jordan Elimination** - Augment $A$ with $I$ and perform row operations until $A$ becomes $I$, and $I$ becomes $A^{-1}$.
- **Method 2: Adjugate Formula** - $A^{-1} = \frac{1}{det(A)} \cdot adj(A)$ where $adj(A)$ is the adjugate (transpose of the cofactor matrix) of $A$.

### BASIS OF A VECTOR SPACE & BASIS PROOF

**Key Concepts:**
- A **basis** of a vector space is a set of vectors in the space that is linearly independent and spans the vector space.
- **Spanning Set:** A set of vectors that can combine to form any vector in the space.
- **Linearly Independent:** No vector in the set can be written as a combination of the others.

**Proving a Basis:**
- To prove that $n$ vectors form a basis of $\mathbb{R}^n$, show that:
  - They are linearly independent.
  - They span $\mathbb{R}^n$, typically by showing the only solution to their homogeneous system is the trivial solution, indicating independence, and counting the vectors matches the dimension of the space for spanning.