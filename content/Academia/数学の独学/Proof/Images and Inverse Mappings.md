# Images and Inverse Mappings

The concepts of images, inverse mappings, and composite mappings play a vital role in the study of mathematical functions and their applications. This note explores these topics in depth, providing a foundational understanding essential for advanced mathematical studies and applications.

## **Images of a Mapping**

The image of a mapping refers to the set of all outputs (values in the codomain) that correspond to elements of the domain under a given function. Formally, for a function $f: A \rightarrow B$, the image of a subset $S \subseteq A$ under $f$ is the set $\{f(s) | s \in S\}$ and is often denoted by $f(S)$.

- **Example:** Consider $f(x) = x^2$ mapping from $\mathbb{R}$ to $\mathbb{R}$. The image of the set $\{-2, -1, 0, 1, 2\}$ under $f$ is $\{0, 1, 4\}$.

## **Inverse Mappings**

An inverse mapping reverses the direction of a bijective (one-to-one and onto) function. For a bijective function $f: A \rightarrow B$, its inverse $f^{-1}: B \rightarrow A$ satisfies $f^{-1}(f(a)) = a$ for every $a \in A$ and $f(f^{-1}(b)) = b$ for every $b \in B$.

- **Existence:** Not all functions have inverses. A function must be bijective to have an inverse.
- **Example:** If $f(x) = 3x + 2$, then its inverse $f^{-1}(x) = \frac{x - 2}{3}$, since it uniquely maps back to the original domain.

## **Composite Mappings**

Composite mappings involve the combination of two functions, where the output of the first function becomes the input to the second. For functions $f: A \rightarrow B$ and $g: B \rightarrow C$, the composite function $g \circ f$ is defined as $(g \circ f)(a) = g(f(a))$ for all $a \in A$.

- **Associativity:** Composite mappings are associative, meaning if $f: A \rightarrow B$, $g: B \rightarrow C$, and $h: C \rightarrow D$, then $h \circ (g \circ f) = (h \circ g) \circ f$.
- **Example:** Given $f(x) = 2x$ and $g(x) = x + 3$, the composite $g \circ f$ is $g(f(x)) = 2x + 3$.

## **Applications**

- **Images** are used in analysis to study the range of functions and in topology to understand continuity.
- **Inverse Mappings** are fundamental in solving equations, understanding functions geometrically as reflections across the line $y = x$, and in cryptography for encoding and decoding messages.
- **Composite Mappings** are crucial in functional analysis, computer science for algorithm design, and in the composition of transformations in geometry.

## **Test Questions**

1. Describe the concept of an image of a mapping and provide an example with a function $f: \mathbb{Z} \rightarrow \mathbb{Z}$.
2. Explain how to determine if a function has an inverse and give an example of a function with its inverse.
3. Define composite mappings and illustrate with two functions $f: \mathbb{R} \rightarrow \mathbb{R}$ and $g: \mathbb{R} \rightarrow \mathbb{R}$, including their composition.

The exploration of **[[Images and Inverse Mappings]]** sheds light on the intricate relationships between sets and functions, enhancing the understanding of mathematical operations and their implications across various domains.