# Summary Notes
[[Mid-Term Content (Algebra).pdf]]
*Draft, then draft again, then draft again - all until it fits on a double-sided piece of A4.*
## Base conversion
The number of digits in base $b$ of a non-negative integer $n$ is given by the formula
$$
k=\log_bn+1=\frac{\log n}{\log b}+1\impliedby b^{k-1}\le n\lt b^k
$$
### Conversion from base b to base 10 (integer numbers)
To convert an integer $n$ from base $b$ to base $10$ we write the conversion as
$$
n=(\ldots((d_{k-1}b+d_{k-2})b+d_{k-3})b+\cdots+d_1)b+d_0
$$
For example,
$$
(61405)_7=(((6\cdot7+1)\cdot7+4)\cdot7+0)\cdot7+5=14950
$$
We can also do the conversion via a tabular method - a special case of Ruffini's Rule for polynomials (or Horner scheme).

| (7) | 6   | 1   | 4   | 0    | 5     |
| --- | --- | --- | --- | ---- | ----- |
|     | 0   | 42  | 301 | 2135 | 14945 |
|     | 6   | 43  | 305 | 2135 | 14050 | 

### Conversion from base 10 to base b (integer numbers)
Converting any $n$ from base $10$ to base $b$ is naturally the opposite routine. If $n$ is an integer, its last digit in base $b$, which is $d_0$, can be obtained as the remainder of dividing $n$ by $b$, then $d_1$ is obtained as the remainder of dividing the previous quotient by $b$, etc., until we get the quotient zero. For example,
$$
\begin{matrix}
14950=7\cdot2135+5\\
2135=7\cdot305+0\\
305=7\cdot43+4\\
43=7\cdot6+1\\
6=7\cdot0+6
\end{matrix}
\implies(14950)_{10}=(61405)_{7},\text{ by reading the remainders upwards}
$$
### Conversion from base b to base 10 (real numbers)
If $n$ is instead a real number, with a finite number $h$ of digits after the point, to convert it to decimal one may use the same procedure, continuing beyond the point, ignoring it. Doing this effectively multiplies $n$ by $b^h$, so we then divide the result by $b^h$. This is also represented very clearly in decimal, with the idea of fraction and decimal equivalence.

For example,
$$
(14.22)_5\to n_{10}:n=\frac{(1422)_{5\to10}}{5^2}=\frac{237}{25}=9.48
$$
Where we calculated the base conversion with the following tabular arrangement,

| (5) | 1   | 4   | 2   | 2   |
| --- | --- | --- | --- | --- |
|     | 0   | 5   | 45  | 235 |
|     | 1   | 9   | 47  | 237 | 

This method also works exclusively with integer numbers, those excluding any approximation errors until the final fraction - which could be a recurring decimal with infinitely many digits (such as $(1.22)_3=(5.\dot{2})_{10}$). If the number we're converting instead has infinitely many digits, we can approximate, or if the number is periodic in its base, then it is rational and we can convert it intro a fraction of integers.
### Conversion from base 10 to base b (real numbers)
Similar to the integer base conversions, we can do the process to real numbers by instead of using the tabular arrangement, we do a repetition of remainder calculations, for example,

$$
2.481\to n_3:2.481=2+0.481\implies
\begin{matrix}
0.481\cdot3=0.433+1\\
0.443\cdot3=0.329+1\\
0.329\cdot3=0.987+0\\
0.987\cdot3=0.961+2\\
0.961\cdot3=0.883+2
\end{matrix}
\therefore2.481=(2.11022\cdots)_3
$$
Note that $2_{10}=2_3$.
## Arithmetic and geometric progressions
### Arithmetic progressions
Given a finite sequence of complex numbers $a_1, a_2, \ldots, a_n$, if the difference $d=a_{k+1}-a_k$ between two consecutive terms is constant ($d$ is independent of $k$), then the sequence is arithmetic.

Hence, a sequence is an arithmetic progression precisely when each term is the arithmetic mean of the preceding and the following term.
$$
a_n=a_1+d(n-1)
$$
#### Sum of an arithmetic progression
$$
\sum_{k=1}^n a_k=a_1+a_2+a_3+\cdots+a_n=\frac{(a_1+a_n)\cdot n}{2}
$$
The above result can be shown by noting that any two terms which have the same distance from both ends have the same sum
$$
a_k+a_{n-k+1}=(a_1+d(k-1))+(a_1+d(n-k))=2a_1+d(n-1)=a_1+a_n
$$
and hence,
$$
2(a_1+a_2+\cdots+a_n)=(a_1+a_2+\cdots+a_n)+(a_n+a_{n-1}+\cdots+a_1)=n\cdot(a_1+a_n)
$$
### Geometric progressions
Given the same finite sequence, the results are analogous to the arithmetic progressions, only that sums and differences map to products and quotients.

Hence, a sequence is a geometric progression precisely when each term is the geometric mean of the preceding and the following term.
$$
a_n=a_1\cdot r^{n-1}
$$
#### Sum of a geometric progression
##### Finite sum
