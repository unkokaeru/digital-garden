## Revision Plan

Final exam made of two parts: A (shorter methodical questions, solutions required for all questions), and B (longer conceptual questions, highest marking solution used for final marks).

In-class revision: 1 hour optics, 2 hours mechanics, 1 hour waves.

- Practical Solutions
	- Week 1, Problem 2 (Optics)
	- Week 2, Problem 4 (Optics)
	- Week 3, Problem 3 (Optics)
- Revision Questions
	- Kinematics (Mechanics)
	- ...

### Optics

Generally, in optics, you should draw a detailed graphical solution to the question, as well as detailed supporting algebraic solution.

#### Week 1, Problem 2

##### Question

A layer of water is on the top of a horizontal rectangular slab of glass. There is no wind or other perturbances on the surface of water. A light ray hits the water at some non-zero angle with the normal to the water surface. Draw all resulting rays. Choose your own angle of incidence for the first ray (you don’t need necessarily to choose a numerical value, you can choose a graphical representation) and find angles of travel for all other rays. The indexes of refraction of air, water and glass are: $n_1$, $n_2$, and $n_3$ correspondingly.

##### Solution

Assuming that the glass is on a non-reflective surface, let $n_1$ be the refractive index of air, $n_2$ the refractive index of water, and $n_3$ the refractive index of glass, such that:

![[Applied Mathematics - Finals Revision Sessions (1-2) 2024-01-09 11.16.00.excalidraw]]

$$
n_{1}<n_{2}<n_{3}
$$

Using Snell's Law for Refraction, $n_{1}\sin(θ_{1}) = n_{2} \sin(θ_{2})$, then we arrive at the following equations:

$$
\begin{matrix}n_{1}\sin(θ_{1}) = n_{2} \sin(θ_{2}) \\ n_{2}\sin(θ_{2}) = n_{3} \sin(θ_{3})\end{matrix}
$$

Which we can then either solve for $\theta_{1},\theta_{2},\theta_{3}$, or arrive at the conclusion that $n_{1}\sin(θ_{1}) = n_{3} \sin(θ_{3})$, such that the angle of the refracted ray in the glass interface is not dependent on the ray in the previous water interface.

$$
\fbox{The refracted ray in the final interface does not depend on the intermediary interface.}
$$

However, there could also be more rays, due to factors such as Total Internal Reflection, etc. - there could (mathematically) be an infinite number of rays, hence we could not draw them all.

#### Week 2, Problem 4

##### Question

A coin of 1.2 cm in diameter is 4 cm away from a biconvex lens that has a focal length of 12 cm. Find the image of the coin. You can choose an orientation of the coin.

##### Solution

Graphically, we can represent the problem as below,

![[Applied Mathematics - Finals Revision Sessions (1-2) 2024-01-09 11.33.04.excalidraw]]

Such that the image, $I$, is 6cm away from the biconvex lens, and is 1.5x the diameter of the object: hence has a diameter of 1.8cm.

Algebraically, we can use the mirror question and magnification equation to find the same results:

$$
\frac{1}{f} = \frac{1}{v} + \frac{1}{u}\iff \frac{1}{12}=\frac{1}{v} + \frac{1}{4}\iff v=-6
$$

$$
m=- \frac{v}{u}=- \frac{-6}{4}=1.5
$$

$$
\fbox{The image has a diamter of 1.8cm, 6cm away from the biconvex lens.}
$$

#### Week 3, Problem 3

##### Question

Light is shining normally to $n_{1}- n_{2}$ interface. The intensity of reflected light is $I = (\frac{n_{1}-n_{2}}{n_{1}+n_{2}})I_0$, where $I_0$ is the incident intensity, and $n_i$ are the refraction indices for the two media.

Find the intensities of the light transmitted through air-glass interface.
Find the intensities of the light transmitted through a slab of glass in air.

##### Solution

Light is shining normally to the $n_1-n_2$ interface, thus the angle is $90^\circ$. Using the equation given in the question,
$$
I=\left(\frac{n_1-n_2}{n_1+n_2}\right)^2\cdot I_0
$$
we can calculate the intensity between an air-glass interface in terms of the incidence intensity, using $n_1=1$ and $n_2=1.5$:
$$
I_1=\left(\frac{1-1.5}{1+1.5}\right)^2\cdot I_0=0.04\cdot I_0
$$

$$
\fbox{Intensity transmitted through the air-glass interface is 0.96x the initial intensity.}
$$

We can then continue this equation to find the following intensities whilst the light travels through the slab of glass:
$$
I_2=\left(\frac{1.5-1}{1.5+1}\right)^2\cdot(0.96\cdot I_0)=0.0384\cdot I_0
$$
Thus, the remaining intensity out of the slab of glass would be $0.96-0.0384$, therefore:
$$
I_{\text{final}}=0.9216\cdot I_{\text{initial}}
$$

$$
\fbox{Intensity transmitted through the glass slab is approximately 0.92x the initial intensity.}
$$


### Mechanics

Generally, in mechanics, ensure you methodically and clearly explain solutions to each question, justifying everything you do.

#### Exercise 1

##### Question

Find the velocity and acceleration vectors of a point object, $M$, moving in a Galilean frame, an inertial frame of reference where Newton's Laws hold, $R=(O,\hat{i},\hat{j})$ with position vector:

$$
\vec{r}(t)=\cos(wt)\hat{i}+\sin(wt)\hat{j}
$$

##### Solution

By definition,
$$
\vec{v}(t)=\dot{\vec{r}}(t)=-w\sin(wt)\hat{i}+w\cos(wt)\hat{j}
$$
$$
\vec{a}(t)=\dot{\vec{v}}(t)=-w^2\cos(wt)\hat{i}-w^2\sin(wt)\hat{j}
$$

#### Exercise 2

##### Question

*Note: the question is lacking some notation, due to the fact that I have no glasses and cannot read it, whoops.*

*I also gave up writing the solution because I couldn't read enough - solution and question to be left for the reader, I guess.*

What should be the velocity $\vec{v}$ of a different frame, $R^{\prime}(O,\hat{i},\hat{j})$ relative to the original frame (in Exercise 1), $R$, for the motion of the object $M$ to be observed with constant velocity $\vec{v}^\prime=v^{\prime}\hat{i}$?

##### Solution

Using the Law of Composition of Velocities, $\vec{v}(M|O^{\prime})=\vec{v}(M|O)+\vec{v}(O|O^{\prime})$, we can derive the fact that:

$$
\begin{align*}
\vec{v}(M|O^{\prime})&=\vec{v}(M|O)+\vec{v}(O|O^{\prime})\\
&= (-w\sin(wt)\hat{i}+w\cos(wt)\hat{j}) + ()
\end{align*}
$$

...