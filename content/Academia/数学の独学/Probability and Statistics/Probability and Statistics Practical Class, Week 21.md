### Question One

#### Question

Two fair six sided dice are thrown:
- The first die comes down a $6$, what is the chance the total is $>10$?
- It is known that at least one of the dice shows $>3$. Find the probability that at least one of them is a $6$.

#### Solution

We have two events, $E_{1}$ and $E_{2}$: the first die shows six spots, and the total is greater than ten, respectively. Hence,

$E_{1}=\{(6,1),(6,2),(6,3),(6,4),(6,5),(6,6)\}$,
$E_{2}=\{(6,5),(6,6)\}$.

Hence $P(E_{2}|E_{1})=\frac{P(E_{1}\cap E_{2})}{P(E_{2})}=\frac{2}{6}$.

___
...

### Question Two

#### Question

Three letters are chosen at random from all the letters of the word AEGEAN. Find the probability that...

- The first letter is a consonant,
- Either the second or the third letter is a vowel,
- An 'E' is not included.

*Hint: it may be easier to work with complements - i.e. events that don't include some outcome.*

#### Solution

$P(E\cap F)=P(E|F)P(F)$.

Let $C_{n}$ be the event that the $n$th letter is a consonant, and let $V_{n}$ be the event that the $n$th letter is a vowel. Given that there are six letters total, four of which are vowels and two of with are consonants,

$$P(C_{1})= \frac{2}{6}$$

$$
\begin{align*}
P(V_{2}\cup V_{3})=P(\overline{C_{2}\cap C_{3}})&=1-P(V_{1})\cdot P(C_{2}|V_{1})\cdot P(C_{3}|V_{1}\cap C_{2})\\
&= 1 - \frac{4}{6} \frac{2}{5} \frac{1}{4}\\
&= \frac{14}{15}
\end{align*}
$$

$$
\begin{align*}
P(\overline{E_{1}}\cap \overline{E_{2}}\cap \overline{E_{3}})&=P(\overline{E_{1}})\cdot P( \overline{E_{2}}|\overline{E_{1}})\cdot P( \overline{E_{3}}|\overline{E_{2}}\cup \overline{E_{1}})\\
&= \frac{1}{5}
\end{align*}
$$

### Question Three

#### Question

In a certain collage, 4% of the men and 1% of the women are taller than 6 feet. Furthermore, 60% of the students are women. Now if a student is selected at random and is taller than 6 feet, what is the probability that the student is a woman?

#### Solution

$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

Let the probability of choosing a man over six feet be $P(M_{h})= \frac{1}{25}$, the probability of choosing a woman over six feet be $P(W_{h})= \frac{1}{100}$, the probability of choosing a woman be $P(W_{t})= \frac{3}{5}$, and the probability of choosing a man be $P(M_{t})= \frac{2}{5}$.

The probability of choosing a random student that is over six feet, and that they are a woman, is...

$$
\begin{align*}
P(W_{t}|M_{h}\cap W_{h})&= (P(W_{h})P(W_{t}))/(\ldots)
\end{align*}
$$

Continue with the generalised form of the Bayes' Theorem.

### Question Four

#### Question

Six married couples are standing in a room.

1. If $2$ people are chosen at random, find the probability $p$ that...
	1. They are married,
	2. One is male and one is female.

2. If 4 people are chosen at random, find the probability $p$ that...
	1. 2 married couples are chosen,
	2. No married couple is among the 4,
	3. Exactly one married couple is among the 4.

#### Solution

...

### Question Five

#### Question

In Glasgow, half of the days have some rain. The local weather forecaster is correct $\frac{2}{3}$ of the time, i.e. the probability that she has predicted rain on a rainy day, and the probability that she predicts no rain on a dry day, are both equal to $\frac{2}{3}$.

When rain is forecast, a Glaswegian lady takes her umbrella. When rain is not forecast, she takes it with probability $\frac{1}{3}$.

1. Draw a tree diagram - start labelling it by whether it rains, then what the forecaster will predict, then finally what the Glaswegian lady does.
2. Check you know what types of probability you are labelling on the diagram.
3. Calculate the probability that the lady has no umbrella, given that it rains.
4. Calculate the probability that she brings her umbrella, given that it doesn't rain.

#### Solution

...

### Question Six

#### Question

One bag contains two dice:
- A fair one that give equiprobable outcomes of $1$ to $6$.
- A "rigged" one: throwing it always gets $6$.

A player has rolled on of the dice and, without examining it, rolled it (once) to get a $6$. What is the probability that he used the "rigged" dice?

#### Solution

...

### Question Seven

#### Question

Microchips are made by three companies. 30% are supplied by firm I, 50% by II and 20% by III.

The probabilities of $A=\text{a defect in a chip}$ are $P(A|I)=0.03,P(A|II)=0.04,P(A|III)=0.01$. If an unlabelled box of chips turns up, what are the probabilities that the box came from I, II, or III.

1. If a random test shows a defective chip?
2. If a random test shows a non-defective chip?
3. If the first chip was defective, and a second chip was then also tested and found defective?

#### Solution

...