# Differentials and Chain Rule

## Introduction
In calculus, differentials play a crucial role in understanding how functions change. The concept of a differential is intimately connected with derivatives, providing a framework to approximate changes in functions. The Chain Rule, a fundamental theorem in calculus, enables us to differentiate composite functions. It's an essential tool for dealing with complex functions constructed from simpler ones.

## Differentials
Differentials can be thought of as the "change" in a function due to a small change in its input. If $y = f(x)$, the differential of $y$, denoted as $dy$, is defined as:
$$dy = f'(x) \, dx$$
Here, $dx$ represents a small change in $x$, and $f'(x)$ is the derivative of $f$ with respect to $x$. The differential $dy$ approximates the change in $y$ due to the change $dx$ in $x$.

## Chain Rule
The Chain Rule is a formula to compute the derivative of a composite function. If a function $y$ is defined as $y = g(f(x))$, then the derivative of $y$ with respect to $x$ is given by:
$$\frac{dy}{dx} = \frac{dg}{df} \cdot \frac{df}{dx}$$
This rule is incredibly useful when dealing with functions where one function is nested inside another.

## Application
Consider a scenario where we have a temperature function $T$ that depends on time $t$, and time $t$ depends on another variable $s$. To find how $T$ changes with $s$, we use the Chain Rule:
$$\frac{dT}{ds} = \frac{dT}{dt} \cdot \frac{dt}{ds}$$

## Test Questions
1. If $y = (3x^2 + 2x)^5$, find $\frac{dy}{dx}$ using the Chain Rule.
2. Calculate the differential $dy$ for the function $y = \sin(x)$ when $dx = 0.1$.
3. Given $f(x) = \ln(x)$ and $g(x) = e^x$, find $\frac{d}{dx}g(f(x))$ using the Chain Rule.

---

This note provides a foundational understanding of differentials and the Chain Rule. Remember, practicing these concepts with various functions enhances comprehension and skill in calculus.