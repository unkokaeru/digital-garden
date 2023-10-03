# Bezout's Lemma

**Bezout's Lemma** is a fundamental theorem in number theory and algebra. It states:

For any integers $a$ and $b$, if $d$ is their greatest common divisor (GCD), then there exist integers $x$ and $y$ such that:

\[ ax + by = d \]

In other words, the GCD of two integers can always be expressed as a linear combination of those integers.

## Proof:

1. Consider the set $S$ of all positive integers of the form $ax + by$, where $x$ and $y$ are integers. Since $a$ and $b$ are not both zero, the set $S$ is non-empty.

2. Let $d$ be the smallest positive integer in $S$. By the division algorithm, for any integer $c$ in $S$, we can write $c = dq + r$ where $0 \leq r < d$.

3. Now, $r = c - dq = (ax + by) - d(ax' + by') = a(x - x'q) + b(y - y'q)$. Since $x - x'q$ and $y - y'q$ are integers, $r$ is also of the form $ax'' + by''$. Thus, $r$ is in $S$.

4. But, $r < d$ and $d$ is the smallest positive integer in $S$. So, the only possibility is $r = 0$. This means every integer in $S$ is a multiple of $d$.

5. Since $a$ and $b$ are in $S$, $d$ divides both $a$ and $b$. Thus, $d$ is a common divisor of $a$ and $b$.

6. If there's any common divisor $c$ of $a$ and $b$, then $c$ divides any integer of the form $ax + by$. In particular, $c$ divides $d$. Thus, $d$ is the greatest common divisor of $a$ and $b$.

7. Therefore, the GCD of $a$ and $b$ can be expressed as a linear combination of $a$ and $b$.

## Applications:

Bezout's Lemma is foundational in many areas of mathematics, especially in number theory. It's used in the proof of the Fundamental Theorem of Arithmetic and in the solution of Diophantine equations. Additionally, it plays a crucial role in the theory of modular arithmetic and the RSA encryption algorithm in cryptography.

---

This note provides a comprehensive overview of Bezout's Lemma, its proof, and its significance in various mathematical applications.