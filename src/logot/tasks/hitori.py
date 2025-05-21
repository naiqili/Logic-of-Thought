import re
import os
import sympy
import json
import pandas as pd
from logot.tasks.base import Task, DATA_PATH, SCRIPT_PATH
from logot.prompts.hitori import * 


class HitoriTask(Task):
    """
    Input (x)   : a string of hitori puzzle
    Output (y)  : a string of hitori answer
    Reward (r)  : 0 or 1, depending on whether the result is correct
    Input Example: 
        2132445322342511433225143
    Output Example: 
        bwbwwwwwbwwbwwwwwbwbwbwww
    """
    def __init__(self, 
                 data_file='hitori.json',
                 sys_desc_file='system_desc_manual.lp'):
        super().__init__()
        path = os.path.join(DATA_PATH, 'hitori', data_file)
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
        self.sys_desc_file = os.path.join(SCRIPT_PATH, 'hitori', sys_desc_file)

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
        gt = self.answer[idx]
        out = output.replace('\n', '')
        return gt==out
    
    @staticmethod
    def gpt_reply_to_state_represent(reply: str) -> str:
        res = reply
        return res
    
    @staticmethod
    def decode_ASP_result(asp_str: str) -> str:    
        lst = HitoriTask._extract_black(asp_str)
        _n = HitoriTask._extract_board_size(asp_str)
        arr = HitoriTask._list2array(lst, _n)
        res = ''
        for x in range(_n):
            for y in range(_n):
                res += str(arr[x][y])
            res += '\n'
        return res
        
    @staticmethod
    def _extract_black(s):
        pattern = r'black\((\d+),\s*(\d+)\)'
        matches = re.findall(pattern, s)
        result = []
        for match in matches:
            x, y = map(int, match)  # Convert the captured strings to integers
            result.append((x, y))            
        return result    
    
    @staticmethod
    def _extract_board_size(s):
        pattern = r'board_size\((\d+)\)'
        matches = re.findall(pattern, s)
        result = int(matches[0])           
        return result    
    
    @staticmethod
    def _list2array(num_lst, _n):
        matrix = [['w' for _ in range(_n)] for _ in range(_n)]
        for x, y in num_lst:
            matrix[x-1][y-1] = 'b'
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
    
