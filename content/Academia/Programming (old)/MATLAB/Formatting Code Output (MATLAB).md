```MATLAB
>> formatting_demo
0.524
5.235988e-01
    5.235988e-01
     5.236e-01
---------------
0.5236
5.235987756e-01
    5.235987756e-01
     5.2360e-01
```

```formatting_demo.m
% A simple script to demonstrate formatting in MATLAB

% Set an x-value
x = asin(1/2);

% Format the x in different ways when outputting to the console
fprintf("%.3f\n", x);

fprintf("%e\n", x);

fprintf("%16.6e\n",x);

fprintf("%14.3e\n",x);

% Separate the two demos
disp("---------------")

% Using disp for contrast
disp(num2str(x));

exp_format = num2str(x, '%.9e');
disp(exp_format);

exp_format_spaces = ['    ' exp_format];
disp(exp_format_spaces);

exp_format_fewer_digits = ['     ' num2str(x, '%.4e')];
disp(exp_format_fewer_digits);
```