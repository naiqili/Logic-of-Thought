import os
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data')
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), '..', 'scripts')

class Task:
    def __init__(self):
        pass

    def __len__(self) -> int:
        pass

    def get_input(self, idx: int) -> str:
        pass

    def test_output(self, idx: int, output: str):
        pass    
    
    @staticmethod
    def gpt_reply_to_state_represent(reply: str) -> str:
        pass
    
    @staticmethod
    def decode_ASP_result(asp_str: str) -> str:       
        pass
            
    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        pass

    @staticmethod
    def logot_state_represent_prompt_wrap(x: str, y:str='') -> str:
        pass
    
    def get_ASP_command(self) -> str:
        return "echo '{sys_desc} {state_repr}' | clingo 1 --verbose=0"
        
    @staticmethod
    def decode_standard_prompt_result(gpt_res: str) -> str:
        pass
                    
    @staticmethod
    def standard_prompt_wrap(args: tuple) -> str:
        pass
    
    @staticmethod
    def decode_standard_prompt_result(gpt_res: str) -> str:
        pass
                    
    @staticmethod
    def cot_prompt_wrap(args: tuple) -> str:
        pass
    
    @staticmethod
    def decode_cot_prompt_result(gpt_res: str) -> str:
        pass