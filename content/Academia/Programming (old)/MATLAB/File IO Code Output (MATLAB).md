```MATLAB
>> body_temp_graph
>> reverse_script
>> type reversed.txt

   1.0000000e+00
   3.0000000e+00
   5.0000000e+00
   7.0000000e+00
   9.0000000e+00
   1.1000000e+01
   1.3000000e+01
>> reverse_script
>> type double_reversed.txt

   1.3000000e+01
   1.1000000e+01
   9.0000000e+00
   7.0000000e+00
   5.0000000e+00
   3.0000000e+00
   1.0000000e+00
>> reverse_function('sample.txt','sample_reversed.txt')
>> type sample_reversed.txt

   1.0000000e+00
   3.0000000e+00
   5.0000000e+00
   7.0000000e+00
   9.0000000e+00
   1.1000000e+01
   1.3000000e+01
>> edit subjexp.txt
>> fileex
5.300000  a
2.200000  b
3.300000  a 
4.400000  a
1.100000  b
File close successful
>> fileex
5.300000  a
2.200000  b
3.300000  a 
4.400000  a
1.100000  b
Sum: 16.3
File close successful
>> edit xypts.dat
>> plot_xy_data_for
File closed successfully.
>> plot_xy_data
File closed successfully.
```

```body_temp_graph.m
% A simple script to plot the temperature of a human body over the day by

% importing the data from files.

time = load("time.txt");

temp = load("temp.txt");

plot(time, temp)

xlabel("Time of day (hours)")

ylabel("Temperature of the human body (Celsius)")

title("Temperature of a human body over the day")
```

![[body_temp_graph.jpg]]

```reverse_script.m
% A simple script to reverse an array of numbers in a file.

inputfilename = "sample.txt"; % then changed to "reversed.txt"

outputfilename = "reversed.txt"; % then changed to "double_reversed.txt"

norm_text = load(inputfilename);

reverse_text = norm_text(end:-1:1);

save(outputfilename, 'reverse_text', '-ascii');
```

```reverse_function.m
function reverse_function(inputfilename, outputfilename)

% Reverses an array in a given file into a given output file

original_text = load(inputfilename);

reversed_text = original_text(end:-1:1);

save(outputfilename, 'reversed_text', '-ascii')

end
```

```fileex.m
% Reads from a file one line at a time using fgetl

% Each line has a number and a character

% The script separates and prints them

% Initalise sum

sum = 0;

% Open the file and check for success

fid = fopen('subjexp.txt');

if fid == -1

disp('File open not successful')

else

while feof(fid) == 0

aline = fgetl(fid);

% Separate each line into the number and character

% code and convert to a number before printing

[num, charcode] = strtok(aline);

sum = sum + str2double(num); % Sum numbers

fprintf('%2f %s\n', str2double(num), charcode);

end

% Print the sum of the numbers in the file

fprintf("Sum: %.1f\n",sum);

% Check the file close for success

closeresult = fclose(fid);

if closeresult == 0

disp('File close successful')

else

disp('File close not successful')

end

end
```

```ploy_xy_data_for.m
% A simple script to read x and y data points from a file and plot them

% Initialize vectors for x and y values

x_values = [];

y_values = [];

% Open the file

fileID = fopen('xypts.dat', 'r');

% Check if the file was opened successfully

if fileID == -1

error('File could not be opened');

else

% Read the file line by line

for i = 1:10

line = fgetl(fileID);

if ~ischar(line)

break; % Exit loop if end of file is reached

end

% Extract x and y values from the line

values = sscanf(line, 'x %f y %f');

x_values(end+1) = values(1);

y_values(end+1) = values(2);

end

% Plot the points

plot(x_values, y_values, 'o-');

xlabel('x values');

ylabel('y values');

title('Plot of x and y values from file');

% Attempt to close the file

fclose_status = fclose(fileID);

if fclose_status == 0

disp('File closed successfully.');

else

disp('File could not be closed.');

end

end
```

![[xy_plot.jpg]]

```plot_xy_data
% MATLAB Script to read x and y data points from a file and plot them

% Handles an unknown number of data points

% Initialize vectors for x and y values

x_values = [];

y_values = [];

% Open the file

fileID = fopen('xypts.dat', 'r');

% Check if the file was opened successfully

if fileID == -1

error('File could not be opened');

else

% Initialize the counter for the number of points

point_count = 0;

% Read the file line by line until the end of the file is reached

while ~feof(fileID)

line = fgetl(fileID);

if ~ischar(line)

break; % Exit loop if an invalid line is encountered

end

% Extract x and y values from the line

values = sscanf(line, 'x %f y %f');

x_values(end+1) = values(1);

y_values(end+1) = values(2);

point_count = point_count + 1;

end

% Plot the points

plot(x_values, y_values, 'o-');

xlabel('x values');

ylabel('y values');

title(['Plot of ' num2str(point_count) ' x and y values from file']);

% Attempt to close the file

fclose_status = fclose(fileID);

if fclose_status == 0

disp('File closed successfully.');

else

disp('File could not be closed.');

end

end
```

![[xy_plot_2.jpg]]