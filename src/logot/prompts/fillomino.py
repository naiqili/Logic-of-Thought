# 5-shot
standard_prompt = '''\
You are solving a Fillomino puzzle.

Rules:
1. The puzzle is played on a rectangular grid.
2. Some cells may initially contain numbers; others contain `0` (representing an empty cell).
3. The objective is to divide the grid into contiguous regions (called polyominoes).
4. Each polyomino must:
   * Contain exactly one number (either pre-filled or filled during solving),
   * Have an area (number of cells) equal to that number,
   * Consist of orthogonally (up/down/left/right) connected cells,
   * Not share an edge with another polyomino of the same size.

Input:
A list of strings representing rows of the grid. Each character is a digit (0–9). For example:
20000
03103
20030
00002
00210

Output:
A list of strings representing the solved grid, where each character is a digit (1–9), and all regions satisfy the Fillomino rules. 
Start the final answer with %.

For example:
%
22444
33143
23433
24442
12212

Keep the answer short. Only show the result.

Input:
{input}
'''

logot_state_represent_prompt = '''\
Input: 
5
40030
03310
20004
03440
01003
% Thought:
% #const n=5.
% pos_(1, 1, 4). pos_(1, 2, 0). pos_(1, 3, 0). pos_(1, 4, 3). pos_(1, 5, 0).
% pos_(2, 1, 0). pos_(2, 2, 3). pos_(2, 3, 3). pos_(2, 4, 1). pos_(2, 5, 0).
% pos_(3, 1, 2). pos_(3, 2, 0). pos_(3, 3, 0). pos_(3, 4, 0). pos_(3, 5, 4).
% pos_(4, 1, 0). pos_(4, 2, 3). pos_(4, 3, 4). pos_(4, 4, 4). pos_(4, 5, 0).
% pos_(5, 1, 0). pos_(5, 2, 1). pos_(5, 3, 0). pos_(5, 4, 0). pos_(5, 5, 3).
% Output:
#const n=5.
pos(1, 1, 4). pos(1, 4, 3).  
pos(2, 2, 3). pos(2, 3, 3). pos(2, 4, 1). 
pos(3, 1, 2). pos(3, 5, 4). 
pos(4, 2, 3). pos(4, 3, 4). pos(4, 4, 4). 
pos(5, 2, 1). pos(5, 5, 3).

Input: 
{input}

In the output, pos(x, y, n) means the number of row x and column y is n. A cell with 0 is skipped.
Complete the text of Thought and Output. Only show the result, do not explain.
'''