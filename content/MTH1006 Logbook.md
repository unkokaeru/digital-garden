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
## Week 3 (09/10/2023 - 15/10/2023)

### Summary
- *Plotted sin(x), cos(x), and various quadratic functions, refining with legends and specific styles.*
- *Worked with vector indexing, extracting and calculating using elements.*
- *Tackled mathematical series and fractional sums using vector operations.*
- *Manipulated and merged strings, making specific modifications.*
- *Evaluated a range of Boolean expressions and made string comparisons.*

### Exercises
#### 3.1 Plotting
[[Plotting Code Output (MATLAB)]]
1. **Plotting sin(x) and cos(x)**
    - Create a script that plots the function $y = \sin(x)$ for $x \in [-2\pi, 2\pi]$ using an interval in $x$ of $\frac{\pi}{50}$.
    - On the same figure plot $y = \cos(x)$ with a dashed, red line.
    - The x-axis should be in the range $-2\pi$ to $2\pi$.
    - Include a legend.
    - Save the [resulting plots](Q3.1.1.png) as `.png` files with the name as the exercise number.

2. **Plotting Quadratic Curves**
    - Plot the four curves $y = x^2 + c$ for $c = 0, 2, 4, 6$, with $x \in [-5, 5]$ (use at least 100 points).
    - Hint: get help on the command `hold`.

3. **Custom Plot of $y(x) = e^{-x^2}$**
    - Create a plot for $x$ in the range -0.5 to 1.5 with the following features:
        - The curve should be a black broken line.
        - Label the y-axis as 'This is the y axis'.
        - x-values range: -0.5 to 1.5.
        - y-values range: 0 to 1.
        - Title: 'Plot of the function $y(x)$. Author: [Your name]'
#### 3.2 Vector indexing – one element
[[Vector Indexing - One Element Code Output (MATLAB)]]
1. **Vector Creation and Indexing**
    - (a) Create a vector of 5 elements ranging from 2 to 4 (equally spaced), and store in variable `v`.
    - (b) Store the first element in `x`.
    - (c) Store the last element in `y`.
    - (d) Store the third element in `z`.
    - (e) Calculate $x + y + z$. Verify your answer by hand.
#### 3.3 Vector operations
[[Vector Operations Code Output (MATLAB)]]
1. **Mathematical Series**
    - (a) Calculate $\sum_{k=1}^{50} k$
    - (b) Calculate $\sum_{k=1}^{20} k^2$

2. **Vector-based Sums**
    - (a) Find the sum: $\frac{3}{1} + \frac{5}{2} + \frac{7}{3} + \frac{9}{4}$
    - (b) Calculate: $\frac{2}{1} + \frac{4}{2} + \frac{8}{3} + \frac{16}{4} + \frac{32}{5} + \frac{64}{6} + \frac{128}{7} + \frac{256}{8}$

3. **Vector and Scalar Variables**
    - (a) Set a scalar variable `maxx` to the maximum of the vector `x`.
    - (b) Set a vector variable `cosx` to the $\cos(x)$ for all values of `x`.
    - (c) Set a scalar variable `meanx` to the average of `x`.
#### 3.4 Strings
[[String Code Output (MATLAB)]]
1. **String Manipulations**
    - (a) Create a string ‘this is a string’ and store in variable `s`.
    - (b) Create a string named `s1` with contents ‘this is ‘.
    - (c) Create a string named `s2` with contents ‘a string’.
    - (d) Combine the two strings in a new variable `stot`.
    - (e) Change the first element of `stot` to 'T'.
    - (f) Add an exclamation mark to the end of `stot`.
#### 3.5 Boolean algebra
[[Boolean Algebra Code Output (MATLAB)]]
1. **Boolean Comparisons**
    - Determine the following:
        - (a) $1 > 0$
        - (b) $3 \geq 4$
        - (c) $(3 > 4)$ or $(3 < 4)$
        - (d) $8 \neq 9$
        - (e) $3 = 3 + 1$
        - (f) not false
        - (g) true and (true or false)

2. **Variable Comparisons**
    - Set a variable `n` equal to $\pi$.
    - Set `b1` equal to $(n > 3)$.
    - Set variable `b2` equal to 'not `b1`'. What is the content of variable `b2`?

3. **String Comparisons**
    - Create a string named `s` with contents 'hi'.
    - Determine if it is equal to the following using `strcmp`:
        - (a) 'Hii'
        - (b) 'hi'
        - (c) 'Hi'
        - (d) 'hi '

### Reflection
- *This session was again very simple, although I did notice I needed a few minutes to relearn the commands from the last few weeks - this week I think I'll do some independent work from a library book to keep me from forgetting everything.*

---
## Week 4 (16/10/2023 - 22/10/2023)

### Summary
- Today, I worked on three main tasks in MATLAB:
	1. **Output Commands**:
	   - Used `disp` command to display strings.
	   - Created scripts to output numerical values as strings.
	2. **Conditional Branching**:
	   - Practiced with `if` statements to evaluate and display conditions.
	   - Developed a script to compare temperatures between two days.
	3. **Functions**:
	   - Completed some modules in Matlab Academy under Matlab Fundamentals.
	   - Created and modified a function `area_circle` to calculate the area of a circle, and adjusted it to handle different input types and scenarios.

### Exercises
#### 4.1 Output
[[Output Code Output (MATLAB)]]
1. Output the string `This string has been written to the screen` using the `disp` command.
2. Write a script that sets the variable $x$ to $\sqrt{3}$ and then outputs a string from $x$. Hint: use `num2str`.
3. Write a script that sets a number to the variable $T$ and subsequently outputs the text `The temperature is ...` where the dots have to be replaced by the actual number contained in $T$. For example, if $T = 37$, the output should be `The temperature is 37`.
#### 4.2 Conditional Branching
[[Conditional Branching Code Output (MATLAB)]]
1. Write a script that sets $x$ to a value. Then use the `if` statement to test if the number is larger than $0$. If it is larger than zero, then write to the screen that `This number is larger than zero`. Run the script with a positive and with a negative number.
   
2. 
    (a) Write a script that sets the variable `Saturday` to $15$, and the variable `Sunday` to $17$. 
    (b) Add at the end an `if` statement that displays the string `Saturday is colder` if `Saturday < Sunday`.
    (c) Add another `if` statement, which displays the string `Sunday is colder`, if `Sunday < Saturday`.
    (d) Add another `if` statement, which displays the string `Both days have the same temperature`, if the two variables are equal.
    (e) Change the first line of the script so that `Saturday` equals $18$ and make sure the script runs as expected.
    (f) Do the same for `Saturday` equal to $17$.

3. Create a script named `testnumber.m`:
    (a) At the start of the script, set a variable $z$ to $2 + 3i$.
    (b) Add an `if` statement to test if the imaginary part of $z$ is unequal to $0$ (this implies it is a complex number). If this is the case, then multiply $z$ by its complex conjugate (see help of `conj`), take the square root of this and store the result in $l$. Also set a string named `s` to `this is a complex number`.
    (c) Add another `if` statement, such that if the number $z$ is not complex (imaginary part is $0$), then just square the number and take the square root of it, and store the result in $l$. In this case, also set the string named `s` to `this is a real number`.
    (d) How would you test if the number is a integer (whole) number? Implement this as well in the script, including an appropriate string.
    (e) Test the script by changing the value of $z$ in the beginning of the script to (i) a real number and (ii) an integer.
#### 4.3 Functions
[[Functions Code Output (MATLAB)]]
1. Go to [Matlab Academy](https://matlabacademy.mathworks.com), login using the credentials you created during week $1$, and open the course Matlab Fundamentals. Complete:
    (a) ~~Increasing automation with functions: Creating and Calling Functions (15.1)~~
    (b) ~~Increasing automation with functions: Function Files (15.2)~~
    (c) ~~Increasing automation with functions: Workspaces (15.3)~~

2. In this exercise a user-defined function will be created:
    (a) Start by creating a new file, named `area_circle`, using `edit area_circle` in the command line.
    (b) Add the following code into this file: 
        ```
        function A=area_circle(r) 
	        % Calculates the area of a circle given the radius 
	        A=pi*r^2; 
        end
        ```
        Notice that $r$ is the input argument and $A$ is the output argument.
    (c) Calculate the area of a circle of radius $4$, by calling the function from the command line by typing `>> area_circle(4)`.
    (d) Call the function for $r = 2$ (instead of $4$).
    (e) Within the function definition, change the input argument $r$ to $R$, and also change the formula to $A=\pi R^2$. Test if the function still works by calling it from the command line.
    (f) Change the output argument $A$ to `area` and make a similar change in the formula. Test if the function still works by calling it from the command line.
    (g) Change the comment in the function and observe this comment by typing `help area_circle` in the command line.
    (h) Now call the function for a vector `radii=[3,4,5]`. Does the function work? If not, adjust the function, by replacing `^` with `.^` and test it again.
    (i) Finally, change the function so that a diameter is expected as an input argument. Change the symbol $R$ to $d$ for this, and adjust the formula accordingly.
### Reflection
- *Unfortunately I did not get time to do some independent work last week as I planned, and yet again did it display to me how much I should be doing it - it's so hard to remember everything when you only use it once a week!*
---
## Week 5 (23/10/2023 - 29/10/2023)
### Summary
 - *Made an Anki deck for MTH1006*
- *I developed functions for temperature conversions and plotted exponential curves, incorporating error checks for complex numbers.*
- *Determined the volume of a cone using its radius and height.*
- *Calculated various summations, both simple and squared, and expanded to geometric series.*
- *Crafted functions to evaluate the sum of series, involving squares, cubes, and factorial denominators, and cross-checked manually.*
- *Implemented a break mechanism in loops to cap the summation based on a set threshold.*
- [[MATLAB Coursework 1 (files)]]
### Exercises
#### 5.1 Functions and scripts
[[Functions and Scripts Code Output (MATLAB)]]
1. **Celsius to Fahrenheit:**
	- (a) Write a script that converts a temperature in Celsius to Fahrenheit using the formula:
      $$
      F = \frac{9}{5} C + 32
      $$
      Subsequently output: `The temperature is ... degrees Celsius, which corresponds to ... degrees Fahrenheit.`
	- (b) Test with: $0^\circ C$, $25^\circ C$, $37.77^\circ C$.
	- (c) Create a function to convert $C$ in Celsius to Fahrenheit. Test: $32^\circ F = 0^\circ C$ and $100^\circ F \approx 37.8^\circ C$.

2. **Volume of a Cone:**
    - The volume of a cone is:
      $$
      V = \frac{1}{3} \pi r^2 h
      $$
      Write a function with inputs $r$ and $h$, and output the volume. Test for $r = 4$ and $h = 6.1$.

3. **Plotting Curves:**
    - (a) Create a function to plot curves of the form:
      $$
      y = c \exp(ax)
      $$
      where $x \in [-3, 3]$ with at least 100 points. Inputs: $c$ and $a$.
    - (b) Create a script to plot curves for:
      - $c = 1, a = 0$
      - $c = 1, a = 1$
      - $c = 1, a = -1$
      - $c = -1, a = -1$
      - $c = -1, a = 1$
    - (c) Modify function: If $a$ or $c$ is complex, show error message.
    - (d) Test for $c = 2, a = 3 - 2i$, $c = \sqrt{15} - i, a = 12$, $c = \sqrt{2}, a = -\pi$.

#### 5.2 Loops
[[Loops Code Output (MATLAB)]]
1. **Summations:**
    - (a) Calculate:
      $$
      \sum_{k=1}^{50} k
      $$
    - (b) Calculate:
      $$
      \sum_{k=1}^{20} k^2
      $$

2. Find:
   $$
   \frac{3}{1} + \frac{5}{2} + \frac{7}{3} + \frac{9}{4}
   $$

3. Calculate:
   $$
   1 + x + x^2 + \ldots + x^{10} \text{ for } x = 0.4
   $$
$$
\implies\frac{a(1-r^n)}{1-r}:a=1,r=0.4\therefore\frac{1-0.4^{11}}{1-0.4}
$$

2. **Functions with Sums:**
    - (a) Function for:
      $$
      S = \sum_{k=1}^{n} k^2
      $$
      Test for $n = 1$, $n = 0$, $n = 3$.
    - (b) Function for:
      $$
      S = \sum_{k=0}^{n} x^k
      $$
      Test: $(n = 1, x = 1)$, $(n = 0, x = -1)$, $(n = 3, x = 2)$.
    - (c) Function for:
      $$
      S2 = \sum_{k=0}^{n} k^2 \text{ and } S3 = \sum_{k=0}^{n} k^3
      $$
      Test: $n = 1$ and $n = 2$.
    - (d) Function for:
      $$
      S = \sum_{\substack{k=0\\ k \neq m}}^{n} \frac{k^2}{k!}
      $$
      Test: $(n = 1, m = 1)$, $(n = 2, m = 0)$, $(n = 2, m = 1)$. Check answers by hand.

3. **Loop with Break:**
   Create a script: set $x = 2$ and compute:
   $$
   S = \sum_{k=0}^{n} x^k
   $$
   The sum should not exceed 1,000,000. Break if adding next term exceeds this limit. Test for $n = 10$ and $n = 100$.
### Reflection
 - *I did some independent work this week, too, for example learning about sprintf/fprintf which has really helped, as well as integrating the commands into my Anki workflow as flashcards so I don't forget them.*
 - *A good week for MATLAB!*
 - *I also completed my MATLAB Coursework this week, which was quite fun!*
---
## Week 5 (30/10/2023 - 05/11/2023)
### Summary
- I delved into complex mathematical calculations using nested loops, focusing on controlling the iteration criteria.
- I experimented with conditional branching by customizing a script. I manipulated case-based responses to different input variables.
- I explored conditional looping, gaining insights into loop termination conditions and avoiding infinite loops. I also applied these concepts to previous exercises for a deeper understanding.
### Exercises
#### 6.1 Nested loops
[[Nested Loops Code Output (MATLAB)]]
##### Exercise 1
**(a)** Calculate $10 \sum_{n=1}^{10} 4 \sum_{m=1}^{10} nx^m$ for $x = 0.4$ using a nested `for` loop.

**(b)** Modify the loop to exclude the terms with $n = 7$.
#### 6.2 Switch Statements
[[Switch Statements Code Output (MATLAB)]]
##### Exercise 1
1. Download the script `switch_test.m` from Blackboard, learning materials.
    - **(a)** At the beginning of the script, set a variable called `number_of_countries` to a number, signifying the number of countries in the UK.
    - **(b)** Modify the script so that the correct answer is 4 and not 5.
    - **(c)** Add another switch option, if the answer is 5: `'The answer is slightly lower'`.
    - **(d)** Add another switch option, if the answer is -1 or -2: `'The answer cannot be negative!'`. Use the construct with `{}`.
    - **(e)** Test the script for all possible pathways of execution.
##### Exercise 2
- Create a script that:
  - Sets the variable `name` to a certain value.
  - By using a `switch` statement, display appropriate messages based on the name.
	  - If it is your own name, display ’Hello, myself’.
	  - If it is one of your neighbour’s name, display: ’Hello, neighbour!’.
	  - If it is any other name, display: ’Hello, Stranger’.
	  - If it is either your surname or your neighbour surname, display: ’Hello, you should have entered your first name’. 
  - Test it for all five cases
##### Exercise 3
**(a)** Write a function that tests whether an input argument string is a certain letter. If the input string is anything other than a `'Q'`, it prints an error message.
  
**(b)** Create a function with a `switch` statement. Test whether the input argument is either 1, 3, or 5, and display the corresponding textual number. If the input is something else, show the message ’Invalid value for the input argument. Test it by calling the function from a script.
#### 6.3 While loop
[[While Loop Code Output (MATLAB)]]
##### Exercise 1
- Given the following loop: `while x < 20 action end`
  - **(a)** For what value of $x$ would the action be skipped entirely? *20*
  - **(b)** What would the action have to include to prevent an infinite loop if $x$ starts at 5? *incrementing x, such that the code would be*  `x = x + 1`  *after init. x*  `x = 5`.
##### Exercise 2
- Repeat exercise 5.2.1 but now with a `while` loop.
##### Exercise 3
- Repeat exercise 6.1.1a but now with a nested `while` loop.
##### Exercise 4
**(a)** Calculate $\sum_{k=1}^{m} k^2$ where $m$ is an integer that makes the sum just exceed 100,000. Hint: use a `while` loop.
  
**(b)** Convert the script into a function with input and output arguments.

**(c)** Modify the function so it returns $m$ that doesn't make the sum exceed a certain number (e.g., 100,000).
### Reflection
 - The session was okay, again more of the same - the Anki has definitely helped!
---
(Continue in the same format for the remaining weeks)

---
## References
- *Enter your references here...*