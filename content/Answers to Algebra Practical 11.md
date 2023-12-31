#### Question 1

Let $f(x) = x^{3}-x+1$.

##### Question 1a

Prove that $f(x)$ is irreducible in $\mathbb{F}_{3}$. Thus, we want to prove that $[0],[1],[2]$, where $[n]\equiv n\mod{3}$, are not solutions; this is equivalent to proving that $[0],[\pm1]$ are not solutions.

$f([0])=[0]^3-[0]+1=[1]$
$f([1])=[1]^3-[1]+1=[1]$
$f([-1])=[-1]^3-[-1]+1=[1]$

Hence, $f(x)$ has no solutions in $\mathbb{F}_{3}\iff\text{irreducible under }\mathbb{F}_3$ .
##### Question 1b

Prove that $f(x)$ is irreducible in $\mathbb{F}_{5}$. Thus, we want to prove that $[0],[1],[2],[3],[4]$, where $[n]\equiv n\mod{5}$, are not solutions; this is equivalent to proving that $[0],[\pm1],[\pm2]$ are not solutions.

$f([0])=[0]^3-[0]+1=[1]$
$f([1])=[1]^3-[1]+1=[1]$
$f([-1])=[-1]^3-[-1]+1=[1]$
$f([2])=[2]^3-[2]+1=[7]=[2]$
$f([-2])=[-2]^3-[-2]+1=[-5]=[0]$

Therefore, $(x+2)|f(x)$, so using Ruffini's Rule...

| (-2) | 1   | 0   | -1  | 1   |
| ---- | --- | --- | --- | --- |
|      | 0   | -2  | 4   | -6  |
|      | 1   | -2  | 3   | -5  | 

Where $r(x)=[-5]=[0]$, therefore, $f(x)=(x+2)(x^2-2x+3)$. Hence if we show that the two factors are irreducible under $\mathbb{F}_{5}$, then we'll show that $f(x)$ is also. Namely that $p(x)=x+2$ has no solutions under the finite field and that neither does $q(x)=x^2-2x+3$.

$p([0]),p([\pm1]),p([\pm2])\ne0$
$q([0]),q([\pm1]),q([\pm2])\ne0$

Hence, if $p(x)$ and $q(x)$ have no solutions in $\mathbb{F}_{5}\iff\text{irreducible under }\mathbb{F}_5$ , $f(x)$ must also be irreducible under $\mathbb{F}_{5}$.$\space\blacksquare$
