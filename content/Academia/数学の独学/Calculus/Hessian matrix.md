# Hessian Matrices

## Introduction

The Hessian matrix is a square matrix of second-order partial derivatives of a scalar-valued function. Named after Ludwig Otto Hesse and first used by him in 1857, it's a critical tool in multivariable calculus.

## Definition

For a function $f: \mathbb{R}^n \to \mathbb{R}$, the Hessian matrix $H$ at a point $\mathbf{x} \in \mathbb{R}^n$ is defined as:

$$ H(f)(\mathbf{x}) = 
\begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}
$$

## Applications

1. **Critical Points Analysis**: The Hessian can be used to determine the nature of critical points (local maxima, minima, or saddle points) of a function.
2. **Optimization**: In optimization, particularly quadratic programming, the Hessian matrix provides second-order information about the feasible region.
3. **Differential Geometry**: It's used to study the curvature of surfaces.

## Test Questions

1. STARTI [Basic] Question: What is the definition of a Hessian Matrix? Back: The Hessian matrix of a function is the square matrix of the function's second-order partial derivatives. ENDI
2. STARTI [Basic] Question: What role does the Hessian matrix play in determining the nature of critical points? Back: It helps determine whether a critical point is a local maximum, minimum, or a saddle point. ENDI
3. STARTI [Basic] Question: Name one field outside of calculus where Hessian matrices are used. Back: Differential Geometry, especially in studying the curvature of surfaces. ENDI

---

For further reading and examples, refer to the [[Multivariable Calculus]] and [[Differential Geometry]] notes.