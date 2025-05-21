# export OPENAI_API_KEY='sk-xxx'
# export OPENAI_API_BASE='https://api.deepseek.com'

export OPENAI_API_KEY='sk-xxx'
export OPENAI_API_BASE='https://api.gptsapi.net/v1'

# Test scripts for logot

# sudoku
python run.py --task sudoku --backend deepseek-chat --cache_file './tmp/sudoku_cache.h5' --verbose 3 --sys_desc_file 'system_desc_fewshot_out.lp' > ./log/sudoku_deepseek-chat.log

# hitori
# python run.py --task hitori --backend deepseek-chat --cache_file './tmp/hitori_cache.h5' --verbose 2 --sys_desc_file 'system_desc_fewshot_out.lp' --pricing gpt-4o-mini # > ./log/hitori_deepseek-chat.log

# fillomino
# python run.py --task fillomino --backend deepseek-chat --cache_file './tmp/fillomino_cache.h5' --verbose 2 --sys_desc_file 'system_desc_fewshot_out.lp' # > ./log/fillomino_deepseek-chat.log

# blocks world - goal recognition
# python run.py --task bwgoalrecg --backend deepseek-chat --cache_file './tmp/bwgoalrecg_gpt_cache.h5' --verbose 2 --sys_desc_file 'system_desc_fewshot_out.lp' # > ./log/bwgoalrecg_deepseek-chat.log
# python run.py --task bwgoalrecg --backend gpt-4o-mini --cache_file './tmp/bwgoalrecg_gpt_cache.h5' --verbose 3 --sys_desc_file 'system_desc_fewshot_out.lp' # > ./log/bwgoalrecg_gpt-4o-mini.log
# python run.py --task bwgoalrecg --backend gpt-4o --cache_file './tmp/bwgoalrecg_gpt-4o_cache.h5' --verbose 3 --sys_desc_file 'system_desc_fewshot_out.lp' # > ./log/bwgoalrecg_gpt-4o.log

# blocks world - legality
# python run.py --task bwlegality --backend deepseek-chat --cache_file './tmp/bwlegality_cache.h5' --verbose 3 --sys_desc_file 'system_desc_fewshot_out.lp' > ./log/bwlegality_deepseek-chat.log
# python run.py --task bwlegality --backend gpt-4o-mini --cache_file './tmp/bwlegality_gpt_cache.h5' --verbose 3 --sys_desc_file 'system_desc_fewshot_out.lp' # > ./log/bwlegality_gpt-4o-mini.log

# blocks world - planning
# python run.py --task bwplanning --backend deepseek-chat --cache_file './tmp/bwplanning_cache.h5' --verbose 2 --sys_desc_file 'system_desc_fewshot_out.lp' > ./log/bwplanning_deepseek-chat.log
# python run.py --task bwplanning --backend gpt-4o-mini --cache_file './tmp/bwplanning_gpt_cache.h5' --verbose 3 --sys_desc_file 'system_desc_fewshot_out.lp' # > ./log/bwplanning_gpt-4o-mini.log

# blocks world - projection
# python run.py --task bwprojection --backend deepseek-chat --cache_file './tmp/bwprojection_cache.h5' --verbose 2 --sys_desc_file 'system_desc_fewshot_out.lp' > ./log/bwprojection_deepseek-chat.log
# python run.py --task bwprojection --backend gpt-4o-mini --cache_file './tmp/bwprojection_gpt_cache.h5' --verbose 3 --sys_desc_file 'system_desc_fewshot_out.lp' # > ./log/bwprojection_gpt-4o-mini.log
# python run.py --task bwprojection --backend gpt-4o --cache_file './tmp/bwprojection_gpt-4o_cache.h5' --verbose 3 --sys_desc_file 'system_desc_fewshot_out.lp' # > ./log/bwprojection_gpt-4o.log

# Test scripts for standard_prompt

# sudoku
# python run.py --method standard_prompt --task sudoku --backend deepseek-chat --cache_file './tmp/sudoku_standard_prompt_cache.h5' --verbose 2 # > ./log/sudoku_standard_prompt_deepseek-chat.log

# hitori
# python run.py --method standard_prompt --task hitori --backend deepseek-chat --cache_file './tmp/hitori_standard_prompt_cache.h5' --verbose 2 # > ./log/hitori_standard_prompt_deepseek-chat.log

# fillomino
# python run.py --method standard_prompt --task fillomino --backend deepseek-chat --cache_file './tmp/fillomino_standard_prompt_cache.h5' --verbose 2 # > ./log/fillomino_standard_prompt_deepseek-chat.log

# blocks world - goal recognition
# python run.py --method standard_prompt --task bwgoalrecg --backend deepseek-chat --cache_file './tmp/bwgoalrecg_standard_prompt_cache.h5' --verbose 2 # > ./log/bwgoalrecg_standard_prompt_deepseek-chat.log
# python run.py --method standard_prompt --task bwgoalrecg --backend gpt-4o-mini --cache_file './tmp/bwgoalrecg_standard_prompt_gpt-4o-mini_cache.h5' --verbose 2 # > ./log/bwgoalrecg_standard_prompt_gpt-4o-mini.log

# blocks world - legality
# python run.py --method standard_prompt --task bwlegality --backend deepseek-chat --cache_file './tmp/bwlegality_standard_prompt_cache.h5' --verbose 2 # > ./log/bwlegality_standard_prompt_deepseek-chat.log
# python run.py --method standard_prompt --task bwlegality --backend gpt-4o-mini --cache_file './tmp/bwlegality_standard_prompt_gpt-4o-mini_cache.h5' --verbose 2 # > ./log/bwlegality_standard_prompt_gpt-4o-mini.log


# blocks world - planning
# python run.py --method standard_prompt --task bwplanning --backend deepseek-chat --cache_file './tmp/bwplanning_standard_prompt_cache.h5' --verbose 2 # > ./log/bwplanning_standard_prompt_deepseek-chat.log
# python run.py --method standard_prompt --task bwplanning --backend gpt-4o-mini --cache_file './tmp/bwplanning_standard_prompt_gpt-4o-mini_cache.h5' --verbose 2 # > ./log/bwplanning_standard_prompt_gpt-4o-mini.log


# blocks world - projection
# python run.py --method standard_prompt --task bwprojection --backend deepseek-chat --cache_file './tmp/bwprojection_standard_prompt_cache.h5' --verbose 2 # > ./log/bwprojection_standard_prompt_deepseek-chat.log
# python run.py --method standard_prompt --task bwprojection --backend gpt-4o-mini --cache_file './tmp/bwprojection_standard_prompt_gpt-4o-mini_cache.h5' --verbose 2 # > ./log/bwprojection_standard_prompt_gpt-4o-mini.log



# Test scripts for cot

# blocks world - goal recognition
# python run.py --method cot --task bwgoalrecg --backend deepseek-chat --cache_file './tmp/bwgoalrecg_cot_cache.h5' --verbose 3 # > ./log/bwgoalrecg_cot_deepseek-chat.log

# blocks world - legality
# python run.py --method cot --task bwlegality --backend deepseek-chat --cache_file './tmp/bwlegality_cot_cache.h5' --verbose 3 # > ./log/bwlegality_cot_deepseek-chat.log

# blocks world - planning
# python run.py --method cot --task bwplanning --backend deepseek-chat --cache_file './tmp/bwplanning_cot_cache.h5' --verbose 3 # > ./log/bwplanning_cot_deepseek-chat.log

# blocks world - projection
# python run.py --method cot --task bwprojection --backend deepseek-chat --cache_file './tmp/bwprojection_cot_cache.h5' --verbose 3 # > ./log/bwprojection_cot_deepseek-chat.log