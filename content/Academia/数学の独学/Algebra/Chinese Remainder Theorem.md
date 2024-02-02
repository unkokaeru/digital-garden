# Chinese Remainder Theorem

## Overview

The Chinese Remainder Theorem (CRT) states that if one has several linear congruences, each with a different modulus, and if these moduli are pairwise coprime, then there exists a solution common to all the congruences. Moreover, this solution is unique modulo the product of the moduli.

## Historical Context

The theorem was first recorded by Sunzi in his book *Sunzi Suanjing* in the 3rd century AD. However, it was not until the 13th century that Qin Jiushao in his book *Shushu Jiuzhang* provided a complete solution to the problem.

## Mathematical Formulation

Suppose we have a system of congruences:
$$x \equiv a_1 \pmod{m_1}$$
$$x \equiv a_2 \pmod{m_2}$$
$$\vdots$$
$$x \equiv a_n \pmod{m_n}$$

Where $m_1, m_2, \ldots, m_n$ are pairwise coprime. Then, there exists a unique solution $x$ modulo $M = m_1 \cdot m_2 \cdot \ldots \cdot m_n$ for this system.

### Solution Method

1. Compute $M = m_1 \cdot m_2 \cdot \ldots \cdot m_n$.
2. For each $i$, compute $M_i = \frac{M}{m_i}$.
3. Find $y_i$ such that $M_i y_i \equiv 1 \pmod{m_i}$ (using, for example, the Extended Euclidean Algorithm).
4. The solution is given by $x = \sum_{i=1}^{n} a_i M_i y_i \pmod{M}$.

## Example

Consider the system:
$$x \equiv 2 \pmod{3}$$
$$x \equiv 3 \pmod{5}$$

1. $M = 3 \cdot 5 = 15$
2. $M_1 = 15/3 = 5, M_2 = 15/5 = 3$
3. $5y_1 \equiv 1 \pmod{3} \implies y_1 = 2$, $3y_2 \equiv 1 \pmod{5} \implies y_2 = 2$
4. $x = 2 \cdot 5 \cdot 2 + 3 \cdot 3 \cdot 2 = 10 + 18 = 28 \equiv 13 \pmod{15}$

Therefore, $x = 13$ is a solution.

## Test Questions

1. STARTI [Basic] Question: Solve the system x ≡ 1 mod 4 and x ≡ 2 mod 5. Back: x ≡ 6 mod 20. ENDI
2. STARTI [Basic] Question: What is the smallest positive solution for the system x ≡ 3 mod 7 and x ≡ 4 mod 9? Back: x ≡ 31 mod 63. ENDI
3. STARTI [Basic] Question: If a system of congruences has moduli that are not pairwise coprime, is it still solvable? Back: It depends on the specific congruences; if they are consistent, a solution might exist, but it's not guaranteed by the CRT. ENDI