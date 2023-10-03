# MATLAB Logbook

## Personal Details
- **Name:** William Fayers
- **Course:** MTH1006 - Computer Algebra and Technincal Computing
- **Academic Year:** 2023-2024
- **Institution:** University of Lincoln, School of Mathematics and Physics

## Declaration
I confirm that this logbook is all my own work and that all references and quotations from both primary and secondary sources have been fully identified and properly acknowledged - William Fayers

---
## Week 1 (25/09/2023 - 01/10/2023)
![[certificate.pdf]]
### Summary
- *Completed on-boarding for MATLAB*

### Reflection
- *Fairly simple at the minute, but it got pretty interesting towards the end of Onramp - I'm looking forward to how I can use MATLAB to further improve my mathematics!*

---
## Week 2 (02/10/2023 - 08/10/2023)

### Summary
Today, I worked on several MATLAB exercises:

**2.1 Calculator**:
- I used MATLAB to determine mathematical operations including basic arithmetic, trigonometric functions, logarithms, and complex calculations. 
- Additionally, I calculated the area of a circle with a given radius and used the `help` command to understand the function of `acos`.

**2.2 Variables**:
- I practiced setting and manipulating various variables in MATLAB. This included performing arithmetic on these variables and updating their values.
- I also learned to use previous commands for convenience through up/down arrow keys.

**2.3 Variable Names**:
- I explored different potential variable names to determine which ones are valid in MATLAB. This helped me understand naming conventions and restrictions in MATLAB.

**2.4 Scripts**:
- I created a MATLAB script named `my_script`, where I assigned values to variables and computed an equation. 
- After writing the script, I executed it to determine the value of the equation.

**2.5 Vectors and Intrinsic Functions**:
- I worked with vectors, learning to create them using the colon operator.
- I also utilized `linspace` to produce vectors and applied different mathematical functions to these vectors.

**2.6 Complex Numbers**:
- I delved into complex number operations, calculating products, magnitudes, and other properties of complex numbers.
- Using MATLAB functions like `imag` and `real`, I extracted the imaginary and real parts of specific complex numbers respectively.
- I also determined the argument of a complex fraction.

### Exercises
#### 2.1 Calculator
[[Calculator Code Output (MATLAB)]]

1. Use MATLAB to determine:
   - (a) $\frac{123}{456}$
   - (b) $\ln(5)$
   - (c) $\log(5)$
   - (d) $\tan(6)$
   - (e) $\frac{71}{3}$
   - (f) $e^8$
   - (g) $\sin\left(\frac{2\pi}{3}\right)$
   - (h) $\sin(\cos(9))$
   - (i) $e^{2\sqrt{3\sin(4+\log(5))+6}-7} + 8$
2. The radius $r$ of a circle is 6. Calculate the area $A$ of the circle using MATLAB. Hint: $A = \pi r^2$
3. Look up the command `acos` using the command `help`, and calculate $\arccos(a)$ for $a = \frac{1}{2}$. Divide the answer by $\pi$ to write the result as a fraction of $\pi$.
#### 2.2 Variables
[[Variables Code Output (MATLAB)]]

1. Set a variable `a` equal to `7/3`, `b` equal to `9/6`. Finally, set a variable `c` equal to `a · b`. What is `c`?
2. Create a variable `myage` and store your age in it. Subtract two from the value of the variable, and update the variable `myage` with this new value. Add one to the value of the variable, and update the variable again. Observe the Workspace Window and Command History Window as you do this.
3. Set a variable `x` equal to `10`. Increase the content of the variable by `1`. Now multiply the content of the variable by a factor `2`. What is the value of `x`?
4. Set a variable `r` equal to `6`. Set another variable $A$ equal to $\pi r^2$ (by referring to the variable `r`), to calculate the area of a circle. Increase the radius by `2` and re-calculate the area. Hint: you can use the up/down arrows on the keyboard to re-use a previously typed command. Afterwards, repeat the calculation for a radius of $1.3 \times 10^{-12}$. Does `A` need to be updated?

#### 2.3 Variable names
[[Variable Names Code Output (MATLAB)]]

1. Test and tell for each of the following names if it is a valid variable name. Hint: see if it appears in your workspace, if you try to assign a value to it.
   - (a) `x` **Valid**
   - (b) `x2` **Valid**
   - (c) `2x` **Invalid**
   - (d) `xy` **Valid**
   - (e) `x x` **Invalid**
   - (f) `exc3.1` **Invalid**
   - (g) `tan` **Valid**
   - (h) `if` **Invalid**
   - (i) `end` **Invalid**
   - (j) `a long variable name` **Invalid**
   - (k) `a_long_variable_name2` **Valid**
   - (l) `x$` **Invalid**
   - (m) `x%` **Invalid**
   - (n) `a_` **Valid**
   - (o) `_a` **Invalid**
#### 2.4 Scripts
[[Scripts Code Output (MATLAB)]]

1. (a) Create a script with the name `my_script`, by typing in the command line: `edit my_script` Note that MATLAB will automatically add the extension `.m`, so one does not need to type this.
   - (b) In the script set `a = 1`, `b = 2`, `c = 3`, `x = 4` and then set a variable $y$ to $ax^2 + bx + c$.
   - (c) Execute the script by typing in the name of the script on the command line (without the extension `.m`). What is the value of $y$?
#### 2.5 Vectors and intrinsic functions
[[Vectors Code Output (MATLAB)]]

1. Use the colon, `:`, to create a vector of integers starting from `11` to `20`. Hint: Use the `help` function for `:` for more information
2. Use the colon operator to:
   - (a) create a vector of integers starting from `100` to `110` with step `2`
   - (b) create a vector starting from `100` to `110` with step `0.1`
3. Use `linspace` to create a vector from `11` to `20` with `50` elements.
4. Create a vector of `10` elements between `0` and `3`, set the result in a variable `x`, and then calculate $\sin(x)$ for all these values at once.
5. Create a vector `x` containing the values `0.1, 0.2, 0.3, . . . , 1.0` and hence find the following functions of the entries:
   - (a) The hyperbolic sine. Hint: use `lookfor hyperbolic`
   - (b) The natural logarithm.
   - (c) The base-10 logarithm.
#### 2.6 Complex numbers
[[Complex Numbers Code Output (MATLAB)]]

1. Calculate:
   - (a) $(1 + i)(1 − i)$
   - (b) $|2 + 4i|$
   - (c) $i^i$
   - (d) $\sqrt{i}$
   - (e) $(3 + 4i)(5 − 6i)^{7+\frac{8i \cos(9+10i)}{11}}$
2. Set `x` to the imaginary part of `tan(i)`. What is the value of `x`? Hint: `imag`.
3. Set `x2` to the real part of $\sqrt{i}$. What is the value of `x2`? Hint: `real`.
4. Determine the argument of $z = \frac{1}{i}$ using MATLAB.
### Reflection
- *This week was again fairly simple, but got me even more excited on how I can use MATLAB for more complex mathematics. This week also gave me my first challenge, where I thought I backed up my notes and then accidentally deleted them... but my back-ups weren't working. So, outside of lecture hours I did some self-study to recreate them all (including this logbook).*
- *I also thought some of the commands were interesting - such as using angle() instead of arg().*
- *Hopefully I'll get used to multiplying by explicitly saying * too! It's pretty tricky to remember, especially with things like $2\pi$ being written as `2*pi`.*

---
## Week 3 (xx/xx/2023 - xx/xx/2023)

### Summary
- *Enter your summary here...*

### Exercises
- *Enter your exercises here...*

### Reflection
- *Enter your reflection here...*

---
(Continue in the same format for the remaining weeks)

---
## References
- *Enter your references here...*