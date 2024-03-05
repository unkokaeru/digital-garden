### Question One

#### Question

Find $x$ in the following equation...

$$
\begin{bmatrix}2 & -1 \\ 1 & 3\end{bmatrix}\begin{bmatrix}x & 3 \\ 2 & -1\end{bmatrix}=\begin{bmatrix}-6 & 7 \\ 4 & 0\end{bmatrix}
$$

#### Solution

$$
\begin{bmatrix}2x-2 & 7 \\ x+6 & 0\end{bmatrix}=\begin{bmatrix}-6 & 7 \\ 4 & 0\end{bmatrix}
$$

$$
\begin{cases}
2x-2=-6 \\
x+6=4
\end{cases}\implies\boxed{x=-2}
$$

### Question Two

#### Question

Do the vectors $\begin{bmatrix}1 \\ 1 \\ 0\end{bmatrix}$, $\begin{bmatrix}1 \\ 0 \\ 1\end{bmatrix}$, $\begin{bmatrix}0 \\ 1 \\ 1\end{bmatrix}$ form a basis for $\mathbb{R}^{3}$?

#### Solution

There are three vectors.

$$
c_{1}\mathbf{u}+c_{2}\mathbf{v}+c_{3}\mathbf{w}=\mathbf{0}\implies c_{1}=c_{2}=c_{3}=0:\text{linearly independent.}
$$

$$
\begin{align*}
\begin{bmatrix}1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1\end{bmatrix}&=\begin{bmatrix}1 & 1 & 0\\
0 & -1 & 0\\
0 & 1 & 1\end{bmatrix}\\
&=\begin{bmatrix}1 & 1 & 0\\
0 & -1 & 1\\
0 & 0 & 2\end{bmatrix}\\
&= \begin{bmatrix}1 & 1 & 0\\
0 & 1 & -1\\
0 & 0 & 1\end{bmatrix}\\
&= \begin{bmatrix}1 & 1 & 0\\
0 & 1 & 0\\
0 & 0 & 1\end{bmatrix}\\
&= \begin{bmatrix}1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1\end{bmatrix}
\end{align*}\implies \text{linearly independent}
$$

$$
\boxed{\therefore \text{basic for }\mathbb{R}^{3}}
$$

### Question Three

#### Question

...

#### Solution

$$
\begin{align*}
\begin{bmatrix}1 & 1 & 1 \\ 1 & 0 & 3 \\ 0 & 1 & -2\end{bmatrix}&=\begin{bmatrix}1 & 1 & 1\\
1 & 1 & 1\\
0 & 1 & -2\end{bmatrix}\text{by }R_{2}+R_{3}\\\\
&= \begin{bmatrix}1 & 1 & 1\\
0 & 1 & -2\\
0 & 0 & 0\end{bmatrix}\\
&= \begin{bmatrix}1 & 0 & 3\\
0 & 1 & -2\\
0 & 0 & 0\end{bmatrix}\\
&= \ldots
\end{align*}
$$

### Question Four

#### Question

$a\ne0$:

$F(x)=f(x)+a$ shifts up for a positive $a$, down for a negative $a$.
$F(x)=f(x+a)$ shifts left for a positive $a$, right for a negative $a$.
$F(x)=f(ax)$ stretches for $a<1$, compresses for $a>1$.

___

$f:[0,1)\to[1,\infty)$

$f(x)=\frac{1}{\sqrt{1-x^{2}}}$

Use the aforementioned transformations to produce another bijection (mapping) $F:[2,4)\to[0,\infty)$.

#### Solution

$F_{1}(x)=f(\frac{x}{2})=\frac{1}{\sqrt{1- \frac{1}{4}x^{2}}}$.
$F_{2}(x)=F_{1}(x-2)=\frac{1}{\sqrt{1- \frac{1}{4}(x-2)^{2}}}$.
$F_{3}(x)=f_{2}(x)-1=\frac{1}{\sqrt{1- \frac{1}{4}(x-2)^{2}}}-1$.

Therefore,

$$
\boxed{F(x) = \frac{1}{\sqrt{1- \frac{1}{4}(x-2)^{2}}}-1}
$$

### Question Five

#### Question

...

#### Solution

...

### Question Six

#### Question

...

#### Solution

...

### Question Seven

#### Question

...

#### Solution

...

### Question Eight

#### Question

...

#### Solution

...

### Question Nine

#### Question

...

#### Solution

...

### Question Ten

#### Question

...

#### Solution

...