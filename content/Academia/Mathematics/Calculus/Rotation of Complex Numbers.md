# Rotation of Complex Numbers

## Introduction
In mathematics, particularly in complex analysis, rotation of complex numbers is an essential concept. Complex numbers, expressed in the form $a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit, can be represented as points or vectors in the complex plane. Rotation in this context involves turning the vector around the origin of the complex plane.

## Representing Complex Numbers
A complex number $z = a + bi$ can be represented in polar form as $z = r(\cos \theta + i\sin \theta)$, where $r$ is the magnitude of $z$ and $\theta$ is the argument (or the angle with the positive x-axis). This polar form is crucial for understanding rotations.

## Basic Rotation
To rotate a complex number $z$ by an angle $\phi$, we multiply $z$ by the complex number $e^{i\phi}$ (Euler's formula). The resulting complex number $z'$ is given by:

$$z' = z \cdot e^{i\phi}$$

This operation rotates $z$ counterclockwise by $\phi$ radians about the origin.

## Example
Consider a complex number $z = 1 + i$. Its polar form is $\sqrt{2}(\cos \frac{\pi}{4} + i\sin \frac{\pi}{4})$. To rotate this number by $\frac{\pi}{2}$ radians, we compute:

$$z' = (\sqrt{2}(\cos \frac{\pi}{4} + i\sin \frac{\pi}{4})) \cdot e^{i\frac{\pi}{2}}$$

This results in a new complex number, representing the rotated point in the complex plane.

## Applications
Rotation of complex numbers has applications in various fields, including engineering, physics, and computer graphics. In these domains, it's often used to model rotations in two-dimensional space.

## Test Questions
1. STARTI [Basic] Question: What is the result of rotating the complex number $1 + i$ by $\frac{\pi}{2}$ radians? Back: The result is $-1 + i$. ENDI
2. STARTI [Basic] Question: How do you represent a complex number in polar form? Back: A complex number $z = a + bi$ is represented in polar form as $z = r(\cos \theta + i\sin \theta)$, where $r$ is the magnitude and $\theta$ is the argument. ENDI
3. STARTI [Basic] Question: What is Euler's formula, and how is it used in the rotation of complex numbers? Back: Euler's formula is $e^{i\phi} = \cos \phi + i\sin \phi$. It is used in rotating a complex number by multiplying the number with $e^{i\phi}$. ENDI