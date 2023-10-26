```MATLAB
>> % Question 1
>> sum(1:1:50)

ans =

        1275

>> sum((1:1:20).^2)

ans =

        2870

>> sum(3:2:9./1:1:4)

ans =

     7

>> (1 - 0.4^11) / (1 - 0.4)

ans =

    1.6666

>> % Question 2
>> sum_squares_1toN(1);sum_squares_1toN(0);sum_squares_1toN(3);
The sum of the squares from 1 to 1 is 1.
The sum of the squares from 1 to 0 is 0.
The sum of the squares from 1 to 3 is 14.
>> sum_x_exp_0toN(1,1);sum_x_exp_0toN(0,-1);sum_x_exp_0toN(3,2);
The sum of 1 to the powers of 0->1 is 2.
The sum of -1 to the powers of 0->0 is 1.
The sum of 2 to the powers of 0->3 is 15.
>> sum_squares_and_cubes_0toN(1);sum_squares_and_cubes_0toN(2);
The sum of the squares from 0 to 1 is 1.
The sum of the cubes from 0 to 1 is 1.
The sum of the squares from 0 to 2 is 5.
The sum of the cubes from 0 to 2 is 9.
>> sum_ratio_square_factorial_exclM_0toN(1,1);sum_ratio_square_factorial_exclM_0toN(2,0);sum_ratio_square_factorial_exclM_0toN(2,1);
The sum of the ratios between the squares and factorials from 0 to 1 excluding 1 is 0.
The sum of the ratios between the squares and factorials from 0 to 2 excluding 0 is 3.
The sum of the ratios between the squares and factorials from 0 to 2 excluding 1 is 2.
>> % Question 3
>> >> loop_with_break
The sum from 0 to 10 is 2047.
>> loop_with_break
The sum from 0 to 100 is 524287.
```

```sum_squares_1toN.m
function S=sum_squares_1toN(n)

S = sum((1:n).^2);

fprintf("The sum of the squares from 1 to %d is %d.\n",n,S)

end
```

```sum_x_exp_0toN.m
function S=sum_x_exp_0toN(n,x)

S = sum(x.^(0:1:n));

fprintf("The sum of %d to the powers of 0->%d is %d.\n",x,n,S)

end
```

```sum_squares_and_cubes_0toN.m
function [S2,S3] = sum_squares_and_cubes_0toN(n)

S2 = sum((0:n).^2);

fprintf("The sum of the squares from 0 to %d is %d.\n",n,S2)

S3 = sum((0:n).^3);

fprintf("The sum of the cubes from 0 to %d is %d.\n",n,S3)

end
```

```sum_ratio_square_factorial_exclM_0toN.m
function S = sum_ratio_square_factorial_exclM_0toN(n,m)

S = 0;

for k = 0:1:n

if k ~= m

S = S + (((k).^2)./factorial(k));

end

end

fprintf("The sum of the ratios between the squares and factorials from 0 to %d excluding %d is %d.\n",n,m,S)

end
```

```loop_with_break.m
x = 2;

n = 100; % Edited from 10 to 100 for the second part of the question

S = 0;

for k = 0:n

if (S + (x^k)) < 1000001

S = S + (x^k);

end

end

fprintf("The sum from 0 to %d is %d.\n",n,S)
```