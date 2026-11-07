% =====================================================================
%  family.pl  -  Pixel's AI Field Guide, Prolog supplement (v1.0, 2026-11-06)
%  A tiny RULE-BASED system: Pixel learns a (made-up) family tree from
%  FACTS and works out new relationships using RULES.
%  The Okafor-Bello family below is fictional.
% =====================================================================
%
%  PROLOG SYNTAX IN 8 BULLETS (read this first!)
%  ---------------------------------------------
%  1. A line starting with % is a COMMENT. Prolog ignores it.
%  2. A FACT states something that is simply true, e.g.
%         parent(grace, ada).
%     Read it as: "grace is a parent of ada".
%     parent is the PREDICATE (the relationship); grace and ada are its
%     ARGUMENTS. The number of arguments is written after a slash:
%     parent/2 means "parent with 2 arguments".
%  3. Names that start with a LOWERCASE letter (grace, ada) are ATOMS:
%     fixed names of things.
%  4. Names that start with an UPPERCASE letter (X, Y, Child) are VARIABLES:
%     blanks that Prolog tries to fill in.
%  5. Every clause (fact or rule) ENDS WITH A PERIOD "."  Forgetting the
%     period is the most common beginner error.
%  6. A RULE has a head and a body separated by  :-  which you can read as
%     "IF". Example:
%         father(X, Y) :- parent(X, Y), male(X).
%     reads: "X is the father of Y IF X is a parent of Y AND X is male."
%  7. A COMMA "," between conditions means AND. All of them must be true.
%  8. A QUERY is a question you ask. In a book it is written with ?- in
%     front:   ?- father(F, ada).
%     In SWISH you type only the part after ?-  (father(F, ada).) into the
%     query box (bottom right) and press "Run!".
%     Prolog answers true/false, or tells you which values make it true:
%         F = samuel.
%
%  Family tree (for reference):
%
%        grace (f) ---+--- samuel (m)
%                     |
%            +--------+--------+
%            |                 |
%         ada (f)          tunde (m)
%            |                 |
%      +-----+-----+           |
%      |           |           |
%   zara (f)    leo (m)     kemi (f)
%
%  (Only one parent is recorded for zara, leo and kemi, to keep it small.)
% =====================================================================

% ---------------------------------------------------------------------
% FACTS: parent(Parent, Child).  "Parent is a parent of Child."
% Keep all clauses of the same predicate together (Prolog prefers this).
% ---------------------------------------------------------------------
parent(grace, ada).
parent(samuel, ada).
parent(grace, tunde).
parent(samuel, tunde).
parent(ada, zara).
parent(ada, leo).
parent(tunde, kemi).

% FACTS: male(Person) and female(Person).
male(samuel).
male(tunde).
male(leo).

female(grace).
female(ada).
female(zara).
female(kemi).

% ---------------------------------------------------------------------
% RULES
% ---------------------------------------------------------------------

% father(X, Y): X is the father of Y IF X is a parent of Y AND X is male.
father(X, Y) :- parent(X, Y), male(X).

% mother(X, Y): X is the mother of Y IF X is a parent of Y AND X is female.
mother(X, Y) :- parent(X, Y), female(X).

% grandparent(X, Z): X is a grandparent of Z IF
%   X is a parent of some Y, AND that same Y is a parent of Z.
% The shared variable Y is the "link" (the middle generation).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% sibling(X, Y): X and Y are siblings IF they share a parent P
%   AND X is not the same person as Y.
% \=  means "cannot be made equal" (here: "is a different person from").
% Without it, Prolog would say everyone is their own sibling!
% NOTE: ada and tunde share TWO parents (grace and samuel), so Prolog finds
% "tunde is ada's sibling" twice - once via grace, once via samuel.
% See queries.md for why this happens.
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.

% ancestor(X, Y): a RECURSIVE rule (a rule that uses itself).
% It has two clauses. Prolog tries them in order:
%   Clause 1 (base case):  X is an ancestor of Y IF X is a parent of Y.
%   Clause 2 (recursive):  X is an ancestor of Y IF X is a parent of some Z
%                          AND Z is an ancestor of Y.
% The base case stops the recursion, like the bottom step of a staircase.
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% ---------------------------------------------------------------------
% YOUR TURN (see queries.md, Part C):
%  - Add yourself or a new baby with a parent/2 fact and a male/1 or
%    female/1 fact, then re-run the queries.
%  - Write a rule  grandmother(X, Z) :- ...  using grandparent and female.
% ---------------------------------------------------------------------
