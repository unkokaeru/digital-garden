```MATLAB
>> my_nexthour(3)

ans =

     4

>> my_nexthour(12)

ans =

     1

>> test_nexthour
Test 1 passed
Test 2 passed
Test 3 passed
Test 4 passed
Test 5 passed
All tests passed!
>> polyno_calc(0)

ans =

     3

>> polyno_calc(1)

ans =

     6

>> test_polyno_calc
Test 1 passed
Test 2 passed
>> polyno_calc([1,2,3])

ans =

     6    11    18
>> test_polyno_calc
Test 1 passed
Test 2 passed
Test 3 passed
```

```my_nexthour.m
function nextHour = my_nexthour(dayHour)

% Calculates the next hour in a 12 hour clock

% :dayHour: integer from 1-12

% :nextHour: integer from 1-12

nextHour = mod(dayHour + 1,12);
```

```test_nexthour.m
% Test 1

msg_error1=['The function nexthour does not work. the nexthour of 1 should be 2. Instead, ', num2str(nexthour(1)), ' was returned.'];

assert(nexthour(1)==2, msg_error1);

disp('Test 1 passed')

% Test 2

msg_error2=['The function nexthour does not work. the nexthour of 2 should be 3. Instead, ', num2str(nexthour(2)), ' was returned.'];

assert(nexthour(2)==3);

disp('Test 2 passed')

% Test 3

msg_error3=['The function nexthour does not work. the nexthour of 12 should be 1. Instead, ', num2str(nexthour(12)), ' was returned.'];

assert(nexthour(12)==1);

disp('Test 3 passed')

% Test 4

msg_error4=['The function nexthour does not work. the nexthour of 4 should be 5. Instead, ', num2str(nexthour(4)), ' was returned.'];

assert(nexthour(4)==5);

disp('Test 4 passed')

% Test 5

msg_error5=['The function nexthour does not work. the nexthour of 12 should be less than 13. Instead, ', num2str(nexthour(12)), ' was returned.'];

assert(nexthour(12)<13);

disp('Test 5 passed')

disp('All tests passed!')
```

```nexthour.m
function nextHour = nexthour(dayHour)

% Calculates the next hour in a 12 hour clock

% :dayHour: integer from 1-12

% :nextHour: integer from 1-12

nextHour = mod(dayHour + 1,12);
```

```polyno_calc.m
function y = polyno_calc(x)

% Calculates the y values of given x values in a polynomial curve

% :x: the x-values on the curve

% :y: the y-values on the curve

y = x.^2 + 2.*x + 3;

end
```

```test_polyno_calc.m
% A simple script to test the function polyno_calc.m

% Test 1

msg_error1=['The function polyno_calc does not work. the polyno_calc of 0 should be 3. Instead, ', num2str(polyno_calc(0)), ' was returned.'];

assert(polyno_calc(0)==3, msg_error1);

disp('Test 1 passed')

% Test 2

msg_error2=['The function polyno_calc does not work. the polyno_calc of 1 should be 6. Instead, ', num2str(polyno_calc(1)), ' was returned.'];

assert(polyno_calc(1)==6);

disp('Test 2 passed')

% Test 3

msg_error3=['The function polyno_calc does not work. the polyno_calc of [1, 2, 3] should be [6, 11, 18]. Instead, ', num2str(polyno_calc([1, 2, 3])), ' was returned.'];

assert(sum(polyno_calc([1, 2, 3])==[6, 11, 18])==3);

disp('Test 3 passed')
```