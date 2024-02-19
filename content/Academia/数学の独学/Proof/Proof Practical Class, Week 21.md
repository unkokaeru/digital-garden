### Question One

#### Question

Use a diagram to prove the property $A\times(B\cup C)=(A\times B)\cup(A\times C)$.

#### Solution

...

### Question Two

#### Question

Let $A=\{1,2,\ldots,100\}$ be the set of all integers from 1 to 100. Let $R$ be a relation on $\mathscr{P}(A)$ (the set of all subsets of $A$) defined as $BRC$ if $|B|\le|C|$. Determine if $R$ is...
1. ...transitive,
2. ...reflexive,
3. ...symmetric,
4. ...antisymmetric,
and in each case giving a proof if yes, or a counterexample if not. Hence state whether $R$ is an order, or an equivalence, or neither.

#### Solution

$R$ is transitive, as if $|B|\le|C|$ and $|C|\le|D|$ then $|B|\le|D|$.
$R$ is reflexive, as for any $|A|$ then $|A|\le|A|$.
$R$ is not symmetric, as if $|B|\le|C|$, then $|C|\ge|B|$ (not $|C|\le|B|$). For example, $2\le3$ then $3\ge2$.
$R$ is not antisymmetric, as $|B|\le|C|$ and $|C|\le|B|$ then clearly $|B|=|C|$, but this does not imply $B=C$, for example $|\{1\}|\ne|\{2\}|$.

Hence, $R$ is neither an order or an equivalence.

### Question Three

#### Question

On the set $S=\{1,2,3,4,5,6,7,8,9\}$, consider the relation $R$ defined as $aRb$ if $a|b$ (that is, $a$ divides $b$). Draw the diagram $R$ as a subset of $S\times S$.

#### Solution

...

### Question Four

#### Question

Let $\sim$ be a relation on the set $\mathbb{R}\times \mathbb{R}$ defined by $(x,y)\sim(a,b)$ if $y-|x|=b-|a|$.

1. Show that $\sim$ is an equivalence.

2. What is the equivalence class of $(2,-3)$ with respect to this equivalence $\sim$?

#### Solution

$\sim$ is an equivalence if the following are valid on the relation:
- **Reflexivity:** For every $a \in S$, $aRa$.
- **Symmetry:** For every $a, b \in S$, if $aRb$, then $bRa$.
- **Transitivity:** For every $a, b, c \in S$, if $aRb$ and $bRc$, then $aRc$.

$\sim$ is reflexive, as if
$$
(x,y)\sim(x,y)\implies LHS=y-|x|,RHS=y-|X|:LHS=RHS
$$

$\sim$ is symmetric, as if
$$
(x,y)\sim(a,b)\implies y-|x|=b-|a|\iff(a,b)\sim(x,y)\implies y-|x|=b-|a|
$$

$\sim$ is transitive, as if
$$
(x,y)\sim(a,b),(a,b)\sim(c,d)\implies y-|x|=b-|a|,b-|a|=d-|c|
$$
$$
\implies y-|x|=d-|c|\iff (x,y)\sim(c,d)
$$

Hence $\sim$ is an equivalence.

### Question Five

#### Question

Consider the order relation on $\mathbb{N}$ defined by divisibility: $a|b$ (when $b=ak$ for $k\in \mathbb{N}$). What are the infimum and supremum of the set $S=\{8,12,36\}$? Does this set have the greatest element? What about the smallest element?

#### Solution

The infimum and supremum of the set of the set are defined by the greatest lower bound and the smallest upper bound, respectively. Hence, $\text{inf}(S)=4$ as it is the smallest number that exactly divides the set, and $\text{sup}(S)=72$ as it is the smallest number that the set exactly divides.

The greatest element is $36$ as both $8|36$ and $12|36$, whilst it does not have a smallest element as there are no elements which divide exactly into every other element in the set. $8$ does not divide $12$, $12$ does not divide $8$, and $36$ does not divide $8$ or $12$.

### Question Six

#### Question

Consider the lexicographical order $\le_{L}$ on $\mathbb{R}\times \mathbb{R}$, which means that by definition $(a,b)\le_{L}(c,d)$ if either $a<c$ (while $b$ and $d$ can be any), or $a=c$ and $b\le d$.

1. Find the supremum (least upper bound), if it exists, with respect to $\le_{L}$ of the set $D=\{(x,y):x^{2}+y^{2}\le1\}$ (the disc of radius $1$ with centre at the origin, including the unit circle).

2. Find the supremum (least upper bound), if it exists, with respect to $\le_{L}$ of the set $D_{0}=\{(x,y):x^{2}+y^{2}\lt1\}$ (the disc of radius $1$ with centre at the origin, without the boundary unit circle).

#### Solution

In lexicographical order, to find an upper bound of $D$, we look for a pair $(a, b)$ such that for all $(x, y) \in D$, $(x, y) \le_{L} (a, b)$.

Considering $x$ (the first component): The maximum value of $x$ in $D$ is $1$ since $x^2 \le 1$. So, any upper bound must have its first component $a \ge 1$.
Considering $y$ (the second component): When $x = 1$, the only $y$ that satisfies $x^2 + y^2 \le 1$ is $y = 0$.

Therefore, the smallest pair that is an upper bound of $D$ in $\mathbb{R}\times \mathbb{R}$ with respect to $\le_{L}$ is $(1, 0)$. This is because $(1, 0)$ is in $D$ and there is no element in $D$ with $x > 1$. Also, for any $(x, y) \in D$ with $x < 1$, $(x, y)$ is lexicographically less than $(1, 0)$. Thus, $(1, 0)$ is the supremum of $D$ with respect to $\le_{L}$.

___

Considering $x$ (the first component): The values of $x$ in $D_{0}$ can approach $1$ but never reach it, so any upper bound must still have its first component $a \ge 1$.
Considering $y$ (the second component): Since $x$ can approach $1$ but not equal it, and $y$ can approach $0$ but not necessarily equal it from both sides, the supremum in terms of $y$ is still considering $y = 0$.

However, the difference here is subtle. While $(1, 0)$ still serves as an upper bound (since no pair in $D_{0}$ has $x = 1$), it's also the smallest such upper bound under $\le_{L}$. The critical observation is that even though all pairs $(x, y) \in D_{0}$ have $x < 1$, the supremum must consider the boundary approach, which is not included in the set.

Thus, for $D_{0}$, the supremum with respect to $\le_{L}$ does not exist.

### Question Seven

#### Question

On the set $S=\mathbb{N}\times \mathbb{N}$, consider the relation $\sim$ defined as $(m_{1},n_{1})\sim(m_{2},n_{2})$ if $m_{1}\cdot n_{2}=m_{2}\cdot n_{1}$. Show that $\sim$ is an equivalence. Describe the equivalence class of $(1,2)$ with respect to this equivalence $\sim$.

#### Solution

 $\sim$ is an equivalence if the following are valid on the relation:
- **Reflexivity:** For every $a \in S$, $aRa$.
- **Symmetry:** For every $a, b \in S$, if $aRb$, then $bRa$.
- **Transitivity:** For every $a, b, c \in S$, if $aRb$ and $bRc$, then $aRc$.

$\sim$ is reflexive, as if
$$
(m_{1},n_{1})\sim(m_{1},n_{1})\implies m_{1}\cdot n_{1}=m_{1}\cdot n_{1}
$$

$\sim$ is symmetric, as if
$$
(m_{1},n_{1})\sim(m_{2},n_{2})\implies m_{1}\cdot n_{2}=m_{2}\cdot n_{1}\implies(m_{2},n_{2})\sim(m_{1},n_{1})
$$

$\sim$ is transitive, as if
$$
(m_{1},n_{1})\sim(m_2,n_2)\implies m_{1}\cdot n_{2}=m_{2}\cdot n_{1}
$$
$$
(m_{2},n_{2})\sim(m_{3},n_{3})\implies m_{2}\cdot n_{3}=m_{3}\cdot n_{2}
$$
$$
\iff\ldots
$$

___
The equivalence class of $(1,2)$ is $\ldots$.