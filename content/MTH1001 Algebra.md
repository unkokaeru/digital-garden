---
title: MTH1001 Algebra
tags:
  - "#MTH1001"
  - "#Algebra"
  - "#Math"
---
# Algebra
Module Co-ordinator: TKouloukas@lincoln.ac.uk (Dr Theodoros Kouloukas, Room 3303)
*Base module before moving into more abstract algebra, like group theory etc.*

Read **[[A Concrete Introduction to Higher Algebra]]** (for the syllabus)
[[Algebra Memorisation Points]]
## Course Components
1. Coursework Assignment (15%)
2. In-Class Assignment (25%)
3. Final Exams (60%)
## Outline Syllabus
 - [x] [Division with remainder](Division%20with%20remainder%20in%20the%20integers) in the [[integers]], including the [[Euclidean algorithm]], [[Bézout's Lemma]], [[divisibility]] and [factorisations](Prime%20Factorisation).
 - [x] [[Arithmetic and Geometric Progressions]].
 - [x] [[Writing decimal numbers in a different base, and back]]. [[Periodic numbers]].
 - [x] [[Division with remainder for polynomials]], including the [[Euclidean algorithm]], and [[Bézout's lemma]].
 - [x] [[Remainder, Factor Theorems, Ruffini’s Rule, and Polynomial Algebra]]
 - [x] [[Irreducible polynomials]].
 - [x] [[Polynomial roots and factorisation]] over the complex numbers ([[Fundamental Theorem of Algebra]]), over the reals (conjugate roots), and over the rational numbers (Rational Root Test).
 - [ ] The coefficients of a polynomial as symmetric functions of the roots.
 - [ ] Polynomial equations and systems of equations which enjoy special symmetries: self reciprocal polynomials, symmetric systems.
 - [ ] Solving congruences in the integers, the Chinese remainder theorem, congruences with polynomials.
 - [ ] The integers modulo n and some applications.
## Learning Outcomes
- [x] **LO1** Find roots and factorise polynomials
- [x] **LO2** Perform the Euclidean algorithm on integers and on polynomials
- [x] **LO3** Apply Euclidean algorithm to questions about integers and polynomials
- [ ] **LO4** Solve congruences and systems of congruences.
## Flashcards
*Automatically ported into Anki*
TARGET DECK
University::MTH1001 Algebra

 - STARTI [Basic] What is the MTH1001 module? Back: Algebra. <!--ID: 1696359359405--> ENDI
 - STARTI [Basic] What is a lemma? Back: A small "theorem" used to prove bigger theorems. <!--ID: 1696415920874--> ENDI
- STARTI [Basic] Question: What does the theorem about the division of integers state? Back: Given two integers \(a,b\) with \(b>0\), there exists unique \(q,r \in \mathbb{z}\) such that \(a=bq+r, 0\le r < b\). <!--ID: 1697559203245--> ENDI
- STARTI [Basic] Question: In the theorem of integer division, what do \(q\) and \(r\) represent? Back: \(q\) represents the quotient and \(r\) represents the remainder. <!--ID: 1697559203262--> ENDI
- STARTI [Basic] Question: How is the theorem extended for negative numbers? Back: The restricting inequality changes to \(0\le r < |b|\). <!--ID: 1697559203274--> ENDI
- STARTI [Basic] Question: What is the greatest common divisor (GCD) of two integers \(a\) and \(b\)? Back: An integer \(d\) that divides both \(a\) and \(b\), and if \(c\) is any integer which divides both, then \(c\le d\). <!--ID: 1697559203288--> ENDI
- STARTI [Basic] Question: How is the GCD definition generalized for all integers? Back: Replace \(c\le d\) with \(c|d\). <!--ID: 1697559203301--> ENDI
- STARTI [Basic] Question: Is the GCD unique? Back: No, if \(d\) is a GCD of \(a\) and \(b\) then \(-d\) is another GCD. <!--ID: 1697559203315--> ENDI
- STARTI [Basic] Question: What is the GCD of 0 and any integer \(a\)? Back: It is \(a\). <!--ID: 1697559203330--> ENDI
- STARTI [Basic] Question: What is Euclid's Algorithm used for? Back: It's an efficient method for computing the greatest common divisor of two numbers, \(a\) and \(b\). <!--ID: 1697559203344--> ENDI
- STARTI [Basic] Question: In Euclid's Algorithm, if \(b = 0\), what is the GCD? Back: The GCD is \(a\). <!--ID: 1697559203359--> ENDI
- STARTI [Basic] Question: How does the Euclidean Algorithm reduce the size of numbers? Back: It uses the remainder operation to successively reduce the pair of numbers until one is 0. <!--ID: 1697559203373--> ENDI
- STARTI [Basic] Question: What is the least common multiple (LCM) of two integers \(a\) and \(b\)? Back: An integer \(m\) such that \(a\) and \(b\) divide \(m\), and if \(c\) is a multiple of both, then \(m|c\). <!--ID: 1697559203387--> ENDI
- STARTI [Basic] Question: What is the relationship between the GCD and LCM of two numbers \(a\) and \(b\)? Back: \((a,b) \times [a,b] = a \times b\). <!--ID: 1697559203403--> ENDI
- STARTI [Basic] Question: Define the set of all whole numbers. Back: \(\mathbb{z} = \{0, \pm1, \pm2, \pm3, ...\}\). <!--ID: 1697559203417--> ENDI
- STARTI [Basic] Question: What does \(b|a\) mean? Back: \(b\) divides \(a\). <!--ID: 1697559203431--> ENDI
- STARTI [Basic] Question: When is \(b|a\) true for \(a\) and \(b\)? Back: If there exists \(c \in \mathbb{z}\) such that \(a = b \times c\). <!--ID: 1697559203445--> ENDI
- STARTI [Basic] Question: What is the set of divisors of \(a\) defined as? Back: \(D(a) = \{x \in \mathbb{z} : x|a\}\). <!--ID: 1697559203456--> ENDI
- STARTI [Basic] Question: What is the set of divisors of 6? Back: \(D(6) = \{\pm1, \pm2, \pm3, \pm6\}\). <!--ID: 1697559203468--> ENDI
- STARTI [Basic] Question: What can be said about the set of divisors for a number and its negative counterpart? Back: \(D(a) = D(-a)\) for any \(a \in \mathbb{z}\). <!--ID: 1697559203479--> ENDI
- STARTI [Basic] Question: What is unique about the set of divisors of 0? Back: \(D(0) = \mathbb{z}\). <!--ID: 1697559203491--> ENDI
- STARTI [Basic] Question: What is the result of dividing 14 by 4 using notation \(a:4\)? Back: \(14:4 = 3r2\). <!--ID: 1697559203502--> ENDI
- STARTI [Basic] Question: How can you express \(14\) divided by \(4\) in fractional notation? Back: \(\frac{14}{4} = 3 + \frac{2}{4}\). <!--ID: 1697559203513--> ENDI
- STARTI [Basic] Question: Describe the principle behind Euclid's Lemma. Back: If \(p\) is prime and divides \(a \times b\), then \(p\) divides \(a\) or \(p\) divides \(b\). <!--ID: 1697559203525--> ENDI
- STARTI [Basic] Question: Is the product of two integers always an integer? Back: Yes, the product of two integers is always an integer. <!--ID: 1697559203536--> ENDI
- STARTI [Basic] Question: Define the term "prime number." Back: A number greater than 1 that has no positive divisors other than 1 and itself. <!--ID: 1697559203548--> ENDI
- STARTI [Basic] Question: What is the Fundamental Theorem of Arithmetic? Back: Every integer greater than 1 can be uniquely expressed as a product of primes, up to the order of the factors. <!--ID: 1697559203561--> ENDI
- STARTI [Basic] Question: Give an example of expressing an integer as a product of primes. Back: \(12 = 2 \times 2 \times 3\). <!--ID: 1697559203576--> ENDI
- STARTI [Basic] Question: What is the definition of a composite number? Back: An integer greater than one that is not prime. <!--ID: 1697559203591--> ENDI
- STARTI [Basic] Question: Name a property of prime numbers. Back: Except for 2, all prime numbers are odd. <!--ID: 1697559203605--> ENDI
- STARTI [Basic] Question: What is the GCD of 21 and 14? Back: \(GCD(21, 14) = 7\). <!--ID: 1697559203617--> ENDI
- STARTI [Basic] Question: Using Euclid's Algorithm, what is the GCD of 54 and 24? Back: \(GCD(54, 24) = 6\). <!--ID: 1697559203630--> ENDI
- STARTI [Basic] Question: What is an arithmetic progression (AP)? Back: An arithmetic progression (AP) is a sequence of numbers in which the difference between consecutive terms is constant. This difference is called the **common difference** and is usually denoted by $d$. <!--ID: 1697559938500--> ENDI
- STARTI [Basic] Question: How is the \( n^{th} \) term of an AP defined? Back: The \( n^{th} \) term \( a_n \) of an AP is given by: \( a_n = a_1 + d(n - 1) \) where \( a_1 \) is the first term, \( d \) is the common difference, and \( n \) is the term number. <!--ID: 1697559938516--> ENDI
- STARTI [Basic] Question: How do you calculate the sum of the first \( n \) terms of an AP? Back: The sum of the first \( n \) terms of an AP is given by: \( S_n = \frac{n}{2} [2a_1 + (n-1)d] \) or \( S_n = \frac{n}{2} (a_1 + a_n) \). <!--ID: 1697559938528--> ENDI
- STARTI [Basic] Question: When is a sequence considered an arithmetic progression? Back: A sequence is an arithmetic progression precisely when each term is the average, or arithmetic mean, of the preceding and the following term. <!--ID: 1697559938539--> ENDI
- STARTI [Basic] Question: How is the arithmetic mean calculated? Back: The arithmetic mean, often called the "average," is the sum of a set of numbers divided by the count of those numbers: \( AM = \frac{a_1 + a_2 + ... + a_n}{n} \). <!--ID: 1697559938551--> ENDI
- STARTI [Basic] Question: What is a geometric progression (GP)? Back: A geometric progression (GP) is a sequence of numbers where each term after the first is found by multiplying the previous term by a fixed, non-zero number called the **common ratio**. This ratio is usually denoted by \( r \). <!--ID: 1697559938562--> ENDI
- STARTI [Basic] Question: How is the \( n^{th} \) term of a GP defined? Back: The \( n^{th} \) term \( a_n \) of a GP is given by: \( a_n = a_1 \times r^{(n-1)} \) where \( a_1 \) is the first term, \( r \) is the common ratio, and \( n \) is the term number. <!--ID: 1697559938574--> ENDI
- STARTI [Basic] Question: How do you calculate the sum of the first \( n \) terms of a GP for \( r \neq 1 \)? Back: The sum of the first \( n \) terms of a GP is given by: \( S_n = \frac{a_1(1 - r^n)}{1 - r} \). <!--ID: 1697559938586--> ENDI
- STARTI [Basic] Question: When is a sequence considered a geometric progression? Back: A sequence is a geometric progression precisely when each term is the geometric mean of the preceding and the following term. <!--ID: 1697559938596--> ENDI
- STARTI [Basic] Question: How is the geometric mean calculated for a set of positive numbers? Back: The geometric mean is the nth root of the product of n numbers. For a set of positive numbers \( a_1, a_2, ..., a_n \), the geometric mean \( GM \) is given by: \( GM = \sqrt[n]{a_1 \times a_2 \times ... \times a_n} \). <!--ID: 1697559938607--> ENDI
 - STARTI [Basic] Question: How is the decimal notation of a positive integer, such as 237, represented? Back: $(237)_{10}=2\cdot10^2+3\cdot10^1+7\cdot10^0$. This means the number 237 in base 10 is constructed using powers of 10 and their respective coefficients. <!--ID: 1697559938618--> ENDI
- STARTI [Basic] Question: How can the notation of integers be extended to represent positive real numbers? Back: The notation can be extended by writing further digits (possibly an infinite amount) after a point, e.g. $(123.456)_{10}=1\cdot10^{2}+2\cdot10^{1}+3\cdot10^{0}+4\cdot10^{-1}+5\cdot10^{-2}+6\cdot10^{-3}$. <!--ID: 1697559938630--> ENDI

- STARTI [Basic] Question: How can you denote a number in base \( b \) using its digits? Back: Let a number \( n \) be denoted by its digits \( (n_1n_2n_3n_4.n_5)_b \) in base \( b \). Then, \( n=n_1\cdot b^3+n_2\cdot b^2+n_3\cdot b^1+n_4\cdot b^0+n_5\cdot b^{-1} \). <!--ID: 1697559938641--> ENDI

- STARTI [Basic] Question: How can you convert integers from any base into a decimal? Back: It can be done either by definition, as demonstrated before, or with an arrangement derived by factorising out the base. For example, converting \( (1422)_5 \) to base 10: \( ((1\cdot5+4)\cdot5+2)\cdot5+2 = (9\cdot5+2)\cdot5+2 = 47\cdot5+2 = 237 \). <!--ID: 1697559938652--> ENDI

- STARTI [Basic] Question: What is a method to convert an integer from base \( b \) to base 10? Back: One can use Horner's Method, a tabular arrangement based on Ruffini's Rule. <!--ID: 1697559938663--> ENDI
- STARTI [Basic] Question: How can you reverse the procedure to convert from decimal to any base? Back: Continuously divide by the base and record the remainder. For instance, converting 14950 to base 7 involves a series of divisions and using the remainders. The result is \( (14950)_{10}=(61405)_7 \). <!--ID: 1697559938675--> ENDI

- STARTI [Basic] Question: What is a similarity between the conversion method and another algorithm? Back: The conversion method looks similar to the Euclidean algorithm in terms of recording remainders, but it's different in the numbers carried forward in each division. <!--ID: 1697559938686--> ENDI
- STARTI [Basic] Question: How can you extend the base conversion method to real numbers? Back: First, remove numbers after the point by multiplying/dividing by \( b^n \) (where \( b \) is the base and \( n \) is the number of digits after the point). After conversion, divide/multiply back by the same number. For infinitely many digits after the point, use an approximation. <!--ID: 1697559938697--> ENDI
- STARTI [Basic] Question: How is an infinitely repeating number denoted? Back: An infinitely repeating number can be represented as $(1.2\dot{3}4\dot{5})$ or $(1.2\bar{3}4\bar{5})$, which means the number is $1.2345345\ldots$. <!--ID: 1697559938709--> ENDI
- STARTI [Basic] Question: Can some numbers in specific bases be written in two ways? Give an example. Back: Yes, for instance, $(1.2\dot{6})_7$ can also be written as $(1.3)_7$, and $(0.\dot{9})_{10}$ is the same as $(1.0)_{10}$. <!--ID: 1697559938720--> ENDI
- STARTI [Basic] Question: What are the steps to convert a repeating decimal into a fraction? Back: 1. Define the Number: $x = 0.\dot{6}$.2. Multiply by a Power of 10: $10x = 6.\dot{6}$.3. Set Up an Equation: $10x - x = 6.\dot{6} - 0.\dot{6}$, which results in $9x = 6$.4. Solve for x: $x = \frac{6}{9}$ or $x = \frac{2}{3}$. This method can be applied to any repeating decimal by choosing the appropriate power of 10. <!--ID: 1697559938731--> ENDI
- STARTI [Basic] Question: How can you convert the repeating decimal $0.8\dot{3}$ into a fraction? Back: 1. Define the number: $x = 0.8\dot{3}$. 2. Multiply by 100: $100x = 83.\dot{3}$. 3. Subtract: $100x - x = 82.5$. 4. Solve for x: $x = \frac{82.5}{99}$, which simplifies to $x = \frac{55}{66}$.<!--ID: 1697559938743--> ENDI
- STARTI [Basic] Question: How can this method of converting repeating decimals into fractions be adapted for other bases? Back: The method can be applied to any base periodic number. Replace 10 with the base, $b$. If in base $b$ and one digit is repeating, multiply by $b$. If two digits are repeating, multiply by $b^2$, and so on. <!--ID: 1697559938754--> ENDI
- STARTI [Basic] Question: What is a polynomial? Back: A polynomial is an expression of the form \(f(x) = a_n x^n + \dots + a_1 x + a_0\), where \(a_0, a_1, \dots, a_n\) are coefficients from a field \(F\). The variable \(x\) is called the indeterminate. <!--ID: 1697559938765--> ENDI
- STARTI [Basic] Question: What are fields in mathematics? Back: Fields are sets of numbers where you can perform addition, subtraction, multiplication, and division (except by zero). Examples include the Rational numbers (\(\mathbb{Q}\)), Real numbers (\(\mathbb{R}\)), and Complex numbers (\(\mathbb{C}\)). <!--ID: 1697559938776--> ENDI
- STARTI [Basic] Question: What is the Field with Two Elements (\(F_2\))? Back: This field consists of two symbols \(\overline{0}\) and \(\overline{1}\) which behave similarly to the integers 0 and 1, with the exception that \(\overline{1} + \overline{1} = \overline{0}\). <!--ID: 1697559938787--> ENDI
- STARTI [Basic] Question: What is the degree of a polynomial? Back: The degree of a non-zero polynomial \(f(x)\) is the largest integer \(n\) such that \(a_n \neq 0\). It's denoted as \(\text{deg}(f)\). For a zero polynomial, we set \(deg(0)=-\infty\). <!--ID: 1697559938797--> ENDI
- STARTI [Basic] Question: How do you add two polynomials? Back: \( (a_n x^n + \dots + a_1 x + a_0) + (b_n x^n + \dots + b_1 x + b_0) = (a_n + b_n) x^n + \dots + (a_1 + b_1) x + (a_0 + b_0) \). <!--ID: 1697559938808--> ENDI
- STARTI [Basic] Question: What is the outcome when multiplying two polynomials? Back: The result involves using the distributive property and then collecting like terms. The degree of the result will be the sum of the degrees of the original polynomials. <!--ID: 1697559938819--> ENDI
- STARTI [Basic] Question: What does the Division Algorithm for \(F[x]\) state? Back: For any polynomials \(f(x)\) and \(g(x)\) in \(F[x]\) with \(g(x) \neq 0\), there exist unique polynomials \(q(x)\) and \(r(x)\) such that: \(f(x) = g(x)q(x) + r(x)\) where either \(r(x) = 0\) or \(\text{deg}(r(x)) < \text{deg}(g(x))\). <!--ID: 1697559938829--> ENDI
- STARTI [Basic] Question: What ensures the uniqueness of \(q(x)\) and \(r(x)\) in polynomial division? Back: Given two different expressions for \(f(x)\) divided by \(g(x)\), \(g(x)[q_1(x) - q(x)]\) would have a higher degree than \(r(x) - r_1(x)\), a contradiction, implying \(q_1(x) = q(x)\) and \(r(x) = r_1(x)\). <!--ID: 1697559938840--> ENDI
- STARTI [Basic] Question: What is the Remainder Theorem for polynomials? Back: The Remainder Theorem states that when a polynomial \( P(x) \) is divided by a linear divisor \( x - a \), the remainder is equal to \( P(a) \). <!--ID: 1697559938851--> ENDI
- STARTI [Basic] Question: What does the Factor Theorem state? Back: The Factor Theorem states that for a polynomial \( P(x) \), if \( P(a) = 0 \), then \( x - a \) is a factor of \( P(x) \). <!--ID: 1697559938862--> ENDI
- STARTI [Basic] Question: How is the Factor Theorem connected to the Remainder Theorem? Back: The Factor Theorem is essentially a special case of the Remainder Theorem. If the remainder when \( P(x) \) is divided by \( x - a \) is zero, then \( x - a \) is a factor of \( P(x) \). <!--ID: 1697559938873--> ENDI
- STARTI [Basic] Question: What is Ruffini's Rule? Back: Ruffini's Rule is a synthetic division method used to divide a polynomial by a linear factor of the form \( x - a \). It offers a fast way to obtain the quotient and the remainder. <!--ID: 1697559938884--> ENDI
- STARTI [Basic] Question: How can \( x^n - a^n \) be factored? Back: \( x^n - a^n \) can be factored as \( (x-a)(x^{n-1} + x^{n-2}a + x^{n-3}a^2 + \dots + xa^{n-2} + a^{n-1}) \). <!--ID: 1697559938893--> ENDI
- STARTI [Basic] Question: How is \( x^n + a^n \) factored for odd \( n \)? Back: \( x^n + a^n \) can be factored using similar principles as \( x^n - a^n \), but the signs within the factors alternate. <!--ID: 1697559938904--> ENDI
- STARTI [Basic] Question: What does expanding a polynomial in terms of \( x - a \) result in? Back: The expansion of a polynomial in terms of \( x - a \) will produce terms of the form \( c_k(x - a)^k \), where \( c_k \) are coefficients determined by the polynomial and the value of \( a \). <!--ID: 1697559938915--> ENDI
- STARTI [Basic] Question: What is the GCD of two polynomials? Back: The GCD (greatest common divisor) of two polynomials is the highest-degree polynomial that divides both given polynomials without leaving a remainder. <!--ID: 1697559938927--> ENDI
- STARTI [Basic] Question: How can the GCD of two polynomials be determined? Back: The GCD of two polynomials can be found using the polynomial division method or the extended Euclidean algorithm. <!--ID: 1697559938938--> ENDI
- STARTI [Basic] Question: What is the Extended Euclidean Algorithm for polynomials? Back: This algorithm is a polynomial version of the extended Euclidean algorithm for integers. It helps find the GCD of two polynomials and represents the GCD as a linear combination of the two polynomials. <!--ID: 1697559938949--> ENDI
- STARTI [Basic] Question: What is Bézout’s Lemma for Polynomials? Back: For polynomials \( P(x) \) and \( Q(x) \) with a GCD \( D(x) \), there exist polynomials \( U(x) \) and \( V(x) \) such that: \( P(x)U(x) + Q(x)V(x) = D(x) \). <!--ID: 1697559938960--> ENDI
- STARTI [Basic] Question: Who introduced Ruffini's Rule? Back: Ruffini's Rule was introduced by Paolo Ruffini, an Italian mathematician who made significant contributions to algebra. <!--ID: 1697559938970--> ENDI
- STARTI [Basic] Question: Who was Bézout and what did he introduce? Back: Étienne Bézout was a French mathematician who first stated and proved Bézout's Lemma for integers. Its adaptation to polynomials is crucial in algebraic computations. <!--ID: 1697559938981--> ENDI
- STARTI [Basic] Question: Sample Exam Question - Using the Remainder Theorem, what is the remainder when \( P(x) = 2x^3 - 3x^2 + 4x - 5 \) is divided by \( x - 2 \)? Back: The remainder is \( P(2) \). <!--ID: 1697559938993--> ENDI
- STARTI [Basic] Question: Sample Exam Question - Using the Factor Theorem, is \( x - 3 \) a factor of \( Q(x) = x^3 - 6x^2 + 11x - 6 \)? Back: If \( Q(3) = 0 \), then \( x - 3 \) is a factor. <!--ID: 1697559939003--> ENDI
- STARTI [Basic] Question: Sample Exam Question - How do you use Ruffini's Rule to divide \( P(x) = x^3 - 2x^2 - 4x + 8 \) by \( x + 1 \)? Back: Arrange the polynomial and the divisor, write down the coefficients, and carry out the synthetic division process. <!--ID: 1697559939014--> ENDI
- STARTI [Basic] Question: Sample Exam Question - Expand \( f(x) = (x - 2)(x - 3)(x - 4) \) in terms of \( x - 2 \). Back: Expansion will result in terms of the form \( c_k(x - 2)^k \). <!--ID: 1697559939026--> ENDI
- STARTI [Basic] Question: Sample Exam Question - How do you use the extended Euclidean algorithm to find the GCD of the polynomials \( A(x) = x^4 - 1 \) and \( B(x) = x^3 + x^2 + x + 1 \)? Back: The method involves repeated polynomial division, similarly to the standard extended Euclidean algorithm with integers. <!--ID: 1697559939037--> ENDI
- STARTI [Basic] Question: Sample Conceptual Question - Describe the significance of Bézout's Lemma in polynomial algebra and its relation to the extended Euclidean algorithm. Back: Bézout's Lemma for polynomials provides a representation of the GCD of two polynomials as a linear combination of them, which is derived using the extended Euclidean algorithm. <!--ID: 1697559939048--> ENDI
- STARTI [Basic] Question: What is Ruffini's Rule? Back: Ruffini's Rule, also known as Ruffini's Horner's method, is a quick polynomial division technique when dividing a polynomial by a linear divisor of the form $x - c$. It's especially useful for synthetic division. ENDI
- STARTI [Basic] Question: What should be the form of the divisor for Ruffini's Rule? Back: The divisor should be in the form $x - c$ or $x + c$. <!--ID: 1697624934219--> ENDI
- STARTI [Basic] Question: How do you set up the polynomial for Ruffini's Rule? Back: Write down the polynomial you want to divide, called $P(x)$, and list its coefficients in descending order of the degree of each term. <!--ID: 1697624934232--> ENDI
- STARTI [Basic] Question: How do you initialize the table for Ruffini's Rule? Back: Draw a small 'L' shape with a horizontal and vertical line. Write the value of $c$ at the corner. Next to $c$, write down the coefficients of $P(x)$ in order. Place a 0 for any missing degree to create the first row of numbers. <!--ID: 1697624934242--> ENDI
- STARTI [Basic] Question: In Ruffini's Rule, what is the first entry after setting up the table? Back: Bring down the leading coefficient from the first row as it is. Write it below the horizontal line to start a new row. <!--ID: 1697624934251--> ENDI
- STARTI [Basic] Question: Describe the multiplication and addition steps in Ruffini's Rule. Back: Multiply the number you just wrote below the line by $c$. Write the result below the next coefficient in the first row. Then, add the coefficient from the first row and the result you obtained. Write this sum below the line. Continue this process for all coefficients in the first row. <!--ID: 1697624934260--> ENDI
- STARTI [Basic] Question: How do you interpret the results of Ruffini's Rule? Back: The numbers in the second row represent the coefficients of the quotient polynomial in descending order. The rightmost number in the second row represents the remainder. If the remainder is 0, $P(x)$ is divisible by $x - c$. If not, it's the remainder when dividing $P(x)$ by $x - c$. <!--ID: 1697624934269--> ENDI
- STARTI [Basic] Question: In the given example, what is the quotient polynomial and remainder when dividing $P(x) = x^3 - 6x^2 + 11x - 6$ by $x - 1$ using Ruffini's Rule? Back: The quotient polynomial is $x^2 - 5x + 6$ and the remainder is 0. <!--ID: 1697624934278--> ENDI
- STARTI [Basic] Question: What is an irreducible polynomial? Back: An irreducible polynomial is a non-constant polynomial that cannot be expressed as the product of two non-constant polynomials. It's analogous to prime numbers in the integers. <!--ID: 1698051503475--> ENDI
- STARTI [Basic] Question: How is an irreducible polynomial mathematically defined over a field $F$? Back: A polynomial $p(x)$ over a field $F$ is irreducible over $F$ if it cannot be written as the product of two non-constant polynomials from $F[x]$. <!--ID: 1698051503493--> ENDI
- STARTI [Basic] Question: What is the status of constant polynomials in terms of reducibility? Back: Constant polynomials are neither reducible nor irreducible by convention. <!--ID: 1698051503505--> ENDI
- STARTI [Basic] Question: Are polynomials of degree 1 reducible or irreducible? Back: Polynomials of degree 1 are always irreducible, trivially. <!--ID: 1698051503517--> ENDI
- STARTI [Basic] Question: Is the polynomial $x^2 + 1$ reducible over the real numbers? Back: No, $x^2 + 1$ is irreducible in the real numbers, but it is reducible in the complex numbers as $(x+i)(x-i)$. <!--ID: 1698051503528--> ENDI
- STARTI [Basic] Question: Why is the concept of irreducibility important? Back: Irreducibility is central in polynomial factorization, algebraic number theory, and various areas of algebra. It provides insights into the structure and properties of polynomials and their roots. <!--ID: 1698051503539--> ENDI
- STARTI [Basic] Question: How can we determine if a quadratic polynomial is reducible? Back: For a quadratic polynomial $p(x)=ax^2+bx+c$ with integer coefficients, it is reducible if and only if $b^2-4ac$ is a square in $F$. <!--ID: 1698051503550--> ENDI
- STARTI [Basic] Question: What does the Rational Root Theorem state? Back: If a polynomial $p(x) = a_nx^n + \dots + a_1x + a_0$ with integer coefficients has a rational root $\frac{p}{q}$, then $p$ divides $a_0$ and $q$ divides $a_n$. <!--ID: 1698051503562--> ENDI
- STARTI [Basic] Question: Does the polynomial $p(x) = x^2 - 2$ have any rational roots? Back: No, $p(x) = x^2 - 2$ doesn't have rational roots. It is irreducible over the rationals but has roots $\sqrt{2}$ and $-\sqrt{2}$ which are irrational. <!--ID: 1698051503575--> ENDI
- STARTI [Basic] Question: How did we check for the rational roots of $p(x) = x^2 - 2$? Back: We used the discriminant: $b^2-4ac\implies 0-4\cdot1\cdot(-2)\implies8>0$ which showed there are no rational roots. <!--ID: 1698051503586--> ENDI
- STARTI [Basic] Question: What should one remember when determining if a polynomial is irreducible? Back: Always test for potential roots using tools like the Rational Root Theorem, but remember this is just one step in determining irreducibility. <!--ID: 1698051503598--> ENDI
- STARTI [Basic] Question: What is the Unique Factorisation Theorem for polynomials? Back: Every non-constant polynomial over a field $F$ is a product of irreducible polynomials, in an essentially unique way (up to permuting factors and multiplying them by non-zero constants). <!--ID: 1698054122915--> ENDI
- STARTI [Basic] Question: How can the polynomial $2x^2+10x+12$ be factored? Back: It can be factored in multiple ways such as: $2(x+2)(x+3)$, $(2x+4)(x+3)$, $(x+2)(2x+6)$, and $(3x+6)(\frac{2}{3}x+2)$. <!--ID: 1698054122939--> ENDI
- STARTI [Basic] Question: How many distinct roots can a polynomial of degree $n \ge 0$ have in a field $F$? Back: A polynomial of degree $n \ge 0$ can have at most $n$ distinct roots in a field $F$. <!--ID: 1698054122957--> ENDI
- STARTI [Basic] Question: Does a polynomial of degree 0 have any roots? Back: No, a polynomial of degree 0 has no roots since $x^0$ is always equal to 1. <!--ID: 1698054122972--> ENDI
- STARTI [Basic] Question: How can one prove that a polynomial of degree $n \ge 0$ can have at most $n$ distinct roots? Back: Using the Factor Theorem and induction, one can deduce that any polynomial can be expressed in terms of its roots. This method will allow us to find at most $n$ distinct roots for the polynomial. <!--ID: 1698054122989--> ENDI
- STARTI [Basic] Question: What does the Interpolation Theorem state? Back: For distinct elements $b_1,\ldots, b_n$ of a field $F$ and arbitrary elements $c_1,\ldots,c_n$ of the same field, there exists a unique polynomial $f(x) \in F[x]$ of degree at most $n-1$ that satisfies $f(b_1) = c_1$, $f(b_2) = c_2$, ..., $f(b_n) = c_n$. <!--ID: 1698054123005--> ENDI
- STARTI [Basic] Question: Who is credited with the Fundamental Theorem of Algebra? Back: Argand, 1806. <!--ID: 1698054123022--> ENDI
- STARTI [Basic] Question: What does the Fundamental Theorem of Algebra guarantee? Back: Every non-constant polynomial has at least one root in the complex number system. <!--ID: 1698054123037--> ENDI
- STARTI [Basic] Question: State the Fundamental Theorem of Algebra. Back: For every non-constant polynomial \( p(z) \) with complex coefficients, there exists a complex number \( c \) such that \( p(c) = 0 \). Every polynomial of degree \( n \geq 1 \) has at least one complex root and, considering multiplicity, has exactly \( n \) complex roots. <!--ID: 1698054123053--> ENDI
- STARTI [Basic] Question: What is the implication about the magnitude of a non-constant polynomial from the proof sketch? Back: There exists some radius \( R \) such that \( |p(z)| \rightarrow \infty \) as \( |z| \rightarrow \infty \), for all \( |z| > R \). <!--ID: 1698054123065--> ENDI
- STARTI [Basic] Question: What does Rolle's Theorem for Complex Polynomials state in the proof sketch? Back: If \( p(z) \) doesn't have a root in the disc of radius \( R \), then neither does its derivative. This is a contradiction since the derivative should have a root. <!--ID: 1698054123074--> ENDI
- STARTI [Basic] Question: What is the implication about complex roots for polynomials with real coefficients? Back: Complex Roots Come in Pairs: If a polynomial has real coefficients and one non-real complex root, then its complex conjugate is also a root. <!--ID: 1698054123082--> ENDI
- STARTI [Basic] Question: What does the degree of a polynomial indicate about its roots? Back: A polynomial of degree \( n \) will have exactly \( n \) roots in the complex numbers, considering multiplicity. <!--ID: 1698054123090--> ENDI
- STARTI [Basic] Question: What is the relationship between roots and factors of a polynomial? Back: If \( c \) is a root of \( p(z) \), then \( (z - c) \) is a factor of \( p(z) \). Using division, \( p(z) \) can be expressed as \( p(z) = (z-c)q(z) \) where \( q(z) \) is of degree \( n-1 \). <!--ID: 1698054123099--> ENDI
- STARTI [Basic] Question: How can you show that the polynomial \( p(z) = z^2 + 1 \) has no real roots but two complex roots? Back: By evaluating and realizing that no real value will satisfy this equation. The roots are \( i \) and \( -i \). <!--ID: 1698054123107--> ENDI
- STARTI [Basic] Question: How do you find all roots, real or complex, of the polynomial \( p(z) = z^3 - 6z^2 + 11z - 6 \)? Back: Factorize or use appropriate root-finding methods. <!--ID: 1698054123116--> ENDI
## Weeks Content
### Week 1
[[Algebra_slides_week_01_handout.pdf]]
[[Algebra_notes_week_01.pdf]]
[[Practical_1.pdf]]

[[Answers to Algebra Practical 1]]
___
### Week 2
[[Algebra_slides_week_02_handout.pdf]]
[[Algebra_notes_week_02.pdf]]
[[Practical_2.pdf]]

[[Answers to Algebra Practical 2]]
___
### Week 3
[[Algebra_slides_week_03_handout.pdf]]
[[Algebra_notes_week_03.pdf]]
[[Practical_3.pdf]]

[[Answers to Algebra Practical 3]]
[[Algebra Coursework 1]]
___
### Week 4
[[Algebra_slides_week_04_handout.pdf]]
[[Algebra_notes_week_04.pdf]]
[[Practical_4.pdf]]

[[Answers to Algebra Practical 4]]
___
### Week 5
![[Algebra_slides_week_05_handout.pdf]]
![[Algebra_notes_week_05.pdf]]
[[Practical_5.pdf]]

[[Answers to Algebra Practical 5]]
