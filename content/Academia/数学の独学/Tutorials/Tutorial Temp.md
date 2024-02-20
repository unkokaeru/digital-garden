$2^{n}>100n$ for any $n\ge10$.

$1^{\circ}\quad n=10:2^{10}>1000\iff1024>1000$.
$2^{\circ}\quad \text{Suppose that }2^{k}>100k:k\ge10$,
$\quad\quad 2^{k+1}=2\cdot2^{k}>2\cdot100k\text{ by the ind. hyp.}$,
$\quad\quad 2\cdot100k=100k+100k>100k+100>100(k+1)\text{ as required}$. From $1^{\circ}$ and $2^{\circ}$, the inequality holds for all $n\ge10$ by the axiom of mathematical induction (AMI).

___

$\mathbf{u}=\begin{bmatrix}1 \\ -1 \\ 2\end{bmatrix},\mathbf{v}=\begin{bmatrix}-3 \\ 2 \\ 4\end{bmatrix},\mathbf{w}=\begin{bmatrix}-2 \\ 1 \\ 6\end{bmatrix}$ : show that these are linearly dependent.

$\mathbf{w}=\mathbf{u}+\mathbf{v}$.

OR

$c_{1}\mathbf{u}+c_{2}\mathbf{v}+c_{3}\mathbf{w}=\mathbf{0}\implies c_{1},c_{2},c_{3}=0$, when linearly independent.

$$
\begin{align*}
\begin{bmatrix}
1 & -3 & -2 & | & 0 \\ 
-1 & 2 & 1 & | & 0 \\ 
2 & 4 & 6 & | & 0
\end{bmatrix}&=\begin{bmatrix}1 & -3 & -2 & | & 0\\
0 & -1 & -1 & | & 0\\
1 & 2 & 3 & | & 0\end{bmatrix}\\
&=\begin{bmatrix}1 & -3 & -2 & | & 0\\
0 & -1 & -1 & | & 0\\
0 & 1 & 1 & | & 0\end{bmatrix}\\
&= \begin{bmatrix}1 & 0 & 1 & | & 0\\
0 & 1 & 1 & | & 0\\
0 & 1 & 1 & | & 0\end{bmatrix}\\
&= \begin{bmatrix}1 & 0 & 1 & | & 0\\
0 & 1 & 1 & | & 0\\
0 & 0 & 0 & | & 0\end{bmatrix}\\
&= \begin{cases}
c_{1}+c_{3}=0\\
c_{2}+c_{3}=0
\end{cases}\\
\end{align*}
$$
$$
-c_{3}\mathbf{u}-c_{3}\mathbf{v}+c_{3}\mathbf{w}=\mathbf{0}
$$
$$
-\mathbf{u}-\mathbf{v}+\mathbf{w}=\mathbf{0}\therefore\boxed{\text{linearly dependent}}
$$


$$
\begin{align*}
\text{span}(\mathbf{u},\mathbf{v},\mathbf{w})&=\text{span}(\mathbf{u},\mathbf{v},\mathbf{u}+\mathbf{v})\\
&= \text{span}(\mathbf{u},\mathbf{v})
\end{align*}
$$

___

For what values of $k$ will...
$$
\begin{cases}
kx+2y&=3\\
2x-4y&=-6
\end{cases}
$$
have 1. infinitely many solutions, 2. a unique solution, 3. no solutions.

$$
\begin{align*}
\begin{bmatrix}k & 2 & | & 3 \\ 2 & -4 & | & -6\end{bmatrix}&=\begin{bmatrix}k & 2 & | & 3\\
1+k & 0 & | & 0\end{bmatrix}\\
&= \begin{cases}
kx+2y&=3\\
(1+k)x&=0
\end{cases}
\end{align*}
$$
$$
\boxed{\therefore\begin{cases}
k=-1&y=\frac{3}{2}+ \frac{1}{2}x \\
k\ne-1 & (0,\frac{3}{2})
\end{cases}}
$$
No values of $k$ such that the system is inconsistent.