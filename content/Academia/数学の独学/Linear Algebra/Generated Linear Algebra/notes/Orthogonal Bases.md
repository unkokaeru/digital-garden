# Orthogonal Bases

## Definition
An orthogonal basis in linear algebra refers to a set of vectors in a vector space that are mutually perpendicular to each other. More formally, let $V$ be a vector space over a field $F$. An orthogonal basis for $V$ is a basis $\{v_1, v_2,\ldots, v_n\}$ for $V$ such that $\langle v_i, v_j\rangle= 0$ for all $i\neq j$, where $\langle\cdot,\cdot\rangle$ denotes the inner product defined on $V$.

## Properties
1. Orthogonal bases provide a convenient way to express vectors in terms of linear combinations, reducing computations involving inner products.
2. If $V$ is a finite-dimensional inner product space, then any orthogonal basis for $V$ is also a linearly independent set and hence forms a basis for $V$.

## Gram-Schmidt Process
Given any basis for a vector space, one can use the Gram-Schmidt process to obtain an orthogonal basis. The process involves successively orthogonalizing each vector in the basis with respect to the previously processed vectors.

## Example
Consider the vector space $\mathbb{R}^3$ with the standard inner product. The vectors $v_1=(1, 0, 0)$, $v_2=(0, 1, 0)$, and $v_3=(1, 1, 1)$ form a basis for $\mathbb{R}^3$. To obtain an orthogonal basis using the Gram-Schmidt process:
1. Normalize $v_1$: $u_1=\frac{v_1}{\|v_1\|}=(1, 0, 0)$
2. Orthogonalize $v_2$ with respect to $u_1$: $u_2= v_2-\langle v_2, u_1\rangle u_1=(0, 1, 0)- 0=(0, 1, 0)$
3. Orthogonalize $v_3$ with respect to $u_1$ and $u_2$: $u_3= v_3-\langle v_3, u_1\rangle u_1-\langle v_3, u_2\rangle u_2=(1, 1, 1)- 1(1, 0, 0)- 1(0, 1, 0)=(0, 0, 1)$

The set $\{u_1, u_2, u_3\}$ is an orthogonal basis for $\mathbb{R}^3$.

## Historical Context
The concept of orthogonal bases plays a fundamental role in various branches of mathematics and physics, particularly in linear algebra, signal processing, quantum mechanics, and optimization. The Gram-Schmidt process, named after mathematicians Jørgen Gram and Erhard Schmidt, is a popular method for constructing orthogonal bases and was first introduced in the late 19th century.

## Real-life Application
In computer graphics, orthogonal bases are used to represent lighting information on 3D models. By decomposing the lighting effects into orthogonal components, computations involving shading and reflections can be simplified and optimized.

## Exam Questions
1. Consider the vector space $\mathbb{R}^2$ with the standard inner product. Show that the vectors $(1, 1)$ and $(-1, 1)$ form an orthogonal basis for $\mathbb{R}^2$.
2. Explain the significance of orthogonal bases in the context of signal processing.
3. Given a basis $\{v_1, v_2, v_3\}$ for a vector space, describe how you would apply the Gram-Schmidt process to obtain an orthogonal basis.