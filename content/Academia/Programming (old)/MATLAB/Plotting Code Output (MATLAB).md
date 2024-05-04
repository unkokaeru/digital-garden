```MATLAB-Script
% Define the range for x

x = -2*pi:pi/50:2*pi;

% Calculate the values of y1 and y2

y1 = sin(x);

y2 = cos(x);

% Plotting the graphs

figure;

plot(x, y1, 'b-', x, y2, 'r--'); % Plot the graphs with unique styles

title('Plot of trigonometric functions');

xlabel('x');

ylabel('y');

legend('sin(x)', 'cos(x)'); % Create a legend for the graphs

axis([-2*pi, 2*pi, -1, 1]); % Define a view range for the graphs

grid on;
```
![[Q3.1.1.png]]
```MATLAB-Script
% Set the range for x

x = linspace(-5,5,100);

% Calculate the values of y without c

y = x.^2;

% Plotting the graphs

figure;

colors = ['b', 'r', 'g', 'm']; % Different colors for each graph

index = 1; % Init. index for color selection

for c = 0:2:6

plot(x, y + c, [colors(index) '-']); % Plot the graph with corresponding color

hold on; % Keep the plot for next iterations

index = index + 1; % Update the color index

end

title('Plot of quadratic functions');

xlabel('x');

ylabel('y');

legend('c = 0','c = 2','c = 4','c = 6'); % Create a legend for the graphs

axis([-5, 5, 0, 32]); % Set a view range for the graphs

grid on;

hold off;
```
![[Q3.1.2.jpg]]
```MATLAB-Script
% Set the range for x

x = linspace(-0.5,1.5,100);

% Calculate the values of y

y = exp(-(x).^2);

% Plotting the graphs

figure;

plot(x, y, "black--"); % Plot the graph with corresponding color

title('Plot of the function y(x). Author: William Fayers');

xlabel('x');

ylabel('y');

legend('y(x)'); % Create a legend for the graph

axis([-0.5, 1.5, 0, 1]); % Set a view range for the graph

grid on;
```
![[Q3.1.3.jpg]]
