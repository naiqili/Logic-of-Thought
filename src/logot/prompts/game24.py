# 5-shot
standard_prompt = '''Use numbers and basic arithmetic operations (+ - * /) to obtain 24.
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) = 24
Input: 2 9 10 12
Answer: 2 * 12 * (10 - 9) = 24
Input: 4 9 10 13
Answer: (13 - 9) * (10 - 4) = 24
Input: 1 4 8 8
Answer: (8 / 4 + 1) * 8 = 24
Input: 5 5 5 9
Answer: 5 + 5 + 5 + 9 = 24
Input: {input}
'''

logot_state_represent_prompt = '''\
Input: 
A B C D
Output:
holds(pos(1,A),0). holds(pos(2,B),0). holds(pos(3,C),0). holds(pos(4,D),0). 
Input: 
1 1 4 6
Output:
holds(pos(1,1),0). holds(pos(2,1),0). holds(pos(3,4),0). holds(pos(4,6),0).
Input: 
7 3 9 8
Output:
holds(pos(1,7),0). holds(pos(2,3),0). holds(pos(3,9),0). holds(pos(4,8),0).  
Input: 
{input}
Output:
'''