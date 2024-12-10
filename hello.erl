-module(factorial).
-export([calculate/1]).

% Base case: factorial of 0 is 1
calculate(0) ->
    1;

% Recursive case: N! = N * (N-1)!
calculate(N) when N > 0 ->
    N * calculate(N - 1).
