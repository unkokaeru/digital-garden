# Complex Numbers

Complex numbers are an extension of the real numbers and can be represented in the form $a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit with the property that $i^2 = -1$.

## Arithmetic of Complex Numbers

### Addition and Subtraction

Given two complex numbers $z_1 = a + bi$ and $z_2 = c + di$, their sum and difference are:
$$
z_1 + z_2 = (a + c) + (b + d)i
$$
$$
z_1 - z_2 = (a - c) + (b - d)i
$$

### Multiplication

The product of $z_1$ and $z_2$ is:
$$
z_1 \times z_2 = (ac - bd) + (ad + bc)i
$$

### Division

The quotient of $z_1$ by $z_2$ is:
$$
\frac{z_1}{z_2} = \frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{c^2 + d^2}
$$
*This is simply multiplying numerator and denominator by the conjugate of the denominator*

## Geometric Interpretation

Complex numbers can be represented geometrically on the complex plane, with the real part on the x-axis and the imaginary part on the y-axis. The distance from the origin to the point $(a, b)$ is the magnitude (or modulus) of the complex number, denoted as $|z|$.

### Modulus and Argument

The modulus of $z = a + bi$ is:
$$
|z| = \sqrt{a^2 + b^2}
$$

The argument (or angle) of $z$, denoted as $arg(z)$, is the angle $\theta$ such that:
$$
\tan(\theta) = \frac{b}{a}
$$

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

## Applications

Complex numbers have applications in various fields of science and engineering, especially in electrical engineering, fluid dynamics, and quantum mechanics.

---

This note provides a comprehensive overview of complex numbers, their properties, and their applications. Complex numbers play a crucial role in advanced mathematics and its applications in various scientific fields.