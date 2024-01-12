#### Question 1

##### Question 1ai

$$
\int^{\frac{\pi}{2}}_{0}\sin^{3}(x)\cos(x)dx
$$

Using the substitution $u=\sin x$, we get $dx=\frac{du}{\cos x}$, thus the expression becomes...

$$
\int^{1}_{0}u^{3}du=\left[\frac{1}{4}u^{4}\right]_{0}^{1}=\frac{1}{4}-0=\frac{1}{4}
$$

##### Question 1aii

$$
\int^{\frac{\pi}{2}}_{0}\cos^{2}(x)dx
$$

If we use the identity $\cos2\theta\equiv2\cos^{2}\theta-1$, rearranged to be $\cos^2\theta\equiv\frac{1+\cos2\theta}{2}$, then we can get the expression...

$$
\int^{\frac{\pi}{2}}_{0} \frac{1}{2}+ \frac{1}{2}\cos(2\theta) dx=\left[\frac{1}{2}x+ \frac{1}{4}\sin(2\theta)\right]_{0}^{\frac{\pi}{2}}=\frac{\pi}{4}-0=\frac{\pi}{4}
$$

##### Question 1bi

$$
\begin{align*}
\int_{0}^{3}\int_{1}^{2}x^{2}y^{2}dxdy&=\int_{0}^{3}\left[\frac{1}{3}x^{3}y^{2}\right]_{1}^{2}dy\\
&=\int_{0}^{3} \left(\frac{8}{3}y^{2}- \frac{1}{3}y^{2}\right)dy\\
&=\int_{0}^{3} \frac{7}{3}y^{2}dy\\
&=\left[\frac{7}{9}y^{3}\right]_{0}^{3}\\
&=\frac{27\cdot7}{9}-0\\
&=21
\end{align*}
$$

##### Question 1bii

$$
\begin{align*}
\int_{0}^{1}\int_{x}^{\sqrt{x}}ydydx&=\int_{0}^{1}\left[\frac{1}{2}y^{2}\right]_{x}^{\sqrt{x}}dx\\
&= \int_{0}^{1}\left(\frac{1}{2}x- \frac{1}{2}x^{2}\right)dx\\
&= \frac{1}{2} - \frac{1}{2}-0 -0\\
&= 0
\end{align*}
$$

##### Question 1c

$$
f(x,y)=x^4-x^2+y^2
$$

First, finding the partial derivatives in terms of $x$ and $y$...

$$
\frac{\delta f}{\delta x}=4x^{3}-2x,\quad\frac{\delta f}{\delta y}=2y
$$

These are both equal to 0 when the function is stationary, therefore we have the system of simultaneous equations:

$$
\begin{cases}
x(4x^{2}-2)=0 \\
2y=0
\end{cases}
$$

Therefore, the stationary points are $(0,0)$, $(\frac{1}{2},0)$, and $(-\frac{1}{2},0)$.

To now determine the nature of these points, we'll calculate the second partial derivatives and then calculate $D$:

$$
D = \left( \frac{\partial^2 f}{\partial x^2} \right)\left( \frac{\partial^2 f}{\partial y^2} \right) - \left( \frac{\partial^2 f}{\partial x \partial y} \right)^2
$$

These second partial derivatives are as follows:

$$
\frac{\partial^2 f}{\partial x^{2}}=12x^{2}-2,\quad\frac{\partial^2 f}{\partial y^2}=2,\quad\frac{\partial^2 f}{\partial x\partial y}=0
$$

$$
\begin{align*}
D &= \left( \frac{\partial^2 f}{\partial x^2} \right)\left( \frac{\partial^2 f}{\partial y^2} \right) - \left( \frac{\partial^2 f}{\partial x \partial y} \right)^2\\
&= (12x^{2}-2)(2)-(0)\\
&= 24x^{2}-4
\end{align*}
$$

Using this determinant $D$, we can find the nature of the points based on the following:

   - If $D > 0$ and $\frac{\partial^2 f}{\partial x^2} > 0$, then $(x_0, y_0)$ is a local minimum.
   - If $D > 0$ and $\frac{\partial^2 f}{\partial x^2} < 0$, then $(x_0, y_0)$ is a local maximum.
   - If $D < 0$, then $(x_0, y_0)$ is a saddle point.
   - If $D = 0$, the test is inconclusive.

Hence,

$$
\begin{matrix}\text{Saddle point:}&(0,0) \\ \text{Local minima:}&\left(\frac{1}{2},0\right),\left(- \frac{1}{2},0\right)\end{matrix}
$$

#### Question 2

##### Question 2ai

Given the parametric curve where $x=t^{2}-1$ and $y=t^{3}-3t$,

$$
\frac{dx}{dt}=2t,\quad \frac{dy}{dt}=3t^{2}-3
$$
$$
\frac{dy}{dx}= \frac{dy}{dt}\cdot\left(\frac{dx}{dt}\right)^{-1} =\frac{3t^{2}-3}{2t}
$$

If we repeat the process once more, then...

$$
\frac{d^{2}x}{dt^{2}}=2,\quad \frac{d^{2}y}{dt^{2}}=6t
$$
$$
\frac{d^{2}y}{dx^{2}}=\frac{d^{2}y}{dt^{2}}\cdot\left(\frac{d^{2}x}{dt^{2}}\right)^{-1}=\frac{6t}{2}=3t
$$

##### Question 2aii

Converting the polar equation $r=4\cos\theta$ to Cartesian then becomes...

$$
r^{2}=4r\cos\theta\iff x^2+y^2=4x\iff x^2-4x+y^2=0
$$
$$
(x-2)^{2}+y^{2}=2^{2}
$$

Hence the centre of circle is $(2,0)$ with radius $2$.

##### Question 2b

Finding the first four terms in the Taylor series of $\sqrt{x}$ about $x=1$,

Using the formula,

$$
f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \frac{f'''(a)}{3!}(x - a)^3 + \cdots
$$

We get the result:

$$
f(x)=1+ \frac{1}{2}x^{-\frac{1}{2}} (x-1) - \frac{1}{4}x^{-\frac{3}{2}}(x-1)^{2}+ \frac{3}{8}x^{- \frac{5}{2}}(x-1)^{3} - \cdots
$$

##### Question 2c

To calculate the volume under a surface $z=xy$ and above the region in the $xy$ plane bounded $y=x^{2}$ and $y=\sqrt{2-x^{2}}$ on the interval $0\le x\le 1$.

Formulating this into a mathematical expression...

$$
\begin{align*}
V&=\int_{0}^{1}\int^\sqrt{2-x^{2}}_{x^{2}} (xy)  dydx\\
&= \int_{0}^{1}\left[\frac{1}{2}xy^{2}\right]_{x^{2}}^\sqrt{2-x^{2}}dx\\
&= \int_{0}^{1}\left(\frac{1}{2}x(2-x^{2}) - \frac{1}{2}x^{5}\right)dx\\
&= \int_{0}^{1}x- \frac{1}{2}x^{3}- \frac{1}{2}x^{5}dx\\
&= \left[\frac{1}{2}x^{2}- \frac{1}{8}x^{4}- \frac{1}{12}x^{6}\right]_{0}^{1}\\
&= \frac{1}{2}- \frac{1}{8}- \frac{1}{12}\\
&= \frac{12}{24}- \frac{3}{24} - \frac{2}{24}\\
&= \frac{7}{24}
\end{align*}
$$

#### Question 3

##### Question 3ai

$$
\begin{align*}
(1-i)(1+i)&=1^{2}-i^{2}\\
&= 1+1\\
&= 2 +0i
\end{align*}
$$

##### Question 3aii

$$
\begin{align*}
\frac{1-i}{1+i}&=\frac{1-i}{1+i}\cdot \frac{1-i}{1-i}\\
&= \frac{(1-i)^{2}}{2}\\
&= \frac{1^{2}-i^{2}-2i}{2}\\
&= 1-i
\end{align*}
$$

##### Question 3aiii

$$
\begin{align*}
\left(\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}i\right)^{20}&=\left(\cos\frac{\pi}{4}+i\sin\frac{\pi}{4}\right)^{20}\\
&= \cos5\pi+i\sin5\pi\\
&= -1 + 0i\\
\end{align*}
$$

##### Question 3b

$$
x^{2}z+y^{2}z+2xy^{2}-z^{3}=0
$$

We can use this to calculate the two partial derivatives, $\frac{\partial z}{\partial x}$ and $\frac{\partial z}{\partial y}$.

$$
2x\frac{\partial z}{\partial x}+y^{2}\frac{\partial z}{\partial x}+2y^{2}-3z^{2}\frac{\partial z}{\partial x}=0\iff\frac{\partial z}{\partial x}=-\frac{2y^{2}}{2x+y^{2}-3z^{2}}
$$

$$
x^{2}\frac{\partial z}{\partial y}+2y\frac{\partial z}{\partial y}4xy-3z^{2}\frac{\partial z}{\partial y}=0\iff\frac{\partial z}{\partial y}=\frac{1}{x^{2}+2y-3z^{2}}
$$

##### Question 3c

$$
\begin{align*}
z^{4}&=\frac{\sqrt{3}}{2} + \frac{1}{2}i\\
&= \cos\frac{\pi}{6}+i\sin\frac{\pi}{6}
\end{align*}
$$

$$
\begin{align*}
\iff z&= \exp\left(\frac{\pi}{6}+2n\pi\right)^{\frac{1}{4}}\\
&= \exp\left(\frac{\frac{\pi}{6}+2n\pi}{4}\right)\\
&= e^{\frac{\pi}{24}},e^{\frac{13\pi}{24}},e^{\frac{25\pi}{24}},e^{\frac{37\pi}{24}}
\end{align*}
$$

#### Question 4

##### Question 4a

$$
f(t)=t\ln t-t\iff f^{\prime}(t)=\ln t
$$
$$
g(t)=-\frac{t}{\sqrt{2\pi}}\exp\left(-\frac{t^{2}}{2}\right)\iff g^{\prime}(t)=\frac{t^{2}}{\sqrt{2}\pi}\exp\left(-\frac{t^{2}}{2}\right)
$$
$$
\begin{align*}
h(t)=\frac{t-1}{t^{2}+1}\iff h^{\prime}(t)&=\frac{(1)(t^{2}+1)-(t-1)(2t)}{t^{2}+1}\\
&= \frac{-t^{2}+2t+1}{t^{2}+1}
\end{align*}
$$

##### Question 4b

$$
\begin{align*}
\lim_{u\to3} \frac{u^{2}-u-6}{u-3}&=\lim_{u\to3}\frac{2u-1}{1}\\
&= 5\text{ by L'Hoptial's Rule}
\end{align*}
$$

$$
\begin{align*}
\lim_{x\to0}\frac{x}{\ln(x+1)}&=\frac{x}{\frac{1}{x+1}}\\
&= 0
\end{align*}
$$

##### Question 4c

$$
f(x)=x^{2}+ \frac{2}{x}
$$

###### Question 4ci

To find the vertical asymptote of the function, $f(x)$, we must evaluate where the function tends to infinity: this is at $x=0$.

###### Question 4cii

To find the local extremum of the function, we must first find its derivative and solve it when equal to zero,

$$
f^{\prime}(x)=2x - \frac{2}{x^{2}}:f^{\prime}(x)=0\iff x=1 \iff y=3
$$

To find the nature of this point, we'll evaluate the second derivative at that point,

$$
f^{\prime\prime}(x)=2 + \frac{4}{x^{3}}:f^{\prime\prime}(1)=6>0\therefore\text{local minimum at }(1,3)
$$

###### Question 4ciii

The function is increasing when the first derivative is greater than zero, and is decreasing when the first derivative is less than zero, hence...

$$
f^{\prime}(x)=2x - \frac{2}{x^{2}}:\begin{cases}
f^{\prime}(x)<0\iff x<1 \\
f^{\prime}(x)>0\iff x>1
\end{cases}
$$

Therefore, the function is decreasing on $x<0$ and $0<x<1$, and increasing $x>1$.