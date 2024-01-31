![[MTH1002_Calculus_Practical_3.pdf]]

### Question 1
$$
-i=e^{\frac{3\pi}{2}}
$$
$$
-\frac{1}{2}-\frac{i}{2}=\sqrt{(-\frac{1}{2})^2+(-\frac{1}{2})^2}\cdot e^{i\tan^{-1}\left(1\right)}=\frac{1}{\sqrt{2}}\cdot e^{i\frac{5\pi}{4}}
$$
$$
-\sqrt{3}+i=\sqrt{(-\sqrt{3})^2+(1)^2}\cdot e^{i\tan^{-1}\left(\frac{1}{-\sqrt{3}}\right)}=2e^{i\frac{5\pi}{6}}
$$
$$
3-\sqrt{3}i=\sqrt{(3)^2+(-\sqrt{3})^2}\cdot e^{i\tan^{-1}\left(\frac{-\sqrt{3}}{3}\right)}=2\sqrt{3}\cdot e^{i\frac{11\pi}{6}}
$$
$$
-\frac{1}{\sqrt{3}}-i=\sqrt{(-\frac{1}{\sqrt{3}})^2+(-1)^2}\cdot e^{i\tan^{-1}\left(\frac{-1}{-\frac{1}{\sqrt{3}}}\right)}=\frac{4}{3}e^{i\frac{4\pi}{3}}
$$
### Question 2
*Plot these on the Argand diagram at home, using my drawing tablet*
$$
z^3=-i\implies\text{arg}(z)=\frac{\text{arg}(-i) + 2k\pi}{3}=\frac{\frac{3\pi}{2}+2k\pi}{3}=\frac{(3+4k)\pi}{6}
$$
$$
\therefore z=e^{i\frac{3\pi}{6}},e^{i\frac{7\pi}{6}},e^{i\frac{11\pi}{6}}
$$
___
$$
z^3=8\implies\text{arg}(z)=\frac{\text{arg}(8) + 2k\pi}{3}=\frac{2k\pi}{3}
$$
$$
\therefore z=1,e^{i\frac{2\pi}{3}},e^{i\frac{4\pi}{3}}
$$
___
$$
z^2=i\implies\text{arg}(z)=\frac{\text{arg}(i)+2k\pi}{2}=\frac{\frac{\pi}{2}+2k\pi}{2}=\frac{(1+4k)\pi}{4}
$$
$$
\therefore z=e^{i\frac{\pi}{4}},z=e^{i\frac{5\pi}{4}}
$$
___
$$
z^4=8\sqrt{2}(1-i)\implies\text{arg}(z)=\frac{\text{arg}(8\sqrt{2}(1-i))+2k\pi}{4}=\frac{\frac{7\pi}{4}+2k\pi}{4}=\frac{(7+8k)\pi}{16}
$$
$$
\therefore z=e^{i\frac{7\pi}{16}},e^{i\frac{15\pi}{16}},e^{i\frac{23\pi}{16}},e^{i\frac{31\pi}{16}}
$$
### Question 3
$$
(\cos\theta+i\sin\theta)^3=\cos3\theta+i\sin3\theta
$$
$$
\implies\text{LHS}=\cos^3\theta+i\cos^2\theta\sin\theta-\cos\theta\sin^2\theta-i\sin^3\theta,\text{RHS}=\cos3\theta+i\sin3\theta
$$
$$
\implies\Re:\cos^3\theta-\cos\theta\sin^2\theta=\cos3\theta,\Im:\cos^2\theta\sin\theta-\sin^3\theta=\sin3\theta
$$
$$
\therefore\sin3\theta=\sin\theta-2\sin^3\theta,\text{ by using }\sin^2\theta+\cos^2\theta\equiv1,
$$
$$
\cos3\theta=2\cos^3\theta-\cos\theta,\text{ by using }\sin^2\theta+\cos^2\theta\equiv1.
$$
### Question 4
*I'm assuming there's an error in the question, where an $i$ is missed from the original given equation, given this:*
$$
(\sqrt{3}-i)^{10}=(2e^{i\frac{11\pi}{6}})^{10}=2^{10}\cdot e^{i\frac{110\pi}{6}}=2^{10}\cdot e^{i\frac{\pi}{3}}
$$
$$
\implies\sqrt{a^2+b^2}=2^{10},\frac{a}{b}=\tan\frac{\pi}{3}=\sqrt{3}:z=a+bi
$$
$$
\implies2^{20}=(b\sqrt{3})^2+b^2
$$
$$
\implies2^{9}=b,a=2^9\sqrt{3}
$$
$$
\therefore2^9(\sqrt{3}+i)\text{ or }2^9\sqrt{3}+2^9i
$$
*This seems very incorrect - check later*
### Question 5
Given that $\omega^0=1,\omega^1=e^{i\frac{2\pi}{3}},\omega^2=e^{i\frac{4\pi}{3}}$, show that $\omega^3=1$ and that $1+\omega+\omega^2=0$.
$$
\omega^3=\omega^2\cdot\omega^1=e^{i\frac{4\pi}{3}}\cdot e^{i\frac{2\pi}{3}}=e^{i2\pi}=e^{i0}=e^0=1\space\blacksquare
$$
$$
1+\omega+\omega^2=e^{i0}+e^{i\frac{4\pi}{3}}+e^{i\frac{2\pi}{3}}
$$
Converting each complex number into the form $a + bi$ gives the following:
$$
e^{i0}:\tan0=\frac{a_1}{b_1},1^2=a_1^2+b_1^2\therefore a_1=0,b_1=\pm1
$$
$$
e^{i\frac{4\pi}{3}}:\tan\frac{4\pi}{3}=\frac{a_2}{b_2},1^2=a_2^2+b_2^2\therefore a_1=\pm\frac{\sqrt{3}}{2},b_2=\pm\frac{1}{2}
$$
$$
e^{i\frac{2\pi}{3}}:\tan\frac{2\pi}{3}=\frac{a_3}{b_3},1^2=a_3^2+b_3^2\therefore a_3=
$$