# Properties of the Definite Integral and Fundamental Theorem of Calculus

## Introduction
Definite integrals are a cornerstone in calculus, representing the accumulation of quantities and areas under curves. The Fundamental Theorem of Calculus (FTC) bridges the concepts of differentiation and integration, revealing a profound connection between them. This note explores the properties of the definite integral and the FTC, providing a comprehensive understanding of these concepts.

## Properties of the Definite Integral
The definite integral of a function $f(x)$ over an interval $[a, b]$ is denoted by $\int_{a}^{b} f(x) \, dx$. It has several key properties:

1. **Additivity over Intervals**: 
   $\int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx = \int_{a}^{b} f(x) \, dx$ for any $c$ between $a$ and $b$.

2. **Zero Width Interval**: 
   $\int_{a}^{a} f(x) \, dx = 0$.

3. **Reversal of Limits**: 
   $\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx$.

4. **Linearity**:
   $\int_{a}^{b} [cf(x) + dg(x)] \, dx = c\int_{a}^{b} f(x) \, dx + d\int_{a}^{b} g(x) \, dx$, where $c$ and $d$ are constants.

## Fundamental Theorem of Calculus
The FTC is divided into two parts:

1. **FTC Part I**: 
   If $f$ is continuous on $[a, b]$ and $F$ is an antiderivative of $f$ on $[a, b]$, then $\int_{a}^{b} f(x) \, dx = F(b) - F(a)$.

2. **FTC Part II**: 
   If $f$ is continuous on $[a, b]$, then the function $g(x) = \int_{a}^{x} f(t) \, dt$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $g'(x) = f(x)$.

## Applications and Historical Context
The FTC not only simplifies the computation of definite integrals but also signifies a major development in mathematical analysis. It was independently discovered by Isaac Newton and Gottfried Wilhelm Leibniz in the late 17th century, laying the groundwork for modern calculus.

## Test Questions

1. **STARTI [Basic] Question:** Calculate $\int_{0}^{2} x^2 \, dx$ using the FTC. **Back:** Let $F(x) = \frac{1}{3}x^3$ be an antiderivative of $f(x) = x^2$. Then, $\int_{0}^{2} x^2 \, dx = F(2) - F(0) = \frac{8}{3}$. ENDI

2. **STARTI [Basic] Question:** Show that $\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx$. **Back:** Let $G(x)$ be an antiderivative of $f(x)$. Then, $\int_{a}^{b} f(x) \, dx = G(b) - G(a)$ and $\int_{b}^{a} f(x) \, dx = G(a) - G(b)$. Thus, $\int_{a}^{b} f(x) \, dx = -(G(a) - G(b)) = -\int_{b}^{a} f(x) \, dx$. ENDI

3. **STARTI [Basic] Question:** Explain the significance of the FTC in calculus. **Back:** The FTC links the concept of integration with differentiation. It shows that the accumulation process (integration) is the inverse of the rate of change (differentiation). This duality is fundamental to many areas of mathematics and physics. ENDI

---

For a deeper exploration, consider linking this note to related topics such as [[Differential Calculus]], [[Antiderivatives]], and [[Applications of Integration]] in your Obsidian vault.