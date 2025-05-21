import os
import openai
import backoff 
import hashlib
import pandas as pd

completion_tokens = prompt_tokens = 0

api_key = os.getenv("OPENAI_API_KEY", "")
if api_key != "":
    openai.api_key = api_key
else:
    print("Warning: OPENAI_API_KEY is not set")
    
api_base = os.getenv("OPENAI_API_BASE", "")
if api_base != "":
    print("OPENAI_API_BASE is set to {}".format(api_base))
    openai.api_base = api_base
    

# Function to generate SHA-256 hash
def generate_hash(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

# Function to store hash-content pair in HDF5
def store_hash_content(hash_code, content, file_path, table_name):
    with pd.HDFStore(file_path, mode='a') as store:
        try:
            df = store.get(table_name)  # Load existing data
        except KeyError:
            df = pd.DataFrame(columns=['hash', 'content'])  # Create new DataFrame if not exists

        if hash_code not in df['hash'].values:
            new_entry = pd.DataFrame({'hash': [hash_code], 'content': [content]})
            df = pd.concat([df, new_entry], ignore_index=True)
            store.put(table_name, df, format='table', data_columns=True)


def completions(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

def gpt(prompt, model="deepseek-chat", temperature=0.7, max_tokens=8000, n=1, stop=None,
        verbose=0, cache_file=None) -> list:
    '''
    When cache_file is not None, it first tries to lookup results in a hash table.
    '''
    if cache_file is None:
        messages = [{"role": "user", "content": prompt}]
        return chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop,
                    verbose=verbose)
    else:
        table_name = f'/hash_table/{model}'
        hash_code = generate_hash(prompt)
        if not os.path.exists(cache_file):
            with pd.HDFStore(cache_file, mode='w') as store:
                df = pd.DataFrame(columns=['hash', 'content']) 
                store.put(table_name, df, format='table', data_columns=True)
        with pd.HDFStore(cache_file, mode='r') as store:
            # print(store.keys())
            if table_name in store.keys():
                df = store.get(table_name)
            else:
                df = pd.DataFrame(columns=['hash', 'content'])                 
        result = df[df['hash'] == hash_code]['content']
        if not result.empty:
            if verbose >= 1:
                print('Retrive result from cache')
            return result.values[0]
        else:
            messages = [{"role": "user", "content": prompt}]
            res = chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop,
                        verbose=verbose)
            store_hash_content(hash_code, res, cache_file, table_name)
            if verbose >= 1:
                print('Save result to cache')
            return res

def chatgpt(messages, model="deepseek-chat", temperature=0.7, max_tokens=1000, n=1, stop=None, verbose=0) -> list:
    global completion_tokens, prompt_tokens
    outputs = []
    res = completions(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens, 
                      n=n, stop=stop)
    if verbose >= 3:
        print('==========GPT==========')
        print('message:\n', messages)
        print('reply:\n', res)
    outputs.extend([choice.message.content for choice in res.choices])
    # log completion tokens
    completion_tokens += res.usage.completion_tokens
    prompt_tokens += res.usage.prompt_tokens
    return outputs[0]
    
def gpt_usage(backend="deepseek-chat"):
    global completion_tokens, prompt_tokens
    if backend == "gpt-4":
        cost = completion_tokens / 1000 * 0.06 + prompt_tokens / 1000 * 0.03
    elif backend == "gpt-3.5-turbo":
        cost = completion_tokens / 1000 * 0.002 + prompt_tokens / 1000 * 0.0015
    elif backend == "gpt-4o":
        cost = completion_tokens / 1000 * 0.00250 + prompt_tokens / 1000 * 0.01
    elif backend == "deepseek-chat":
        cost = 0 # TODO
    elif backend == "deepseek-reasoner":
        cost = 0 # TODO
    return {"completion_tokens": completion_tokens, "prompt_tokens": prompt_tokens, "cost": cost}
