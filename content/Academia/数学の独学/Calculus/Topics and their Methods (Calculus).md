## Topics and their Methods

1. **Differentiate Functions** (5/5 occurrences)
	- Differentiate with power, chain, and quotient rules.
	- Usually question 1.
2. **Calculate Limits** (5/5 occurrences)
	- Either by using L'Hôptial's Rule, or by multiplying through by a negative exponentiated variable to find an expression with a limit of $\frac{1}{\infty}$, thus tending to $0$.
	- Usually question 1.
3. **Identify Features of a Function** (4/5 occurrences)
	- Finds the axis intercepts by setting $x,y=0$, individually; finding asymptotes by exploring behaviour tending towards extremes (vertical: denominator is zero as the function is undefined, horizontal: $x\to\pm\infty$); concavity based on the polarity of a second derivative ($f^{\prime\prime}>0$ concave up, $f^{\prime\prime}<0$ concave down); extrema with differentiation and setting equal to zero; increasing/decreasing functions ($f^{\prime}>0$ increasing, $f^{\prime}<0$ decreasing); sketching by combining all of this information.
	- Usually question 1.
4. **Evaluate Definite Integrals** (5/5 occurrences)
	- Often have to deduce a $u$-substitution to simplify the evaluation, occasionally one is given - e.g. something trigonometric, like the double angle identities. Remember to state use of the Fundamental Theorem of Calculus (F.T.C) when evaluating limits.
	- Usually question 1; unless an unusual area, then usually question 3 or 4.
5. **Evaluate Double Definite Integrals** (5/5 occurrences)
	- Simple integration, done twice: often often given limits, occasionally need to find them after a simple sketch of a the region bounds.
	- Usually question 2.
6. **Find Classified Stationary Points of a Function in x, y** (4/5 occurrences)
	- Occur where $\frac{\partial f}{\partial x}=0$ and $\frac{\partial f}{\partial y}=0$. To classify these points, we can use the discriminant $D=f_{xx}f_{yy}-(f_{xy})^{2}$, where if $D>0$ then the stationary point is a local min/max (former if $f_{xx}>0$, latter if $f_{xx}<0$), a saddle point if $D<0$, and inconclusive if $D=0$.
	- Usually question 1 or 2.
7. **Relate Parametric Equations** (2/5 occurrences)
	- Often using $\sin^{2}t+\cos^{2}t\equiv1$, or simple solving a substitution.
	- Usually question 3 or 4.
8. **Differentiate Parametric Equations** (4/5 occurrences)
	- Either use a Cartesian conversion, or differentiate both parametric equations and use the chain rule to combine them into $\frac{dy}{dx}$.
	- Usually question 2 or 3.
9. **Convert Polar Form to Cartesian** (3/5 occurrences)
	- Use the identities $r^{2}=x^{2}+y^{2}$ and $x=r\cos\theta$, $y=r\sin\theta$.
	- Usually question 1, 2, or 3.
10. **Find the Volume Under a Plane** (3/5 occurrences)
	- Integrate the function $z=f(x,y)$, with the inner integral in terms of $y$ between functions of $x$, and the outer integral between two real numbers in terms of $x$.
	- Usually question 2.
11. **Standardise Complex Numbers** (5/5 occurrences)
	- Either simply convert between forms using fundamentals such as $r=\sqrt{a^{2}+b^{2}}$ and $\theta=\arctan(\frac{b}{a})$, where $z=a+bi$, or multiply by conjugates, etc. Remember that $i^{2}=-1$.
	- Usually question 3 or 4.
12. **Find Partial Derivatives** (5/5 occurrences)
	- Differentiate partially to one variable, or occasionally use the chain rule for parametric partial derivatives ($\frac{\partial z}{\partial s}=\frac{\partial z}{\partial x}\cdot\frac{\partial x}{\partial s}+\frac{\partial z}{\partial y}\cdot\frac{\partial y}{\partial s}$, or $\frac{\partial z}{\partial t}=\frac{\partial z}{\partial x}\cdot\frac{\partial x}{\partial t}+\frac{\partial z}{\partial y}\cdot\frac{\partial y}{\partial t}$). Remember mixed second derivatives (and that they're equal for continuous functions!)
	- Usually question 3 or 4.
13. **Estimate a Function with a Taylor Polynomial** (5/5 occurrences)
	- Using the formula $f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \frac{f'''(a)}{3!}(x - a)^3 + \cdots$, or simplified as $\sum_{n=0}^\infty\frac{f^n(a)}{n!}(x-a)^n$, determine the Taylor Polynomial to a suitable number of terms. This often done in a tabular manner. To find an upper error bound, calculate one extra term (the remainder term $R(x)$), where the value in the derivative is $c$, which we maximise.
	- Usually question 3.
14. **Find the Roots of a Complex Numbers** (2/5 occurrences)
	- Convert into exponential form using basic identities, ensuring that the angle is in the form $\theta+2k\pi$, then raise to the power of $\frac{1}{n}$ for the $n$th root. Simplify.
	- Usually question 3 or 4.
15. **Determine Odd/Even Functions** (1/5 occurrences)
	- A function is even if $f(-x)=f(x)$ (symmetric about the $y$-axis), and odd if $f(-x)=-f(x)$ (symmetric about the origin, rotationally). It is also possible to be neither odd nor even.
	- Usually question 4.
### Topics that haven't been tested yet

- Testing for Continuity.
	- $\lim_{x \to a} f(x) = f(a)$.
- Types of Discontinuity.
	- A **jump discontinuity** occurs when the function has two distinct limit values as it approaches from the left and the right of a certain point. In other words, the function 'jumps' from one value to another.
	- An **infinite discontinuity** occurs when the function approaches infinity as it nears a certain point.
	- A **removable discontinuity** is present when a function is not defined at a point, but the limit exists and is the same from both sides. By redefining the function at that point, the discontinuity can be 'removed.'
	- An **oscillating discontinuity** occurs when the function oscillates between different values as it approaches the discontinuous point.
- Logarithmic Differentiation.
	1. **Taking Logarithms**: Given a function $y = f(x)$, we take the natural logarithm of both sides: $\ln(y) = \ln(f(x))$.
	2. **Applying Properties of Logarithms**: Utilize the properties of logarithms to simplify the equation. For instance, $\ln(a \cdot b) = \ln(a) + \ln(b)$, and $\ln(a^b) = b \ln(a)$.
	3. **Differentiating**: Differentiate both sides with respect to $x$. Remember that $\frac{d}{dx}[\ln(y)] = \frac{1}{y} \frac{dy}{dx}$.
	4. **Solving for $\frac{dy}{dx}$**: Rearrange and solve for $\frac{dy}{dx}$.
- The Mean Value Theorem.
	- The Mean Value Theorem (MVT) extends Rolle's Theorem. It states that if a function $f(x)$ is continuous on a closed interval $[a, b]$ and differentiable on the open interval $(a, b)$, then there exists at least one $c$ in $(a, b)$ such that $f'(c) = \frac{f(b) - f(a)}{b - a}$.
- Slant Asymptotes.
	- These occur when the graph of a function approaches a line that is not horizontal as $x$ tends to infinity or negative infinity. They are common in rational functions where the degree of the numerator is one more than the degree of the denominator.
	- You can find it by performing the division such that the remainder is the equation of the asymptote.
- Linearisation.
	- $L(x) = f(a) + f'(a)(x - a)$
- Sandwich Theorem.
	- The theorem states that if you have three functions, $f(x)$, $g(x)$, and $h(x)$, and if $f(x) ≤ g(x) ≤ h(x)$ for all $x$ in some interval around a point $c$ (except possibly at $c$ itself), and if the limit as $x$ approaches $c$ of $f(x)$ and $h(x)$ are equal, then the limit of $g(x)$ as $x$ approaches $c$ must also be equal to this common limit.
	- Often used with trigonometric functions.
- Hyperbolic Functions.
	- **Hyperbolic Sine ($\sinh$)**: Defined as $\sinh x = \frac{e^x - e^{-x}}{2}$
	- **Hyperbolic Cosine ($\cosh$)**: Defined as $\cosh x = \frac{e^x + e^{-x}}{2}$
	- **Hyperbolic Tangent ($\tanh$)**: Defined as $\tanh x = \frac{\sinh x}{\cosh x}$
- Integration by Parts (recursive, reduction formulae).
	- **Integration by Parts:** Based on differentiation's product rule, for integrals involving products of functions.
		- Formula: $\int u \, dv = uv - \int v \, du$
		- Example: $\int x \cdot e^x \, dx$
	- $\int \sin^n(x) \, dx = -\frac{\sin^{n-1}(x) \cos(x)}{n} + \frac{n-1}{n} \int \sin^{n-2}(x) \, dx$
	- $\int \cos^n(x) \, dx = \frac{\cos^{n-1}(x) \sin(x)}{n} + \frac{n-1}{n} \int \cos^{n-2}(x) \, dx$
	- $\int \tan^n(x) \, dx = \frac{\tan^{n-1}(x)}{n-1} - \int \tan^{n-2}(x) \, dx$
	- etc. - you can also use the "DI method".
- Curve Length.
	- $L = \int_{a}^{b} \sqrt{1 + \left( \frac{dy}{dx} \right)^2} \, dx$
	- $L = \int_{a}^{b} \sqrt{\left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2} \, dt$
	- Derived from $\Delta s=\sqrt{(\Delta x)^2+(\Delta y)^2}$
- Cylindrical Polar Equations.
	- Conversion to Cartesian is the same as standard polar formulae, where $z=z$ is the only addition.

![[Pasted image 20240122103659.png]]