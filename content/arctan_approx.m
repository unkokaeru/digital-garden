% arctan_approx.m

x = 0.6; % Set the value for x

% Check if x is within the validity range for arctan(x)
if x < -1 || x > 1
    fprintf('The value of x = %.4f is out of the validity range.\n', x);
    return;
end

sum = 0; % Initialise the sum

% Calculate the sum for the first 10 terms to approximate arctan(x)
for n = 1:10
    term = ((-1)^(n+1)) * (x^(2*n-1)) / (2*n - 1);
    sum = sum + term;
end

fprintf('Evaluating arctan(%.4f) is approximately %.4f.\n', x, sum); % Display the result using an fstring