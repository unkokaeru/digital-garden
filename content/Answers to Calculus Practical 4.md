![[MTH1002_Calculus_Practical_4.pdf]]

#### Question 1
##### Question 1a
$$
\lim_{x\to0}\frac{x^2+2x+1}{x+1}=1
$$
##### Question 1b
$$
\lim_{x\to2}\frac{x^2-5x+6}{x^2-4}:\text{undefined at x=2, so use L'Hôpital's Rule}
$$
$$
\implies\lim_{x\to2}\frac{2x-5}{2x}=-\frac{1}{4}
$$
#### Question 2
##### Question 2a
$$
\lim_{x\to0}(x\cos x)=0
$$
##### Question 2b
$$
\lim_{x\to0}\frac{\sin x}{e^{2x}-e^{-2x}}:\text{undefined at x=0, so use L'Hôpital's Rule}
$$
$$
\implies\lim_{x\to0}\frac{\cos x}{2e^{2x}+2e^{-2x}}=\frac{1}{4}
$$
##### Question 2c
$$
\lim_{x\to0}\frac{1-\cos2x}{xe^x-x}:\text{undefined at x=0, so use L'Hôpital's Rule}
$$
$$
\implies\lim_{x\to0}\frac{2\sin2x}{e^x+xe^x-1}:\text{undefined at x=0, so use L'Hôpital's Rule}
$$
$$
\implies\lim_{x\to0}\frac{4\cos2x}{2e^x+xe^x}=2
$$
##### Question 2d
$$
\lim_{y\to0}\frac{\tan y}{\tan ay}, \text{ where }a\text{ is a non-zero constant}:\text{undefined at y=0, so use L'Hôpital's Rule}
$$
$$
\lim_{y\to0}\frac{\sec^2y}{a\sec^2ay}=\frac{1}{a}
$$
##### Question 2e
$$
\lim_{t\to5}\frac{2-\sqrt{t-1}}{t^2-25}\text{undefined at t=5, so use L'Hôpital's Rule}
$$
$$
\lim_{t\to5}\frac{-\frac{1}{2}(t-1)^{-\frac{1}{2}}}{2t}=-\frac{1}{40}
$$
#### Question 3
##### Question 3a
$$
\lim_{x\to\infty}\frac{x^4-2x^3+3x^2+5}{4x^4-1}=\frac{1}{4}\text{, by evaluating the ratio between the highest order }x
$$
##### Question 3b
$$
\lim_{v\to\infty}\frac{5v^9-4v^5+3v-21}{-2v^9+v^8-4v^2+3v}=-\frac{5}{2}\text{, by evaluating the ratio between the highest order }v
$$
##### Question 3c
$$
\lim_{u\to\infty}\frac{u^3-3u^2+5}{u^4+5u^3+1}=0\text{, by evaluating the ratio between the highest order }u
$$
#### Question 4
##### Question 4a
$$
f(x)=x\sin\left(\frac{1}{x}\right):\text{continuous for the interval }(-\infty,0)\cup(0,\infty)\text{, as shown below.}
$$
As $x$ approaches $0$, the function oscillates infinitely, making it hard to predict its behaviour at $x=0$, thus it's an oscillating discontinuity.

However, the $x$ multiplying the sine function ensures that it is equal to 0 ($0\cdot a=0$, even if $a$ is undefined). So it is *continuous for all real values of $x$.*

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-1,1,-1,1]
disableZoom: false
grid: true
---
f(x)=x*sin(1/x)
```
##### Question 4b
$$
F(x)=\frac{x^2-3x+2}{x-2}:\text{continuous for the interval }(-\infty,2)\cup(2,\infty)\text{, as shown below.}
$$
$$
F(2)=\frac{2^2-3\cdot2+2}{2-2}=\text{undefined}
$$
However, if we simplify the function by factorising $x^2-3x+2\implies(x-2)(x-1)$, then function simplifies to just $x-1$. Thus, it's a *removable discontinuity*.
```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
f(x)=(x^2-(3*x)+2)/(x-2)
```
##### Question 4c
$$g(x)=\tan x$$
The tangent function is continuous everywhere except where its denominator, $\cos x$, is zero. This occurs at odd multiples of $\frac{\pi}{2}$. Therefore, $g(x)$ is continuous for all $x$ except at $x = (2n + 1)\frac{\pi}{2}$ where $n$ is any integer.
*I wasn't sure how to write this in interval notation.*

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
g(x)=tan(x)
```

##### Question 4d
$$
G(x) = \cos(x^3 + 2x^2 + 3):\text{continuous for the interval }(-\infty,\infty)\text{, as shown below.}
$$
The cosine function is continuous everywhere. Since the polynomial inside the cosine function is also continuous everywhere, $G(x)$ is *continuous for all real values of $x$.*

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
G(x)=cos(x^3+2x^2+3)
```

##### Question 4e
$$
h(x) = x^{500} - 2x^6 + 80
$$
This is a polynomial, and polynomials are continuous everywhere. Therefore, $h(x)$ is *continuous for all real values of $x$.*

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-5,5,70,100]
disableZoom: false
grid: true
---
h(x)=x^500-2x^6+80
```

##### Question 4f
$$
H(x) = \frac{x^2 + 2x + 3}{x^2 - 1}:\text{continuous for the interval }(-\infty,-1)\cup(-1,1)\cup(1,\infty)\text{, as shown below.}
$$
This is a rational function. Rational functions are continuous wherever their denominator is not zero. In this case, the denominator $x^2 - 1$ is zero when $x = 1$ and $x = -1$. Therefore, $H(x)$ is *continuous for all $x$ except at $x = 1$ and $x = -1$.*

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
H(x)=(x^2+2x+3)/(x^2-1)
```
#### Question 5
$$
g(x)=\lim_{x\to\infty}\frac{\sin x}{x}
$$
The Squeeze Theorem dictates that:
*If $f(x) \leq g(x) \leq h(x)$ for all $x$ in some open interval containing $a$ (except possibly at $a$), and: $\lim_{x \to a} f(x) = \lim_{x \to a} h(x) = L$, then: $\lim_{x \to a} g(x) = L$.*

Thus, if we find $f(x)$ and $h(x)$ as defined, we can find the limit of $g(x)$.

We know that $\sin x$ is defined as $-1\le\sin x\le 1$, so if we divide through by $x$ then:
$$
-\frac{1}{x}\le\frac{\sin x}{x}\le\frac{1}{x}\implies f(x)\le g(x)\le h(x)
$$
Thus the limit of $g(x)$ is the same as the limit of $h(x)$:
$$
\lim_{x\to\infty}h(x)=\lim_{x\to\infty}\frac{1}{x}=0
$$
$$
\implies \lim_{x\to\infty}\frac{\sin x}{x}=0\text{ by Squeeze Theorem}\space\blacksquare
$$
#### Question 6
##### Question 6a
$$
\lim_{x\to0}\left(\frac{1}{\sin x}-\frac{1}{x}\right)=\lim_{x\to0}\left(\frac{1}{\sin x}\right)-\lim_{x\to0}\left(\frac{1}{x}\right)=\infty-\infty=0
$$
*I know this is incorrect notation, but I don't know the correct version.*
##### Question 6b
$$
\lim_{\theta\to\frac{\pi}{2}}(\sec\theta-\tan\theta)=\lim_{\theta\to\frac{\pi}{2}}(\sec\theta)-\lim_{\theta\to\frac{\pi}{2}}(\tan\theta)=\frac{1}{\lim_{\theta\to\frac{\pi}{2}}(\cos\theta)}-\frac{\lim_{\theta\to\frac{\pi}{2}}(\sin\theta)}{\lim_{\theta\to\frac{\pi}{2}}(\cos\theta)}
$$
$$
=\frac{1}{\lim_{\theta\to\frac{\pi}{2}}(\cos\theta)}-\frac{1}{\lim_{\theta\to\frac{\pi}{2}}(\cos\theta)}=0
$$
##### Question 6c
$$
\lim_{h\to0}\frac{\sqrt[5]{32+h}-2}{h}=\lim_{h\to0}\frac{\sqrt[5]{32+h}-\sqrt[5]{32}}{h}:f'(x) = \lim_{{h \to 0}} \frac{f(x + h) - f(x)}{h}
$$
Thus, evaluation of the limit is equal to differentiating the function $f(x)=\sqrt[5]{x}=x^\frac{1}{5}$ at the point $x=32$:
$$
f^\prime(x)=\frac{1}{5}x^{-\frac{4}{5}}\implies f^\prime(32)=\frac{1}{5}\cdot\frac{1}{2^4}=\frac{1}{80}
$$