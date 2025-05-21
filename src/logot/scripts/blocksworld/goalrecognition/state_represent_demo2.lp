% State Encoding:
holds(on(pink, magenta), 0).
holds(on(tan, table), 0).
holds(clear(pink), 0).
holds(on(aquamarine, tan), 0).
holds(on(red, aquamarine), 0).
holds(on(magenta, table), 0).
holds(clear(red), 0).
block(pink). block(magenta). block(tan). block(aquamarine). block(red).
% Observation Encoding:
query_success :-
    occurs(move(red, aquamarine, table), 0).
% Query Encoding:
goal(I) :-
    holds(on(aquamarine, table), I),
    holds(on(magenta, tan), I).