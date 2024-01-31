---
title: Integers
tags:
  - MTH1001
  - Algebra
  - Math
  - Integers
  - Divisibility
---

*Set of all whole numbers (incl. 0, negative): $\mathbb{z}=\{0,\pm1, \pm2, \pm3, ...\}$*
## Divisibility on $\mathbb{z}$
$a,b\space\epsilon\space\mathbb{z}$ : $b$ divides $a$ if there is $c\space\epsilon\space\mathbb{z}$ such that $a=b\times c$. This is written as $b | a$, e.g. $3|6 \because 3\times2=6$ . In the same way, we can say something does not divide by crossing out the $|$.

$b|a\iff \frac{a}{b}\space\epsilon\space\mathbb{z}$ : b divides a if and only if a divided by b exists in the set of integers (is an integer).
For example, if $0|a : a \ne 0$, there are no solutions. But, if $a|0$ then there exists a solution, $c=0 \because 0=a\times c \implies 0=a\times0$.

For $a\space\epsilon\space\mathbb{z}$ we define $D(a)=\{x\space\epsilon\space\mathbb{z}:x|a\}$, the set of divisors of $a$. For example, $D(6)=\{\pm1, \pm2, \pm3, \pm6\}$. This is the same set as $-a$, e.g. $D(6)=\{\pm1, \pm2, \pm3, \pm6\} = D(-6)$. So we may propose a statement that $D(a)=D(-a)$ for any $a\space\epsilon\space\mathbb{z}$.

Another set may be $D(0) : D(0) = \mathbb{z}$, a rather unique set. This is because $0|0$ is defined as true since there always exists a solution for $0=0\times c$.

**Example**
$D(24)=\{\pm1,\pm2,\pm3,\pm4,\pm6,\pm8,\pm12,\pm24\} \because 24 = 2^3 \times 3$; finding a [[Divisibility]] set using [[Prime factorisation]].