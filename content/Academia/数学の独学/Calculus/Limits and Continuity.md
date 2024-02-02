## Limits and Undefined Functions: Bridging Gaps in Mathematics

In calculus, the concept of a limit is fundamental. It describes the behaviour of a function as its input approaches a particular value.

- For instance, the function $f(x) = \frac{1}{x}$ is undefined at $x = 0$. However, we can still explore its behaviour as $x$ approaches 0 using limits.
- Another example of this is a sinc function: $y=\frac{\sin x}{x}$, used often in technology industries.

It is defined by supposing that $f(x)$ is defined on an open interval that contains the number $a$, except possibly at $a$ itself. Then, we say that the limit of $f(x)$ as $x$ approaches $a$ is $L$, and we write:
$$
\lim_{x\rightarrow a}f(x)=L
$$
if, for every $\epsilon>0$, there exists a $\delta>0$ such that, if $0<|x-a|<\delta$, then $|f(x)-L|<\epsilon$.

*This definition is needed in rigorous proofs, as it uses variables rather than statements.*
### Behaviour of Functions at Infinity: Exploring the Unbounded

Studying how functions behave as their inputs grow without bound (tend towards infinity) provides insights into their overall nature and characteristics.

- For example, if a function $f(x)$ tends to a finite value as $x$ becomes infinite, it indicates that the function levels off or stabilizes as $x$ grows.

### Rules of Limits
Limits form a foundational concept in calculus, and understanding the rules governing them is crucial for delving deeper into the subject. Here are the primary rules and properties of limits:

1. **Constant Rule**: 
   If $c$ is a constant, then:
   $$\lim_{x \to a} c = c$$

2. **Identity Rule**: 
   $$\lim_{x \to a} x = a$$

3. **Sum/Difference Rule**: 
   If the limits of $f(x)$ and $g(x)$ exist, then:
   $$\lim_{x \to a} [f(x) \pm g(x)] = \lim_{x \to a} f(x) \pm \lim_{x \to a} g(x)$$

4. **Product Rule**: 
   If the limits of $f(x)$ and $g(x)$ exist, then:
   $$\lim_{x \to a} [f(x) \cdot g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)$$

5. **Quotient Rule**: 
   If the limits of $f(x)$ and $g(x)$ exist and $\lim_{x \to a} g(x) \neq 0$, then:
   $$\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}$$

6. **Power Rule**: 
   If $n$ is a positive integer and the limit of $f(x)$ exists, then:
   $$\lim_{x \to a} [f(x)]^n = [\lim_{x \to a} f(x)]^n$$

7. **Root Rule**: 
   If $n$ is a positive integer and the limit of $f(x)$ exists, then:
   $$\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to a} f(x)}$$
   provided the values are real.

8. **Squeeze (or Sandwich) Theorem**: 
   If $f(x) \leq g(x) \leq h(x)$ for all $x$ in some open interval containing $a$ (except possibly at $a$), and:
   $$\lim_{x \to a} f(x) = \lim_{x \to a} h(x) = L$$
   then:
   $$\lim_{x \to a} g(x) = L$$

9. **Limit of a Composite Function (Chain Rule)**: 
   If $g(x)$ approaches a limit $L$ as $x$ approaches $a$, and $f(u)$ has a limit as $u$ approaches $L$, then:
   $$\lim_{x \to a} f(g(x)) = \lim_{u \to L} f(u)$$
   provided $g(x) \neq L$ for all $x$ near $a$.

10. **Limits Involving Infinity**: 
   - If $f(x)$ becomes arbitrarily large as $x$ approaches $a$, then:
     $$\lim_{x \to a} f(x) = \infty$$
   - If $f(x)$ becomes arbitrarily large in the negative sense as $x$ approaches $a$, then:
     $$\lim_{x \to a} f(x) = -\infty$$

11. **Limits at Infinity**: 
   If $f(x)$ approaches a constant $L$ as $x$ becomes infinitely large, then:
   $$\lim_{x \to \infty} f(x) = L$$

These rules provide a framework for evaluating limits in various scenarios. They are essential for understanding more advanced topics in calculus, such as derivatives and integrals.

# Continuity in Mathematics

Continuity is a foundational concept in mathematics. Essentially, it ensures that functions behave predictably without any "breaks" or "jumps". Let's delve deeper with definitions and examples.

## Intuitive Idea

Consider sketching a function's graph without pausing your pen. If you manage to do so without any stops, the function is continuous. But if you must pause (due to a gap or jump), then the function has a discontinuity.

## Formal Definition

A function $f: \mathbb{R} \to \mathbb{R}$ is said to be continuous at a point $c$ if:

1. $f(c)$ is defined.
2. The limit of $f$ as $x$ approaches $c$ exists.
3. $\lim_{x \to c} f(x) = f(c)$

Expressed using limits:
$$ \lim_{x \to c} f(x) = f(c) $$

If $f$ meets these criteria for all points in its domain, it's continuous over its domain.

## Detailed Examples

1. **Function**: $f(x) = x^2$
   * This function is continuous over all real numbers because for every $x$ in $\mathbb{R}$, the function value and limit as $x$ approaches any point are the same.

2. **Function**: $g(x) = \frac{1}{x}$
   * This function is discontinuous at $x = 0$. As $x$ approaches 0 from the left, $g(x)$ approaches negative infinity, and from the right, it approaches positive infinity. Hence, the limit does not exist at $x = 0$.

## Types of Discontinuities with Examples

1. **Removable Discontinuity**: 
   * **Example**: $f(x) = \frac{x^2 - 1}{x - 1}$
   * At $x = 1$, the function isn't defined because of the denominator. However, by factoring the numerator, we get $f(x) = x + 1$ which is continuous, making the discontinuity at $x = 1$ removable.

2. **Jump Discontinuity**:
   * **Example**: The Heaviside step function, defined as:
     $$ H(x) = \begin{cases} 
        0 & \text{if } x < 0 \\
        1 & \text{if } x \geq 0 
        \end{cases} $$
   * This function jumps from 0 to 1 at $x = 0$, hence the name.

3. **Infinite Discontinuity**:
   * **Example**: $g(x) = \frac{1}{x}$
   * As mentioned earlier, $g(x)$ approaches infinity (from both directions) as $x$ gets closer to 0.

4. **Oscillating Discontinuity**:
   * **Example**: $h(x) = \sin\left(\frac{1}{x}\right)$ for $x \neq 0$.
   * As $x$ approaches 0, the function oscillates infinitely, making it hard to predict its behaviour at $x = 0$.

## Continuity in Calculus

Continuity's importance extends to calculus. For example, the Fundamental Theorem of Calculus requires the integrand to be continuous over the interval of integration. When you start differentiating or integrating, ensuring continuity (or understanding its absence) is crucial.

---
## Continuity of Composite Functions

When you compose two functions, their individual continuities influence the continuity of the resulting composite function. Let's explore this.

## Definition

Given two functions, $f$ and $g$, their composite function is defined as:
$$(f \circ g)(x) = f(g(x))$$

For $f \circ g$ to be continuous at a point $x = c$, $g$ must be continuous at $c$ and $f$ must be continuous at $g(c)$.

## Examples

1. **Function**: 
   * $f(x) = x^2$ 
   * $g(x) = \sin(x)$
   
   Here, both $f$ and $g$ are continuous everywhere. Their composite function $f(g(x)) = \sin^2(x)$ is also continuous everywhere.

2. **Function**:
   * $f(x) = \frac{1}{x}$ 
   * $g(x) = x + 1$

   While $g$ is continuous everywhere, $f$ has a discontinuity at $x = 0$. However, since $g(c) \neq 0$ for any $c$, the composition $f(g(x)) = \frac{1}{x + 1}$ is continuous everywhere.

3. **Function**:
   * $f(x) = \sqrt{x}$ 
   * $g(x) = x - 2$

   $g$ is continuous everywhere, but $f$ is only continuous for $x \geq 0$. When composing them, $f(g(x)) = \sqrt{x - 2}$, the resulting function is continuous for $x \geq 2$.

## Points to Remember

- If both functions are continuous at a point, their composite function is usually continuous at that point. However, always check the continuity of the inner function at that point and the continuity of the outer function at the value given by the inner function.
  
- Discontinuities in the outer function can be introduced by the inner function, especially if the inner function's range includes points where the outer function is not defined or not continuous.

*As always, visualizing or sketching these functions can provide deeper insights.*

---
# The Intermediate Value Theorem (IVT)

The Intermediate Value Theorem is a fundamental result in calculus related to continuous functions. It provides an assurance about the behaviour of continuous functions over a closed interval.

## Statement of IVT

Let $f$ be a function that is continuous on the closed interval \([a, b]\). If $k$ is any value between $f(a)$ and $f(b)$ (exclusive), then there exists at least one $c$ in the open interval \((a, b)\) such that $f(c) = k$.

In simpler terms, if you have a continuous function that starts below a value $k$ and ends above $k$ (or vice versa) on an interval, then the function must take on the value $k$ somewhere in that interval.

## Visual Interpretation

Imagine drawing the graph of a continuous function over an interval without lifting your pen. If one end of the interval is below the horizontal line $y = k$ and the other end is above it, your pen must cross the line $y = k$ at some point in the interval.

## Examples

1. **Function**: 
   * $f(x) = x^3 - x$
   
   On the interval \([-1, 1]\), $f(-1) = -2$ and $f(1) = 0$. If you pick any value between -2 and 0, say $k = -1$, by IVT, there exists some $c$ in the interval \([-1, 1]\) such that $f(c) = -1$.

2. **Function**:
   * $g(x) = \sin(x)$
   
   Over the interval \([0, \pi]\), $g(0) = 0$ and $g(\pi) = 0$. But for any $k$ value between 0 (exclusive) and 1, IVT guarantees a $c$ in the interval where $g(c) = k$.

## Importance

The IVT is especially useful in root-finding algorithms. If we know that a continuous function changes sign over an interval, then by the IVT, the function has a root in that interval. Algorithms like the bisection method utilize this property to approximate roots.

---

With the Intermediate Value Theorem, one understands that continuous functions exhibit predictable behaviours, making them amenable to various mathematical and computational techniques. It's a foundational tool in analysis and calculus, linking continuity and the behaviour of functions over intervals.