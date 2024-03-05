## Topics

- Relations,
- Mappings,
- Cardinalities,
- Logical operations,
- Proofs by contradiction.

## In-Class Material

### Practical Worksheets

- [[Proof Practical Class, Week 21]],
- [[Proof Practical Class, Week 22]],
- [[Proof Practical Class, Week 23]],
- [[Proof Practical Class, Week 24]].

### Slides

- [[Proof Prelim Slides (Week 21).pdf]],
- [[Proof Prelim Slides (Week 22).pdf]],
- [[Proof Prelim Slides (Week 23).pdf]],
- [[Proof Prelim Slides (Week 24).pdf]] (up to page 69).

## Past Papers

> Note: These are for the final exams, hence are twice as long as the mid-term papers - take this into account when testing the time taken to complete the exam(s).

- [[Proof PP (2021).pdf]],
- [[Proof PP (2021) - checks.pdf]].

- [[Proof PP (2022).pdf]],
- [[Proof PP (2022) - checks.pdf]].

- [[Proof PP (2023).pdf]],
- [[Proof PP (2023) - checks.pdf]].

## All Relevant Questions (summarised)

... (irrelevant questions)

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

42. Draw the mapping $g: \mathbb{R}\to \mathbb{R}$ on the $(x,y)$ plane defined by the rule following rule - is it injective, surjective?

$$
g(x)=\text{largest integer}\le x
$$

43. For the following mapping, what is the image of $g$? What is the full inverse image $g^{-1}(2)$?

$$
g(x)=\text{largest integer}\le x
$$

44. Given any mapping $f:A\to B$, prove that the relation $\sim$ on $A$ defined by $a_{1}\sim a_{2}$ if $f(a_{1})=f(a_{2})$ is an equivalence relation. What are the equivalence classes?

45. Prove that the following sets have the same cardinality by producing explicitly a bijection between the sets and describing this bijection...
	1. ... by a formula for $|(-\infty, 0]|=|[3,+\infty)$;
	2. ... by representing the set on the right as a sequence: $|\mathbb{N}|=|\set{a,b,c}\cup \mathbb{N}|$;
	3. ... by any method: $|\set{a,b}\times \mathbb{Z}|=|\mathbb{Z}|$;
	4. ... by using a sequence of points: $|[0,1]|=|(0,1)|$;
	5. ... geometrically: $|(0,1)|=|(0,\infty)|$.

46. Use [[this theorem]] to prove that $|\mathbb{N}\times \mathbb{N}\times \mathbb{N}|=\aleph_{0}$.

47. Let $S$ be the set of all sequences of the form $(a_{1},a_{2},a_{3},\ldots)$, where every $a_{i}$ is either $A$ or $B$. Use Cantor's "diagonal method" to prove that the set $S$ is not countable.

48. Recall that $\set{0,1}\times\set{0,1}\times\set{0,1}$ consists of triples of $1$s and $0$s, and $\mathscr{P}(\set{a,b,c})$ is the set of all subsets of $\set{a,b,c}$. Consider the following mapping, in which a subset $X\subset \set{a,b,c}$ is mapped to a string of length $3$ consisting of $0$s and $1$s depending on which of the elements $a,b,c$ belong to $X$ (with $1$ indicating yes and $0$ indicating no). Write the images $f(\emptyset)$, $f(\set{a,c})$, $f(\set{b})$. Is $f$ a bijection?

$$
f:\mathscr{P}(\set{a,b,c})\to\set{0,1}\times\set{0,1}\times\set{0,1}
$$

49. Use [[this theorem]] to show that any set consisting of pairwise disjoint intervals of the real line (each of $\text{length}>0$) is countable.