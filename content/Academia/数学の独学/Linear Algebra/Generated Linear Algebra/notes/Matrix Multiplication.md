# Matrix Multiplication

Matrix multiplication is an essential operation in linear algebra that combines two matrices to produce a new matrix. It is important for various applications in mathematics, physics, computer science, and many other fields.

## Definition

Given two matrices **A** and **B**, where the number of columns in matrix **A** is equal to the number of rows in matrix **B**, the matrix product **C** is calculated by multiplying the elements of each row of matrix **A** by the corresponding elements of each column of matrix **B** and summing these products.

If **A** is an m x n matrix and **B** is an n x p matrix, their product **C** is an m x p matrix defined as:

$$ C= AB$$
where the element in the ith row and jth column of **C** is the sum of the products of the elements in the ith row of **A** and the jth column of **B**.

## Example

Consider the following matrices:

$$ A=\begin{bmatrix} 1& 2\\ 3& 4\end{bmatrix}$$
$$ B=\begin{bmatrix} 5& 6\\ 7& 8\end{bmatrix}$$

To find the matrix product **C** = **AB**, we multiply the corresponding elements and sum them up:

$$ C=\begin{bmatrix} 1*5+ 2*7& 1*6+ 2*8\\ 3*5+ 4*7& 3* 6+ 4*8\end{bmatrix}$$
$$ C=\begin{bmatrix} 19& 22\\ 43& 50\end{bmatrix}$$

## Properties

1. **Matrix multiplication is not commutative**: In general, **AB** is not equal to **BA**. The order of multiplication matters.
2. **Associative property**: For matrices **A**, **B**, and **C** of appropriate sizes, (**AB**) **C** = **A** (**BC**).
3. **Distributive property**: **A** (**B** + **C**) = **AB** + **AC**.

## Historical Context

Matrix multiplication has its roots in the mid-19th century with the development of matrix theory and notation by mathematicians like Arthur Cayley and James Joseph Sylvester. It gained importance in the early 20th century with the emergence of quantum mechanics and other fields that required efficient mathematical tools for computation.

## Real-life Application

Matrix multiplication is used in various real-life scenarios such as computer graphics, where transformations of 2D and 3D objects are represented by matrices. It is also essential in solving systems of linear equations in physics and engineering.

## Exam Questions

1. Calculate the product of the following matrices:
$$ A=\begin{bmatrix} 2& 3\\ 4& 5\end{bmatrix}$$
$$ B=\begin{bmatrix} 1\\ 2\end{bmatrix}$$

2. Show that matrix multiplication is not commutative with a counterexample.

3. Prove the associative property of matrix multiplication for three matrices **A**, **B**, and **C**.

Remember to show all your work in detail.