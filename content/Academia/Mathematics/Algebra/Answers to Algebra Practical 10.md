#### 10.1
Compute the right-most decimal digit of $7^{1234567}$.
$$
\begin{matrix}
([7]_{10})^1=[7]_{10}\\
([7]_{10})^2=[-1]_{10}\\
([7]_{10})^3=[-7]_{10}=[3]_{10}\\
([7]_{10})^4=[1]_{10}\\
\cdots\\
\end{matrix}
$$
$$
\text{Period of 4}
$$
$$
\implies 1234567 = 308641\cdot4+3:1234567\equiv3\mod10
$$
$$
\implies[7]^{1234567}=[7]^{308461\cdot4+3}=([7]^3)^{308461}=([7]_{10})^3=[3].
$$
$$
\therefore\text{The right-most decimal digit is }3
$$
#### 10.2
Compute $[5]^{-12}$ working in $\mathbb{Z}=17\mathbb{Z}$.
$$
([5]^{-1})^{12}=[7]^{12}=[7]^{2\cdot2\cdot3}=[15]^{2\cdot3}=[4]^3=[13]
$$
$$
\therefore[5]^{-12}=[13]
$$
#### 10.3
##### 10.3a
$$
a=987654321123456789
$$
$$
:a=\cdots+7\cdot10^2+8\cdot10+9=\cdots+7\cdot(9+1)^2+8\cdot(9+1)+9
$$
$$
\implies a\mod9=\cdots+7+8+9=90=9\cdot10
$$
$$
\text{if }a\mod9\text{ is divisible by 9, then so is }a\therefore 9|a\space\square
$$
##### 10.3b
$$
a=987654321123456789
$$
$$
:a=\cdots+7\cdot10^2+8\cdot10+9=\cdots+7\cdot(11-1)^2+8\cdot(11-1)+9
$$
$$
\implies a\mod11=\cdots+7-8+9=0=11\cdot0
$$
$$
\text{if }a\mod11\text{ is divisible by 11, then so is }a\therefore 11|a\space\square
$$
##### 10.3c
$$
\text{let }n,k\in\mathbb{Z}:n=n_1\cdot10^{k}+n_2\cdot10^{k-1}+n_3\cdot10^{k-2}+\cdots+n_3\cdot10^2+n_2\cdot10+n_1,
$$
$$
\text{where }k\text{ is the number of digits in }n.
$$
$$
n=n_1\cdot(11-1)^{k}+n_2\cdot(11-1)^{k-1}+n_3\cdot(11-1)^{k-2}+\cdots+n_3\cdot(11-1)^2+n_2\cdot(11-1)+n_1
$$
$$
\text{If }k\text{ is even,}
$$
$$
n\mod11=-n_1+n_2-n_3+\cdots+n_3-n_2+n_1=0\therefore 11|n_\text{even}
$$
$$
\text{If }k\text{ is odd,}
$$
$$
n\mod11=n_1-n_2+n_3-\cdots-n_3+n_2-n_1=0\therefore 11|n_\text{odd}
$$
$$
\therefore\text{if }11|n_\text{even}\text{ and }11|n_\text{odd}\implies11|n\text{ for all palindromic }n\space\square
$$
**This is flawed apparently, check later: depends on definition?**
#### 10.4
##### 10.4a
$$
x^2=[-1]\text{ in }\mathbb{F}_3
$$

| x   | [0] | [1] | [-1] |
| --- | --- | --- | ---- |
| x^2 | [0] | [1] | [1]  |

$$
\therefore\text{no solutions for the equation in }\mathbb{F}_3
$$

##### 10.4b
...