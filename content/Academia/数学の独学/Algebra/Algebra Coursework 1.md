![[MTH1001_CW.pdf]]

___
___

## Problem 1
*Use Euclid’s algorithm to compute the greatest common divisor $d$ of $442$ and $273$. Use negative remainders whenever convenient.*

Using Euclid's algorithm,
$$(442,273):442=273\cdot2-104$$
$$\implies273=104\cdot3-39$$
$$\implies104=39\cdot3-13$$
$$\implies39=13\cdot3+0$$
$$\therefore(442,273)=13\text{, as 13 was the last remainder.}$$
## Problem 2
*Extend the calculations in the previous exercise (that is, apply the extended Euclidean algorithm) to find integers $x$ and $y$ such that $442x + 273y = d$, where $d = (442, 273)$ is the greatest common divisor found before.*

Solving the equation $442x+273y=13$ results in a pair of solutions $(x_0,y_0)$ such that:
$$104(-1)+39(3)=13\text{, by rearranging the third step in problem 1}$$
$$\implies104(-1)+(273-104(3))(-3)=13\text{, by rearranging the second step in 
problem 1}$$
$$\implies104(8)+273(-3)=13\text{, through simplification}$$
$$\implies(442-273(2))(-8)+273(-3)=13\text{, by rearranging the first step in problem 1}$$
$$\implies442(-8)+273(13)=13\text{, through simplification}$$
$$\therefore(x_0,y_0)=(-8,13)$$
## Problem 3
*Find all integer solutions of $442x + 273y = 52$. Then find the solution such that $|x|$ is smallest.*

Continuing to solve the equation $442x+273y=13$ requires finding such integers $a,b$ that the following is true:
$$442(-8+an)+273(13-bn)=13:n\space\epsilon\space\mathbb{z}$$
This is true if $442an-273bn=0$, or $34a-21b=0$ (simplifying the equation by dividing through by $13n$). $a,b$ are thus each other's coefficient, namely that $a,b=21,34$.

This gives the solution:
$$x=-8+21n,y=13-24n\text{, for any }n\space\epsilon\space\mathbb{z}$$
## Problem 4
*Convert the decimal number $862.4$ to a periodic number in $\text{base } 7$.*

To convert the number $862.4$ into its periodic base 7 counterpart, one may do the following division after separating the integer and its fraction: $862.4=862+\frac{4}{10}$

First, the whole part:
$$862:862=123\cdot7+1$$
$$\implies123=17\cdot7+4$$
$$\implies17=2\cdot7+3$$
$$\implies2=0\cdot7+2$$
$$\therefore(862)_{10}=(2341)_{7}\text{, by reading the remainders from the bottom step up}$$
Then the fraction:
$$0.4:0.4\cdot7=2+0.8$$
$$\implies0.8\cdot7=5+0.6$$
$$\implies0.6\cdot7=4+0.2$$
$$\implies0.2\cdot7=1+0.4$$
$$\implies0.4\cdot7=2+0.8\text{, this is a repetition, so the number is periodic}$$
$$\therefore (0.4)_{10}=(0.\dot{2}54\dot{1})_{7}$$
Thus, the final answer is as follows...
$$
(862.4)_{10}=(2341.\dot{2}54\dot{1})_{7}
$$
