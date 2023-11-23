# Rules for Differentiation

Differentiation is a fundamental concept in calculus, focusing on finding the rate at which a function changes at any given point. In undergraduate mathematics, understanding the rules of differentiation is crucial for solving complex problems. Here, we will explore these rules, with historical context and practical examples.

### Historical Context

Differentiation, as part of calculus, was developed independently in the late 17th century by Isaac Newton and Gottfried Wilhelm Leibniz. While their notation and approach differed, the essence of their findings laid the foundation for modern calculus.

### Basic Rules of Differentiation

1. **Power Rule**  
   $$\frac{d}{dx}[x^n] = nx^{n-1}$$  
   Where $n$ is any real number.

2. **Constant Rule**  
   $$\frac{d}{dx}[c] = 0$$  
   Where $c$ is a constant.

3. **Constant Multiple Rule**  
   $$\frac{d}{dx}[cf(x)] = c \cdot \frac{d}{dx}[f(x)]$$  
   Where $c$ is a constant.

4. **Sum Rule**  
   $$\frac{d}{dx}[f(x) + g(x)] = \frac{d}{dx}[f(x)] + \frac{d}{dx}[g(x)]$$

5. **Difference Rule**  
   $$\frac{d}{dx}[f(x) - g(x)] = \frac{d}{dx}[f(x)] - \frac{d}{dx}[g(x)]$$

6. **Product Rule**  
   $$\frac{d}{dx}[f(x) \cdot g(x)] = f(x) \cdot \frac{d}{dx}[g(x)] + g(x) \cdot \frac{d}{dx}[f(x)]$$

7. **Quotient Rule**  
   $$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{g(x) \cdot \frac{d}{dx}[f(x)] - f(x) \cdot \frac{d}{dx}[g(x)]}{[g(x)]^2}$$

8. **Chain Rule**  
   $$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$$

### Examples

1. **Power Rule Example**  
   If $f(x) = x^3$, then $\frac{d}{dx}f(x) = 3x^2$.

2. **Product Rule Example**  
   For $f(x) = x^2$ and $g(x) = x+1$, $\frac{d}{dx}[f(x)g(x)] = x^2 + 2x(x+1)$.

3. **Chain Rule Example**  
   Given $f(x) = (3x+1)^2$, $\frac{d}{dx}f(x) = 2(3x+1) \cdot 3$.

### Test Questions

1. **STARTI [Basic] Question:** Use the power rule to differentiate $f(x) = x^5$. Back: $\frac{d}{dx}f(x) = 5x^4$. ENDI
2. **STARTI [Basic] Question:** Apply the product rule to differentiate $f(x) = x^2 \cdot \ln(x)$. Back: $\frac{d}{dx}f(x) = 2x \cdot \ln(x) + x$. ENDI
3. **STARTI [Basic] Question:** Use the chain rule to differentiate $f(x) = \sqrt{4x+1}$. Back: $\frac{d}{dx}f(x) = \frac{1}{2\sqrt{4x+1}} \cdot 4$. ENDI