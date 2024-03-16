> Ideas of Mathematical Proof Cheat Sheet by William Fayers :)

### Simul. inequalities -> interval solution

$$
\begin{align*}

\begin{cases}
\text{inequality one} \\
\text{inequality two}
\end{cases}
&\iff
\begin{cases}
\text{factorised inequality one} \\
\text{factorised inequality two}
\end{cases}\\
&\iff
\begin{cases}
\text{solutions in interval notation}\\
\text{solutions in interval notation}
\end{cases}
\end{align*}
$$

Then, draw out sketches of each solution set interval, finding their overlap.

$$
\boxed{\therefore \text{solutions as a union of intervals}}
$$

### Mapping -> injective, surjective?

$$
f:\mathbb{N}\times\mathbb{N}\to\mathbb{N},f((a,b))=\ldots \text{is...}
$$

- (Not) injective: $\text{example of two inputs can give the same output}$ OR $\text{assuming two unique inputs have equal outputs}$, $\text{prove that the inputs must also be equal simultaneously}$.
- (Not) surjective: $\text{example of an output in the set that can't be made}$ OR $\text{prove that any output in the set can be made}$.

### Prove an equivalence -> visualise classes (and list elements)

$\sim$ is an equivalence relation if it is...

- Reflexive: for any $x$ it is clear that $x=x$ (input can be related to itself).
- Symmetric: if $x\sim y$, then $x=y$. By the definition of equality, $y=x$, hence $y\sim x$ (a relation can be flipped).
- Transitive: if $x\sim y$ and $y\sim z$, then $x=y$ and $y=z$. By the transitive property of equality, $x=z\implies x\sim z$ (you can connect through middle relations).

$$
\therefore\sim \text{is an equivalence relation. }\square
$$

Plot relations, where the axes take the values of every possible input and output (respectively), and a dot is plotted where two elements relate. Include the empty set $\emptyset$ either as the origin or as the first element of both axes. **Unless it specifies a co-ordinate plane, then plot it like a graph.**

Find all elements that are equivalent under the relation - give the same output - and list these as a set.

### Prove an order relation -> visualise subset

For $A=\set{1,2,3,4,5,6,7,8,9}$ and $aRb$ if $b|a$ ($a$ divides $b$),

- $R$ is transitive: $b|a \text{ and }a|c\implies b|c$ , hence $aRb,bRc\implies aRc$ (you can connect through middle relations).
- $R$ is reflexive: $a|a$ for any $a\in A$, hence $aRa$ for any $a\in A$.
- $R$ is not symmetric: $b|a\centernot\implies a|b$, e.g. $9|3$ but $3\centernot|9$.
- $R$ is antisymmetric: $b|a \text{ and }a|b\implies a=b$, hence $aRb \text{ and }bRa\implies a=b$.

$$
\therefore R\text{ is a partial order relation }\square
$$

Plot relations, where the axes take the values of every possible input and output (respectively), and a dot is plotted where two elements relate. Include the empty set $\emptyset$ either as the origin or as the first element of both axes.

### Bijective mapping -> same cardinality demonstration

The bijective mapping $f:\mathbb{Z}\to \mathbb{N}$ can be defined as

$$
\begin{cases}
2n & \text{if }n\ge0 \\
-2n+1 & \text{if }n\lt0
\end{cases}
$$

This maps non-negative integers to positive even integers, and negative integers to positive odd integers. Hence, the mapping is injective and surjective.

A bijective mapping $f:\mathbb{Z}\to \mathbb{N}$ can be defined, hence $\mathbb{Z}$ and $\mathbb{N}$ have the same cardinality. $\square$

### Create truth tables -> categorise tautologies/contradictions

Per statement, create a truth table (where the individual elements come first, then build up the left hand side combinations and the right hand side combinations - the number of individual elements determine the number of rows, as each row needs to create every possible combo - e.g. $2$ elements, $4$ rows; $3$ elements, $8$ rows; $n$ elements, $2^n$ elements):

| $P$ | $Q$ | \|\| | $P\lor Q$ | $\neg Q$ | $P\land\neg Q$ |
| :-: | :-: | :--: | :-------: | :------: | :------------: |
| $T$ | $T$ | \|\| |    $T$    |   $F$    |      $F$       |
| $T$ | $F$ | \|\| |    $T$    |   $T$    |      $T$       |
| $F$ | $T$ | \|\| |    $T$    |   $F$    |      $F$       |
| $F$ | $F$ | \|\| |    $F$    |   $T$    |      $F$       |
Other common expressions include those with $\implies$, which is only false when if $T\implies F\equiv \neg P\lor Q$. Also note that they share properties with set notation.

Then, classify if the statement is a tautology (only $T$ in a column) or a contradiction (only $F$ in a column) - if any are either.

### Evaluate logical statements -> true or false

Either simplify the statement(s), prove the statements (if $\forall$, demonstrate a proof; if $\exists$, give one example) , or provide a counterexample to them.

### Prove by contradiction -> Cantor diagonal argument

Suppose the opposite, that is, that there is a bijection $f:\mathbb{N}\to S$, where $S$ as a vertical list is

$$
\begin{matrix}f(1)=(a_{11}, & a_{12}, & a_{13}, & a_{14}, & a_{15}, & \ldots) \\ f(2)=(a_{21}, & a_{22}, & a_{23}, & a_{24}, & a_{25}, & \ldots) \\ f(3)=(a_{31}, & a_{32}, & a_{33}, & a_{34}, & a_{35}, & \ldots) \\ f(4)=(a_{41}, & a_{42}, & a_{43}, & a_{44}, & a_{45}, & \ldots) \\f(5)=(a_{51}, & a_{52}, & a_{53}, & a_{54}, & a_{55}, & \ldots) \\ \vdots\quad\quad\quad\vdots & \vdots & \vdots & \vdots & \ddots & \ddots & \ddots\end{matrix}
$$

We now define another sequence $(b_{1},b_{2},b_{3},\ldots)$ by the following rule:

$$
b_{i}=1\text{ or }2, \text{ but }b_{i}\ne a_{ii}:b=\begin{cases}
1 & \text{if }a_{ii}=2 \\
2 & \text{if }a_{ii}=1
\end{cases}
$$

Then this sequence consists of $1$  and $2$, so is in the set $S$, but does not lie in the list: it cannot be $f(i)$ since $b$ differs in the $i$th element by our construction.

This is a contradiction with the assumption that $f$ was a bijection onto the entire set $S$. Therefore our assumption that there is a bijection between $\mathbb{N}$ and $S$ was false, which precisely means that there cannot be such a bijection, as required. $\square$

### Prove by contradiction -> number is irrational

Suppose the opposite: $\sqrt{5}\in \mathbb{Q}$, that is, $\sqrt{5}=\frac{m}{n}$ for $m,n\in \mathbb{Z}$ and $\text{g.c.d.}(m,n)=1$.

Squaring both sides: $5=\frac{m^{2}}{n^{2}}\iff5n^{2}=m^{2}$, hence $m$ is divisible by $5$ such that $m=5a:a\in \mathbb{Z}$, due to the properties of squares and primes.

Substituting into the original assumption: $5n^{2}=(5a)^{2}=25a^{2}\iff n^{2}=5a^{2}$, hence $n$ is also divisible by $5$ such that $n=5b:b\in \mathbb{Z}$, due to the properties of squares and primes.

This is a contradiction with the initial assumption $\text{g.c.d.}(m,n)=1$ as both $m,n$ are divisible by $5$. The contradiction means that the assumption $\sqrt{5}\in \mathbb{Q}$ is false, hence the assertion that $\sqrt{5}$ is an irrational number is true.

*Similarly, you can prove $log_{10}7$ is irrational.*

### Prove by induction -> sequence

$$
\begin{align*}
1^{\circ}&\quad\text{For }n=3,6+2(4)-4=10=2^{3}+2,\\
&\quad\text{For }n=4,10+2(6)-4=18=2^{4}+2.\\
2^{\circ}&\quad\text{Suppose now that the assertion is true for }n=k:\\
&\quad a_{k}=2^{k}+2 \text{ and }a_{k-1}=2^{k-1}+2.\\
\end{align*}
$$

$$
\text{Now, we prove for n=k+1},
$$

$$
\begin{align*}
a_{k+1}&= a_{k}+2a_{k-1}-4 & \text{ by definition}\\
&= (2^{k}+2)+2(2^{k-1}+2)-4 & \text{ by the ind. hyp.}\\
&= 2^{k}+2+2^{k}+4-4\\
&= 2\cdot2^{k}+2\\
&= 2^{k+1}+2
\end{align*}
$$

$$
\begin{align*}
\therefore&\text{We derived the assertion for }n=k+1. \text{ From }1^\circ\\
& \text{and }2^{\circ}, \text{the assertion follows for all }n\ge3 \text{ by E.A.M.I. }\square
\end{align*}
$$

### Prove by induction -> inequality

$$
\begin{align*}
1^{\circ}&\quad \text{For }k=2,6^{2}=36\gt15\cdot2=30,\text{ which is true.}\\
2^{\circ}&\quad \text{Suppose now that the assertion is true for }k=n:\\
&\quad  6^{n}\gt15n.
\end{align*}
$$

$$
\text{Now, we prove for }k=n+1
$$

$$
\begin{align*}
6^{n+1}&=6\cdot6^{n}&\text{by definition}\\
&\gt 6\cdot 15n&\text{by ind. hyp.}\\
&=90n\\
&=15n+75n\\
&\gt15n+75\\
&\gt15(n+1)
\end{align*}
$$

$$
\begin{align*}
\therefore&\text{We derived the assertion for }k=n+1. \text{ From }1^{\circ}\\
&\text{and }2^{\circ},\text{ the assertion follows for all }k\ge2\text{ by E.A.M.I. }\square
\end{align*}
$$

### Prove by induction -> divisibility

$$
\begin{align*}
1^{\circ}&\quad \text{For }n=1, 2^{2(1)+1}+1=9\text{ is indeed divisible by 3}.\\
2^{\circ}&\quad \text{Suppose now that the assertion is true for }n=k:\\
&\quad 2^{2k+1}+1=3a \text{ for }a\in \mathbb{Z}.
\end{align*}
$$

$$
\text{Now, we prove for n=k+1},
$$

$$
\begin{align*}
2^{2k+3}+1&= 2^{2}\cdot2^{2k+1}+1\\
&= 4\cdot2^{2k+1}+1\\
&= 3\cdot2^{2k+1}+(2^{2k+1}+1)\\
&= 3\cdot2^{2k+1}+3a&\text{by the ind. hyp.}\\
&= 3(a+2^{2k+1})\\
&:a+2^{2k+1}\in \mathbb{Z}
\end{align*}
$$

$$
\begin{align*}
\therefore&\text{We derived the assertion for }n=k+1.\text{ From }1^{\circ}\\
&\text{and }2^{\circ}, \text{ the assertion follows for all }n \text{ by A.M.I. }\square
\end{align*}
$$

### Properties of set operations -> Expression simplification

$$
\begin{align*}
\overline{\overline{A}\cap(B\cup A)}&= A\cup\overline{(B\cup A)}&\text{by De Morgan's Law}\\
&= A\cup(\overline{B}\cap\overline{A})&\text{by De Morgan's Law}\\
&= (A\cup\overline{B})\cap(A\cup\overline{A})&\text{by the dist. prop.}\\
&=(A\cup \overline{B})\cap \mathscr{U}\\
&= A\cup \overline{B}
\end{align*}
$$
### SUDOKU 🥚🥚🥚

![[sudoku.png]]
