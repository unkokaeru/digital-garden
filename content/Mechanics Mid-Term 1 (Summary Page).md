| Angle (°) | Sine       | Cosine     | Tangent    |
|-----------|------------|------------|------------|
| 0         | 0          | 1          | 0          |
| 30        | 1/2        | √3/2       | 1/√3       |
| 45        | √2/2       | √2/2       | 1          |
| 60        | √3/2       | 1/2        | √3         |
| 90        | 1          | 0          | Undefined  |

- Equations of linear motion.
	  1. $v = u + at$ for final velocity.
	  2. $s = ut + \frac{1}{2}at^2$ for displacement.
	  3. $v^2 = u^2 + 2as$ for velocities with displacement without time.
- Converting units.
	- $1 \text{ inch} = 0.0254\text{m}$
	- $1 \text{ day} = 86400\text{s}$
	- $1 \text{ week} = 604800\text{s}$
	- $1 \text{ lightyear} = 9.5\cdot10^{15}\text{m}$
	- $1\text{km}\cdot\text{h}^{-1} = \frac{1}{3.6}\text{m}\cdot\text{s}^{-1}$
- Dimensional analysis to determine equation completion.
	- Write $\text{LHS}$ and $\text{RHS}$ in terms of dimensions $L,T,M$ (length, time, and mass) - include their order, e.g. $T^\frac{1}{2}$ or $LT^{-1}$.
	- Note that angles are constant, so ignored.
	- Compare $\text{LHS}=\text{RHS}$ or $\text{LHS}\ne\text{RHS}$, therefore complete, or not complete.
- Determining a velocity to cover a distance in a set time.
	- $v_x\cdot t=(x-x_0)$, which can then be rearranged to be $v_x=\ldots$
	- Substitute in given values (or further calculate them) to find the velocity, remembering to use units in every calculation.
- Calculating distance travelled given a constant velocity in a set time.
	- $x_t=v_{x_0}\cdot t$
	- Substitute in given values (or further calculate them) to find the distance, remembering to use units in every calculation.
- Calculating a minimum acceleration to reach $v=0$ in a given distance.
	- For example, the remaining distance could be the distance travelled whilst breaking, and the target distance could be something you want to stop before hitting.
	- $2\cdot a_x\cdot(x(t)-x_\text{remaining})=v_x^2(t)-v_{x_0}^2$, a SUVAT equation. We want $v_x(t)=0$ whilst $x(t)\le x_\text{target}$.
	- So, $x(t)=x_\text{remaining}-\frac{v_{x_0}^2}{2\cdot a_x}\le x_\text{target}\implies x_\text{remaining}\le\frac{v_{x_0}^2}{2\cdot a_x}+x_\text{target}$.
	- Thus, $a_x\le \frac{v_{x_0}^2}{2(x_\text{remaining}-x_\text{target})}$. Substitute and calculate, using units in every calculation.
- Deriving the equations of constant acceleration (SUVATs).
	- Given that $x(t)=x_0+\frac{1}{2}(v_x(t)+v_0)t$ and $v_x(t)=v_0+a_x t$,
	- You can substitute the latter equation into the former to get $x(t)=x_0 + v_0t+\frac{1}{2}a_xt^2$.
	- You can then substitute that equation into the first equation to get $2a_x(x(t)-x_0)=v_x^2(t)-v_0^2$.
	- And so on to get $x(t)=x_0+v_x(t)t-\frac{1}{2}a_xt^2$.
- Using calculus to convert between acceleration, velocity, and position.
	- $a_x(t)\equiv\dot{v}_x(t) \implies \int_0^t a_x(t)dt^\prime = \int_0^t\dot{v}_x(t^\prime)dt^\prime$. Both sides can then be evaluated to give the expected result $v_x(t)=\ldots$
		- For example, $a_x(t)=a_0 : \text{LHS}=a_0\cdot(t-0),\text{RHS}=v_x(t)-v_x(0)$, where the $\text{RHS}$ is evaluated using the Fundamental Theorem of Calculus. $v_x(0)$ usually is equal to zero, as objects often begin movement from rest. Thus, $v_x(t)=a_0t$.
	- One can repeat a similar process given that $v_x(t)\equiv\dot{x}(t)$ to find position.
	- Reversing this, you can differentiate. If given in vectors, we can simple differentiate each component independently of the others.
- Using the definition of average 1D velocity to re-write in terms of integration.
	- Given that $v_{x,\text{avg}}\equiv\frac{x(t_2)-x(t_1)}{t_2-t_1}$, from the Fundamental Theorem of Calculus we have $x(t_2)-x(t_1)=\int_{t_1}^{t_2}\dot{x}(t)dt$, and since $v_x(t)\equiv\dot{x}(t)$, we can re-write it all as $v_{x,\text{avg}}=\frac{1}{t_2-t_1}\int_{t_1}^{t_2}v_x(t)dt\space\square$.
	- From this, we can also include that velocity is equal to the arithmetical average of the velocities, $\frac{v_x(t_2)-v_x(t_1)}{2}$.
- The product of monodirectional orthonormal vectors is one, whilst the product of perpendicular orthonormal vector is 0.
- Using the aforementioned to perform a change of basis.
	- Given a point object $M$ with velocity $\vec{v}$ in an orthonormal frame $R=(O,\hat{i},\hat{j})$, we can create a rotated frame $R^\prime=(O,\hat{i}^\prime,\hat{j}^\prime)$ simply by multiplying the original $\vec{v}$ by the new $\hat{i}^\prime=\cos\alpha\hat{i}-\sin\alpha\hat{j}$ to get the new $\hat{i}$ component, and similarly by $\hat{j}^\prime=\sin\alpha\hat{j}+\cos\alpha\hat{j}$ to get the new $\hat{j}$ component, where $\alpha$ is the angle to which it's being rotated, e.g. $30^\circ$.
	- This expansion can then be simplified using the aforementioned rules.
- Using the law of composition of velocities, determine relative velocities.
	- The law states that $\vec{v}(A|B)=\vec{v}(A|M)+\vec{v}(M|A)$, as well as by definition $\vec{v}(M|M)=\vec{0}$ and $\vec{v}(A|B)=-\vec{v}(B|A)$, where $\vec{v}(A|B)$ represents the velocity of $A$ relative to $B$.
	- Given this, you can work out intermediary velocities until you reach your preferred relative velocity.
- Determining the overall force on a system, given mass and acceleration.
	- First, draw a diagram and determine all of the forces acting on and in the system. Usually, this is weight ($\vec{W}=-(m_1+m_2)g\hat{j}$), a constant force ($\vec{F}=F\hat{i}$), and a normal force ($\vec{N}=N\hat{j}$).
	- Since it'll usually be a Galilean frame, we can use Newton's 2nd law of Dynamics, $(m_1+m_2)\vec{a}=\sum\vec{F}_\text{ext}:$ The sum of the external forces acting on the system is equal to the product of acceleration and the sum of the masses within the system.
	- As a system of equations, $\begin{cases}(m_1+m_2)a_x=F\\(m_1+m_2)a_y=-(m_1+m_2)g+N\\\end{cases}$, using the assumed forces mentioned earlier. Normally $a_y=0$, which also simplifies the system.
	- Substitute and solve, using units in every calculation.
- Determining an individual force within a system, given mass and acceleration.
	- Again, start by drawing a diagram and determining all of the forces acting on and in the system. This will often be the same as the aforementioned steps, with the addition of something like $\vec{F}_{B_2\to B_1}=F_{B_2\to B_1}\hat{i}$.
	- Example Diagram:![[Mechanics Mid-Term 1 (Question Formats) 2023-11-27 16.23.06.excalidraw]]
	- Continue with the steps from before, forming a system from the components and substituting then solving. To find the reverse, use Newton's 3rd Law of Motion.
- Finding the maximum altitude in a 2d kinematics problem.
	- Draw a diagram, write down the system of components, identify the vertical component of acceleration and integrate it until it becomes position (using the fundamental theorem of calculus), then find its maximum using basic calculus (when $\frac{dy}{dx}=0\implies\text{critical point}$, then check it's a maximum with the second derivative or checking the y value on either side).
	- Alternative, you can use the equations of constant acceleration, but that might not be understandable internationally, so the former is "better" - it's also good to have multiple methods of solution.
- Finding the time for a projectile to reach maximum altitude and then return to the floor.
	- Similar to the previous type of question, but find the time to travel to that critical turning position, then double it to find the total time to go up and then down again - assuming its landing position is the same y-level as the starting position.
- Finding the static friction coefficient $\mu_s$ of an object on a slope.
	- First, change the basis with the following logic (in order to simplify the slope part of the question):![[Mechanics Mid-Term 1 (Question Formats) 2023-11-27 15.58.14.excalidraw]]
	- From this diagram, we can use basic trigonometry to define the new basis: $\hat{i}^\prime=(\hat{i}^\prime\cdot\hat{i})\hat{i}+(\hat{i}^\prime\cdot\hat{j})\hat{j}=\cos\theta\hat{i}+\cos(\pi+(\frac{\pi}{2}-\theta))\hat{j}=\cos\theta\hat{i}-\sin\theta\hat{j}$, $\hat{j}^\prime=(\hat{j}^\prime\cdot\hat{i})\hat{i}+(\hat{j}^\prime\cdot\hat{j})\hat{j}=\cos(\frac{\pi}{2}-\theta)\hat{i}+\cos\theta\hat{j}=\sin\theta\hat{i}+\cos\theta\hat{j}$. This change of basis can be applied either way.
	- Then, create the system of components, using the new inertial frame for ease of calculation: Normal reaction ($\vec{N}=N\hat{j}^\prime$), friction force ($\vec{T}=T\hat{i}^\prime$ with $|\vec{T}|\le\mu_s|\vec{N}|$), and weight ($\vec{W}=-mg\hat{j}=-mg(-\sin\theta\hat{i}^\prime+\cos\theta\hat{j}^\prime)$).
	- Frame is inertial so we can use Newton's 2nd Law of Dynamics, and then simplify it with the question statements.
	- Usually, this will result in $\begin{cases}N-mg\cos\theta=0\implies N=mg\cos\theta\\T+mg\sin\theta=0\quad\text{for }\theta\le30^\circ=\frac{\pi}{6}\end{cases}$, therefore when $\theta=\theta_\text{max}, mg\sin\theta_\text{max}=|\vec{T}|_\text{max}=\mu_s|\vec{N}|\implies mg\sin\theta_\text{max}=\mu_s mg\cos\theta_\text{max}$.
	- $\implies \mu_s=\tan\theta_\text{max}$.
- Determine the acceleration of an object falling down a slope against a kinetic friction constant $\mu_k$.
	- Same diagram set-up as the previous question type, and similar force components, with the exception of the friction forces: $\vec{T}=-T\hat{i}^\prime$ with $|\vec{T}|\equiv\mu_k|\vec{N}|$.
	- Continuing, the frame is again inertial so we can use Newton's 2nd Law of Dynamics similarly to result in a system of components. With some rearrangement and substitution, we can solve for $a_{x^\prime}=-\mu_kg\cos\theta +g\sin\theta$.
- If there is no friction, there are no friction coefficients ($\mu=0$).
- Applying familiar friction knowledge with liquid fluid friction forces with drag coefficient $\gamma$.
	- Diagram, system of components, use given information, sub. and solve. May require some calculus and other mathematical tools, but this is the fundamental.
- Show that a one-dimensional force is conservative.
	- Note that all forces only depend on position, which is a necessary prerequisite for a force to be conservative. Next, a given force $F$ in one dimension derives from a potential $U$ if there exists a function $U : F(x)=-\frac{dU}{dx}$ .
	- Given this, we can setup an equation, integrate both sides, and find potential $U$, therefore proving that it is conservative.
- Show that a one-dimensional force is not conservative.
	- Show that the force fails to satisfy at least one of the definitions of a conservative force: 1. The work done by the force on an object moving from one point to another is independent of the path taken; 2. The work done by the force on an object moving around any closed path is zero.
	- For example, a one-dimensional solid kinematic friction force $F_\text{friction}=\begin{cases}-F&\dot{x}\gt0\\F&\dot{x}\lt0\end{cases}$ gives a work done $W(F_\text{friction}|\tau_{A\to A})$, which is given by the integral of the force over the displacement ($dx$): $\int_{x_A}^{x_B}F_\text{friction}dx+\int_{x_B}^{x_A}F_\text{friction}dx=2(x_A-x_B)F$, which cannot equal zero unless $x_A=x_B$, therefore the work done on the object is not independent of the path taken.
	- Another example, a one-dimensional drag force $F_\text{drag}=-\gamma v(t)$. Consider any closed path $\tau_{A\to A}$, we have $W(F_\text{drag}|\tau_{A\to A})=\oint_A F_\text{drag}dx$. However, $v(t)=\dot{x}(t)$ and $dx=\dot{x}(t)dt$ because path can always be characterised by the equation of motion $x(t)$. Thus, $W(F_\text{drag}|\tau_{A\to A})=-\oint_A \gamma\dot{x}^2dt$, given that $\gamma \dot{x}^2\gt0$ unless $\dot{x}=0$ at all times, which is impossible for a closed path. Therefore, $F_\text{drag}$ is non-conservative.
- Considering without and with friction respectively, determine the speed of a block when it reaches the bottom of a slope by reasoning in terms of energy.
	- Without friction, the mechanical energy $E_m$ of the system must be conserved, thus all of the potential energy must be converted into kinetic energy: $mgh=\frac{1}{2}mv^2$, which can then be solved for $v=\sqrt{2gh}$. To solve the problem more formally, you can draw a diagram, list the forces, (normal reaction and weight -> GPE), then use the General Work-Energy Theorem: $E_m(B)-E_m(A)=\int_{\tau_{A\to B}}\vec{F}_{n-c}\cdot d\vec{p}$, where $E_m\equiv \frac{1}{2}m\vec{v}^2+U(\vec{r})$ and $\vec{F}_{n-c}$ represents the normal contact force vector. The integral on the $\text{RHS}$ can be evaluated as 0, thus proving conservation in the mechanical energy: $\int_{\tau_{A\to B}}\vec{F}_{n-c}\cdot d\vec{p}=\int_{x_A^\prime}^{x_B^\prime}N\cdot\hat{i}\cdot\hat{j}dx^\prime$, where $\hat{i}\cdot\hat{j}=0$. Thus, because the normal reaction from the ground is perpendicular to the direction of motion, we can continue as formerly demonstrated.
	- Drawing a diagram, tabulating the contact and distant forces, then assuming an inertial frame to use Newton's 2nd Law, then creating a system of components, simplify with information from the question, invoke the Work-Energy Theorem, then solve and simplify with geometry/algebra: $v=\sqrt{2gh(1-\mu_k\cot\theta)}$.
- Defining elastic collisions in one dimension.
	- A collision is elastic if both total linear momentum is conserved and total kinetic energy is conserved.
	- $\begin{cases}m_1v_1=m_1v_1^\prime+m_2v_2^\prime\\\frac{1}{2}m_1v_1^2=\frac{1}{2}m_1{v_1^\prime}^2+\frac{1}{2}m_2{v_2^\prime}^2\\\end{cases}$, you can then rearrange this system to get other equations, such as $v_1^\prime=\frac{m_1-m_2}{m_1+m_2}v_1$ and $v_2^\prime=\frac{2m_1}{m_1+m_2}v_1$.
- Circular motion equations
	- Characterising Circular Motion: 
	    - Position Vector: $\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j}$
	    - Circle of Radius $R$: $\|\mathbf{r}(t)\| = \text{constant} = R$
	    - Equations: $x(t) = R \cos(\theta(t)), y(t) = R \sin(\theta(t))$
	- Velocity in Circular Motion: 
	    - Velocity Vector: $\mathbf{v}(t) = \mathbf{\dot{r}}(t) = R\dot{\theta}(t)\sin(\theta(t))\mathbf{i} + R\dot{\theta}(t)\cos(\theta(t))\mathbf{j}$
	    - Angular Velocity: $\omega(t) = \dot{\theta}(t)$
	    - Magnitude of Velocity: $\|\mathbf{v}(t)\| = R|\dot{\theta}(t)|$
	- Acceleration in Circular Motion: 
	    - Acceleration Vector: $\mathbf{a}(t) = \mathbf{\dot{v}}(t) = R\ddot{\theta}(t)(-\sin(\theta(t))\mathbf{i} + \cos(\theta(t))\mathbf{j}) + R\dot{\theta}^2(t)(-\cos(\theta(t))\mathbf{i} - \sin(\theta(t))\mathbf{j})$
	    - Tangential Acceleration: $a_T(t) = R\ddot{\theta}(t)$
	    - Centripetal Acceleration: $a_N(t) = R\omega^2(t) = \|\mathbf{v}(t)\|^2/R$
	- Angular Momentum in Circular Motion: 
	    - Definition: $\mathbf{L}_O(t) = \mathbf{r}(t) \times m\mathbf{v}(t)$

- **Projectile Motion**: Analysis without air resistance, with equations for horizontal ($x = v_{0x}t$) and vertical ($y = v_{0y}t - \frac{1}{2}gt^2$) motion.
- **Circular Motion**: Uniform and non-uniform motion, with concepts like centripetal acceleration ($a_c = \frac{v^2}{r}$) and force ($F_c = \frac{mv^2}{r}$).