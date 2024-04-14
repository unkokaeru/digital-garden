# Vector Representation

## Introduction
In mathematics, vectors are objects that have both magnitude and direction. They are widely used in various areas of mathematics and physics to represent physical quantities such as force, velocity, and displacement. One common way to represent vectors is using coordinates in a vector space.

## Vector Space
A vector space is a mathematical structure that satisfies certain properties and allows for the addition and scalar multiplication of vectors. Formally, a vector space is a set $V$ along with two operations: vector addition, denoted by $+$, and scalar multiplication, denoted by $\cdot$. These operations must satisfy the following properties:
1. **Closure under addition**: For any vectors $\mathbf{v},\mathbf{w}\in V$, their sum $\mathbf{v}+\mathbf{w}$ is also in $V$.
2. **Associativity of addition**: $(\mathbf{v}+\mathbf{w})+\mathbf{u}=\mathbf{v}+(\mathbf{w}+\mathbf{u})$ for all $\mathbf{v},\mathbf{w},\mathbf{u}\in V$.
3. **Existence of additive identity**: There exists a vector $\mathbf{0}\in V$ such that for any vector $\mathbf{v}\in V$, $\mathbf{v}+\mathbf{0}=\mathbf{v}$.
4. **Existence of additive inverse**: For every vector $\mathbf{v}\in V$, there exists a vector $-\mathbf{v}\in V$ such that $\mathbf{v}+(-\mathbf{v})=\mathbf{0}$.
5. **Closure under scalar multiplication**: For any scalar $a$ and vector $\mathbf{v}\in V$, the product $a\mathbf{v}$ is also in $V$.
6. **Distributivity of scalar with respect to vector addition**: $a(\mathbf{v}+\mathbf{w})= a\mathbf{v}+ a\mathbf{w}$ for all scalars $a$ and vectors $\mathbf{v},\mathbf{w}\in V$.
7. **Distributivity of scalar with respect to field addition**: $(a+ b)\mathbf{v}= a\mathbf{v}+ b\mathbf{v}$ for all scalars $a, b$ and vector $\mathbf{v}\in V$.
8. **Compatibility of scalar multiplication with field multiplication**: $a(b\mathbf{v})=(ab)\mathbf{v}$ for all scalars $a, b$ and vector $\mathbf{v}\in V$.
9. **Identity element of scalar multiplication**: $1\mathbf{v}=\mathbf{v}$ for all vectors $\mathbf{v}\in V$, where $1$ is the multiplicative identity of the field.

## Vector Representation in $\mathbb{R}^n$
One of the most common ways to represent vectors is in $n$-dimensional Euclidean space $\mathbb{R}^n$. A vector in $\mathbb{R}^n$ can be represented as an ordered collection of $n$ real numbers, known as coordinates. For example, a vector in $\mathbb{R}^2$ can be represented as $\begin{bmatrix} x\\ y\end{bmatrix}$, where $x$ and $y$ are the coordinates of the vector in the $x$ and $y$ directions, respectively.

### Example
Consider the vector $\mathbf{v}=\begin{bmatrix} 3\\-2\end{bmatrix}$ in $\mathbb{R}^2$. This vector can be visualized as an arrow starting at the origin $(0,0)$ and ending at the point $(3,-2)$ in the plane.

## Historical Context
The concept of vectors dates back to the 19th century when mathematicians like Hermann Grassmann and Josiah Willard Gibbs developed the formalism of vector spaces and vector algebra. Vectors have since become a fundamental element of mathematical and physical theories, playing a key role in fields such as physics, engineering, computer graphics, and more.

## Real-life Applications
Vectors are used in various real-life applications, such as:
- **Navigation**: Vectors are used in GPS systems to represent positions and directions.
- **Engineering**: Vectors are used to represent forces, velocities, and displacements in structural analysis and design.
- **Computer Graphics**: Vectors are used to represent positions, colors, and orientations of objects in computer graphics.
- **Machine Learning**: Vectors are used to represent features of data points in machine learning algorithms.

## Exam Questions
1. Define a vector space and explain the eight axioms that define its structure.
2. Represent the vector $\mathbf{w}=\begin{bmatrix} 1\\-1\\ 2\end{bmatrix}$ in $\mathbb{R}^3$. Draw a geometric representation of this vector.
3. Discuss the historical development of vector theory and the contributions of Hermann Grassmann and Josiah Willard Gibbs to the field of vectors.