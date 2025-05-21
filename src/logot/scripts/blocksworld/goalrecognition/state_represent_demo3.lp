% State Encoding:
holds(on(green, pink), 0).
holds(on(red, olive), 0).
holds(clear(brown), 0).
holds(on(olive, green), 0).
holds(on(brown, table), 0).
holds(on(pink, table), 0).
holds(clear(red), 0).
block(green). block(pink). block(red). block(olive). block(brown).

% Observation Encoding:
query_success :-
    occurs(move(red, olive, table), 0),
    occurs(move(red, table, olive), 1),
    occurs(move(red, olive, table), 2).

% Query Encoding:
goal(I) :-
    -holds(on(pink, table), I),
    -holds(on(brown, olive), I).