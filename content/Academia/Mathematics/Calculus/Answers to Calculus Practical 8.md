#### Question 1
$$
\text{Around the point }a=0,
$$
$$
f(x)=\cos(x)\approx f(0)+f^\prime(0)(x-0)+\frac{f^{\prime\prime}(0)}{2}(x-0)^2+\frac{f^{3}(0)}{6}(x-0)^3+\frac{f^4(0)}{24}(x-0)^4
$$
$$
\begin{matrix}
f^\prime(x)=-\sin x&&f^\prime(0)=0\\
f^{\prime\prime}(x)=-\cos x&&f^{\prime\prime}(0)=-1\\
f^3(x)=\sin  x&&f^3(0)=0\\
f^4(x)=\cos x&&f^4(0)=1\\
\end{matrix}
$$
$$
f(x)\approx1-\frac{1}{2}x^2+\frac{1}{24}x^4
$$
#### Question 2
$$
\text{Around the point }a=\frac{\pi}{6},
$$
$$
f(x)=\sin(x)\approx f(\frac{\pi}{6})+f^\prime(\frac{\pi}{6})(x-\frac{\pi}{6})+\frac{f^{\prime\prime}(\frac{\pi}{6})}{2}(x-\frac{\pi}{6})^2+\frac{f^{3}(\frac{\pi}{6})}{6}(x-\frac{\pi}{6})^3+\frac{f^4(\frac{\pi}{6})}{24}(x-\frac{\pi}{6})^4
$$
$$
\begin{matrix}
f^\prime(x)=\cos x&&f^\prime(\frac{\pi}{6})=\frac{\sqrt{3}}{2}\\
f^{\prime\prime}(x)=-\sin x&&f^{\prime\prime}(\frac{\pi}{6})=-\frac{1}{2}\\
f^3(x)=-\cos  x&&f^3(\frac{\pi}{6})=-\frac{\sqrt{3}}{2}\\
f^4(x)=\sin x&&f^4(\frac{\pi}{6})=\frac{1}{2}\\
\end{matrix}
$$
$$
f(x)\approx\frac{1}{2}+\frac{\sqrt{3}}{2}(x-\frac{\pi}{6})-\frac{1}{2}\frac{1}{2}(x-\frac{\pi}{6})^2-\frac{1}{6}\frac{\sqrt{3}}{2}(x-\frac{\pi}{6})^3+\frac{1}{24}\frac{1}{2}(x-\frac{\pi}{6})^4
$$
$$
f(x)\approx\frac{1}{2}+\frac{\sqrt{3}}{2}(x-\frac{\pi}{6})-\frac{1}{4}(x-\frac{\pi}{6})^2-\frac{\sqrt{3}}{12}(x-\frac{\pi}{6})^3+\frac{1}{48}(x-\frac{\pi}{6})^4
$$
#### Question 3
$$
\text{Around the point }x=2,
$$
$$
e^x\approx\sum_{n=0}^\infty\frac{e^2}{n!}(x-2)^n
$$
#### Question 4
$$
\text{Around the point }x=0,
$$
$$
(1-x)^{-1}\approx f(0)+f^\prime(0)x+\frac{1}{2}f^{\prime\prime}(0)x^2+\frac{1}{6}f^{3}(0)x^3
$$
$$
\begin{matrix}
f(x)=(1-x)^{-1}&&f(0)=1\\
f^1(x)=(1-x)^{-2}&&f(0)=1\\
f^2(x)=2(1-x)^{-3}&&f(0)=2\\
f^3(x)=6(1-x)^{-4}&&f(0)=6
\end{matrix}
$$
$$
(1-x)^{-1}\approx1+x+x^2+x^3
$$
#### Question 5
$$
\text{Around the point }x=0,
$$
$$
\sinh x\approx f(0)+f^1(0)x+\frac{1}{2}f^2(0)x^2+\frac{1}{6}f^3(0)x^3+\frac{1}{24}f^4(0)x^4+\frac{1}{120}f^5(0)x^5
$$
$$
\begin{matrix}
f(x)=\sinh x&&f(0)=0\\
f^1(x)=\cosh x&&f(0)=1\\
f^2(x)=\sinh x&&f(0)=0\\
f^3(x)=\cosh x&&f(0)=1\\
f^4(x)=\sinh x&&f(0)=0\\
f^5(x)=\cosh x&&f(0)=1\\
\end{matrix}
$$
$$
\sinh x\approx x+\frac{1}{6}x^3+\frac{1}{120}x^5
$$
#### Question 6
$$
\text{Finding a quadratic approximation of }e^x\text{ for }x=\frac{1}{3},\text{find one about }x=0
$$
$$
\text{(otherwise there'll be values of }e^a\text{ in the approximation for }e^a\text{)}
$$
$$
e^x\approx f(0)+f^\prime(0)x+\frac{1}{2}f^{\prime\prime}(0)x^2:f^n(x)=e^x\implies f^n(0)=1
$$
$$
e^x\approx1+x+\frac{1}{2}x^2\implies e^\frac{1}{3}\approx1+\frac{1}{3}+\frac{1}{2}\cdot\left(\frac{1}{3}\right)^2
$$
$$
\therefore e^\frac{1}{3}\approx\frac{25}{18}
$$
$$
\text{Using the fact that }e^\frac{1}{3}\lt2,\text{ the upper bound on the error of the estimate is,}
$$
$$
R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{(n+1)}
$$