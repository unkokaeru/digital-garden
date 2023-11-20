# Composition of Functions

## Overview
In mathematics, the concept of the composition of functions (or function composition) is a fundamental operation. It involves applying one function to the results of another. This concept is essential in various branches of mathematics, including calculus, abstract algebra, and functional analysis.

### Definition
Given two functions $f: X \to Y$ and $g: Y \to Z$, the composition of $f$ and $g$ is written as $g \circ f$ and is defined as:
$$(g \circ f)(x) = g(f(x))$$
for all $x$ in $X$. In this composition, $f$ is first applied to $x$, and then $g$ is applied to the output of $f$.

### Properties
- **Associativity:** If $f, g,$ and $h$ are functions, then $h \circ (g \circ f) = (h \circ g) \circ f$.
- **Identity Function:** For any function $f: X \to Y$, the composition with the identity function $i_X: X \to X$ or $i_Y: Y \to Y$ is the same as $f$, i.e., $f \circ i_X = f$ and $i_Y \circ f = f$.

## Historical Context
The concept of function composition dates back to the origins of modern calculus in the 17th century. It was more rigorously formalized in the 19th century with the development of abstract algebra and set theory.

## Applications
- **Calculus:** In calculus, composition of functions is used in the chain rule for derivatives.
- **Computer Science:** Function composition is foundational in programming, particularly in functional programming languages.
- **Abstract Algebra:** In group theory, composition of functions (or operations) is a basic example of a binary operation.

## Examples

1. **Polynomial Composition:** If $f(x) = 2x + 3$ and $g(x) = x^2$, then $(g \circ f)(x) = (2x + 3)^2$.
2. **Trigonometric Composition:** For $f(x) = \sin(x)$ and $g(x) = x^2$, $(g \circ f)(x) = \sin^2(x)$.

## Test Questions
1. STARTI [Basic] Question: If $f(x) = x + 1$ and $g(x) = 3x$, what is $(g \circ f)(x)$? Back: $(g \circ f)(x) = 3(x + 1) = 3x + 3$. ENDI
2. STARTI [Basic] Question: What is the composition $(f \circ g)(x)$ for $f(x) = \sqrt{x}$ and $g(x) = 4x + 1$? Back: $(f \circ g)(x) = \sqrt{4x + 1}$. ENDI
3. STARTI [Basic] Question: Prove the associativity of function composition with functions $f, g,$ and $h$. Back: Demonstrate that $h \circ (g \circ f)(x) = (h \circ g) \circ f)(x)$ for all $x$ in the domain. ENDI