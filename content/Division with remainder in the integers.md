*The idea of the following is to extended the simple notion that two numbers can divide with an integer remainder into the full set of integers (including zero and negative numbers*
## Theorem
Given two integers $a,b$ with $b>0$, there exists unique $q,r\space\epsilon\space\mathbb{z} : a=bq+r, 0\le r\lt b$. Note that $q$ represents the quotient and $r$ represents a remainder.
![[Proof of remainder division theorem.excalidraw]]

Extending the theorem into the negative world is simple (proven above), changing the restricting inequality into $0\le r \lt |b|$.

Notation to expresses results of division can be in a multitude of ways, for example $a=14, b=4$ such that $a$ divides $b$:
 - $14=4\times3+2$ : *good for us, shows what we need to know*
 - The quotient is $3$ and the remainder is $2$ : *Good*
 - $q=3,r=2$ : *Okay*
 - $14:4=3\text{r}2$ : *Often in school, but misleads to think that $14|4$*
 - $\frac{14}{4}=3+\frac{2}{4}$ : *Mathematically correct, but using rational numbers opposed to integers*

## Greatest common divisor
Let $a,b > 0$ be integers. An integer $d$ is called the *greatest common divisor* of $a$ and $b$ if:
 - $d$ divides $a,b$ and
 - if $c$ is any integer which divides both $a,b$ then $c\le d$

This definition however does not generalise well to the entire set of $\mathbb{z}$ or to polynomials etc.

For $\mathbb{z}^+$ a simple rule to find the GCD could be as follows:
![[Finding a GCD.excalidraw]]

Expanding this into the entire set of $\mathbb{z}$ can be done by using divisors, by replacing $c\le d$ with $c|d$. This is also easier to figure out graphically with a [Hasse diagram](Prime%20Factorisation).

So we define the greatest common divisor of $a$ and $b$ if:
 - $d$ divides $a,b$ and
 - if $c$ is any integer with divides both $a,b$ then $c|d$.

Now the GCD is **not unique** (although isn't that much of a big deal; the magnitude is still unique): if $d$ is a GCD of $a$ and $b$ then $-d$ is another GCD, but there are no more GCDs. The GCD of $0$ and and integer $a$ now exists, and equals $a$ because $D(0) \cap D(a) = D(a)$. Including when $a = 0$.

## Euclid's Algorithm
Euclid's Algorithm is an efficient method for computing the greatest common divisor of two numbers, $a$ and $b$. The main principle behind the algorithm is that the greatest common divisor of $a$ and $b$ is the same as the greatest common divisor of $b$ and $a \mod b$.

The Euclidean Algorithm starts with a pair of positive integers and forms a new pair that consists of the lesser number and the remainder of the Euclidean division (also called division with remainder) of the greater by the lesser. This process repeats until the pair is $(0, d)$ where $d$ is the greatest common divisor.

The algorithm can be written as follows:

1. If $b = 0$, then the GCD is $a$ and the process ends.
2. Otherwise, compute $a'$ and $b'$ as $a' = b$ and $b' = a \mod b$.
3. Replace $a$ and $b$ with $a'$ and $b'$ respectively and return to step 1.

Implemented in a loop-free manner, the algorithm can be expressed as:

```
function EuclidGCD(a, b)
    while b ≠ 0
       t := b; 
       b := a mod b; 
       a := t; 
    return a;
```

This algorithm is particularly efficient because it rapidly reduces the size of the numbers. This reduction is based on the observation that, if $r$ is the remainder of $a$ divided by $b$, then the common divisors of $a$ and $b$ are precisely the same as the common divisors of $b$ and $r$. Thus we can use the remainder operation to successively reduce the pair of numbers until we reach a pair where the second number is $0$. At this point, the other number will be the greatest common divisor.