## Example

### Question

Compute the linear combinations of the vectors

$$
\mathbf{u}=\begin{bmatrix}1 \\ 1 \\ 0\end{bmatrix} \text{and }\mathbf{v}=\begin{bmatrix}0 \\ 1 \\ 1\end{bmatrix}
$$
and show that they span a plane in $\mathbb{R}^{3}$. Find a vector that is not a linear combination of $\mathbf{u}$, $\mathbf{v}$.

### Solution

Assume $c_{1}$ and $c_{2}$ such that

$$
c_{1}\mathbf{u}+c_{2}\mathbf{v}\iff\begin{bmatrix}c_{1} \\ c_{1}+c_{2} \\ c_{2}\end{bmatrix}
$$

$$
\begin{align*}
\iff\text{span}(\mathbf{u},\mathbf{v})&=\left(\begin{bmatrix}c_{1} \\ c_{1} +c_{2} \\ c_{2}\end{bmatrix}:c_{1},c_{2}\in \mathbb{R}\right)\\
&= \left(\begin{bmatrix}x\\
x+z\\
z\end{bmatrix}:x,z\in \mathbb{R}\right)
\end{align*}
$$

Hence $y=x+z$, a plane in $\mathbb{R}^{3}$. One vector that contradicts this, is simply any vector that does not lie on this plane: where $y\ne x+z$, e.g.

$$
w=\begin{bmatrix}1 \\ 0 \\ 2\end{bmatrix}
$$
