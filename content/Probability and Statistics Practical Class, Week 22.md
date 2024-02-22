### Question One

#### Question

Let $Z$ be the "number around the base when a four sided die is rolled".

1. Write down a sample space for the experiment.
2. Define the values of $Z$ and the events they correspond to.
3. Write down the probability mass function of $Z$.

#### Solution

1. The sample space of the experiment is $\mathbb{S}=\set{1,2,3,4}$.

2. The values of $Z$ and their corresponding events are...
- If the die shows 1 at the base, then $Z = 1$.
- If the die shows 2 at the base, then $Z = 2$.
- If the die shows 3 at the base, then $Z = 3$.
- If the die shows 4 at the base, then $Z = 4$.

3. Since each side of the die is equally likely to appear, thus the probability mass function would be defined as...

$$
P(Z)=\begin{cases}
\frac{1}{4}&Z=1,2,3,4 \\
0&Z\ne1,2,3,4
\end{cases}
$$

### Question Two

#### Question

Fully define random variables corresponding to the experiments...

1. "The number of heads shown when two coins are thrown."
2. "The number of successes out of four trials."
3. "An urn contains three white and two blue balls. Two balls are selected without replacement."

#### Solution

1. The sample space would be $\mathbb{S}=\set{0,1,2}$, where either $Z=0$ and no heads are shown on either coin, $Z=1$ and one head is shown on either coin, or $Z=2$ and heads is shown on both coins. Thus, its probability mass function, assuming the two coins are fair, would be...

$$
P(Z)=\begin{cases}
0.25 & Z=0 \\
0.5 & Z=1 \\
0.25 & Z=2
\end{cases}
$$

*Note: define more accurately, e.g. the sample space for 2.1 would be {H,H} etc. where X would then take 0, 1, 2 depending on the subset results. Also note that the probability functions are defined separately in the given solutions - perhaps research whether or not that is necessary.*

2. The sample space would be...

$$
\mathbb{S} = \set{\set{S, S, S, S}, \set{S, S, S, F}, \set{S, S, F, S}, \set{S, S, F, F}, \set{S, F, S, S}, \set{S, F, S, F}, \set{S, F, F, S}, \set{S, F, F, F}, \set{F, S, S, S}, \set{F, S, S, F}, \set{F, S, F, S}, \set{F, S, F, F}, \set{F, F, S, S}, \set{F, F, S, F}, \set{F, F, F, S}, \set{F, F, F, F}}
$$
where the result is either a success $S$ or a failure $F$. Hence,

$$
Z(z)=\begin{cases}
0 & \text{if 0 successes in event} \\
1 & \text{if 1 successes in event} \\
2 & \text{if 2 successes in event} \\
3 & \text{if 3 successes in event} \\
4 & \text{if 4 successes in event}
\end{cases}
$$

Let the probability of success be $p$ and failure $p=1-q$,

$$
p_{Z}(z)=\begin{cases}
\binom{4}{0}q^{4} & \text{if }Z=0 \\
\binom{4}{1}q^{3} & \text{if }Z=1 \\
\binom{4}{2}p^{2}q^{2} & \text{if }Z=2 \\
\binom{4}{3}p^{3}q & \text{if }Z=3 \\
\binom{4}{4}p^{4} & \text{if }Z=4
\end{cases}
\iff
p_{Z}(z)=\begin{cases}
q^{4} & \text{if }Z=0 \\
4q^{3} & \text{if }Z=1 \\
6p^{2}q^{2} & \text{if }Z=2 \\
4p^{3}q & \text{if }Z=3 \\
p^{4} & \text{if }Z=4
\end{cases}
$$

3. The sample space would be...

$$
\mathbb{S} = \set{\set{W_1, W_2}, \set{W_1, W_3}, \set{W_1, B_1}, \set{W_1, B_2}, \set{W_1, B_3}, \set{W_2, W_3}, \set{W_2, B_1}, \set{W_2, B_2}, \set{W_2, B_3}, \set{W_3, B_1}, \set{W_3, B_2}, \set{W_3, B_3}, \set{B_1, B_2}, \set{B_1, B_3}, \set{B_2, B_3}}
$$

where a there are three white balls, $W_{1},W_{2},W_{3}$, and two blue balls, $B_{1},B_{2}$. Hence,

$$
P(Z)=\begin{cases}
\frac{3}{15} & W=2,B=0 \\
\frac{9}{15} & W=1,B=1 \\
\frac{3}{15} & W=0,B=2
\end{cases}
$$

*Note: in future, define a number two a alphanumerical counterpart, then define the probability mass function. It is also not necessary to define each ball uniquely.*

### Question Three

#### Question

The cumulative distribution functions (CDF) for the variables in questions one and two is given by the expression $F(a)=\sum\limits_{\text{all }x\le a}p_{x}(x)$. What do the plots of the CDFs look like?

#### Solution

Essentially, they'll look like staircases with a vertical jump at each discrete probability.

### Question Four

#### Question

Let $X$ be the discrete random variable, representing "the number of tails shown when two coins are thrown".

Define two more random variables:
- $X_{1} = \text{the number of tails shown on the first coin,}$
- $X_{2} = \text{the number of tails shown on the second coin.}$

Show that $X$, $X_{1}$ and $X_{2}$ are random variables.

#### Solution

Simple definitions, then prove that their probabilities add to $1$.

___
Etc.

[[More Questions.pdf]]

### Question Five

#### Question

...

#### Solution

...

### Question Six

#### Question

...

#### Solution

...