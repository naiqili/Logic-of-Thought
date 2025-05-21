% State Encoding:
holds(on(cyan, aquamarine), 0).
holds(on(gray, cyan), 0).
holds(on(turquoise, table), 0).
holds(clear(gray), 0).
holds(clear(orange), 0).
holds(on(aquamarine, turquoise), 0).
holds(on(orange, table), 0).
block(cyan). block(aquamarine). block(gray). block(turquoise). block(orange).
% Observation Encoding:
query_success :-
    occurs(move(gray, cyan, table), 0),
    occurs(move(cyan, aquamarine, table), 1).
% Query Encoding:
goal(I) :-
    -holds(on(turquoise, table), I),
    -holds(on(gray, turquoise), I).