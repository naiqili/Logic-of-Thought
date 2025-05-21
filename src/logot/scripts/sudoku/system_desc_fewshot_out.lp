
% Description of a 9x9 grid.
board_size(9).
coord(1..9,1..9).
num(1..9).
1 { pos(X, Y, N) : num(N) } 1 :- coord(X, Y).

% Fill each row with the numbers 1 through 9 without repeating any number.
:- pos(X, Y1, N), pos(X, Y2, N), Y1 != Y2.

% Fill each column with the numbers 1 through 9 without repeating any number.
:- pos(X1, Y, N), pos(X2, Y, N), X1 != X2.

% Fill each 3x3 subgrid with the numbers 1 through 9 without repeating any number.
:- pos(X1, Y1, N), pos(X2, Y2, N),
   (X1-1)/3 == (X2-1)/3, (Y1-1)/3 == (Y2-1)/3,
   (X1, Y1) != (X2, Y2).



#show pos/3.

