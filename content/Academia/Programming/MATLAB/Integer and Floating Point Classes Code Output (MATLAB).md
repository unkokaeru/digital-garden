```MATLAB
>> dataTypes = {'int8', 'uint8', 'int16', 'uint16'}; for i = 1:length(dataTypes) testDataType(dataTypes{i}); end
Testing int8
Min Value: -128
Max Value: 127
Overflow Test: 127
Underflow Test: -128
Overflow does not exceed system max value.
Underflow does not go below system min value.
Testing uint8
Min Value: 0
Max Value: 255
Overflow Test: 255
Underflow Test: 0
Overflow does not exceed system max value.
Underflow does not go below system min value.
Testing int16
Min Value: -32768
Max Value: 32767
Overflow Test: 32767
Underflow Test: -32768
Overflow does not exceed system max value.
Underflow does not go below system min value.
Testing uint16
Min Value: 0
Max Value: 65535
Overflow Test: 65535
Underflow Test: 0
Overflow does not exceed system max value.
Underflow does not go below system min value.
>> var_doub = 3.1415;
>> var_int32 = cast(var_doub,"int32");
>> disp(var_int32);
   3

>> whos("var_int32");
  Name           Size            Bytes  Class    Attributes

  var_int32      1x1                 4  int32              

>> a = cos(pi / 2) % Expected: 0

a =

   6.1232e-17

>> b = sqrt(2)^2 - 2 % Expected: 0

b =

   4.4409e-16

>> certainSumCalc
    1.1111

>> certainSumCalc
    1.1111   17.0000

>> certainSumCalc
    1.1111    9.0000

>> 
```

```testDataType.m
function testDataType(dataType)

% Tests the data type given and returns its max/min values.

% :dataType: a data type (string)

% :return: None

% Display the data type being tested

disp(['Testing ', dataType]);

% Find minimum and maximum values for the data type

minValue = intmin(dataType);

maxValue = intmax(dataType);

% Display min and max values

disp(['Min Value: ', num2str(minValue)]);

disp(['Max Value: ', num2str(maxValue)]);

% Test for overflow

overflowValue = cast(maxValue + 1, dataType);

underflowValue = cast(minValue - 1, dataType);

% Display overflow/underflow results

disp(['Overflow Test: ', num2str(overflowValue)]);

disp(['Underflow Test: ', num2str(underflowValue)]);

% Compare against system values

if overflowValue > maxValue

disp('Overflow exceeds system max value.');

else

disp('Overflow does not exceed system max value.');

end

if underflowValue < minValue

disp('Underflow is less than system min value.');

else

disp('Underflow does not go below system min value.');

end

end
```

```certainSumCalc
S_prev = single(1);

S = single(0);

n = 0;

while S_prev ~= S

S_prev = S;

S = S + 10^(-n);

n = n + 1;

end

disp([S,n]);
```