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