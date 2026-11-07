# Pixel's Prolog Missions: Build a Tiny Rule-Based System

**Pixel's AI Field Guide: Missions for Curious Humans** · Supplement · Version 1.0 · 2026-11-06
Belongs to: Mission 03 (Pixel's Rulebook: rule-based AI). Also connects to Mission 08 (Time Machine: expert systems of the 1980s) and contrasts with Mission 04 (learning from examples).

**[MISSION BRIEF]** Pixel has been told some facts about a (made-up) family and about broken lab robots. Dr. Ada Okafor wants Pixel to work out **new** facts nobody wrote down: who is whose grandparent, and what is wrong with each robot. Pixel can only use precise facts and rules, so you will write them in **Prolog**, a logic programming language.

| File | What it is |
|---|---|
| `family.pl` | A family tree: facts, simple rules, and a recursive `ancestor` rule. The top of the file has an 8-point beginner's guide to Prolog syntax. |
| `robot-troubleshooter.pl` | A tiny expert system: IF-THEN rules diagnose made-up robot faults, with a "no diagnosis" fallback. |
| `find-the-bug.pl` | Two rules with hidden mistakes for you to find and fix. |
| `queries.md` | **The worksheet:** every query, a prediction prompt, the exact expected answers, explanations, and fixes. |
| `test_queries.cjs`, `test-output.txt` | The automated test of every query, and its saved output. |

---

## Goal
- Explain the three building blocks of a rule-based system: **facts**, **rules** and **queries**.
- Read and write simple Prolog: `:-` (IF), `,` (AND), the period that ends every clause, lowercase atoms vs Uppercase variables, and `\=` ("is different from").
- Trace how Prolog reaches a conclusion, including a **recursive** rule (`ancestor`) and the **duplicate answers** that come from two different proofs.
- Extend a knowledge base by adding a fact and a rule, and **debug** rules that load without error but give wrong answers.

## Preparation
- **Knowledge:** Missions 01 and 02 of the guide, and the start of Mission 03 (rule-based AI). No programming experience is needed. Read the comment box at the top of `family.pl` first (5 minutes).
- **Tool:** SWISH, a free browser-based Prolog at <https://swish.swi-prolog.org>, which runs SWI-Prolog.
  - **Online:** yes, SWISH needs an internet connection.
  - **Account:** **not needed** to write and run programs. A login (Google or StackOverflow) is optional and only needed to save programs on the SWISH server. To keep your work without logging in, copy your program into a text file on your own computer.
  - **Offline alternative:** install SWI-Prolog from <https://www.swi-prolog.org> and load a file with `consult('family.pl').` In the terminal you press `;` for the next answer and Enter to stop.
- **Files:** the three `.pl` files. Open them in any text editor to copy their text.
- **Time:** about 45 to 60 minutes for Parts A to E.

## Task (step by step)
Follow `queries.md`. In short:
1. **Set up SWISH** (`queries.md` Section 0): open SWISH, choose **Empty**, then **Program**, and paste all of `family.pl` into the editor.
2. **Part A, facts:** type `parent(ada, Child).` in the query box and click **Run!**. Use **Next** to get more answers. Always **[PREDICT]** first.
3. **Part B, rules:** run the `father`, `grandparent`, `sibling` and `ancestor` queries. Use the trace table in `queries.md` B6 to see why `sibling(ada, S)` answers `tunde` **twice**.
4. **Part C, extend:** add a `grandmother` rule, then add a new baby (`parent(kemi, tayo).`, `male(tayo).`) and see that `ancestor` finds four ancestors **without any new rule**.
5. **Part D, expert system:** replace the program with `robot-troubleshooter.pl`, diagnose the robots, and add one piece of expert knowledge (the `dry_joints` rule) to fix gizmo's "no diagnosis".
6. **Part E, find the bug:** load `find-the-bug.pl`, run the two queries, and explain and fix both bugs before opening the hints.

## Observation questions
1. In A2, why does `zara` come before `leo`? What decides the order of Prolog's answers?
2. In B3, Prolog says `false` for zara's father. Is that because zara has no father? What does `false` really mean in Prolog?
3. In B6, how many answers did you get for ada's siblings? Fill in the trace table: which shared parent produced each one?
4. In C2, how many ancestors did tayo get after you added **one** fact? Which rule did the work?
5. In D4 and D7, what changed in the program to turn "no diagnosis" into `dry_joints`? Did Pixel learn it from data?
6. In Part E, both buggy files loaded with **no error message**. How did you discover the bugs?

## Reflection
- **[EXPLAIN]** Write one sentence explaining how Prolog decided that grace is an ancestor of kemi. Name the rule clauses it used.
- Compare the troubleshooter with Pixel's spam filter (`../spam-filter/`): who supplies the "rules" in each, and what happens when a new case appears that no rule covers?
- Why might a hospital or a bank **like** a rule-based system, even though it cannot learn by itself? (Hint: think about explaining decisions.)
- The 1980s expert-system boom ended partly because writing and maintaining thousands of hand-made rules was expensive. Which part of Part D gives you a taste of that problem?

## Feedback: expected results
The **exact** answers for all 31 queries, with explanations, are in `queries.md` (each one hidden in a "show answer" box so you can predict first). The key ones:

| Query | Expected answer (SWI-Prolog / SWISH order) |
|---|---|
| `parent(ada, Child).` | `Child = zara ;` `Child = leo.` |
| `father(F, ada).` | `F = samuel.` |
| `father(F, zara).` | `false.` (no father recorded: the "closed world" assumption) |
| `sibling(ada, S).` | `S = tunde ;` `S = tunde.` (two proofs: via grace and via samuel) |
| `ancestor(A, kemi).` | `A = tunde ;` `A = grace ;` `A = samuel ;` `false.` |
| `diagnosis(gizmo, D).` | `D = no_diagnosis_ask_dr_okafor.` (after adding the dry_joints rule: `D = dry_joints ;` `false.`) |
| Buggy `sibling(zara, S).` | `S = zara ;` `S = leo.` (fix: add `X \= Y`) |
| Buggy `mother(M, zara).` | `false.` (fix: `female(x)` should be `female(X)`) |

**Reflection key points:** Prolog proves a query by matching it against facts and the heads of rules, then proving each condition in the rule's body from left to right, backtracking when a condition fails. It lists every **proof**, which is why duplicates appear. All of its "knowledge" was written by a human, so it can explain every conclusion (it follows the rules you can read), but it cannot improve itself or cope with anything outside its rules.

## [LAB NOTE] Limitations
- **Closed world:** Prolog treats anything it cannot prove as false. A missing fact (zara's father) looks the same as a fact that is really false.
- **Toy knowledge bases:** a 7-person family and 4 robots. Real expert systems had hundreds or thousands of rules, and experts often disagreed about them.
- **No uncertainty:** the troubleshooter's rules are all-or-nothing. Real diagnosis deals with "probably" and "sometimes". Some historical expert systems added certainty factors for this; Prolog on its own does not.
- **Only a small subset of Prolog** is used here. Real Prolog also has lists, arithmetic, the cut (`!`) and more.
- **Display differs between Prolog systems:** SWISH shows answers with **Next** buttons. A terminal shows `;`. Tau Prolog always prints a final `false.`. The answers and their order are the same (see the LAB NOTE in `queries.md`).

## Fallback if SWISH is unavailable
1. Install SWI-Prolog (free, offline) from <https://www.swi-prolog.org>, or use any other standard Prolog. All files use only basic ISO Prolog features. Part B12's `setof/3` is also standard.
2. **No Prolog at all (paper version):** print `family.pl` and the family-tree picture at its top. For each query in `queries.md`, write your prediction, then **trace it by hand**: go through the facts top to bottom, as in the trace table in B6. Check against the hidden answers. `test-output.txt` shows the full output of a real run for every query, so you can compare your trace with it.

## Test evidence
- **Date:** 2026-11-06. **Command:** `NODE_PATH=<folder with packages> node test_queries.cjs > test-output.txt` (Node v26.10.0). The two npm packages are **not** shipped with this activity and learners never need them: to re-run the test, run `npm install swipl-wasm tau-prolog` in any temporary folder and point `NODE_PATH` at its `node_modules`. This activity has no separate UI test, because the learner-facing tool is SWISH, not a page in this folder.
- **Engines:**
  - **SWI-Prolog 10.1.20** via the npm package swipl-wasm 8.3.0. This is the same Prolog system that SWISH runs, so the answer order matches SWISH. The live site may run a different SWI-Prolog version.
  - **Tau Prolog 0.3.4** (npm package `tau-prolog`), a separate JavaScript Prolog, as a cross-check.
- **What was run:** all 31 queries in `queries.md`, including the edited programs for Parts C, D7 to D9 and the fixed Part E. The script builds those edits by inserting the exact lines that `queries.md` tells learners to add, in the places it says.
- **Result:** both engines gave the same answers in the same order for all 31 queries. The only difference was the display (Tau Prolog always ends with `false.`). No load warnings or errors appeared, including for `find-the-bug.pl`, which confirms that its bugs are silent.
- **Re-checked:** on 2026-11-06, after all supplements were finished, the test was run again; its output was identical to `test-output.txt`.
- **Not automated:** the SWISH web page itself (button names come from the SWISH help page and a published SWISH tutorial).
