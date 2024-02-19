[[Proof Practical Class, Week 19]]
[[Proof Tutorial Class, Week 20]]
[[Proof Practical Class, Week 20]]
[[Proof Tutorial Class, Week 21]]
[[Proof Practical Class, Week 21]]
[[Proof Tutorial Class, Week 22]]
[[Proof Practical Class, Week 22]]

1. Use mathematical induction to prove that $5^{n}+3$ is divisible by $4$ for all positive integers $n$.

2. Use mathematical induction to prove that $11^{n}-4^{n}$ is divisible by $7$ for all positive integers $n$.

3. Use the method of undetermined coefficients to guess a formula for $1 + 3 + 5 + \cdots + (2n-1)$ as a quadratic expression in $n$, and then use mathematical induction to prove this formula.

4. Use mathematical induction to prove the following for any positive integer $n$,
$$
\frac{1}{1\cdot2\cdot3} + \frac{1}{2\cdot3\cdot4} + \cdots + \frac{1}{n(n+1)(n+2)} = \frac{1}{4} - \frac{1}{2(n+1)(n+2)}
$$

5. Use mathematical induction to prove that $n!>3^{n}$ for any $n\ge7$.

6. What is wrong in the following "proof" that all men are bald? We use induction on the number of hairs on the head, $n$:
	1. If $n=1$, then a man with just one hair is of course bald.
	2. Suppose the assertion is true for $n=k$, that is, having $k$ hairs means the man is bald. Now, if he has $k+1$ hairs, then it is just one more, so, surely, does not transform a man from being bald to non-bald.
	3. Thus, by the Axiom of Mathematical Induction, a man is bald if he has $n$ hairs, for any $n$.

7. Prove by induction that for $x\ne1$ we have the following, for any positive integer $n$: $$1+x+x^{2}+\cdots+x^{n-1} = \frac{1-x^{n}}{1-x}$$

8. Use mathematical induction to prove the following for all positive integers $n$: $$\frac{1}{2} + \frac{2}{2^{2}} + \frac{3}{2^{3}} + \cdots + \frac{n}{2^{n}} = 2 - \frac{n+2}{2^{n}}$$

9. Use mathematical induction to prove that $n^{3}<2^{n}$ for any $n\ge10$.

10. Prove by induction that $6^{n}-1$ is divisible by $5$ for any $n\in \mathbb{N}$.

11. Suppose that $a$ is a real number such that $a + \frac{1}{a}$ is an integer. Use Cumulative Induction to prove that then $a^{n} + \frac{1}{a^{n}}$ is also an integer for every $n=1,2,3,\ldots$.

12. Use induction on $n$ to prove that any 'map' formed by intersections of $n$ straight lines can be coloured in two colours in such a way that no two countries of the same colour have a common boundary segment. (Each country is coloured in one colour; corner points between two countries of the same colour are allowed.)

13. Let $(a_{i})_{i\in \mathbb{N}}$ be a sequence defined recursively as $a_{1}=1$ and $a_{i+1}=3a_{i}-1$. Use induction to prove that $a_{n}=\frac{3^{n-1}+1}{2}$ for all $n\in \mathbb{N}$.

14. Let $(b_{i})_{i\in \mathbb{N}}$ be a sequence defined recursively as $b_{1}=0$, $b_{2}=1$, and $b_{i}=3b_{i-1}-2b_{i-2}$ for $i\ge3$. Use induction to prove that $b_{n}=2^{n-1}-1$ for all $n\in \mathbb{N}$.

15. Let the universal set be $\mathscr{U}=\{x\in \mathbb{Z}:-9\le x\le 9\}$, and let $\mathbb{A}$ be the set of all odd integers in $\mathscr{U}$, let $\mathbb{B}=\{x\in \mathscr{U}:x^{2}>25\}$, and $\mathbb{C}=\{x\in \mathscr{U}:x<0\}$. Determine each of the following sets and list their elements:
	1. $\mathbb{A}\cap \mathbb{B}\cap \mathbb{C}$;
	2. $\mathbb{A}\cap \overline{\mathbb{B}}$;
	3. $\mathbb{A}\cap \overline{\mathbb{C}}$;
	4. $\mathbb{B}\cup \mathbb{C}$.

16. Use Venn diagrams to prove that $\mathbb{A}\cup(\mathbb{B}\cap \mathbb{C})=(\mathbb{A}\cup \mathbb{B})\cap(\mathbb{A}\cup \mathbb{C})$ for any sets $\mathbb{A}$, $\mathbb{B}$, and $\mathbb{C}$.

17. Use the properties of operations on sets to simplify the expression $\mathbb{B}\cup\overline{(\overline{\mathbb{A}}\cap \overline{\mathbb{B}})}$.

18. Solve the simultaneous system of inequalities using intersection of solutions of individual inequalities and write the solution as a set:
$$
\begin{cases}
x^{2}+x-6&\ge 0 \\
x^{2}-7x+10&\ge 0
\end{cases}
$$

19. Prove, based on the definitions, that $\overline{(\mathbb{A}\cap \mathbb{B})}=\overline{\mathbb{A}}\cup\overline{\mathbb{B}}$.

20. Use mathematical induction to prove that every positive integer $n\ge8$ can be represented as $n=3a+5b$ where $a$ and $b$ are non-positive integers.

21. Consider the function $f(x)= \frac{x}{x+1}$, and define recursively a sequence of functions $f_{1}(x)=f(x)$ and $f_{i+1}(x)=f(f_{i}(x))$.

22. Use mathematical induction to prove that $2^{n}>100n$ for any $n\ge10$.

23. Where is the mistake in the following "proof" that all triangles have the same area?
    >Obviously, it is sufficient to prove that, given any $n$ triangles, they all have the same area. We use induction on $n$. Indeed,
>1. If we have one triangle, the assertion is of course true.
>2. Suppose the assertion is true for $n=k$. Consider any $k+1$ triangles $T_{1},\ldots,T_{k+1}$. Apply the induction hypothesis to the first $k$ of the triangles: $T_{1},\ldots,T_{k+1}$ all have the same area. Then apply the induction hypothesis to the last $k$ of them: $T_{2},\ldots,T_{k+1}$ all have the same area. Then obviously all $k+1$ triangles $T_{1},\ldots,T_{k+1}$ have the same area: area of $T_{1}=\text{area of }T_{2}=\dots=\text{area of }T_{k}=\text{area of }T_{k+1}$.
>Thus, by the Axiom of Mathematical Induction, the assertion is true for all $n$, and therefore all triangles have the same area.

24. How does one tie a goat so it can eat grass within exactly a semicircle? It can be leashed multiple times, with several pegs. For example, one peg and a leash mean that the goat eats within a circle. It is also allowed to string one rope tightly between two pegs, and to tie the goat with a leash to a small ring sliding on the first rope. *Hint: use intersections of sets*.

25. Use a diagram to prove the property $A\times(B\cup C)=(A\times B)\cup(A\times C)$.

26. Let $A=\{1,2,\ldots,100\}$ be the set of all integers from 1 to 100. Let $R$ be a relation on $\mathscr{P}(A)$ (the set of all subsets of $A$) defined as $BRC$ if $|B|\le|C|$. Determine if $R$ is...
	1. ...transitive,
	2. ...reflexive,
	3. ...symmetric,
	4. ...antisymmetric,
    and in each case giving a proof if yes, or a counterexample if not. Hence state whether $R$ is an order, or an equivalence, or neither.

27. On the set $S=\{1,2,3,4,5,6,7,8,9\}$, consider the relation $R$ defined as $aRb$ if $a|b$ (that is, $a$ divides $b$). Draw the diagram $R$ as a subset of $S\times S$.

28. Let $\sim$ be a relation on the set $\mathbb{R}\times \mathbb{R}$ defined by $(x,y)\sim(a,b)$ if $y-|x|=b-|a|$.
	1. Show that $\sim$ is an equivalence.
	2. What is the equivalence class of $(2,-3)$ with respect to this equivalence $\sim$?

29. Consider the order relation on $\mathbb{N}$ defined by divisibility: $a|b$ (when $b=ak$ for $k\in \mathbb{N}$). What are the infimum and supremum of the set $S=\{8,12,36\}$? Does this set have the greatest element? What about the smallest element?

30. Consider the lexicographical order $\le_{L}$ on $\mathbb{R}\times \mathbb{R}$, which means that by definition $(a,b)\le_{L}(c,d)$ if either $a<c$ (while $b$ and $d$ can be any), or $a=c$ and $b\le d$.
	1. Find the supremum (least upper bound), if it exists, with respect to $\le_{L}$ of the set $D=\{(x,y):x^{2}+y^{2}\le1\}$ (the disc of radius $1$ with centre at the origin, including the unit circle).
	2. Find the supremum (least upper bound), if it exists, with respect to $\le_{L}$ of the set $D_{0}=\{(x,y):x^{2}+y^{2}\lt1\}$ (the disc of radius $1$ with centre at the origin, without the boundary unit circle).

31. On the set $S=\mathbb{N}\times \mathbb{N}$, consider the relation $\sim$ defined as $(m_{1},n_{1})\sim(m_{2},n_{2})$ if $m_{1}\cdot n_{2}=m_{2}\cdot n_{1}$. Show that $\sim$ is an equivalence. Describe the equivalence class of $(1,2)$ with respect to this equivalence $\sim$.

32. Give an example of finite sets $A, B, X, Y$ such that $(A\times Y)\cup(B\times Y)\ne (A\cup B)\times(X\cup Y)$. *Hint: try small sets, say, subsets of ${1,2,3,4}$.*

33. For a fixed set $S$, consider $\mathscr{P}(S)$ (set of all subsets of $S$) ordered by inclusion. For $A,B\subset S$, what is $\sup\set{A,B}$ with respect to this order? What is $\inf\set{A,B}$?

34. How to tie a goat so as it can eat grass exactly within a square? It is allowed to use several leashes, with several pegs. For example, one peg and leash mean that the goat eats within a circle. It is also allowed to string one rope tightly between two pegs, and to tie the goat with leash to as small ring sliding on the first rope. *Hint: use intersections of sets.

35. For which of the following pairs $A,B\subset \mathbb{R}$ does the relation $f=\set{(x,y):x=|y|}\subset A\times B$ define a mapping $f:A\to B$? Give reasons to your answers:
	1. $A=\mathbb{R},\quad B=[0,\infty)$.
	2. $A=[0,\infty),\quad B=\mathbb{R}$.
	3. $A=[0,\infty),\quad B=(-\infty,0]$.

36. Given the following mappings, determine which of the composites $f\circ g,g\circ f$ is defined, and write the resulting mapping in standard form:

$$
\begin{matrix}
f: \mathbb{Z}\times \mathbb{Z}\to \mathbb{R}, f((x,y))=x+y,\quad\text{and} \\ 
g: \mathbb{R}\to \mathbb{R}, g(a)=a^{2}+1
\end{matrix}
$$

37. For each of the following mappings, determine whether it is injective and/or surjective:
	1. $f:\mathbb{Z}\to \mathbb{N},f(k)=k^{2}+2$.
	2. $f: \mathbb{R}\times \mathbb{R}\to \mathbb{R}, f((x,y))=x+y$.
	3. $f: \mathbb{N}\times \mathbb{N}\to \mathbb{N}, f((m,n))=2^{m-1}\cdot(2n-1)$.

38. Let $A=\mathscr{P}(\set{u,v,w})$ be the set of all subsets of $\set{u,v,w}$ and let $f:A\to A, f(x)=X\cap\set{u,v}$. Draw the diagram of the Cartesian product $A\times A$ and indicate $f$ as a subset of $A\times A$. What is the image of $f$?

39. Find the image of the mapping $f:\mathbb{R}\to \mathbb{R}, f(x)=\frac{1}{x^{2}+5}$.

40. Show that $f:[3,\infty)\to(0,1],f(x)=\frac{2}{x-1}$ is a bijection and find the inverse mapping $f^{-1}$ - indicating its domain and image.

41. Let $f:\mathbb{R}\to \mathbb{R},f(x)=2x+1$. Define recursively the mappings $F_{1}=f$ and $F_{k+1}=f\circ F_{k}$ for all $k\in \mathbb{N}$. Compute several first mappings, conjecture an expression for $F_{n}$, and prove it by induction.