# Vectors in Two Dimensions

## Introduction

In the field of mathematics, particularly in linear algebra and physics, a **vector** is a fundamental concept. Vectors in two dimensions are especially important as they lay the foundation for understanding more complex multidimensional vectors. This note explores the properties and operations of two-dimensional vectors.

## Properties of Vectors

A two-dimensional vector can be represented as an ordered pair (x, y), where 'x' and 'y' are components along the horizontal and vertical axes, respectively.

### Key Properties:

1. **Direction**: The direction of a vector is the angle it makes with the positive x-axis. 
2. **Magnitude**: The length of the vector, calculated using the Pythagorean theorem: $\sqrt{x^2 + y^2}$.
3. **Zero Vector**: A special vector (0,0) with zero magnitude.
4. **Commutativity**: The order of vector *addition* makes no difference, $\vec{u}+\vec{w}=\vec{w}+\vec{u}$.
5. **Associativity**: Brackets make no difference on the order of vector *addition*, $(\vec{u}+\vec{v})+\vec{w}=\vec{u}+(\vec{v}+\vec{w})$.
6. This continues for other key properties that make vector addition a group in [[Group Theory]], such as distributivity, closure, identities, inverses, etc.

#### Additional Property (Span)

The set of all linear combinations is called the span of $\mathbf{u}_{1}$ and $\mathbf{u}_{2}$, denoted by $\text{span}(\mathbf{u}_{1},\mathbf{u}_{2})$.

$$
\mathbb{S}=\{c_{1}\mathbf{u}_{1}+c_{2}\mathbf{u}_{2}:c_{1},c_{2}\in \mathbb{R}\}
$$

If the linear combination of the two vectors can product any vector in the plane, then the vectors span the plane, denoted by...

$$
\text{span}(\mathbf{u}_{1},\mathbf{u}_{2})=\mathbb{R}^{2}
$$

Some questions can ask you to prove whether or not two vectors span a plane. For example, our basic vectors $\mathbf{e}_{1}$ and $\mathbf{e}_{2}$ span the 2d plane, by definition.

Another example could be...

$$
\begin{align*}
\mathbb{S}&=\text{span}(\mathbf{e}_{1},-2\mathbf{e}_{1})\\
&= \{c_{1}(\mathbf{e}_{1})+c_{2}(-2\mathbf{e}_{1}):c_{1},c_{2}\in \mathbb{R}\}\\
&= \{(c_{1}-2c_{2})\mathbf{e}_{1}:c_{1},c_{2}\in \mathbb{R}\}\\
&= \{d \mathbf{e}_{1}:d \in \mathbb{R}\}
\end{align*}
$$

Which thus show that it spans the $x$-axis, but not the 2d plane.

### Standard Vectors:

1. $\vec{e}_{1}=\begin{bmatrix}1 \\ 0\end{bmatrix}$, the standard $\hat{i}$ component.
2. $\vec{e}_{2}=\begin{bmatrix}0 \\ 1\end{bmatrix}$, the standard $\hat{j}$ component.

These are useful, in combination with the following operations, to demonstrate simple vectors in an algebraic form, for example...

$$
\begin{align*}
\mathbf{u}&=\begin{bmatrix}3\\
4\end{bmatrix}\\
&=\begin{bmatrix}3\\
0\end{bmatrix}+\begin{bmatrix}0\\
4\end{bmatrix}\\
&= 3\begin{bmatrix}1\\
0\end{bmatrix}+4\begin{bmatrix}0\\
1\end{bmatrix}\\
&= 3\hat{i}+4\hat{j}
\end{align*}
$$

This is called a *linear combination*, and its how vectors are often expressed in physics, as well as other fields.

## Operations on Vectors

1. **Addition**: Vector addition is done component-wise. If $\mathbf{v} = (v_1, v_2)$ and $\mathbf{w} = (w_1, w_2)$, then $\mathbf{v} + \mathbf{w} = (v_1 + w_1, v_2 + w_2)$.
2. **Scalar Multiplication**: Multiplying a vector by a scalar 'k' changes its magnitude without altering its direction: $k\mathbf{v} = (kv_1, kv_2)$.
3. **Dot Product**: The dot product of $\mathbf{v}$ and $\mathbf{w}$ is given by $v_1w_1 + v_2w_2$. It is a measure of how much one vector extends in the direction of another.

Note: All of these operations can be shown graphically, too, for example the addition of vectors can be shown as a parallelogram, made predominately by the two initial vectors as its sides. Scalar multiplication on the other hand is simply extending the line (vector).

## Applications in Physics

Vectors are extensively used in physics to represent quantities that have both magnitude and direction, such as force, velocity, and acceleration.

## Historical Context

The concept of vectors dates back to the late 19th century. The term "vector" was introduced by William Rowan Hamilton as part of his quaternions work.

## Conclusion and Test Questions

Understanding vectors in two dimensions is essential for delving into higher dimensions in mathematics and physics. Their simplicity in two dimensions lays the groundwork for more complex applications.

### Test Questions

1. STARTI [Basic] Question: What is the magnitude of a vector (3, 4) in a two-dimensional plane? Back: The magnitude is $\sqrt{3^2 + 4^2} = 5$. ENDI
2. STARTI [Basic] Question: How do you compute the dot product of vectors (1, 2) and (3, 4)? Back: The dot product is $1*3 + 2*4 = 11$. ENDI
3. STARTI [Basic] Question: What happens to a vector when it is multiplied by a scalar? Back: Multiplying a vector by a scalar changes its magnitude but not its direction. ENDI

---

This note on **[[Vectors in Two Dimensions]]** provides a concise overview of the fundamental aspects of vectors in a 2D plane, a cornerstone concept in mathematics and physics.