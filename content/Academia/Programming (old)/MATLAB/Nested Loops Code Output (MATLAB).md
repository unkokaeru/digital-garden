```MATLAB
>> % Question 6.1.1a
>> nested_sum_a
The sum is 35.728000
>> % Question 6.1.1b
>> nested_sum_b
The sum is 31.180800
```

```nested_sum_a.m
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

```nested_sum_b.m
% A short script to calculate a nested sum excl. a

sum = 0;

x = 0.4;

a = 7;

for n = 1:10

for m = 1:4

if n ~= a

sum = sum + n*x^m;

end

end

end

fprintf("The sum is %f\n",sum);
```