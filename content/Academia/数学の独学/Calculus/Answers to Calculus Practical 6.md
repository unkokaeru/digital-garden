![[MTH1002_Calculus_Practical_6.pdf]]

#### Question 1
Finding the critical points of the following functions...
##### Question 1a
$$
f(x)=x^{\frac{7}{8}}(x-3)^2:x\ge0
$$
$$\text{Differentiating this function using the product and chain rules,}$$
$$
f^\prime(x)=\frac{7}{8}x^{-\frac{1}{8}}(x-3)^2+2x^{\frac{7}{8}}(x-3):x\ge0
$$
$$
\implies f^\prime(x)=(x-3)\left[\frac{7}{8}x^{-\frac{1}{8}}(x-3)+2x^{\frac{7}{8}}\right]
$$
$$\text{Solving for when }f^\prime(x)=0\text{ to find the critical points (as the gradient would be 0),}$$
$$
(x-3)\left[\frac{7}{8}x^{-\frac{1}{8}}(x-3)+2x^{\frac{7}{8}}\right]=0
$$
$$
\implies x=0,\frac{21}{23},3
$$
$$\text{After substituting these x values into the original equation, we find}$$
$$
\text{Critical points }(x,y)=(0,0),\left(\frac{21}{23},\frac{230421^\frac{7}{8}}{52923^\frac{7}{8}}\right),(3,0)
$$
##### Question 1b
$$
f(x)=\frac{x-1}{x^2+4}
$$
$$
\text{Differentiating this function by using the quotient rule}
$$
$$
f^\prime(x)=\frac{2x(x-1)-(x^2+4)}{(x^2+4)^2}
$$
$$
\implies f^\prime(x)=\frac{x^2-2x-4}{(x^2+4)^2}
$$
$$\text{Solving for when }f^\prime(x)=0\text{ to find the critical points (as the gradient would be 0),}$$
$$
f^\prime=0:x^2-2x-4=0
$$
$$
\implies x=1\pm\sqrt{5}\text{ by using the quadratic formula}
$$
$$\text{After substituting these x values into the original equation, we find}$$
$$
\text{Critical points }(x,y)=\left(1+\sqrt{5},\frac{\sqrt{5}-1}{8}\right),\left(1-\sqrt{5},-\frac{\sqrt{5}+1}{8}\right)
$$
#### Question 2
Finding the absolute maxima and minima of the following functions...
##### Question 2a
$$
f(x)=2x^3+3x^2-12x-12\in[-3,2]
$$
$$
\implies f^\prime(x)=6x^2+6x-12=0\quad\text{gradient}=0\text{ at extrema}
$$
$$
\implies x^2+x-2=0:x=-2,1
$$
$$
f^{\prime\prime}(x)=12x+6:f^{\prime\prime}(-2)<0,f^{\prime\prime}(1)>0
$$
$$
\therefore\begin{matrix}
\text{Absolute maxima at }(-2,8)\\
\text{Absolute minima at }(1,-19)
\end{matrix}\quad\text{for the given interval }[-3,2]
$$
##### Question 2b
$$
f(x)=x+\frac{1}{x}\in[0.2,4]
$$
$$
\implies f^\prime(x)=1-\frac{1}{x^2}=0\quad\text{gradient}=0\text{ at extrema}
$$
$$
\implies x^2-1=0:x=\pm1:x=-1\text{ is not in the interval}
$$
$$
f^{\prime\prime}(x)=\frac{2}{x^3}:f^{\prime\prime}(1)>0
$$
$$
\therefore\text{Absolute minima at }(1,2)\text{ for the given interval }[0.2,4]
$$
#### Question 3
Find the intervals of increase and decrease of the following functions...
##### Question 3a
$$
f(x)=x^3-3x+2
$$
$$
\implies f^\prime(x)=3x^2-3\quad\text{gradient}=0\text{ at extrema}
$$
$$
\implies x^2-1=0:x=\pm1
$$
$$
\therefore\text{Three intervals of increase/decrease: }(-\infty,-1),(-1,1),(1,\infty)
$$
$$
\text{Testing one value from each interval,}
$$
$$
\begin{matrix}
(-\infty,-1)\implies f^\prime(-2)=9>0\implies\text{increasing}\\
(-1,1)\implies f^\prime(0)=-3<0\implies\text{decreasing}\\
(1,\infty)\implies f^\prime(2)=9>0\implies\text{increasing}
\end{matrix}
$$
##### Question 3b
$$
g(x)=x\cdot e^{-\frac{3x^2}{2}}
$$
$$
\implies g^\prime(x)=e^{-\frac{3x^2}{2}}-\frac{3x^2}{3}\cdot e^{-\frac{3x^2}{2}}\quad\text{gradient }=0\text{ at extrema}
$$
$$
\implies e^{-\frac{3x^2}{2}}\left(1-x^2\right)=0:x=\pm1
$$
$$
\therefore\text{Three intervals of increase/decrease: }(-\infty,-1),(-1,1),(1,\infty)
$$
$$
\text{Testing one value from each interval,}
$$
$$
\begin{matrix}
(-\infty,-1)\implies f^\prime(-2)=-3e^{-6}<0\implies\text{decreasing}\\
(-1,1)\implies f^\prime(0)=1>0\implies\text{increasing}\\
(1,\infty)\implies f^\prime(2)=-3e^{-6}<0\implies\text{decreasing}
\end{matrix}
$$
#### Question 4
To find a formula for $\tanh^{-1}(x)$,
$$
\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}=y
$$
$$\text{Then by solving for x,}$$
$$
e^x-e^{-x}=y(e^x+e^{-x})
$$
$$
\implies e^x-e^{-x}=ye^x+ye^{-x}
$$
$$
\implies (1-y)e^x-(1+y)e^{-x}=0
$$
$$
\implies (1-y)e^{2x}-(1+y)=0
$$
$$
\implies e^{2x}=\frac{1+y}{1-y}
$$
$$
\implies x=\frac{1}{2}\ln\left(\frac{1+y}{1-y}\right)
$$
$$
\therefore \tanh^{-1}(x)=\frac{1}{2}\ln\left(\frac{1+x}{1-x}\right):
\begin{matrix}
\text{domain: }\\
\text{range: }
\end{matrix}
$$
