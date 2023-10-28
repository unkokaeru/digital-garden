% summation_script.m

sum_val = 0; % Initalise the sum value

% Loop from -5^2 to 5^2
for n = -5^2:5^2
    sum_val = sum_val + 3*n^2 - 3; % Slowly calculate the sum for each value of n
end

fprintf("The calculated sum is %d.\n",sum_val); % Print the answer using an fstring