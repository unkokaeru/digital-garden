### Question One

#### Question

Let $\{\mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\}$ be the standard vectors in $\mathbb{R}^{3}$. Determine whether

$$
\text{span}(\mathbf{e}_{1},-2\mathbf{e}_{2},\mathbf{e}_{1}+\mathbf{e}_{2}-\mathbf{e}_{3})=\mathbb{R}^{3}
$$

#### Solution

If the three vectors span $\mathbb{R}^{3}$, then they must be able to generate any general vector in the plane $\mathbf{x}=[x_{1},x_{2},x_{3}]\in \mathbb{R}^{3}$, such that if we let $c_{1},c_{2},c_{3}\in \mathbb{R}$ and $\mathbf{w}\in \mathbb{R}^{3}$ satisfy the following equation:

$$
c_{1}(\mathbf{e}_{1})+c_{2}(-2\mathbf{e}_{2})+c_{3}(\mathbf{e}_{1}+\mathbf{e}_{2}-\mathbf{e}_{3})=\mathbf{w}
$$

$$
\iff (c_{1}+c_{3})\mathbf{e}_{1}+(-2c_{2}+c_{3})\mathbf{e}_{2}+(-c_{3})\mathbf{e}_{3}=\mathbf{w}
$$

$$
\iff\begin{bmatrix}c_{1}+c_{3} \\ -2c_{2}+c_{3} \\ -c_{3}\end{bmatrix}=\mathbf{w}=\mathbf{x}
$$

$$
\iff\begin{cases}
c_{1}+c_{3}=x_{1} \\
-2c_{2}+c_{3}=x_{2} \\
-c_{3}=x_{3}
\end{cases}
$$

$$
\iff c_{3}=-x_{3},\quad c_{2}=-\frac{x_{2}+x_{3}}{2},\quad c_{1}=x_{1}+x_{3}
$$

Hence, the vectors span $\mathbb{R}^{3}$.$\quad\square$

### Question Two

#### Question

Find the span of the following vectors:

$$
\mathbf{u}=\begin{bmatrix}0 \\ -2 \\ 0 \\ 5\end{bmatrix},\mathbf{v}=\begin{bmatrix}3 \\ 1 \\ 1 \\ 0\end{bmatrix}
$$
and

$$
\mathbf{u}=\begin{bmatrix}1 \\ -1 \\ 0 \\ 2\end{bmatrix},\mathbf{v}=\begin{bmatrix}0 \\ - \frac{1}{2} \\ \frac{3}{2} \\ 1\end{bmatrix},\mathbf{w}=\begin{bmatrix}-1 \\ 0 \\ 1 \\ 0\end{bmatrix}
$$

#### Solution

$$
\begin{align*}
\text{span}_{1}&=c_{1}\mathbf{u}+c_{2}\mathbf{v}\\
&= c_{1}\begin{bmatrix}0\\
-2\\
0\\
5\end{bmatrix}+c_{2}\begin{bmatrix}3\\
1\\
1\\
0\end{bmatrix}\\
&= \begin{bmatrix}c_{2}\\
-2c_{1}+c_{2}\\
c_{2}\\
5c_{1}\end{bmatrix}
\end{align*}
$$

...

### Question Three

#### Question

Find a value for $c$ so that the following vectors are linearly independent:

$$
\mathbf{u}=\begin{bmatrix}1 \\ 1-c\end{bmatrix}, \mathbf{v}=\begin{bmatrix}1 \\ 0\end{bmatrix}
$$

#### Solution

By inspection, we can see that the solution is such that:
$$
c\ne1
$$

Formerly however, if we let $c_{1},c_{2}\in \mathbb{R}$, then the vectors must satisfy the equation $c_{1}\mathbf{u}+c_{2}\mathbf{v}=\mathbf{0}\implies c_{1}=c_{2}=0$.

$$
\begin{bmatrix}c_{1}+c_{2} \\ c_{1}(1-c)\end{bmatrix}=\begin{bmatrix}0 \\ 0\end{bmatrix}\iff\begin{cases}
c_{1}+c_{2}=0 \\
c_{1}(1-c)=0
\end{cases}:c=1\implies c\ne1
$$

if linearly independent (since if $c=1$ then the vectors are linearly dependent, but if $c=k:k\ne1$ then the vectors are linearly independent).

### Question Four

#### Question

Find the dot product, the length, and the angle between the vectors:

$$
\mathbf{u}=\begin{bmatrix}0 \\ \frac{1}{2} \\ - \frac{1}{2}\end{bmatrix}, \mathbf{v}=\begin{bmatrix} \frac{1}{2} \\ \frac{2}{3} \\ \frac{2}{3}\end{bmatrix}
$$

Then, verify the Cauchy-Schwarz inequality and the triangle inequality.

#### Solution

$$
\begin{align*}
\mathbf{u}\cdot \mathbf{v}&=\begin{bmatrix}0\\
\frac{1}{2}\\
- \frac{1}{2}\end{bmatrix}\cdot\begin{bmatrix} \frac{1}{2}\\
\frac{2}{3}\\
 \frac{2}{3}\end{bmatrix}\\
&= 0 + \frac{2}{6} - \frac{2}{6}\\
&= 0\therefore\text{orthogonal}
\end{align*}
$$

...