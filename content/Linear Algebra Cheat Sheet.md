# Linear Algebra Cheat Sheet

## Vector Operations

- **Vector addition**: $\mathbf{v} + \mathbf{w} = (v_1 + w_1, v_2 + w_2, \ldots)$
- **Scalar multiplication**: $c\mathbf{v} = (cv_1, cv_2, \ldots)$
- **Dot product**: $\mathbf{v} \cdot \mathbf{w} = v_1w_1 + v_2w_2 + \ldots$
- **Length of a vector**: $\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}}$
- **Angle between vectors**: $\cos \theta = \frac{\mathbf{v} \cdot \mathbf{w}}{\|\mathbf{v}\|\|\mathbf{w}\|}$

## Matrix Operations

- **Addition**: $(A + B)_{ij} = A_{ij} + B_{ij}$
- **Multiplication**: $(AB)_{ij} = \sum_k A_{ik}B_{kj}$
- **Transpose**: $(A^T)_{ij} = A_{ji}$
- **Inverse**: $AA^{-1} = A^{-1}A = I$
- **Determinant**: $\det(A) = \sum (-1)^{i+j} a_{ij} \det(A_{ij})$ for 2x2: $\det(A) = ad - bc$

## Systems of Linear Equations

- **Row Echelon Form (REF)**: Leading entry of each nonzero row after the first occurs to the right of the leading entry of the previous row.
- **Reduced Row Echelon Form (RREF)**: The leading entry in each nonzero row is 1, and is the only nonzero entry in its column.
- **Gauss-Jordan Elimination**: Process to reduce a matrix to RREF.

## Linear Independence and Span

- **Linear Independence**: A set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ is linearly independent if no vector in the set can be written as a linear combination of the others. This is equivalent to the equation $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \ldots + c_n\mathbf{v}_n = \mathbf{0}$ having only the trivial solution ($c_1 = c_2 = \ldots = c_n = 0$).
- **Span**: The span of a set of vectors is the set of all possible linear combinations of those vectors. It represents a vector space or subspace that those vectors can generate.

## Vector Spaces

- **Subspaces**: Must contain the zero vector, be closed under addition and scalar multiplication.
- **Basis**: A linearly independent set of vectors that spans the space.
- **Dimension**: Number of vectors in a basis for the space.

## Symmetric and Triangular Matrices

- **Symmetric Matrix**: $A$ is symmetric if $A = A^T$. Eigenvectors of symmetric matrices corresponding to different eigenvalues are orthogonal.
- **Triangular Matrix**: A matrix is upper triangular if all the entries below the main diagonal are zero. Similarly, it's lower triangular if all entries above the main diagonal are zero. The determinant of a triangular matrix is the product of its diagonal entries.

## Cofactor Expansion

- **Cofactor**: The cofactor $C_{ij}$ of an element $a_{ij}$ in a matrix $A$ is given by $C_{ij} = (-1)^{i+j}\det(M_{ij})$, where $M_{ij}$ is the submatrix obtained by removing the $i$-th row and $j$-th column from $A$.
- **Determinant via Cofactor Expansion**: $\det(A) = a_{i1}C_{i1} + a_{i2}C_{i2} + \ldots + a_{in}C_{in}$ for any row $i$, or similarly for any column.

## Properties of Inverses and Determinants

- **Inverse Properties**: The inverse of a product of matrices is the product of their inverses in reverse order: $(AB)^{-1} = B^{-1}A^{-1}$. The determinant of an inverse matrix is the reciprocal of the determinant of the matrix: $\det(A^{-1}) = 1/\det(A)$.
- **Determinant Properties**: The determinant of a product of matrices equals the product of their determinants: $\det(AB) = \det(A)\det(B)$.

## Determinants and Volume

- **Geometric Interpretation**: The determinant of a matrix represents the scaling factor of the linear transformation described by the matrix and the orientation (positive for same orientation as the original space, negative for opposite).
- **Volume Interpretation**: The absolute value of the determinant of a matrix describing a transformation gives the volume of the parallelepiped spanned by the column vectors of the matrix.

## Eigenvalues and Eigenvectors

- For matrix $A$, vector $\mathbf{v}$, and scalar $\lambda$, if $A\mathbf{v} = \lambda\mathbf{v}$, then $\lambda$ is an eigenvalue and $\mathbf{v}$ is an eigenvector.
- **Characteristic polynomial**: $p(\lambda) = \det(A - \lambda I)$
- **Diagonalisation**: $A = PDP^{-1}$ where $D$ is diagonal and columns of $P$ are eigenvectors.

## Fundamental Theorem of Invertible Matrices and Rank Theorem

- **Fundamental Theorem of Invertible Matrices**: A matrix is invertible if and only if it is row equivalent to an identity matrix, its determinant is not zero, it has full rank, and there exists a matrix $B$ such that $AB=BA=I$.
- **Rank Theorem**: For any matrix $A$, the rank of $A$ plus the nullity of $A$ equals the number of columns of $A$ ($\text{rank}(A) + \text{nullity}(A) = n$). This highlights the relationship between the dimensions of the column space and the null space.

## Special Topics

- **Determinant Properties**:
  - Swap rows reverses sign.
  - Factor of $k$ out of a row multiplies det by $k$.
  - Det of identity is 1.
- **Cramer's Rule**: Solution of $Ax = b$ is $x_i = \frac{\det(A_i)}{\det(A)}$ where $A_i$ is $A$ with column $i$ replaced by $b$.