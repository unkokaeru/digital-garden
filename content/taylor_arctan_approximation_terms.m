function min_terms = taylor_arctan_approximation_terms(x, Delta)
    % Calculate the minimum number of terms needed for a specific accuracy approximation of arctan(x) using a Taylor's series

    % Check if x is within the valid range
    if x < -1 || x > 1 || imag(x)~=0
        error('The value of x is out of the valid range [-1, 1].');
    end

    % Initialise the sum and the number of terms
    sum = 0;
    min_terms = 0;
    true_value = atan(x); % True value of arctan(x)

    % While the absolute difference is larger than Delta, keep adding terms
    while abs(true_value - sum) > Delta
        min_terms = min_terms + 1;
        term = ((-1)^(min_terms+1)) * (x^(2*min_terms-1)) / (2*min_terms - 1);
        sum = sum + term;
    end
end