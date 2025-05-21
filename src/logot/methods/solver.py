import itertools
import os
import numpy as np
from functools import partial
from logot.models import gpt
from logot.tasks.base import Task
import tiktoken

def get_tokens(s: str, model: str = "gpt-3.5-turbo") -> int:
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(s)
    return len(tokens)


def solve(args, task: Task, idx, verbose=0):
    global gpt
    gpt = partial(gpt, model=args.backend, temperature=args.temperature,
                  verbose=verbose, cache_file=args.cache_file)

    x = task.get_input(idx)
    logot_prompt = task.logot_state_represent_prompt_wrap(x)
    gpt_res = gpt(logot_prompt)
    state_repr = task.gpt_reply_to_state_represent(gpt_res)
    with open(task.sys_desc_file, 'r') as f:
        sys_desc = f.read()
    
    # asp_output = os.popen(f"echo '{sys_desc} {state_repr}' | clingo 1 --verbose=0").read()
    cmd = task.get_ASP_command().format(sys_desc=sys_desc, state_repr=state_repr)
    asp_output = os.popen(cmd).read()

    res = task.decode_ASP_result(asp_output)
    if verbose >= 3:
        print('========DEBUGGING IN SOLVE========')
        for v in ['x', 'logot_prompt', 'gpt_res', 'sys_desc', 'state_repr']:
            print(v)
            print(eval(v))
        print('==================================')
    input_tokens = get_tokens(logot_prompt)
    output_tokens = get_tokens(gpt_res)
    return res, input_tokens, output_tokens



def solve_standard_prompt(args, task: Task, idx, verbose=0):
    global gpt
    gpt = partial(gpt, model=args.backend, temperature=args.temperature,
                  verbose=verbose, cache_file=args.cache_file)

    x = task.get_input(idx)
    prompt = task.standard_prompt_wrap(x)
    gpt_res = gpt(prompt)
    res = task.decode_standard_prompt_result(gpt_res)
    if verbose >= 3:
        print('========DEBUGGING IN SOLVE========')
        for v in ['x', 'prompt', 'gpt_res']:
            print(v)
            print(eval(v))
        print('==================================')
    input_tokens = get_tokens(prompt)
    output_tokens = get_tokens(gpt_res)
    return res, input_tokens, output_tokens

def solve_cot_prompt(args, task: Task, idx, verbose=0):
    global gpt
    gpt = partial(gpt, model=args.backend, temperature=args.temperature,
                  verbose=verbose, cache_file=args.cache_file)

    x = task.get_input(idx)
    prompt = task.cot_prompt_wrap(x)
    gpt_res = gpt(prompt)
    res = task.decode_cot_prompt_result(gpt_res)
    if verbose >= 3:
        print('========DEBUGGING IN SOLVE========')
        for v in ['x', 'prompt', 'gpt_res']:
            print(v)
            print(eval(v))
        print('==================================')
    input_tokens = get_tokens(prompt)
    output_tokens = get_tokens(gpt_res)
    return res, input_tokens, output_tokens