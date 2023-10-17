## Motion in One Dimension

1. **Displacement, $s$**: Displacement is the change in position of a particle. It is a vector quantity but in one dimension, it's typically represented as a scalar with sign indicating direction.
   
   $$ s = s_f - s_i $$
   where $s_f$ is the final position and $s_i$ is the initial position.

2. **Velocity, $v$ (or $u$ for initial velocity)**: It is the rate of change of displacement.
   
   **Average velocity**:
   $$ v_{avg} = \frac{\Delta s}{\Delta t} = \frac{s_f - s_i}{t_f - t_i} $$
   
   **Instantaneous velocity**: 
   $$ v(t) = \frac{ds}{dt} $$

3. **Acceleration, $a$**: It's the rate of change of velocity.
   
   $$ a = \frac{dv}{dt} $$

### Dot Notation

In calculus, the dot notation represents differentiation with respect to time. For instance:
   
   - $\dot{s}$ is the first derivative of $s$ with respect to $t$, representing velocity.
   - $\dot{v}$ or $\ddot{s}$ represents acceleration, the second derivative of $s$ with respect to $t$.

### Primitive Functions

A primitive function (or antiderivative) of a function $f$ is a function $F$ such that:

$$ F'(x) = f(x) $$

In mechanics, this often means finding displacement when given velocity or finding velocity when given acceleration by integrating. For instance, if $v(t) = \int a(t) dt$, then $s(t) = \int v(t) dt$.

### Particles Under Constant Acceleration (SUVAT Equations)

1. $s = ut + \frac{1}{2} a t^2$
   - Derivation: Integrate acceleration to get velocity, then integrate velocity to get displacement.

2. $v = u + at$
   - Derived directly from the definition of acceleration.

3. $v^2 = u^2 + 2as$
   - Derived by multiplying the second equation by $t$ and adding to the first.

4. $s = \frac{u + v}{2} t$
   - Derivation: Average of initial and final velocities multiplied by time.

5. $s = vt - \frac{1}{2} a t^2$
   - Derived similarly to the first equation but considering final velocity.

## Motion in Two and Three Dimensions

In 2D or 3D, motion can be analysed component-wise:

1. **Displacement Vector**: $\mathbf{s} = \langle s_x, s_y, s_z \rangle$
   
2. **Velocity Vector**: $\mathbf{v} = \langle v_x, v_y, v_z \rangle$
   - Each component: $v_x = \frac{ds_x}{dt}, v_y = \frac{ds_y}{dt}, v_z = \frac{ds_z}{dt}$

3. **Acceleration Vector**: $\mathbf{a} = \langle a_x, a_y, a_z \rangle$
   - Each component: $a_x = \frac{dv_x}{dt}, a_y = \frac{dv_y}{dt}, a_z = \frac{dv_z}{dt}$

In 2D or 3D motion with constant acceleration, the SUVAT equations apply to each dimension independently.

---

**NB**: Always remember that vectors have both magnitude and direction, so when dealing with multiple dimensions, consider each component of the vector independently.
___
## Historical Context of Motion

Understanding motion has been a foundational aspect of human curiosity, leading to numerous profound discoveries in physics and mathematics. Here's a brief overview:

### Ancient Civilizations:

1. **Aristotle (384-322 BC)**: The Greek philosopher postulated that objects in the heavens (like stars and planets) moved in perfect circles and had different physics than objects on Earth. He believed heavier objects fell faster than lighter ones and that motion required a continuous application of force. Although many of Aristotle's ideas were later disproven, they held sway in the Western world for almost two millennia.

### Renaissance and Early Modern Period:

2. **Galileo Galilei (1564-1642)**: Often called the "father of modern physics," Galileo conducted experiments by rolling balls down inclined planes. He contradicted Aristotle's belief by showing that objects fall at the same rate regardless of their weight (in the absence of air resistance). He also laid the groundwork for understanding uniformly accelerated motion.

3. **Johannes Kepler (1571-1630)**: Using detailed observations made by Tycho Brahe, Kepler described planetary motions with three laws. His laws showed that planets move in elliptical orbits with the Sun at one focus, and they swept out equal areas in equal times, which was a departure from the previously held belief of circular orbits.

### The Newtonian Revolution:

4. **Sir Isaac Newton (1643-1727)**: Newton's contributions are monumental. In his work "Philosophiæ Naturalis Principia Mathematica," he set down three laws of motion, which became the bedrock of classical mechanics. He introduced the concept of force and showed that the motion of objects on Earth and in space could be described by the same set of laws. His equation, $F = ma$, linked force (F), mass (m), and acceleration (a) in a quantitative relationship. Furthermore, his law of universal gravitation described how every mass attracts every other mass in the universe.

### Later Developments:

5. **Albert Einstein (1879-1955)**: While Newtonian mechanics excellently describes everyday objects' motion, it fails at very high speeds or in strong gravitational fields. Einstein's theory of relativity gave a new framework for understanding motion in such contexts. His famous equation, $E = mc^2$, established the relationship between energy and mass, reshaping our understanding of motion and energy.

6. **Quantum Mechanics**: In the early 20th century, scientists like Max Planck, Niels Bohr, and Werner Heisenberg developed quantum mechanics to explain motion at the atomic and subatomic levels. This theory showed that, at microscopic scales, motion doesn't adhere to classical ideas, introducing concepts like wave-particle duality and the uncertainty principle.

### In Summary:

The understanding of motion has evolved from ancient philosophical musings to rigorous scientific and mathematical formulations. This journey has reshaped our understanding of the universe, from the motion of celestial bodies to the behaviour of fundamental particles. The history of motion is a testament to human curiosity and our endeavour to understand the natural world.
## Questions
### One Dimension:

1. A car accelerates uniformly from rest to a speed of $60 \text{ m/s}$ over a time of $10 \text{ seconds}$. Calculate:
   a. The acceleration of the car.
   b. The distance travelled by the car in this time.

2. An object falls from rest under the influence of gravity alone (ignoring air resistance). If the object falls for $4 \text{ seconds}$, determine:
   a. Its velocity at the end of the fall.
   b. The total distance it has fallen.

### Two Dimensions:

3. A projectile is launched from the ground level at an angle of $30^\circ$ above the horizontal with an initial speed of $50 \text{ m/s}$. Ignoring air resistance:
   a. Calculate its maximum height.
   b. Determine the horizontal range (the horizontal distance it will travel before hitting the ground).

4. A plane is heading due east at $150 \text{ km/h}$. A wind is blowing from the north at $50 \text{ km/h}$. Calculate the plane's resultant velocity.

### Three Dimensions:

5. A drone starts at a point $A(2,3,4)$ and moves with a constant velocity $\mathbf{v} = \langle 3, -2, 1 \rangle \text{ m/s}$. Find its position after $5 \text{ seconds}$.

6. A particle is moving in space with a velocity given by $\mathbf{v}(t) = \langle t^2, 2t, 3t^3 \rangle \text{ m/s}$. Find:
   a. The particle's acceleration at $t = 2 \text{ seconds}$.
   b. The displacement of the particle between $t = 0$ and $t = 2 \text{ seconds}$.

### Conceptual Questions:

7. Describe the difference between instantaneous velocity and average velocity using a real-world example.

8. A ball is thrown vertically upwards and then comes back down. At what point of its motion does it have maximum potential energy? At what point does it have maximum kinetic energy?

9. Explain the importance of breaking down vectors into their components when analyzing two or three-dimensional motion. Provide an example.

10. A car moves with a constant acceleration in a straight line. If its velocity at $t = 0$ is zero, at what time will its average velocity be equal to its instantaneous velocity? Explain.