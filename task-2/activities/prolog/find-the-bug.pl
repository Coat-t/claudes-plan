% =====================================================================
%  find-the-bug.pl - Pixel's AI Field Guide (v1.0, 2026-11-06)
%  Pixel copied two rules from family.pl but made TWO mistakes.
%  Both rules load WITHOUT any error message, yet give wrong answers.
%  Your job: run the queries in queries.md (Part E), spot the bugs,
%  and fix them. (Hints and fixes are in queries.md - try first!)
%  The family below is the same made-up family as in family.pl.
% =====================================================================
%
%  QUICK SYNTAX REMINDER (full version at the top of family.pl)
%  -------------------------------------------------------------
%  parent(grace, ada).         a FACT: "grace is a parent of ada".
%                              Every clause ENDS WITH A PERIOD.
%  lowercase words             ATOMS: fixed names (grace, ada, x).
%  Uppercase words             VARIABLES: blanks Prolog fills in (X, Y, P).
%  head :- a, b.               a RULE: "head is true IF a AND b".
%                              :- means IF, the comma means AND.
%  X \= Y                      "X and Y cannot be made equal"
%                              (X and Y are different things).
%  ?- sibling(zara, S).        a QUERY (in SWISH type it without ?- ).
%
%  Detective tip from Dr. Okafor: a program that loads without errors
%  can still be wrong. Prolog checks the GRAMMAR of your rules, not
%  whether they say what you MEANT. Test with cases where you already
%  know the right answer.
% =====================================================================

% FACTS: parent(Parent, Child).
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

% BUGGY RULE 1: Pixel thinks this finds brothers and sisters.
% Pixel's reading: "X and Y are siblings IF some P is a parent of X
% AND that same P is a parent of Y."  What did Pixel forget?
sibling(X, Y) :- parent(P, X), parent(P, Y).

% BUGGY RULE 2: Pixel thinks this finds mothers.
% Pixel's reading: "X is the mother of Y IF X is a parent of Y
% AND X is female."  Look very closely at every letter.
mother(X, Y) :- parent(X, Y), female(x).
