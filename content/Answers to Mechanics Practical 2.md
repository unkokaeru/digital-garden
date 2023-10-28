![[Practical2.pdf]]

#### Question 1
##### Question 1a
$$
\text{LHS=}\sqrt{x^2+y^2},\text{RHS}=2\text{m}
$$
$$
\implies\text{LHS=}[L]^2+[L^2],\text{RHS}=[L]^2
$$
$$
\implies\text{LHS}=\text{RHS}\therefore\text{complete equation}
$$
##### Question 1b
$$
\text{LHS}=\frac{v_x^2}{y},\text{RHS}=(65\text{km}\cdot\text{h}^{-3})t
$$
$$
\implies \text{LHS=}[L]^2[T]^{-2}[L]^{-1},\text{RHS}=[L][T]^{-3}[T]
$$
$$\implies\text{LHS}=\text{RHS}\therefore\text{complete equation}
$$

##### Question 1c
$$
\text{LHS}=y^{-\frac{1}{2}}\sqrt{v^3_x},\text{RHS}=(12\text{cm})t^{\frac{3}{2}}
$$
$$
\implies LHS=[L][L]^3[T]^{-3},RHS=[L][T]^3
$$
$$
\implies\text{LHS}\ne\text{RHS}\therefore\text{incomplete equation}
$$
##### Question 1d
$$
\text{LHS}=\frac{\sqrt{v^2_x}}{v_y},\text{RHS}=3
$$
$$
\implies\text{LHS}=[L][T]^{-1}[L]^{-1}[T],\text{RHS}=0
$$
$$
\implies\text{LHS}=\text{RHS}\therefore\text{complete equation}
$$
##### Question 1e
$$
LHS=1\text{ light year},\text{RHS}=(1.17\text{ rad})x
$$
$$
\implies\text{LHS}=[L],\text{RHS}=[L]
$$
$$
\implies\text{LHS}=\text{RHS}\therefore\text{complete equation}
$$
##### Question 1f
$$
\text{LHS}=\theta^2v_x^2,\text{RHS}=\frac{y^2}{t^2}
$$
$$
\implies\text{LHS}=[L]^2[T]^{-2},\text{RHS}=[L]^2[T]^{-2}
$$
$$
\implies\text{LHS}=\text{RHS}\therefore\text{complete equation}
$$
#### Question 2
Given that $v_x(t=0)=0$ and $x(t=0)=0$,
##### Question 2a
$$
a_x(t)=a_0
$$
$$
\implies v_x(t)=\int a_x(t)dt=a_0t+c_1:c_1=0\implies v_x(t)=a_0t
$$
$$
\implies x(t)=\int v_x(t)dt=\frac{1}{2}a_0t^2+c_2:c_2=0\implies x(t)=\frac{1}{2}a_0t^2
$$
$$
\therefore\text{the acceleration is constant, so it probably describes freefall or something similar.}
$$

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: false
---
y=2
```

##### Question 2b
$$
a_x(t)=\gamma t
$$
$$
\implies v_x(t)=\int a_x(t)dt=\frac{1}{2}\gamma t^2+c_1:c_1=0\implies v_x(t)=\frac{1}{2}\gamma t^2
$$
$$
\implies x(t)=\int v_x(t)dt=\frac{1}{6}\gamma t^3+c_2:c_2=0\implies x(t)=\frac{1}{6}\gamma t^3
$$
$$
\therefore\text{the acceleration is linearly increasing, but I don't know what this means.}
$$

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: false
---
y=2x
```

##### Question 2c (integrated incorrectly, tau should be multiplied because it's dividing a quotient)
$$
a_x(t)=\frac{v_\infty}{\tau}e^{-\frac{t}{\tau}}
$$
$$
\implies v_x(t)=\int a_x(t)dt=-\frac{v_\infty}{\tau^2}e^{-\frac{t}{\tau}}+c_1:c_1=\frac{v_\infty}{\tau}\implies v_x(t)=\frac{v_\infty}{\tau}-\frac{v_\infty}{\tau}e^{-\frac{t}{\tau}}
$$
$$
\implies x(t)=\int v_x(t)dt=\frac{v_\infty}{\tau}t+\frac{v_\infty}{\tau^2}e^{-\frac{t}{\tau}}+c_2:c_2=-\frac{v_\infty}{\tau}
$$
$$
\implies x(t)=\frac{v_\infty}{\tau}t+\frac{v_\infty}{\tau^2}e^{-\frac{t}{\tau}}-\frac{v_\infty}{\tau}
$$
$$
\therefore\text{I have no idea what physical conditions this could be under.}
$$
##### Question 2d
*Note that this follows a different, safer method*
$$
a_x(t)=a_0\cos(\omega t)
$$
$$
\implies v_x(t)=v_x(0)+\int_0^t a_x(t^\prime)dt^\prime=\left[\frac{a_0}{\omega}\sin(\omega t^\prime)\right]_0^t=\frac{a_0}{\omega}\sin(\omega t)
$$
$$
\implies x(t)=x(0)+\int_0^t v_x(t)dt=\left[-\frac{a_0}{\omega^2}\cos(\omega t^\prime)\right]^t_0=\frac{a_0}{\omega^2}-\frac{a_0}{\omega^2}\cos(\omega t)
$$
$$
\therefore\text{I have no idea what physical conditions this could be under.}
$$
#### Question 3
##### Question 3a
$$
\vec{r}(t)=\left[(10\text{m}\cdot\text{s}^{-1})t\right]\hat{\textbf{i}}+\left[(-2.5\text{m}\cdot\text{s}^{-2})t^2\right]\hat{\textbf{j}}
$$
$$
\implies\vec{v}(t)=\left[10\text{m}\cdot\text{s}^{-2}\right]\hat{\textbf{i}}+\left[(-5\text{m}\cdot\text{s}^{-3})t\right]\hat{\textbf{j}}
$$
$$
\implies\vec{a}(t)=\left[0\text{m}\cdot\text{s}^{-3}\right]\hat{\textbf{i}}+\left[-5\text{m}\cdot\text{s}^{-4}\right]\hat{\textbf{j}}
$$
##### Question 3b
$$
\vec{r}(t)=\left[R\cos(\omega t)\right]\hat{\textbf{i}}+\left[R\sin(\omega t)\right]\hat{\textbf{j}}
$$
$$
\implies\vec{v}(t)=\left[-R\omega\sin(\omega t)\right]\hat{\textbf{i}}+\left[R\omega\cos(\omega t)\right]\hat{\textbf{j}}
$$
$$
\implies\vec{a}(t)=\left[-R\omega^2\cos(\omega t)\right]\hat{\textbf{i}}+\left[-R\omega^2\sin(\omega t)\right]\hat{\textbf{j}}
$$
##### Question 3c
$$
\vec{r}(t)=\left[R(\omega t-\sin(\omega t))\right]\hat{\textbf{i}}+\left[R(\omega t-\cos(\omega t))\right]\hat{\textbf{j}}
$$
$$
\implies\vec{v}(t)=\left[R(\omega-\omega\cos(\omega t))\right]\hat{\textbf{i}}+\left[R(\omega+\omega\sin(\omega t))\right]\hat{\textbf{j}}
$$
$$
\implies\vec{a}(t)=\left[\omega^2R\sin(\omega t)\right]\hat{\textbf{i}}+\left[\omega^2R\cos(\omega t)\right]\hat{\textbf{j}}
$$
#### Question 4
##### Question 4a
$$
v_{avg} = \frac{\Delta s}{\Delta t} = \frac{s_f - s_i}{t_f - t_i} 
$$
##### Question 4b
Given the aforementioned definition that $v_{avg} = \frac{\Delta s}{\Delta t}$, we can say that:
$$
v_{x,avg}=\frac{x_2-x_1}{t_2-t_1}
$$
$$
\implies v_{x,avg}=\frac{1}{t_2-t_1}\cdot x_{avg}
$$
$$
\implies v_{x,avg}=\frac{1}{t_2-t_1}\cdot\int_{t_1}^{t_2}v_x(t)dt
$$
##### Question 4c
Given that acceleration is constant, we can say that
$$
v_x(t)=v_{x0}+a(t-t_0)
$$
Thus we can calculate the velocity at $t_1$ and $t_2$:
$$
(1)\quad v_x(t_1)=v_{x0}+a(t_1-t_0)
$$
$$
(2)\quad v_x(t_2)=v_{x0}+a(t_2-t_0)
$$
Now, integrating $v_x(t)$ over $[t_1,t_2]$:
$$
\int_{t_1}^{t^2}v_x(t)dt=\int_{t_1}^{t^2}\left(v_{x0}+a(t-t_0)\right)dt
$$
$$
\implies \int_{t_1}^{t^2}v_x(t)dt=v_{x0}(t_2-t_1)+\frac{1}{2}a((t_2-t_0)^2-(t_1-t_0)^2)
$$
Then we can simplify the equation by using the equations $(1),(2)$ from earlier:
$$
\implies \int_{t_1}^{t^2}v_x(t)dt=\frac{1}{2}(v_x(t_1)+v_x(t_2))(t_2-t_1)
$$
$$
\implies \frac{1}{t_2-t_1}\int_{t_1}^{t^2}v_x(t)dt=\frac{1}{2}(v_x(t_1)+v_x(t_2))
$$
Then by using the equation derived in part (b):
$$
\implies v_{x,avg}=\frac{1}{2}(v_x(t_1)+v_x(t_2))\space\square
$$
