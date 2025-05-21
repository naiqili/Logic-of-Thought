% State Encoding:
holds(clear(pink), 0).
holds(on(orange, gray), 0).
holds(on(pink, yellow), 0).
holds(on(red, table), 0).
holds(on(yellow, table), 0).
holds(on(gray, red), 0).
holds(clear(orange), 0).
block(pink). block(orange). block(gray). block(red). block(yellow).
% Goal Encoding:
query_success :-
    holds(on(red, table), num_step),
    holds(on(gray, yellow), num_step).
% Query Encoding:
occurs(move(orange, gray, table), 0).
occurs(move(pink, yellow, orange), 1).
occurs(move(gray, red, yellow), 2).
#const num_step=3.