![[Practical34bis.pdf]]

#### Question 1
$$
\vec{a}(t)=a_x\hat{i}+a_y\hat{j}
$$
$$
\vec{v}(0)=v_{x,0}\hat{i}+v_{y,0}\hat{j}
$$
$$
\vec{r}(0)=x_0\hat{i}+y_0\hat{j}
$$
##### Question 1a
$$
\vec{v}(t)=\vec{v}(0)+\int_0^t a_x(t^\prime)dt^\prime
$$
$$
\implies \vec{v}(t)=v_{x,0}\hat{i}+v_{y,0}\hat{j}+\left[a_xt^\prime\hat{i}+a_yt^\prime\hat{j}\right]_0^t
$$
$$
\implies \vec{v}(t)=v_{x,0}\hat{i}+v_{y,0}\hat{j}+a_xt\hat{i}+a_yt\hat{j}
$$
$$
\implies \vec{v}(t)=(v_{x,0}+a_xt)\hat{i}+(v_{y,0}+a_yt)\hat{j}
$$
##### Question 1b
$$
\vec{r}(t)=\vec{r}(0)+\int_0^t v_x(t^\prime)dt^\prime
$$
$$
\implies \vec{r}(t)=x_0\hat{i}+y_0\hat{j}+\left[(v_{x,0}+a_xt^\prime)\hat{i}+(v_{y,0}+a_yt^\prime)\hat{j}\right]_0^t
$$
$$
\implies \vec{r}(t)=x_0\hat{i}+y_0\hat{j}+(a_xt)\hat{i}+(a_yt)\hat{j}
$$
$$
\implies \vec{r}(t)=(x_0+a_xt)\hat{i}+(y_0+a_yt)\hat{j}
$$
#### Question 2
$$
\vec{v}=(\sqrt{3}\text{m}\cdot\text{s}^{-1})\hat{i}+(-1\text{m}\cdot\text{s}^{-1})\hat{j}
$$
Map this to a new frame tilted by an angle $\alpha=30^\circ$ such that $\hat{i}\mapsto\cos\alpha\hat{i}-\sin\alpha\hat{j}$ and $\hat{j}\mapsto\sin\alpha\hat{i}+\cos\alpha\hat{j}$.

$$
\cos30^\circ=\frac{\sqrt{3}}{2},\quad\sin30^\circ=\frac{1}{2}
$$
Using the relationships between orthonormal vectors,
$$
\hat{i}\cdot\hat{j}=\hat{j}\cdot\hat{i}=\hat{i}^\prime\cdot\hat{j}^\prime=\hat{j}^\prime\cdot\hat{i}^\prime=0
$$
$$
\hat{i}\cdot\hat{i}=\hat{j}\cdot\hat{j}=\hat{i}^\prime\cdot\hat{i}^\prime=\hat{j}^\prime\cdot\hat{j}^\prime=1
$$
##### Question 2a
*Change of basis from* $R\to R^\prime$
$$
\vec{v}\cdot\hat{i}^\prime=\vec{v}^\prime_i
$$
$$
\implies \vec{v}^\prime_i=\sqrt{3}\cdot\frac{\sqrt{3}}{2}-(-1)\frac{1}{2}
$$
$$
\implies\vec{v}^\prime_i=\frac{3}{2}+\frac{1}{2}=2\text{m}\cdot\text{s}^{-1}
$$
##### Question 2b
*Change of basis from* $R\to R^\prime$
$$
\vec{v}\cdot\hat{j}^\prime=\vec{v}^\prime_j
$$
$$
\implies \vec{v}^\prime_j=\frac{1}{2}\cdot\sqrt{3}+\frac{\sqrt{3}}{2}(-1)
$$
$$
\implies \vec{v}^\prime_j=\frac{\sqrt{3}}{2}-\frac{\sqrt{3}}{2}=0\text{m}\cdot\text{s}^{-1}
$$
##### Question 2c
The tilted frame $R^\prime$ is more suitable as it removes one component, the $j$ component.
#### Question 3
$$
\text{Law of composition of velocities}:\vec{v}(A|B)=\vec{v}(A|M)+\vec{v}(M|B)
$$
Given a basis $(\hat{i},\hat{j})$,
Bob has velocity $\vec{v}({B|M})=(3\text{m}\cdot\text{s}^{-1})\hat{i}$ relative to Matt with velocity $0$.
Tim has velocity $\vec{v}(T|M)=-(12\text{m}\cdot{s}^{-1})\sin[6\text{s}^{-1}t]\hat{i}+(12\text{m}\cdot\text{s}^{-1})\cos[(6\text{s}^{-1})t]\hat{j}$ relative to Matt with velocity $0$.
##### Question 3a
By using the above law of composition of velocities, determine the relative velocities of Matt and Tim relative to Bob.
$$
\vec{v}(M|B)=-\vec{v}(B|M)=(-3\text{m}\cdot\text{s}^{-1})\hat{i},
$$
$$
\vec{v}(T|B)=\vec{v}(T|M)+\vec{v}(M|B)
$$
$$
\implies\vec{v}(T|B)=-(12\text{m}\cdot{s}^{-1})\sin[6\text{s}^{-1}t]\hat{i}+(12\text{m}\cdot\text{s}^{-1})\cos[(6\text{s}^{-1})t]\hat{j}+(-3\text{m}\cdot\text{s}^{-1})\hat{i}
$$
$$
\implies\vec{v}(T|B)=-(3\text{m}\cdot\text{s}^{-1}+(12\text{m}\cdot{s}^{-1})\sin[(6\text{s}^{-1})t])\hat{i}+(12\text{m}\cdot\text{s}^{-1})\cos[(6\text{s}^{-1})t]\hat{j}
$$
##### Question 3b
By using the above law of composition of velocities, determine the relative velocities of Matt and Bob relative to Tim.
$$
\vec{v}(M|T)=-\vec{v}(T|M)=(12\text{m}\cdot{s}^{-1})\sin[6\text{s}^{-1}t]\hat{i}-(12\text{m}\cdot\text{s}^{-1})\cos[(6\text{s}^{-1})t]\hat{j}
$$
$$
\vec{v}(B|T)=\vec{v}(B|M)+\vec{v}(M|T)
$$
$$
\implies\vec{v}(B|T)=(3\text{m}\cdot\text{s}^{-1})\hat{i}+(12\text{m}\cdot{s}^{-1})\sin[6\text{s}^{-1}t]\hat{i}-(12\text{m}\cdot\text{s}^{-1})\cos[(6\text{s}^{-1})t]\hat{j}
$$
$$
\implies\vec{v}(B|T)=(3\text{m}\cdot\text{s}^{-1}+12\text{m}\cdot{s}^{-1})\sin[6\text{s}^{-1}t]\hat{i}-(12\text{m}\cdot\text{s}^{-1})\cos[(6\text{s}^{-1})t]\hat{j}
$$
#### Question 4
Two blocks $B_1$ and $B_2$ with respective masses $m_1=5\text{ kg}$ and $m_2=20\text{ kg}$ are being pushed by a constant force $\vec{F}=F_\hat{i}$ applied on $B_1$. The two blocks moves with the same acceleration $\vec{a}=1\text{ m}\cdot\text{s}^{-2}\hat{i}$ as see from a Galilean frame $(O,\hat{i},\hat{j})$. As shown below,
![[Answers to Mechanics Practical 3 2023-11-03 16.48.56.excalidraw]]

##### Question 4a
By considering $B=B_1+B_2$, we can determine the force $\vec{F}=F_\hat{i}$.
$$
\Sigma F=ma
$$
$$
\implies\vec{F}=(m_1+m_2)\cdot\vec{a}
$$
$$
\implies\vec{F}=(25\text{ N})\hat{i}
$$
##### Question 4b
By considering $B_1$, we can determine the force $\vec{F}_{B_2\to B_1}$ exerted by $B_2$ on $B_1$.
$$
\vec{F}_\hat{i}-\vec{F}_{B_2\to B_1}=m_1\cdot\vec{a}
$$
$$
\implies (25\text{ N})\hat{i}-\vec{F}_{B_2\to B_1}=5\hat{i}
$$
$$
\therefore \vec{F}_{B_2\to B_1}=(20\text{ N})\hat{i}
$$
##### Question 4c
By Newton' third law, we can determine the force $\vec{F}_{B_1\to B_2}$ exerted by $B_1$ on $B_2$.
$$
\vec{F}_{B_1\to B_2}=-\vec{F}_{B_2\to B_1}
$$
$$
\therefore \vec{F}_{B_1\to B_2} = -(20\text{ N})\hat{i}
$$

#### Etc.
