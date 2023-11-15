# Summary Notes (Algebra, Mid-Term 1)
## Bases
The number of digits in base $b$ of a non-negative integer $n$ is given by the formula
$$
k=\log_bn+1=\frac{\log n}{\log b}+1\impliedby b^{k-1}\le n\lt b^k
$$
### Converting from base $b$ to $10$
#### For an integer $n$
$$
n=(\ldots((d_{k-1}b+d_{k-2})b+d_{k-3})b+\cdots+d_1)b+d_0
$$
e.g.
$$
(61405)_7=(((6\cdot7+1)\cdot7+4)\cdot7+0)\cdot7+5=14950
$$
or via a tabular method

| (7) | 6   | 1   | 4   | 0    | 5     |
| --- | --- | --- | --- | ---- | ----- |
|     | 0   | 42  | 301 | 2135 | 14945 |
|     | 6   | 43  | 305 | 2135 | 14050 | 
#### For a real number $n$
$$
n_b:n_{10}=\frac{(\text{integer part|point part})_{b\to10}}{b^\text{number of point digits}}
$$
e.g.
$$
(14.22)_5\to n_{10}:n=\frac{(1422)_{5\to10}}{5^2}=\frac{237}{25}=9.48
$$
### Converting from base $10$ to $b$
#### For an integer $n$
$$
\begin{matrix}
14950=7\cdot2135+5\\
2135=7\cdot305+0\\
305=7\cdot43+4\\
43=7\cdot6+1\\
6=7\cdot0+6
\end{matrix}
\implies(14950)_{10}=(61405)_{7},\text{ by reading the remainders upwards}
$$
#### For a real number $n$
$$
2.481\to n_3:2.481=2+0.481\implies
\begin{matrix}
0.481\cdot3=0.433+1\\
0.443\cdot3=0.329+1\\
0.329\cdot3=0.987+0\\
0.987\cdot3=0.961+2\\
0.961\cdot3=0.883+2
\end{matrix}
\therefore2.481=(2.11022\cdots)_3
$$
Note that $2_{10}=2_3$.
## Arithmetic and geometric progressions
### Arithmetic progressions
Given a finite sequence of complex numbers $a_1, a_2, \ldots, a_n$, if the difference $d=a_{k+1}-a_k$ between two consecutive terms is constant ($d$ is independent of $k$), then the sequence is arithmetic.

Hence, a sequence is an arithmetic progression precisely when each term is the arithmetic mean of the preceding and the following term.
$$
a_n=a_1+d(n-1)
$$
#### Sum of an arithmetic progression
$$
\sum_{k=1}^n a_k=a_1+a_2+a_3+\cdots+a_n=\frac{(a_1+a_n)\cdot n}{2}
$$
The above result can be shown by noting that any two terms which have the same distance from both ends have the same sum
$$
a_k+a_{n-k+1}=(a_1+d(k-1))+(a_1+d(n-k))=2a_1+d(n-1)=a_1+a_n
$$
and hence,
$$
2(a_1+a_2+\cdots+a_n)=(a_1+a_2+\cdots+a_n)+(a_n+a_{n-1}+\cdots+a_1)=n\cdot(a_1+a_n)
$$
### Geometric progressions
Given the same finite sequence, the results are analogous to the arithmetic progressions, only that sums and differences map to products and quotients.

Hence, a sequence is a geometric progression precisely when each term is the geometric mean of the preceding and the following term.
$$
a_n=a_1\cdot r^{n-1}
$$
#### Product of a geometric progression
$$
\prod_{k=1}^{n}a_k=a_1\cdot a_2\cdots a_n=\sqrt{(a_1a_n)^n}\quad n\text{th power of the geometric mean}
$$
#### Sum of a geometric progression
##### Finite sum
$$
a_1+a_2+a_3+\cdots=a_1(1+r+r^2+\cdots+r^{n-1})=\frac{a_1(1-r^n)}{1-r}
$$
##### Infinite sum
$$
a_1+a_2+a_3+\cdots=a_1(1+r+r^2+r^3+\cdots)=\frac{a_1}{1-r}
$$

## Square roots of complex numbers
$$
\sqrt{a + bi} = \pm \left( \sqrt{\frac{a + \sqrt{a^2 + b^2}}{2}} + i\sqrt{\frac{-a + \sqrt{a^2 + b^2}}{2}} \right)
$$
This is derived by the following
$$
(x+iy)^2=a+ib
$$
$$
x^2-y^2+2ixy=a+ib
$$
$$
\begin{matrix}
\Re: x^2-y^2=a\\
\Im: 2xy=b\\
\end{matrix}
$$
$$
4x^4-4ax^2-b^2=0
$$
This is a biquadratic and easy to solve to then get the above result.
## Polynomials
$$
\begin{matrix}
x^2-a^2=(x-a)(x+a)\\
x^2+a^2=(x-ai)(x+ai)\\
x^3-a^3=(x-a)(x^2+ax+a^2)\\
x^3+a^3=(x+a)(x^2-ax+a^2)\\
x^4+a^4=(x^2-\sqrt{2}ax+a^2)(x^2+\sqrt{2}ax+a^2)\\
\end{matrix}
$$
### Ruffini's rule application to find a polynomial in terms of $x-a$
Special case, where you're doing repeated divisions, so can just carry on the table down (taking off one column at a time as the remainder.)
![[Pasted image 20231113123615.png]]
### Euclid's algorithm for polynomials
Repeat the Euclidean algorithm as it is for integers, until the remainder is zero.
#### Extending the algorithm
...
## Finding rational roots of a polynomial
Given a polynomial $f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_2x^2+a_1x+a_0$, if $f(\frac{r}{s})=0:(r,s)=1\implies r|a_0, s|a_n$.
Thus, the rational roots of $f(x)$ by the rational root theorem are:
$$
\frac{r}{s}=\frac{D(\pm a_0)}{D(\pm a_n)}:f(\frac{r}{s})=0
$$
### Shortcuts
#### Self-reciprocal polynomials
The solving process for self-reciprocal polynomials involves manipulation to take advantage of their structure. Given a polynomial:

$$
ax^4+bx^3+cx^2+bx+a=0
$$

Divide through by $x^2$ to get:

$$
a\left(x^2+\frac{1}{x^2}\right)+b\left(x+\frac{1}{x}\right)+c=0
$$

Next, recognize that $x^2 + \frac{1}{x^2}$ can be rewritten using the identity $x + \frac{1}{x}$, giving us a transformed quadratic equation:

$$
a\left(x+\frac{1}{x}\right)^2+b\left(x+\frac{1}{x}\right)+(c-2a)=0
$$

Solving for $x+\frac{1}{x}$ yields:

$$
x+\frac{1}{x}=\frac{-b\pm\sqrt{b^2-4a(c-2a)}}{2a}=k
$$

We simplify the quadratic formula to reach a constant $k$, and solve the new quadratic equation:

$$
x^2-kx+1=0
$$

Hence:

$$
x=\frac{k\pm\sqrt{k^2-4}}{2}:k=\frac{-b\pm\sqrt{b^2-4a(c-2a)}}{2a}
$$
## Symmetric functions of the roots of quadratic polynomials
$$
ax^2+bx+c=a(x-\alpha)(x-\beta)=a(x^2-(\alpha+\beta)x+\alpha\beta)
$$
Using this result, we can solve systems of two equations by using a quadratic equation, such as
$$
\begin{matrix}
x+y=s\\
xy=p\\
\end{matrix}
$$
Symmetric polynomials are made of these two expressions $(x+y)$ and $(xy)$.
![[Pasted image 20231113141525.png]]
