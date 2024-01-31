## Topics and their Methods

1. **Base Conversion** (3/3 occurrences)
	- Convert a base 10 number around 1000 to base 7 or 9 using repeated division. Verify the validity at the end.
	- Usually question 1.

2. **Bézout's Lemma with Integers** (3/3 occurrences)
	- Solve $as+bt=1$ where $a$ is around 350 and $b$ is around 180 using the Extended Euclidean Algorithm. Check validity at each step.
	- Usually question 2, 3, or 4.

3. **Congruence System** (3/3 occurrences)
	- Solve a system of congruences, often mod 9 and mod 13, by converting into two linear combinations, then equate and solve using the Extended Euclidean Algorithm. Ensure the final answer is in the form of a congruence and check validity at each step.
	- Usually question 3, 4, or 5.

4. **Self-Reciprocal Polynomial** (3/3 occurrences)
	- Solve a polynomial in the form $ax^{4}+bx^{3}+cx^{2}+bx+a$ by multiplying by $x^{-2}$ (after checking $x\ne0$) and manipulating into the form $a(x + \frac{1}{x})^{2}+b(x + \frac{1}{x})+c+2=0$. Then solve as a quadratic, and solve the second quadratic for the final four answers.
	- Usually question 5 or 7.

5. **Rational Root Test** (3/3 occurrences)
	- Quote "The Rational Root Test states that if a polynomial $f(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0$ has a rational root $\frac{p}{q}$, where $p$ and $q$ are integers with no common factors other than 1, then $p$ is a factor of the constant term $a_0$, and $q$ is a factor of the leading coefficient $a_n$." and use it to find a rational root of a cubic (checking each potential value with Ruffini's Rule, then solving the leftover quadratic), then fully factorising into three irreducible factors under the integers.
	- Usually question 6.

6. **Polynomial Root Transformation** (3/3 occurrences)
	- Using the relationships between the roots of a polynomial, usually a cubic ($\alpha+\beta+\gamma=-\frac{b}{a},\alpha\beta+\alpha\gamma+\beta\gamma=\frac{c}{a},\alpha\beta\gamma=-\frac{d}{a}$), which are easily derivable by equating the given equation with its factorised form $(x-\alpha)(x-\beta)(x-\gamma)$, then expanding and equating coefficients, find those expressions. Then, rearrange the required form into a form composing of the former expressions, then substitute and evaluate. Common useful identities include $\alpha^{-1}+\beta^{-1}+\gamma^{-1}=\frac{\alpha\beta+\alpha\gamma+\beta\gamma}{\alpha\beta\gamma}$, $\alpha^{2}+\beta^{2}+\gamma^{2}=(\alpha+\beta+\gamma)^{2}-2(\alpha\beta+\alpha\gamma+\beta\gamma)$, $(\alpha^{2}+\beta^{2})=(\alpha+\beta)^{2}-2(\alpha\beta)$, $(\alpha^{3}+\beta^{3})=(\alpha+\beta)^{3}-3(\alpha\beta)(\alpha+\beta)$, $(\alpha^{4}+\beta^{4})=(\alpha+\beta)^{4}-4(\alpha\beta)(\alpha^{2}+\beta^{2})-6(\alpha\beta)^{2}$.
	- Usually question 7 or 8.

7. **High Powers in a Finite Field** (2/3 occurrences)
	- Compute $5^{n}$ where $15<|n|<7000$ under a finite field (usually $11$ or $13$), where, if $n<0$, first calculate $5^{-1}$ (the inverse of $5$) and simplify to the smallest absolute value under the finite field, then continue like normal: decompose the power into prime factors to simplify calculation, then evaluate each step, simplifying as you go.
	- Usually question 3 or 8.

8. **Bézout's Lemma with Polynomials** (2/3 occurrences)
	- Decompose a fraction $\frac{1}{(x^{n}+ax+b)(x^{2}+1)}:n=2,3$ using the Extended Euclidean Algorithm. Check validity at each step.
	- Usually question 9.

9. **Monic Irreducible Polynomials in a Finite Field** (2/3 occurrences)
	- Find degree two polynomials of the form $x^{2}+ax+b$, where $a^{2}-4b<0$, whilst being aware of congruency in solutions. The finite field is often $\mathbb{F}_5$ or $\mathbb{F}_7$, which translates to the set of either $\{0,1,2,3,4\}$ or $\{0,1,2,3,4,5,6\}$.
	- Usually question 10.

10. **Invertible Residue Classes** (2/3 occurrences)
    - List all classes under $\mathbb{Z}/60\mathbb{Z}$ or $\mathbb{Z}/30\mathbb{Z}$ by finding prime factors of 60 or 30 and identifying numbers in the class that don't share those factors. Note that $[1]$ is always invertible as it is its own inverse. There may also be a pattern to make it quicker to list each class.
    - A class $[a]_{n} \in \mathbb{Z}/n\mathbb{Z}$ is invertible precisely when $(a, n) = 1$.
    - Usually question 2 or 8.

11. **Congruence Equation** (2/3 occurrences)
    - Convert the equation of form $ax\equiv b \quad(\text{mod }c)$ into $ax=b+cn$, where $a,b\in \mathbb{Z}$, and you define $n$ as an integer, then rearrange into a linear combination and solve using the Extended Euclidean Algorithm, ensuring to conclude in the correct form: similar to the Congruence System.
    - Usually 4 or 10.

12. **Symmetric System** (1/3 occurrences)
    - Solve $x^3+y^3=a$ and $x+y=b$ using $x^{3}+y^{3}=(x+y)^{3}-3xy(x+y)$. Ensure validity through substitution at the end.
    - Usually question 2.

13. **Decomposition into Irreducible Factors in a Finite Field** (1/3 occurrences)
    - Use the Rational Root Theorem to solve the polynomial as far as you can, before factorising as far as you can - conclude by proving that you cannot go further than you do, without leaving the field. Check validity through expansion at the end.
    - Usually question 9.

### Topics that haven't been tested yet

- Arithmetic and geometric progressions: $S_{n}=\frac{n}{2}(2a+(n-1)d)$ and $S_{n}=a\frac{1-r^{n}}{1-r}$, respectively.
- Periodic numbers (in decimal notation or any other base): $\text{integer part}.\text{pre-period}|\text{period}=\frac{[\text{integer part}|\text{pre-period}|\text{period}]-[\text{integer part}|\text{pre-period}]}{\text{digits of period -> 9}|\text{digits of pre-period -> 0}}$.
- Expansion of a polynomial in terms of $x-a$: using an extension of Ruffini's Rule until fully decomposed.
- Polynomial interpolation: creating a system of equations based on the given co-ordinates.
- Biquadratic polynomials: solving by substituting $y=x^2$, to abstract into a quadratic in $y$.
- Square roots of complex numbers: solve the equation $\sqrt{z}=a+bi$, where $z$ is the complex number given, by equating real and imaginary parts and solving that system of equations.
- Casting out nines, and divisibility criteria: we can test the divisibility of $[a]=[a_{k-1}10^{k-1}+a_{k-2}10^{k-2}+\cdots+a_{1}10+a_{0}]$ by separating the classes and using the cyclic nature of a class' power to find a pattern in the sum of the digits (e.g. in $n=9$, each coefficient is $1$, and in $n=7$ each coefficient is a cycle of $1,3,2,-1,-3,-2,\ldots$, and $n=37$ is just a cycle of $1,10,-11,\ldots$).
- Cryptography: convert characters to numbers, input those into a function in a finite field, convert those into characters again (often this is with an affine map, $f(x)=ax+b$). Decryption is simply an inverse procedure, and one can "crack the code" with simultaneous equations and/or character frequency analysis.
- Fermat factorisation: used to crack simple RSA cryptosystems, such that $a^{2}\equiv b^{2}\quad(\text{mod }n):a\ne \pm b\quad(\text{mod }n),a\ge\sqrt{n}$, then check if $a^{2}=n\cdot x+b^{2}$. Solutions often come after incrementing $a$ by just a few integers, and then using the difference of two squares to find something like $15943=(128-21)(128+21)=107\cdot149$.