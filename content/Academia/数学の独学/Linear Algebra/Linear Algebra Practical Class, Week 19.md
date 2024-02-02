### Question One

#### Question

Determine whether the following vectors are [[linearly independent]]:

1. $\vec{u}=\begin{bmatrix}3 \\ 1\end{bmatrix}, \vec{v}=\begin{bmatrix}0 \\ -1\end{bmatrix}$.

2. $\vec{u}=\begin{bmatrix}2 \\ -1\end{bmatrix}, \vec{v}=\begin{bmatrix}-1 \\ -1\end{bmatrix}$.

#### Solution

$$
\begin{align*}
\begin{bmatrix}0\\
0\end{bmatrix}&=c_{1}\begin{bmatrix}3 \\ 1\end{bmatrix}+c_{2}\begin{bmatrix}0 \\ -2\end{bmatrix}\\
&= \begin{bmatrix}3c_{1}\\
c_{1}\end{bmatrix}+\begin{bmatrix}0\\
-2c_{2}\end{bmatrix}
\end{align*}
$$

Thus the only solution is $c_{1}=0$ and $c_2=0$, therefore the two vectors are linearly independent.

___
$$
\begin{align*}
\begin{bmatrix}0\\
0\end{bmatrix}&=c_{1}\begin{bmatrix}2 \\ -1\end{bmatrix}+c_{2}\begin{bmatrix}-1 \\ -1\end{bmatrix}\\
&= \begin{bmatrix}2c_{1}\\
-c_{1}\end{bmatrix}+\begin{bmatrix}-c_{2}\\
-c_{2}\end{bmatrix}
\end{align*}
$$

Thus $c_{1}=-c_{2}\implies 0=3c_{1}$, therefore the only solution is $c_{1}=0$ and $c_{2}=0$ such that both vectors are linearly independent.

### Question Two

#### Question


Find a value for $x$ so that the following vectors are linearly dependent, and another value for which they are linearly independent:

$$\vec{u}=\begin{bmatrix}1 \\ 1\end{bmatrix}, \vec{v}=\begin{bmatrix}1 \\ x\end{bmatrix}$$

#### Solution

Let $c_{1},c_{2}\in \mathbb{R}$ satisfying $c_{1}\mathbf{u}+c_{2}\mathbf{v}=0\implies$

$$
\begin{bmatrix}c_{1}+c_{2} \\ c_{1}+x\cdot c_{2}\end{bmatrix}=\begin{bmatrix}0 \\ 0\end{bmatrix}\implies c_{2}(x-1)=0
$$

Thus, the vectors are linearly dependent if $x=1$ as the two vectors are then multiples of one another and there are infinite solutions to the system of equations.

Alternatively, the vectors are linearly independent if $x\ne1$, for example $x=2$, as the solution to the system of equations would be where $c_{1}=c_{2}=0$.

### Question Three

#### Question

Find two nontrivial vectors (other than $\vec{e}_{1},\vec{e}_{2}$) that span the plane.

#### Solution

The are an infinite number of vectors that span the 2D plane, other than the trivial vectors $\mathbf{e}_{1}$ and $\mathbf{e}_{2}$, and simply include any two linearly independent vectors. For example,

$$
\mathbf{v}_{1}=\begin{bmatrix}2 \\ 1\end{bmatrix},\mathbf{v}_{2}=\begin{bmatrix}-1 \\ 2\end{bmatrix}
$$

### Question Four

#### Question

Show that the following vectors are [[linearly dependent]]:

$$\vec{u}=\begin{bmatrix}-1 \\ 1\end{bmatrix}, \vec{v}=\begin{bmatrix} \frac{1}{3} \\ -\frac{1}{3} \end{bmatrix}$$

#### Solution

Let $c_{1},c_{2}\in \mathbb{R}$ satisfying $c_{1}\mathbf{u}+c_{2}\mathbf{v}=0\implies$

$$
\begin{bmatrix}-c_{1} + \frac{1}{3}c_{2} \\ c_{1}- \frac{1}{3}c_{2}\end{bmatrix}=\begin{bmatrix}0 \\ 0\end{bmatrix}
$$

Here we can see the system of equations is unsolvable and has infinite solutions, as $\mathbf{u}$ and $\mathbf{v}$ are multiples of one another.

### Question Five

#### Question

Determine whether the vector $\vec{u}=\begin{bmatrix}1 \\ 2\end{bmatrix}$ is a linear combination of $\vec{v}=\begin{bmatrix}0 \\ 2\end{bmatrix}$ and $\vec{w}=\begin{bmatrix}1 \\ 4\end{bmatrix}$.

If so, find the scalars.

#### Solution

If $\mathbf{u}$ is a linear combination of $\mathbf{v}$ and $\mathbf{w}$, then $\mathbf{u}=c_{1}\mathbf{v}+c_{2}\mathbf{w}\implies$

$$
\begin{bmatrix}0+c_{2} \\ c_{1}+4c_{2}\end{bmatrix}=\begin{bmatrix}1 \\ 2\end{bmatrix}\implies c_{1}=-2,\quad c_{2}=1
$$

Therefore, $\mathbf{u}$ is a linear combination of $\mathbf{v}$ and $\mathbf{w}$, where the scalars are $-2$ and $1$, respectively.