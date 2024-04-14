# Matrix Addition and Subtraction

In linear algebra, **matrix addition** and **subtraction** are fundamental operations that involve adding or subtracting corresponding elements of matrices. These operations are only defined for matrices of the same size.

## Matrix Addition

Given two $m\times n$ matrices $A=[a_{ij}]$ and $B=[b_{ij}]$, the sum $A+ B$ is defined as the matrix $C=[c_{ij}]$ where $c_{ij}= a_{ij}+ b_{ij}$ for all $1\leq i\leq m$, $1\leq j\leq n$.

### Properties of Matrix Addition
1. **Commutative Property**: $A+ B= B+ A$ for any matrices $A$ and $B$ where $A$ and $B$ are of the same size.
2. **Associative Property**: $(A+ B)+ C= A+(B+ C)$ for any matrices $A$, $B$, and $C$ of the same size.
3. **Identity Element**: The zero matrix, denoted by $0$, acts as the additive identity matrix in matrix addition. For any matrix $A$, $A+ 0= A$.

## Matrix Subtraction

Matrix subtraction is defined similarly to matrix addition. Given two $m\times n$ matrices $A=[a_{ij}]$ and $B=[b_{ij}]$, the difference $A- B$ is defined as the matrix $C=[c_{ij}]$ where $c_{ij}= a_{ij}- b_{ij}$ for all $1\leq i\leq m$, $1\leq j\leq n$.

### Properties of Matrix Subtraction
1. **Non-commutativity**: Matrix subtraction is not commutative, i.e., $A- B\neq B- A$ in general.
2. **Inverse Element**: For any matrix $A$, there exists a matrix $B$ such that $A+ B= 0$, where $0$ is the zero matrix. The matrix $B$ is called the additive inverse of $A$ and is denoted by $-A$.

## Example

Let's consider the following matrices:
$$
A=\begin{bmatrix} 1& 2\\ 3& 4\end{bmatrix}\quad\text{and}\quad B=\begin{bmatrix} 4& 3\\ 2& 1\end{bmatrix}$$

The sum $A+ B$ is:
$$
A+ B=\begin{bmatrix} 1+ 4& 2+ 3\\ 3+ 2& 4+ 1\end{bmatrix}=\begin{bmatrix} 5& 5\\ 5& 5\end{bmatrix}$$

The difference $A- B$ is:
$$
A- B=\begin{bmatrix} 1- 4& 2- 3\\ 3- 2& 4- 1\end{bmatrix}=\begin{bmatrix}-3&-1\\ 1& 3\end{bmatrix}$$

## Historical Context

Matrix operations, including addition and subtraction, were first introduced by the mathematician James Joseph Sylvester in the mid-19th century. Matrices have since become a fundamental tool in various fields such as physics, computer science, economics, and engineering.

## Real-life Example

Consider a scenario where a company tracks its monthly sales data using matrices. The matrix $A$ represents the sales data for the first quarter of the year, and the matrix $B$ represents the sales data for the second quarter. By adding the matrices $A$ and $B$, the company can obtain the total sales for the first half of the year. Similarly, by subtracting the matrices $A$ and $B$, the company can analyze the difference in sales between the two quarters.

## Exam Questions
1. Given matrices $A=\begin{bmatrix} 2& 3\\ 4& 1\end{bmatrix}$ and $B=\begin{bmatrix} 1& 1\\ 2& 2\end{bmatrix}$, calculate $A+ B$.
2. Show that matrix addition is commutative using arbitrary matrices $A$ and $B$ of the same size.
3. Define the zero matrix and explain its role in matrix addition.