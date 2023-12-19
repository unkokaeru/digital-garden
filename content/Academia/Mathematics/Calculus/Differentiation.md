# Differentiation

**Definition**: Differentiation is a fundamental concept in calculus that deals with the rate at which a function changes. The derivative of a function gives us the slope of the tangent line to the curve of that function at any given point.

For example, the graph below ($y=f(x)$) is a continuous functions on the interval $[a,x]$ (in this case $a=1,x=4$), so the average rate of change of $y$ with respect to $x$ in the interval $[a,x]$ is $\frac{\Delta y}{\Delta x}=\frac{f(x)-f(a)}{x-a}$. This is the difference quotient and is used to define the derivative - usually using the limit definition.

```functionplot
---
title: 
xLabel: x
yLabel: f(x)
bounds: [1,4,0,10]
disableZoom: true
grid: false
---
f(x)=-((x-3)^2)+5
```

The limit definition of differentiation is foundational to understanding how the concept of the derivative is established in calculus. The derivative of a function at a point is defined as the limit of the average rate of change of the function over a small interval around that point as the interval's width approaches zero.

Given a function $f(x)$, the average rate of change of $f$ over the interval $[x, x + h]$ is the difference quotient:

$$\frac{f(x + h) - f(x)}{h}$$

As $h$ approaches zero, this average rate of change approaches the instantaneous rate of change of $f$ at $x$. This limit, if it exists, is the derivative of $f$ at $x$.

Formally, the derivative of $f$ with respect to $x$, denoted $f'(x)$ or $\frac{df}{dx}$, is given by:

$$f'(x) = \lim_{{h \to 0}} \frac{f(x + h) - f(x)}{h}$$

Provided the limit exists. In summation,
#### Formal Differentiability Definition
**Definition**: Suppose that $f(x)$ is defined on an interval $(a,b)$ containing the point $x_0$ (i.e. $a<x_0<b$). Then, $f(x)$ is differentiable at $x_0$ if and only if the following limit exists:
$$f'(x) = \lim_{{h \to 0}} \frac{f(x + h) - f(x)}{h}$$
$f(x)$ is a differentiable function if every point in its domain is differentiable by the above statement.
### Intuitive Explanation

Imagine you're walking along a curved path and you want to know how steep the path is at a particular point. One way to figure it out is to look at how much higher or lower you'd be if you took a small step forward (that's the difference in the function values) and divide it by the size of the step (that's $h$). This gives you an average slope over that small step. As you take smaller and smaller steps (making $h$ approach 0), you get a better and better idea of the slope exactly at the point you're standing on. The limit captures this idea: as $h$ gets infinitely small, the average slope becomes the instantaneous slope, which is the derivative.

### Example

To find the derivative of the function $f(x) = x^2$ at a general point $x$ using the limit definition:

$$f'(x) = \lim_{{h \to 0}} \frac{(x+h)^2 - x^2}{h}$$

Expanding and simplifying:

$$f'(x) = \lim_{{h \to 0}} \frac{x^2 + 2xh + h^2 - x^2}{h}$$
$$= \lim_{{h \to 0}} (2x + h)$$
$$= 2x$$

So, the derivative of $f(x) = x^2$ is $f'(x) = 2x$.

## Notation:

There are various ways to denote the derivative of a function, as shown above in practice, as well:

1. If $y = f(x)$, then the derivative is represented as $f'(x)$ or $\frac{dy}{dx}$.
2. For higher-order derivatives: $f''(x)$, $f'''(x)$, and $f^{(n)}(x)$ for the nth derivative.
3. The differential operator, $D$, can also be used: $Df(x)$.

## Basic Rules:

1. **Constant Rule**: The derivative of a constant is zero.
   
   $$ \frac{d}{dx} c = 0 $$

   where $c$ is a constant.

2. **Power Rule**: For any real number $n$,

   $$ \frac{d}{dx} x^n = nx^{n-1} $$

3. **Constant Multiple Rule**: If $c$ is a constant and $f(x)$ is a function, then

   $$ \frac{d}{dx} [c \cdot f(x)] = c \cdot \frac{d}{dx} f(x) $$

4. **Sum Rule**: If $f(x)$ and $g(x)$ are functions, then

   $$ \frac{d}{dx} [f(x) + g(x)] = \frac{d}{dx} f(x) + \frac{d}{dx} g(x) $$

5. **Product Rule**: For functions $f(x)$ and $g(x)$,

   $$ \frac{d}{dx} [f(x) \cdot g(x)] = f'(x)g(x) + f(x)g'(x) $$

6. **Quotient Rule**: For functions $f(x)$ and $g(x)$ where $g(x) \neq 0$,

   $$ \frac{d}{dx} \left( \frac{f(x)}{g(x)} \right) = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2} $$


## Logarithmic Differentiation
*Related to [[implicit differentiation]].*

Begin by writing $y=f(x)$, where $f(x)$ is the function to be differentiated. We then take natural logarithms of both sides, and simplify $\ln(f(x))$ using the [[laws of logarithms]]. Then, differentiate both sides of the equation with respect to $x$, then solving the resulting equation for $\frac{dy}{dx}$.

**Example:** Differentiate $\frac{x^2\sin x}{\cos 2x}$.
$$
y=\frac{x^2\sin x}{\cos 2x}\implies\ln y=\ln\left(\frac{x^2\sin x}{\cos 2x}\right)
$$
$$
\implies \ln y=2\ln x+\ln \sin x-\ln\cos2x
$$
$$
\implies\frac{d}{dx}\left(\ln y\right)=\frac{d}{dx}\left(2\ln x+\ln\sin x-\ln\cos2x\right)
$$
$$
\implies\frac{1}{y}\frac{dy}{dx}=\frac{2}{x}+\frac{\cos x}{\sin x}+2\frac{\sin 2x}{\cos 2x}
$$
$$
\implies\frac{dy}{dx}=\frac{2y}{x}+\cot x+2\tan2x:y=\frac{x^2\sin x}{\cos2x}
$$
$$
\therefore\frac{dy}{dx}=2\frac{x\sin x}{\cos2x}+\cot x+2\tan2x
$$
## Higher Order Derivatives
- For functions that require differentiation multiple times, we use notation like $f''(x)$ or $f^{(iv)}(x)$ to denote the second, third, fourth, etc., derivatives respectively.
## Basic Derivatives:

1. $\frac{d}{dx} x = 1$
2. $\frac{d}{dx} x^2 = 2x$
3. $\frac{d}{dx} \sqrt{x} = \frac{1}{2\sqrt{x}}$
4. $\frac{d}{dx} \ln(x) = \frac{1}{x}$
5. $\frac{d}{dx} e^x = e^x$
6. $\frac{d}{dx} \sin(x) = \cos(x)$
7. $\frac{d}{dx} \cos(x) = -\sin(x)$

## Applications:

1. **Tangents and Normals**: The derivative gives the slope of the tangent to the curve at a particular point. Thus, knowing the point and the slope, the equation of the tangent can be found.
2. **Motion**: In physics, the derivative of position with respect to time gives velocity, and the second derivative gives acceleration.
3. **Optimization Problems**: Differentiation can be used to find maximum or minimum values of functions.

## Challenges:

1. Differentiate the function $y = 3x^2 - 4x + 7$.
2. Using the Product Rule, differentiate $y = x^2 \sin(x)$.
3. Find the equation of the tangent line to the curve $y = x^2$ at the point $(1,1)$.

Remember, practice makes perfect! Regularly working on problems involving differentiation will help solidify your understanding.