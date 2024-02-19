### Question One

#### Question

Find the solution set which corresponds to the following row echelon forms:

1. $M_{1}=\begin{bmatrix}1 & -2 & -1 & | & 0 \\ 0 & 2 & 1 & | & 0\end{bmatrix}$,

2. $M_{2}=\begin{bmatrix}1 & 0 & 1 & 2 & | & 0 \\ 0 & 3 & -1 & -1 & | & 0\end{bmatrix}$.

#### Solution

$$
\begin{align*}
R_{2}\mapsto R_{2}+R_{1}&\iff\begin{bmatrix}1 & 0 & 0 & | & 0\\
0 & 1 & \frac{1}{2} & | & 0\end{bmatrix}\\\\
&\iff \begin{cases}
x=0\\
y+ \frac{1}{2}z=0
\end{cases}\\
&\iff z=-2y\\
&\iff S=\{\begin{bmatrix}0 \\ y \\ -2y\end{bmatrix}\in \mathbb{R}^{3}:y\in \mathbb{R}\}\\
&\iff S=\text{span}(\begin{bmatrix}0\\1\\-2\end{bmatrix})
\end{align*}
$$
___
$$
\begin{align*}
...
\end{align*}
$$

### Question Two

#### Question

Solve the system with three equations and four unknowns using Gauss-Jordan elimination, and write its set of solutions:

$$
\begin{cases}
x_{1}+2x_{2}-2x_{3}+2x_{4}=1 \\
2x_{1}-4x_{2}+4x_{3}+6x_{4}=0 \\
x_{1}+2x_{2}-2x_{3}+3x_{4}=0
\end{cases}
$$

#### Solution

$$
\begin{align*}
\begin{cases}
x_{1}+2x_{2}-2x_{3}+2x_{4}=1 \\
2x_{1}-4x_{2}+4x_{3}+6x_{4}=0 \\
x_{1}+2x_{2}-2x_{3}+3x_{4}=0
\end{cases}&\iff\begin{bmatrix}1 & 2 & -2 & 2 & | & 1\\
2 & -4 & 4 & 6 & | & 0\\
1 & 2 & -2 & 3 & | & 0\end{bmatrix}\\
&\iff R_{1}\mapsto R_{1}-R_{3}\\
&\iff \begin{bmatrix}0 & 0 & 0 & -1 & | & 1\\
2 & -4 & 4 & 6 & | & 0\\
1 & 2 & -2 & 3 & | & 0\end{bmatrix}\\
&\iff R_{2}\mapsto \frac{R_{2}+2R_{3}}{4}\\
&\iff \begin{bmatrix}0 & 0 & 0 & -1 & | & 1\\
1 & 0 & 0 & 3 & | & 0\\
1 & 2 & -2 & 3 & | & 0\end{bmatrix}\\
&\iff \begin{cases}
-x_{4}=1\\
x_{1}+3x_{4}=0\\
x_{1}+2x_ 2-3x_{3}+3x_{4}=0
\end{cases}\\
&\iff x_{1}=3,x_{4}=-1, x_{2}=\frac{3}{2} x_{3}\\
&\iff S=\set{\begin{bmatrix}3\\
\frac{3}{2}x_{3}\\
x_{3}\\
-1\end{bmatrix}\in \mathbb{R}^{4}:x_{3}\in \mathbb{R}}
\end{align*}
$$

### Question Three

#### Question

Let $\mathbf{v}_{1}=\begin{bmatrix}1 \\ 0 \\ 0\end{bmatrix},\quad \mathbf{v}_{2}=\begin{bmatrix}1 \\ 1 \\ 0\end{bmatrix},\quad\mathbf{v}_{3}=\begin{bmatrix}1 \\ 1 \\ 1\end{bmatrix}$ be vectors in $\mathbb{R}^{3}$.

Using Gauss-Jordan elimination:

1. Show that the vectors are linearly dependent.

2. Determine whether the vector $\mathbf{u}=\begin{bmatrix}0 \\ 1 \\ 1\end{bmatrix}$ belongs to the span of the vectors $\mathbf{v}_{1},\mathbf{v}_{2},\mathbf{v}_{3}$.

#### Solution

$$
\begin{align*}
\begin{bmatrix}1 & 1 & 1 & | & 0 \\ 0 & 1 & 1 & | & 0 \\ 0 & 0 & 1 & | & 0\end{bmatrix}&\iff R_{1}\mapsto R_{1}-R_{2},R_{2}\mapsto R_{2}-R_{3}\\
&\iff\begin{bmatrix}1 & 0 & 0 & | & 0\\
0 & 1 & 0 & | & 0\\
0 & 0 & 1 & | & 0\end{bmatrix}\\
&\iff\begin{cases}
x=0\\
y=0\\
z=0
\end{cases}\\
&\therefore\text{linearly dependent}
\end{align*}
$$

___
$$
\begin{align*}
\begin{bmatrix}1 & 1 & 1 & | & 0\\
0 & 1 & 1 & | & 1\\
0 & 0 & 1 & | & 1\end{bmatrix}&\iff R_{2}\mapsto R_{2}-R_{3}\\
&\iff\begin{bmatrix}1 & 1 & 1 & | & 0\\
0 & 1 & 0 & | & 0\\
0 & 0 & 1 & | & 1\end{bmatrix}\\
&\iff\begin{cases}
x+y+z=0\\
y=0\\
z=0
\end{cases}\\
&\iff x=y=z=0
\end{align*}
$$

### Question Four

#### Question

Considering the following matrices, denote which are in row-echelon form and which of those are in reduced row-echelon form:

1. $B_{1}=\begin{bmatrix}-1 & 0 & 1 \\ 0 & 2 & 1 \\ 0 & 0 & 5 \\ 0 & 0 & -1\end{bmatrix}$,

2. $B_{2}=\begin{bmatrix}1 & 2 & 0 & 5 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0\end{bmatrix}$,

3. $B_{3}=\begin{bmatrix}1 & -1 \\ 0 & 1 \\ 0 & 0\end{bmatrix}$,

4. $B_{4}=\begin{bmatrix}1 & 0 & 0 & -2 & 5 \\ 0 & 1 & 0 & 9 & -2 \\ 0 & 0 & 1 & 4 & 3\end{bmatrix}$.

#### Solution

Row Echelon Form: $B_{2},B_{3},B_{4}$.
Reduced Row Echelon Form: $B_{2},B_{4}$.