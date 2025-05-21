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
block(tan). block(black). block(aquamarine). block(brown). block(green).
% Action Sequence Encoding:
occurs(move(aquamarine, table, green), 0).
#const num_step=1.
% Query Encoding:
query_success :-
    holds(on(aquamarine, green), num_step).
    -holds(on(aquamarine, black), num_step).