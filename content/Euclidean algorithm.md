# Euclidean Algorithm and Related Topics

## How to use the Euclidean Algorithm

The **Euclidean Algorithm** is a method to find the greatest common divisor (GCD) of two integers. It's based on the principle that the GCD of two integers also divides their difference.

### Example:

To find the GCD of 252 and 105:

1. $252 = 105 \times 2 + 42$
2. $105 = 42 \times 2 + 21$
3. $42 = 21 \times 2 + 0$

The GCD of 252 and 105 is 21.

## Variant of integer division: Negative Remainders

Instead of always having a positive remainder, we can also have negative remainders. This can sometimes simplify the calculations.

For two integers $a$ and $b$:

1. Divide $a$ by $b$.
2. If the remainder is greater than $\frac{b}{2}$, then subtract $b$ from the remainder to get a negative remainder and add 1 to the quotient.

### Example:

For $a = 57$ and $b = 21$:

1. $57 \div 21 = 2$ with a remainder of 15. Since 15 is less than $\frac{21}{2}$, we keep the positive remainder.
   $57 = 21 \times 2 + 15$

2. For other values, if the remainder was, say, 16, then:
   $a = 21 \times (2 + 1) - 5$
   Here, the remainder is -5.

## Extended Euclidean Algorithm and Bezout's Lemma

The **Extended Euclidean Algorithm** is an extension of the Euclidean Algorithm that not only computes the greatest common divisor (GCD) of two integers, but also finds the coefficients of Bézout's identity, which are integers $x$ and $y$ such that:

$ax + by = \text{GCD}(a, b)$

### How to do it by hand:

1. **Initialization**: Start with two integers, $a$ and $b$, where $a > b$. Initialize two pairs of coefficients: $(s, t) = (1, 0)$ and $(s', t') = (0, 1)$.

2. **Division Step**: Divide $a$ by $b$, getting the quotient $q$ and the remainder $r$, so that $a = bq + r$.

3. **Update Coefficients**: Compute the new coefficients $(s'', t'')$ as:
   $s'' = s - q \times s'$
   $t'' = t - q \times t'$

4. **Iteration**: Replace $a$ with $b$, $b$ with $r$, $(s, t)$ with $(s', t')$, and $(s', t')$ with $(s'', t'')$. Repeat the division and update steps until $b$ becomes 0. The GCD is the last non-zero remainder, and the coefficients of Bézout's identity are the last pair $(s, t)$.

### How and Why it Works:

The Extended Euclidean Algorithm works by keeping track of the coefficients of the linear combinations of $a$ and $b$ that yield the remainders at each step of the Euclidean Algorithm. The key insight is that each remainder can be expressed as a linear combination of $a$ and $b$.

The algorithm ensures that after each iteration, the current remainder $r$ can be expressed as:
$r = a \times s + b \times t$
This property is maintained throughout the algorithm, and when the remainder becomes the GCD, the coefficients $s$ and $t$ are the ones that satisfy Bézout's identity.

### Historical Background:

The Euclidean Algorithm is ancient and was known to mathematicians like Euclid over 2000 years ago. The "extended" version, which computes Bézout's coefficients, is a natural extension of the original algorithm and has been known for many centuries. The importance of these coefficients and the realization that they could be computed as a by-product of the GCD computation likely became clear as mathematicians delved deeper into number theory and linear Diophantine equations.

## Solving the equation $ax + by = c$ in the integers

Using the Extended Euclidean Algorithm, if $d = \text{GCD}(a, b)$ divides $c$, then the equation $ax + by = c$ has a solution in integers. The solutions can be expressed as:

$x = x_0 + \frac{b}{d}t$
$y = y_0 - \frac{a}{d}t$

Where $x_0$ and $y_0$ are particular solutions and $t$ is any integer.

## Four Arithmetical Lemmas

1. If $a | b$ and $a | c$, then $a | (b + c)$.
2. If $a | b$, then $a | bc$ for all integers $c$.
3. If $a | b$ and $c | d$, then $ac | bd$.
4. If $a | b$ and $b | a$, then $a = \pm b$.

## The least common multiple

The least common multiple (LCM) of two integers $a$ and $b$ is the smallest positive integer that is divisible by both $a$ and $b$. It's denoted as $\text{LCM}(a, b)$. Using the GCD, the LCM can be found as:

$\text{LCM}(a, b) = \frac{|a \times b|}{\text{GCD}(a, b)}$

### Historical Background

The Euclidean Algorithm is named after the ancient Greek mathematician Euclid, who first described it in his Elements (circa 300 BC). However, it's likely that the algorithm was known to mathematicians before Euclid's time. The algorithm is fundamental in number theory and has been widely used throughout history.
Certainly! Let's add a proof for why the Euclidean Algorithm works.

---

## Proof of the Euclidean Algorithm

To understand why the Euclidean Algorithm works, we need to understand the properties of the greatest common divisor (GCD).

### Lemma:

Let $a$ and $b$ be integers, not both zero, and let $q$ and $r$ be the quotient and remainder, respectively, when $a$ is divided by $b$. That is, $a = bq + r$ where $0 \leq r < |b|$. Then, $\text{GCD}(a, b) = \text{GCD}(b, r)$.

### Proof:

Let $d = \text{GCD}(a, b)$. Since $d$ divides both $a$ and $b$, it must also divide their linear combination: $a - bq = r$. Thus, $d$ is a common divisor of $b$ and $r$.

Now, let's assume there's a common divisor $c$ of $b$ and $r$. Then, $c$ divides $bq$ and $c$ divides $r$. Therefore, $c$ divides $a = bq + r$. This means $c$ is a common divisor of $a$ and $b$.

From the above, the common divisors of $a$ and $b$ are exactly the same as the common divisors of $b$ and $r$. Hence, $\text{GCD}(a, b) = \text{GCD}(b, r)$.

This lemma justifies the iterative process of the Euclidean Algorithm. Each step reduces the problem to finding the GCD of smaller numbers, and the algorithm terminates when one of the numbers is reduced to zero. At this point, the other number is the GCD of the original pair.

---

This proof provides a foundational understanding of why the Euclidean Algorithm is a valid method for finding the GCD of two numbers.
Certainly! Let's prove each of the four arithmetical lemmas:

---

## Proofs of the Four Arithmetical Lemmas

### Lemma 1: 
If $a | b$ and $a | c$, then $a | (b + c)$.

#### Proof:
If $a | b$, then there exists an integer $k$ such that $b = ak$. Similarly, if $a | c$, then there exists an integer $l$ such that $c = al$. Adding these two equations, we get:
$b + c = ak + al = a(k + l)$
This shows that $a$ divides $b + c$.

### Lemma 2: 
If $a | b$, then $a | bc$ for all integers $c$.

#### Proof:
If $a | b$, then there exists an integer $k$ such that $b = ak$. Multiplying both sides by $c$, we get:
$bc = a(kc)$
This shows that $a$ divides $bc$.

### Lemma 3: 
If $a | b$ and $c | d$, then $ac | bd$.

#### Proof:
If $a | b$, then there exists an integer $k$ such that $b = ak$. Similarly, if $c | d$, then there exists an integer $l$ such that $d = cl$. Multiplying these two equations, we get:
$bd = a(kc)l = ac(kl)$
This shows that $ac$ divides $bd$.

### Lemma 4: 
If $a | b$ and $b | a$, then $a = \pm b$.

#### Proof:
If $a | b$, then there exists an integer $k$ such that $b = ak$. Similarly, if $b | a$, then there exists an integer $l$ such that $a = bl$. Using the first equation, we can substitute for $b$ in the second equation to get:
$a = a(kl)$
This implies $kl = 1$ or $kl = -1$. Thus, $k$ and $l$ are either 1 or -1. This means $a = \pm b$.

---

These proofs provide a foundational understanding of the properties of divisibility and are fundamental in number theory.