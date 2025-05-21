# 5-shot
standard_prompt = '''\
You are a Sudoku-solving assistant.
Given a 9x9 Sudoku puzzle, where each row is a string of 9 digits and '0' represents an empty cell, solve the puzzle and print the completed Sudoku grid.
Input: 
{input}

Keep the answer short. Output like:
%
GRID OF PUZZLE ANSWER
'''

logot_state_represent_prompt = '''\
Input: 
000850000
020000000
010900700
070025093
402000000
000000500
097500000
563000004
000000680
Thought:
pos_(1, 1, 0). pos_(1, 2, 0). pos_(1, 3, 0). pos_(1, 4, 8). pos_(1, 5, 5). pos_(1, 6, 0). pos_(1, 7, 0). pos_(1, 8, 0). pos_(1, 9, 0).
pos_(2, 1, 0). pos_(2, 2, 2). pos_(2, 3, 0). pos_(2, 4, 0). pos_(2, 5, 0). pos_(2, 6, 0). pos_(2, 7, 0). pos_(2, 8, 0). pos_(2, 9, 0).
pos_(3, 1, 0). pos_(3, 2, 1). pos_(3, 3, 0). pos_(3, 4, 9). pos_(3, 5, 0). pos_(3, 6, 0). pos_(3, 7, 7). pos_(3, 8, 0). pos_(3, 9, 0).
pos_(4, 1, 0). pos_(4, 2, 7). pos_(4, 3, 0). pos_(4, 4, 0). pos_(4, 5, 2). pos_(4, 6, 5). pos_(4, 7, 0). pos_(4, 8, 9). pos_(4, 9, 3).
pos_(5, 1, 4). pos_(5, 2, 0). pos_(5, 3, 2). pos_(5, 4, 0). pos_(5, 5, 0). pos_(5, 6, 0). pos_(5, 7, 0). pos_(5, 8, 0). pos_(5, 9, 0).
pos_(6, 1, 0). pos_(6, 2, 0). pos_(6, 3, 0). pos_(6, 4, 0). pos_(6, 5, 0). pos_(6, 6, 0). pos_(6, 7, 5). pos_(6, 8, 0). pos_(6, 9, 0).
pos_(7, 1, 0). pos_(7, 2, 9). pos_(7, 3, 7). pos_(7, 4, 5). pos_(7, 5, 0). pos_(7, 6, 0). pos_(7, 7, 0). pos_(7, 8, 0). pos_(7, 9, 0).
pos_(8, 1, 5). pos_(8, 2, 6). pos_(8, 3, 3). pos_(8, 4, 0). pos_(8, 5, 0). pos_(8, 6, 0). pos_(8, 7, 0). pos_(8, 8, 0). pos_(8, 9, 4).
pos_(9, 1, 0). pos_(9, 2, 0). pos_(9, 3, 0). pos_(9, 4, 0). pos_(9, 5, 0). pos_(9, 6, 0). pos_(9, 7, 6). pos_(9, 8, 8). pos_(9, 9, 0).
Output:
pos(1, 4, 8). pos(1, 5, 1). 
pos(2, 2, 2). 
pos(3, 2, 1). pos(3, 4, 9). pos(3, 7, 7).
pos(4, 2, 7). pos(4, 5, 2). pos(4, 6, 5). pos(4, 8, 9). pos(4, 9, 3).
pos(5, 1, 4). pos(5, 3, 2).
pos(6, 7, 5). 
pos(7, 2, 9). pos(7, 3, 7). pos(7, 4, 5).
pos(8, 1, 5). pos(8, 2, 6). pos(8, 3, 3). pos(8, 9, 4).
pos(9, 7, 6). pos(9, 8, 8).

Input: 
{input}

In the output, pos(x, y, n) means the number of row x and column y is n. A cell with 0 is skipped.
Complete the text of Thought and Output. Only show the result, do not explain.
'''