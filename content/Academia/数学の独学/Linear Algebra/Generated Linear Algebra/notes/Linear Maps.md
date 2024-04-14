# Linear Maps

Linear maps, also known as linear transformations or linear functions, are fundamental objects in linear algebra that preserve vector addition and scalar multiplication. Formally, a function $ T: V\to W$ between two vector spaces over the same field is called a **linear map** if it satisfies the following properties:

1. **Additivity**: For all vectors $\mathbf{v},\mathbf{w}$ in $V$, $T(\mathbf{v}+\mathbf{w})= T(\mathbf{v})+ T(\mathbf{w})$.
2. **Homogeneity**: For any scalar $a$ and vector $\mathbf{v}$ in $V$, $T(a\mathbf{v})= aT(\mathbf{v})$.

A linear map can be represented by a matrix if bases for the vector spaces are chosen. Let $V$ and $W$ be finite-dimensional vector spaces with bases $\{\mathbf{v}_1,\ldots,\mathbf{v}_n\}$ and $\{\mathbf{w}_1,\ldots,\mathbf{w}_m\}$, respectively. If $T: V\to W$ is a linear map, then there exists a unique matrix $A$ such that for all $\mathbf{v}\in V$, the action of $T$ on $\mathbf{v}$ is given by matrix-vector multiplication: $T(\mathbf{v})= A\mathbf{v}$.

Linear maps arise in various areas of mathematics and its applications in physics, engineering, and computer science. For example, in physics, the laws of conservation of energy and momentum are often described by linear equations and transformations. In computer graphics, linear transformations are used to manipulate images and graphics efficiently.

### Examples

1. **Rotation in $\mathbb{R}^2$**: The rotation of a vector in the plane by an angle $\theta$ counterclockwise is a linear map.
2. **Projection onto a Subspace**: The projection of a vector onto a subspace is a linear transformation.
3. **Dilation**: Scaling a vector by a factor of $c$ is a linear transformation.

### Historical Context

The concept of linear maps dates back to the 18th and 19th centuries when mathematicians like Leonhard Euler, Joseph-Louis Lagrange, and Carl Friedrich Gauss made significant contributions to linear algebra and its applications. The formal definition of linear maps and their properties were established in the 19th century and have since become fundamental in various mathematical disciplines.

### Exam Questions

1. Define a linear map between vector spaces and explain the properties that characterize a linear map.
2. Consider the linear map $T:\mathbb{R}^3\to\mathbb{R}^2$ given by $T(\begin{bmatrix} x\\ y\\ z\end{bmatrix})=\begin{bmatrix} 2x+ y\\ 3z\end{bmatrix}$. Find the standard matrix representation of $T$.
3. Show that the composition of two linear maps is also a linear map.