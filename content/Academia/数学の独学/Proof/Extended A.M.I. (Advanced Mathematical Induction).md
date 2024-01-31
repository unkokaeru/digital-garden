# Extended A.M.I. (Advanced Mathematical Induction)

## Introduction

**Advanced Mathematical Induction (A.M.I.)** is a fundamental principle of mathematics used to prove statements or propositions that are formulated in terms of natural numbers. The classic form of mathematical induction involves proving a base case (typically at $n = 1$) and then demonstrating that if the statement holds for an arbitrary natural number $n$, it must also hold for $n+1$. However, in **Extended A.M.I.**, the base case can start at any natural number $n > 1$. This technique is particularly useful when the statement to be proven does not hold for the initial few natural numbers.

## Principle of Extended A.M.I.

The principle of Extended A.M.I. is similar to the classical induction but with a slight modification in the base step. The steps are as follows:

1. **Base Step**: Prove that the statement is true for a starting value $n = k$, where $k > 1$.

2. **Inductive Step**: Show that if the statement is true for some arbitrary number $n \geq k$, then it is also true for $n+1$.

Once these two steps are successfully demonstrated, it can be concluded that the statement holds for all natural numbers greater than or equal to $k$.

## Applications

Extended A.M.I. is particularly useful in scenarios where a proposition is not true for the initial few natural numbers. For example, certain properties in combinatorics, number theory, or sequences and series may only hold for larger values of $n$. Extended A.M.I. allows mathematicians to bypass the initial "problematic" values and still establish a general proof for the proposition.

## Example

Consider the statement: "For every integer $n \geq 5$, the inequality $2^n > n^2$ holds."

1. **Base Step**: For $n = 5$, $2^5 = 32$ which is greater than $5^2 = 25$. Hence, the statement is true for the base case.

2. **Inductive Step**: Assume the statement is true for some $n \geq 5$. We need to show it's true for $n+1$. By the inductive hypothesis, $2^n > n^2$. Multiplying both sides by 2, we get $2^{n+1} > 2n^2$. Since $n \geq 5$, it's clear that $2n^2 > (n+1)^2$, thus $2^{n+1} > (n+1)^2$, proving the inductive step.

## Conclusion

By the principle of Extended A.M.I., the statement holds for all integers $n \geq 5$. This technique extends the power of classical mathematical induction to a wider range of problems, particularly when initial values do not satisfy the proposition.

---

### Test Questions

1. STARTI [Basic] Question: Define the base step in Extended A.M.I. Back: In Extended A.M.I., the base step involves proving that the statement is true for a starting value $n = k$, where $k > 1$. ENDI
2. STARTI [Basic] Question: How does Extended A.M.I. differ from classical mathematical induction? Back: Extended A.M.I. differs in that the base case starts at any natural number $n > 1$, rather than the classic base case of $n = 1$. ENDI
3. STARTI [Basic] Question: Apply Extended A.M.I. to prove that for every integer $n \geq 5$, $2^n > n^2$. Back: Base Step: Verify for $n = 5$. Inductive Step: Assume true for $n$, show for $n+1$. The proof follows from the inequality $2^{n+1} > 2n^2$ and $2n^2 > (n+1)^2$ for $n \geq 5$. ENDI