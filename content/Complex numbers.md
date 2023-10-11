# Complex Numbers ($\mathbb{C}$)
*Note that sometimes $j$ is used instead of $i$, especially in physics/engineering.*

Complex numbers are an extension of the real numbers and can be represented in the form $a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit with the property that $i^2 = -1$.

They appear most notably when solving quadratic equations, where in lower levels of mathematics education you may stop, here we continue:

**Example: The quadratic formula give the solutions of the quadratic equation $z^2-4z+5=0$ as $2\pm\frac{\sqrt{-4}}{2}$**

Continuing this by using the definition aforementioned, we can show that the full answer can be denoted by $2\pm i$.
## Separation of Real and Imaginary Parts

Complex numbers are in the form $z=a+bi$, where $a,b\space\epsilon\space\mathbb{R}$. $a$ and $b$ are the real and imaginary parts, respectively, of $z$, and are often denoted as $\Re(z)$ and $\Im(z)$.

If $a=0$, then $z$ is purely imaginary.
If $b=0$, then $z$ is real.

A complex number written as the sum of a real and an imaginary term is in standard form ($a+bi$).
## Arithmetic of Complex Numbers

### Addition and Subtraction

Given two complex numbers $z_1 = a + bi$ and $z_2 = c + di$, their sum and difference are:
$$
z_1 + z_2 = (a + c) + (b + d)i
$$
$$
z_1 - z_2 = (a - c) + (b - d)i
$$
*Note: ensure that you keep the real and imaginary separate!*

**Example: $(2+3i) + (1-2i)$**
$$
(2+3i)+(1-2i)=3+i
$$
**Example: $(2+3i) - (1-2i)$**
$$
(2+3i)-(1-2i)=1+5i
$$

### Multiplication

The product of $z_1$ and $z_2$, by using the definition of $i$, is:
$$
z_1 \times z_2 = (ac - bd) + (ad + bc)i
$$

**Example: $(2+3i)(1-2i)$**
$$
(2+3i)(1-2i)=2-4i+3i-6(i^2)=2-i+6=8-i
$$

### Division

The quotient of $z_1$ by $z_2$ is:
$$
\frac{z_1}{z_2} = \frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{c^2 + d^2}
$$
*This is simply multiplying numerator and denominator by the [conjugate](Complex%20numbers#Conjugate) of the denominator*

**Example: $\frac{2+3i}{1-2i}$**
$$
\frac{2+3i}{1-2i}=\frac{2+3i}{1-2i}\cdot\frac{1+2i}{1+2i}=\frac{7i-4}{5}=-\frac{4}{5}+\frac{7}{5}i
$$

## Geometric Interpretation

Complex numbers can be represented geometrically on the complex plane, with the real part on the x-axis and the imaginary part on the y-axis. The distance from the origin to the point $(a, b)$ is the magnitude (or modulus) of the complex number, denoted as $|z|$.

These graphs are often called Argand diagrams, for example:
![[Argand Diagram Example.excalidraw]]

### Modulus and Argument

The modulus of $z = a + bi$ is:
$$
|z| = \sqrt{a^2 + b^2}
$$

The argument (or angle) of $z$, denoted as $arg(z)$, is the angle $\theta$ such that:
$$
\tan(\theta) = \frac{b}{a}
$$
These are both derived from simple trigonometry in collusion with the Argand diagram. Note also that the argument is not unique, since it's derived using a periodic function.

In this course, we hence define it as $0\le\theta\lt2\pi$ for simplicity through convention. Ensure that the angle is pointing in the right direction, though - for example, the bottom left quadrant opposed to the top right quadrant (simply add $\pi$ if needed).

## Polar Form

A complex number can be represented in polar form as:
$$
z = r(\cos(\theta) + i\sin(\theta))
$$
where $r = |z|$ is the modulus and $\theta$ is the argument.

## Exponential Form

Using Euler's formula, the polar form can be expressed in exponential form:
$$
z = re^{i\theta}
$$
where $e$ is the base of the natural logarithm.

### Euler's Formula

Euler's formula relates the exponential function to the trigonometric functions:
$$
e^{i\theta} = \cos(\theta) + i\sin(\theta)
$$

### Euler's Identity

Euler's identity is a special case of Euler's formula when $\theta = \pi$:
$$
e^{i\pi} + 1 = 0
$$
This equation beautifully connects five of the most important numbers in mathematics: $e$, $i$, $\pi$, $1$, and $0$.

## Operations in Exponential Form

Multiplication and division become simpler in exponential form:

### Multiplication

$$
re^{i\theta} \times se^{i\phi} = rs e^{i(\theta + \phi)}
$$

### Division

$$
\frac{re^{i\theta}}{se^{i\phi}} = \frac{r}{s} e^{i(\theta - \phi)}
$$

## Conjugate

The conjugate of a complex number $z = a + bi$ is:
$$
\bar{z} = a - bi
$$

The product of a complex number and its conjugate is always a real number:
$$
z \times \bar{z} = |z|^2
$$
The derivation of the latter equation is as follows:
$$
z\times \bar{z}=(a+bi)(a-bi)=a^2+b^2=|z|^2\text{ by Pythagoras and the Difference of Two Squares}
$$

*Note that this is sometimes denoted as $z^\star=a-ib$, especially in physics.*
## Complex Numbers and Their Connection to Trigonometric Functions

Complex numbers, which have both a real and an imaginary component, can be expressed in terms of trigonometric functions. This representation is particularly useful when dealing with problems in physics and engineering where phase angles are involved.

- Euler's formula, named after the 18th-century Swiss mathematician Leonhard Euler, provides a profound connection between complex numbers and trigonometry. It states:
  - $e^{i\theta} = \cos(\theta) + i\sin(\theta)$

Using Euler's formula, the trigonometric functions sine and cosine can be defined in terms of complex exponentials:
  - $\cos(\theta) = \frac{e^{i\theta} + e^{-i\theta}}{2}$
  - $\sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i}$

Historically, Euler's formula was groundbreaking as it provided a bridge between the seemingly unrelated worlds of exponentials and trigonometry. This formula not only simplified many mathematical operations involving complex numbers but also paved the way for advancements in fields like electrical engineering and quantum mechanics.

## De Moivre's Theorem & Derivation of Double Angle Formulas

Named after Abraham de Moivre, a French mathematician of the 18th century, De Moivre's theorem is a powerful tool in the world of complex numbers. It provides a method to raise complex numbers to integer powers.

- Consider the expression $(\cos\theta + i\sin\theta)^2$. Using De Moivre's theorem, this can be simplified to:
  - $\cos2\theta + i\sin2\theta$

To understand this better, we can equate the real and imaginary parts after expanding the original expression:
  - The real part, $\cos2\theta$,  is equal to $\cos^2\theta - \sin^2\theta$
  - The imaginary part, $\sin2\theta$, is $2\sin\theta\cos\theta$
  - These are both respectively double angle formulae

De Moivre's theorem was instrumental in the development of complex number theory and has applications in various fields, from physics to engineering.

The theorem is generalised as the following...
$$
(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta
$$

## The Beauty of Argument and Modulus in Complex Numbers

In the complex plane, every number has a magnitude (modulus) and a direction (argument). The Argand diagram, named after Jean-Robert Argand, a French amateur mathematician of the 19th century, is a graphical representation of complex numbers where the x-axis represents the real part and the y-axis represents the imaginary part.

- The argument of a complex number is the angle it makes with the positive real axis. For instance, the argument in the Argand diagram for a certain complex number might be $\tan^{-1}\left(\frac{1}{1}\right) = \frac{\pi}{4} = \frac{5\pi}{4}$.

## Multiplication and Division in the Complex Realm

Complex numbers might seem intimidating at first, but their operations are elegantly simple, especially when expressed in exponential form; they can also assist with rotating complex numbers (as we add powers when multiplying two exponentials, we would add arguments - increasing or decreasing the angle of the complex number).

- Multiplying complex numbers in exponential form is more straightforward and intuitive than in their standard form. It involves multiplying their magnitudes and adding their arguments.
  - **Example**: If $z_1 = r_1e^{i\theta_1}$ and $z_2 = r_2e^{i\theta_2}$, then $z_1 \times z_2 = r_1r_2e^{i(\theta_1+\theta_2)}$

- For division, the process is just as elegant. For instance, to divide two complex numbers $z_1$ and $z_2$, represented in exponential form as $r_1e^{i\theta_1}$ and $r_2e^{i\theta_2}$ respectively, the result is:
  - $\frac{z_1}{z_2} = \frac{r_1e^{i\theta_1}}{r_2e^{i\theta_2}}$

## Roots of Complex Numbers: A Glimpse into Advanced Mathematics

Finding the roots of complex numbers is a topic that delves deep into the heart of mathematics. The nth root of a complex number is essentially the number which, when raised to the power of n, gives the original number.

- For a complex number $z$ and its nth root $w$, the general formula is:
  - $z^n = w$
  - The argument of the nth root is given by $\frac{\text{arg}(w) + 2k\pi}{n}$ for $k = 0, 1, \ldots, n-1$