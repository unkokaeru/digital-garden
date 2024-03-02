# The History of Numbers

## 18th Century, by William Fayers

### Introduction

The 18th century was a pivotal point in the development of mathematics, catapulting mathematicians into the Era of Enlightenment, driven by the consequences of the Scientific Revolution. Mathematics was slowly becoming more modern: notation was becoming globally standard, proofs were becoming more formal, and more abstract concepts were becoming more accepted. Eight key mathematicians were driving this innovation in the century. Some were more influential towards the 17th and 19th centuries, but all still made enormous waves in the mathematical community during the 18th century. Together, these figures propelled topics such as calculus, complex numbers, and number theory - as well as others - towards the Enlightenment's age of reason. The 18th century's contributions were not merely incrementing the global knowledge of mathematics; they were foundational, shaping the trajectory of mathematics and its application for centuries to come.

### Calculus

However, such intellectual ferment often leads to multiple academics independently developing similar or identical concepts. Such was the case coming into the 18th century with the calculus controversy. Calculus, an area of mathematics focussing on change and motion, became a central point of debate. It provides two main tools: one to understand the rate at which a quantity changes (differentiation) and another to understand the accumulation of quantities (integration). Hence, the study was crucial in multiple fields, inside and outside the mathematical world - especially within applied work.

During the previous century, Isaac Newton and Gottfried Wilhelm Leibniz independently developed the fundamentals of calculus, resulting in a bitter dispute driven by nationalistic biases coming into the century: a significant conflict. Newton introduced what we now call differentiation in his book "Method of Fluxions", posthumously published in 1736 (although completed in 1671). Newton applied the method to problems of motion under the force of gravity, one of his most famous research areas. The theorem laid the foundation for the fundamental theorem of calculus - a cornerstone of mathematics. The theorem linked the concepts of differentiation and integration, formalising the process of finding the area under a curve and finding the rate of change at any point on a curve.

On the other hand, Leibniz developed a notation of differentiation and integration - both of which remain common in the modern era of mathematics. His notation for the derivative ($\frac{dy}{dx}$) and the integral sign ($\int$) beautifully encapsulate the essence of calculus as the study of change and accumulation, respectively.

Whilst Leibniz was from Continental Europe, Newton was British and a prominent member of the Royal Society, the entity that investigated the matter. Unsurprisingly, they concluded with Newton's endorsement, which was widely criticised as biased, as Newton himself had a significant influence on the proceedings of the Society. Whilst eventually the mathematical community recognised the contributions of both mathematicians, the dispute highlights the importance of the development. Newton's work was an instrumental tool for the physical sciences, whilst Leibniz's notation and systematic approach facilitated the broader application of calculus in mathematics.

### Complex Numbers

This idea of notation was significant in the 18th century, as with the rapid expansion of mathematics came a confusing environment for new mathematicians. If mathematical notation were inconsistent, then mathematicians would be unable to understand one another or build upon another's concepts. Hence, when Abraham de Moivre conceived his formula relating properties of complex numbers in geometric terms, it was relatively untouched by future mathematicians. That is, until Leonhard Euler introduced a notation for these so-called complex numbers, denoting the square root of negative one as $i$ in 1777. The notation originated in scepticism, with those like René Descartes referring to them as "imaginary numbers". However, some mathematicians still worked with them, albeit without a formal understanding - such as Gerolamo Cardano and the previously mentioned de Moivre.

De Moivre's theorem states that, for any number $x\in\mathbb{R}$ and integer $n$, $(\cos x + i\sin x)^n = \cos(nx) + i\sin(nx)$. This beautifully and concisely illustrates the power of complex numbers in combination with trigonometry and is quite simple to prove with mathematical induction:

$$
\begin{align*}
1^{\circ\quad}&\text{For }n=1,(\cos x+i\sin x)^{1}\text{ is indeed }\cos(1x)+i\sin(1x).\\
2^{\circ}\quad&\text{Suppose now that the assertion is true for }n=k:\\
& (\cos x + i\sin x)^k = \cos(kx) + i\sin(kx)
\end{align*}
$$

$$
\text{Now, we prove for }n=k+1
$$

$$
\begin{align*}
(\cos x + i\sin x)^{k+1} &= (\cos x+i\sin x)(\cos x+i\sin x)^{k}\\
&= (\cos x+i\sin x)(\cos kx+i\sin kx)\\
& \text{by the induction hypothesis}\\
&= (\cos x\cos kx)-(\sin x\sin kx)+i(\cos x\sin kx+\sin x\cos kx)\\
&= \cos((k+1)x)+i\sin((k+1)x)\\
& \text{by the trigonometric addition identities}
\end{align*}
$$

$$
\text{We derived the assertion for }n=k+1.
$$

$$
\text{From }1^{\circ}\text{ and }2^{\circ}\text{, the assertion holds true for all }n \text{ by the A.M.I.}\square
$$

With the new notation for imaginary numbers, Euler developed his eponymous formula, $e^{ix}=\cos(x)+i\sin(x)$, linking complex numbers to trigonometry and even logarithms. This formula simplifies many complex number computations and has various applications in applied mathematics, from quantum mechanics to electrical engineering, underlining the role of complex numbers in science and engineering. This new simplicity is evident when proving De Moivre's theorem, as the theorem is now a simple remark from Euler's formula:

$$
\begin{align*}
(\cos(x)+i\sin(x))^{n}&=(e^{ix})^{n}\\
&= e^{inx}\\
&= \cos(nx)+i\sin(nx)\square
\end{align*}
$$

This formalisation of the field was pivotal to its acceptance, concluding at the turn of the 19th century with Carl Friedrich Gauss' 1799 doctoral dissertation providing rigorous proof that every non-constant polynomial has at least one root, thus implying the necessity of complex numbers.

### Number Theory

#### Euler

Euler even continued his spree of notation creation with these logarithms, denoting the number $e$, approximately $2.71$, in 1731. Again, whilst mathematicians before him had researched the areas that Euler notated, Euler was the first to formalise these studies. For example, Jacob Bernoulli investigated Euler's number during the previous century when considering the problem of continuous compound interest.

Euler also pioneered substantial parts of number theory, including his work on the infinity of primes, introducing the totient function, $\phi(n)$, defined as the number of positive integers less than $n$ that are coprime to $n$. This function was crucial in Euler's success in generalising Fermat's Little Theorem. His eponymous theorem states that if $n$ is a positive integer and $a$ is an integer coprime to $n$, then $a^{\phi(n)}\equiv1\mod n$. This relationship underpins most modern number theory and cryptography due to its relation between the totient function and modular arithmetic.

Moreover, Euler exemplified his innovative approach to the distribution of prime numbers with his product formula for the Riemann zeta function, $\zeta(s)$. He discovered that $\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}$ for $s > 1$, where the product is over all prime numbers $p$. This formula demonstrated the profound link between the zeta function and prime numbers and laid the groundwork for future research in analytic number theory, including the famous Riemann Hypothesis.

However, these contributions were not simply a matter of revolutionising number theory due to their results; Euler's contributions revolutionised mathematics as a whole: they encapsulated a new, more concrete and logical methodology for mathematical proof.

#### Lagrange

Another contributor to number theory during the 18th century is the prominent Joseph-Louis Lagrange. Similar to Euler, his contributions to mathematics were numerous and diverse. However, number theory was perhaps his most notable. He set a foundation for the systematic study of numbers, similar to Euler, as opposed to the more disorganised past studies: he was the first to apply rigorous analytical methods to the study of numbers, moving away from the more empirical approaches of previous academics, marking a significant shift towards the modern approach to number theory, where mathematics is more abstract and logical deduction is more standard among mathematicians.

One of Lagrange's most celebrated contributions to number theory is his proof of the Four-Square Theorem. The theorem asserts that one can express every positive integer as the sum of four square numbers. For example, $30=1^{2} + 2^{2} + 3^{2} + 4^{2}$. Lagrange's proof, presented in 1770, was completed with an ingenious new methodology, combining algebraic identities with analytical techniques, such as infinite descent (a method of contradiction developed by Fermat in the previous century), to demonstrate the theorem's validity. This blend of topics was unprecedented in mathematics, influencing future generations of mathematicians and seeding the development of algebraic number theory.

### Transcendental Numbers

However, not all developments in the 18th century were quickly apparent. Transcendental numbers, though not explicitly named and studied until the 19th century, subtly underpin the mathematical innovations of the 18th century. These numbers are similar to irrational numbers, yet even more abstract. They're defined negatively, being the set of numbers that aren't roots of any non-zero polynomial equation with rational coefficients. In contrast, algebraic numbers are precisely those that can be roots of such equations. The concept indirectly touched upon the work of Euler and his number $e$ - a number which turned out to be transcendental with the work of Charles Hermite in 1873. This new distinction between algebraic and transcendental numbers highlights a deeper structure within the number system, illustrating the vast unexplored territories that mathematicians of the 18th century were beginning to hint at, even if they didn't have the entire framework to understand it.

### Infinite Series

Amid this period of vigorous intellectual activity, another field of study emerged: the exploration of infinite series and the principles of convergence. This concept originated from Zeno of Elea in Ancient Greece and further developed with the dawn of calculus. With the standardisation of mathematical notation and a move toward more formal proofs and abstract concepts, the 18th century set the stage for mathematics to advance even further. Euler, a mathematical giant of the era, was instrumental in advancing the field, notably solving the Basel problem by demonstrating that the sum of reciprocal squares converges to a sixth of the square of pi, $\sum\limits_{n=1}^{\infty} \frac{1}{n^{2}}= \frac{\pi^{2}}{6}$. This result highlighted the relationship between infinite series and fundamental constants of mathematics, such as pi.

Euler's solution to the Basel problem is a prime example of infinite series' utility and simplistic beauty. By relating a seemingly monstrous sum of reciprocal squares to the simplistic $\frac{\pi^{2}}{6}$, Euler uncovered a deep connection between number theory and geometry. The proof is complicated and interconnected between multiple fields of mathematics, such as the use of complex analysis and trigonometric series, beautifully showcasing the interconnectedness of mathematics.

Whilst this showcased the power of infinite series, it was not as pivotal as the work of Brook Taylor and Colin Maclaurin for the representation of these series. Their eponymous series defined any function as an infinite series - a versatile tool for applied mathematics when seeking approximations.

The Taylor series of a function $f(x)$ about a point $x=a$ is given by:
$$ f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots $$
It represents the function as an infinite sum of its derivatives at a point, providing a powerful method for approximating functions with polynomials.

The Maclaurin series is a special case of the Taylor series, centred at $a=0$:
$$ f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots $$
These series are immensely useful in physics, engineering, and other sciences for approximating functions, offering the ability to solve complicated functions.

For example, one can express the exponential function $e^x$ as a Maclaurin series:
$$ e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots $$
This series approximation is crucial in fields ranging from quantum mechanics to financial mathematics, where exact solutions are unattainable or impractical.

### Conclusion

The exploration and development of mathematical concepts in the 18th century marked a monumental shift towards modern mathematics, laying the groundwork for future generations of mathematicians. From the calculus controversy that underscored the importance of notation and formal proofs to the formalisation and acceptance of complex numbers, the century was rife with innovation and intellectual ferment. The works of Euler, Lagrange, and others in number theory and beyond revolutionised their respective fields and demonstrated the increasing interconnectedness of mathematical disciplines. The introduction and standardisation of notational systems by figures like Leibniz and Euler facilitated a universal understanding and application of mathematical concepts, bridging gaps between mathematicians across Europe and setting a precedent for international collaboration.

The advancements in understanding infinite series, transcendental numbers, and the foundational work in calculus and number theory have profoundly influenced the field of mathematics and the applied sciences, engineering, and technology. These contributions have enabled us to navigate the complexities of the natural world, from quantum mechanics to modern cryptography, showcasing the timeless relevance of 18th-century mathematics.

In summary, the 18th century was not merely a period of incremental progress in mathematics but a transformative era that redefined the landscape of the discipline. Mathematicians in the era, through their rigorous proofs, innovative notations, and foundational theories, propelled mathematics into the Enlightenment, fostering an environment of critical thinking and analytical rigour that continues to define the field today. As we reflect on the history of numbers, it becomes evident that the 18th century's legacy is its enduring impact on how we perceive, utilise, and advance mathematics, a testament to the epoch's ingenuity and foresight.