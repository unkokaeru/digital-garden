```MATLAB
>> mat_indexing_demo
     1    -1     0     0
    -1     2    -1     0
     0    -1     3    -1
     0     0    -1     4
```

```mat_indexing_demo.m
% A simple script to demonstrate matrix indexing.

M = zeros(4);
n=1;

for row = 1:4
    for col = 1:4
        if row == col
            M(row, col) = n;
            n = n + 1;
        elseif abs(row - col) == 1
            M(row, col) = -1;
        end
    end
end

disp(M);
```