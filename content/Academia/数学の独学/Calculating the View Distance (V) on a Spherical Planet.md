# Calculating the View Distance ($V$) on a Spherical Planet

## Attempt One

![[Calculating view distance on a sphere 2024-01-04 06.39.14.excalidraw]]

If we model the view distance as shown above, our end result should be the **blue** length: a fraction of the circumference of the circle, $2\pi r$. Hence we can use the green portion and its $\theta$ to calculate the end result:

$$
\frac{\theta}{2\pi}\cdot 2\pi r\implies \frac{\theta}{r}:\theta\mapsto\theta^{\text{ c}}
$$

From this simplified result, we can see that the problem is likely in trigonometry. So let's reframe the situation slightly:

![[Calculating view distance on a sphere 2024-01-04 07.00.39.excalidraw]]

Since we're working with estimations, we can model the triangle to be a right-angled triangle, and the Earth is a perfect sphere. That allows us to draw the conclusion that $(r+h)^{2}=r^{2}+d^{2}:d$ is the distance to the horizon.

Rearranging this, we can find $d$ to be $\sqrt{(r+h)^2-r^2}$, or (simplified) $\sqrt{h(2r+h)}$. Then to find $\theta$, we can use the basic definition of $\sin$ as a ratio: here, $\frac{d}{r+h}$. Hence,

$$
\begin{align*}
\theta&=\arcsin\left(\frac{d}{d+h}\right)\\
&=\arcsin\left(\frac{\sqrt{h(2r+h)}}{h+\sqrt{h(2r+h)}}\right)\\\\
&=\arcsin\left(\frac{\sqrt{h(2r+h)}}{h+\sqrt{h(2r+h)}}\cdot\frac{h-\sqrt{h(2r+h)}}{h-\sqrt{h(2r+h)}}\right)\\\\
&=\arcsin\left(\frac{h\sqrt{h(2r+h)}-h(2r+h)}{h^{2}-h(2r+h)}\right)\\
&=\arcsin(\frac{h(\sqrt{h(2r+h)}-2r-h)}{h^2-2rh-h^2})\\
&=\arcsin(-\frac{h(\sqrt{h(2r+h)}-2r-h)}{2rh})\\
&=\arcsin(-\frac{\sqrt{h(2r+h)}-2r-h}{2r})
\end{align*}
$$

Substituting this into our original expression gives...

$$
\frac{1}{r}\cdot\arcsin(-\frac{\sqrt{h(2r+h)}-(2r+h)}{2r})
$$

Note also that often the diameter is using opposed to the radius, so we'll change our formula slightly to use $d$ as the diameter instead of $2r$, just to simplify calculation slightly.

$$
\frac{2}{d}\cdot\arcsin(-\frac{\sqrt{h(d+h)}-(d+h)}{d})
$$

It may also be preferred to calculate $d+h$ just once, as it comes up twice in the formula, so an optional simplification could be to let something like $D=d+h$ to give the final formula:

$$
\text{View distance (curved)}=V=\frac{2}{d}\cdot\arcsin(-\frac{\sqrt{Dh}-D}{d}):D=d+h
$$

In order to test this final formula and see if it gives a meaningful result, we can make the estimate that a human's sight is $1.8\text{m}$ above sea level, and that the diameter of the Earth is $12742000\text{m}$ (assuming it is perfectly spherical).

$$
\begin{matrix}
d=12742000 \\ h=1.8 \\ D=12742001.8
\end{matrix}
\implies
V=\frac{2}{12742000}\cdot\arcsin\frac{-(\sqrt{12742001.8\cdot12742000}-12742001.8)}{12742000}
$$

Evaluating this returns the following result of approximately $0\text{m}$ - the distance to the horizon is substantially greater, but is still approximately $0\text{m}$.

Clearly, there's something wrong here.

## Attempt Two

### Analysis of Attempt One

In my first attempt, I correctly set up the problem by considering the observer's height above the Earth's surface and the radius of the Earth. My use of the right-angled triangle to find the distance to the horizon (d) is a common approach in such problems and is mathematically sound, after some brief research.

I then proceeded to find the angle $\theta$ using the arcsine function, which also seems logical given the geometric setup. However, it seems that there might be an error in the algebraic manipulation of the arcsine expression, specifically in the simplification steps.

### Identifying the Issue

The issue seems to lie in the expression inside the arcsin function:

$$
\frac{\sqrt{h(2r+h)}-(2r+h)}{2r}
$$

This expression simplifies to a negative value, which doesn't make intuitive sense in this context. The view distance should be a positive value. Also, the algebraic manipulation in the arcsin argument seems to be incorrect. The term $-\frac{\sqrt{h(2r+h)}-(2r+h)}{2r}$ is not simplifying correctly.

### Correcting the Formula

To correct the formula, let's revisit the geometry of the problem:

1. **Distance to the Horizon ($d$)**: As I correctly stated, $d = \sqrt{h(2r+h)}$.

2. **Finding the Angle ($\theta$)**: The angle can be found using the cosine rule or similar triangle principles. The angle should be calculated with respect to the centre of the Earth, considering the observer's height.

3. **Calculating the Arc Length ($V$)**: Once we have the angle, the arc length can be calculated using the formula $V = r \cdot \theta$, where $\theta$ is in radians.

### Proposed Solution

Let's correct the approach:

1. Recalculate $d$ as $d = \sqrt{h(2r+h)}$.
2. Find $\theta$ using either the cosine rule or similar triangles.
3. Calculate $V = r \cdot \theta$.

### Implementation

1. $d = \sqrt{h(2r+h)}$.
2. $\theta=\arccos\left(\frac{r}{r+h}\right)$.
3. $V=r\cdot\arccos\left(\frac{r}{r+h}\right)$.

## Final Evaluation

The corrected view distance, calculated using the revised approach, is approximately $4789.11$ meters. This value represents the distance to the horizon for an observer standing $1.8$ meters above sea level on a spherical Earth with a radius of $6371000$ meters.

This result is much more realistic and aligns better with empirical observations and calculations for the distance to the horizon. The key was to use the correct geometric relationships and ensure that the trigonometric calculations were accurately applied.

# An interesting observation

![[desmos-graph.svg]]

Note the above, also - a graph of how far the observer can see as it increases its height from sea level. After performing some analysis on the function, we can find that the asymptote is at $3185500\pi\text{m}\approx1.00075\times10^{7}\text{m}$. Interestingly, this is just $\frac{\pi}{2}r$.

This made me wonder if I could plot a graph showing a percentage of the surface area of the Earth that the observer can see at once.

## Conversion into area

Using the formula for a [[spherical cap]], based solely on radius ($r$) and arc length ($V$), we can produce the following formula:

$$
A=2\pi r\left[r\left(1−\cos\left(\frac{2r}{r\cdot\arccos\left(\frac{r}{r+h}\right)}\right)\right)\right]
$$

However, for this to be a percentage of the viewable surface area, we should divide it by the surface area of the Earth, given that it's a perfect sphere: $4 \pi r^{2}$.

This simplifies to our final formula...

$$
A=\frac{1}{2}−\frac{1}{2}\cos\left(\frac{2r}{r\cdot\arccos\left(\frac{r}{r+h}\right)}\right)
$$

However, we already know what the maximal arc length is: $\frac{\pi}{2}r$. So, the expression for the maximum area is

$$
\frac{1}{2}−\frac{1}{2}\cos\left(\frac{4}{\pi}\right)\approx35.34\%
$$

Weird.