# 5-shot
standard_prompt = '''\
You are given a Hitori puzzle represented as a square grid of digits. Your task is to solve the puzzle according to the following rules:
1. No row or column can have duplicate numbers among the unmarked (white) cells.
2. Black cells (`b`) cannot be adjacent horizontally or vertically (no two `b`s side by side).
3. White cells (`w`) must form a single connected group (i.e., you can reach any white cell from any other white cell by moving horizontally or vertically through other white cells).

Input:
A grid of digits representing the Hitori puzzle. For example:
44254
51442
14434
23415
42122

Output:
A grid of the same size, where each cell is either:
'b' for a blacked-out cell (duplicate eliminated),
'w' for a white cell (kept in the puzzle).
Start the final answer with %.

For example:
%
bwwwb
wwbww
wbwwb
wwbww
wbwwb

Please solve the puzzle and return only the output grid.
Input: 
{input}

Keep the answer short. Only show the result.
'''

logot_state_represent_prompt = '''\
Input: 
5
21324
45322
34251
14332
25143
Output:
#const n=5.
pos(1, 1, 2). pos(1, 2, 1). pos(1, 3, 3). pos(1, 4, 2). pos(1, 5, 4). 
pos(2, 1, 4). pos(2, 2, 5). pos(2, 3, 3). pos(2, 4, 2). pos(2, 5, 2). 
pos(3, 1, 3). pos(3, 2, 4). pos(3, 3, 2). pos(3, 4, 5). pos(3, 5, 1). 
pos(4, 1, 1). pos(4, 2, 4). pos(4, 3, 3). pos(4, 4, 3). pos(4, 5, 2).
pos(5, 1, 2). pos(5, 2, 5). pos(5, 3, 1). pos(5, 4, 4). pos(5, 5, 3).

Input: 
8
83161254
76651426
31254865
53182432
48632574
24356137
54727718
52718145
Output:
#const n=8.
pos(1, 1, 8). pos(1, 2, 3). pos(1, 3, 1). pos(1, 4, 6). pos(1, 5, 1). pos(1, 6, 2). pos(1, 7, 5). pos(1, 8, 4).
pos(2, 1, 7). pos(2, 2, 6). pos(2, 3, 6). pos(2, 4, 5). pos(2, 5, 1). pos(2, 6, 4). pos(2, 7, 2). pos(2, 8, 6).
pos(3, 1, 3). pos(3, 2, 1). pos(3, 3, 2). pos(3, 4, 5). pos(3, 5, 4). pos(3, 6, 8). pos(3, 7, 6). pos(3, 8, 5).
pos(4, 1, 5). pos(4, 2, 3). pos(4, 3, 1). pos(4, 4, 8). pos(4, 5, 2). pos(4, 6, 4). pos(4, 7, 3). pos(4, 8, 2).
pos(5, 1, 4). pos(5, 2, 8). pos(5, 3, 6). pos(5, 4, 3). pos(5, 5, 2). pos(5, 6, 5). pos(5, 7, 7). pos(5, 8, 4).
pos(6, 1, 2). pos(6, 2, 4). pos(6, 3, 3). pos(6, 4, 5). pos(6, 5, 6). pos(6, 6, 1). pos(6, 7, 3). pos(6, 8, 7).
pos(7, 1, 5). pos(7, 2, 4). pos(7, 3, 7). pos(7, 4, 2). pos(7, 5, 7). pos(7, 6, 7). pos(7, 7, 1). pos(7, 8, 8).
pos(8, 1, 5). pos(8, 2, 2). pos(8, 3, 7). pos(8, 4, 1). pos(8, 5, 8). pos(8, 6, 1). pos(8, 7, 4). pos(8, 8, 5).

Input: 
{input}
Output:

Complete the text. Only show the result, do not explain.
'''