# Dot Product, Angle, Length

The **dot product**, also known as the scalar product, is a crucial operation in the study of vectors in multidimensional spaces. It serves as a foundational concept in linear algebra, physics, and engineering, providing a way to calculate the angle between vectors and determine their length. This note will guide you through the essentials of understanding the dot product, how to use it to calculate angles between vectors, and how to determine the length of vectors in multidimensional spaces.

## Dot Product Definition

The dot product of two vectors $\vec{a}$ and $\vec{b}$ is defined as:

$$\vec{a} \cdot \vec{b} = \|\vec{a}\| \|\vec{b}\| \cos(\theta)$$

where $\|\vec{a}\|$ and $\|\vec{b}\|$ are the magnitudes (lengths) of vectors $\vec{a}$ and $\vec{b}$, respectively, and $\theta$ is the angle between them. In a more algebraic form, for vectors $\vec{a} = (a_1, a_2, ..., a_n)$ and $\vec{b} = (b_1, b_2, ..., b_n)$ in an $n$-dimensional space, the dot product can also be calculated as:

$$\vec{a} \cdot \vec{b} = a_1b_1 + a_2b_2 + ... + a_nb_n$$

## Calculating Angles Between Vectors

The angle $\theta$ between two vectors can be found using the dot product formula. Rearranging the formula gives us:

$$\cos(\theta) = \frac{\vec{a} \cdot \vec{b}}{\|\vec{a}\| \|\vec{b}\|}$$

To find $\theta$, we calculate the dot product of $\vec{a}$ and $\vec{b}$, divide by the product of their magnitudes, and then use the inverse cosine function:

$$\theta = \cos^{-1}\left(\frac{\vec{a} \cdot \vec{b}}{\|\vec{a}\| \|\vec{b}\|}\right)$$

## Determining Vector Length

The length or magnitude of a vector $\vec{a}$ in $n$-dimensional space is given by the square root of the dot product of the vector with itself:

$$\|\vec{a}\| = \sqrt{\vec{a} \cdot \vec{a}} = \sqrt{a_1^2 + a_2^2 + ... + a_n^2}$$

This formula shows that the magnitude of a vector is the square root of the sum of the squares of its components.

## Applications

Understanding the dot product and its relation to vector angles and lengths is essential in various fields, including:

- **Physics**: Calculating work done by a force.
- **Computer Graphics**: Determining light intensity in rendering.
- **Machine Learning**: Measuring similarity between feature vectors.

## Test Questions

1. **[Basic]** Question: What is the dot product of vectors $\vec{a} = (1, 2, 3)$ and $\vec{b} = (4, -5, 6)$? Back: $\vec{a} \cdot \vec{b} = 1\cdot4 + 2\cdot(-5) + 3\cdot6 = 4 - 10 + 18 = 12$.
2. **[Basic]** Question: How do you calculate the angle between two vectors using the dot product? Back: The angle $\theta$ between two vectors can be calculated using the formula $\theta = \cos^{-1}\left(\frac{\vec{a} \cdot \vec{b}}{\|\vec{a}\| \|\vec{b}\|}\right)$.
3. **[Basic]** Question: Given vectors $\vec{a} = (3, 4)$ and $\vec{b} = (4, 3)$, calculate the angle between them. Back: First, find the dot product: $\vec{a} \cdot \vec{b} = 3\cdot4 + 4\cdot3 = 24$. Then, calculate the magnitudes: $\|\vec{a}\| = 5$, $\|\vec{b}\| = 5$. The angle is $\theta = \cos^{-1}\left(\frac{24}{25}\right)$.

This exploration of the dot product, its relationship with angles between vectors, and the determination of vector length provides a foundational understanding critical for applications across multiple disciplines.