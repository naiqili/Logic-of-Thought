# Goal Recognition
logot_state_represent_prompt_goalrecog = '''\
State Input:
The tan block is on the table. The black block is on the table. The aquamarine block is on the table. The brown block is clear. The green block is clear. The aquamarine block is clear. The brown block is on the table. The green block is on the table. The tan block is clear. The black block is clear.
Observation Input:
Jane moves the aquamarine block from the table to the green block.
Query Input:
The aquamarine block is on top of the green block. The aquamarine block is not on top of the black block.
% State Encoding:
holds(on(tan, table), 0).
holds(on(black, table), 0).
holds(on(aquamarine, table), 0).
holds(clear(brown), 0).
holds(clear(green), 0).
holds(clear(aquamarine), 0).
holds(on(brown, table), 0).
holds(on(green, table), 0).
holds(clear(tan), 0).
holds(clear(black), 0).
% All Blocks:
block(tan). block(black). block(aquamarine). block(brown). block(green).
% Observation Encoding:
query_success :-
    occurs(move(aquamarine, table, green), 0).
:- not query_success.
% Query Encoding:
goal(I) :-
    holds(on(aquamarine, green), I).
    -holds(on(aquamarine, black), I).
    
State Input:
The tan block is on the table. The white block is clear. The white block is on the table. The brown block is clear. The orange block is clear. The green block is clear. The brown block is on the table. The orange block is on the table. The green block is on the table. The tan block is clear.
Observation Input:
Jane moves the white block from the table to the brown block. Jane moves the white block from the brown block onto the table. Jane moves the brown block from the table to the white block.
Query Input:
The brown block is on top of the green block. The orange block is not on top of the tan block.
% State Encoding:
holds(on(tan, table), 0).
holds(clear(white), 0).
holds(on(white, table), 0).
holds(clear(brown), 0).
holds(clear(orange), 0).
holds(clear(green), 0).
holds(on(brown, table), 0).
holds(on(orange, table), 0).
holds(on(green, table), 0).
holds(clear(tan), 0).
% All Blocks:
block(tan). block(white). block(brown). block(orange). block(green).
% Observation Encoding:
query_success :-
    occurs(move(white, table, brown), 0),
    occurs(move(white, brown, table), 1),
    occurs(move(brown, table, white), 2).
% Query Encoding:
goal(I) :-
    holds(on(brown, green), I),
    -holds(on(orange, tan), I).
    
State Input:
The cyan block is on top of the aquamarine block. The gray block is on top of the cyan block. The turquoise block is on the table. The gray block is clear. The orange block is clear. The aquamarine block is on top of the turquoise block. The orange block is on the table.
Observation Input:
Jane moves the gray block from the cyan block onto the table. Jane moves the cyan block from the aquamarine block onto the table.
Query Input:
the turquoise block is not on the table and the gray block is not on top of the turquoise block
% State Encoding:
holds(on(cyan, aquamarine), 0).
holds(on(gray, cyan), 0).
holds(on(turquoise, table), 0).
holds(clear(gray), 0).
holds(clear(orange), 0).
holds(on(aquamarine, turquoise), 0).
holds(on(orange, table), 0).
% All Blocks:
block(cyan). block(aquamarine). block(gray). block(turquoise). block(orange).
% Observation Encoding:
query_success :-
    occurs(move(gray, cyan, table), 0),
    occurs(move(cyan, aquamarine, table), 1).
% Query Encoding:
goal(I) :-
    -holds(on(turquoise, table), I),
    -holds(on(gray, turquoise), I).    
    
State Input:
The pink block is on top of the magenta block. The tan block is on the table. The pink block is clear. The aquamarine block is on top of the tan block. The red block is on top of the aquamarine block. The magenta block is on the table. The red block is clear.
Observation Input:
Jane moves the red block from the aquamarine block onto the table.
Query Input:
the aquamarine block is on the table and the magenta block is on top of the tan block
% State Encoding:
holds(on(pink, magenta), 0).
holds(on(tan, table), 0).
holds(clear(pink), 0).
holds(on(aquamarine, tan), 0).
holds(on(red, aquamarine), 0).
holds(on(magenta, table), 0).
holds(clear(red), 0).
% All Blocks:
block(pink). block(magenta). block(tan). block(aquamarine). block(red).
% Observation Encoding:
query_success :-
    occurs(move(red, aquamarine, table), 0).
% Query Encoding:
goal(I) :-
    holds(on(aquamarine, table), I),
    holds(on(magenta, tan), I).
    
State Input:
{state}
Observation Input:
{obs}
Query Input:
{query}

Complete the text, output % State Encoding, % All Blocks, % Observation Encoding, % Query Encoding.
Only show the result, do not explain.
'''

standard_prompt_goalrecog = '''\
You are given a description of a blocks world scenario and a goal-recognition task.

Rules of the Domain:
1. Blocks can be stacked on each other or placed on the table.
2. Only clear blocks (with nothing on top) can be moved.
3. The table has infinite space.

Input:
- state: A description of the initial positions of all blocks.
- observations: A sequence of actions taken (e.g., moving blocks).
- query: A goal description.

Your task is to determine whether the given observations could be a prefix of any optimal plan to achieve the described goal starting from the given state.

Format your answer starting with % followed by either True or False, based on whether the goal can be the agent’s objective given the observations.

Example Input:
state: 
The navy block is on top of the blue block. The gray block is on top of the navy block. The blue block is on the table. The indigo block is clear. The indigo block is on the table. The white block is clear. The white block is on the table. The gray block is clear.

observations:
Jane moves the gray block from the navy block onto the table. Jane moves the navy block from the blue block onto the table.

query: 
the white block is not on the table and the blue block is on top of the gray block

Your Answer:
%
True

The new input is as follows:
Input:
state: 
{state}

observations:
{obs}

query: 
{query}

Keep the answer short. Only show the result.
'''

cot_prompt_goalrecog = '''\
Given:
- An initial state describing the positions and properties of blocks.
- A sequence of observed actions.
- A goal query in the form of a partial or complete final configuration.
Your task is to determine if the sequence of actions is consistent with an optimal plan toward achieving the queried goal.

Step-by-step reasoning:

Step 1: Parse the initial state and reconstruct the block configuration (what is on what, what is clear, what is on the table).

Step 2: Apply each observed action sequentially to update the world state.

Step 3: After all actions, check if the resulting state is consistent with a prefix of any optimal plan toward the queried goal. Consider whether achieving the goal from the current state (after observed actions) would involve unnecessary steps or if a more efficient path could have been followed.

Step 4: If the observed actions could be part of an optimal plan that leads to the queried goal, output “True”; otherwise, “False”.

Now let’s work through an example:

Input:
state: 
The navy block is on top of the blue block. The gray block is on top of the navy block. The blue block is on the table. The indigo block is clear. The indigo block is on the table. The white block is clear. The white block is on the table. The gray block is clear.
observations:
Jane moves the gray block from the navy block onto the table. Jane moves the navy block from the blue block onto the table.
query: 
the white block is not on the table and the blue block is on top of the gray block

Step 1: Initial state reconstruction:
- blue is on the table, navy is on blue, gray is on navy → forming a tower: gray → navy → blue → table
- gray is clear
- indigo and white are both clear and on the table

Step 2: Apply observations:
1) gray is moved from navy to table → now navy is clear; gray is on table
2) navy is moved from blue to table → now blue is clear; navy is on table

New configuration:
- blue is on table and clear
- gray is on table and clear
- navy is on table and clear
- indigo is clear on table
- white is clear on table

Step 3: Query: “white block is not on the table” → this is not satisfied, since no move involved white
“blue block is on top of the gray block” → this is also not satisfied; blue and gray are on the table

Thus, the actions cannot be a prefix of an optimal plan to achieve this query.

%  
False


The new input is as follows:
Input:
state: 
{state}

observations:
{obs}

query: 
{query}


Use the same step-by-step reasoning to get the result.    
'''

# Projection
logot_state_represent_prompt_projection = '''\
State Input:
The tan block is on the table. The violet block is clear. The black block is on top of the teal block. The indigo block is on the table. The violet block is on top of the indigo block. The teal block is on the table. The tan block is clear. The black block is clear.
Action Sequence Input:
Jane moves the violet block from the indigo block to the tan block.
Query Input:
The violet block is not clear. The indigo block is on top of the black block.
% State Encoding:
holds(on(tan, table), 0).
holds(clear(violet), 0).
holds(on(black, teal), 0).
holds(on(indigo, table), 0).
holds(on(violet, indigo), 0).
holds(on(teal, table), 0).
holds(clear(tan), 0).
holds(clear(black), 0).
% All Blocks:
block(tan). block(violet). block(black). block(teal). block(indigo).
% Action Sequence Encoding:
occurs(move(violet, indigo, tan), 0).
#const num_step=1.
% Query Encoding:
query_success :-
    -holds(clear(violet), num_step), 
    holds(on(indigo, black), num_step).

State Input:
The tan block is on the table. The black block is on the table. The aquamarine block is on the table. The brown block is clear. The green block is clear. The aquamarine block is clear. The brown block is on the table. The green block is on the table. The tan block is clear. The black block is clear.
Action Sequence Input:
Jane moves the aquamarine block from the table to the green block.
Query Input:
The aquamarine block is on top of the green block. The aquamarine block is not on top of the black block.
% State Encoding:
holds(on(tan, table), 0).
holds(on(black, table), 0).
holds(on(aquamarine, table), 0).
holds(clear(brown), 0).
holds(clear(green), 0).
holds(clear(aquamarine), 0).
holds(on(brown, table), 0).
holds(on(green, table), 0).
holds(clear(tan), 0).
holds(clear(black), 0).
% All Blocks:
block(tan). block(black). block(aquamarine). block(brown). block(green).
% Action Sequence Encoding:
occurs(move(aquamarine, table, green), 0).
#const num_step=1.
% Query Encoding:
query_success :-
    holds(on(aquamarine, green), num_step).
    -holds(on(aquamarine, black), num_step).
    
State Input:
The tan block is on the table. The white block is clear. The white block is on the table. The brown block is clear. The orange block is clear. The green block is clear. The brown block is on the table. The orange block is on the table. The green block is on the table. The tan block is clear.
Action Sequence Input:
Jane moves the white block from the table to the brown block. Jane moves the white block from the brown block onto the table. Jane moves the brown block from the table to the white block.
Query Input:
The brown block is on top of the green block. The orange block is not on top of the tan block.
% State Encoding:
holds(on(tan, table), 0).
holds(clear(white), 0).
holds(on(white, table), 0).
holds(clear(brown), 0).
holds(clear(orange), 0).
holds(clear(green), 0).
holds(on(brown, table), 0).
holds(on(orange, table), 0).
holds(on(green, table), 0).
holds(clear(tan), 0).
% All Blocks:
block(tan). block(white). block(brown). block(orange). block(green).
% Action Sequence Encoding:
occurs(move(white, table, brown), 0).
occurs(move(white, brown, table), 1).
occurs(move(brown, table, white), 2).
#const num_step=3.
% Query Encoding:
query_success :-
    holds(on(brown, green), num_step),
    -holds(on(orange, tan), num_step).

State Input:
The lime block is on top of the aquamarine block. The olive block is clear. The lime block is clear. The teal block is on the table. The olive block is on the table. The navy block is on top of the teal block. The navy block is clear. The aquamarine block is on the table.
Action Sequence Input:
Jane moves the navy block from the teal block to the lime block. Jane moves the navy block from the lime block onto the table. Jane moves the lime block from the aquamarine block to the navy block.
Query Input:
The navy block is not on top of the olive block. The teal block is on top of the navy block.
% State Encoding:
holds(on(lime, aquamarine), 0).
holds(clear(olive), 0).
holds(clear(lime), 0).
holds(on(teal, table), 0).
holds(on(olive, table), 0).
holds(on(navy, teal), 0).
holds(clear(navy), 0).
holds(on(aquamarine, table), 0).
% All Blocks:
block(lime). block(olive). block(teal). block(navy). block(aquamarine).
% Action Sequence Encoding:
occurs(move(navy, teal, lime), 0).
occurs(move(navy, lime, table), 1).
occurs(move(lime, aquamarine, navy), 2).
#const num_step=3.
% Query Encoding:
query_success :-
    -holds(on(navy, olive), num_step),
    holds(on(teal, navy), num_step).

State Input:
{state}
Action Sequence Input:
{act}
Query Input:
{query}

Complete the text, output % State Encoding, % All Blocks, % Action Sequence Encoding, % Query Encoding.
Only show the result, do not explain.
'''

standard_prompt_projection = '''\
You are given a block world scenario. Blocks can be stacked or placed on the table. A block is clear if no block is on top of it. You will be given:

1. An initial state describing the positions and clarity of blocks.
2. A sequence of actions (one or more) where a person moves a block.
3. A query, consisting of one or more propositions about the final state.

Your task is to determine whether each query proposition is True or False after the action sequence is performed.

Input Example:

state:
The red block is on the table. The tan block is on the table. The maroon block is on top of the teal block. The teal block is on top of the cyan block. The maroon block is clear. The red block is clear. The cyan block is on the table. The tan block is clear.

action_sequence:
Jane moves the tan block from the table to the maroon block.

query:
The red block is not on the table. The red block is not on top of the tan block.

Respond with:

%
True

or

%
False

The new input is as follows:
Input:
state: 
{state}

action_sequence:
{act}

query: 
{query}

Keep the answer short. Only show the result.
'''

cot_prompt_projection = '''\


You are solving a puzzle in a Blocks World domain with these rules:

 The table has infinite space.
 Blocks are of identical size and can be stacked.
 A block can be moved only if it is clear (nothing on top of it).
 A block can only be placed on the table or on another block that is clear.
 Only one block can be moved at a time.

You are given:

 an initial state describing the positions and clear status of each block,
 a sequence of actions, each moving a block from one place to another,
 and a query, which is a proposition about the final world state.

Your task is to determine if the query will be true or false after executing the action sequence. Follow these steps:

Step 1: Parse the initial state
Record where each block is and whether it is clear.

Step 2: Apply the action sequence
For each action: Check if the source block is clear.
 Check if the destination (another block or the table) is clear (if not the table).
 Update the world state accordingly.

Step 3: Evaluate the query
After all actions, assess whether the proposition described in the query is true.

Step 4: Output the result
If the query holds in the final state, write:

Final output:
True

Otherwise, write:

Final output:
False

Example:

state:
The red block is on the table. The tan block is on the table. The maroon block is on top of the teal block. The teal block is on top of the cyan block. The maroon block is clear. The red block is clear. The cyan block is on the table. The tan block is clear.

action_sequence:
Jane moves the tan block from the table to the maroon block.

query:
The red block is not on the table. The red block is not on top of the tan block.

Step 1: Initial state

 red: on table, clear
 tan: on table, clear
 maroon: on teal, clear
 teal: on cyan
 cyan: on table
  \=> Valid state

Step 2: Apply action
Move tan from table to maroon

 tan is clear ✔
 maroon is clear ✔
  \=> Move succeeds
  Now: tan is on maroon, maroon is no longer clear

Step 3: Evaluate query

 “The red block is not on the table” → red is still on the table ✘
 “The red block is not on top of the tan block” → red is not on tan ✔

Since one part of the query is false, the entire conjunction is false.

Final output:
False


The new input is as follows:
Input:
state: 
{state}

action_sequence:
{act}

query: 
{query}
'''

# Legality
logot_state_represent_prompt_legality = '''\
State Input:
The tan block is on the table. The violet block is clear. The black block is on top of the teal block. The indigo block is on the table. The violet block is on top of the indigo block. The teal block is on the table. The tan block is clear. The black block is clear.
Query Input:
Jane moves the violet block from the indigo block to the tan block.
% State Encoding:
holds(on(tan, table), 0).
holds(clear(violet), 0).
holds(on(black, teal), 0).
holds(on(indigo, table), 0).
holds(on(violet, indigo), 0).
holds(on(teal, table), 0).
holds(clear(tan), 0).
holds(clear(black), 0).
% All Blocks:
block(tan). block(violet). block(black). block(teal). block(indigo).
% Query Encoding:
occurs(move(violet, indigo, tan), 0).
% Steps:
#const num_step=1.
    
State Input:
The tan block is on the table. The white block is clear. The white block is on the table. The brown block is clear. The orange block is clear. The green block is clear. The brown block is on the table. The orange block is on the table. The green block is on the table. The tan block is clear.
Query Input:
Jane moves the white block from the table to the brown block. Jane moves the white block from the brown block onto the table. Jane moves the brown block from the table to the white block.
% State Encoding:
holds(on(tan, table), 0).
holds(clear(white), 0).
holds(on(white, table), 0).
holds(clear(brown), 0).
holds(clear(orange), 0).
holds(clear(green), 0).
holds(on(brown, table), 0).
holds(on(orange, table), 0).
holds(on(green, table), 0).
holds(clear(tan), 0).
% All Blocks:
block(tan). block(white). block(brown). block(orange). block(green).
% Query Encoding:
occurs(move(white, table, brown), 0).
occurs(move(white, brown, table), 1).
occurs(move(brown, table, white), 2).
% Steps:
#const num_step=3.

State Input:
The maroon block is on the table. The red block is on the table. The white block is clear. The violet block is clear. The indigo block is clear. The white block is on the table. The indigo block is on the table. The violet block is on the table. The maroon block is clear. The red block is clear.
Query Input:
Jane moves the red block from the violet block to the maroon block.
% State Encoding:
holds(on(maroon, table), 0).
holds(on(red, table), 0).
holds(clear(white), 0).
holds(clear(violet), 0).
holds(clear(indigo), 0).
holds(on(white, table), 0).
holds(on(indigo, table), 0).
holds(on(violet, table), 0).
holds(clear(maroon), 0).
holds(clear(red), 0).
% All Blocks:
block(maroon). block(red). block(white). block(violet). block(indigo).
% Query Encoding:
occurs(move(red, violet, maroon), 0).
% Steps:
#const num_step=1.

State Input:
The lime block is on top of the aquamarine block. The olive block is clear. The lime block is clear. The teal block is on the table. The olive block is on the table. The navy block is on top of the teal block. The navy block is clear. The aquamarine block is on the table.
Query Input:
Jane moves the navy block from the teal block to the lime block. Jane moves the navy block from the lime block onto the table. Jane moves the lime block from the aquamarine block to the navy block.
% State Encoding:
holds(on(lime, aquamarine), 0).
holds(clear(olive), 0).
holds(clear(lime), 0).
holds(on(teal, table), 0).
holds(on(olive, table), 0).
holds(on(navy, teal), 0).
holds(clear(navy), 0).
holds(on(aquamarine, table), 0).
% All Blocks:
block(lime). block(olive). block(teal). block(navy). block(aquamarine).
% Query Encoding:
occurs(move(navy, teal, lime), 0).
occurs(move(navy, lime, table), 1).
occurs(move(lime, aquamarine, navy), 2).
% Steps:
#const num_step=3.

State Input:
{state}
Query Input:
{query}

Complete the text, output % State Encoding, % State Encoding, % All Blocks, % Query Encoding, % Steps.
Only show the result, do not explain.
'''

standard_prompt_legality = '''\
You are a reasoning assistant in a blocks world.
Rules:

1. All blocks are of equal size.
2. A block can only be moved if it is clear (nothing on top of it).
3. A block can only be placed on another block if the target block is clear.
4. Blocks may also be placed on the table, which always has space.
5. A block can only be on one other block or the table.

Decide whether a given action is legal in the initial state.

Input format:
state: A set of facts describing the world.
query: An action to evaluate.

Output:
Format your answer starting with % followed by a line of either True or False.

Example:
Input
state:
The red block is on the table. The tan block is on the table. The navy block is on top of the turquoise block. The tan block is clear. The red block is clear. The green block is clear. The green block is on the table. The navy block is clear. The turquoise block is on the table.
query:
Jane moves the navy block from the turquoise block to the green block.

Output:
%
True


The new input is as follows:
Input:
state: 
{state}

query: 
{query}


Keep the answer short. Only show the result.
'''

cot_prompt_legality = '''\


1. Identify which block is being moved.
2. Find where that block currently is.
3. Check whether the block is clear (nothing on top of it).
4. Check whether the destination block is clear.
5. If the block is clear, is currently in the stated location, and the destination is clear, then the action is legal. Otherwise, it is not.
6. Conclude with "True" if legal, or "False" if not.

---

### Example 1:

state:
The red block is on the table. The tan block is on the table. The green block is on the red block. The green block is clear. The tan block is clear.

query:
Jane moves the green block from the red block to the tan block.

Reasoning:
The green block is the one being moved.
It is currently on the red block.
It is clear, meaning there is nothing on top of it.
The tan block is clear as well.
All conditions are satisfied to move the green block from the red block to the tan block.

Final output:
True


### Example 2:

state:
The red block is on the table. The tan block is on the table. The green block is on the red block. The green block is clear. The tan block is not clear.

query:
Jane moves the green block from the red block to the tan block.

Reasoning:
The green block is the one being moved.
It is currently on the red block.
It is clear.
However, the tan block is not clear, so the green block cannot be placed there.

Final output:
False



### Now solve this:

state:
{state}

query:
{query}

'''

# Planning
logot_state_represent_prompt_planning = '''\
State Input:
The tan block is on the table. The violet block is clear. The black block is on top of the teal block. The indigo block is on the table. The violet block is on top of the indigo block. The teal block is on the table. The tan block is clear. The black block is clear.
Goal Input:
The violet block is not clear. The indigo block is on top of the black block.
Query Input:
Jane moves the violet block from the indigo block to the tan block.
% State Encoding:
holds(on(tan, table), 0).
holds(clear(violet), 0).
holds(on(black, teal), 0).
holds(on(indigo, table), 0).
holds(on(violet, indigo), 0).
holds(on(teal, table), 0).
holds(clear(tan), 0).
holds(clear(black), 0).
% All Blocks:
block(tan). block(violet). block(black). block(teal). block(indigo).
% Goal Encoding:
query_success :-
    -holds(clear(violet), num_step), 
    holds(on(indigo, black), num_step).
% Query Encoding:
occurs(move(violet, indigo, tan), 0).
% Step:
#const num_step=1.

State Input:
The tan block is on the table. The black block is on the table. The aquamarine block is on the table. The brown block is clear. The green block is clear. The aquamarine block is clear. The brown block is on the table. The green block is on the table. The tan block is clear. The black block is clear.
Goal Input:
The aquamarine block is on top of the green block. The aquamarine block is not on top of the black block.
Query Input:
Jane moves the aquamarine block from the table to the green block.
% State Encoding:
holds(on(tan, table), 0).
holds(on(black, table), 0).
holds(on(aquamarine, table), 0).
holds(clear(brown), 0).
holds(clear(green), 0).
holds(clear(aquamarine), 0).
holds(on(brown, table), 0).
holds(on(green, table), 0).
holds(clear(tan), 0).
holds(clear(black), 0).
% All Blocks:
block(tan). block(black). block(aquamarine). block(brown). block(green).
% Goal Encoding:
query_success :-
    holds(on(aquamarine, green), num_step).
    -holds(on(aquamarine, black), num_step).
% Query Encoding:
occurs(move(aquamarine, table, green), 0).
% Step:
#const num_step=1.

State Input:
The indigo block is clear. The brown block is on top of the navy block. The brown block is clear. The indigo block is on the table. The black block is clear. The navy block is on top of the cyan block. The black block is on the table. The cyan block is on the table.
Goal Input:
the cyan block is not on top of the brown block and the black block is not on top of the brown block
Query Input:
Jane moves the black block from the table to the brown block. Jane moves the cyan block from the navy block onto the table.
% State Encoding:
holds(clear(indigo), 0).
holds(on(brown, navy), 0).
holds(clear(brown), 0).
holds(on(indigo, table), 0).
holds(clear(black), 0).
holds(on(navy, cyan), 0).
holds(on(black, table), 0).
holds(on(cyan, table), 0).
% All Blocks:
block(indigo). block(brown). block(navy). block(black). block(cyan).
% Goal Encoding:
query_success :-
    -holds(on(cyan, brown), num_step),
    -holds(on(black, brown), num_step).
% Query Encoding:
occurs(move(black, table, brown), 0).
occurs(move(cyan, navy, table), 1).
% Step:
#const num_step=2.

State Input:
The pink block is clear. The orange block is on top of the gray block. The pink block is on top of the yellow block. The red block is on the table. The yellow block is on the table. The gray block is on top of the red block. The orange block is clear.
Goal Input:
the red block is on the table and the gray block is on top of the yellow block
Query Input:
Jane moves the orange block from the gray block onto the table. Jane moves the pink block from the yellow block to the orange block. Jane moves the gray block from the red block to the yellow block.
% State Encoding:
holds(clear(pink), 0).
holds(on(orange, gray), 0).
holds(on(pink, yellow), 0).
holds(on(red, table), 0).
holds(on(yellow, table), 0).
holds(on(gray, red), 0).
holds(clear(orange), 0).
% All Blocks:
block(pink). block(orange). block(gray). block(red). block(yellow).
% Goal Encoding:
query_success :-
    holds(on(red, table), num_step),
    holds(on(gray, yellow), num_step).
% Query Encoding:
occurs(move(orange, gray, table), 0).
occurs(move(pink, yellow, orange), 1).
occurs(move(gray, red, yellow), 2).
% Step:
#const num_step=3.

State Input:
{state}
Goal Input:
{goal}
Query Input:
{query}

Complete the text, output % State Encoding, % Goal Encoding, % Query Encoding, % Step.
Only show the result, do not explain.
'''

standard_prompt_planning = '''\
You are given an initial world state, a goal condition, and a sequence of actions. Determine whether the actions, when applied in order to the initial state, will result in a final state that satisfies the goal condition.

Rules:
* A block is either on another block or directly on the table.
* A block is clear if there is no block on top of it.
* A block can only be moved if it is clear.
* Only one block can be moved at a time.
* Moving a block changes its position and may change the clear status of involved blocks.

Input:
state:
The aquamarine block is on the table. The blue block is on the table. The maroon block is clear. The orange block is on top of the yellow block. The yellow block is on the table. The maroon block is on top of the blue block. The aquamarine block is clear. The orange block is clear.

goal:
the orange block is not on top of the yellow block and the aquamarine block is on top of the maroon block

query:
Jane moves the aquamarine block from the table to the maroon block. Jane moves the orange block from the yellow block onto the table.


Task:

Answer whether the goal condition is satisfied after executing the query actions in the given order from the initial state. Respond with:

%
True

or

%
False

The new input is as follows:
Input:
state: 
{state}

goal:
{goal}

query: 
{query}


Keep the answer short. Only show the result.
'''

cot_prompt_planning = '''\


You are given a puzzle involving blocks in a world where:

 The table has infinite space.
 Blocks are stackable and can be moved under certain conditions.
 A block is clear if no other block is on top of it.
 A block can only be moved if it is clear.
 Blocks can be moved onto another clear block or onto the table.

You will be given:

 an initial state describing where each block is and which are clear,
 a goal describing what should be true after a sequence of actions,
 and a query, which is a sequence of actions taken.

Your task is to decide if the actions, when applied step-by-step from the initial state, lead to a final state that satisfies the goal. Follow these reasoning steps:

---

Step 1: Parse the initial state
List the position of each block and whether it's clear. Build a world model.

Step 2: Parse the goal
Break down the goal into specific conditions that must be true in the final state.

Step 3: Apply each action in order
For each action:

 Check if the block being moved is clear.
 Check if the destination (another block or the table) is clear (if a block).
 Update the world state accordingly.

Step 4: Check the final state against the goal
See if the goal conditions are satisfied.

Step 5: Output whether the sequence of actions achieves the goal
If the final state satisfies the goal, output:

Final output:
True

Otherwise, output:

Final output:
False

Example 

state:
The aquamarine block is on the table. The blue block is on the table. The maroon block is clear. The orange block is on top of the yellow block. The yellow block is on the table. The maroon block is on top of the blue block. The aquamarine block is clear. The orange block is clear.

goal:
the orange block is not on top of the yellow block and the aquamarine block is on top of the maroon block

query:
Jane moves the aquamarine block from the table to the maroon block. Jane moves the orange block from the yellow block onto the table.

Step 1: Initial state

 aquamarine: on table, clear
 blue: on table
 maroon: on blue, clear
 orange: on yellow, clear
 yellow: on table
  \=> All blocks are in valid positions.

Step 2: Goal

 orange is not on yellow
 aquamarine is on maroon

Step 3: Apply actions

1. Move aquamarine from table to maroon
    aquamarine is clear ✔
    maroon is clear ✔
     \=> Move succeeds; aquamarine is now on maroon; maroon is no longer clear
2. Move orange from yellow to table
    orange is clear ✔
     \=> Move succeeds; orange is now on table; yellow is now clear

Step 4: Final state
 orange is on table ≠ on yellow ✔
 aquamarine is on maroon ✔

Step 5: Check goal
All goal conditions are met.

Final output:
True

### Now solve this:

state: 
{state}

goal:
{goal}

query: 
{query}
'''