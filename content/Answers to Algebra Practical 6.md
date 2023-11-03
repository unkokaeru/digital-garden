![[Practical_6.pdf]]

#### Question 1
Factorise $p(x)$ into a product of irreducible factors in $\mathbb{Q}[x]$, showing that each of the factors is irreducible, such that
$$
p(x)=x^3+4x^2+5x+6
$$
$$
\text{Using the rational root test, }\frac{r}{s}=\frac{\pm6,\pm3,\pm2,\pm1}{\pm1}
$$
$$
\text{As all coefficients are positive, the only values of }\frac{r}{s}\text{ possible are negative:}
$$
$$
\frac{r}{s}=-1,-2,-3,-6
$$
$$
\implies \begin{matrix}
p(-1)=4\ne0\\
p(-2)=4\ne0\\
p(-3)=0\therefore\text{a rational root}\\
p(-6)=-6\ne0
\end{matrix}
$$
$$
\therefore p(x)=(x+3)(x^2+x+2)\quad\text{this is a complete factorisation in }\mathbb{Q}[x].
$$
#### Question 2
Find the complex roots of the biquadratic polynomial $p(x)$, and write its complete factorisations in $\mathbb{Q}[x]$, in $\mathbb{R}[x]$, and in $\mathbb{C}[x]$, such that
$$
p(x)=3x^4-7x^2-6
$$
$$
\implies x^2=\frac{-(-7)\pm\sqrt{(-7)^2-4(3)(-6)}}{2(3)}\quad\text{using the quadratic formula}
$$
$$
\implies p(x)=\left(x^2-3\right)\left(3x^2+2\right)\quad\text{complete factorisation in }\mathbb{Q}[x].
$$
$$
\implies p(x)=(x+\sqrt{3})(x-\sqrt{3})(3x^2+2)\quad\text{complete factorisation in }\mathbb{R}[x].
$$
$$
\implies p(x)=\frac{1}{3}(x+\sqrt{3})(x-\sqrt{3})(3x+i\sqrt{6})(3x-i\sqrt{6})\quad\text{complete factorisation in }\mathbb{C}[x].
$$
#### Question 3
Consider the self-reciprocal polynomial $p(x)=6x^4-35x^3+62x^2-35x+6$.
##### Question 3(i, ii, iii)
Factorise the polynomial $p(x)$ into a product of three linear factors in $\mathbb{C}[x]$.
$$
\text{Using the rational root test, }\frac{r}{s}=\frac{\pm1,\pm2,\pm3,\pm6}{\pm1,\pm2,\pm3,\pm6}
$$
$$
\text{As it's a self-reciprocal polynomial, we may exclude reciprocals such that }\frac{r}{s}=\frac{s}{r}.
$$
$$
\text{The polarity of the coefficients are alternating, thus we may exclude any }\frac{r}{s}<0.
$$
$$
\implies\frac{r}{s}=1,2,3,6,\frac{2}{3}
$$
$$
\text{Then, testing these potential roots:}\quad
\begin{matrix}
p(1)=4\\
p(2)=0\\
p(3)=0\\
p(6)=2244\\
p(\frac{2}{3})=\frac{28}{27}
\end{matrix}
$$
$$
\implies x=2,3\text{ are valid roots}\implies x=\frac{1}{2},\frac{1}{3}\text{ are valid roots, because of the type of p(x)}
$$
$$
\therefore p(x)=(x-2)(x-3)(2x-1)(3x-1)\quad\text{this is a complete factorisation in }\mathbb{C}[x].
$$
___
**Correction in method:**
$$
6x^4-35x^3+62x^2-35x+6=0
$$
$$
\implies6\left(x^2+\frac{1}{x^2}\right)-35\left(x+\frac{1}{x}\right)+62=0
$$
$$
\implies6\left(x+\frac{1}{x}\right)^2-35\left(x+\frac{1}{x}\right)+50=0
$$
$$
\text{etc.}
$$
#### Question 4
Factorise the following polynomial into a product of linear factors with complex coefficients, then factorise it into a product of irreducible factors over $\mathbb{R}$.
$$
p(x)=x^4+(2-\sqrt{3})x^2-2\sqrt{3}
$$
$$
\implies x^2=a,b:ab=-2\sqrt{3},a+b=2-\sqrt{3}\therefore x^2=2,-\sqrt{3}
$$
$$
\implies p(x)=(x^2-2)(x^2+\sqrt{3})
$$
$$
\implies p(x)=(x-\sqrt{2})(x+\sqrt{2})(x-i\sqrt{3})(x+i\sqrt{3})
$$
