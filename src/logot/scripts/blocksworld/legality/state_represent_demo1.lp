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
block(maroon). block(red). block(white). block(violet). block(indigo).
% Query Encoding:
occurs(move(red, violet, maroon), 0).
#const num_step=1.