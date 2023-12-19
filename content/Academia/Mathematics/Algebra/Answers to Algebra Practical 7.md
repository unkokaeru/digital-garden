[[Practical_8.pdf]]

#### Question 1
Find all complex solutions of the following symmetric system:
$$
\begin{matrix}
x^3+y^3=37\\
x+y=3\\
\end{matrix}
$$
$$
:(x+y)^3=x^3+3x^2y+3xy^2+y^3
$$
$$
(x+y)^3=x^3+y^3+3xy(x+y)
$$
$$
-\frac{10}{9}=xy\quad\text{after substituting in the system}
$$
$$
\begin{matrix}
xy=-\frac{10}{9}\\
x+y=3\\
\end{matrix}
$$
$$
\text{Solving this, }x\cdot\left(3-x\right)=-\frac{10}{9}
$$
$$
x^2-3x-\frac{10}{9}=0
$$
$$
9x^2-27x-10=0:x=\frac{27\pm33}{18}
$$
$$
x=-\frac{1}{3},\frac{10}{3}
$$
$$
\therefore\begin{matrix}
x=-\frac{1}{3},y=\frac{10}{3}\\
\text{OR}\\
x=\frac{10}{3},y=-\frac{1}{3}\\
\end{matrix}
$$
#### Question 2
Find a polynomial $g(y)$ such that
$$
g\left(1+\frac{1}{x}\right)=x^3+\frac{1}{x^3}
$$
$$
\left(x+\frac{1}{x}\right)^3=x^3+\frac{1}{x^3}+3\left(x+\frac{1}{x}\right)
$$
$$
g\left(1+\frac{1}{x}\right)=\left(x+\frac{1}{x}\right)^3-3\left(x+\frac{1}{x}\right)
$$
$$
\therefore g(z)=z^3-3z:z=x+\frac{1}{x}
$$
#### Question 3
Let $\alpha$ and $\beta$ be the complex roots of the polynomial $x^2+x+2$. Without computing $\alpha$ and $\beta$ separately, compute $\alpha^2+\beta^2$, $\alpha^3+\beta^3$ and $\alpha^4+\beta^4$.
$$
\begin{matrix}
\alpha+\beta=-1\\
\alpha\beta=2\\
\end{matrix}
$$
$$
:(\alpha+\beta)^4=\beta^4+4\alpha\beta^3+8\alpha^2\beta^2+4\alpha^3\beta+\alpha^4
$$
$$
1=(\alpha^4+\beta^4)+4\alpha\beta(\alpha^2+\beta^2+2\alpha\beta)
$$
$$
:(\alpha+\beta)^2-2\alpha\beta=\alpha^2+\beta^2
$$
$$
1=(\alpha^4+\beta^4)+4\alpha\beta(((\alpha+\beta)^2-2\alpha\beta)+2\alpha\beta)
$$
$$
\alpha^4+\beta^4=1-4\cdot2\cdot(((-1)^2-2\cdot2)+2\cdot2)
$$
$$
\alpha^4+\beta^4=-7
$$
$$
\alpha^3+\beta^3=5\text{ from previous questions}
$$
$$
\alpha^2+\beta^2=-3
$$
#### Question 4
Let $\alpha,\beta,\gamma$ be the complex roots of the polynomial $2x^3-4x-6$. Find a polynomial of degree three, with integer coefficients, having roots $\frac{1}{\alpha},\frac{1}{\beta},\frac{1}{\gamma}$.
$$
q(x)=-6x^3-4x^2+2\text{ by reading the coefficients in reverse}
$$
---
**Alternative Method**
$$
q(x)=x^3+p\left(\frac{1}{x}\right)
$$
$$
q(x)=x^3+\left(\frac{2}{x^3}-\frac{4}{x}-6\right)
$$
$$
q(x)=-6x^3-4x^2+2
$$
#### Question 5
Let $\alpha, \beta, \gamma$ be the complex roots of the polynomial $x^3+2x^2-x+3$. Compute $\alpha^2+\beta^2+\gamma^2$ and $\alpha^{-1},\beta^{-1},\gamma^{-1}$.
$$
\begin{matrix}
\alpha+\beta+\gamma=-2\\
\alpha\beta+\alpha\gamma+\beta\gamma=-1\\
\alpha\beta\gamma=-3\\
\end{matrix}
$$
$$
\alpha^2+\beta^2+\gamma^2=(\alpha+\beta+\gamma)^2-2(\alpha\beta+\alpha\gamma+\beta\gamma)=6
$$
$$
\frac{1}{\alpha}+\frac{1}{\beta}+\frac{1}{\gamma}=\frac{\alpha\beta+\alpha\gamma+\beta\gamma}{\alpha\beta\gamma}=\frac{1}{3}
$$
