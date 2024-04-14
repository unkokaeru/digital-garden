# Eigenspaces

## Definition
Given a linear transformation $T:V\rightarrow V$ on a vector space $V$ and a scalar $\lambda$, the **eigenspace** corresponding to the eigenvalue $\lambda$, denoted by $E_{\lambda}$, is the set of all vectors in $V$ that get mapped to a scalar multiple of themselves under $T$. Formally, 

$$E_{\lambda}=\{ v\in V\,|\, T(v)=\lambda v\}.$$

## Properties
1. Eigenspaces are subspaces of $V$.
2. The eigenspace associated with an eigenvalue is never empty, as at the very least, the zero vector will always belong to it.

## Examples
Consider a $2\times 2$ matrix $A$ and its eigenvector equation $A\mathbf{v}=\lambda\mathbf{v}$. If we find that the eigenvalues are $\lambda_1= 2$ and $\lambda_2= 3$, the corresponding eigenspaces can be calculated as follows:
- For $\lambda_1= 2$, we solve $(A-2I)\mathbf{v}=\mathbf{0}$ to find the eigenspace $E_2$.
- For $\lambda_2= 3$, we solve $(A-3I)\mathbf{v}=\mathbf{0}$ to find the eigenspace $E_3$.

## Historical Context
The concept of eigenspaces is closely tied to the development of linear algebra, particularly in the study of matrices and transformations. It was first introduced in the 19th century by mathematicians such as Arthur Cayley and Camille Jordan as part of their work on matrices and linear transformations.

## Real-life Example
In physics, eigenspaces are used to understand the behavior and stability of physical systems. For instance, in quantum mechanics, eigenvectors and eigenvalues are used to represent the possible states and energies of a quantum system. The eigenspaces associated with these eigenvalues help determine the probabilities of observing a particle in a specific state.

## Exam Questions
1. Let $A=\begin{pmatrix} 3& 1\\ 1& 3\end{pmatrix}$. Find the eigenspace corresponding to the eigenvalue $\lambda= 4$.
2. Define eigenspaces and explain their significance in the context of linear transformations.
3. In a given linear transformation, if an eigenspace consists of only the zero vector, what can be said about the matrix or transformation?