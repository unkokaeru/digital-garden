**Note: below is a list of corrections to the solutions provided by the lecturer, but everything I have written here is correct, I think.**
- Question 5a: error in answer, should be $3ax^2+b$ not $ax^2+b$
- Question 6: easier route through logarithmic differentiation

![[MTH1002_Calculus_Practical_5.pdf]]

#### Question 1
##### Question 1a
$$
f(x)=3x^5-2x^2+7x^{-\frac{1}{2}}+2\implies f^\prime(x)=15x^4-4x-\frac{7}{2}x^{-\frac{3}{2}}
$$
##### Question 1b
$$
f(x)=\frac{x^3+3x^2+7}{x-1}\implies f^\prime(x)=\frac{(3x^2+6x)(x-1)-(1)(x^3+3x^2+7)}{(x-1)^2}
$$
$$
\implies f^\prime(x)=\frac{2x^3-6x-7}{(x-1)^2}
$$
##### Question 1c
$$
f(x)=e^x\sin x\implies f^\prime(x)=e^x\sin x+e^x\cos x
$$
$$
\implies f^\prime(x)=e^x(\sin x + \cos x)
$$
##### Question 1d
$$
f(x)=4x^4e^{cx}\implies f^\prime(x)=16x^3e^{cx}+4cx^4e^{cx}
$$
$$
\implies f^\prime(x) = 4x^3e^{cx}(4+x)
$$
##### Question 1e
$$
f(x)=\frac{\cos ax}{x^3}\implies f^\prime(x)=-\frac{ax^3\sin ax-3x^2\cos ax}{x^6}
$$
$$
\implies f^\prime(x) = \frac{3\cos ax - ax\sin ax}{x^4}
$$
##### Question 1f
$$
f(x)=\frac{ae^{bx}}{\sin cx}\implies f^\prime(x)=\frac{abe^{bx}\sin cx-ace^{bx}\cos cx}{\sin^2cx}
$$
$$
\implies f^\prime(x)=\frac{ae^{bx}(b\sin cx-c\cos cx)}{\sin^2cx}
$$
#### Question 2
##### Question 2a
$$
f(x)=\sin(5x+2)\implies f^\prime(x)=5\cos(5x+2)
$$
##### Question 2b
$$
f(x)=\ln\left(1+x^{-2}\right)\implies f^\prime(x)=-\frac{2x^{-3}}{1+x^{-2}}
$$
$$
\implies f^\prime(x)=-\frac{2}{x(x^2+1)}
$$
##### Question 2c
$$
f(x)=\sin^3x\implies f^\prime(x)=3\cos x\sin^2x
$$
#### Question 3
##### Question 3a
$$
h(t)=(t^3-1)^{100}\implies h^\prime(t)=300t^2(t^3-1)^{99}
$$
##### Question 3b
$$
h(t)=\sin(a+bt^4)\implies h^\prime(t)=4bt^3\cos(a+bt^4)
$$
##### Question 3c
$$
h(t)=a\cos(b\tan ct)\implies h^\prime(t)=-abc\sec^2(ct)\sin(b\tan ct)
$$
#### Question 4
##### Question 4a
$$
\frac{d}{dx}\left(x^4e^{3x}\tan x\right)\implies\frac{d}{dx}\left(4\ln x+3x+\ln\tan x\right)
$$
$$
\implies x^4e^{3x}\tan x\cdot(\frac{4}{x}+3+2\csc(2x))
$$
##### Question 4b
$$
\frac{d}{dx}\left(\frac{e^{4x}}{x^3\cosh2x}\right)\implies\frac{d}{dx}(4x-3\ln x -\ln\cosh2x)
$$
$$
\implies\frac{e^{4x}}{x^3\cosh2x}\cdot(4-\frac{3}{x}-\tanh2x)
$$
#### Question 5
##### Question 5a
$$
f(x)=ax^3+bx:f^\prime(x)=\lim_{h\to0}\left(\frac{f(x+h)-f(x)}{h}\right)
$$
$$
\implies f^\prime(x)=\lim_{h\to0}\left(\frac{(a(x+h)^3+b(x+h))-(ax^3+bx)}{h}\right)
$$
$$
\implies f^\prime(x)=\lim_{h\to0}\left(\frac{a((x+h)^3-x^3)+bh}{h}\right)
$$
$$
\implies f^\prime(x)=\lim_{h\to0}\left(\frac{bh+a((x+h)-x)((x+h)^2+x(x+h)+x^2)}{h}\right)
$$
$$
\implies f^\prime(x)=\lim_{h\to0}\left(b+a(3x^2+h^2+3xh)\right)
$$
$$
\implies f^\prime(x)=3ax^2+b
$$
##### Question 5b
$$
f(x)=\sqrt{cx+d}:f^\prime(x)=\lim_{h\to0}\left(\frac{f(x+h)-f(x)}{h}\right)
$$
$$
\implies f^\prime(x)=\lim_{h\to0}\left(\frac{(\sqrt{c(x+h)+d})-(\sqrt{cx+d})}{h}\right)
$$
$$
\implies f^\prime(x)=\lim_{h\to0}\left[\left(\frac{\sqrt{(cx+d)+ch}-\sqrt{cx+d}}{h}\right)\left(\frac{\sqrt{(cx+d)+ch}+\sqrt{cx+d}}{\sqrt{(cx+d)+ch}+\sqrt{cx+d}}\right)\right]
$$
$$
\implies f^\prime(x)=\lim_{h\to0}\left(\frac{c}{\sqrt{cx+d+ch}+\sqrt{cx+d}}\right)
$$
$$
\therefore f^\prime(x)=\frac{c}{2\sqrt{cx+d}}
$$

##### Question 5c (to-do)
$$
f(x)=\frac{1}{\sqrt{ex+f}}:f^\prime(x)=\lim_{h\to0}\left(\frac{f(x+h)-f(x)}{h}\right)
$$
$$
\implies f^\prime(x)=\lim_{h\to0}\left(\frac{(e(x+h)+f)^{-\frac{1}{2}}-(ex+f)^{-\frac{1}{2}}}{h}\right)
$$
$$
\implies f^\prime(x)=\lim_{h\to0}\left(\frac{}{h}\right)
$$
Solution: [[Pasted image 20231027195115.png]]
#### Question 6
$$
f(x)=(x-a)(x-b)(x-c)\implies f(x) =\ln(x-a)+\ln(x-b)+\ln(x-c)
$$
$$
\implies f^\prime(x)=(x-a)(x-b)(x-c)\cdot\left(\frac{1}{x-a}+\frac{1}{x-b}+\frac{1}{x-c}\right)
$$
$$
\therefore\frac{f^\prime(x)}{f(x)}=\frac{1}{x-a}+\frac{1}{x-b}+\frac{1}{x-c}\space\square
$$
#### Question 7
##### Question 7a
$$
\cos2x=\cos^2x-\sin^2x\implies-2\sin2x=-2\sin x\cos x-2\sin x\cos x
$$
$$
\implies\sin2x=2\sin x\cos x
$$
##### Question 7b
$$
\sin(a+b)=\sin a\cos b+\cos a\sin b
$$
$$
\implies\left(1+\frac{db}{da}\right)\cos(a+b)=\left(\cos a\cos b-\frac{db}{da}\sin a\sin b\right)+\left(-\sin a\sin b+\frac{db}{da}\cos a\cos b\right)
$$
$$
\implies\cos(a+b)=\frac{\left(1+\frac{da}{db}\right)(\cos a\cos b-\sin a\sin b)}{1+\frac{db}{da}}
$$
$$
\therefore\cos(a+b)=\cos a\cos b-\sin a\sin b
$$