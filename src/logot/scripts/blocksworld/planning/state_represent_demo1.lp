% State Encoding:
holds(on(indigo, table), 0).
holds(clear(indigo), 0).
holds(on(brown, navy), 0).
holds(clear(brown), 0).
holds(on(navy, cyan), 0).
holds(on(black, table), 0).
holds(clear(black), 0).
holds(on(cyan, table), 0).
block(indigo). block(brown). block(navy). block(black). block(cyan).
% Goal Encoding:
query_success :-
    -holds(on(cyan, brown), num_step),
    -holds(on(black, brown), num_step).
% Query Encoding:
occurs(move(black, table, brown), 0).
occurs(move(cyan, navy, table), 1).
#const num_step=2.