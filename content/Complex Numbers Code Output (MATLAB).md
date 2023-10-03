```MATLAB
>> % Question 1
>> q1a = (1+i)*(1-i)

q1a =

     2

>> q1b = abs(2+4*i)

q1b =

    4.4721

>> q1c = i^i

q1c =

    0.2079

>> q1d = sqrt(i)

q1d =

   0.7071 + 0.7071i

>> q1e = (3+4i)(5-6i)^(7+(8i*cos(9+10i))/11)
 q1e = (3+4i)(5-6i)^(7+(8i*cos(9+10i))/11)
             ↑
Invalid expression. When calling a function or indexing a variable, use parentheses.
Otherwise, check for mismatched delimiters.
 
>> q1e = (3+4i)*(5-6i)^(7+(8i*cos(9+10i))/11)

q1e =

 -8.5380e+176 -4.2955e+176i

>> % Question 2
>> x = imag(tan(i))

x =

    0.7616

>> % Question 3
>> x2 = real(sqrt(i))

x2 =

    0.7071

>> % Question 4
>> z = 1/i; q4 = arg(z)
Unrecognized function or variable 'arg'.
 
>> z = 1/i; q4 = angle(z)

q4 =

   -1.5708

>> 
```