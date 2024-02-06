### Question One

#### Question

Prove by induction that $6^{n}-1$ is divisible by $5$ for any $n\in \mathbb{N}$.

#### Solution

**Base Case**: $6^{1}-1=5=5|5$.
**Inductive Step**: Suppose that $6^{k}-1=5m:m\in \mathbb{N}$. Hence $6^{k+1}-1\iff 6^{k}\cdot6-1\iff 5(6^{k})+6^{k}-1$
$\iff5(6^{k})+5m\iff5(5^{k}+m)$.
Hence, the proposition is true for all $n\in \mathbb{N}$, given that $5^{k}+m\in \mathbb{N}$, by the Axiom of Mathematical Induction.

### Question Two

#### Question

Suppose that $a$ is a real number such that $a + \frac{1}{a}$ is an integer. Use Cumulative Induction (**Strong Induction**) to prove that then $a^{n} + \frac{1}{a^{n}}$ is also an integer for every $n=1,2,3,\ldots$.

#### Solution

...

### Question Three

#### Question

**Note that this question is more difficult**.

Use induction on $n$ to prove that any 'map' formed by intersections of $n$ straight lines can be coloured in two colours in such a way that no two countries of the same colour have a common boundary segment. (Each country is coloured in one colour; corner points between two countries of the same colour are allowed.)

#### Solution

...