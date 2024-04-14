# Change of Basis Matrix

## Introduction
In linear algebra, understanding the change of basis matrix is crucial when working with vector spaces. When we change the basis of a vector space, we can represent the same vector in terms of different basis vectors. The change of basis matrix allows us to convert coordinates relative to one basis into coordinates relative to another basis. By knowing how to calculate and work with the change of basis matrix, mathematicians can transform vectors and linear transformations between different bases efficiently.

## Definitions
1. **Basis:** A basis of a vector space is a set of vectors that are linearly independent and span the space.
   
2. **Change of Basis Matrix:** Suppose we have two bases $B=\{v_1, v_2,..., v_n\}$ and $C=\{w_1, w_2,..., w_n\}$ for an $n$-dimensional vector space. The change of basis matrix from basis $B$ to basis $C$, denoted as $P_{B\rightarrow C}$, is a matrix that enables us to convert coordinates of vectors from basis $B$ to basis $C$.

## Calculating the Change of Basis Matrix
Let's say we have a vector $v$ represented with respect to basis $B$ as $(v)_B=[v]_B=\begin{bmatrix} a_1\\ a_2\\\vdots\\ a_n\end{bmatrix}$. To find the coordinates of the same vector with respect to basis $C$, we use the change of basis matrix:

$$(v)_C= P_{B\rightarrow C}\cdot(v)_B$$

To calculate $P_{B\rightarrow C}$, we place the basis vectors of $C$ as columns in the matrix, each expressed in terms of basis $B$. For example, if $w_1= c_{11}v_1+ c_{21}v_2+\ldots+ c_{n_{1}}v_n$, then the first column of $P_{B\rightarrow C}$ will be $[w_1]_B=\begin{bmatrix} c_{11}\\ c_{21}\\\vdots\\ c_{n_{1}}\end{bmatrix}$.

## Real-Life Example
Consider a spaceship navigating in 3-dimensional space. The spaceship has its navigation system with a basis $B=\{v_1, v_2, v_3\}$. When a neighboring space station communicates with the spaceship using its basis $C=\{w_1, w_2, w_3\}$, the change of basis matrix provides the transformation needed to interpret the spaceship's coordinates correctly.

## Historical Perspective
The concept of change of basis matrix has applications in various fields, including quantum mechanics, computer graphics, and control systems. It plays a fundamental role in transforming vectors and operators across different coordinate systems, making calculations more manageable and allowing for efficient computations.

## Exam Questions
1. Explain what a change of basis matrix is and why it is important in linear algebra.
2. Given two bases $B=\{v_1, v_2\}$ and $C=\{w_1, w_2\}$, calculate the change of basis matrix from $B$ to $C$ if $[v_1]_C=\begin{bmatrix} 1\\ 2\end{bmatrix}$ and $[v_2]_C=\begin{bmatrix}-1\\ 3\end{bmatrix}$.
3. In the context of control systems, explain how the change of basis matrix can be utilized to analyze and transform state variables.

Remember, understanding how to calculate and apply the change of basis matrix is essential for dealing with vector transformations in various contexts.