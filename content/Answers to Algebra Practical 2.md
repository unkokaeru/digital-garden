![[Practical_2.pdf]]

### Question 1
Greatest common divisor of 89 and 55 (using the Euclidean algorithm, positive remainders):
$$
(89,55):89=55\cdot1+34\implies55=34\cdot1+21\implies34=21\cdot1+13\implies21=13\cdot1+8\implies13=8\cdot1+5\implies8=5\cdot1+3\implies5=3\cdot1+2\implies3=2\cdot1+1\implies2=1\cdot2+0
$$
$$
\therefore (89,55)=1\implies\text{coprime}
$$
### Question 2
Greatest common divisor of 89 and 55 (using the Euclidean algorithm, any remainders):
$$
(89,55):89=55\cdot2-21\implies55=21\cdot3-8\implies21=8\cdot3-3\implies8=3\cdot2-1\implies3=3\cdot1+0
$$
$$
\therefore (89,55)=1\implies\text{coprime}
$$
### Question 3
Using the extended Euclidean Algorithm to find integers $s$ and $t$ such that 89$s$ + 55$t$ = 1.
$$
8=3\cdot2-1\implies-1=8-3(2)
$$
$$
\implies-1=8+(21-8(3))(2)=8(-5)+21(2)
$$
$$
\implies-1=(5)(55-21(3))+21(2)=21(-13)+55(5)
$$
$$
\implies-1=(13)(89-55(2))+55(5)=55(-21)+89(13)
$$
$$
\implies1=89(-13)+55(21)
$$
$$
\therefore s=-13,t=21
$$
### Question 4
*unimportant question, return to later*
### Question 5
Find all the integer solutions $x,y$ of $20x+12y=6$.

From the Euclidean algorithm we find...
$$
(20,12):20=12\cdot2-4\implies12=4\cdot3+0\therefore(20,12)=4
$$
There are no integer solutions to the equation $20x+12y=6$, since the greatest common divisor, 4, does not divide 6.
### Question 6
#### Question 6a
Find all the integer solutions $x,y$ of $19x+12y=1$.

From the Euclidean algorithm we find...
$$
(19,12):19=12\cdot2-5\implies12=5\cdot2+2\implies5=2\cdot2+1\implies2=1\cdot2+0
$$
$$
\therefore(19,12)=1\implies\text{coprime}
$$
Thus, using the extended Euclidean algorithm we can deduce $x_0,y_0$:
$$
1=5-2(2)
$$
$$
1=5+(12+5(2))(2)=5(5)-12(2)
$$
$$
1=(-5)(19-12(2))-12(2)=19(-5)+12(8)
$$
$$
\therefore (x_0,y_0)=(-5,8)
$$
Extending this to be more generalised means finding $a,b$ such that
$$
19(-5+an)+12(8-bn)=1
$$
This means finding the lowest common multiple of 19 and 12, so that $19an+12bn=0:n\space\epsilon\space\mathbb{Z}$.
$$
LCM=[19,12]:1\cdot LCM=19\cdot12\therefore[19,12]=228
$$
Thus $(a,b)=(12,19)$.

Therefore, all the integer solutions $x,y$ of $19x+12y=1$ are in the form:
$$
19(-5+12n)+12(8-19n)=1
$$
$$
\therefore x=12n-5,y=8-19n
$$
#### Question 6b
How many of them satisfy $|x|\lt12$ and $|y|\lt19$?

$|12n-5|\lt12:$
 - $12n-5\lt12\implies n\lt\frac{17}{12}$
 - $12n-5\gt-12\implies n\gt-\frac{7}{12}$
Thus, the integers that satisfy the constraints for $x$ are $\{0,1\}$.

$|8-19n|\lt19:$
 - $19n-8\gt-19\implies n\gt-\frac{11}{19}$
 - $19n-8\lt19\implies n\lt\frac{27}{19}$
Thus, the integers that satisfy the constraints for $y$ are $\{0,1\}$.

Therefore, the integers that satisfy both constraints for $x,y$ are $\{0,1\}$: 2 satisfying integers.

*Correction: $|a|<c\iff -c<a<c$.*
### Question 7
Express the fraction $\frac{1}{77}$ as a difference $\frac{a}{7}-\frac{b}{11}$, finding all solutions for positive integers $a,b$.

$$
\frac{1}{77}=\frac{a}{7}-\frac{b}{11}=\frac{11a-7b}{77}\therefore11a-7b=1
$$
This is a linear combination, thus requires the Euclidean algorithm, then the extended Euclidean algorithm, then the LCM to find the general solutions for $a,b$.

-->