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
block(tan). block(white). block(brown). block(orange). block(green).
% Query Encoding:
occurs(move(white, table, brown), 0).
occurs(move(white, brown, table), 1).
occurs(move(brown, table, white), 2).
#const num_step=3.