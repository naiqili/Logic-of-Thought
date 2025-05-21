import re
import os
import sympy
import json
import pandas as pd
from logot.tasks.base import Task, DATA_PATH, SCRIPT_PATH
from logot.prompts.fillomino import * 
from collections import deque

class FillominoTask(Task):
    """
    Input (x)   : a string of fillomino puzzle
    Output (y)  : a string of fillomino answer
    Reward (r)  : 0 or 1, depending on whether the result is correct
    Input Example: 
        4003003310200040344001003
    Output Example: 
        4443343313223443344131333
    """
    def __init__(self, 
                 data_file='fillomino.json',
                 sys_desc_file='system_desc_manual.lp'):
        super().__init__()
        path = os.path.join(DATA_PATH, 'fillomino', data_file)
        self.data_path = path
        self.question = []
        self.answer = []        
        self.sizen = []
        with open(self.data_path, 'r') as file:
            data = json.load(file)
        for key, val in data.items():
            self.question.append(val['question'])
            self.answer.append(val['answer'])
            self.sizen.append(val['size'])
        self.sys_desc_file = os.path.join(SCRIPT_PATH, 'fillomino', sys_desc_file)

    def __len__(self) -> int:
        return len(self.question)
    
    @staticmethod
    def str2grid(s: str, n: int) -> str:
        res = '\n'.join(s[i:i+n] for i in range(0, len(s), n))
        return res
        
    def get_input(self, idx: int) -> str:
        q_str = self.question[idx]
        n = self.sizen[idx]
        res = f'{n}\n'
        res += self.str2grid(q_str, n)
        return res

    def test_output(self, idx: int, output: str):
        def is_valid_fillomino(grid):
            if not grid or not grid[0]:
                return False

            rows, cols = len(grid), len(grid[0])
            visited = [[False for _ in range(cols)] for _ in range(rows)]

            def bfs(r, c):
                num = grid[r][c]
                queue = deque([(r, c)])
                visited[r][c] = True
                region = [(r, c)]

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                            if grid[nx][ny] == num:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                region.append((nx, ny))
                return region

            for i in range(rows):
                for j in range(cols):
                    if not visited[i][j]:
                        region = bfs(i, j)
                        if len(region) != grid[i][j]:
                            print(f"Region with number {grid[i][j]} at ({i},{j}) has size {len(region)}")
                            return False

                        # Check for same-sized neighbors
                        for x, y in region:
                            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nx, ny = x + dx, y + dy
                                if (nx, ny) not in region and 0 <= nx < rows and 0 <= ny < cols:
                                    if grid[nx][ny] == grid[x][y]:
                                        print(f"Adjacent regions with same number {grid[x][y]} at ({x},{y}) and ({nx},{ny})")
                                        return False
            return True
        def string_to_grid(s, n):
            rows = cols = n
            grid = [[int(s[i * cols + j]) for j in range(cols)] for i in range(rows)]
            return grid
        _n = self.sizen[idx]
        q_str = self.question[idx]
        q_arr =  string_to_grid(q_str, _n)
        out_str = output.replace('\n', '')
        out_arr = string_to_grid(out_str, _n)
        for i in range(_n):
            for j in range(_n):
                if q_arr[i][j] != 0 and q_arr[i][j] != out_arr[i][j]:
                    return False
        if not is_valid_fillomino(out_arr):
            return False
        return True
    
    @staticmethod
    def gpt_reply_to_state_represent(reply: str) -> str:
        res = reply
        return res
    
    @staticmethod
    def decode_ASP_result(asp_str: str) -> str:    
        lst = FillominoTask._extract_black(asp_str)
        _n = FillominoTask._extract_board_size(asp_str)
        arr = FillominoTask._list2array(lst, _n)
        res = ''
        for x in range(_n):
            for y in range(_n):
                res += str(arr[x][y])
            res += '\n'
        return res
        
    @staticmethod
    def _extract_black(s):
        pattern = r'pos\((\d+),\s*(\d+),\s*(\d+)\)'
        matches = re.findall(pattern, s)
        result = []
        for match in matches:
            x, y, n = map(int, match)  # Convert the captured strings to integers
            result.append((x, y, n))            
        return result    
    
    @staticmethod
    def _extract_board_size(s):
        pattern = r'board_size\((\d+)\)'
        matches = re.findall(pattern, s)
        result = int(matches[0])           
        return result    
    
    @staticmethod
    def _list2array(num_lst, _n):
        matrix = [[0 for _ in range(_n)] for _ in range(_n)]
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
    
