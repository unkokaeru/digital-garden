# Vector Space Properties

In mathematics, a **vector space** over a field is a set of elements, called vectors, together with two operations: vector addition and scalar multiplication. These operations must satisfy a set of properties to make the set a vector space.

## Definition:

Let **V** be a non-empty set and **F** be a field. A set **V** is called a *vector space* over **F** if for any vectors **u, v, w** in **V** and any scalars **a, b** in **F**, the following properties hold:

1. **Addition Properties**:
   - Closure under addition: **u + v** is in **V**.
   - Commutativity: **u + v = v + u**.
   - Associativity: **(u + v) + w = u + (v + w)**.
   - Identity element: There exists a zero vector **0** such that **u + 0 = u** for all **u** in **V**.
   - Inverse element: For every **u** in **V**, there exists a vector **-u** such that **u + (-u) = 0**.

2. **Scalar Multiplication Properties**:
   - Closure under scalar multiplication: **a * u** is in **V**.
   - Associativity: **a * (b * u) = (a * b) * u**.
   - Identity element: The scalar 1 in **F** acts as the identity element for scalar multiplication in **V**.
   - Distributivity of scalar sums: **(a + b) * u = a * u + b * u**.
   - Distributivity of vector sums: **a * (u + v) = a * u + a * v**.

## Examples:

1. **Euclidean Space**: The set of all n-tuples of real numbers **R**^n with standard vector addition and scalar multiplication is a vector space.

2. **Polynomial Space**: The set of all polynomials with coefficients in a field **F** forms a vector space over **F** with polynomial addition and scalar multiplication defined as usual.

3. **Function Space**: The set of all real-valued functions defined on a closed interval [a, b] forms a vector space with function addition and scalar multiplication defined pointwise.

## Historical Context:

The concept of a vector space was first formulated by the mathematician Giuseppe Peano in 1888. It was further developed by David Hilbert and Hermann Weyl in the early 20th century as part of the broader study of linear algebra. Vector spaces have since become fundamental objects of study in mathematics, physics, computer science, and various other fields.

## Real-life Example:

Consider a three-dimensional space where vectors represent forces acting on an object. The properties of vector addition and scalar multiplication allow us to analyze these forces in terms of their magnitude and direction, making it easier to predict the object's motion.

## Exam Questions:

1. Prove that the set of all 2x2 matrices forms a vector space over the field of real numbers **R**.
2. Show that the set of all continuous functions defined on the interval [-1, 1] is a vector space.
3. Consider the vector space of polynomials of degree at most 3. Is this vector space closed under addition and scalar multiplication? Justify your answer.