% plot_functions.m

x = linspace(0,3,200); % Create a vector of 200 elements from 0 to 3
y = 12 - 12*x - 3*x.^2 + 5*x.^3; % Generate the cubic y from x
y2 = 6*sqrt(2) * (sqrt(1 + 1./(1 + x.^2)) + asin(1./(1 + x.^2)) - pi/2); % Define the second y values

plot(x,y,"r--"); % Plot x against y with a red dashed line
title("Plot of a polynomial by William Fayers (27378661)"); % Title the graph

hold on; % Hold the graph so you can plot another curve
plot(x,y2); % Plot the second function
hold off; % Stop holding the graph

xlabel("independent variable"); % Set the x-axis label
ylabel("dependent variable"); % Set the y-axis label

ylim([-20,20]); % Set the range of the y-axis to [-20, 20]

legend("cubic polynomial","entire function") % Create the legend