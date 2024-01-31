[[Applied Mathematics - Finals Revision Sessions (1-2)]]
[[Geometrical Optics Revision]]

Fermat's Principle of Mathematics - Principle of Least Time.
Lens-Maker's Equation: $\frac{1}{f}=(n-1)(\frac{1}{R_{1}} - \frac{1}{R_{2}})$

#### Sign Conventions

For spherical mirrors,

$p,q$: Positive if in front of of the mirror (real), negative if behind (virtual).
$f,R$: Positive if the centre of curvature is in front (concave), negative if behind (convex).
$M$: Positive if upright, negative if inverted.

For refracting surfaces and thin lenses, the same theoretical conventions are used: positive in the direction of the ray travel and areas of thickness/convergence, otherwise negative.

- 2023
	- A
		- 1
			- Pythagoras' Theorem, where $a^{2}+b^{2}=c^{2}$.
			- Finding a minimum with differentiation.
		- 2
			- Calculating mechanical energy with $E_{\text{initial}}=KE_{\text{initial}}+PE_{\text{initial}}$, where $KE_{\text{initial}}=\frac{1}{2}mv_{0}^{2}$ and $PE_{\text{initial}}=mgh_{0}$.
			- Calculate maximum altitude with the conservation of mechanical energy, e.g. all $KE$ is transferred into $PE$ $\implies E_{\text{initial}}=PE_{\text{max}}=mgh_{\text{max}}$. Make sure to add the initial height, also.
			- Calculate velocity when an object lands on the ground with the conservation of mechanical energy, e.g. all $PE$ is transferred into $KE\implies E_{\text{initial}}=KE_{\text{final}}=\frac{1}{2}mv^{2}_{\text{final}}$.
		- 3
			- Given a harmonic wave $h(x,t)=A\cos(kx-\omega t)$, where $A$ is the amplitude (maximum displacement from rest position), $k$ is the wave number (wave cycles in a unit of distance), $\omega$ is the angular frequency (rate of change of the phase of a sinusoidal waveform), $x$ is the position, and $t$ is the time, $kx-\omega t$ represents the phase of the wave. For a fixed point in time, the phase changes with $x$; for a fixed point in space, the phase changes with $t$. Hence the wave is forward propagating if the $wt$ term is negative, which it is - as time increases, the wave moves in the positive $x$-direction to maintain a constant phase.
			- Calculate the wavelength and time period of a harmonic wave with $\lambda=\frac{2\pi}{k}$ and $T=\frac{2\pi}{\omega}$, respectively.
			- Calculate the phase velocity (the rate at which the wave propagates in space) with $v_{\phi}=\frac{\omega}{k}$.
	- B
		- 1
			- Given a position vector, find the acceleration vector through repeated differentiation.
			- Justify that tension and weight satisfy two given equations. The former by explaining how tension is always directed along the string towards the pivot point and is hence proportional to the position of the string: $\vec{T}=T\vec{r}$. The latter by explaining the direction of weight and hence $\vec{W}=mg\hat{j}$, which when decomposed is equal to $mg(\cos\theta\hat{r}-\sin\theta\hat{\theta})$.
			- Given that the gravitational force has the tangential component $F_{\text{tan}}=mg\sin(\theta)$, we can apply Newton's Second Law $\sum\limits F=ma$ such that the tangential acceleration $a_{\text{tan}}=L\ddot{\theta}$ is the second derivative of arc length ($L\theta$) for small angles, hence: $mg\sin(\theta)=mL\ddot{\theta}$, which can be simplified by using the small angle approximations and dividing through by $m$ and $L$ to result in $\ddot{\theta}- \frac{g}{L}\theta=0$.
			- Calculate the period of oscillation with $T=2\pi\sqrt{\frac{L}{g}}$.
		- 2
			- Given that glass has a refractive index of $n=1.5$, that means the propagation of light in glass is a speed that is $\frac{1}{1.5}$ times the speed of light in air, and bends towards the normal as shown in Snell's Law (given that air has a refractive index of 1): $\sin\theta_{1}=1.5\sin\theta_{2}$.
			- Given that $\theta_{1}=45^{\circ}$, we can use Snell's law from (a) to find $\theta_{2}$.
			- Since the angles in a triangle add up to $180^{\circ}$, we can form the equation $180^{\circ}=\theta_{2}+\theta_{3}+120^{\circ}$ which when solved for $\theta_{3}=60^{\circ}-\theta_{2}$.
			- Using Snell's Law for the final interface, we can calculate $\theta_{4}$ from $\theta_{3}$.
			- Redo (b) and (d) given that $\theta_{1}=25^{\circ}$.
- 2022
	- A
		- 1
			- Draw a diagram where a light ray passes between two medium such that $n_{1}<n_{2}$, thus bending towards the normal.
			- Use Snell's Law to find a missing angle, given two refractive indices.
			- If $n_{1}>n_{2}$ instead, then light will bend away from the normal. If the angle of incidence is greater than a certain critical angle, total internal reflection will occur.
		- 2
			- Define an elastic collision as a collision in which both momentum and kinetic energy are conserved. In the situation of a small truck colliding with a tennis ball, it's a somewhat realistic assumption to make, as they'll separate after the collision and will collide without any permanent deformation or generation of heat.
			- In a one dimensional elastic collision, momentum and kinetic energy are conserved, which can be defined as a system of equations where before = after.
			- Solving the system of equations and inputting given data, we can calculate the truck's speed after the collision.
			- We can calculate the number of tennis balls to make the truck's speed after the collision equal to zero by finding the mass that gives that result and dividing by the mass of a single tennis ball.
		- 3
			- Find velocity by integrating a given acceleration, remembering to add the initial velocity onto the result.
			- To find the smallest frequency $\omega$ for an object to return after one hour of travel, we can solve the velocity for function for where it is equal to zero at $t=0$, 
			- To find the distance to leave and return, we can integrate again to find the position (with the addition of the initial position), then substitute the given and calculated information.
		- 4
			- Calculate two second order partial derivatives and substitute them into an equation to validify a solution.
			- The group velocity of waves is the velocity with which the overall shape of the waves' amplitudes propagates through space. This is often equal to the phase velocity ($v_{\phi}=\frac{\omega}{k}$), when dealing with a simple monochromatic wave.
	- B
		- 1
			- Given a static block on a wedge, the forces acting on it are: gravitational force ($F_{g}=mg$), normal force ($N$, decomposed gravitational force, perpendicular component to the wedge), static friction force ($F_{s}=\mu_{s}N$, also decomposed gravitational force, parallel component to the wedge).
			- Given that the friction force can be expressed in two expressions, we can set the equal to one another and solve for any given variable.
			- Logically, we can extend this solution to demonstrate theoretical scenarios with substitutions and inequalities etc.
		- 2
			- To find the final image in a double lens problem algebraically, one can use the lens formula $\frac{1}{f}=\frac{1}{d_{o}} + \frac{1}{d_{i}}$, taking care to use the correct sign conventions. If $L$ is the distance between the two lenses, our final formula for the final image distance would be $d_{i_{2}}=\frac{1}{\frac{1}{f_{2}} - \frac{1}{L-|d_{i_{1}}|}}$.
			- One can find the total magnification of the double lens system by finding their product, where each individual magnification is found by dividing $-d_{i}$ by $d_{o}$.
			- To construct a ray diagram, one could use a ray parallel to the principal axis of a lens that will then pass through the focal point on the other side of the lens, and/or, one could use a ray passing through the center of the lens which will continue in the same direction without bending. The same set of rays can be used for both lenses in the system: the image will be different for each lens because the object distance for the second lens depends on the image formed by the first lens.
			- To draw the full diagram, we can use all of the aforementioned in combination with accurate drawing.
- 2021
	- A
		- 1
			- For a converging thin lens, given that magnification is given by the negative ratio between image distance $q$ and object distance $p$, $- \frac{q}{p}$, if the distance to the object is multiplied by a factor of 1 billion, then the magnification would hence be reduced by the same factor.
			- The size of an object on a human retina is directly proportional to the actual size, hence if Venus is 6000km in radius and Sirius is the same retina size, yet 1 million times further away, then Sirius must be 1 million times greater in radius, hence 6 billion kilometres.
			- The angular resolution of an optical system determines the smallest angle between two points that can still be distinguished. For the human eye, this is about $\frac{1}{60}^{\circ}$. To access whether or not (b) is reasonable, we can calculate its angular size with the formula $\theta=2\times\arctan(\frac{R_{S}}{D_{S}})$. However, when we calculate this for the former part, it's definitely an irregularly large result: 2 radians.
		- 2
			- Given a constant force implies a dynamics a problem: dynamics is the branch of mechanics that is concerned with the forces and their effect on motion, whilst, kinematics deals with motion without considering its causes.
			- To find the velocity vector, we can use Newton's second law and integrate the constant acceleration we find.
			- To calculate work done, we can use the work-energy theorem which states that work done is equal to the change in kinetic energy of a particle, or, we could use the formula $W=\vec{F}\cdot\vec{d}$. There are also other ways, like using an equation of constant acceleration, $\vec{d} =\vec{v}_{0}t + \frac{1}{2}\vec{a}t^{2}$.
		- 3
			- To find a solution to the given equation and validify the given solution, we must calculate the two second partial derivatives and substitute them into the given equation.
			- A positive velocity would indicate a forward propagating wave, while a negative velocity would indicate a backward propagating wave: we can draw a diagram to show this, also.
		- 4
			- In simple terms, Newton's first law says there's no way to tell the difference between being still and moving straight at a constant speed unless you look at other things to compare with. This comparison is what makes motion "relative" not "absolute."
	- B
		- 1
			- The acceleration of the mass within the box's frame is the same as the box's acceleration: $-12\text{ms}^{-1}\hat{i}$. This can be shown using the change of frame formula.
			- The forces acting on the mass are: the elastic force exerted by the spring (contact force), and the inertial force due to the acceleration of the non-inertial frame (considered a force at a distance in this frame).
			- By Newton's Second Law, $\sum\limits F=ma$, thus the sum of the aforementioned forces must sum to equal $ma$, with respect to the box's frame. Hence, $-kx\hat{i}+ma_\text{box}\hat{i} = 0$, where they are equal to zero since the mass is immobile with respect to the box. Hence, $x=\frac{ma_\text{box}}{k}\hat{i}$.
			- The potential elastic energy is found by calculating $U=\frac{1}{2}kx^{2}$, where we calculate $x$ in the previous part and were given $k$.
			- If we relax the condition that the box's acceleration must be accounted for as an inertial force, then the mass can be considered in mechanical equilibrium in the box's frame of reference by introducing a fictitious force that balances the spring force. This fictitious force would have a magnitude equal to $ma_\text{box}$ and would be directed opposite to the acceleration of the box.
		- 2
			- Using Snell's Law of refraction, we can calculate the angles at a refraction interface.
			- By using the basic properties of triangles, we can find a complimentary angle to the one previously calculated, and hence relate it to the incident ray.
			- Given that total internal reflection occurs, the reflected angle will be equal to the one previously calculated, and hence again can be related to the incident ray. Moreover, we can calculate it given that this can only occur at or above the critical angle, given by the formula $\sin(c)=\frac{n_{1}}{n_{2}}$.
			- Using the latter method to calculate the former relationship, we can calculate a range for which an angle will satisfy the requirements.
			- Finally, we can relate the aforementioned range to the incident ray, so we can always ensure that total internal reflection occurs.