[[Ideas of Mathematical Proof - Assignment.pdf]]

> Complete as a digital document here first to complete my solutions in a neat, logical, elegant manner, then copy them onto a physical A4 handwritten document to then scan and turn in.


### Question One

#### Question

Use mathematical induction to prove that $5^{2n-1}+1$ is divisible by $6$ for any $n\in \mathbb{N}$.

#### Solution

$$
\begin{align*}
1^{\circ}&\text{ For }n=1, 5^{2(1)-1}+1=6\text{ is indeed divisible by }6.\\
2^{\circ}&\text{ Suppose now that the assertion is true for }n=k:\\
& 5^{2k-1}+1=6a \text{ for }a\in \mathbb{Z}\\
\end{align*}
$$

$$
\text{Now, we prove for }n=k+1
$$

$$
\begin{align*}
5^{2k+1}+1&=5^{2}\cdot5^{2k-1}+1\\
&= 24\cdot5^{2k-1}+(5^{2k-1}+1)\\
&= 6(4\cdot5^{2k-1})+6a \text{ by the ind. hyp.}\\
&= 6(4\cdot5^{2k-1}+a):4\cdot5^{2k-1}+a\in \mathbb{Z}
\end{align*}
$$

$$
\boxed{5^{2n-1}+1 \text{ is divisible by }6 \text{ for any }n \in N \text{ by A.M.I. }\square}
$$

### Question Two

#### Question

Let $(b_{i})_{i\in\mathbb{N}}$ be a sequence defined recursively as $b_{1}=2$, $b_{2}=4$, and $b_{i}=2b_{i-1}+3b_{i-2}-4$ for all $i\ge3$. Use mathematical induction to prove that $b_{n}=3^{n-1}+1$ for all $n\in \mathbb{N}$.

#### Solution

$$
\begin{align*}
1^{\circ}&\text{ For }n=1, 3^{1-1}+1=3^{0}+1=1+1=2=b_{1}\\
&\text{For }n=2, 3^{2-1}+1=3^{1}+1=3+1=4=b_{2}\\
2^{\circ}&\text{ Suppose now that the assertion is true for  }n=k:\\
&b_{k}=3^{k-1}+1 \text{ and } b_{k-1}=3^{k-2}+1.\\
\end{align*}
$$

$$
\text{Now, we prove it for }n=k+1:
$$

$$
\begin{align*}
b_{k+1} &= 2b_{k} + 3b_{k-1} - 4\\
&= 2(3^{k-1}+1) + 3(3^{k-2}+1) - 4 \text{ by the ind. hyp.}\\
&= 2\cdot3^{k-1} + 2 + 3\cdot3^{k-2} + 3 - 4\\
&= 2\cdot3^{k-1} + 3^{k-1} + 1\\
&= 3\cdot3^{k-1} + 1\\
&= 3^{k} + 1
\end{align*}
$$

$$
\boxed{b_{n} = 3^{n-1}+1 \text{ for all } n \in \mathbb{N} \text{ by A.M.I. } \square}
$$

### Question Three

#### Question

Use mathematical induction to prove that $3^{n}\gt 4n^{2}$ for all positive integers $n\ge 4$.

#### Solution

$$
\begin{align*}
1^{\circ}&\text{ For }n=4, 3^{4} = 81 > 4\cdot4^{2} = 64, \text{ which is true.}\\
2^{\circ}&\text{ Suppose the inequality is true for }n=k, \text{ i.e., } 3^{k} > 4k^{2}.\\
\end{align*}
$$

$$
\text{Now, we prove it for }n=k+1:
$$

$$
\begin{align*}
3^{k+1} &= 3\cdot3^{k}\\
&> 3\cdot4k^{2} \text{ by the ind. hyp.}\\
&= 12k^{2}\\
&= 4k^{2} + 8k^{2}\\
&> 4k^{2} + 4\cdot2k\\
&= 4k^{2} + 8k + 16 - 16\\
&= 4(k^{2} + 2k + 4) - 16\\
&= 4(k + 1)^{2} - 16\\
&> 4(k + 1)^{2}\\
\end{align*}
$$

This step shows that if $3^{k} > 4k^{2}$ is true, then $3^{k+1} > 4(k+1)^{2}$ is also true, thus completing the inductive step.

$$
\boxed{3^{n} > 4n^{2} \text{ for all positive integers } n \ge 4 \text{ by A.M.I. } \square}
$$

### Question Four

#### Question

Let the universal set be $\mathscr{U}=\set{x \in \mathbb{Z} : -8\le x\le 8}$, let $A$ be the set of all even integers in $\mathscr{U}$, let $B = \set{x \in \mathscr{U}:x^{2}<9}$, and $C=\set{x \in \mathscr{U} : x<0}$. Determine each of the following sets and list their elements:

1. $A\cup B$,
2. $A\cap\overline{C}$,
3. $A\cap\overline{B}$.

#### Solution

$A=\set{-8,-6,-4,-2,0,2,4,6,8}$

$B=\set{-2,-1,0,1,2}$

$C=\set{-8,-7,-6,-5,-4,-3,-2,-1}$

Hence,

$A\cup B=\set{-8,-6,-4,-2,-1,0,1,2,4,6,8}$

$A\cap\overline{C}=\set{0,2,4,6,8}$

$A\cap\overline{B}=\set{-8,-6,-4,4,6,8}$

### Question Five

#### Question

Use the properties of operations on sets to simplify the expression:

$$
\overline{(\overline{A}\cap\overline{B})\cup B}
$$

#### Solution

Using De Morgan's Laws...

$$
\begin{align*}
\overline{(\overline{A}\cap\overline{B})\cup B}&=\overline{\overline{(A\cup B)}\cup B}\\
&= (A\cup B)\cap\overline{B}\\
&= (A\cap\overline{B})\cup(B\cap\overline{B})\\
&= (A\cap\overline{B})\cup\emptyset\\
&= A\cap\overline{B}
\end{align*}
$$

### Question Six

#### Question

Solve the (simultaneous) system of inequalities using the intersection of solutions of individual inequalities and write the solution as a union of intervals:

$$
\begin{cases}
x^{2}-5x+6\ge 0 \\
x^{2}-x\gt0
\end{cases}
$$

#### Solution

$$
\begin{align*}
\begin{cases}
x^{2}-5x+6\ge 0 \\
x^{2}-x\gt0
\end{cases}&\iff\begin{cases}
(x-3)(x-2)\ge0\\
x(x-1)>0
\end{cases}\\
&\iff \begin{cases}
(-\infty,2]\cup[3,\infty)\\
(-\infty,0)\cup (1,\infty)
\end{cases}\\
&\iff ((-\infty,2]\cup[3,\infty))\cap((-\infty,0)\cup (1,\infty))\\
&\iff (-\infty,0)\cup(1,2]\cup[3,\infty)
\end{align*}
$$

### Question Seven

#### Question

For each of the following relations $R$ on a given set $S$, determine if $R$ is transitive, reflexive, symmetric, antisymmetric (in each case giving a proof if yes, or a counterexample if not). Hence state if the relation is an order, or an equivalence, or neither.

1. $S=\mathbb{R}$ and $aRb$ if $|a|\le|b|$,
2. $S=\mathbb{Z}$ and $mRn$ if $(m,n)\ne 1$.

#### Solution

##### Part One

For $S = \mathbb{R}$ and $aRb$ if $|a| \le |b|$

- $R$ is **transitive**: $|a|\le|b|$ and $|b|\le|c|$ implies $|a|\le|c|$, that is, $aRb$ and $bRc$ implies $aRc$.
- $R$ is **reflexive**: $|a|\le|a|$ for any $a\in S$, that is, $aRa$ for any $a\in S$.
- $R$ is **not symmetric**: $|a|\le|b|$ does not imply $|b|\le|a|$, e.g., $|1|\le|2|$, but $|2|\nleq|1|$.
- $R$ is **not antisymmetric**: whilst $|a|\le|b|$ and $|b|\le|a|$ does imply that $|a|=|b|$, it does not imply $a=b$, e.g., $|-1|\le|1|$ and $|1|\le|-1|$, but $-1\ne1$.

$$
\therefore\boxed{R\text{ is neither an order nor an equivalence.}}
$$

##### Part Two

For $S = \mathbb{Z}$ and $mRn$ if $(m,n) \ne 1$

- $R$ is **not reflexive**: For $m=1$, $(1,1) = 1$ does not satisfy $(m,m) \ne 1$, thus $mRm$ does not hold for all $m \in S$.
- $R$ is **symmetric**: If $(m,n) \ne 1$, then $(n,m) \ne 1$ as well, meaning if $mRn$, then $nRm$.
- $R$ is **not antisymmetric**: $(m,n) \ne 1$ and $(n,m) \ne 1$ does not imply $m = n$, e.g., $(2,4) \ne 1$ and $(4,2) \ne 1$, but $2 \ne 4$.
- $R$ is **not transitive**: If $mRn$ because $(m,n) \ne 1$ and $nRp$ because $(n,p) \ne 1$, it does not ensure $(m,p) \ne 1$. For example, $2R4$ and $4R3$ hold, but $2R3$ does not since $(2,3) = 1$.

$$
\therefore\boxed{R\text{ is neither an order nor an equivalence.}}
$$

### Question Eight

#### Question

Let a relation $\sim$ be defined on $\mathscr{P}(\set{a,b,c})$ by the rule $B\sim C$ if $|B|=|C|$.

1. Show that $\sim$ is an equivalence.
2. Draw the diagram of $\sim$ as a subset of $\mathscr{P}(\set{a,b,c})\times \mathscr{P}(\set{a,b,c})$.
3. List all elements of the equivalence class $\set{a,b}$ with respect to this equivalence $\sim$.


*Note: Recall that $\mathscr{P}(\set{a,b,c})$ is the set of all subsets of $\set{a,b,c}$.*

#### Solution

##### Part One

To prove that $\sim$ is an equivalence relation, we must show that it satisfies three properties: reflexivity, symmetry, and transitivity.

Reflexivity: For any set $B \subseteq {a, b, c}$, it is clear that $|B| = |B|$. Thus, $B \sim B$, satisfying the reflexivity condition.

Symmetry: If $B \sim C$, then $|B| = |C|$. By the definition of equality, $|C| = |B|$, which means $C \sim B$. Hence, the symmetry condition is satisfied.

Transitivity: If $B \sim C$ and $C \sim D$, then $|B| = |C|$ and $|C| = |D|$. By the transitive property of equality, $|B| = |D|$, which implies $B \sim D$. Therefore, the transitivity condition is satisfied.

Since $\sim$ satisfies reflexivity, symmetry, and transitivity, it is an equivalence relation.

##### Part Two

Cartesian product diagram:

The subsets are grouped into levels based on their cardinalities.
Subsets with cardinality 0 (just the empty set) are related.
Subsets with cardinality 1 ($\set{a}$, $\set{b}$, $\set{c}$) are all related to each other but not to subsets of different cardinalities.
Subsets with cardinality 2 ($\set{a,b}$, $\set{a,c}$, $\set{b,c}$) are all related to each other.
The subset with cardinality 3 ($\set{a,b,c}$) is only related to itself.

##### Part Three

The equivalence class of ${a,b}$ with respect to $\sim$ includes all subsets of ${a,b,c}$ that have the same cardinality as ${a,b}$. Since ${a,b}$ has a cardinality of 2, we are looking for all subsets of ${a,b,c}$ that also have a cardinality of 2. These are:

$\set{a,b}$
$\set{a,c}$
$\set{b,c}$

Therefore, the elements of the equivalence class ${{a,b}}$ are ${a,b}$, ${a,c}$, and ${b,c}$, as these sets all share the same size, demonstrating the nature of the equivalence relation based on cardinality.

### Question Nine

#### Question

For each of the following mappings, determine whether it is injective or not, and/or if it's surjective or not (in each case giving a proof if yes, or a counterexample if not):

1. $f:\mathbb{N}\times \mathbb{N}\to \mathbb{Z},\quad f((a,b))=a-b$,
2. $f: \mathbb{R}\to \mathbb{R}\times \mathbb{R},\quad f(x)=(2x,3x)$.

#### Solution

##### Part One

Not injective: $f((2,1))=1=f((3,2))$, but $(2,1)\ne(3,2)$.

Is surjective: For any $z\in \mathbb{Z}$ we can choose $(a,b)$ such that $a - b = z$.

- If $z \geq 0$, we can pick $(a,b) = (z,0)$. 
- If $z < 0$, we can choose $(a,b) = (0,|z|)$, where $|z|$ denotes the absolute value of $z$. 

##### Part Two

Is injective: Given $f(x_1) = (2x_1, 3x_1)$ and $f(x_2) = (2x_2, 3x_2)$, if $f(x_1) = f(x_2)$, then $(2x_1, 3x_1) = (2x_2, 3x_2)$. This implies $2x_1 = 2x_2$ and $3x_1 = 3x_2$. Both equations lead to $x_1 = x_2$, proving that $f$ is **injective**.

Not surjective: There is no single $x$ that satisfies $f(x) = (1, 2)$, since solving $2x = 1$ and $3x = 2$ simultaneously is impossible. Thus, $f$ is **not surjective**.

### Question Ten

#### Question

Let $A=\mathscr{P}(\set{u,v,w})$ be the set of all subsets of $\set{u,v,w}$ and let $f:A\to A$ be a mapping defined by the rule $f(X)=X\cup \set{v}$.

1. Draw the diagram of the Cartesian product $A\times A$ and indicate $f$ as a subset of $A\times A$.
2. Determine the image of $f$ and list all elements of this image.

#### Solution

##### Part One

Since $A = \mathscr{P}(\{u,v,w\})$, the set of all subsets of $\{u,v,w\}$, we can list all elements of $A$. These are the empty set $\emptyset$, singletons $\{u\}$, $\{v\}$, $\{w\}$, pairs $\{u, v\}$, $\{u, w\}$, $\{v, w\}$, and the entire set $\{u, v, w\}$. Thus, $A$ has $2^3 = 8$ elements because the power set of a set with $n$ elements has $2^n$ elements.

The Cartesian product $A \times A$ consists of ordered pairs $(X, Y)$ where $X, Y \in A$. Since there are 8 elements in $A$, there are $8 \times 8 = 64$ ordered pairs in $A \times A$.

The mapping $f: A \to A$ defined by $f(X) = X \cup \{v\}$ means that for each subset $X$ of $A$, we add $v$ to $X$ if it's not already present. So, $f$ as a subset of $A \times A$ consists of pairs $(X, X \cup \{v\})$ for each $X \in A$.

It's not practical to draw a detailed diagram with all 64 elements of $A \times A$ in this format. However, the idea is that for every subset $X$ of $\{u,v,w\}$, you have an arrow (in a conceptual diagram) from $X$ to $X \cup \{v\}$ indicating the function $f$.

##### Part Two

The image of $f$ is the set of all possible outputs of the function $f$. Since $f(X) = X \cup {v}$ ensures that $v$ is in every output, the image will exclude any set that does not contain $v$. Let's list all possible subsets of ${u, v, w}$ that include $v$:

$\set{v}$,
$\set{u, v}$,
$\set{v, w}$,
$\set{u, v, w}$.