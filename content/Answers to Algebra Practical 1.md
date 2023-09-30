![[Practical_1.pdf]]
### Question 1
(a) $300 = 2\times150=2^2\times75=2^2\times3\times5^2$
(b) ![[D(300) Hasse Diagram.excalidraw]](c) 18
### Question 2
(a) $75600 = 2^4\times5^2\times3^3\times7$
(b) All positive divisors of $75600$ would be in the form of $2^a\times5^b\times3^c\times7^d$, where $0\le a\le4,0\le b\le2, 0\le c\le3,0\le d\le1$. In total that gives $5\times3\times4\times2=120$.
(c) All positive odd divisors of $75600$ would be in the form of $2^a\times5^b\times3^c\times7^d$, where $a=0, 0\le b\le2, 0\le c\le3, 0\le d\le1$.  Thus there are $3\times4\times2=24$ positive odd divisors.
(d) The three largest positive divisors of $n$ would be the three combinations of $a,b,c,d$ that give the largest values - thus the three largest values of $a,b,c,d$ (with preference given to the larger number's index to remain as large as possible): $a=4,b=2,c=3,d=1\implies75600$ and $a=3,b=2,c=3,d=1\implies37800$ and $a=4,b=1,c=3,d=1\implies25200$. Another way to look at is by simply dividing by 1, then 2, then 3, then 4, etc. (if possible).
### Question 3
The greatest common divisor (GCD) of $300$ and $221$ is the same as the GCD between $300\mod221=79$ and $221$. Repeating this, it has the same GCD as $221\mod79=63$ and $79$. Next would be $16$ and $63$, then $15$ and $16$, then $1$ and $15$: so the **GCD is 1**.
### Question 4
The greatest common divisor (GCD) of 299 and 221 would similarly be the same as the GCD between $299\mod221=78$ and $221$. Repeating this gives $65$ and $78$, then $13$ and $65$, which then ends the algorithm with an **answer of 13** (as the next $\text{mod}$ gives a value of $0$).
### Question 5
The greatest common divisor (GCD) of $2\times10^8+11$ and $10^8+3$ calculated by Euclid's algorithm would be first be calculated as follows:
$$
(2\times10^8+11)=(10^8+3)\times(2)+4
$$
Thus the $\text{mod}$ is 4. Continuing,
$$
(10^8+3)=(4)\times(2.5\times10^7)+3
$$
Thus the $\text{mod}$ is 3. Again, the next pair of numbers given would be $4,3\implies \text{coprime}$. So the GCD would be 1.

### Question 6
If $n$ is any positive integer, $10^n+1$ and $2\times10^n+1$ must be coprime if their greatest common divisor is 1. This can be found using Euclid's algorithm below:
$$
(2\times10^n+1)=(10^n+1)\times2+1
$$
$$
\implies(10^n+1)=1\times1+0
$$
Thus, their greatest common divisor is 1 $\implies$ coprime.
### Question 7
Assume $a|b$ and $a|c$ and thus prove that $a|b+c$, $a|b-c$, $a|bc$.
$$
a|b:b=a\times n+0,\space\text{for some integer }n
$$
$$
a|c:c=a\times m+0,\space\text{for some integer }m
$$
Thus, $b=an,c=am$. So, $b+c=an+am=a(n+m)\implies a|b+c$.
Similarly, $b-c=an-am=a(n-m)\implies a|b-c$.
Finally, $bc=a^2nm=a(anm)\implies a|bc \space\blacksquare$.
### Question 8
Assume $a|b$ and $b|c$ and thus prove that $a|c$.
$$
b=an+0,\space\text{for some integer }n
$$
$$
c=bm+0,\space\text{for some integer }m
$$
Thus, $b=an,c=bm$. Rearranging for $a=\frac{b}{n}$. From that we can show the following:
$$
a|c:bm=\frac{b}{n}x,\space\text{for some integer x}
$$
If we take $x$ to be equal to $nm$, then the equation is valid thus $a|c$. $\blacksquare$
### Question 9
$$
\text{If } a, b\space\epsilon\space\mathbb{z},\text{ and }b | a,\text{ then }b \le a.
$$
The above statement is false for $(a,b)=(-4,2)$ as $-4\lt2$.

A true statement would be:
$$
\text{If } a, b\space\epsilon\space\mathbb{z},\text{ and }b | a,\text{ then }b \le |a|.
$$