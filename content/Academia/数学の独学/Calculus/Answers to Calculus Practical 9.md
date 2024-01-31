#### 9.1
Using integration by substitution,
##### 9.1a
$$
\int2x\sqrt{1+x^2}dx:u=1+x^2\implies \frac{du}{2x}=dx
$$
$$
=\int2x\sqrt{u}\frac{du}{2x}=\int\sqrt{u}=\frac{2}{3}u^\frac{3}{2}+C
$$
$$
\therefore\int2x\sqrt{1+x^2}dx=\frac{2}{3}(1+x^2)^\frac{3}{2}+C
$$
##### 9.1b
$$
\int x^3\cos(x^4+2)dx:u=x^4+2\implies\frac{du}{4x^3}=dx
$$
$$
=\int \frac{1}{4}\cos(u)du=\frac{1}{4}\sin(x^4+2)+C
$$
##### 9.1c
$$
\int\sqrt{2x+1}dx:u=2x+1\implies\frac{du}{2}=dx
$$
$$
=\frac{1}{2}\int\sqrt{u}du=\frac{1}{3}(2x+1)^\frac{3}{2}+C
$$
##### 9.1d
$$
\int\frac{x}{\sqrt{1-4x^2}}dx:u=1-4x^2\implies\frac{du}{-8x}=dx
$$
$$
=-\frac{1}{8}\int\frac{1}{\sqrt{u}}dx=-\frac{1}{4}(1-4x^2)^\frac{1}{2}+C
$$
#### 9.2
##### 9.2a
$$
\int_1^2\frac{dx}{(3-5x)^2}:u=3-5x\implies\frac{du}{-5}=dx
$$
$$
=-\frac{1}{5}\int_{-2}^{-7}u^{-2}du=\frac{1}{5}\left[\frac{1}{u}\right]_{-2}^{-7}
$$
$$
=\frac{1}{5}\left(\frac{1}{2}-\frac{1}{7}\right)=\frac{1}{14}
$$
##### 9.2b
$$
\int_2^4\frac{e^\sqrt{t}}{\sqrt{t}}dt:u=\sqrt{t}\implies\frac{du}{\frac{1}{2}t^{-\frac{1}{2}}}=dx
$$
$$
=2\int_\sqrt{2}^2e^udu=2\left[e^u\right]_\sqrt{2}^2
$$
$$
=2(e^2-e^\sqrt{2})
$$
##### 9.2c
$$
\int_0^t\frac{\cos x}{(2+\sin x)^\frac{2}{7}}dx:u=2+\sin x\implies\frac{du}{\cos x}=dx
$$
$$
=\int_2^{2+\sin t}\frac{1}{u^\frac{2}{7}}du=\left[\frac{7}{5}u^\frac{5}{7}\right]_2^{2+\sin t}=\frac{7}{5}((2+\sin t)^\frac{5}{7}-2^\frac{5}{7})
$$
##### 9.2d
$$
\int_{-\frac{\pi}{2}}^\frac{\pi}{2}e^{\sin x}\cdot\sin x\cdot\cos x dx:u=\sin x\implies\frac{du}{\cos x}=dx
$$
$$
\int^1_{-1}u\cdot e^u du =\left[\right]
$$
$+$ $u$ $e^u$
$-$ $1$ $e^u$
$+$ $0$ $e^u$
