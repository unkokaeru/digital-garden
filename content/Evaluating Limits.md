# Evaluating Limits

**Overview:** 
Evaluating limits is a fundamental concept in calculus that deals with finding the value that a function approaches as the input approaches a certain point. This concept is crucial in understanding the behaviour of functions, especially near points of discontinuity or at infinity.

## 1. Direct Substitution
**Definition:** 
Direct substitution involves plugging the point of interest directly into the function, provided the function is continuous at that point.

**Example:**
Consider $\lim_{x \to 3} (2x + 1)$. 
Direct substitution yields $2 \cdot 3 + 1 = 7$.

## 2. Indeterminate Forms
**Definition:** 
An indeterminate form arises when the limit yields an expression like $\frac{0}{0}$ or $\frac{\infty}{\infty}$, which does not have a clear value.

**Example:**
$\lim_{x \to 0} \frac{\sin x}{x}$ results in the indeterminate form $\frac{0}{0}$.

## 3. L'Hôpital's Rule
**Definition:** 
L'Hôpital's Rule is used to evaluate limits involving indeterminate forms. It states that if the limit yields an indeterminate form $\frac{0}{0}$ or $\frac{\infty}{\infty}$, the limit can be computed by taking the derivative of the numerator and denominator separately.

[[Derivation of L'Hôpital's Rule]]

**Example:**
For $\lim_{x \to 0} \frac{\sin x}{x}$, applying L'Hôpital's Rule gives $\lim_{x \to 0} \frac{\cos x}{1}$, which evaluates to 1.

## Historical Context
The concept of limits was formalized in the 17th century, contributing significantly to the development of calculus. L'Hôpital, a French mathematician, published the first known text containing these rules, although the Scottish mathematician John Bernoulli may have discovered them independently.

## Test Questions
1. Evaluate $\lim_{x \to 2} (3x^2 - 2x + 4)$ using direct substitution.
2. Determine if $\lim_{x \to \infty} \frac{x^2 - 1}{x^2 + 1}$ is an indeterminate form and evaluate it.
3. Use L'Hôpital's Rule to find $\lim_{x \to 0} \frac{e^x - 1}{x}$. 