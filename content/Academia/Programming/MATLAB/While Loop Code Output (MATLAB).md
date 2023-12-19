```MATLAB
>> % Question 6.3.2
>> while_sum
The first sum is 1275, and the second sum is 2870.
>> % Question 6.3.3
>> nested_while_sum
The sum is 0.649600
>> % Question 6.3.4
>> sum_squares_a(100000)

ans =

    68

>> sum_squares_b(100000)

ans =

    67
```

```while_sum.m
% A short script to determine sums with a while loop

sum1 = 0;

sum2 = 0;

k = 1;

n = 1;

while k <= 50

sum1 = sum1 + k;

k = k + 1;

end

while n <= 20

sum2 = sum2 + n^2;

n = n + 1;

end

fprintf("The first sum is %d, and the second sum is %d.\n",sum1, sum2)
```

```nested_while_sum.m
% A short script to calculate a nested sum excl. a with a while loop

n = 1;

m = 1;

sum = 0;

x = 0.4;

a = 7;

while n <= 10

while m <= 4

if n ~= a

sum = sum + n*x^m;

end

m = m + 1;

end

n = n + 1;

end

fprintf("The sum is %f\n",sum);
```

```sum_squares_a.m
function termsNeeded = sum_squares_a(targetSum)

% Calculates terms needed to sum squares to just beyond a given value

termsNeeded = 1;

sum = 0;

while sum < targetSum

sum = sum + termsNeeded^2;

termsNeeded = termsNeeded + 1;

end

end
```

```sum_squares_b.m
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