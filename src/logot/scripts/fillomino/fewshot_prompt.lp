% Introduction:
% Hitori is a logic-based puzzle game. 
% It is typically played on a square grid filled with numbers, 
% and the objective is to eliminate duplicates by marking some cells as black
% in each row and column according to specific rules.

% The logic program includes the following atoms:
% coord(X, Y) : The coordination of the grid.
% pos(X, Y, N) : The number in the cell (X, Y) is N.
% num(N) : Possible numbers in the cells, N=1..9
% black(X, Y) : Cell (X, Y) is marked as black.
% adj(X1, Y1, X2, Y2) : Cell (X1, Y1) and cell (X2, Y2) are adjacent to each other.
% reachable(X1, Y1, X2, Y2) : Cell (X1, Y1) and cell (X2, Y2) are reachable to each other.

% Description of a nxn grid.
board_size(n).
coord(1..n,1..n). 
num(1..9).
1 { pos(X, Y, N): num(N)} 1 :- coord(X, Y).


% 1. Eliminate numbers by marking them black,
% so that no row or column has duplicate numbers.
1 { black(X, Y1); black(X, Y2) } 2 :- pos(X, Y1, N), pos(X, Y2, N), Y1 != Y2.
1 { black(X1, Y); black(X2, Y) } 2 :- pos(X1, Y, N), pos(X2, Y, N), X1 != X2.

% Blackened cells cannot be horizontally or vertically adjacent.
:- black(X, Y), black(X + 1, Y).
:- black(X, Y), black(X, Y + 1).

% We have complete knowledge for blackened cells.
-black(X, Y) :- coord(X, Y), not black(X, Y).

% Not blackened cells must form a single connected group, 
% meaning they are reachable to each other,
% and a cell is not reachable if it is blackened.

adj(X, Y, X, Y+1) :- coord(X, Y), coord(X, Y+1).
adj(X+1, Y, X, Y) :- coord(X, Y), coord(X+1, Y).
adj(X2, Y2, X1, Y1) :- adj(X1, Y1, X2, Y2).

reachable(X1, Y1, X1, Y1) :- -black(X1, Y1).
reachable(X1, Y1, X3, Y3) :- reachable(X1, Y1, X2, Y2), adj(X2, Y2, X3, Y3),
    -black(X1, Y1), -black(X2, Y2), -black(X3, Y3).
reachable(X2, Y2, X1, Y1) :- reachable(X1, Y1, X2, Y2).

:- -black(X1, Y1), -black(X2, Y2), not reachable(X1, Y1, X2, Y2).



% Introduction:
% Sudoku is a popular logic-based number placement puzzle. 
% The puzzle is played on a 9×9 grid divided into nine 3×3 subgrids (also called regions).
% The goal is to fill in the grid so that each number appears exactly once in each 
% row, column, and 3×3 subgrid.

% The logic program includes the following atoms:
% coord(X, Y) : The coordination of the grid.
% pos(X, Y, N) : The number in the cell (X, Y) is N.
% num(N) : Possible numbers in the cells, N=1..9
% adj(X1, Y1, X2, Y2) : Cell (X1, Y1) and cell (X2, Y2) are adjacent to each other.
% reachable(X1, Y1, X2, Y2) : Cell (X1, Y1) and cell (X2, Y2) are reachable to each other.

% Description of a 9x9 grid.
board_size(9).
coord(1..9,1..9). 
num(1..9).
1 { pos(X, Y, N): num(N)} 1 :- coord(X, Y).

% Fill each row with the numbers 1 through 9 without repeating any number.
:- pos(X, Y1, N), pos(X, Y2, N), Y1 != Y2.

% Fill each column with the numbers 1 through 9 without repeating any number.
:- pos(X1, Y, N), pos(X2, Y, N), X1 != X2.

% Fill each 3x3 subgrid with the numbers 1 through 9 without repeating any number.
:- pos(X1, Y1, N), pos(X2, Y2, N),
   (X1-1)/3 == (X2-1)/3, (Y1-1)/3 == (Y2-1)/3, (X1,Y1) != (X2,Y2).


% Introduction
% Fillomino is a number logic puzzle. 
% The puzzle is played on a rectangular grid where some cells may initially contain numbers. 
% The goal is to divide the grid into regions, or "polyominoes," 
% such that each region contains exactly one number and has an area (number of cells) equal to that number.

% The logic program includes the following atoms:
% coord(X, Y) : The coordination of the grid.
% pos(X, Y, N) : The number in the cell (X, Y) is N.
% num(N) : Possible numbers in the cells, N=1..9
% adj(X1, Y1, X2, Y2) : Cell (X1, Y1) and cell (X2, Y2) are adjacent to each other.
% reachable(X1, Y1, X2, Y2) : Cell (X1, Y1) and cell (X2, Y2) are reachable to each other.

% Description of a nxn grid.
ASP_RULES

% 1. Divide the grid into regions where each region consists of connected cells,
% (horizontally or vertically adjacent).
ASP_RULES

% The cout of cells in that region must be the same with the number in the cell.
ASP_RULES
                
Complete the ASP_RULES.

