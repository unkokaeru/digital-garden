#### Question 1
Solve each of the following congruences:
##### Question 1a
*Using the first method,*
$$
6x\equiv10\quad (\text{mod }19)\iff6x\equiv10+19k:k\in\mathbb{Z}
$$
$$
6x-19k=10
$$
$$
\text{Using the Euclidean Algorihtm,}
$$
$$
19=6\cdot3+1,6=1\cdot6+0\therefore\text{coprime}
$$
$$
\text{Extending the Algorithm,}
$$
$$
(1)19+(-3)6=1\implies(10)19+(-30)6=10
$$
$$
k_0=10,x_0=-30,\text{ from Bezout's Lemma}
$$
$$
\begin{matrix}
x=-30+19h\iff x\equiv-30\text{ mod }19\equiv8\text{ mod }19,\\
k=10+6h\iff k\equiv10\text{ mod }6\equiv4\text{ mod }6\\
\end{matrix}
$$
##### Question 1b
*Using the second method,*
$$
[6x]_{20}=[10]_{20}\iff[6]_{20}[x]_{20}=[10]_{20}\iff[3]_{10}[x]_{10}=[5]_{10}:(6,20)=2
$$
$$
[x]_{10}=[3]_{10}^{-1}[5]_{10}:[3]_{10}[3]_{10}=[9]_{10}=[-1]_{10}\therefore[3]_{10}^{-1}=[-3]_{10}
$$
$$
[x]_{10}=[-3]_{10}[5]_{10}=[-15]_{10}=[5_{10}]\iff x\equiv5\text{mod10}\equiv5+10k
$$
##### Question 1c
$$
6x\equiv10\text{mod21}\iff6x+21k=10:(6,21)=3,\text{GCD does not divide 10}
$$
$$
\therefore\text{no solutions}
$$
#### Question 2
Find a positive integer $x$ such that $44x$ has $92$ as its last two decimal digits. Then, find all integers $0\lt x\lt 100$ such that $44x$ has $92$ as its last two decimal digits.
$$
44x=92+100k_1\cdots
$$
$$
44x=92\text{mod}100
$$
$$
44x+100k=92:(44,100)=d
$$
$$
\text{Euclid's Algorithm: }100=44\cdot2+12,44=12\cdot4-4\therefore d=4
$$
$$
\text{Extended: }4(2(44)-1(100))-1(44)=4=7(44)-4(100)\therefore x_0=7,k_0=-4
$$
$$
(161)(44)+(-92)(100)=92
$$
#### Question 3
For each of the following systems of congruences, decide if there are any solutions, and in the affirmative case find all solutions,
$$
\begin{cases}
x\equiv3\quad(\text{mod }12)\\
x\equiv5\quad(\text{mod }16)
\end{cases}
$$
$$
\begin{cases}
x\equiv3\quad(\text{mod }13)\\
x\equiv5\quad(\text{mod }17)
\end{cases}
$$
$$
\begin{cases}
x\equiv3\quad(\text{mod }14)\\
x\equiv5\quad(\text{mod }18)
\end{cases}
$$
#### Question 4
Write the multiplicative table of $\frac{\mathbb{Z}}{11\mathbb{Z}}$, then use the table to check that...