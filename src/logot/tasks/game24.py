import re
import os
import sympy
import pandas as pd
from logot.tasks.base import Task, DATA_PATH, SCRIPT_PATH
from logot.prompts.game24 import * 


class Game24Task(Task):    
    def __init__(self, 
                 data_file='24.csv',
                 sys_desc_file='system_desc_manual.lp'):
        """
        file: a csv file (fixed)
        """
        super().__init__()
        path = os.path.join(DATA_PATH, 'game24', data_file)
        self.data_path = path
        self.data = list(pd.read_csv(path)['Puzzles'])
        self.sys_desc_file = os.path.join(SCRIPT_PATH, 'game24', sys_desc_file)

    def __len__(self) -> int:
        return len(self.data)    
        
    def get_input(self, idx: int) -> str:
        res = self.data[idx]
        return res

    def test_output(self, idx: int, output: str):
        if 'UNSATISFIABLE' in output:
            return False
        if 'UNKNOWN' in output:
            return False
        pattern = r'\(\d+,\s*\d+,\s*24\),3' 
        matches = re.findall(pattern, output)
        if len(matches) > 0:
            return True
        else:
            return False
    
    @staticmethod
    def gpt_reply_to_state_represent(reply: str) -> str:
        pattern = r'holds\(pos\(\d+,\s*\d+\),\s*\d+\).' # e.g. holds(pos(1,7),0).
        matches = re.findall(pattern, reply)
        res = ' '.join(matches)
        return res
    
    @staticmethod
    def decode_ASP_result(asp_str: str) -> str:   
        return asp_str
                    
    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        return standard_prompt.format(input=x) + y

    @staticmethod
    def logot_state_represent_prompt_wrap(x: str, y:str='') -> str:
        return logot_state_represent_prompt.format(input=x) + y
    
    
