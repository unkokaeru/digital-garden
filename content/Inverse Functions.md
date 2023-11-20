# Inverse Functions

## Introduction
Inverse functions are foundational in mathematics, particularly in algebra and calculus. They provide a way to 'undo' the action of a function. For example, if you have a function that adds 2 to any number, its inverse would subtract 2, returning you to your original number.

## Definition
A function $f: X \rightarrow Y$ has an inverse $f^{-1}$ if, for every element $y$ in the codomain $Y$, there is an element $x$ in the domain $X$ such that $f^{-1}(y) = x$. This implies that $f(f^{-1}(y)) = y$ and $f^{-1}(f(x)) = x$. The function $f$ must be bijective (both injective and surjective) to have an inverse.

## Examples
1. **Addition/Subtraction**: If $f(x) = x + 5$, then its inverse $f^{-1}(x) = x - 5$.
2. **Multiplication/Division**: For $f(x) = 3x$, the inverse is $f^{-1}(x) = \frac{x}{3}$.
3. **Exponential/Logarithmic Functions**: The inverse of $f(x) = e^x$ is $f^{-1}(x) = \ln(x)$.

## Properties
1. **Symmetry**: The graph of $f^{-1}$ is a reflection of the graph of $f$ across the line $y = x$.
2. **Composition**: $f(f^{-1}(x)) = x$ and $f^{-1}(f(x)) = x$.
3. **Domain and Range**: The domain of $f^{-1}$ is the range of $f$, and vice versa.

## Finding Inverse Functions
To find the inverse of a function:
1. Replace $f(x)$ with $y$.
2. Solve the equation for $x$ in terms of $y$.
3. Replace $y$ with $f^{-1}(x)$.

## Historical Context
The concept of inverse functions has been around since the introduction of functions themselves. It gained prominence with the development of calculus in the 17th century, especially in the work of mathematicians like Newton and Leibniz.

## Test Questions
1. **Basic**: Given $f(x) = 2x - 4$, find $f^{-1}(x)$.
   Back: $f^{-1}(x) = \frac{x + 4}{2}$.
2. **Intermediate**: Show that the inverse of $f(x) = \frac{1}{x}$ is itself.
   Back: Replacing $f(x)$ with $y$, we get $y = \frac{1}{x}$. Solving for $x$ gives $x = \frac{1}{y}$, so $f^{-1}(x) = \frac{1}{x}$, which is $f(x)$.
3. **Advanced**: Prove that the function $f(x) = x^3$ has an inverse.
   Back: $f(x) = x^3$ is a bijective function (both injective and surjective) since every $y$ value has a unique $x$ value. Therefore, it has an inverse, which is $f^{-1}(x) = \sqrt[3]{x}$.

[[Algebra]] | [[Calculus]]