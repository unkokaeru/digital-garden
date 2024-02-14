
$$
\begin{cases}
3x+2y=10 \\
6x+4y=c
\end{cases}
$$

$$
\iff
\begin{bmatrix}
3 & 2 & | & 10 \\ 
6 & 4 & | & c
\end{bmatrix}
$$

$$
\iff
\begin{bmatrix}
3 & 2 & | & 10 \\ 
0 & 0 & | & c-20
\end{bmatrix}
$$

$$
\iff
\begin{cases}
c=20&:\mathbb{S}=\{\begin{bmatrix}x \\
5 - \frac{3}{2}x\end{bmatrix}\in \mathbb{R}^{2}:x\in \mathbb{R}\} \\
c\ne20&:\mathbb{S}=\emptyset
\end{cases}
$$

___
Determine whether $\mathbf{u}\in\text{span}(\mathbf{v},\mathbf{w})$, where...

$$
\mathbf{u}=\begin{bmatrix}1 \\ 2 \\ 3\end{bmatrix},\mathbf{v=\begin{bmatrix}1 \\ 0 \\ 3\end{bmatrix}},\mathbf{w}=\begin{bmatrix}1 \\ 1 \\ 3\end{bmatrix}
$$

$\mathbf{u}\in\text{span}(\mathbf{v},\mathbf{w})\iff$ there are scalars $x,y$ such that $x \mathbf{v}+y \mathbf{w}= \mathbf{u}$,

$$
\begin{bmatrix}
1 & 1 & | & 1 \\ 
0 & 1 & | & 2 \\ 
3 & 3 & | & 3\end{bmatrix}
$$

$$
\iff
\begin{bmatrix}
1 & 0 & | & 3 \\ 
0 & 1 & | & 2 \\ 
0 & 0 & | & 0\end{bmatrix}
$$

$$
\iff x=3,y=2\therefore\text{Yes}
$$
