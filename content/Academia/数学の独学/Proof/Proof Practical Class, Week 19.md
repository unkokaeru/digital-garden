### Question One

#### Question

Use mathematical induction to prove that $5^{n}+3$ is divisible by $4$ for all positive integers $n$.

#### Solution

**Trivial Case**
$$
n=0:5^{0}+3=4(1)\implies\text{True for }n=0
$$
**Inductive Step**
If true for $n=0$, then assume true for $n=k$:
$$
n=k:5^{k}+3\text{ is divisble by }4
$$
Hence, by the Axiom of [[Mathematical Induction]], if $n=k+1$ is true using the assumption, then we have proved the statement by induction.

$$
\begin{align*}
n=k+1:5^{k+1}+3&=5(5^{k})+3\\
&= 4(5^{k})+(5^{k}+3)\\
&= 4a+b
\end{align*}
$$

Therefore, if the statement is valid for $n=k$, then it is valid for $n=k+1$ and therefore valid for all positive integers $n$ by the inductive hypothesis.

### Question Two

#### Question

Use mathematical induction to prove that $11^{n}-4^{n}$ is divisible by $7$ for all positive integers $n$.

#### Solution

**Trivial Case**
For the trivial case $n=0$, $11^{n}-4^{n}=11^{0}-4^{0}=7(1)$, hence the statement is true for the trivial case.

**Inductive Step**
Suppose that $11^{k}-4^{k}=7m:m\in \mathbb{Z}$, hence for $n=k+1$
$$
\begin{align*}
11^{k+1}-4^{k+1}&=11(11^{k})-4(4^{k})\\
&= 7(11^{k})+4(11^{k})-4(4^{k})\\
&= 7(11^{k})+4(11^{k}-4^{k})\\
&= 7(11^{k})+4(7m)\text{ by the inductive step}\\
&= 7(11^{k}+4m):11^{k}+4m\in \mathbb{Z}\\
&= 7a:a\in \mathbb{Z}
\end{align*}
$$
Therefore, by the Axiom of Mathematical Induction, the statement is true for all positive integers $n$.

### Question Three

#### Question

Use the method of undetermined coefficients to guess a formula for $1 + 3 + 5 + \cdots + (2n-1)$ as a quadratic expression in $n$, and then use mathematical induction to prove this formula.

#### Solution

Assuming that the formula is of the form $an^{2}+bn+c$, solving for multiple cases to find the coefficients $a,b,c$:

$$
n=1:a+b+c=1
$$
$$
n=2:4a+2b+c=4
$$
$$
n=3:9a+3b+c=9
$$

Hence, solving this system of equations results in the coefficients $a=1,b=0,c=0$.

Proving the formula, $n^{2}$ for all $n\ge1:n\in \mathbb{Z}$ by induction:

**Trivial Step**
For the trivial case $n=1$, $n^{2}=1^{2}=1$, hence the statement is true for the trivial case.

**Inductive Step**
Suppose that $k^{2}=1+3+5+\cdots+(2n-1)$, hence for $n=k+1$
$$
\begin{align*}
(k+1)^{2}&=k^{2}+2k+1\\
&= k^{2}+(2(k+1)-1)
\end{align*}
$$
Therefore, by the Extended Axiom of Mathematical Induction, the statement is true for all integers where $n\ge1$.

*Unsure on notation for this question.*

### Question Four

#### Question

Use mathematical induction to prove the following for any positive integer $n$:

$$
\frac{1}{1\cdot2\cdot3} + \frac{1}{2\cdot3\cdot4} + \cdots + \frac{1}{n(n+1)(n+2)} = \frac{1}{4} - \frac{1}{2(n+1)(n+2)}
$$

#### Solution

...

### Question Five

#### Question

Use mathematical induction to prove that $n!>3^{n}$ for any $n\ge7$.

#### Solution

**Trivial Step**
For the trivial case $n=7$, $n!>3^{n}\implies7!>3^7\iff5040>2187$, hence the statement is true for the trivial step.

**Inductive Step**
...

### Question Six

#### Question

What is wrong in the following "proof" that all men are bald? We use induction on the number of hairs on the head, $n$:

1. If $n=1$, then a man with just one hair is of course bald.
2. Suppose the assertion is true for $n=k$, that is, having $k$ hairs means the man is bald. Now, if he has $k+1$ hairs, then it is just one more, so, surely, does not transform a man from being bald to non-bald.
3. Thus, by the Axiom of Mathematical Induction, a man is bald if he has $n$ hairs, for any $n$.

#### Solution

There is no mathematical definition for being bald stated in the argument, hence there is no mathematical proof.

### Question Seven

#### Question

Prove by induction that for $x\ne1$ we have the following, for any positive integer $n$:

$$1+x+x^{2}+\cdots+x^{n-1} = \frac{1-x^{n}}{1-x}$$

#### Solution

**Trivial Step**
For $n=1$, $\frac{1-x^{n}}{1-x}=1$, hence the statement is valid for the trivial case.

**Inductive Step**
Suppose that $1+x+x^{2}+\cdots+x^{k-1}=\frac{1-x^{k}}{1-x}:x\ne0$, hence for $n=k+1$,

$$
\begin{align*}
1+x+x^{2}+\cdots+x^k&=\frac{1-x^{k+1}}{1-x}\\
&= \frac{1-x(x^{k})}{1-x}
\end{align*}
$$

...

### Question Eight

#### Question

Use mathematical induction to prove the following for all positive integers $n$:

$$\frac{1}{2} + \frac{2}{2^{2}} + \frac{3}{2^{3}} + \cdots + \frac{n}{2^{n}} = 2 - \frac{n+2}{2^{n}}$$

#### Solution

...

### Question Nine

#### Question

Use mathematical induction to prove that $n^{3}<2^{n}$ for any $n\ge10$.

#### Solution

**Trivial Step**
For $n=10$, $10^{3}<2^{10}$, which is valid as $1000<1024$, therefore the statement is true for the trivial case.

**Inductive Step**
Suppose that $k^{3}<2^{k}:k\ge10$, such that $(k+1)^{3}<2^{k+1}$ by the induction hypothesis.

$$
(3k^{2}+3k+1)+k^3<(2)2^{k}
$$

...