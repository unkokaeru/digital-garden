```MATLAB
>> subplotter
>> logplotter
>> surfplotter
>> lorenzplotter
>> pyramidplotter
```

```subplotter.m
% A simple script to plot two subplots.

% Define the range for x
x = linspace(0, 2*pi, 100);

% Define the functions
y1 = sin(3 * x);
y2 = cos(pi * x).^2;

% Create a figure for the plots
figure;

% Plot y = sin(3x) in the top subplot
subplot(2,1,1);
plot(x, y1, 'b-');
title('y = sin(3x)');
ylabel('y');

% Plot y = cos(πx)^2 in the bottom subplot
subplot(2,1,2);
plot(x, y2, 'r-');
title('y = cos(πx)^2');
xlabel('x');
ylabel('y');
```

![[subplot_demo.png]]

```logplotter.m
% A simple script to plot on a logarithmic scale.

% Define the range for x
x = linspace(1, 10, 100);

% Calculate the values for each function
y1 = x.^2;
y2 = x.^x;
y3 = exp(x);

% Create a figure for the plot
figure;

% Plot the functions
plot(x, y1, 'b-', x, y2, 'r-', x, y3, 'g-');
set(gca, 'YScale', 'log');

% Add title and labels
title('Graphs of x^2, x^x, and e^x');
xlabel('x');
ylabel('y');
legend('x^2', 'x^x', 'e^x');

% Display the plot
grid on;
```

![[logplot_demo.png]]

```surfplotter.m
% A simple script to plot the surface and contour of a 3d function

% Define the range for x and y
x = linspace(-pi, pi, 100);
y = linspace(-pi, pi, 100);

% Create a meshgrid for x and y
[X, Y] = meshgrid(x, y);

% Calculate z
Z = cos(X) + sin(Y);

% Create a figure for the plots
figure;

% Plot the surface in the top subplot
subplot(2, 1, 1);
surf(X, Y, Z);
title('Surface of z = cos(x) + sin(y)');
xlabel('x');
ylabel('y');
zlabel('z');

% Plot the contour in the bottom subplot
subplot(2, 1, 2);
contour(X, Y, Z);
title('Contour of z = cos(x) + sin(y)');
xlabel('x');
ylabel('y');
```

![[surfplot_demo.png]]

```lorenzplotter.m
% A simple script to use a lorenz curve.

% Call the function
[x, y, z] = lorenz_curve();

% Plot the curve and store the figure handle
figureHandle = plot3(x, y, z);
title('Lorenz Attractor');
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');

% Change line width and color
set(figureHandle, 'LineWidth', 2, 'Color', 'red');

% Animated plot using comet3
figure;
comet3(x, y, z);

% Write the values to a file
A = [x, y, z];
save('lorenz-values.txt', 'A', '-ascii');
```

![[lorenz_demo_1.png]]

![[lorenz_demo_2.png]]

```pyramidplotter.m
% A simple script to plot a population pyramid.

% Load the data into a matrix
data = readmatrix('yearmalefemale.txt');

% Extract the columns
year = data(:, 1); % First column
male = data(:, 2); % Second column
female = data(:, 3); % Third column

% Create figure
figure;

% Plot male population on the left
subplot(1, 2, 1);
male_plot = barh(year, male, 'b');
set(gca, 'Xdir', 'reverse');
xlabel('Male Population');
ylabel('Year');
title('Male Population Pyramid');

% Plot female population on the right
subplot(1, 2, 2);
barh(year, female, 'r');
xlabel('Female Population');
title('Female Population Pyramid');
```

![[pyramidplot_demo.png]]