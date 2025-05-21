import re
import os
import sympy
import json
import pandas as pd
from logot.tasks.base import Task, DATA_PATH, SCRIPT_PATH
from logot.prompts.blocksworld import * 

def remove_backtick_lines(text):
    lines = text.splitlines(keepends=True)  # Keep line endings
    filtered_lines = [line for line in lines if not line.startswith('`')]
    return ''.join(filtered_lines)

class BWGoalRecogTask(Task):    
    def __init__(self, 
                 data_file=['goalrecognition.jsonl'],
                 sys_desc_file='system_desc_manual.lp'):
        """
        file: a csv file (fixed)
        """
        super().__init__()
        self.data = []
        self.observations = []
        self.query = []
        self.label = []
        for file in data_file:
            path = os.path.join(DATA_PATH, 'blocksworld', 'goalrecognition', 'blocksworld', file)
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    data = json.loads(line)  # Parse each JSON object
                    self.data.append(data["state"])  # Extract the "state" field
                    self.observations.append(data["observations"])
                    self.query.append(data["query"])
                    self.label.append(data["label"])
        self.sys_desc_file = os.path.join(SCRIPT_PATH, 'blocksworld', 'goalrecognition', sys_desc_file)

    def __len__(self) -> int:
        return len(self.data)    
        
    def get_input(self, idx: int) -> str:
        return self.data[idx], self.observations[idx], self.query[idx]
    
    def get_ASP_command(self) -> str:
        return "echo '{sys_desc} {state_repr}' | clingo 0 --verbose=0 --opt-mode=optN"

    def test_output(self, idx: int, output: str):
        if int(self.label[idx]) == int(output):
            return True
        else:
            return False
    
    @staticmethod
    def gpt_reply_to_state_represent(reply: str) -> str:
        res = remove_backtick_lines(reply)
        return res
    
    @staticmethod
    def decode_ASP_result(asp_str: str) -> str:   
        if 'query_success' in asp_str:
            return True
        else:
            return False
                    
    @staticmethod
    def standard_prompt_wrap(args: tuple) -> str:
        state, obs, query = args
        return standard_prompt_goalrecog.format(state=state, obs=obs, query=query) 

    @staticmethod
    def logot_state_represent_prompt_wrap(args: tuple) -> str:
        state, obs, query = args
        return logot_state_represent_prompt_goalrecog.format(state=state, obs=obs, query=query) 
    
    @staticmethod
    def decode_standard_prompt_result(gpt_res: str) -> str:
        res = gpt_res.split('%')[-1]
        res = res.strip()
        res = res.replace(' ', '').lower()
        if 'true' in res:
            return True
        else:
            return False    
                    
    @staticmethod
    def cot_prompt_wrap(args: tuple) -> str:
        state, obs, query = args
        return cot_prompt_goalrecog.format(state=state, obs=obs, query=query) 
    
    @staticmethod
    def decode_cot_prompt_result(gpt_res: str) -> str:
        res = gpt_res.split(':')[-1]
        res = res.strip()
        res = res.replace(' ', '').lower()
        if 'true' in res:
            return True
        else:
            return False
        
  
class BWProjectionTask(Task):    
    def __init__(self, 
                 data_file=['projection.jsonl'],
                 sys_desc_file='system_desc_manual.lp'):
        """
        file: a csv file (fixed)
        """
        super().__init__()
        self.data = []
        self.act = []
        self.query = []
        self.label = []
        for file in data_file:
            path = os.path.join(DATA_PATH, 'blocksworld', 'projection', 'blocksworld', file)
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    data = json.loads(line)  # Parse each JSON object
                    self.data.append(data["state"])  # Extract the "state" field
                    self.act.append(data["action_sequence"])
                    self.query.append(data["query"])
                    self.label.append(data["label"])
        self.sys_desc_file = os.path.join(SCRIPT_PATH, 'blocksworld', 'projection', sys_desc_file)

    def __len__(self) -> int:
        return len(self.data)    
        
    def get_input(self, idx: int) -> str:
        return self.data[idx], self.act[idx], self.query[idx]

    def test_output(self, idx: int, output):
        if int(self.label[idx]) == int(output):
            return True
        else:
            return False
    
    @staticmethod
    def gpt_reply_to_state_represent(reply: str) -> str:
        res = remove_backtick_lines(reply)
        return res
    
    @staticmethod
    def decode_ASP_result(asp_str: str) -> str:   
        if 'query_success' in asp_str:
            return True
        else:
            return False
                    
    @staticmethod
    def standard_prompt_wrap(args: tuple) -> str:
        state, act, query = args
        return standard_prompt_projection.format(state=state, act=act, query=query) 

    @staticmethod
    def logot_state_represent_prompt_wrap(args: tuple) -> str:
        state, act, query = args
        return logot_state_represent_prompt_projection.format(state=state, act=act, query=query) 
    
    @staticmethod
    def decode_standard_prompt_result(gpt_res: str) -> str:
        res = gpt_res.split('%')[-1]
        res = res.strip()
        res = res.replace(' ', '').lower()
        if 'true' in res:
            return True
        else:
            return False
                    
    @staticmethod
    def cot_prompt_wrap(args: tuple) -> str:
        state, act, query = args
        return cot_prompt_projection.format(state=state, act=act, query=query) 
    
    @staticmethod
    def decode_cot_prompt_result(gpt_res: str) -> str:
        res = gpt_res.split(':')[-1]
        res = res.strip()
        res = res.replace(' ', '').lower()
        if 'true' in res:
            return True
        else:
            return False
      
class BWLegalityTask(Task):    
    def __init__(self, 
                 data_file=['legality.jsonl'],
                 sys_desc_file='system_desc_manual.lp'):
        """
        file: a csv file (fixed)
        """
        super().__init__()
        self.data = []
        self.query = []
        self.label = []
        for file in data_file:
            path = os.path.join(DATA_PATH, 'blocksworld', 'legality', 'blocksworld', file)
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    data = json.loads(line)  # Parse each JSON object
                    self.data.append(data["state"])  # Extract the "state" field
                    self.query.append(data["query"])
                    self.label.append(data["label"])
        self.sys_desc_file = os.path.join(SCRIPT_PATH, 'blocksworld', 'legality', sys_desc_file)

    def __len__(self) -> int:
        return len(self.data)    
        
    def get_input(self, idx: int) -> str:
        return self.data[idx], self.query[idx]

    def test_output(self, idx: int, output):
        if int(self.label[idx]) == int(output):
            return True
        else:
            return False
    
    @staticmethod
    def gpt_reply_to_state_represent(reply: str) -> str:
        res = remove_backtick_lines(reply)
        return res
    
    @staticmethod
    def decode_ASP_result(asp_str: str) -> str:   
        if 'UNSATISFIABLE' in asp_str:
            return False
        elif 'UNKNOWN' in asp_str:
            return False
        else:
            return True
                    
    @staticmethod
    def standard_prompt_wrap(args: tuple) -> str:
        state, query = args
        return standard_prompt_legality.format(state=state, query=query) 

    @staticmethod
    def logot_state_represent_prompt_wrap(args: tuple) -> str:
        state, query = args
        return logot_state_represent_prompt_legality.format(state=state, query=query) 
    
    @staticmethod
    def decode_standard_prompt_result(gpt_res: str) -> str:
        res = gpt_res.split('%')[-1]
        res = res.strip()
        res = res.replace(' ', '').lower()
        if 'true' in res:
            return True
        else:
            return False
                    
    @staticmethod
    def cot_prompt_wrap(args: tuple) -> str:
        state, query = args
        return cot_prompt_legality.format(state=state, query=query) 
    
    @staticmethod
    def decode_cot_prompt_result(gpt_res: str) -> str:
        res = gpt_res.split(':')[-1]
        res = res.strip()
        res = res.replace(' ', '').lower()
        if 'true' in res:
            return True
        else:
            return False
    
  
class BWPlanningTask(Task):    
    def __init__(self, 
                 data_file=['planning.jsonl'],
                 sys_desc_file='system_desc_manual.lp'):
        super().__init__()
        self.data = []
        self.goal = []
        self.query = []
        self.label = []
        for file in data_file:
            path = os.path.join(DATA_PATH, 'blocksworld', 'planning', 'blocksworld', file)
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    data = json.loads(line)  # Parse each JSON object
                    self.data.append(data["state"])  # Extract the "state" field
                    self.goal.append(data["goal"])
                    self.query.append(data["query"])
                    self.label.append(data["label"])
        self.sys_desc_file = os.path.join(SCRIPT_PATH, 'blocksworld', 'planning', sys_desc_file)

    def __len__(self) -> int:
        return len(self.data)    
        
    def get_input(self, idx: int) -> str:
        return self.data[idx], self.goal[idx], self.query[idx]

    def test_output(self, idx: int, output):
        if int(self.label[idx]) == int(output):
            return True
        else:
            return False
    
    @staticmethod
    def gpt_reply_to_state_represent(reply: str) -> str:
        res = remove_backtick_lines(reply)
        return res
    
    @staticmethod
    def decode_ASP_result(asp_str: str) -> str:   
        if 'query_success' in asp_str:
            return True
        else:
            return False
                    
    @staticmethod
    def standard_prompt_wrap(args: tuple) -> str:
        state, goal, query = args
        return standard_prompt_planning.format(state=state, goal=goal, query=query) 

    @staticmethod
    def logot_state_represent_prompt_wrap(args: tuple) -> str:
        state, goal, query = args
        return logot_state_represent_prompt_planning.format(state=state, goal=goal, query=query) 
    
    @staticmethod
    def decode_standard_prompt_result(gpt_res: str) -> str:
        res = gpt_res.split('%')[-1]
        res = res.strip()
        res = res.replace(' ', '').lower()
        if 'true' in res:
            return True
        else:
            return False
                    
    @staticmethod
    def cot_prompt_wrap(args: tuple) -> str:
        state, goal, query = args
        return cot_prompt_planning.format(state=state, goal=goal, query=query) 
    
    @staticmethod
    def decode_cot_prompt_result(gpt_res: str) -> str:
        res = gpt_res.split(':')[-1]
        res = res.strip()
        res = res.replace(' ', '').lower()
        if 'true' in res:
            return True
        else:
            return False
      
