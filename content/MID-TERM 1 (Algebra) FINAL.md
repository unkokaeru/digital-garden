# Formulae
The number of digits in base $b$ of a non-negative integer $n$ is given by the formula
$$
k=\log_bn+1=\frac{\log n}{\log b}+1\impliedby b^{k-1}\le n\lt b^k
$$
$$
n_b:n_{10}=\frac{(\text{integer part|point part})_{b\to10}}{b^\text{number of point digits}}
$$
$$
\frac{\text{integer part|pre-period|period}-\text{intger part|pre-period}}{\text{digits of the period replaced by }(b-1)\text{s|digits of the pre-period replaced by 0s}}
$$
Given a polynomial $f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_2x^2+a_1x+a_0$, if $f(\frac{r}{s})=0:(r,s)=1\implies r|a_0, s|a_n$.
Thus, the rational roots of $f(x)$ by the rational root theorem are:
$$
\frac{r}{s}=\frac{D(\pm a_0)}{D(\pm a_n)}:f(\frac{r}{s})=0
$$
___
$$
a_n=a_1\cdot r^{n-1}
$$
$$
\prod_{k=1}^{n}a_k=a_1\cdot a_2\cdots a_n=\sqrt{(a_1a_n)^n}\quad n\text{th power of the geometric mean}
$$
$$
a_1+a_2+a_3+\cdots=a_1(1+r+r^2+\cdots+r^{n-1})=\frac{a_1(1-r^n)}{1-r}
$$
$$
a_1+a_2+a_3+\cdots=a_1(1+r+r^2+r^3+\cdots)=\frac{a_1}{1-r}
$$
___
$$
a_n=a_1+d(n-1)
$$
$$
S_n=\frac{n}{2}(a_1+a_n)=\frac{n}{2}(2a_1+(n-1)d)
$$
# Summary Examples (Algebra, Mid-Term 1)
*7 Questions*
## Bases
### The first way
Convert the following base 8 periodic number into base 10, then convert the answer back to verify it.
$$
7431.8774\overline{2516}
$$
**Solution**
$$
\frac{(743187742516)_8-(74318774)_8}{(77770000)_8}=\frac{(743113423742)_8}{(77770000)_8}=\frac{64846964706}{16773120}=\frac{10807827451}{2795520}
$$

| (8) | 7   | 4   | 3   | 1    | 1     | 3      | 4       | 2        | 3         | 7          | 4          | 2           |
| --- | --- | --- | --- | ---- | ----- | ------ | ------- | -------- | --------- | ---------- | ---------- | ----------- |
|     | 0   | 56  | 480 | 3864 | 30920 | 247368 | 1978968 | 15831776 | 126654224 | 1013233816 | 8105870584 | 64846964704 |
|     | 7   | 60  | 483 | 3865 | 30921 | 247371 | 1978972 | 15831778 | 126654227 | 1013233823 | 8105870588 | 64846964706            |

| (8) | 7   | 7   | 7   | 7    | 0     | 0      | 0       | 0        |
| --- | --- | --- | --- | ---- | ----- | ------ | ------- | -------- |
|     | 0   | 56  | 504 | 4088 | 32760 | 262080 | 2096640 | 16773120 |
|     | 7   | 63  | 511 | 4095 | 32760 | 262080 | 2096640 | 16773120 | 
### The second way
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
## Polynomials
Find solutions to the following linear combination. Use Ruffini's rule where possible, otherwise use polynomial long division. Afterwards, express every function in terms of powers of $(x-2)$.
$$
(x^3-2x^2+x-2)\cdot u(x)+(x^2-3x+2)\cdot v(x)=1
$$
**Solution**
$$
(x^3-2x^2+x-2)=(x^2-3x+2)(x+1)+(2x-4)
$$
![[Pasted image 20231113194216.png]]
$$
(x^2-3x+2)=(x-2)(x-1)+0
$$

| (2) | 1   | -3  | 2   |
| --- | --- | --- | --- |
|     | 0   | 2   | -2  |
|     | 1   | -1  | 0    |
$$
r(x)=x-2
$$
etc. - extended is just plugging the last remainder into the one above, and so on (simplifying each step into a linear combination), until the final linear combination.
If it's numerical rather than polynomial, then you may need to find every solution. This means in a linear combination $ax+by=r$ the full solution would be $a(x+cn)+b(x-dn)=r$, where $ac-bd=0$.
### Finding irreducible polynomials
Always conclude that it's irreducible, showing why (by trying to do it and showing you cannot).
#### Techniques
##### Formulae
$$
\begin{matrix}
x^2-a^2=(x-a)(x+a)\\
x^2+a^2=(x-ai)(x+ai)\\
x^3-a^3=(x-a)(x^2+ax+a^2)\\
x^3+a^3=(x+a)(x^2-ax+a^2)\\
x^4+a^4=(x^2-\sqrt{2}ax+a^2)(x^2+\sqrt{2}ax+a^2)\\
\end{matrix}
$$
##### Finding the square root of a complex number
Find the square root of $3+4i$, purely algebraically.
**Solution**
$$
(x+iy)^2=3+4i
$$
$$
x^2-y^2+2ixy=3+4i
$$
$$
\begin{matrix}
x^2-y^2=3\\
2xy=4
\end{matrix}
$$
$$
x^2-\frac{2^2}{x^2}=3\implies x^4-3x^2-4=0\implies x^2=4,-1\implies x=\pm2,y=\pm1
$$
$$
\therefore\pm(2+i)
$$
#### Decomposition into irreducible factors
Decompose $x^4-5x^2+6$ into irreducible factors under $\mathbb{Z}[x],\mathbb{Q}[x],\mathbb{R}[x],\mathbb{C}[x]$.
**Solution**
$$
\begin{matrix}
\mathbb{Z}:x^4-5x^2+6=(x^2-3)(x^2-2)\\
\mathbb{Q}:x^4-5x^2+6=(x^2-3)(x^2-2)\\
\mathbb{R}:x^4-5x^2+6=(x+\sqrt{3})(x-\sqrt{3})(x+\sqrt{2})(x-\sqrt{2})\\
\mathbb{C}:x^4-5x^2+6=(x+\sqrt{3})(x-\sqrt{3})(x+\sqrt{2})(x-\sqrt{2})\\
\end{matrix}
$$
### Finding roots of a polynomial
Find all of the rational roots, and then all general roots, of the polynomial $p(x)=4x^4+6x^3+2x^2+6x+4$
**Solution**
$$
\frac{r}{s}=\frac{D(4)}{D(4)}=\frac{\pm1,\pm2,\pm4}{\pm1,\pm2,\pm4}=1,2,4,\frac{1}{2},\frac{1}{4}
$$
$$
\text{Only positive co-efficients, thus positive r/s, also self-reciprocal}
$$
$$
\begin{matrix}
p(1)\ne0\\
p(136)\ne0\\
p(1468)\ne0\\
p(8.5)\ne0\\
p(5.734375)\ne0\\
\end{matrix}\therefore\text{no rational roots}
$$
___
$$
a\left(x^2+\frac{1}{x^2}\right)+b\left(x+\frac{1}{x}\right)+c=0
$$
$$
a\left(x+\frac{1}{x}\right)^2+b\left(x+\frac{1}{x}\right)+(c-2a)=0
$$
