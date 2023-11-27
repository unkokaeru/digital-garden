 - When we write a positive integer in decimal notation, say 237, we mean that $(237)_{10}=2\cdot10^2+3\cdot10^1+7\cdot10^0$. This can be written in any base, however, e.g. $(237)_{10}=(456)_7=(1422)_5=(11101101)_2=(ED)_{16}$.
 - The notation extends from integers to positive real numbers by writing further digits (possibly an infinite amount) after a point, as we're used to with base 10, e.g. $(123.456)_{10}=1\cdot10^{2}+2\cdot10^{1}+3\cdot10^{0}+4\cdot10^{-1}+5\cdot10^{-2}+6\cdot10^{-3}$.
 - As we can see, the pattern for notation is like so: let a number $n$ be denoted by its digits $(n_1n_2n_3n_4.n_5)_b$ in base $b$. Thus, $n=n_1\cdot b^3+n_2\cdot b^2+n_3\cdot b^1+n_4\cdot b^0+n_5\cdot b^{-1}$.
 - Converting integers from any base into a decimal is trivial - either by definition, as demonstrated before, or with the following arrangement derived by factorising out the base (to reduce the number of operations):$$(1422)_5=((1\cdot5+4)\cdot5+2)\cdot5+2=(9\cdot5+2)\cdot5+2=47\cdot5+2=237$$
 - There are also tabular arrangements (based on [[Ruffini's Rule]]): [Horner's Method](https://demonstrations.wolfram.com/HornersMethodForConvertingAnIntegerFromBaseBToBase10/)
 - Reversing this procedure converts from decimal to any base - keep dividing by the base, ignoring the remainder, e.g. converting 14950 to base 7:
$$
14950=7\cdot2135+5
$$
$$
2135=7\cdot305+0
$$
$$
305=7\cdot43+4
$$
$$
43=7\cdot6+1
$$
$$
6=7\cdot0+6
$$
 - The digits in base 7 are then the remainders, read from the bottom up: $(14950)_{10}=(61405)_7$. Note that this looks similar to the [[Euclidean algorithm (original note)]], but it is completely different in terms of the numbers carried forward in each division.
 - Extending both parts into the real set of numbers is fairly simple, just first remove any numbers after their point by multiplying/dividing by a number ($b^n$, where $b$ is the base and $n$ is the number of digits after the point), then divide/multiply by the same number after the conversion. If there are infinitely many digits after the point, then just take an approximation.