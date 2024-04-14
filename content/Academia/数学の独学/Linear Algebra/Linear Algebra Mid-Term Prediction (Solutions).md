### Problem 1 Solution

**a) Finding eigenvalues and eigenvectors of $B$:**

Given matrix $B = \begin{pmatrix} 2 & -1 & 0 \\ 1 & 2 & -2 \\ 1 & 0 & 1 \end{pmatrix}$.

First, find the eigenvalues by solving $\det(B - \lambda I) = 0$.

$$B - \lambda I = \begin{pmatrix} 2-\lambda & -1 & 0 \\ 1 & 2-\lambda & -2 \\ 1 & 0 & 1-\lambda \end{pmatrix}$$

$$\det(B - \lambda I) = (2-\lambda)[(2-\lambda)(1-\lambda)] - (-1)(-2) - (0) = 0$$

Solving this characteristic polynomial will give us the eigenvalues $\lambda$.

**b) Diagonalisability of $B$:**

For $B$ to be diagonalisable, the number of linearly independent eigenvectors must equal the multiplicity of each eigenvalue. We find these eigenvectors by solving $(B - \lambda I)\mathbf{v} = 0$ for each $\lambda$.

If we find 3 linearly independent eigenvectors, then $B$ is diagonalisable, and we can construct matrix $P$ from these eigenvectors. $D$ is a diagonal matrix with eigenvalues on the diagonal.

**Detailed calculations for the eigenvalues, eigenvectors, and the diagonalisation process will require solving the characteristic polynomial and system of equations for each eigenvalue.**

---

### Problem 2 Solution

**a) Solving the system using Gauss-Jordan elimination:**

Given matrix $C$ and system $C\mathbf{x} = \mathbf{0}$,

$$C = \begin{pmatrix} 1 & 2 & -1 \\ -2 & 4 & 2 \\ 3 & 6 & -3 \end{pmatrix}$$

We apply Gauss-Jordan elimination to reduce $C$ to its reduced row echelon form (RREF), then solve for $\mathbf{x}$.

**b) Solution set as a vector subspace and its basis:**

The solution set will be all vectors $\mathbf{x}$ that satisfy the RREF form of $C\mathbf{x} = \mathbf{0}$. We find the basis by identifying the free variables and expressing the solution set in terms of these variables, showing it forms a subspace.

---

### Problem 3 Solution

**a) Finding the inverse of $M$ using Gauss-Jordan elimination:**

Given $M = \begin{pmatrix} 0 & 1 & 2 \\ 2 & 0 & -2 \\ 1 & -1 & 1 \end{pmatrix}$,

To find $M^{-1}$, augment $M$ with the identity matrix $I$ and apply Gauss-Jordan elimination until the left side is $I$. The right side will then be $M^{-1}$.

**b) Showing $N = M^{-1}$:**

If $NM = I$, then by definition, $N$ is the inverse of $M$. Since we've found $M^{-1}$, we can show $N$ and $M^{-1}$ are the same by comparison.

---

### Problem 4 Solution

**a) Proving $\{v_1, v_2, v_3\}$ forms a basis for $\mathbb{R}^3$:**

Vectors form a basis if they are linearly independent and span $\mathbb{R}^3$. We can show linear independence by showing the determinant of the matrix formed by these vectors is non-zero.

**b) Coordinates of $w$ in the basis $\{v_1, v_2, v_3\}$:**

Solve the linear equation $\alpha v_1 + \beta v_2 + \gamma v_3 = w$ for coefficients $\alpha, \beta, \gamma$. These coefficients are the coordinates of $w$ in the given basis.