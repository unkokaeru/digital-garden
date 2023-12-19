```MATLAB
>> % Exercise 7.1.1
>> mkdir session7
>> cd session7
>> my_square(3)

ans =

     9

>> cd ..
>> cd session7
>> addpath(pwd)
>> cd ..
>> my_square(3)

ans =

     9

>> % Exercise 7.1.2
>> cd session7
>> mkdir functions
>> mkdir scripts
>> addpath(pwd)
>> cd scripts
>> addpath(pwd)
>> cd ..
>> cd functions
>> log3(3)

result =

     1


ans =

     1

>> log3(3)

ans =

     1

>> cd ..
>> cd scripts
>> cd ..
>> calc_logs
Log base 10: 1.00
Log base 3: 2.10
Log base 2: 3.32
>> 
```

```my_square.m
function squareNum = my_square(num)

% Squares the input arg

% :num: A matrix of real numbers

% :squareNum: A matrix of the square of each element in the input matrix

squareNum = num.^2;

end
```

```log3.m
function result = log3(num)

% Calculates log base 3 of the input arg

% :num: any real number

% :result: log base 3 of num

result = log(num)/log(3);

end
```

```calc_logs.m
% A simple script to find the log of a number in base 10,3,2

num = 10;

if num > 0

fprintf("Log base 10: %.2f\nLog base 3: %.2f\nLog base 2: %.2f\n",log10(num),log3(num),log2(num));

else

error("Error: Number is less than or equal to 0")

end
```

```readradius.m
function radius = readradius()

% Returns the user input

% :radius: any real number

radius = input("What is the radius? ");

end
```

```calcarea.m
function area = calcarea(radius)

% Calculates the area of a circle based on its radius

% :radius: a matrix of real numbers

% :area: the area of every circle in the matrix (to two decimal places)

area = pi .* radius.^2;

end
```

```printarea.m
function printarea(radius,area)

% Prints the area of a circle based on its radius

% :radius: any real number

% :area: the area of the circle

fprintf("The area of a circle of radius %.2f equals %.2f\n",radius,area);

end
```

```calc_circle_area.m
% A simple script to calculate and return the area of a circle based on the

% user inputted radius

radius = readradius();

area = calcarea(radius);

printarea(radius, area);
```