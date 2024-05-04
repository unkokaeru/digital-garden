```MATLAB
>> % Question 6.2.1
>> switch_test
That is correct!
>> switch_test
Way off, try again
>> switch_test
The answer cannot be negative!
>> switch_test
The answer cannot be negative!
>> switch_test
The answer is slightly higher
>> switch_test
That is correct!
>> switch_test
The answer is slightly lower
>> % Question 6.2.2
>> greeting_script
Hello, myself
>> greeting_script
Hello, neighbour!
>> greeting_script
Hello, you should have entered your first name.
>> greeting_script
Hello, you should have entered your first name.
>> greeting_script
Hello, stranger!
>> % Question 6.2.3
>> input_checker("Q")
>> input_checker("sdghsdhig")
Error: sdghsdhig is not valid input.
>> % Question 6.2.4
>> test_script
Invalid value for the input argumement 2.
>> test_script
one
>> test_script
three
>> test_script
five
```

```switch_test.m
number_of_countries = 5;

switch number_of_countries

case {-1,-2}

msg='The answer cannot be negative!';

case 3

msg='The answer is slightly higher';

case 4

msg='That is correct!';

case 5

msg='The answer is slightly lower';

otherwise

msg='Way off, try again';

end

disp(msg);
```

```greeting_script.m
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

```input_checker.m
function input_checker(input)

% Checks validity of input

if input ~= "Q"

fprintf("Error: %s is not valid input.\n",input)

end

end
```

```digit2text.m
function txt = digit2txt(digit)

% Converts digit to textual number

switch digit

case 1

txt = "one";

case 3

txt = "three";

case 5

txt = "five";

otherwise

fprintf("Invalid value for the input argumement %d.\n",digit)

txt = "";

end
```

```test_script.m
% A short script to convert a digit to text

disp(digit2txt(5))
```