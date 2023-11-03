# Newton's Laws

Newton's Laws of Motion are a fundamental part of classical mechanics and provide the basis for understanding the motion of objects. These laws describe the relationship between the forces acting on an object and its motion due to those forces.

## Newton's First Law: Law of Inertia

Newton's First Law states that an object will remain at rest or in uniform motion in a straight line unless acted upon by an external force. This property of matter is known as inertia. 

In mathematical terms, if the sum of all forces $\vec{F}$ acting on an object is zero, then the velocity $\vec{v}$ of the object is constant:

$$
\sum \vec{F} = 0 \Rightarrow \frac{d\vec{v}}{dt} = 0
$$

## Newton's Second Law: Law of Acceleration

The Second Law quantifies how the velocity of an object changes when it is subjected to an external force. The law states that the force $\vec{F}$ acting on an object is equal to the mass $m$ of the object multiplied by the acceleration $\vec{a}$ of the object:

$$
\vec{F} = m\vec{a}
$$

This can also be written as:

$$
\vec{F} = m\frac{d\vec{v}}{dt}
$$

If multiple forces are acting on the object, the second law is often written as:

$$
\sum \vec{F} = m\vec{a}
$$

## Newton's Third Law: Law of Interaction

For every action, there is an equal and opposite reaction. This means that for every force there is a reaction force that is equal in size, but opposite in direction. This is described mathematically as:

$$
\vec{F}_{1\to2} = -\vec{F}_{2\to1}
$$

Where $\vec{F}_{1\to2}$ is the force applied by object 1 on object 2, and $\vec{F}_{2\to1}$ is the force applied by object 2 on object 1.

# Orthonormal Frames

Orthonormal frames are a set of vectors in a vector space that are mutually orthogonal (perpendicular to each other) and all of unit length. They form a basis for the vector space in which they reside, and they are especially important in transformations because they simplify calculations and provide a clear geometric interpretation.

## Definition

An orthonormal set of vectors $\{\vec{e}_1, \vec{e}_2, ..., \vec{e}_n\}$ in an $n$-dimensional space satisfies the following conditions:

- Orthogonality: $\vec{e}_i \cdot \vec{e}_j = 0$ for all $i \neq j$.
- Normality: $\|\vec{e}_i\| = 1$ for all $i$.

In LaTeX, we express the orthogonality and normality conditions as:

$$
\vec{e}_i \cdot \vec{e}_j = \delta_{ij} = 
\begin{cases} 
0 & \text{if } i \neq j \\
1 & \text{if } i = j 
\end{cases}
$$

Where $\delta_{ij}$ is the Kronecker delta function.

## Performing Transformations

To perform a transformation using an orthonormal frame, we typically want to express a vector $\vec{v}$ in the basis of the orthonormal frame. If $\{\vec{e}_1, \vec{e}_2, ..., \vec{e}_n\}$ is an orthonormal basis for our space, then any vector $\vec{v}$ can be expressed as a linear combination of these basis vectors:

$$
\vec{v} = v^1\vec{e}_1 + v^2\vec{e}_2 + ... + v^n\vec{e}_n
$$

Where $v^i = \vec{v} \cdot \vec{e}_i$ are the components of $\vec{v}$ in this basis.

In transformations, such as rotations, we can use matrix multiplication with the components of $\vec{v}$ in the orthonormal frame to find the transformed vector.

Remember, the key advantage of using an orthonormal frame is that the matrix representing the transformation will be orthogonal, meaning its inverse is simply its transpose, and this greatly simplifies many computations in linear algebra and vector calculus.