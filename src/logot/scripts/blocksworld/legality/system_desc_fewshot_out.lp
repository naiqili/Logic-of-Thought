

% Definition of Types.
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
holds(F,I+1) :- fluent(inertial,F), holds(F,I), not -holds(F,I+1), I<num_step. 
-holds(F,I+1) :- fluent(inertial,F), -holds(F,I), not holds(F,I+1), I<num_step. 

% Close world assumption for Actions.
-occurs(A,I) :- action(A), step(I), not occurs(A,I).

% Close world assumption for init state.
-holds(on(B,L),0) :- block(B), location(L), not holds(on(B,L),0).
-holds(clear(B),0) :- block(B), not holds(clear(B),0).

% Do not allow concurrent actions.
:- action(A1), action(A2), occurs(A1,I), occurs(A2,I), A1 != A2.

% Miscs.
step(0..num_step).
#show holds/2.

