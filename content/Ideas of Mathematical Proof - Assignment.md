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

...

#### Solution

...

### Question Five

#### Question

...

#### Solution

...

### Question Six

#### Question

...

#### Solution

...

### Question Seven

#### Question

...

#### Solution

...

### Question Eight

#### Question

...

#### Solution

...

### Question Nine

#### Question

...

#### Solution

...

### Question Ten

#### Question

...

#### Solution

...