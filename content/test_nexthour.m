% Test 1
msg_error1=['The function nexthour does not work. the nexthour of 1 should be 2. Instead, ', num2str(nexthour(1)), ' was returned.'];
assert(nexthour(1)==2, msg_error1);
disp('Test 1 passed')

% Test 2
assert(nexthour(2)==3);

% Test 3
assert(nexthour(12)==1);


disp('All tests passed!')
