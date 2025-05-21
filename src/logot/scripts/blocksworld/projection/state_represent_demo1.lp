% State Encoding:
holds(on(tan, table), 0).
holds(clear(violet), 0).
holds(on(black, teal), 0).
holds(on(indigo, table), 0).
holds(on(violet, indigo), 0).
holds(on(teal, table), 0).
holds(clear(tan), 0).
holds(clear(black), 0).
block(tan). block(violet). block(black). block(teal). block(indigo).
% Action Sequence Encoding:
occurs(move(violet, indigo, tan), 0).
#const num_step=1.
% Query Encoding:
query_success :-
    -holds(clear(violet), num_step), 
    holds(on(indigo, black), num_step).