

% Description of a nxn grid.
board_size(n).
coord(1..n,1..n). 
num(1..9).
1 { pos(X, Y, N): num(N) } 1 :- coord(X, Y).
0 { black(X, Y) } 1 :- coord(X, Y).

% 1. Eliminate numbers by marking them black,
% so that no row or column has duplicate numbers.
:- pos(X, Y1, N), pos(X, Y2, N), Y1 != Y2, not black(X, Y1), not black(X, Y2).
:- pos(X1, Y, N), pos(X2, Y, N), X1 != X2, not black(X1, Y), not black(X2, Y).

% Blackened cells cannot be horizontally or vertically adjacent.
adj(X, Y, X+1, Y) :- coord(X, Y), coord(X+1, Y).
adj(X, Y, X, Y+1) :- coord(X, Y), coord(X, Y+1).
adj(X2, Y2, X1, Y1) :- adj(X1, Y1, X2, Y2).
:- black(X1, Y1), black(X2, Y2), adj(X1, Y1, X2, Y2).

% We have complete knowledge for blackened cells.
% (Already ensured by the choice rule: 0 { black(X,Y) } 1)

% Not blackened cells must form a single connected group,
% meaning they are reachable to each other,
% and a cell is not reachable if it is blackened.

reachable(X, Y, X, Y) :- coord(X, Y), not black(X, Y).
reachable(X1, Y1, X3, Y3) :- reachable(X1, Y1, X2, Y2), adj(X2, Y2, X3, Y3), 
                              not black(X3, Y3).

% Pick one white cell as starting point.
start(X, Y) :- coord(X, Y), not black(X, Y).

% Ensure that all non-black cells are reachable from the start.
:- coord(X, Y), not black(X, Y), start(X0, Y0), not reachable(X0, Y0, X, Y).
           

#show black/2.
#show board_size/1.
