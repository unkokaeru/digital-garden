Graph sketching is an essential skill in mathematics and engineering that allows us to visualize functions and their properties. We'll go through some key topics you need to understand to become adept at graph sketching.

## Inverse Functions & Their Graphs

### Basic Idea
Inverse functions "reverse" the operation of the original function. For a function $f$ and its inverse $f^{-1}$:

$$
f(f^{-1}(x)) = x \quad \text{and} \quad f^{-1}(f(x)) = x
$$

The graph of an inverse function is a reflection of the original function's graph across the line $y = x$.

### Inverse Hyperbolic Functions
Hyperbolic functions like $\sinh, \cosh, \tanh$ have their inverses, denoted as $\text{arsinh}, \text{arcosh}, \text{artanh}$:

$$
f(x) = \sinh(x) \Rightarrow f^{-1}(x) = \text{arsinh}(x)
$$

Understanding inverse functions will help you see how the graph of $f$ relates to $f^{-1}$, which is a key skill in sketching graphs.

## Critical Points of Functions

### The What and Why
Critical points are where a function has local minima, maxima, or saddle points. Specifically, a critical point occurs when the derivative $f'(x) = 0$ or is undefined.

$$
f'(x) = 0 \quad \text{or} \quad f'(x) \text{ is undefined}
$$

Knowing where these critical points are allows us to identify important features of the graph.

### Transition to Extreme Value Theorem
Now, once you have these critical points, the Extreme Value Theorem can often tell us more about them.

## The Extreme Value Theorem

### Gist of the Theorem
The Extreme Value Theorem states that if $f(x)$ is continuous on a closed interval $[a,b]$, then $f(x)$ attains both a global maximum and minimum. 

### Importance for Graph Sketching
When sketching a graph, it's valuable to know where these global extreme values occur, as they are key points on your graph. 

## Fermat's Theorem

### What It Says
Fermat's Theorem is more specific than the Extreme Value Theorem. It states that if $f(x)$ has a local extremum at $x = c$ and $f'(c)$ exists, then $f'(c) = 0$.

### Relevance to Graph Sketching
The theorem helps you pinpoint exactly where local maxima and minima can occur, thus refining your sketch further. Now, how do we identify whether it's a maxima or minima? That brings us to the concept of intervals of increase and decrease.

## Mean Value Theorem and Rolle's Theorem

### Mean Value Theorem: The Statement and Relevance

The Mean Value Theorem generalizes what Rolle's Theorem states. It posits that if $f(x)$ is continuous on the closed interval $[a, b]$ and differentiable on the open interval $(a, b)$, then there exists at least one $c$ in $(a, b)$ such that

$$
f'(c) = \frac{f(b) - f(a)}{b - a}
$$

In the context of graph sketching, this theorem tells us that somewhere between $a$ and $b$, the instantaneous rate of change $f'(c)$ equals the average rate of change $\frac{f(b) - f(a)}{b - a}$. This can be visually represented as a tangent line that is parallel to the secant line through $(a, f(a))$ and $(b, f(b))$.

### Rolle's Theorem: A Special Case

Rolle's Theorem is essentially the Mean Value Theorem with $f(a) = f(b)$. In this special case, the theorem simplifies to:

$$
f(a) = f(b) \Rightarrow \exists c \in (a, b) : f'(c) = 0
$$

It's almost as if Rolle's Theorem tells us that within a certain range where the function starts and ends at the same value, there's at least one spot where the function "pauses" (i.e., the tangent is horizontal).

### Combining the Two in Graph Sketching

Both theorems add rich detail to your graph. While the Mean Value Theorem assures you that a certain slope is achieved somewhere within the interval, Rolle's Theorem narrows this down to specific conditions under which the slope is zero. This makes it easier to identify features like local maxima, minima, and points of inflection, which are key to sketching a comprehensive graph.

These theorems not only help in sketching graphs but also deepen your understanding of how a function behaves over an interval. As such, they are invaluable tools for any mathematician.

## Intervals of Increase and Decrease

### How to Find Them
To find where the function is increasing or decreasing, first find the critical points by solving $f'(x) = 0$. Then, classify these points into intervals. In each interval, pick a test point to determine the sign of $f'(x)$.

### Why This Matters
Understanding where the function increases or decreases allows you to sketch the "hills" and "valleys" of the function, which is crucial for a detailed graph.

## Classifying Critical Points as Local Maxima or Local Minima

### Criteria
- **Local Maximum**: $f'(x) > 0$ before and $f'(x) < 0$ after the critical point
- **Local Minimum**: $f'(x) < 0$ before and $f'(x) > 0$ after the critical point

Understanding the type of extremum helps in making your graph more accurate.

## Concavity and Testing for It

### The Basics
A function is concave up where $f''(x) > 0$ and concave down where $f''(x) < 0$.

### Importance
Concavity gives the "direction" of the curve, letting you draw more than just lines connecting maxima and minima. This leads us to the concept of points of inflection.

## Points of Inflection

### Definition
A point where the concavity changes is called a point of inflection. Mathematically, this is where $f''(x)$ will be 0 or undefined.

### Role in Graph Sketching
Points of inflection are where the graph changes its "bending direction," an important nuance in sketching.

## Second Derivative Test for Maxima and Minima

### The Test
- If $f''(c) > 0$, $f(c)$ is a local minimum
- If $f''(c) < 0$, $f(c)$ is a local maximum

$$
f''(c) > 0 \Rightarrow \text{Local Minimum at } c \\
f''(c) < 0 \Rightarrow \text{Local Maximum at } c
$$

### Why It's Useful
The second derivative test provides a quick way to classify local maxima and minima, which is another piece of the puzzle in graph sketching.

## Summary

Each of these topics contributes to your ability to sketch graphs comprehensively and accurately. While it may seem overwhelming initially, mastering these topics will provide you with a robust set of tools for understanding not only graphs but also the behaviour of functions.