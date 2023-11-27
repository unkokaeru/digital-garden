#### Derivation of the area of an oval
*Expected result: $A=\pi\cdot ab$.*

$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\implies y=\pm\frac{b}{a}\sqrt{a^2-x^2}
$$
$$
\text{In the top-right quadrant, }y=\frac{b}{a}\sqrt{a^2-x^2}:0\le x\le a
$$
$$
\therefore \frac{1}{4}A=\int_0^a\frac{b}{a}\sqrt{a^2-x^2}dx
$$
$$
A=\frac{4b}{a}\int_0^a\sqrt{a^2-x^2}dx,\quad\text{let }x=a\sin\theta:dx=a\cos\theta d\theta
$$
$$
A = 4ab\int_0^\frac{\pi}{2}\cos^2\theta d\theta:\cos^2\theta=\frac{1}{2}(1+\cos2\theta)
$$
$$
\therefore A=2ab\int_0^\frac{\pi}{2}(1+\cos2\theta)d\theta=2ab\left[\theta+\frac{1}{2}\sin2\theta\right]_0^\frac{\pi}{2}=2ab\cdot\frac{\pi}{2}=\pi\cdot ab\quad\square
$$
