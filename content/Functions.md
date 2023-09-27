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

### Graphs of $x^n$

Graphs of $y=x^n$ for even $n\ge 2$ have the general form below:
![[Even xn graph.excalidraw]]

For odd $n\ge3$, the graph of $y=x^n$ has the following general form:
![[Odd xn graph.excalidraw]]

### Rational Functions

Rational functions are functions that can be expressed as the ratio of two polynomial functions. In other words, a rational function is a function $f$ that can be written in the form:

$$f(x) = \frac{P(x)}{Q(x)}$$

where $P(x)$ and $Q(x)$ are polynomial functions, and $Q(x) \neq 0$. 

The domain of a rational function includes all real numbers except for the values that make the denominator $Q(x)$ equal to zero, because division by zero is undefined. The range of a rational function is all real numbers except any value $b$ for which there is no number $a$ such that $f(a) = b$.

Rational functions can often have graphs that contain holes, vertical asymptotes, or oblique asymptotes, depending on the degrees and coefficients of the polynomials $P(x)$ and $Q(x)$. 

Just like with polynomials, understanding the domain, the range, and the graph of a rational function is crucial to understanding its behaviour.

### Graphs of Rational Functions

The graph of a rational function typically contains one or more vertical asymptotes, corresponding to the zeros of the denominator $Q(x)$. It may also contain a horizontal or oblique asymptote, determined by the degrees of the polynomials $P(x)$ and $Q(x)$. 

In some cases, the graph may also contain holes, which are single points where the function is undefined. These occur when a factor in the denominator $Q(x)$ cancels out with a factor in the numerator $P(x)$.

Rational functions and their graphs are an important topic in calculus and real analysis, as they often exhibit complex behaviours not found in polynomial functions.

Take the function $y= x^{-n}$. For odd $n$, the top two quadrants of the graph diverge to positive infinity, whilst in the case where $n$ is even, the top right continues the same behaviour but the bottom right quadrant diverges to negative infinity.

These are examples of functions whose domain does not include the whole real line (because of $x=0$ and $y=0$): these are asymptotes. The domains are all real numbers (excluding $x=0$ and $y=0$ respectively), but the two respective ranges are: $(-\infty,0)\cup(0,\infty)$ and $(0,\infty)$.