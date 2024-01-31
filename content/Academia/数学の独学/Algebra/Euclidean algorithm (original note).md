[[Bullet-pointed notes on Euclidean Algorithm]]
## **Euclidean Algorithm and Its Extensions**

### **Euclidean Algorithm**

The **Euclidean Algorithm** is a classical method used to determine the greatest common divisor (GCD) of two integers. It operates on the principle that the GCD of two integers also divides their difference.

#### **Procedure**:

1. Given two integers $a$ and $b$ where $a > b$, divide $a$ by $b$.
2. Replace $a$ with $b$ and $b$ with the remainder from the division.
3. Repeat the process until $b$ becomes 0. The non-zero remainder is the GCD.

#### **Example**:

To find the GCD of 252 and 105:

$252 = 105 \times 2 + 42$
$105 = 42 \times 2 + 21$
$42 = 21 \times 2$

The GCD of 252 and 105 is 21.

**Alternative layout:**
![[Pasted image 20231004201650.png]]
https://www.youtube.com/watch?v=_rRu1jg7Kus
### **Variant: Negative Remainders**

Instead of always having a positive remainder, it's possible to use negative remainders, which can sometimes simplify calculations.

#### **Procedure**:

1. Divide integer $a$ by $b$.
2. If the remainder is greater than $\frac{b}{2}$, subtract $b$ from the remainder to get a negative remainder and add 1 to the quotient.

#### **Example**:

For $a = 57$ and $b = 21$:

$57 \div 21 = 2$ with a remainder of 15. Since 15 is less than $\frac{21}{2}$, we keep the positive remainder.
$57 = 21 \times 2 + 15$

### **Extended Euclidean Algorithm**

The **Extended Euclidean Algorithm** is an enhancement of the Euclidean Algorithm. It computes the GCD of two integers and also determines the coefficients of Bézout's identity.

#### **Bézout's Identity**:

For any integers $a$ and $b$, there exist integers $x$ and $y$ such that:

$ax + by = \text{GCD}(a, b)$

#### **Procedure**:

1. Start with two integers, $a$ and $b$, where $a > b$. Initialize two coefficient pairs: $(s, t) = (1, 0)$ and $(s', t') = (0, 1)$.
2. Divide $a$ by $b$, obtaining quotient $q$ and remainder $r$, such that $a = bq + r$.
3. Update coefficients: 
$s'' = s - q \times s'$
$t'' = t - q \times t'$
4. Replace $a$ with $b$, $b$ with $r$, $(s, t)$ with $(s', t')$, and $(s', t')$ with $(s'', t'')$. Repeat until $b$ becomes 0.
![[Extended Euclidean Algorithm Example.excalidraw]]
*Shown in red, working bottom to top from the original Euclidean algorithm, rearranging for the remainder and substituting into the below equation - simplifying each time into a ![[linear combination]].*

---
### **Least Common Multiple (LCM)**

The LCM of two integers $a$ and $b$ is the smallest positive integer divisible by both $a$ and $b$. It can be denoted as $\text{LCM}(a, b)$ or $[a,b]$ and can be computed using the GCD:

$\text{LCM}(a, b) = \frac{|a \times b|}{\text{GCD}(a, b)}$
or equivalently,
$[a,b] = \frac{|a \times b|}{(a, b)}$

### **Proofs of the Four Arithmetical Lemmas**

1. **Lemma**: If $a | b$ and $a | c$, then $a | (b + c)$.

   **Proof**: 
   Given $a | b$, there exists an integer $k$ such that $b = ak$. Similarly, given $a | c$, there exists an integer $l$ such that $c = al$. Summing these two equations, we get:
   $b + c = ak + al = a(k + l)$
   This demonstrates that $a$ divides $b + c$.

2. **Lemma**: If $a | b$, then $a | bc$ for all integers $c$.

   **Proof**: 
   Given $a | b$, there exists an integer $k$ such that $b = ak$. Multiplying both sides by $c$, we obtain:
   $bc = a(kc)$
   This shows that $a$ divides $bc$.

3. **Lemma**: If $a | b$ and $c | d$, then $ac | bd$.

   **Proof**: 
   Given $a | b$, there exists an integer $k$ such that $b = ak$. Similarly, given $c | d$, there exists an integer $l$ such that $d = cl$. Multiplying these two equations, we get:
   $bd = a(kc)l = ac(kl)$
   This demonstrates that $ac$ divides $bd$.

4. **Lemma**: If $a | b$ and $b | a$, then $a = \pm b$.

   **Proof**: 
   Given $a | b$, there exists an integer $k$ such that $b = ak$. Similarly, given $b | a$, there exists an integer $l$ such that $a = bl$. Using the first equation, we can substitute for $b$ in the second equation to get:
   $a = a(kl)$
   This implies $kl = 1$ or $kl = -1$. Thus, $k$ and $l$ are either 1 or -1. This means $a = \pm b$.

---
