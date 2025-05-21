import re
import os
import sympy
import pandas as pd
from logot.tasks.base import Task, DATA_PATH, SCRIPT_PATH
from logot.prompts.sudoku import * 


class SudokuTask(Task):
    """
    Input (x)   : a string of sudoku puzzle
    Output (y)  : a string of sudoku answer
    Reward (r)  : 0 or 1, depending on whether the result is correct
    Input Example: 
        1..5.37..6.3..8.9......98...1.......8761..........6...........7.8.9.76.47...6.312
    Output Example: 
        198543726643278591527619843914735268876192435235486179462351987381927654759864312
    """
    def __init__(self, 
                 data_file='sudoku.csv',
                 sys_desc_file='system_desc_manual.lp'):
        """
        file: a csv file (fixed)
        """
        super().__init__()
        path = os.path.join(DATA_PATH, 'sudoku', data_file)
        self.data_path = path
        self.data = list(pd.read_csv(path)['puzzle'])
        self.difficulty = list(pd.read_csv(path)['difficulty'])
        self.sys_desc_file = os.path.join(SCRIPT_PATH, 'sudoku', sys_desc_file)

    def __len__(self) -> int:
        return len(self.data)
    
    @staticmethod
    def str2grid(s: str) -> str:
        res = '\n'.join(s[i:i+9] for i in range(0, len(s), 9))
        return res
        
    def get_input(self, idx: int) -> str:
        res = self.data[idx]
        res = res.replace('.', '0')
        res = self.str2grid(res)
        return res

    def test_output(self, idx: int, output: str):
        def parse_sudoku(sudoku_str):
            return [[int(char) for char in line] for line in sudoku_str.split()]

        def is_valid_sudoku_solution(str_input, str_output):
            """Check if str_output is a valid solution for the given str_input Sudoku puzzle."""
            grid_input = parse_sudoku(str_input)
            grid_output = parse_sudoku(str_output)
            
            # Ensure the original numbers are unchanged
            for i in range(9):
                for j in range(9):
                    if grid_input[i][j] != 0 and grid_input[i][j] != grid_output[i][j]:
                        return False
            
            # Check rows and columns
            for i in range(9):
                if sorted(grid_output[i]) != list(range(1, 10)):
                    return False
                if sorted([grid_output[j][i] for j in range(9)]) != list(range(1, 10)):
                    return False
            
            # Check 3x3 subgrids
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    subgrid = [
                        grid_output[x][y]
                        for x in range(i, i + 3)
                        for y in range(j, j + 3)
                    ]
                    if sorted(subgrid) != list(range(1, 10)):
                        return False
            
            return True
        
        return is_valid_sudoku_solution(self.get_input(idx), output)
    
    @staticmethod
    def gpt_reply_to_state_represent(reply: str) -> str:
        pattern = r'pos\(\d+,\s*\d+,\s*\d+\).'
        matches = re.findall(pattern, reply)
        res = ' '.join(matches)
        return res
    
    @staticmethod
    def decode_ASP_result(asp_str: str) -> str:            
        lst = SudokuTask._extract_numbers(asp_str)
        arr = SudokuTask._list2array(lst)
        res = ''
        for x in range(9):
            for y in range(9):
                res += str(arr[x][y])
            res += '\n'
        return res
        
    @staticmethod
    def _extract_numbers(s):
        pattern = r'pos\((\d+),\s*(\d+),\s*(\d+)\)'
        matches = re.findall(pattern, s)
        result = []
        for match in matches:
            x, y, n = map(int, match)  # Convert the captured strings to integers
            result.append((x, y, n))            
        return result    
    
    @staticmethod
    def _list2array(num_lst):
        matrix = [[0 for _ in range(9)] for _ in range(9)]
        for x, y, n in num_lst:
            matrix[x-1][y-1] = n            
        return matrix
            
    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        return standard_prompt.format(input=x) + y

    @staticmethod
    def logot_state_represent_prompt_wrap(x: str, y:str='') -> str:
        return logot_state_represent_prompt.format(input=x) + y
    
    @staticmethod
    def decode_standard_prompt_result(gpt_res: str) -> str:
        res = gpt_res.split('%')[-1]
        res = res.strip()
        res = res.replace(' ', '')
        return res