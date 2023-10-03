# Functions and Their Graphs

A **function** is a mathematical rule that transforms an element from one set into an element of another set. Specifically, a function $f$ from a set $X$ to a set $Y$ assigns a unique element $y \in Y$ to each element $x \in X$.
## Domain and Range

The **domain** $X$ of a function is the set of all possible input values, i.e., the values to which the function can be applied. The **range** of a function is the set of all possible output values, i.e., the values generated as $x$ varies through the domain.

For example, the function $y = \sqrt{x}$ has a domain of $[0, \infty)$ and also a range of $[0, \infty)$ in [[interval]] notation.

However, the domain and range of a function can be different. For instance, the function $y = \sqrt{10 - x}$ has a domain of $(-\infty, 10]$ and a range of $[0, \infty)$.

Understanding the domain, the range, and the graph of a function is crucial to understanding the behaviour of a [[continuous function]].

## Graphs of Functions

A function can be visualised using a **graph**, the set of all Cartesian coordinates where $x$ is in the domain $X$ and $y = f(x)$.

Recall the definition of a function - this definition can be tested on graphs using a vertical line test.
### Vertical Line Test

The below graph is a function as the three vertical lines passing through the graph only intersect once each: so it is a function.

![[GraphPassingVerticalLineTest.excalidraw]]

The next graph however, the vertical line passes through the graph twice: so it is not a function.

![[GraphFailingVerticalLineTest.excalidraw]]

This is similar with the equation of a circle, both of which can be fixed by splitting it into two functions, for example with a circle: $x^2+y^2=r^2\implies y=\sqrt{r^2-x^2},y=-\sqrt{r^2-x^2}$.

### Polynomial functions

A polynomial in $x$ of degree $n$ has the form $f(x)=a_n x^n + \ldots + a_2 x^2 + a_1 x + a_0$.  Alternative (sigma) notation is as follows: 
$$f(x) = \sum_{i=0}^{n} a_i x^i$$
where the quantities $a_i$ are constant coefficients where $a_n \ne 0$. The domain of a polynomial expressed in this way is always $\mathbb{R}$, because there are only integer powers of $x$ - thus no risk of square rooting a negative number (leading the range outside of the real plane). There are also no negative powers of $x$, so there is no risk of division by zero.

#### Graphs of $x^n$

Graphs of $y=x^n$ for even $n\ge 2$ have the general form below:
![[Even xn graph.excalidraw]]

For odd $n\ge3$, the graph of $y=x^n$ has the following general form:
![[Odd xn graph.excalidraw]]

#### Rational Functions

Rational functions are functions that can be expressed as the ratio of two polynomial functions. In other words, a rational function is a function $f$ that can be written in the form:

$$f(x) = \frac{P(x)}{Q(x)}$$

where $P(x)$ and $Q(x)$ are polynomial functions, and $Q(x) \neq 0$. 

The domain of a rational function includes all real numbers except for the values that make the denominator $Q(x)$ equal to zero, because division by zero is undefined. The range of a rational function is all real numbers except any value $b$ for which there is no number $a$ such that $f(a) = b$.

Rational functions can often have graphs that contain holes, vertical asymptotes, or oblique asymptotes, depending on the degrees and coefficients of the polynomials $P(x)$ and $Q(x)$. 

Just like with polynomials, understanding the domain, the range, and the graph of a rational function is crucial to understanding its behaviour.

##### Graphs of Rational Functions

The graph of a rational function typically contains one or more vertical asymptotes, corresponding to the zeros of the denominator $Q(x)$. It may also contain a horizontal or oblique asymptote, determined by the degrees of the polynomials $P(x)$ and $Q(x)$. 

In some cases, the graph may also contain holes, which are single points where the function is undefined. These occur when a factor in the denominator $Q(x)$ cancels out with a factor in the numerator $P(x)$.

Rational functions and their graphs are an important topic in calculus and real analysis, as they often exhibit complex behaviours not found in polynomial functions.

Take the function $y= x^{-n}$. For odd $n$, the top two quadrants of the graph diverge to positive infinity, whilst in the case where $n$ is even, the top right continues the same behaviour but the bottom right quadrant diverges to negative infinity.

These are examples of functions whose domain does not include the whole real line (because of $x=0$ and $y=0$): these are asymptotes. The domains are all real numbers (excluding $x=0$ and $y=0$ respectively), but the two respective ranges are: $(-\infty,0)\cup(0,\infty)$ and $(0,\infty)$.

**Example (Exam 2020)** Write down the domain and range of $f(x)=(x-3)^{-4}$.

The domain is restricted by division by zero at $x=3$, so $x=3$ is excluded from the domain: $\{x\space\epsilon\space\mathbb{R}:x\ne3\} = (-\infty,3)\cup(3,\infty)$.

The range produces arbitrarily small numbers as $x$ approaches $\pm\infty$ and arbitrarily large numbers as $x$ approaches $3$. The power is even, so these numbers are positive thus the range is $\{x\space\epsilon\space\mathbb{R}:x\gt0\}=(0,\infty)$.

### Periodic functions

A function is periodic if there is a number, $p\gt0 : f(x+p)=f(x)$, for all $x$ in the domain of $f$.
The smallest such number is called the period of $f$.
#### Trigonometry functions

The basic functions are $\sin$ and $\cos$. These are $\frac{\pi}{2}$ out of phase, but are otherwise identical. Both also have the domain $(-\infty,\infty)$ and range $[-1,1]$.

They are defined by the following power series:
$$
\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \ldots
$$
$$
\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \ldots
$$
The quotient of these two is defined as $\tan x = \frac{\sin x}{\cos x}$. As it's a rational function, it's undefined at some points, when $\cos x = 0$, i.e. $x=(n+\frac{1}{2})\pi, n\space\epsilon\space\mathbb{z}$. Thus its domain is defined as $\{x\space\epsilon\space\mathbb{R}:x\ne(n+\frac{1}{2})\pi,n\space\epsilon\space\mathbb{z}\}$. Its range is in all the real numbers, $y\space\epsilon\space\mathbb{R}$.

**Example** Sketch the graph of $\csc x = \frac{1}{\sin x}$ *(cosec x is the British version of csc x)*, and state its domain and range.
![[Csc graph.excalidraw]]
Domain : $\{x\space\epsilon\space\mathbb{R}:x\ne n\pi,n\space\epsilon\space\mathbb{Z}\}$
Range : $\{y\space\epsilon\space\mathbb{R}:y\le-1\space\text{or}\space y\ge1\}$ or $(-\infty,-1]\cup[1,\infty)$

## Even & Odd Functions

An even function has reflective symmetry: $f(-x)=f(x)$, for all $x$ in the domain of $f$.
![[Even f(x).excalidraw]]

An odd function has rotational symmetry: $f(-x)=f(x)$ for all $x$ in the domain of $f$.
![[Odd f(x).exalidraw]]

To identify a function as odd, even, or neither: replace every instance of $x$ with $-x$, if the original is returned then $f$ is even, if the negative of $f$ is returned then $f$ is odd. If neither occurs, then the function is neither even nor odd.

**Example** Identify $g(x)$ as odd or even or neither, where $g(x)=2x^3+x$.
$$
\implies g(-x) = 2(-x)^3+(-x)
\implies g(-x) = -2x^3-x=-g(x)
$$
Thus the function is odd.
## Exponential Functions

Exponential functions are functions in which the variable is in the exponent. The general form of an exponential function is:
$$f(x) = a \cdot b^x$$
where $a$ and $b$ are constants, and $b > 0$.

### Historical Background

Exponential functions have been studied since ancient times. The concept of an exponential function was first introduced by the Swiss mathematician Johann Bernoulli in the 17th century. The exponential function and its inverse, the logarithm, have been fundamental in the development of mathematics, especially in calculus and complex analysis.

### Equations and Properties

The base $b$ of the exponential function determines its behaviour:

- If $0 < b < 1$, the function is decreasing.
- If $b > 1$, the function is increasing.

The domain of an exponential function is all real numbers $\mathbb{R}$, and its range is all positive real numbers $(0, \infty)$.

### Examples

1. $f(x) = 2^x$
   - Domain: $\mathbb{R}$
   - Range: $(0, \infty)$

2. $f(x) = \frac{1}{3}^x$
   - Domain: $\mathbb{R}$
   - Range: $(0, \infty)$

## Piece-wise Defined Functions

Piece-wise defined functions are functions that are defined by different formulas over different intervals of their domain.

### Absolute Value Function

The absolute value function is defined as:
$$f(x) = |x| = 
\begin{cases} 
x & \text{if } x \geq 0 \\
-x & \text{if } x < 0 
\end{cases}$$

- Domain: $\mathbb{R}$
- Range: $[0, \infty)$

### Signum Function

The signum function, often denoted as $sgn(x)$, is defined as:
$$sgn(x) = 
\begin{cases} 
1 & \text{if } x > 0 \\
0 & \text{if } x = 0 \\
-1 & \text{if } x < 0 
\end{cases}$$

- Domain: $\mathbb{R}$
- Range: \{-1, 0, 1\}

## Hyperbolic Functions

Hyperbolic functions are analogs of the trigonometric functions for the hyperbola, just as the trigonometric functions are for the circle.

### Definitions

1. Hyperbolic Sine: $\sinh(x) = \frac{e^x - e^{-x}}{2}$
2. Hyperbolic Cosine: $\cosh(x) = \frac{e^x + e^{-x}}{2}$
3. Hyperbolic Tangent: $\tanh(x) = \frac{\sinh(x)}{\cosh(x)}$

### Properties

- $\cosh^2(x) - \sinh^2(x) = 1$
- The domain of $\sinh(x)$ and $\cosh(x)$ is $\mathbb{R}$, and their range is also $\mathbb{R}$.
- The domain of $\tanh(x)$ is $\mathbb{R}$, and its range is (-1, 1).

## Composition of Two Functions

Given two functions $f$ and $g$, the composition of $f$ with $g$ is defined as:
$$(f \circ g)(x) = f(g(x))$$

### Example

Let $f(x) = x^2$ and $g(x) = 3x + 1$. Then:
$$(f \circ g)(x) = f(3x + 1) = (3x + 1)^2$$

### Properties

- The domain of $f \circ g$ is the set of all $x$ in the domain of $g$ such that $g(x)$ is in the domain of $f$.
- The range of $f \circ g$ is the range of $f$.

In conclusion, understanding the various types of functions and their properties is crucial for a deeper understanding of mathematics. Whether it's the simple polynomial or the more complex hyperbolic functions, each has its unique characteristics and applications.