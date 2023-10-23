# Tutorial Week 1: Revision of Vectors

## Warm-up questions

1. What is the difference between a vector and a scalar?

2. What is the resultant of two vectors? How would you find this graphically?

3. How would you subtract one vector from another?

4. What can you say about the vectors $\mathbf{a}$, $2\mathbf{a}$ and $3\mathbf{a}$?

5. What is a position vector?

6. What are the different ways of representing a given vector?

## Numerical questions

1. Give two vectors that are parallel to each of the following:
   - $2\mathbf{a}$
   - $3\mathbf{i} + 4\mathbf{j} - 2\mathbf{k}$
   - $$
     \begin{bmatrix}
     1 \\
     2 \\
     -1 \\
     \end{bmatrix}
     $$

2. Find the magnitude of the following vectors:
   - $\mathbf{v} = 5\mathbf{i} + 7\mathbf{j} + 3\mathbf{k}$
   - $\mathbf{w} = 3\mathbf{i}_3 + 4\mathbf{j}_4 - 2\mathbf{k}_5$
   - $$
     \mathbf{u} = 
     \begin{bmatrix}
     2 \\
     1 \\
     -1 \\
     \end{bmatrix}
     $$

3. The position vector of point $A$ is $3\mathbf{i}_3 + 2\mathbf{j}_4 + 4\mathbf{k}_5$, and the position vector of point $B$ is $2\mathbf{i}_3 + 6\mathbf{j}_4 - 5\mathbf{k}_5$. Find $\mathbf{AB}$.

4. If point $A$ is at $(1, 2, 3)$ and $B$ is at $(3, -1, -2)$, find $\mathbf{OA}$, $\mathbf{OB}$ and $\mathbf{AB}$.

5. Find the vector equations of the following:
   - a straight line through $(3, 2, 4)$ and $(-1, 3, 0)$;
   - a straight line through $(4, 1, 2)$ parallel to the vector $3\mathbf{i}_3 + \mathbf{j}_4 - \mathbf{k}_5$;
   - a straight line parallel to the vector $\mathbf{i}_3 + 3\mathbf{j}_4 - 2\mathbf{k}_5$ passing through the point with position vector $3\mathbf{i}_3 + 2\mathbf{j}_4 + 6\mathbf{k}_5$.

6. Determine whether the lines
   $$
   \mathbf{l}_3 = 
   \begin{bmatrix}
   5 \\
   2 \\
   -1 \\
   \end{bmatrix}
   + \lambda
   \begin{bmatrix}
   1 \\
   -2 \\
   -3 \\
   \end{bmatrix}
   $$
   and
   $$
   \mathbf{l}_4 = 
   \begin{bmatrix}
   2 \\
   0 \\
   4 \\
   \end{bmatrix}
   + \mu
   \begin{bmatrix}
   1 \\
   2 \\
   -1 \\
   \end{bmatrix}
   $$
   intersect. If so, find the point of intersection.


# Tutorial Week 2: Vectors and Hyperbolic Functions

1. How do we define the scalar product of two vectors $\mathbf{a}$ and $\mathbf{b}$?
	$|\underline{a}||\underline{b}|\cos\theta$.

2. If the scalar product of two vectors is zero, what does this tell us about the vectors?
	Perpendicular vectors

3. What is the scalar product of two parallel vectors?
	$|\underline{a}||\underline{b}|$

4. Show that, if $\mathbf{a} = a_1\mathbf{e}_1 + a_2\mathbf{e}_2 + a_3\mathbf{e}_3$ and $\mathbf{b} = b_1\mathbf{e}_1 + b_2\mathbf{e}_2 + b_3\mathbf{e}_3$, then $\mathbf{a} \cdot \mathbf{b} = a_1b_1 + a_2b_2 + a_3b_3$.
	Multiply the two vectors out, then all perpendicular vectors are 0, so you're left with the required result.

5. Find $\mathbf{a} \cdot \mathbf{b}$ if 
   (a) $\mathbf{a} = 3\mathbf{e}_1 + 4\mathbf{e}_2$ and $\mathbf{b} = \mathbf{e}_1 - 2\mathbf{e}_2 + 3\mathbf{e}_3$ 
   $$\underline{a}\cdot\underline{b}=-5$$
   (b) $\mathbf{a} = \begin{bmatrix} 4 \\ 2 \\ 1 \end{bmatrix}$ and $\mathbf{b} = \begin{bmatrix} 3 \\ -4 \\ -3 \end{bmatrix}$.
$$
12-8-3=1
$$

6. Find the angle between the vectors $\mathbf{a}$ and $\mathbf{b}$.
$$
\cos\theta=\frac{\underline{a}\cdot\underline{b}}{|\underline{a}||\underline{b}|}\implies\cos\theta=-\frac{16}{\sqrt{37}\sqrt{84}}\implies\theta=1.86\ldots^c= 106.7^\circ
$$

7. Line $l$ has the equation $\mathbf{r} = \begin{bmatrix} 2 \\ 0 \\ 4 \end{bmatrix} + \lambda \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}$. Point $A$ and point $B$ have coordinates $(4, 4, 2)$ and $(1, 0, 3)$ respectively. Find the acute angle between $l$ and the line segment $AB$.
$$
\underline{AB}:\mathbf{r} = \begin{bmatrix} 4 \\ 4 \\ 2 \end{bmatrix} + \lambda \begin{bmatrix} 3 \\ 4 \\ -1 \end{bmatrix}
$$
$$
\cos\theta=\frac{\underline{a}\cdot\underline{b}}{|\underline{a}||\underline{b}|}\implies\cos\theta=-\frac{12}{\sqrt{6}\sqrt{26}}\implies\cos\theta=2.86^c=0.28^c\text{ (acute angle)}
$$

8. Show that the lines $\mathbf{r}_1 = (\mathbf{e}_1 + 6\mathbf{e}_2 + 2\mathbf{e}_3) + \lambda(\mathbf{e}_1 + 2\mathbf{e}_2 + 2\mathbf{e}_3)$ and $\mathbf{r}_2 = (3\mathbf{e}_1 - \mathbf{e}_2 + \mathbf{e}_3) + \mu(4\mathbf{e}_1 - 3\mathbf{e}_2 + \mathbf{e}_3)$ are perpendicular.
Work out the dot product of the two direction vectors = 0.

9. Show that $\cosh(x) - \cosh(y) = 2\sinh\left(\frac{x+y}{2}\right)\sinh\left(\frac{x-y}{2}\right)$.
$$
2\cdot\frac{e^\frac{x+y}{2}-e^{-\frac{x+y}{2}}}{2}\cdot\frac{e^\frac{x-y}{2}-e^{-\frac{x-y}{2}}}{2}\implies\frac{1}{2}\left(e^x-e^y-e^{-y}+e^{-x}\right)
$$
$$
\implies\frac{e^x+e^{-x}}{2}-\frac{e^y-e^{-y}}{2}\implies\cosh x-\cosh y
$$

10. Find all real solutions of the following hyperbolic equations:
    (a) $\cosh(x) - 5\sinh(x) - 5 = 0$
    (b) $2\cosh^2(x) - \sinh^2(x) - 2 = 0$
    (c) $3\cosh^2(x) - \sinh^2(x) - 3 = 0$.

11. The $\tanh$ function was used by the (no longer active) UK Health Forum to fit data on the gradual increase in the percentage of the British population who can be classed as obese. Sketch the graph of the $\tanh$ function, and answer the following questions:
    (a) Which region of this graph would be most suitable for fitting this kind of data?
    (b) What properties does this function have that enable it to fit data on the gradual increase in the percentage incidence of obesity?
    (c) A function used for curve fitting will include at least one adjustable parameter. In the case of the hyperbolic tangent, we could have $f(t) = a\tanh\left(\frac{t-b}{c}\right)$, where $a$, $b$ and $c$ are the adjustable parameters and $t$ is a time.
        (i) What would be the effect of changing each of these parameters on the graph of $f(t)$?
        (ii) If $t$ is measured in years, what units would $b$ and $c$ be measured in?
# Tutorial Week 3: Algebra, Trigonometry, and General Revision
[[Y3_Revision.pdf]]
![[Week_3_Tutorial.pdf]]
![[Tutorial_week_3.pdf]]
# Tutorial Week 4: Algebra and Complex Numbers
![[Tutorial_week_4.pdf]]
![[Week_4_Tutorial.pdf]]


# Tutorial Week 5: Arbitrary Bases and Limits
![[Tutorial_week_5.pdf]]
![[Tutorial_5.pdf]]