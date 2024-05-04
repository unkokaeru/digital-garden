```test_temp_1
x = -42;

if x>0

disp('This number is greater than zero')

end
```

```test_temp_2
x = 42;

if x>0

disp('This number is greater than zero')

end
```

```compare_days_1
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

```compare_days_2
Saturday = 18;

Sunday = 17;

if Saturday < Sunday

disp('Saturday is colder')

elseif Sunday < Saturday

disp('Sunday is colder')

elseif Saturday == Sunday

disp('Both days have the same temperature')

end
```

```compare_days_3
Saturday = 17;

Sunday = 17;

if Saturday < Sunday

disp('Saturday is colder')

elseif Sunday < Saturday

disp('Sunday is colder')

elseif Saturday == Sunday

disp('Both days have the same temperature')

end
```

```testnumber
% (a) Set a variable z to 2 + 3i

z = 2;

% (b) Test if z is a complex number

if imag(z) ~= 0

% Multiply z by its complex conjugate and store the result in l

l = sqrt(z * conj(z));

% Set string s to indicate that z is a complex number

s = 'this is a complex number';

end

% (c) Test if z is a real number

if imag(z) == 0

% Square z, take the square root of it, and store the result in l

l = sqrt(z^2);

% Set string s to indicate that z is a real number

s = 'this is a real number';

end

% (d) Test if z is a whole number

if imag(z) == 0 && z == round(z)

% Set string s to indicate that z is an integer

s = 'this is a whole number';

end

% Output the string s and the value of l to the Command Window

disp(s);

disp(l);
```