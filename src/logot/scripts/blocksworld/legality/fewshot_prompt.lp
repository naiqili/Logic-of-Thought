

% Introduction:
% Domain: We use a variant of the blocks world (BW) as an example where 
% 1) a table has infinite space to hold blocks, 
% 2) blocks have identical sizes and can be stacked as towers (a block is either on another one or immediately on the table), 
% 3) a block can be moved only if certain conditions are met.
% Types:
% 1) block(X): X is a block.
% 2) location(L): L is a location.
% Fluents:
% 1) on(X, Y) states that X is on Y.
% 2) clear(X) declares that there is no block on X.
% Task (Goal-Recognition): Goal-Recognition is the task to recognize the goal from the partial observation of actions. Given an initial state s, a potential goal g, and a sequence a of N actions as the observation, decide if g is the true objective. That is, decide if a is a prefix of any optimal plans to achieve g. 

% Definition of Types.
% Location includes all the blocks and the table.
location(X) :- block(X). 
location(table).

% Definition of Fluents.
fluent(inertial, on(B,L)) :- block(B), location(L). 
fluent(inertial, clear(B)) :- block(B). 

% Definition of Actions.
action(move(B,L1,L2)) :- block(B), location(L1), location(L2), 
    B!=L1, B!=L2, L1!=L2.

% Action effects.
holds(on(B,L2),I+1) :- occurs(move(B,L1,L2),I), I < num_step.
-holds(on(B,L1),I+1) :- occurs(move(B,L1,L2),I), I < num_step.
holds(clear(L1),I+1) :- occurs(move(B,L1,L2),I), I < num_step.
-holds(clear(L2),I+1) :- occurs(move(B,L1,L2),I), I < num_step.

% Action precondition.
-occurs(move(B,L1,L2),I) :- location(L1), location(L2), holds(on(B1,B),I). 
-occurs(move(B,L1,L2),I) :- location(L1), location(L2), -holds(clear(B),I). 
-occurs(move(B1,L1,B2),I) :- block(B1), location(L1), block(B2), holds(on(B,B2),I).
-occurs(move(B1,L1,B2),I) :- block(B1), location(L1), block(B2), -holds(clear(B2),I).
-occurs(move(B,L1,L2),I) :- location(L2), -holds(on(B,L1),I). 

% General inertia axiom.
holds(F,I+1) :- fluent(inertial ,F), holds(F,I), not -holds(F,I+1), I<num_step. 
-holds(F,I+1) :- fluent(inertial ,F), -holds(F,I), not holds(F,I+1), I<num_step. 

% Close world assumption for Actions.
-occurs(A,I) :- action(A), step(I), not occurs(A,I).

% Close world assumption for init state.
-holds(on(B,L),0) :- block(B), location(L), not holds(on(B,L),0).
-holds(clear(B),0) :- block(B), not holds(clear(B),0).

% Do not allow concurrent actions.
:- action(A1), action(A2), occurs(A1,I), occurs(A2,I), A1 != A2.

% Rules for planning.
success :- goal(I), I<=num_step. 
:- not success. 

occurs(A,I) | -occurs(A,I) :- action(A), step(I), not goal(I), I<num_step. 

% Do not allow concurrent actions.
:- action(A1), action(A2), occurs(A1,I), occurs(A2,I), A1 != A2.

% Rule for optimal plan. Occurred (Action, K) should be minimized.
#minimize{1, Action, K: occurs(Action , K)}.



% Introduction:
% Domain: We use a variant of the blocks world (BW) as an example where 
% 1) a table has infinite space to hold blocks, 
% 2) blocks have identical sizes and can be stacked as towers (a block is either on another one or immediately on the table), 
% 3) a block can be moved only if certain conditions are met.
% Types:
% 1) block(X): X is a block.
% 2) location(L): L is a location.
% Fluents:
% 1) on(X, Y) states that X is on Y.
% 2) clear(X) declares that there is no block on X.
% Task (Plan Verification): Planning is the task of formulating actions to fulfill a certain goal. We use the verification version that asks systems to recognize if the provided actions can achieve the goal: Given an initial state s and a goal g, a proposition, and a sequence a of N actions, decide if a can achieve g.

% Definition of Types.
% Location includes all the blocks and the table.
location(X) :- block(X). 
location(table).

% Definition of Fluents.
fluent(inertial, on(B,L)) :- block(B), location(L). 
fluent(inertial, clear(B)) :- block(B). 

% Definition of Actions.
action(move(B,L1,L2)) :- block(B), location(L1), location(L2), 
    B!=L1, B!=L2, L1!=L2.

% Action effects.
holds(on(B,L2),I+1) :- occurs(move(B,L1,L2),I), I < num_step.
-holds(on(B,L1),I+1) :- occurs(move(B,L1,L2),I), I < num_step.
holds(clear(L1),I+1) :- occurs(move(B,L1,L2),I), I < num_step.
-holds(clear(L2),I+1) :- occurs(move(B,L1,L2),I), I < num_step.

% Action precondition.
-occurs(move(B,L1,L2),I) :- location(L1), location(L2), holds(on(B1,B),I). 
-occurs(move(B,L1,L2),I) :- location(L1), location(L2), -holds(clear(B),I). 
-occurs(move(B1,L1,B2),I) :- block(B1), location(L1), block(B2), holds(on(B,B2),I).
-occurs(move(B1,L1,B2),I) :- block(B1), location(L1), block(B2), -holds(clear(B2),I).
-occurs(move(B,L1,L2),I) :- location(L2), -holds(on(B,L1),I). 

% General inertia axiom.
holds(F,I+1) :- fluent(inertial ,F), holds(F,I), not -holds(F,I+1), I<num_step. 
-holds(F,I+1) :- fluent(inertial ,F), -holds(F,I), not holds(F,I+1), I<num_step. 

% Close world assumption for Actions.
-occurs(A,I) :- action(A), step(I), not occurs(A,I).

% Close world assumption for init state.
-holds(on(B,L),0) :- block(B), location(L), not holds(on(B,L),0).
-holds(clear(B),0) :- block(B), not holds(clear(B),0).

% Do not allow concurrent actions.
:- action(A1), action(A2), occurs(A1,I), occurs(A2,I), A1 != A2.


% Rules for planning.
success :- goal(I), I<=num_step. 
:- not success. 

occurs(A,I) | -occurs(A,I) :- action(A), step(I), not goal(I), I<num_step. 



% Introduction:
% Domain: We use a variant of the blocks world (BW) as an example where 
% 1) a table has infinite space to hold blocks, 
% 2) blocks have identical sizes and can be stacked as towers (a block is either on another one or immediately on the table), 
% 3) a block can be moved only if certain conditions are met.
% Types:
% 1) block(X): X is a block.
% 2) location(L): L is a location.
% Fluents:
% 1) on(X, Y) states that X is on Y.
% 2) clear(X) declares that there is no block on X.
% Task (Projection): The projection task directly asks about the effects of actions. Given an initial state s and an applicable sequence a of N actions, decide whether the projection query q, a proposition, would hold after the execution of a.

% Definition of Types.
% Location includes all the blocks and the table.
location(X) :- block(X). 
location(table).

% Definition of Fluents.
fluent(inertial, on(B,L)) :- block(B), location(L). 
fluent(inertial, clear(B)) :- block(B). 

% Definition of Actions.
action(move(B,L1,L2)) :- block(B), location(L1), location(L2), 
    B!=L1, B!=L2, L1!=L2.

% Action effects.
holds(on(B,L2),I+1) :- occurs(move(B,L1,L2),I), I < num_step.
-holds(on(B,L1),I+1) :- occurs(move(B,L1,L2),I), I < num_step.
holds(clear(L1),I+1) :- occurs(move(B,L1,L2),I), I < num_step.
-holds(clear(L2),I+1) :- occurs(move(B,L1,L2),I), I < num_step.

% Action precondition.
-occurs(move(B,L1,L2),I) :- location(L1), location(L2), holds(on(B1,B),I). 
-occurs(move(B,L1,L2),I) :- location(L1), location(L2), -holds(clear(B),I). 
-occurs(move(B1,L1,B2),I) :- block(B1), location(L1), block(B2), holds(on(B,B2),I).
-occurs(move(B1,L1,B2),I) :- block(B1), location(L1), block(B2), -holds(clear(B2),I).
-occurs(move(B,L1,L2),I) :- location(L2), -holds(on(B,L1),I). 

% General inertia axiom.
holds(F,I+1) :- fluent(inertial ,F), holds(F,I), not -holds(F,I+1), I<num_step. 
-holds(F,I+1) :- fluent(inertial ,F), -holds(F,I), not holds(F,I+1), I<num_step. 

% Close world assumption for Actions 
-occurs(A,I) :- action(A), step(I), not occurs(A,I).

% Close world assumption for init state
-holds(on(B,L),0) :- block(B), location(L), not holds(on(B,L),0).
-holds(clear(B),0) :- block(B), not holds(clear(B),0).

% Do not allow concurrent actions: 
:- action(A1), action(A2), occurs(A1,I), occurs(A2,I), A1 != A2.


% Introduction:
% Domain: We use a variant of the blocks world (BW) as an example where 
% 1) a table has infinite space to hold blocks, 
% 2) blocks have identical sizes and can be stacked as towers (a block is either on another one or immediately on the table), 
% 3) a block can be moved only if certain conditions are met.
% Types:
% 1) block(X): X is a block.
% 2) location(L): L is a location.
% Fluents:
% 1) on(X, Y) states that X is on Y.
% 2) clear(X) declares that there is no block on X.
% Task (Legality): This task directly targets the preconditions of actions: Given an initial state s and a sequence ⃗a of N actions, decide whether ⃗a can be executed consecutively in s. 

% Definition of Types.
% Location includes all the blocks and the table.
ASP_RULES

% Definition of Fluents.
ASP_RULES

% Definition of Actions.
ASP_RULES

% Action effects.
ASP_RULES

% Action precondition.
ASP_RULES

% General inertia axiom.
ASP_RULES

% Close world assumption for Actions.
ASP_RULES

% Close world assumption for init state
ASP_RULES

% Do not allow concurrent actions: 
ASP_RULES

Complete the ASP_RULES above. Do not add new rules.
