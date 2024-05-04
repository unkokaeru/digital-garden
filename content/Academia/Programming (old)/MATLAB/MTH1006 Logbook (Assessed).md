# MATLAB Logbook

## Personal Details

- **Name:** William Fayers
- **Course:** MTH1006 - Computer Algebra and Technical Computing
- **Academic Year:** 2023-2024
- **Institution:** University of Lincoln, School of Mathematics and Physics

## Declaration

I confirm that this logbook is all my own work and that all references and quotations from both primary and secondary sources have been fully identified and properly acknowledged - William Fayers

## Table of Contents

1. **Personal Details**
	- Name, Course, Academic Year, Institution
2. **Declaration**
	- Originality statement
3. **Weekly Work Log**
	- **[Week 1 (2023.09.25 - 2023.10.01)](###Week%201%20(2023.09.25%20-%202023.10.01))**: Introduction to MATLAB and Setup.
	- **[Week 2 (2023.10.02 - 2023.10.08)](###Week%202%20(2023.10.02%20-%202023.10.08))**: Basic Calculations and Data Types.
	- **[Week 3 (2023.10.09 - 2023.10.15)](###Week%203%20(2023.10.09%20-%202023.10.15))**: Data Visualization and Basic Operations.
	- **[Week 4 (2023.10.16 - 2023.10.22)](###Week%204%20(2023.10.16%20-%202023.10.22))**: Programming Foundations for MATLAB.
	- **[Week 5 (2023.10.23 - 2023.10.29)](###Week%205%20(2023.10.23%20-%202023.10.29))**: Advanced Scripting and Looping Constructs.
	- **[Week 6 (2023.10.30 - 2023.11.05)](###Week%206%20(2023.10.30%20-%202023.11.05))**: Complex Control Structures.
	- **[Week 7 (2023.11.06 - 2023.11.12)](###Week%207%20(2023.11.06%20-%202023.11.12))**: Enhanced MATLAB Skills through Self-Study.
	- **[Week 8 (2023.11.13 - 2023.11.19)](###Week%208%20(2023.11.13%20-%202023.11.19))**: Program Management and Testing.
	- **[Week 9 (2023.11.20 - 2023.11.26)](###Week%209%20(2023.11.20%20-%202023.11.26))**: File Handling and Debugging in MATLAB.
	- **[Week 10 (2023.11.27 - 2023.12.03)](###Week%2010%20(2023.11.27%20-%202023.12.03))**: Advanced Data Types and Matrix Operations.
	- *The Logbook continues into week 13, but has been shortened to ten weeks due to deadline constraints.*
4. **Weekly Reflections, Tabulated**
	- Summarised reflections on each week
5. **References**
	- List of all referenced materials and resources

## Weekly Work Log

[[MTH1006 Logbook (Questions).pdf]]

*Linked directly above is a document containing all of the questions I completed from the weeks, this was just useful whilst completing the work, and for reference to which questions I was completing - my goal for this log was to have everything in the same place, just in case I needed it.*

Note that my log is structured by the week date, followed by a summary of what I did in the week, then followed by some key highlights from the exercises (categorised by subheadings followed by the full code output from exercises, found in a hyperlink), then concluded with a reflection/summary of what self-study I did during the week.

The logbook is structured like this to give me the best possible use of it for revision, rather than filling it with repetition and code output - however, this raw full code output is still included, in case I ever require additional examples, etc. But, this is only accessible via a hyperlink to increase the readability of the logbook.

Practically, these can be printed physically separately and organised to give a similar logging environment for revision and browsing.

### Week 1 (2023.09.25 - 2023.10.01)
**Introduction to MATLAB and Setup**: Getting started with MATLAB Onramp Course and installing the MATLAB software for computational tasks.

#### Exercises

##### 1.1 MATLAB Onramp Course

Completed the exercises within the course, then achieved this [[Onramp certificate.pdf]].

##### 1.2 MATLAB Installation

Installed MATLAB and ensured it worked as intended, then helped some other students do the same.

#### Reflection

MATLAB seems very simple at the minute, but towards the end of the Onramp course I began to understand how it could be very useful for certain problems. I'm quite interested in using it in the future!

### Week 2 (2023.10.02 - 2023.10.08)
**Basic Calculations and Data Types in MATLAB**: Exploring MATLAB as a calculator, understanding variables, scripts, vectors, intrinsic functions, and complex numbers.

#### Exercises

##### 2.1 Calculator
[[Calculator Code Output (MATLAB)]]

In these exercises, I determined the values of several functions using the MATLAB terminal and commands like `exp(x)` for $e^x$ and `sqrt(x)` for $\sqrt{x}$, as well as more intuitive commands such as `sin(x)` for $\sin(x)$. One interesting point during these exercises was the differentiation between `log(x)` and `log10(x)`; normally, $\log(x)$ represents $\log_{10}(x)$ rather than $\ln(x)$, but I suppose it makes sense since the programming language is predominantly used by mathematicians.

I also used the `help` command for the first time here, and begun to understand that answers aren't exact, but approximations (usually to four decimal places).

The most complicated question was probably:

```MATLAB
>> q1i = exp(2*sqrt(3*sin(4+log10(5))+6)-7)+8

q1i =

    8.0291
```

##### 2.2 Variables
[[Variables Code Output (MATLAB)]]

These exercises introduced the idea of variables, much like variables in other programming languages. However, interestingly, MATLAB allows the user to see the values both printed to the terminal (as expected), as well as in a separate window. 

There wasn't much more to this section, just playing around with variables, such as:

```MATLAB
>> a = 7/3; b = 9/6; c = a*b

c =

    3.5000
```

##### 2.3 Variable names
[[Variable Names Code Output (MATLAB)]]

This section of exercises was particularly useful, as it introduced what variables names are valid in MATLAB. These were mostly intuitive, such as `x x` and `if` being invalid, but `tan` being valid surprised me.

```MATLAB
>> tan=1

tan =

     1
```

The full list of tested variables names is below:

| Variable Name           | Validity |
| ----------------------- | -------- |
| `x`                     | ✅       |
| `x2`                    | ✅       |
| `2x`                    | ❎       |
| `xy`                    | ✅       |
| `x x`                   | ❎       |
| `exc3.1`                | ❎       |
| `tan`                   | ✅       |
| `end`                   | ❎       |
| `a long variable name`  | ❎       |
| `a_long_variable_name2` | ✅       |
| `x$`                    | ❎       |
| `x%`                    | ❎       |
| `a_`                    | ✅       |
| `_a`                    | ❎         |

##### 2.4 Scripts
[[Scripts Code Output (MATLAB)]]

We then delved into the idea of scripts, taking the basic commands we've learned thus far and combining them into something resembling an actual MATLAB program. My first script calculated the y-value of a specified quadratic equation at a given x-value:

```MATLAB
a=1;
b=2;
c=3;
x=4;

y=a*x^2+b*x+c
```

In the case of $x^2+2x+3$ at $x=4$, it gave a y-value of $y=27$. However at this point, I was wondering about making my own functions - that would make this "program" a lot more useful.

##### 2.5 Vectors and intrinsic functions
[[Vectors Code Output (MATLAB)]]

Here, we started looking at creating vectors - this in particular was quite novel to me, as I haven't used an operator like `:` before whilst programming. Here's an example from 2.5.2:

```MATLAB
>> q2a = 100:2:110 % Creates a vector from 100 to 110 in steps of 2

q2a =

   100   102   104   106   108   110
```

Similarly, 2.5.3 demonstrated the command `linspace`, which creates a certain number of linearly spaced elements within a set vector:

```MATLAB
>> q3 = linspace(11,20,50)

q3 =

  Columns 1 through 8

   11.0000   11.1837   11.3673   11.5510   11.7347   11.9184   12.1020   12.2857

...

  Columns 49 through 50

   19.8163   20.0000
```

This also first demonstrated to me how MATLAB handles larger vectors, opting to print them in sections. The most impactful learning point of these exercises to me, however, was the idea that we could easily create these vectors, then perform a single function on them to transform the entire vector. For example, taking the previous vector and then performing `sin(x)` to calculate 50 sine values at once.

##### 2.6 Complex numbers
[[Complex Numbers Code Output (MATLAB)]]

During our calculus lectures, we began to study complex numbers - around the same time as using them during our MATLAB lectures. This was quite interesting, as (whilst I've already studied complex numbers extensively previously) it gave instant insight into how we can apply the mathematics we were learning. As with the other exercises, it was quite simple to complete, yet very interesting as to how we can further exploit MATLAB's functionality.

However, I did first struggle to remember to explicitly multiply multiples of pi, for example, writing $4\pi$ as `4pi` opposed to `4*pi`. As well as this, the naming of functions was initially confusing, as during lectures and writing Latex code, the angle of a complex number was usually given as the **argument**, or $\arg(z)$. In MATLAB however, it's simple denoted the **angle** - which makes much more sense. This first confused me in 2.6.4:

```MATLAB
>> z = 1/i; q4 = arg(z)
Unrecognized function or variable 'arg'.
 
>> z = 1/i; q4 = angle(z)

q4 =

   -1.5708
```

#### Self-Study

During this week, I intended to develop some Anki flashcards to help me learn the various commands, but I ended up having no time. On top of this, I spent most of my self-study during week 2 re-writing notes due to accidentally deleting them - which was quite a set-back.

### Week 3 (2023.10.09 - 2023.10.15)
**Data Visualization and Basic Operations**: Introduction to plotting in MATLAB, handling vector indexing, operations, string manipulations, and Boolean algebra.

#### Exercises

##### 3.1 Plotting
[[Plotting Code Output (MATLAB)]]

Beginning week three, we reviewed plotting functions, but increasing the complexity and detail of the graphs. For example, we used the vectors from week two to create a range for $x : [-2\pi,2\pi]$ in steps of $\frac{\pi}{50}$ (this was later further enforced with the `axis` command):

```MATLAB
% Define the range for x
x = -2*pi:pi/50:2*pi;
```

Then we calculated the corresponding y-values with `y1 = sin(x)` and `y2 = cos(x)`, and created a figure with `figure`. The next new part of MATLAB graphs came with plotting with unique styles, adding axes labels, a title, and a legend.

```MATLAB
plot(x, y1, 'b-', x, y2, 'r--');
title('Plot of trigonometric functions');
xlabel('x');
ylabel('y');
legend('sin(x)', 'cos(x)');
```

To finalise the graph, we enforced the view range and enabled a grid with `grid on` to produce the following:

![[Q3.1.1.png]]

We practiced this two more times, plotting both some quadratic curves and and exponential function $y = e^{-x^2}$. During these exercises, I decided to try and experiment a bit with MATLAB, using an array to store my colour for easier code readability - shown in this code snippet:

```MATLAB
colors = ['b', 'r', 'g', 'm']; % Different colors for each graph
index = 1; % Init. index for color selection

plot(x, y + c, [colors(index) '-']); % Plot the graph with corresponding color
index = index + 1; % Update the color index
```

For the third exercise, I then tried to use `linspace` instead of the colon operator `:` to generate the x-values:

```MATLAB
% Set the range for x
x = linspace(-0.5,1.5,100);
```

##### 3.2 Vector indexing – one element
[[Vector Indexing - One Element Code Output (MATLAB)]]

This section introduces indexing, for example if you have a vector `v = linspace(2,4,5)`, then you could take the sum of the first and last elements with the code:

```MATLAB
sum = v(1) + v(5);
```

##### 3.3 Vector operations
[[Vector Operations Code Output (MATLAB)]]

Next, we looked at calculating mathematical series by using vectors. This began quite simple, just summing integers between $1\to50$ and then more complicated sums, such as:

$$
\frac{2}{1} + \frac{4}{2} + \frac{8}{3} + \frac{16}{4} + \frac{32}{5} + \frac{64}{6} + \frac{128}{7} + \frac{256}{8}
$$

Calculating the answers the following MATLAB code:

```MATLAB
sum((2.^(1:1:8))./1:1:8) % 3.3.2b
```

Then, we learned a few other new functions involving vectors, like finding the maximum value in a vector with `max(v)`, the mean with `mean(v)`, and the idea that you can perform trigonometric functions on vectors, like `cos(v)`.

##### 3.4 Strings
[[Strings Code Output (MATLAB)]]

Here, we discovered the first steps to more complex terminal output: combining strings with variables:

```MATLAB
s = 'this is a string'

s1 = 'this is '

s2 = 'a string'

stot = [s1,s2]

stot(1)='T'

stot = [stot,'!']
```

This creates various strings, by manipulating the original string `s`, splitting it into `s1` and `s2`, then by combining them again into `stot` by placing them both into an array `[s1,s2]`, and finally by using the indexing similar to the previous section 3.3 to replace the first character.

This works because MATLAB stores strings like a vector, thus the same vector indexing applies.

##### 3.5 Boolean algebra
[[Boolean Algebra Code Output (MATLAB)]]

Boolean algebra refers to algebra that works with "True" and "False". First, we determined which of these some expression evaluate to, for example `1 > 0` evaluated to `1`, and `and(true,or(true,false))` evaluated to `1`.

Next, we moved onto storing Boolean values within variables, then doing the same process, then further adding complexity with string comparisons:

```MATLAB
% Question 3

s = 'hi';

a2 = strcmp(s,'Hii');
b2 = strcmp(s,'hi');
c2 = strcmp(s,'Hi');
d2 = strcmp(s,'hi ');

q3 = [a2,b2,c2,d2] % Question 3 output: 0  1  0  0
```

#### Self-Study

This week, I finally made my Anki flashcards which helped greatly with remembering commands, but beyond this I didn't do much self-study. I have however loaned a book on MATLAB from the library that I plan to study from during the following weeks.

### Week 4 (2023.10.16 - 2023.10.22)
**Programming Foundations in MATLAB**: Focusing on output formatting, conditional branching, and creating user-defined functions.

#### Exercises

##### 4.1 Output
[[Output Code Output (MATLAB)]]

In this section we learned how to output text to the console, which I found very useful for user interaction. You do this with the `disp` command ("display", shortened), with a single string argument, or even a combination like so:

```MATLAB
T = 42;

disp(['The temperature is ',num2str(T)])
```

##### 4.2 Conditional branching
[[Conditional Branching Code Output (MATLAB)]]

To continue on this week's trend of learned new powerful MATLAB functions, we introduced `if` and `elseif` statements. Very intuitive, they test **if** something is true, and then continue if so. **Else**, they'll do another thing, **if** yet another thing is true - these can also be changed for more complex conditional branching.

This is first tested with the following script, designed to just compare two daily temperatures:

```MATLAB
Saturday = 16;
Sunday = 17;

if Saturday < Sunday
	disp('Saturday is colder')
elseif Sunday < Saturday
	disp('Sunday is colder')
elseif Saturday == Sunday
	disp('Both days have the same temperature')
end
```

Clearly, this will be very helpful, however, it would be much more useful if we could get user input to compare - if only there were functions.

##### 4.3 Functions
[[Functions Code Output (MATLAB)]]

But, functions is exactly what we learned next! We began by completing the parts of MATLAB Fundamentals on functions: 15.1, 15.2, 15.3. Then, we created a simple function to calculate the area of a circle, and experimented a bit with it.

```MATLAB
function area=area_circle(d)
	% Calculates the area of a circle given the diameter
	area=pi*(d/2).^2;
end
```

This is particularly exciting, as it means we can create more MATLAB functions that even interact with the `help` command by making our own comments, to give output:

```MATLAB
>> help area_circle
  Calculates the area of a circle given the diameter
```

#### Self-Study

This week I unfortunately did not have much time to do some self-study, but I at least kept on top of my in-lesson work and my flashcards. Next week is definitely going to be the beginning of my textbook self-study, though!

### Week 5 (2023.10.23 - 2023.10.29)
**Advanced Scripting and Looping Constructs**: Delving deeper into functions and scripts with an emphasis on implementing loops in MATLAB.

#### Exercises

##### 5.1 Functions and scripts
[[Functions and Scripts Code Output (MATLAB)]]

To begin this week, we continued our previous week's work on functions, as well as scripts in general, to create more MATLAB functions to calculate simple common calculations, such as temperature conversions and the volume of a cone, both shown below:

```MATLAB
function fahrenheit = temp_conv_c2f(celsius)
	% Converts from Celsius to Fahrenheit
	
	fahrenheit = 1.8*celsius+32;
	disp(['The temperature is ',num2str(celsius),' degrees Celsius, which corresponds to ',num2str(fahrenheit),' degrees Fahrenheit.'])
end
```

```MATLAB
function volume = vol_cone(radius,height)
	% Calculates the volume of a cone based on a given radius and height
	
	volume = (pi*height*radius^2)/3;
end
```

Then, we extended this to being able to plot graphs of a certain with a function. In 5.1.3, this form was $y=c\exp(ax)$. This was quite simple, and the most complex part of the solution was ensuring all points were real with the `if imag(c) == 0 && imag(a) == 0` conditional statement. The more exciting and challenging part was using this function in a script to plot multiple curves, as I decided to try and auto-generate the legend with the following:

```MATLAB
labels = cell(1,length(cn));
for count = 1:1:length(cn)
	plot_exp(cn(count),an(count))
	hold on
	labels{count} = sprintf('c=%d, a=%d', cn(count), an(count));
end
```

This resulted in a very satisfying graph as a result:
![[exp_graphs.jpg]]

##### 5.2 Loops
[[Loops Code Output (MATLAB)]]

Loops! A wonderful programming construct that, similar to functions, helps to improve code readability and re-use. In this section, we used some simple loops to calculate some sums - as well as checking them by hand. For example, finding the sum of all squares and cubes from $0\to n$ was calculated in 5.2.2c with the following function:

```MATLAB
function [S2,S3] = sum_squares_and_cubes_0toN(n)
	% Finds the sum of the squares and cubes from 0 to n
	
	S2 = sum((0:n).^2);
	fprintf("The sum of the squares from 0 to %d is %d.\n",n,S2)
	
	S3 = sum((0:n).^3);
	fprintf("The sum of the cubes from 0 to %d is %d.\n",n,S3)
end
```

The `sum` function here contains the loop, which could look like this (where `mySum` is a recreation of what the in-built `sum` function could look like):

```MATLAB
function sum = mySum(numbers)
    % This function takes an array of numbers and returns their sum.
    % :numbers: a vector or array of numbers
    % :sum: sum of the numbers

    sum = 0;  % Initialize the total to zero
    for i = 1:length(numbers)
        sum = sum + numbers(i);
    end
end
```

#### Self-Study

This week, as planned, I did some self-study! I learned about `sprintf` and `fprintf` which really helped me further some of my scripts, as I found it easier to print variables alongside strings with these commands. Of course, I also added these into my Anki workflow so I don't forget them. I also completed my MATLAB coursework this week, which was quite fun - so, overall, a good week!

### Week 6 (2023.10.30 - 2023.11.05)
**Complex Control Structures**: Exploring nested loops, switch statements, and while loops for advanced programming control.

#### Exercises

##### 6.1 Nested loops
[[Nested Loops Code Output (MATLAB)]]

To begin this week, we extended our concept of loops to nesting them inside of one another to calculate more complex sums, which included just one example:

```MATLAB
% A short script to calculate a nested sum
sum = 0;
x = 0.4;

for n = 1:10
	for m = 1:4
		sum = sum + n*x^m
	end
end

fprintf("The sum is %f\n",sum);
```

##### 6.2 Switch
[[Switch Statements Code Output (MATLAB)]]

Next, we introduced "switch statements": a completely new concept to me, having previously exclusively programmed in Python, and even then at a fairly elementary level. This was quite intriguing, and I managed to create a few scripts utilising the new function. However, its practical use thus far seemed to be limited to error handling and gimmick-like use, but I'm excited to see how we can further use it!

For example, a greeting script - one of the more gimmick-like uses, but useful  as a proof of concept nevertheless:

```MATLAB
% A short script to greet someone based on their name
name = "siughdsiug";

switch name
	case "Student"
		greeting = "Hello, myself";
	case "Neighbour"
		greeting = "Hello, neighbour!";
	case {"StudentSurname","NeighbourSurname"}
		greeting = "Hello, you should have entered your first name.";
	otherwise
		greeting = "Hello, stranger!";
end

disp(greeting);
```

##### 6.3 While loop
[[While Loop Code Output (MATLAB)]]

Finally, to conclude week 6, we investigated `while` loops, opposed to restricting ourselves to `for` loops. This consisted of mainly similar exercises to those with `for` loops, but this time extending the usefulness of the function in niche use cases. For example, in 6.3.4, it was essential to use a `while` loop rather than a `for` loop to calculate $\sum_{k=1}^{m} k^2$ where $m$ is an integer that makes the sum just exceed 100,000.

```MATLAB
function termsNeeded = sum_squares_b(targetSum)
	% Calculates terms needed to sum squares to just before a given value
	termsNeeded = 1;
	sum = 0;
	
	while sum < targetSum
		termsNeeded = termsNeeded + 1;
		sum = sum + termsNeeded^2;
	end
end
```

#### Self-Study

I watched some YouTube videos on various MATLAB programming ideas, just to head everything from a different perspective. This helped quite a lot also, again, alongside by textbook study and flashcards.

### Week 7 (2023.11.06 - 2023.11.12)
**Enhanced MATLAB Skills through Self-Study**: Focused on advanced numerical calculations, complex plotting, and exploring differential equations and matrix operations through self-guided study.

This week was during our reading week, or reduced lecture week, so I had a lot of time to catch up and consolidate, as well as extend my existing knowledge - as summarised above.

### Week 8 (2023.11.13 - 2023.11.19)
**Program Management and Testing**: Learning about managing paths and programs in MATLAB and the fundamentals of test-driven development.

#### Exercises

##### 7.1 Paths and programs
[[Paths and Programs Code Output (MATLAB)]]

This week was a bit different from the others, as other than exploring programming constructs we began by exploring Linux-style file navigation. There isn't much to note from the session, just the following commands.

| Command        | Use                                                 |
| -------------- | --------------------------------------------------- |
| `cd`           | Change directory                                    |
| `mkdir`        | Make directory                                      |
| `addpath(pwd)` | Add the current print working directory to the path | 

This helped me organise my MATLAB environment (directory structure) and so I added previous scripts etc. into respective directories.

##### 7.2 Test-driven development
[[Test-Driven Development Code Output (MATLAB)]]

Continuing the week in a slightly different style to the other weeks, we developed tests for some scripts. This was done predominately with the `assert` command which quickly creates tests.

The main template used to do this is shown in the following example:

```MATLAB
% Test 3

msg_error3=['The function polyno_calc does not work. the polyno_calc of [1, 2, 3] should be [6, 11, 18]. Instead, ', num2str(polyno_calc([1, 2, 3])), ' was returned.'];

assert(sum(polyno_calc([1, 2, 3])==[6, 11, 18])==3);

disp('Test 3 passed')
```

#### Self-Study

This week was quite busy for me, so I only had time to study my flashcards, which I could luckily do during lesson time as I could complete the given work in fairly minimal time.

### Week 9 (2023.11.20 - 2023.11.26)
**File Handling and Debugging in MATLAB**: Understanding file input/output operations, variable scope, and debugging techniques.

#### Exercises

##### 8.1 File I/O
[[File IO Code Output (MATLAB)]]

Here, we investigated opening files and using the data within them - obviously a very useful thing to know. We did this using `load`, then saving it to a variable. For example, if we're handling a large amount of data (such as the temperature of a human body over a day), we can import the data from the file with `temp = load("temp.txt");`, then graph it:

```MATLAB
plot(1:24, temp);
xlabel("Time of day (hours)");
ylabel("Temperature of the human body (Celsius)");
title("Temperature of a human body over the day");
```

Which results in...

![[body_temp_graph.jpg]]

Alternatively, we can modify data within a file. In the exercises, we created a function to reverse all of the numbers in a file:

```MATLAB
function reverse_function(inputfilename, outputfilename)
	% Reverses an array in a given file into a given output file
	original_text = load(inputfilename);
	reversed_text = original_text(end:-1:1);
	
	save(outputfilename, 'reversed_text', '-ascii')
end
```

If we want to take it one step further, then we can generalise the first function we made into a MATLAB script to plot any data, as long as we have a data file of all of the x and y co-ordinates. We can also utilise functions like `fopen` to make this slightly more efficient (opening something only in read mode, for example).

Breaking the script into a few parts, first we initialise everything: the x,y-values, opening the file, and the point count...

```MATLAB
% Initialize vectors for x and y values
x_values = [];
y_values = [];

% Open the file
fileID = fopen('xypts.dat', 'r');

% Check if the file was opened successfully
if fileID == -1
	error('File could not be opened');
else
	% Initialize the counter for the number of points
	point_count = 0;
	...
```

Continuing this `else` statement, we can read the file line by line until we run out of data, then extract the x,y-values from each line:

```MATLAB
	% Read the file line by line until the end of the file is reached
	while ~feof(fileID)
		line = fgetl(fileID);
		if ~ischar(line)
			break; % Exit loop if an invalid line is encountered
		end
		
		% Extract x and y values from the line
		values = sscanf(line, 'x %f y %f');
		
		x_values(end+1) = values(1);
		y_values(end+1) = values(2);
		
		point_count = point_count + 1;
	end
	...
```

Then finally we conclude the file by plotting the points and close the file:

```MATLAB
	% Plot the points
	plot(x_values, y_values, 'o-');
	xlabel('x values');
	ylabel('y values');
	title(['Plot of ' num2str(point_count) ' x and y values from file']);
	
	% Attempt to close the file
	fclose_status = fclose(fileID);
	if fclose_status == 0
		disp('File closed successfully.');
	else
		disp('File could not be closed.');
	end
end
```

An example plot of an arbitrary data set would be the following...

![[xy_plot_2.jpg]]

##### 8.2 Scope

This section was more to just test our understanding of MATLAB:

- MATLAB uses function scoping, so variables made within a function cannot be interacted with in the command prompt.
- Vice versa, a variable made in the command prompt cannot be interacted with within a function - unless it's a global variable, which is against best practice and heavily discouraged.

##### 8.3 Debugging

Similar to the previous section, there wasn't a lot of code in this part - more so testing our use of MATLAB. Specifically, how to debug our code using breakpoints (conditional and otherwise).

Breakpoints work as expected, creating a **point** in the code where the runtime **breaks**, or pauses - conditional breakpoints just do this given a condition.

#### Self-Study

This week I was introduced to Project Euler, which was very fun. I've done about twenty questions from it so far, just because of how exciting it is! This has also somewhat distracted me from my weekly textbook self-study, but I've kept on top of the flashcards - although because of the spaced repetition algorithm there aren't many to do this week. It's been super fun doing Project Euler questions, though - I've been attempting them in both Python and MATLAB, which has been an interesting challenge, since Python is what I'm more used to. (and is probably more what Project Euler is aiming for).

### Week 10 (2023.11.27 - 2023.12.03)
**Advanced Data Types and Matrix Operations**: Exploring integer and floating-point classes and the use of matrices for handling multiple numbers in MATLAB.

#### Exercises

##### 9.1 Integer and floating point classes
[[Integer and Floating Point Classes Code Output (MATLAB)]]

Here we began to do delve further into the inner workings of MATLAB - specifically, its data types. Predominately, this consisted of a single test function to test the workings of a given data type:

```MATLAB
function testDataType(dataType)
	% Tests the data type given and returns its max/min values.
	% :dataType: a data type (string)
	% :return: None
	
	% Display the data type being tested
	disp(['Testing ', dataType]);
	
	% Find minimum and maximum values for the data type
	minValue = intmin(dataType);
	maxValue = intmax(dataType);
	
	% Display min and max values
	disp(['Min Value: ', num2str(minValue)]);
	disp(['Max Value: ', num2str(maxValue)]);
	
	% Test for overflow
	overflowValue = cast(maxValue + 1, dataType);
	underflowValue = cast(minValue - 1, dataType);
	
	% Display overflow/underflow results
	disp(['Overflow Test: ', num2str(overflowValue)]);
	disp(['Underflow Test: ', num2str(underflowValue)]);
	
	% Compare against system values
	if overflowValue > maxValue
		disp('Overflow exceeds system max value.');
	else
		disp('Overflow does not exceed system max value.');
	end
	if underflowValue < minValue
		disp('Underflow is less than system min value.');
	else
		disp('Underflow does not go below system min value.');
	end
end
```

For example, when testing `int8` the function returns:

```MATLAB
Testing int8
Min Value: -128
Max Value: 127
Overflow Test: 127
Underflow Test: -128
Overflow does not exceed system max value.
Underflow does not go below system min value.
```

Showing that `int8` can only contain a value between -128 and 127. We also tested `uint8`, `int16`, and `uint16`, which I did with the following code snippet...

```MATLAB
>> dataTypes = {'int8', 'uint8', 'int16', 'uint16'}; for i = 1:length(dataTypes) testDataType(dataTypes{i}); end
```

After this, we learned the new command `whos`, which returns the name, size, bytes, class, and attributes of a given variable, for example,

```MATLAB
>> whos("var_int32");
  Name           Size            Bytes  Class    Attributes

  var_int32      1x1                 4  int32      
```

These data types can have varied effects, for example, approximating certain values to numbers approaching their true value, but never reaching it. This is clearly the case when evaluated an expression like $\sqrt{2}^2 - 2$, which is clearly $0$, but returns a value of $4.4409\times10^{-16}$: a number very close to the true value, but not quite.

##### 9.2 Matrices for handling multiple numbers
[[Matrices for Handling Multiple Numbers Code Output (MATLAB)]]

Finally, to conclude week 10, we combined all of our knowledge thus far into some more complex graphs, such as the average high temperatures for multiple locations, as well as the population by gender and age in the UK (2014).

![[graph.png]]

![[graphTempC.png]]

The scripts for these graphs are fairly extensive, so shall mostly remain in the code output linked, especially since a lot of the code is repetition of previous tasks, however we do use one new command: `readmatrix`. This can store matrix data from a text file, which we can then use to extract specific columns of data from. For example, in the first example:

```MATLAB
% Load the data into a matrix
data = readmatrix('yearmalefemale.txt');

% Extract the columns
year = data(:, 1); % First column
male = data(:, 2); % Second column
female = data(:, 3); % Third column
```

#### Self-Study

I've been busy with mid-terms, so haven't done much extra MATLAB - not even the flashcards this week. This said, I don't think I've necessarily needed it this week, since everything has been fairly simple and I'm grasping it pretty quickly. During the lesson I watched a video on the week's content for some further explanation, but that's it.


## Weekly Reflections, Tabulated

Below are some detailed reflections on each week. They contain references to the module learning objectives, achievements, as well as any difficulties faced in the week. Some of this in repeated in the above log, but I found it was more useful to have the reflections separate as well for easier navigation.

| Week | Module LOs    | Syllabus                                                                                                                                          | Achievements                                                                                                  | Difficulties                                                                 |
| ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 1    | LO1, LO2      | Onramp course, MATLAB installation                                                                                                                | Completed the Onramp course.                                                                                  | Initially very simple, so struggled to engage as I wasn't challenged enough. |
| 2    | LO1, LO2, LO3 | Numerical calculations, variables, script files, built in functions and constants, basic algebraic operations, naming and evaluating expressions. | Understood how MATLAB can complete calculations and understood various commands.                              | Differentiating `log(x)` and `log10(x)`.                                     |
| 3    | LO1, LO2      | Plotting graphs (cartesian), graphical display of data, 1D and 2D arrays and how to address and modify the elements in these arrays, strings      | Learned how to plot graphs, index vectors and skills with Boolean algebra.                                    | Remembering how to index vectors: using () not [].                           |
| 4    | LO1, LO2, LO3 | Data input & output, control structures of a procedural language including if and if-else statements, defining and evaluating functions           | Figured out how to display to the terminal in different ways, as well as conditional branching and functions. | No notable difficulties this week.                                           |
| 5    | LO1, LO2      | Creating functions, designing solutions of coding problems, control structures of a procedural language including for-loops                       | Further developed my scripts and loops.                                                                       | Balancing self-study with coursework.                                        |
| 6    | LO2           | Control structures of a procedural language including while-loops, nested-if and switch statements                                                | Developed nested loops, among other statements.                                                               | Familiarising with the novel idea of switch statements.                      |
| 7    | LO1, LO2      | Paths and programs, test-driven development, programming language syntax.                                                                         | Completed some self-study.                                                                                    | Finding tasks to complete by myself.                                         |
| 8    | LO3           | Files, scope, writing and debugging computer programs.                                                                                            | Understood how paths work in MATLAB.                                                                          | Adapting to the new style of the tasks: navigation rather than coding.       |
| 9    | LO2, LO3      | Data types including integers, floating point numbers, and matrices handling multiple numbers                                                     | Used files to further my scripting and functions, as well as understood debugging techniques.                 | Learning about variable scope.                                               |
| 10   | LO1, LO2      | Advanced data types, matrix operations, technical computing aspects in MATLAB.                                                                    | Recognised the inner workings of MATLAB's data types a bit more.                                              | Balancing this module with my other module mid-terms.                        | 

## References

1. MATLAB documentation, Version R2023b, The MathWorks, Inc., 2023. [Online]. Available: within MATLAB software using the `help` function.
2. S. Attaway, *MATLAB: A Practical Introduction to Programming and Problem Solving*, 3rd ed., Amsterdam: Elsevier, 2013.
3. D. Hanselman and B. Littlefield, *Mastering MATLAB*, Pearson Education, 2011.
4. R. Pratap, *Getting Started with MATLAB: A Quick Introduction for Scientists and Engineers*, Oxford University Press, 2009.