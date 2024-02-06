[[Proof Practical Class, Week 19]]
[[Proof Tutorial Class, Week 20]]
[[Proof Practical Class, Week 20]]

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