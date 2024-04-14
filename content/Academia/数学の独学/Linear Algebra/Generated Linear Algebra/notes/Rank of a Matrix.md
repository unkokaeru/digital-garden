# Rank of a Matrix

In the field of linear algebra, the **rank of a matrix** is a fundamental concept that helps us understand the properties and behavior of matrices. The rank of a matrix is defined as the maximum number of linearly independent rows or columns in the matrix. It gives us crucial information about the size of the largest non-zero minor in the matrix.

## Definitions
1. **Linearly Independent Vectors**: Vectors are said to be linearly independent if no vector in the set can be represented as a linear combination of the others. In simpler terms, if you have a set of vectors and one of them can be expressed as a sum of the others multiplied by constants, then they are linearly dependent.
2. **Non-zero Minor**: A minor of a matrix is a determinant of a square submatrix obtained by deleting some rows and columns. A non-zero minor is a minor whose determinant is not zero.

## Rank Theorem
For any matrix A, the rank of A is equal to the rank of its transpose. 

## Example
Consider the matrix:
$$ A=\left[\begin{array}{ccc} 1& 2& 3\\ 2& 4& 6\\ 3& 6& 9\end{array}\right]$$

To find the rank of matrix A, we perform row operations to reduce it to row-echelon form:
$$\left[\begin{array}{ccc} 1& 2& 3\\ 0& 0& 0\\ 0& 0& 0\end{array}\right]$$

Here, we see that there is only one linearly independent row. Thus, the rank of matrix A is 1.

## Historical Context
The concept of rank was first introduced by the German mathematician David Hilbert in the late 19th century. It played a crucial role in the development of linear algebra and its applications in various fields such as physics, engineering, and computer science.

## Real-life Example
In a system of linear equations, the rank of the coefficient matrix can tell us whether the system has a unique solution, infinitely many solutions, or no solution at all. This information is essential in various real-life scenarios, such as in image processing, control systems, and optimization problems.

## Exam Questions
1. Calculate the rank of the matrix $$ B=\left[\begin{array}{ccc} 2& 4& 6\\ 1& 2& 3\\ 3& 6& 9\end{array}\right]$$
2. Discuss the significance of the rank of a matrix in the context of solving a system of linear equations.
3. Prove that the rank of a matrix is equal to the number of linearly independent columns in the matrix.