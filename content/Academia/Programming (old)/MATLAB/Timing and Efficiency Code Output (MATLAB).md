```MATLAB
>> Kronecker_double_sum(10000)

ans =

    50005000

>> Kronecker_testing
>> eff_Kronecker_double_sum(10000)

ans =

    50005000

>> efff_Kronecker_double_sum(10000)

ans =

    50005000

>> Kronecker_eff_test % k = 10000
Elapsed time is 0.131591 seconds.
Elapsed time is 0.000163 seconds.
Elapsed time is 0.000332 seconds.
>> Kronecker_eff_test % k = 20000
Elapsed time is 0.466981 seconds.
Elapsed time is 0.000145 seconds.
Elapsed time is 0.000124 seconds.
>> Kronecker_eff_test % k = 30000
Elapsed time is 1.032543 seconds.
Elapsed time is 0.000582 seconds.
Elapsed time is 0.000118 seconds.
>> Kronecker_eff_test % k = 40000
Elapsed time is 1.813770 seconds.
Elapsed time is 0.000132 seconds.
Elapsed time is 0.000229 seconds.
>> 
```

```Kronecker_double_sum.m
function S = Kronecker_double_sum(N)
    % Calculates a double sum up to N using the Kronecker delta-function.
    % :param N: Upper limit of the summation.
    % :return S: The result of the summation.
    
    % Initalise the sum, S
    S = 0;

    % Calculate the Kronecker double sum
    for n = 1:N
        for m = 1:N
            if n == m
                S = S + (1 * n); % \delta_{nm} = 1
            else
                S = S + (0 * n); % \delta_{nm} = 0
            end
        end
    end
end
```

```eff_Kronecker_double_sum.m
function S = eff_Kronecker_double_sum(N)
    % Calculates a double sum up to N using the Kronecker delta-function,
    % efficiently.
    % :param N: Upper limit of the summation.
    % :return S: The result of the summation.
    
    % Initalise the sum, S
    S = 0;

    % Calculate the Kronecker double sum
    for n = 1:N
        S = S + n;
    end
end
```

```efff_Kronecker_double_sum.m
function S = efff_Kronecker_double_sum(N)
    % Calculates a double sum up to N using the Kronecker delta-function,
    % very efficiently.
    % :param N: Upper limit of the summation.
    % :return S: The result of the summation.

    % Calculate the Kronecker double sum
    S = (N^2 + N) / 2;
end
```

```Kronecker_eff_test.m
% A simple script to test the efficiency of three functions

k = 40000;

tic;
Kronecker_double_sum(k);
toc;

tic;
eff_Kronecker_double_sum(k);
toc;

tic;
efff_Kronecker_double_sum(k);
toc;
```