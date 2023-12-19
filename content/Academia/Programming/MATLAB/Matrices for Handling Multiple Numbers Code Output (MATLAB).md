```MATLAB
>> graphGenderCount
>> edit averhighs.txt
>> graphMonthlyTemp
>> graphMonthlyTemp
>> 
```

```graphGenderCount.m
% A simple script to graph the data in a txt file.

% Load the data into a matrix
data = readmatrix('yearmalefemale.txt');

% Extract the columns
year = data(:, 1); % First column
male = data(:, 2); % Second column
female = data(:, 3); % Third column

% Plot the number of males
plot(year, male, 'b'); % 'b' for blue line
hold on; % Keep the current plot

% Plot the number of females
plot(year, female, 'r'); % 'r' for red line

% Adding labels and legends
xlabel('Age');
ylabel('Population');
legend('Males', 'Females');
title('Population by Gender and Age in the UK (2014)');

% Display the graph
hold off;

```

![[graph.png]]

```graphMonthlyTemp.m
data = load('averhighs.txt');

months = 1:12;

figure;

hold on;

legendInfo = cell(size(data, 1), 1);

for i = 1:size(data, 1)

celsiusTemps = fahrenheitToCelsius(data(i, 2:end));

plot(months, celsiusTemps);

legendInfo{i} = ['Location ' num2str(data(i, 1))];

end

title('Average High Temperatures for Three Locations (in Celsius)');

xlabel('Month');

ylabel('Temperature (°C)');

legend(legendInfo, 'Location', 'best');

hold off;

function celsius = fahrenheitToCelsius(fahrenheit)

celsius = (fahrenheit - 32) * 5 / 9;

end
```

```fah2cel.m
function celsius = fah2cel(fahrenheit)

% Converts Fahrenheit to Celsius

celsius = (fahrenheit - 32)*(5/9);

end
```

![[graphTemp.png]]
![[graphTempC.png]]