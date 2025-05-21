
% Description of a nxn grid.
board_size(n).
coord(1..n,1..n). 
num(1..9).
1 { pos(X, Y, N): num(N) } 1 :- coord(X, Y).

% 1. Divide the grid into regions where each region consists of connected cells,
% (horizontally or vertically adjacent).

% Two cells belong to the same region if they have the same number and are connected.
adj(X, Y, X+1, Y) :- coord(X, Y), coord(X+1, Y).
adj(X, Y, X, Y+1) :- coord(X, Y), coord(X, Y+1).
adj(X2, Y2, X1, Y1) :- adj(X1, Y1, X2, Y2).

% Define reachability between cells with same numbers (i.e., regions).
reachable(X, Y, X, Y) :- coord(X, Y).
reachable(X1, Y1, X3, Y3) :- reachable(X1, Y1, X2, Y2),
    adj(X2, Y2, X3, Y3),
    pos(X1, Y1, N), pos(X2, Y2, N), pos(X3, Y3, N).

reachable(X2, Y2, X1, Y1) :- reachable(X1, Y1, X2, Y2).

% 2. The count of cells in that region must be the same as the number in the cell.

% First, count the number of cells reachable from a starting cell with the same number.
count(X, Y, C) :- pos(X, Y, N), C = #count{(X2,Y2): reachable(X,Y,X2,Y2), pos(X2,Y2,N)}.

% Then, enforce that the count equals the number in the starting cell.
:- pos(X, Y, N), count(X, Y, C), C != N.

% 3. Different regions with the same number must not touch.

:- pos(X1, Y1, N), pos(X2, Y2, N), adj(X1, Y1, X2, Y2), not reachable(X1, Y1, X2, Y2).

#show pos/3.
#show board_size/1.

