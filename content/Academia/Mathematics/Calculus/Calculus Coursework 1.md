![[MTH1002_Coursework.pdf]]

___
___

## Question 1
### Question 1a
$$
f(x)=\sin(3x^4-x^2+2)\
$$
$$
\implies f(-x)=\sin(3(-x)^4-(-x)^2+2):\text{testing the behaviour of the function}
$$
$$
\implies f(-x)=\sin(3x^4-x^2+2)=f(x)
$$
$$
\therefore f(-x)=f(x):\text{the function is even (it displays reflective symmetry).}
$$
### Question 1b
$$
g(v)=\frac{v^5-v^3+1}{v^4+v^2+v}
$$
$$
\implies g(-v)=\frac{(-v)^5-(-v)^3+1}{(-v)^4+(-v)^2+(-v)}:\text{testing the behaviour of the function}
$$
$$
g(-v)=\frac{-v^5+v^3+1}{v^4+u^2-v}\ne \pm g(\mp v)
$$
$$
\therefore g(-v)\ne\pm g(\mp v):\text{the function is neither odd nor even (asymmetrical).}
$$
## Question 2
### Question 2a
$$
\sinh x=\frac{e^x-e^{-x}}{2},\cosh x=\frac{e^x+e^{-x}}{2}
$$
$$
\implies2\sinh x\cosh x=2\left(\frac{e^x-e^{-x}}{2}\frac{e^x+e^{-x}}{2}\right)
$$
$$
\implies2\sinh x\cosh x=\frac{(e^x-e^{-x})(e^x+e^{-x})}{2}
$$
$$
\implies2\sinh x\cosh x=\frac{e^{2x}-e^{-2x}}{2}:\text{by the difference of two squares}
$$
$$
\implies2\sinh x\cosh x=\frac{e^{2x}-e^{-2x}}{2}=\sinh2x
$$
$$
\therefore2\sinh x\cosh x=\sinh2x\space\square
$$
### Question 2b
$$
\sinh x=\frac{e^x-e^{-x}}{2},\cosh x=\frac{e^x+e^{-x}}{2}
$$
$$
\implies\cosh x\cosh y+\sinh x\sin y=\left(\frac{e^x+e^{-x}}{2}\frac{e^y+e^{-y}}{2}\right)+\left(\frac{e^x-e^{-x}}{2}\frac{e^y-e^{-y}}{2}\right)
$$
$$
\implies\cosh x\cosh y+\sinh x\sin y=\frac{(e^x+e^{-x})(e^y+e^{-y})+(e^x-e^{-x})(e^y-e^{-y})}{4}
$$
$$
\implies\cosh x\cosh y+\sinh x\sin y=\frac{(e^{x+y}+e^{x-y}+e^{y-x}+e^{-x-y})+(e^{x+y}-e^{x-y}-e^{y-x}+e^{-x-y})}{4}
$$
$$
\implies\cosh x\cosh y+\sinh x\sin y=\frac{2e^{x+y}+2e^{-(x+y)}}{4}
$$
$$
\implies\cosh x\cosh y+\sinh x\sin y=\frac{e^{(x+y)}+e^{-(x+y)}}{2}=\cosh(x+y)
$$
$$
\therefore\cosh x\cosh y+\sinh x\sin y=\cosh(x+y)\space\square
$$
## Question 3
$$
z_1=3+i,z_2=7-i
$$
### Question 3a
$$
z_1z_2=(3+i)(7-i)
$$
$$
\implies z_1z_2=22+4i
$$
### Question 3b
$$
\frac{|z_1|}{|z_2|}=\frac{\sqrt{(3)^2+(1)^2}}{\sqrt{(7)^2+(-1)^2}}
$$
$$
\implies\frac{|z_1|}{|z_2|}=\frac{\sqrt{10}}{\sqrt{50}}=\frac{10}{5\sqrt{2}}
$$
### Question 3c
$$
\frac{z_1}{z_2}=\frac{3+i}{7-i}\cdot\frac{7+i}{7+i}
$$
$$
\implies\frac{z_1}{z_2}=\frac{20+10i}{50}=\frac{2+i}{5}
$$
$$
\implies\frac{z_1}{z_2}=\frac{2}{5}+\frac{1}{5}i
$$
### Question 3d
$$
\frac{\bar{z_2}}{\bar{z_1}}=\frac{7+i}{3-i}\cdot\frac{3+i}{3+i}
$$
$$
\implies\frac{\bar{z_2}}{\bar{z_1}}=\frac{20+10i}{10}=2+i
$$
## Question 4
### Question 4a
$$
2\sqrt{2}-2\sqrt{2}i\implies(r,\theta)=\left(\sqrt{(2\sqrt{2})^2+(-2\sqrt{2})^2},\tan^{-1}\left(\frac{-2\sqrt{2}}{2\sqrt{2}}\right)\right)
$$
$$
\implies(r,\theta)=\left(4,-\frac{\pi}{4}\right):0\le\theta\lt2\pi
$$
$$
\therefore(r,\theta)=\left(4,\frac{7\pi}{4}\right)
$$
![[Calculus Coursework 1 2023-10-26 16.34.17.excalidraw]]
Above (in red) is plotted the complex number $2\sqrt{2}-2\sqrt{2}i$, which in polar form is represented as $4\left(\cos\frac{7\pi}{4}+isin\frac{7\pi}{4}\right)$.
### Question 4b
$$
-2\sqrt{3}+2i\implies(r,\theta)=\left(\sqrt{(-2\sqrt{3})^2+(2)^2},\tan^{-1}\left(\frac{2}{-2\sqrt{3}}\right)\right)
$$
$$
\implies(r,\theta)=\left(4,-\frac{\pi}{6}\right):0\le\theta\lt2\pi
$$
$$
\therefore(r,\theta)=\left(4,\frac{11\pi}{6}\right)\text{, however this is in the wrong direction}
$$
$$
\implies(r,\theta)=\left(4,\frac{5\pi}{6}\right)
$$
![[Calculus Coursework 1 2023-10-26 16.36.15.excalidraw]]
Above is plotted the complex number $-2\sqrt{3}+2i$, which in polar form is represented as $4\left(\cos\frac{5\pi}{6}+isin\frac{5\pi}{6}\right)$.
## Question 5
### Question 5a
$$
z^3=4(-1+\sqrt{3}i)\implies z=4^{\frac{1}{3}}(-1+\sqrt{3}i)^\frac{1}{3}
$$
First, working out the angle of $z$, which would be the same as the angle of any multiple of $z$, hence:
$$
\angle z=\frac{\angle(-1+\sqrt{3}i)+2n\pi}{3}=\frac{\tan^{-1}\left(\frac{\sqrt{3}}{-1}\right)+2n\pi}{3}=\frac{-\frac{\pi}{3}+2n\pi}{3}=\frac{(6n-1)\pi}{9}
$$
$$
\implies\angle z=\frac{(6n-1)\pi}{9}=\theta,
$$
Next, working out the modulus of $z$,
$$
|z|=4^{\frac{1}{3}}\cdot|-1+\sqrt{3}i|=4^{\frac{1}{3}}\cdot\sqrt{(-1)^2+(\sqrt{3})^2}=4^{\frac{1}{3}}\cdot2
$$
$$
\implies|z|=2^{\frac{2}{3}}\cdot2=2^{\frac{5}{3}}=r.
$$
Combining this information gives us the polar form of $z$:
$$
\therefore z=(r,\theta)=\left(2^\frac{5}{3},\frac{(6n-1)\pi}{9}\right):n\in\mathbb{z}
$$
$$
\implies z=\left(2^\frac{5}{3},\frac{5\pi}{9}\right),\left(2^\frac{5}{3},\frac{11\pi}{9}\right),\left(2^\frac{5}{3},\frac{17\pi}{9}\right)
$$
Which we can then convert into exponential form:
$$
\therefore z=2^\frac{5}{3}\cdot e^\frac{5\pi}{9},2^\frac{5}{3}\cdot e^\frac{11\pi}{9},2^\frac{5}{3}\cdot e^\frac{17\pi}{9}
$$
### Question 5b
$$
z^4=\frac{1}{i}\cdot\frac{-i}{-i}=-i\implies z=(-i)^\frac{1}{4}
$$
First, working out the angle of $z$:
$$
\angle z=\frac{\angle(-i)+2n\pi}{4}=\frac{\frac{3\pi}{2}+2n\pi}{4}=\frac{(3+4n)\pi}{8}
$$
$$
\implies\angle z=\frac{(3+4n)\pi}{8}=\theta,
$$
Next, working out the modulus of $z$,
$$
|z|=\sqrt{(0)^2+(\sqrt{-1})^2}=1=r
$$
Combining this information gives us the polar form of $z$:
$$
\therefore z=(r,\theta)=\left(1,\frac{(3+4n)\pi}{8}\right):n\in\mathbb{z}
$$
$$
\implies z=\left(1,\frac{3\pi}{8}\right),\left(1,\frac{7\pi}{8}\right),\left(1,\frac{11\pi}{8}\right),\left(1,\frac{15\pi}{8}\right)
$$
Which we can then convert into exponential form:
$$
\therefore z=e^\frac{3\pi}{8},e^\frac{7\pi}{8},e^\frac{11\pi}{8},e^\frac{15\pi}{8}
$$
## Question 6
### Question 6a
$$
\lim_{x\to3}\frac{x-3}{x^2+x-12}=\frac{0}{0}:\text{undefined, use L'hôptial's Rule - differentiate}
$$
$$
\implies\lim_{x\to3}\frac{1}{2x+1}=\frac{1}{7}
$$
### Question 6b
$$
\lim_{v\to\infty}\frac{1-v^2+3v^3-4v^4}{9v^4+2v^3-5}=\lim_{v\to\infty}\left(\frac{1-v^2+3v^3-4v^4}{9v^4+2v^3-5}\cdot\frac{v^{-4}}{v^{-4}}\right)
$$
$$
=\lim_{v\to\infty}\frac{v^{-4}-v^{-2}+3v^{-1}-4}{9+2v^{-1}-5v^{-4}}=-\frac{4}{9}
$$
### Question 6c
$$
\lim_{y\to0}\frac{e^{ay}-1-ay}{y^2}=\frac{0}{0}:\text{undefined, use L'hôptial's Rule - differentiate}
$$
$$
\implies\lim_{y\to0}\frac{ae^{ay}-y}{2y}=\frac{a}{0}:\text{undefined, use L'hôptial's Rule - differentiate}
$$
$$
\implies\lim_{y\to0}\frac{a^2e^{ay}-1}{2}=\frac{a^2-1}{2}
$$
### Question 6d
$$
\lim_{x\to1}\left(\frac{1}{\ln x}-\frac{1}{x-1}\right)=\lim_{x\to1}\left(\frac{(x-1)-(\ln x)}{(\ln x)(x-1)}\right)=\lim_{x\to1}\left(\frac{x-1-\ln x}{x\ln x-\ln x}\right)=\frac{0}{0}
$$
$$
:\text{undefined, use L'hôptial's Rule - differentiate using product rule/chain rule}
$$
$$
\implies \lim_{x\to1}\left(\frac{1-\frac{1}{x}}{\ln x+1-\frac{1}{x}}\right)=\frac{0}{0}:\text{undefined, use L'hôptial's Rule - differentiate}
$$
$$
\implies\lim_{x\to1}\left(\frac{x^{-2}}{x^{-2}+x^{-1}}\right)=\frac{1}{2}
$$