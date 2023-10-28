![[Practical_5.pdf]]

#### Question 1
$$
\frac{4x^3-3x+9}{2x^3+x^2-3x+6}
$$
First, finding the greatest common divisor of both the numerator and the denominator,
$$
(4x^3-3x+9)=(2x^3+x^2-3x+6)q(x)+r(x)
$$
$$
\implies(4x^3-3x+9)=(2x^3+x^2-3x+6)(2)-(2x^2-3x+3)
$$
$$
\implies(2x^3+x^2-3x+6)=(2x^2-3x+3)(x)+2(2x^2-3x+3)
$$
$$
\implies (2x^2-3x+3)=(2x^2-3x+3)(1)+(0)
$$
$$
\therefore \text{GCD}=2x^2-3x+3
$$
Using this to then factorise the fraction,
$$
\implies\frac{4x^3-3x+9}{2x^3+x^2-3x+6}=\frac{(2x^2-3x+3)(2x+3)}{(2x^2-3x+3)(x+2)}=\frac{2x+3}{x+2}
$$
#### Question 2
$$
(2x^2+x+3)\cdot u(x)+(x^2+1)\cdot v(x)=1
$$
First, finding the greatest common divisor of both the numerator and the denominator,
$$
(2x^2+x+3)=(x^2+1)(2)+(x+1)
$$
$$
\implies(x^2+1)=(x+1)(x-1)+2
$$
(working for that division is [here](Answers%20to%20Algebra%20Practical%205%202023-10-27%2011.20.16.excalidraw))
$$
\implies (x+1)=2(\frac{1}{2}x+\frac{1}{2})+0
$$
$$
\therefore\text{GCD}=2,\text{ or any other integer, e.g. 1}:\text{coprime}
$$
Next, using the extended Euclidean algorithm,
$$
2=(x^2+1)-(x+1)(x-1)
$$
$$
\implies2=(x^2+1)-(x-1)((2x^2+x+3)-2(x^2+1))
$$
$$
=(x^2+1)-(x-1)(2x^2+x+3)+2(x-1)(x^2+1)
$$
$$
=(x^2+1)(2x-1)+(1-x)(2x^2+x+3)
$$
$$
\therefore(2x^2+x+3)(\frac{1}{2}-\frac{1}{2}x)+(x^2+1)(x-\frac{1}{2})=1
$$
So, $u(x)=\frac{1}{2}-\frac{1}{2}x$ and $v(x)=x-\frac{1}{2}$. Note that I'm not sure if that's the end of the question, or if we need to introduce $n$.
#### Question 3
$$
(x^3+x+1)\cdot u(x)+(x^2-x-1)\cdot v(x)=1
$$
First, finding the greatest common divisor of both the numerator and the denominator,
$$
(x^3+x+1)=(x^2-x-1)(x+1)+(3x+2)
$$
(working for that division is [here](Answers%20to%20Algebra%20Practical%205%202023-10-27%2011.34.57.excalidraw))
$$
\implies(x^2-x-1)=(3x+2)(\frac{3}{9}x-\frac{5}{9})-(\frac{1}{9})
$$
(working for that division is [here](Answers%20to%20Algebra%20Practical%205%202023-10-27%2011.37.53.excalidraw))
$$
\implies9(x^2-x-1)=(3x+2)(3x-5)-(1)
$$
$$
\implies(3x+2)=(1)(3x+2)+(0)
$$
$$
\therefore\text{GCD}=1:\text{coprime}
$$
Next, using the extended Euclidean algorithm,
$$
1=9(x^2-x-1)-(3x+2)(3x-5)
$$
$$
\implies1=9(x^2-x-1)-((x^3+x+1)-(x+1)(x^2-x-1))(3x-5)
$$
$$
=9(x^2-x-1)-(3x-5)(x^3+x+1)+(3x-5)(x+1)(x^2-x-1)
$$
$$
=(9+(3x-5)(x+1))(x^2-x-1)-(3x-5)(x^3+x+1)
$$
$$
=(x^3+x+1)(5-3x)+(x^2-x-1)(3x^2-2x+4)=1
$$
$$
\therefore  u(x)=5-3x,v(x)=3x^2-2x+4
$$
#### Question 4
$$
10^6-3^6=999271
$$
$$
\implies(10^3+3^3)(10^3-3^3)=999271
$$
$$
\implies(10+3)(10^2-(10)(3)+3^2)(10-3)(10^2+(10)(3)+3^2)=999271
$$
$$
\implies (13)(79)(7)(139)=999271
$$
$$
\implies999271=79\cdot13^3\cdot7:\text{these are prime}\space\square
$$
#### Question 5
##### Question 5a
$$
f(x)=x^4+2x^3-6x^2+8x+80
$$

| (2+2i) | 1   | 2    | -6     | 8       | 80  |
| ------ | --- | ---- | ------ | ------- | --- |
|        | 0   | 2+2i | 4+12i  | -28+20i | -80 |
|        | 1   | 4+2i | -2+12i | -20+20i | 0   | 

$$
\implies f(x)=[x-(2+2i)][x^3+(4+2i)x^2+(-2+12i)x+(-20+20i)]
$$
##### Question 5b
If $z$ is a root, then $\bar{z}$ will be a root, so using Ruffini's Rule we can decompose the cubic as well:

| (2-2i) | 1   | 4+2i | -2+12i | -20+20i |
| ------ | --- | ---- | ------ | ------- |
|        | 0   | 2-2i | 12-12i | 20-20i  |
|        | 1   | 6    | 10     | 0       | 

$$
\implies f(x)=[x-(2+2i)][x-(2-2i)][x^2+6x+10]
$$
Then we can use the quadratic formula for the remaining two roots:
$$
x^2+6x+10:\frac{-b\pm\sqrt{b^2-4ac}}{2a}\implies\frac{-6\pm\sqrt{6^2-4\cdot1\cdot10}}{2}\implies-3\pm i
$$
Thus the final factorised form of $f(x)$ is:
$$
\therefore f(x)=[x-(2+2i)][x-(2-2i)][x-(-3+i)][x-(-3-i)]
$$
$$
\text{The roots are: }2+2i,2-2i,-3+i,-3-i.
$$
#### Question 6
| (1) | 1   | 0   | ... | 0   | 2   | 0   | ... | 0   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0   | 1   | 1   | 1   | 1   | 3   | 3   | 3   | 3   |
|     | 1   | 1   | 1   | 1   | 3   | 3   | 3   | 3   | 4   |

$$
(x^{100}+2x^6+1)=(x-1)(x^{100}+x^{99}+x^{98}+\cdots+x^6+3x^5+3x^4+\cdots+3x+3)+4
$$
#### Question 7
Using the following points,
$$
f(-1)=-7,\quad f(0)=-3,\quad f(1)=-3,\quad f(2)=-1
$$
we can model a unique polynomial $f(x)$:
$$
f(x)=ax^3+bx^2+cx+d
$$
$$
\implies-7=-a+b-c+d,\quad -3=d,\quad -3=a+b+c+d\quad -1=8a+4b+2c+d
$$
$$
\implies-4=-a+b-c,\quad 6=a+b+c\quad 2=8a+4b+2c
$$
$$
\implies
\begin{bmatrix}
-1&1&-1\\
1&1&1\\
8&4&2
\end{bmatrix}
\begin{bmatrix}
a\\
b\\
c
\end{bmatrix}
=
\begin{bmatrix}
-4\\
6\\
2
\end{bmatrix}
$$
$$
\implies
\begin{bmatrix}
a\\
b\\
c
\end{bmatrix}
=
\begin{bmatrix}
-1&1&-1\\
1&1&1\\
8&4&2
\end{bmatrix}^{-1}
\begin{bmatrix}
-4\\
6\\
2
\end{bmatrix}
$$
$$
\implies
\begin{bmatrix}
a\\
b\\
c
\end{bmatrix}
=
\begin{bmatrix}
-2\\
1\\
7
\end{bmatrix}
$$
$$
\therefore f(x)=-2x^3+x^2+7x-3
$$
#### Question 8
$$
f(x)=a_nx^n+\cdots+a_1x+a_0
$$
##### Question 8a
Considering the sum of only the even order coefficients,
$$
S_{even}=a_n+a_{n-2}+a_{n-4}+\cdots+a_4+a_2+a_0
$$
We can then consider the behaviour of $f(x)$ at $x=\pm1$,
$$
f(1)=a_n+a_{n-1}+a_{n-2}+\cdots+a_2+a_1+a_0
$$
$$
f(-1)=a_n-a_{n-1}+a_{n-2}-\cdots+a_2-a_1+a_0
$$
where we see that $f(1)$ is the sum of all coefficients, and $f(-1)$ is an alternating sequence of adding and subtracting the coefficients - adding the even terms, subtracting the odd.

Thus, if we find the sum of the two sequences, we'll end with $2S_{even}$, where $_{even}S$ was defined earlier:
$$
f(1)+f(-1)=2a_n+2a_{n-2}+2a_{n-4}+\cdots+2a_4+2a_2+2a_0=2S_{even}
$$
$$
\implies S_{even}=\frac{1}{2}(f(1)+f(-1))\space\square
$$
##### Question 8b
Considering the sum of only the odd order coefficients,
$$
S_{odd}=a_{n-1}+a_{n-3}+a_{n-5}+\cdots+a_3+a_1
$$
We can then consider the behaviour of $f(x)$ at $x=\pm1$,
$$
f(1)=a_n+a_{n-1}+a_{n-2}+\cdots+a_2+a_1+a_0
$$
$$
f(-1)=a_n-a_{n-1}+a_{n-2}-\cdots+a_2-a_1+a_0
$$
where we see that $f(1)$ is the sum of all coefficients, and $f(-1)$ is an alternating sequence of adding and subtracting the coefficients - adding the even terms, subtracting the odd.

Thus, if we find the difference of the two sequences, we'll end with $2S_{odd}$, where $S_{odd}$ was defined earlier:
$$
f(1)-f(-1)=2a_{n-1}+2a_{n-3}+2a_{n-5}+\cdots+2a_5+2a_3+2a_1=2S_{odd}
$$
$$
\implies S_{odd}=\frac{1}{2}(f(1)-f(-1))\space\square
$$
#### Question 9
If we want to find the sum of the coefficients of a polynomial, we can substitute $x=1$ and have that returned to us - this is irrelevant of what form it is in.

So, if we consider the polynomial
$$
p(x)=(2x-1)(3x^2-2)(4x^3-3)(5x^4-4)(6x^5-5)
$$
then the sum of its coefficients would be
$$
p(1)=(1)(1)(1)(1)(1)=1\space\square
$$
*Note that I initially tried to solve this using sequences and combinations, which may have eventually worked, but then I realised I could just do this.*
