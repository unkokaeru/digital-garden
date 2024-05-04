```MATLAB-Script
% Question 1

a1 = 1 > 0;

b1 = 3 >= 4;

c1 = or(3 > 4, 3 < 4);

d1 = 8 ~= 9;

e1 = 3 == 3 + 1;

f1 = not(false);

g1 = and(true,or(true,false));

q1 = [a1,b1,c1,d1,e1,f1,g1] % Question 1 output

% Question 2

n = pi;

b1 = n > 3;

b2 = not(b1);

q2 = b2 % Question 2 output

% Question 3

s = 'hi';

a2 = strcmp(s,'Hii');

b2 = strcmp(s,'hi');

c2 = strcmp(s,'Hi');

d2 = strcmp(s,'hi ');

q3 = [a2,b2,c2,d2] % Question 3 output
```

```MATLAB
>> boolean_algebra

q1 =

  1×7 logical array

   1   0   1   1   0   1   1


q2 =

  logical

   0


q3 =

  1×4 logical array

   0   1   0   0

>> 
```