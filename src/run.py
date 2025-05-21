from functools import partial
from argparse import Namespace
from logot.models import gpt
from logot.methods.solver import solve, solve_standard_prompt, solve_cot_prompt

from logot.tasks.sudoku import SudokuTask
from logot.tasks.hitori import HitoriTask
from logot.tasks.fillomino import FillominoTask
from logot.tasks.blocksworld import BWGoalRecogTask, BWPlanningTask, BWLegalityTask, BWProjectionTask

import argparse

pricing_info = {
    "gpt-4o-mini": {"input": 0.00015, "output": 0.00060},
    "deepseek-chat": {"input": 0.00014, "output": 0.00028},
    "gpt-3.5-turbo": {"input": 0.0015, "output": 0.002},
    "gpt-4o": {"input": 0.005, "output": 0.015},
    "gpt-4-turbo": {"input": 0.01, "output": 0.03}
}

def calculate_gpt_cost(input_tokens: int, output_tokens: int, model: str, pricing: dict) -> float:
    """
    Calculate the cost of a GPT model call.

    Args:
        input_tokens (int): Number of input tokens.
        output_tokens (int): Number of output tokens.
        model (str): Model name.
        pricing (dict): Dictionary with pricing info per 1K tokens
    Returns:
        float: Total cost in USD.
    """
    if model not in pricing:
        raise ValueError(f"Pricing for model '{model}' not found.")
    
    model_pricing = pricing[model]
    input_cost = (input_tokens / 1000) * model_pricing["input"]
    output_cost = (output_tokens / 1000) * model_pricing["output"]
    total_cost = input_cost + output_cost
    
    return round(total_cost, 6)


def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--method', default='logot', 
                        help='logot / standard_prompt / cot')
    parser.add_argument('--task', default='sudoku', 
                        help='sudoku / hitori / fillomino / bwgoalrecg / bwlegality / bwplanning / bwprojection')
    parser.add_argument('--backend', default='deepseek-chat', help='GPT backend. deepseek-chat / ')
    parser.add_argument('--pricing', default=None, help='Model for calculating cost.')
    parser.add_argument('--temperature', type=float, default=0.7, help='GPT temperature.')
    parser.add_argument('--cache_file', default='./tmp/sudoku_cache.h5', help='Cache file for GPT response.')
    parser.add_argument('--verbose', type=int, default=1, help='Output detail level. (0-3)')
    parser.add_argument('--sys_desc_file', default='system_desc_manual.lp', 
                        help='ASP script for system description. system_desc_manual.lp / system_desc_fewshot_in.lp / system_desc_fewshot_out.lp')
    
    args = parser.parse_args()
    
    if args.task == 'sudoku':
        task = SudokuTask(sys_desc_file=args.sys_desc_file)
    elif args.task == 'hitori':
        task = HitoriTask(sys_desc_file=args.sys_desc_file)
    elif args.task == 'fillomino':
        task = FillominoTask(sys_desc_file=args.sys_desc_file)
    elif args.task == 'bwgoalrecg':
        task = BWGoalRecogTask(sys_desc_file=args.sys_desc_file)
    elif args.task == 'bwlegality':
        task = BWLegalityTask(sys_desc_file=args.sys_desc_file)
    elif args.task == 'bwplanning':
        task = BWPlanningTask(sys_desc_file=args.sys_desc_file)
    elif args.task == 'bwprojection':
        task = BWProjectionTask(sys_desc_file=args.sys_desc_file)
    else:
        raise NotImplementedError()
    
    num_correct = 0
    total_cost = 0.0
    pricing = args.pricing
    if pricing is None:
        pricing = args.backend
    print('id, result')
    for IDX in range(len(task)):
        try:
            if args.method == 'logot':
                res, input_tokens, output_tokens = solve(args, task, IDX, args.verbose)
            elif args.method == 'standard_prompt':
                res, input_tokens, output_tokens = solve_standard_prompt(args, task, IDX, args.verbose)
            elif args.method == 'cot':
                res, input_tokens, output_tokens = solve_cot_prompt(args, task, IDX, args.verbose)
            else:               
                raise NotImplementedError(f'{args.method} not implemented.')
            total_cost += calculate_gpt_cost(input_tokens, output_tokens, pricing, pricing_info)
            output = task.test_output(IDX, res)
            print(f'{IDX}, {output}')
            if output:
                num_correct += 1
            if args.verbose >= 2:
                print('Test input:')
                print(task.get_input(IDX))
                print('Test output:')
                print(res)
                print('========================')
        except Exception as e:
            print(f'{IDX}, Failed to solve')
            print('error:', e)
            
    print(f'Result summary: {num_correct} / {len(task)}')
    print('Total cost:', total_cost)
    print('Per cost:', total_cost / len(task))

if __name__ == '__main__':
    main()