# Angle between Vectors

In mathematics, the angle between two vectors is a fundamental concept used in various applications including physics, engineering, and computer science. The angle between two vectors can provide important information about the relationship between them.

## Definition

Given two vectors **v** and **w** in a vector space, the angle θ between them is defined as:

$$\theta=\arccos\left(\frac{{\text{v}\cdot\text{w}}}{{\|\text{v}\|\|\text{w}\|}}\right)$$

where:
- $\cdot$ denotes the dot product of vectors,
- $\|\text{v}\|$ denotes the magnitude (length) of vector **v**,
- $\|\text{w}\|$ denotes the magnitude (length) of vector **w**,
- and $\arccos$ is the inverse cosine function.

## Explanation

The dot product of two vectors **v** and **w** is given by:

$$\text{v}\cdot\text{w}=\|\text{v}\|\|\text{w}\|\cos(\theta)$$

Where $\theta$ is the angle between the two vectors. Therefore, by rearranging this formula, we can solve for $\theta$ as shown in the definition.

The angle between vectors ranges from 0 to $\pi$ (180 degrees) inclusive. When the vectors are orthogonal (perpendicular), the angle is 90 degrees. In contrast, when the vectors are parallel, the angle is 0 degrees.

## Example

Let's consider two vectors **v** = $$2, 4,-1$$ and **w** = $$1,-2, 3$$. To find the angle between them, we first calculate the dot product:

$$\text{v}\cdot\text{w}=(2)(1)+(4)(-2)+(-1)(3)= 2- 8- 3=-9$$

Next, we find the magnitudes of each vector:

$$\|\text{v}\|=\sqrt{2^2+ 4^2+(-1)^2}=\sqrt{4+ 16+ 1}=\sqrt{21}$$

$$\|\text{w}\|=\sqrt{1^2+(-2)^2+ 3^2}=\sqrt{1+ 4+ 9}=\sqrt{14}$$

Now, we substitute these values into the formula for the angle between vectors:

$$\theta=\arccos\left(\frac{-9}{\sqrt{21}\cdot\sqrt{14}}\right)\approx 119.16^\circ$$

Therefore, the angle between vectors **v** and **w** is approximately 119.16 degrees.

## Historical Context

The concept of the angle between vectors dates back to the early development of vector algebra in the 19th century. Mathematicians such as William Rowan Hamilton and Hermann Grassmann made significant contributions to the understanding of vectors and their geometric properties, including the concept of the angle between vectors.

## Real-life Application

In physics, the angle between vectors is used to determine the direction of forces acting on an object. For example, in structural engineering, understanding the angle between forces acting on a beam is crucial for ensuring the stability of the structure.

## Exam Questions

1. Calculate the angle between the vectors **a** = $$3,-1$$ and **b** = $$4, 2$$.
2. Explain the significance of the angle between vectors in the context of computer graphics.
3. Given two vectors **u** = $$1, 2, 3$$ and **v** = $$2,-1, 0$$, calculate the angle between them.

Remember to show all your workings in the exam.