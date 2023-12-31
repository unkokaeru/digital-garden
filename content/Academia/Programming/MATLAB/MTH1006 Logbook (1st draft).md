# MATLAB Logbook

## Personal Details
- **Name:** William Fayers
- **Course:** MTH1006 - Computer Algebra and Technical Computing
- **Academic Year:** 2023-2024
- **Institution:** University of Lincoln, School of Mathematics and Physics

## Declaration
I confirm that this logbook is all my own work and that all references and quotations from both primary and secondary sources have been fully identified and properly acknowledged - William Fayers

---
## Week 1 (25/09/2023 - 01/10/2023)
[[Onramp certificate.pdf]]
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
[[Strings Code Output (MATLAB)]]
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
	   - Completed some modules in MATLAB Academy under MATLAB Fundamentals.
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
1. Go to [MATLAB Academy](https://MATLABacademy.mathworks.com), login using the credentials you created during week $1$, and open the course MATLAB Fundamentals. Complete:
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
## Week 6 (30/10/2023 - 05/11/2023)
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
## Week 8 (13/11/2023 - 19/11/2023)
### Summary
#### 7.1 Paths and Programs
- Focused on directory management and function creation in MATLAB.
- Practiced creating and using custom functions and scripts.
- Implemented file path manipulation and command execution.
#### 7.2 Test-riven Development
- Developed functions with specific outputs and tested their accuracy.
- Emphasized on debugging and validating functions using test scripts.
- Explored test-driven development techniques in MATLAB.
### Exercises
#### 7.1 Paths and Programs
[[Paths and Programs Code Output (MATLAB)]]
##### Exercise 1
If you do not understand a certain function or command, use the MATLAB help function for more information.
- **(a)** If the user account that you use to log into the windows computer is User, then go to the folder `C:\Users\User\Documents\MATLAB`, by clicking on the current folder, and replacing the text with `C:\Users\User\Documents\MATLAB`. If you have used a different user name, replace User by your user name.
- **(b)** From within the command window, create a folder called `session7`, using `mkdir`.
- **(c)** Go to this folder within MATLAB using the command `cd` (i.e., type `cd session7`).
- **(d)** Within this folder, create a function `my_square.m` that squares the input argument number and returns as an output argument this square.
- **(e)** Call the function from the current folder by typing in the name of the function from the command window. Make sure it is working as expected.
- **(f)** Go to the parent folder, using `cd ..`.
- **(g)** See if you can run the function from this folder. MATLAB should respond with an error message.
- **(h)** Go back to the `session7` folder, using again `cd`.
- **(i)** Add the current folder to the path, making use of the functions `addpath` and `pwd`, e.g., use `addpath(pwd)`.
- **(j)** Go to the parent folder, using the command typed in before.
- **(k)** See if you can run the function `my_square` from this parent folder (if not, something went wrong; try to fix it).
##### Exercise 2
- **(a)** If you haven’t done so already, create a folder `session7`. Then go to this folder.
- **(b)** From here, create the folders `functions` and `scripts`. Add the two folders to the path.
- **(c)** In the folder `functions`, create a function that calculates `log3(x)`, i.e., the logarithm with base 3, and returns the result. Call the function `log3`.
- **(d)** In the `scripts` folder, create a script that first sets a number to a certain value. Then test if the number is larger than zero. If so, calculate `log10(x)`, `log3(x)`, and `log2(x)` of the number, otherwise show an error message. Name the script `calc_logs`. For the `log3(x)` calculation, use your previously created function.
- **(e)** From the folder `session7` call the script `calc_logs`.
##### Exercise 3
- **(a)** Create a function `readradius` that asks the user for a radius. The function should return this radius.
- **(b)** Create a function `calcarea`, that has a radius as input argument and returns the area as output argument (see one of the previous exercises).
- **(c)** Create a function `printarea`, that has a radius and area as input and uses `disp` to display "The area of a circle of radius ... equals ....".
- **(d)** Finally, create a script that first calls `readradius`, then `calcarea` and finally `printarea`, while passing appropriate parameters for all these functions.
#### 7.2 Test-Driven Development
[[Test-Driven Development Code Output (MATLAB)]]
##### Exercise 1
Write a function `my_nexthour` that receives one integer argument, which is an hour of the day, and returns the next hour. This assumes a 12-hour clock, so for example the next hour after 12 would be 1. Here are two examples of calling this function:
```MATLAB
>> my_nexthour(3)
ans = 4
>> my_nexthour(12)
ans = 1
```
Test your function for both these values.
##### Exercise 2
Download the files `test_nexthour.m` and `nexthour.m` from Blackboard and place them in a convenient folder (which is not necessarily the Downloads folder).
- **(a)** The first `assert` test in the script file `test_nexthour.m` has an appropriate error message. Modify the two other tests, so that they also have an appropriate error message.
- **(b)** Add appropriate pass messages after each `assert`.
- **(c)** Modify the function `nexthour`, by editing the file `nexthour.m` and fixing the bugs in this file. The behaviour of the function `nexthour` should be the same as the previous exercise.
- **(d)** Add an extra line in the test script, that tests if `nexthour(4)` equals 5.
- **(e)** Add an extra line in the test script, that tests if `nexthour(12)` is smaller than 13.
- **(f)** Now run the script `test_nexthour`, and make sure all `assert` tests pass.
##### Exercise 3
- **(a)** Write a function that, given a scalar `x`, returns `x^2 + 2x + 3`. Test it with `x = 0` and `x = 1`, and check your result by hand.
- **(b)** Create a script with name `test_my_polynomial` that tests the function `my_polynomial`. Test that if this function is given the argument 0, it returns 3, and for the argument 1, it returns 6. The tests should use `assert` as in the previous exercise on `nexthour`.
- **(c)** Write a function that, given a vector `x`, returns `x^2 + 2x + 3`, element-wise. Test it with the vector `[1, 2, 3]` and check your result by hand.
- **(d)** How would you test this function with vector input in the script `test_my_polynomial`?
### Reflection
- Basically just navigating Linux and then error-handling. Overall not that exciting stuff, but definitely useful - the "assert" command is also quite interesting.
- Not too many problems, but any problems I did have I could figure out after a short while - mostly syntax.

## Week 9 (20/11/2023 - 26/11/2023)
### Summary
#### 8.1 File I/O
- Focused on file input/output operations in MATLAB.
- Learned to read from and write to files, and practiced data manipulation from file data.
- Developed skills in plotting data from files and reversing data sequences in files.
#### 8.2 Scope
- Explored the scope of variables in MATLAB, particularly in the context of user-defined functions and command prompt interactions.
- Investigated how local variables behave differently in scripts and functions.
#### 8.3 Debugging
- Practiced debugging techniques in MATLAB.
- Worked with breakpoints, conditional breakpoints, and monitored variable changes during script execution.
### Exercises
#### 8.1 File I/O
[[File IO Code Output (MATLAB)]]
##### Exercise 1
- **(a)** Create the folder `session8`, and make this the current MATLAB work directory (you could use `cd`).
- **(b)** Download both the files `time.txt` and `temp.txt` (they are in the aforementioned .zip file) and put them in this folder.
- **(c)** Create a script, where you load each file in a variable, using `load` (twice). Finally, plot the time of the day in hours vs the temperature of a human in degrees Celsius.
##### Exercise 2
- **(a)** Download the file `sample.txt` from Blackboard (this is in the aforementioned .zip file) and put it in your current MATLAB work directory.
- **(b)** Create a script named `reverse_script.m` that does the following:
    - **(i)** Set a string that signifies an input filename in the variable `inputfilename`.
    - **(ii)** Set a string that signifies an output filename in the variable `outputfilename`.
    - **(iii)** Reads the data in the input file into a vector (make use of the `load` command and the variable `inputfilename`).
    - **(iv)** Reverse the order of the vector (i.e., [1,4,6] should become [6,4,1]), using the `(end:-1:1)` indexing method on your vector variable.
    - **(v)** Writes the vector to the output file in plain text. You can use the `save` command for writing the output file with name `outputfilename`. A plain text file in MATLAB is known as ASCII encoding, and can be selected using the option `-ascii` with `save`, see help.
- **(c)** Run your script with the input file `sample.txt` and output file `reversed.txt`. Check the contents of the output file by opening it in Microsoft Word or by using `type reversed.txt` in MATLAB.
- **(d)** Run it with input file `reversed.txt` and now output file `double_reversed.txt`. Check that the original file is restored, by opening both `sample.txt` and `double_reversed.txt`.
- **(e)** Create a function named `reverse_function.m` that has two input arguments: `inputfilename` and `outputfilename` and has no output arguments. The function should do the same as the `reverse_script.m` (except now the lines with the string variables that appeared in your script are now input parameters for the function). Also test this function by calling it from the MATLAB command line, i.e., `reverse_function('sample.txt', 'sample_reversed.txt')` and check if the output file contains the expected data.
##### Exercise 3
- **(a)** Download the script `fileex.m` from Blackboard (this is in the aforementioned .zip file). Open a file with name `subjexp.txt` by typing `edit subjexp.txt` at the MATLAB prompt.
- **(b)** Modify the script `fileex.m` such that it displays the sum of the numbers from the file.
##### Exercise 4
- **(a)** Write a script that will read from a file x and y data points in the following format:
    ```
    x 0 y 1
    x 1.3 y 2.2
    ```
    The format of every line in the file is the letter 'x', a space, the x value, space the letter 'y', space, and the y value. First, create the data file with 10 lines in this format. Do this by using the editor, then save the file as `xypts.dat`. The script will attempt to open the data file and error-check to make sure it was opened. If so, it uses a for loop (since the file contains exactly 10 points) and `fgetl` to read each line as a string. In the loop, it creates x and y vectors for the data points. After the loop, it plots these points and attempts to close the file. The script should print whether or not the file was closed successfully.
##### Exercise 5
- **(a)** Modify the script from the previous problem. Assume that the data file is in exactly the same format, but do not assume that the number of lines in the data file is known a priori. Hence, instead of using a for loop, loop until the end of the file is reached using a while loop. The number of points in the file should be mentioned in the plot title.
#### 8.2 Scope
##### Exercise 1
- **(a)** If one sets a local variable within a user-defined function to a value. Can one change this value from the command prompt? *No, MATLAB uses function scoping.*
- **(b)** If one sets a local variable within the command prompt, can one change this value from within a user-defined function? *No, but it could be set as a global variable - although discouraged.*
#### 8.3 Debugging
##### Exercise 1
- **(a)** Create a new script with the following piece of code.
    ```MATLAB
    S=0;
    x=0;
    while x<5
        x=x+1
        S=S+x
    end
    ```
    It adds the numbers 1 till 5 together. 
- **(b)** Place a breakpoint at line 6, by clicking on the 6 in the editor. A red indicator will appear. Run the code, and when paused press Continue or enter `dbcont` three times. What are the values of S and x now? Is this what you expect? *The code runs as expected, with values at each breakpoint consistent with the logic of the loop.*
- **(c)** Now place a conditional breakpoint at line 6, by clicking on the 6 in the editor → right-mouse click → and enter the text `x==3`. Then run the program. What is S when the program breaks? Is this what you expected? How many times do you have to press Continue or enter `dbcont` to end the program? *The breakpoints only begin when x is equal to 3 onwards, from which the values are still consistent with the logic of the loop.*
### Reflection
- Feels like we're reaching the end of the MATLAB work, and I feel fairly confident using it to help me solve maths problems! I've been doing some Project Euler work, too, and it's been interesting using Python and then using MATLAB to do the same problem.
___
## Week 10 (27/11/2023 - 03/12/2023)
### Summary
#### 9.1 Integer and Floating Point Classes
- Explore the range of values for integer and floating-point classes in MATLAB.
- Determine suitable data types for specific applications.
#### 9.2 Matrices for Handling Multiple Numbers
- Learn to manipulate and visualise data stored in matrices.
- Analyse demographic data and temperature records using MATLAB.
### Exercises
#### 9.1 Integer and Floating Point Classes
[[Integer and Floating Point Classes Code Output (MATLAB)]]
##### Exercise 1
- **(a)** Determine the range of values for int8 by generating a positive and negative overflow. Verify results with `intmax` and `intmin`.
- **(b)** Do the same for uint8.
- **(c)** Repeat the process for int16.
- **(d)** Similarly, for uint16.
- **Question:** Which type would be suitable and most economical for storing the age of a human? *`uint8` would probably be most economical, as whilst `int8` would currently work (as the oldest age recorded is around `122`, which under under the max `127`), it'd futureproof if the max was instead `255` and the positive integers would be useful, compared to the negative.*
##### Exercise 2
- Store a number with a decimal place in a double variable, then convert it to int32 and inspect the new variable's content and size with `whos`.
##### Exercise 3
- Calculate the following using MATLAB and comment on the analytical expectations and any differences:
  - **(a)** $\cos(\frac{\pi}{2})$ 
  - **(b)** $\sqrt{2}^2 - 2$
*They both only approach zero, even though they should equal zero.*
##### Exercise 4
- **(a)** Determine the sum of $10^{-n}$ for $n=0$ to $N=20$ using a for loop and an accumulator `S`. *1.1111*
- **(b)** Modify the script to find from what value of `n` the accumulator does not change anymore. Use an extra variable `S_prev`. *n=17*
- **(c)** Change `S` to type single and observe the result. *n=9*
#### 9.2 Matrices for Handling Multiple Numbers
[[Matrices for Handling Multiple Numbers Code Output (MATLAB)]]
##### Exercise 1
- **(a)** Create the folder `session9` and set it as the current MATLAB work directory.
- **(b)** Download and store the file `yearmalefemale.txt` in this folder.
- **(c)** Create a script to:
  - Load the data into a matrix.
  - Extract the first column into `year`, the second into `male`, and the third into `female`.
  - Plot the number of males and females versus the number of years.
  - Add appropriate labels and legends.
- **(d)** Analyse the biggest difference between the male and female graphs. *More females than males above the age of ~70 years old.*
##### Exercise 2
- **(a)** Create the file `averhighs.txt` in MATLAB with specified temperature data.
- **(b)** Write a script to read these data and plot the temperatures for three locations in one graph.
- **(c)** Create a function to convert Fahrenheit to Celsius.
- **(d)** Plot the converted temperatures with appropriate labels and legend.
### Reflection
- It's interesting applying more and more of my MATLAB knowledge into the problems as they get more difficult, it's quite fun! I initially struggled to make my script for Exercise 9.2.2 code efficient, but it was a fun problem to solve.
---
## References
- *Enter your references here...*