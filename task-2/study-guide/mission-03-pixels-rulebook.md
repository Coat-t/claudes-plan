# Mission 03: Pixel's Rulebook

**Pixel's AI Field Guide: Missions for Curious Humans** · Version 1.0 (2026-11-06)
**Covers:** Topic 02, [How AI operates](../../task-1/topics/02-how-ai-operates.md), part 2: rule-based (symbolic) AI and **expert systems** · **Time:** about 75 minutes (core) + 20 minutes (optional)
**Navigation:** [Start here](00-start-here.md) · Previous: [Mission 02](mission-02-the-river-problem.md) · Next: [Mission 04](mission-04-learning-from-examples.md) · [Glossary](glossary.md)

**Supplement used:** [activities/prolog/](../activities/prolog/README.md): `family.pl`, `robot-troubleshooter.pl`, `find-the-bug.pl`, and the full worksheet [`queries.md`](../activities/prolog/queries.md) (31 tested queries). Everything you need for the core path is also printed below.

---

## [MISSION BRIEF] "Zara has no father!"

Dr. Ada Okafor gives Pixel a few facts about a (made-up) family and asks a simple question: "Who is Zara's father?" Pixel searches its facts and announces, very confidently, "Zara has no father!" Dr. Okafor sighs: Pixel only knows what it has been told, and nobody told it. In this mission you will write Pixel's knowledge as **facts and rules** in a logic language called **Prolog**, and find out exactly what Pixel can and cannot conclude.

### Learning goals

By the end of this mission you should be able to:

- **Explain** the three building blocks of a rule-based system: **facts**, **rules** and **queries**.
- **Read and write** simple Prolog: `:-` (IF), `,` (AND), the period at the end of every clause, lowercase **atoms** vs Uppercase **variables**.
- **Trace** how Prolog reaches a conclusion, including a **recursive** rule and a **duplicate** answer.
- **Extend** a knowledge base with a new fact and a new rule, and **debug** rules that load without error but give wrong answers.
- **Explain** the strengths and weaknesses of expert systems compared with learning-based AI.

---

## Setting up (about 5 minutes)

**Online (recommended): SWISH**, a free website that runs SWI-Prolog in your browser: <https://swish.swi-prolog.org/>

- **Account:** **not needed** to write and run programs. A Google or StackOverflow login is optional and only needed to save programs on the site. **You do not need to save.** If you do save, note that SWISH saves programs as **public and searchable by default**: untick "Public" and never put personal information in the code. To keep your work privately, copy it into a text file on your computer.
- **Device:** a laptop or desktop is recommended (the editor panes are wide; phones were not tested). Internet needed.
- **Steps:** (1) Open SWISH. (2) In the program panel, make sure **Empty** is selected, then click **Program**; a blank editor opens on the left. (The exact start-screen wording may differ slightly; you can also just type into the left editor.) (3) Paste the program into the **left** editor. (4) Type a query into the **query box** (bottom right) **without** `?-` and **with** the final period, e.g. `parent(ada, Child).` (5) Click **Run!** (or press Enter). (6) If more answers are possible, click **Next**. (7) To switch programs, delete all the old text first: two programs pasted together cause errors.

**Offline:** install SWI-Prolog from <https://www.swi-prolog.org>, then load a file with `consult('family.pl').` In the terminal, press `;` for the next answer and Enter to stop.

**No computer:** every activity below can be done on paper by tracing the facts from top to bottom. All expected answers were produced by running the real files (SWI-Prolog 10.1.20, the system behind SWISH, cross-checked with Tau Prolog 0.3.4).

**How to read answers in this guide** (the way the SWI-Prolog terminal prints them):

| You see | Meaning |
|---|---|
| `Child = zara ;` | An answer; more may follow. In SWISH, click **Next**. |
| `Child = leo.` | The **last** answer. |
| `false.` | No (more) answers. After other answers, it just means "I looked again and found nothing new". Not an error. |
| `true.` | Yes. |

SWISH shows each answer in its own box and may or may not show a final `false`. That is a display difference only: the answers and their order are the same.

---

## [PREDICT] Before you start (2 minutes)

1. A computer is told: "Grace is a parent of Ada" and "Ada is a parent of Zara". It has **no** fact about grandparents. Can it work out that Grace is Zara's grandparent? What would it need?
2. If you ask the computer "Is Pixel human?" and it has no fact either way, what should it answer: yes, no, or "I don't know"? What do you think it *will* answer?

---

## [TRY IT] Activity 3.1: Warm-up with Pixel's tiny knowledge base (10 minutes)

**Goal:** Run your first Prolog query and see the difference between a fact, a rule and a query.

**Preparation:** SWISH. This link opens SWISH with the program and the first query already loaded: [open Pixel's tiny knowledge base in SWISH](https://swish.swi-prolog.org/?code=%25%20Pixel%27s%20tiny%20knowledge%20base%20%28Curiosity%20Lab%29%0Arobot%28pixel%29.%0Arobot%28bolt%29.%0Ahuman%28ada%29.%0Alikes%28pixel%2C%20puzzles%29.%0Alikes%28ada%2C%20puzzles%29.%0Alikes%28bolt%2C%20oil%29.%0Afriends%28X%2C%20Y%29%20%3A-%20likes%28X%2C%20Z%29%2C%20likes%28Y%2C%20Z%29%2C%20X%20%5C%3D%20Y.%0A&q=friends%28pixel%2C%20Who%29.). If the link is blocked, paste this program by hand:

```prolog
% Pixel's tiny knowledge base (Curiosity Lab)
robot(pixel).
robot(bolt).
human(ada).
likes(pixel, puzzles).
likes(ada, puzzles).
likes(bolt, oil).
friends(X, Y) :- likes(X, Z), likes(Y, Z), X \= Y.
```

Read the rule aloud as: "X and Y are friends **IF** X likes some thing Z, **AND** Y likes that same Z, **AND** X is different from Y." (`\=` means "cannot be made equal".)

**Task:** **[PREDICT]** first, then run each query:
1. `friends(pixel, Who).`
2. `robot(R).`
3. `human(pixel).`
4. Add the fact `likes(bolt, puzzles).` under `likes(bolt, oil).` and run `friends(pixel, Who).` again.
5. Remove the fact you added in step 4. Then delete `, X \= Y` from the rule (keep the final period!) and run `friends(pixel, Who).` again.

**Observation:** Write each answer next to your prediction.

**Reflection:** In query 3, does `false` mean Prolog *knows* Pixel is not human?

**Feedback:**

<details>
<summary>[DEBRIEF] Warm-up answers (queries run on the live SWISH server and in SWI-Prolog)</summary>

| Query | Answer | Why |
|---|---|---|
| 1 `friends(pixel, Who).` | `Who = ada` (only answer) | Pixel and Ada both like puzzles. |
| 2 `robot(R).` | `R = pixel ;` `R = bolt` | Facts are read top to bottom. |
| 3 `human(pixel).` | `false.` | No fact says Pixel is human. |
| 4 after adding `likes(bolt, puzzles).` | `Who = ada ;` `Who = bolt.` | One new fact, one new conclusion. No new rule needed. |
| 5 original facts, `X \= Y` deleted | `Who = pixel ;` `Who = ada` | Pixel likes puzzles, and so does... Pixel. Without "X is different from Y", Pixel becomes its own friend. |

**Reflection:** No. `false` means "**cannot be proved** from the facts and rules I was given". Prolog assumes anything it cannot prove is false. This is called the **closed-world assumption**, and it is exactly Pixel's "Zara has no father!" mistake.
</details>

---

## [TRY IT] Activity 3.2: Facts, rules and queries in a family tree

**Goal:** Use rules to derive facts that nobody wrote down, and trace how Prolog finds each answer.

**Preparation:** Paste the program below into SWISH (it is [`family.pl`](../activities/prolog/family.pl) without its long comment box). Read the Prolog cheat sheet first.

**Prolog cheat sheet**

| Write | Means |
|---|---|
| `parent(grace, ada).` | A **fact**: "grace is a parent of ada". Every clause ends with a **period**. |
| `grace`, `ada` | **Atoms** (lowercase): fixed names of things. |
| `X`, `Child` | **Variables** (Uppercase): blanks Prolog tries to fill in. |
| `head :- a, b.` | A **rule**: "head is true **IF** a **AND** b". |
| `X \= Y` | "X and Y cannot be made equal" (are different). |
| `% text` | A comment; Prolog ignores it. |
| `parent(ada, Child).` in the query box | A **query** (a book writes it as `?- parent(ada, Child).`). |

```
     grace (f) ---+--- samuel (m)
                  |
         +--------+--------+
         |                 |
      ada (f)          tunde (m)
         |                 |
   +-----+-----+           |
   |           |           |
zara (f)    leo (m)     kemi (f)
```
*(A made-up family. Only one parent is recorded for zara, leo and kemi, to keep it small.)*

```prolog
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

% RULES
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
```

**Task:** For each query, write your **[PREDICT]**ion (answers and their order), then run it.

| # | Query | Question to think about before running |
|---|---|---|
| Q1 | `parent(ada, Child).` | How many answers, in which order? |
| Q2 | `male(ada).` | |
| Q3 | `father(F, ada).` | Which person passes **both** tests in the `father` rule? |
| Q4 | `father(F, zara).` | Zara obviously has a father in real life. What will Prolog say? |
| Q5 | `grandparent(G, zara).` | Which variable in the rule is the "link" between generations? |
| Q6 | `sibling(ada, S).` | Ada has exactly one brother. How many answers? |
| Q7 | `sibling(zara, S).` | Will leo appear once or twice? |
| Q8 | `ancestor(A, kemi).` | List the ancestors, then guess the order. |

**Observation:** Mark each prediction right or wrong. For Q6, fill in this trace table: which shared parent P produced each answer?

| Try | P (shared parent) | Y | Is ada different from Y? | Result |
|---|---|---|---|---|
| 1 | grace | ada | | |
| 2 | grace | tunde | | |
| 3 | samuel | ada | | |
| 4 | samuel | tunde | | |

**Reflection:** Which answers did Prolog derive that are **not written anywhere** as facts? What does `false` in Q4 really mean?

**Feedback:**

<details>
<summary>[DEBRIEF] Expected answers and explanations</summary>

| # | Expected answer | Explanation |
|---|---|---|
| Q1 | `Child = zara ;` `Child = leo.` | `Child` is a variable. Prolog reads facts **top to bottom**, so zara (written first) comes first. |
| Q2 | `false.` | There is no fact `male(ada).` |
| Q3 | `F = samuel.` | Prolog tries `parent(X, ada)`: first X = grace, but `male(grace)` fails, so it **backtracks** (goes back and tries the next possibility): X = samuel, and `male(samuel)` succeeds. The comma means AND. |
| Q4 | `false.` | Only **one** parent (ada, female) is recorded for zara. Missing data gives "false", not "unknown": the **closed-world assumption**. Pixel's "Zara has no father!" is wrong; the correct reading is "I cannot prove who zara's father is." |
| Q5 | `G = grace ;` `G = samuel ;` `false.` | `Y` is the link (the middle generation): grace is a parent of ada, and ada is a parent of zara. The final `false.` only means no more grandparents were found. |
| Q6 | `S = tunde ;` `S = tunde.` | **tunde appears twice, and that is not a bug.** Prolog lists every **proof**, not every person. Trace: try 1 rejected (ada \= ada fails); try 2 **S = tunde** (proof via grace); try 3 rejected; try 4 **S = tunde** (proof via samuel). Ada and tunde share two parents, so there are two proofs. (Optional: `setof(S, sibling(ada, S), Siblings).` gives `Siblings = [tunde].`, a sorted list without duplicates.) |
| Q7 | `S = leo.` | Only one parent (ada) is recorded for zara and leo, so there is only one proof. |
| Q8 | `A = tunde ;` `A = grace ;` `A = samuel ;` `false.` | `ancestor` is **recursive** (it uses itself). Clause 1, the **base case**, gives tunde (kemi's parent). Clause 2 walks the parent facts: grace is a parent of tunde, and tunde is an ancestor of kemi, so grace is too; the same for samuel. The base case is the bottom step of the staircase: without it the recursion would never stop. |

**Derived, not written:** every answer to Q3, Q5, Q6, Q7 and Q8 came from **rules**. No fact says "samuel is ada's father" or "grace is kemi's ancestor".

**Common mistakes:** predicting answers in "family order" rather than **file order**; thinking `false` means "known to be untrue"; expecting Prolog to remove duplicates by itself.
</details>

---

## [TRY IT] Activity 3.3: Extend the knowledge base

**Goal:** Add new knowledge and see how rules build on rules.

**Preparation:** The family program from Activity 3.2 in SWISH.

**Task:**

1. **Add a rule.** Add this line at the **end** of the program:
   ```prolog
   grandmother(X, Z) :- grandparent(X, Z), female(X).
   ```
   **[PREDICT]** then run `grandmother(G, leo).`
2. **Add a baby.** Kemi has a baby called tayo. Add `parent(kemi, tayo).` directly **after** `parent(tunde, kemi).`, and `male(tayo).` directly **after** `male(leo).` (Keep clauses with the same name together; SWI-Prolog warns about "discontiguous" clauses if you scatter them.) **[PREDICT]** You wrote no new rule. Will Prolog find tayo's great-grandparents? Run `ancestor(A, tayo).`
3. **Your own rule.** Start again from the original program (without tayo). Write a rule `aunt_or_uncle(A, N)`: "A is an aunt or uncle of N **IF** some P is a parent of N **AND** A is a sibling of P." Add it at the end, then run `aunt_or_uncle(A, kemi).` **[PREDICT]** how many answers first.

**Observation:** Record the answers. In step 2, note the **order** of the ancestors. In step 3, count the answers.

**Reflection:** In step 2, one new fact produced four ancestors. Which rule did the work? In step 3, why might the answer appear more than once?

**Feedback:**

<details>
<summary>[DEBRIEF] Expected answers</summary>

**Step 1:** `G = grace ;` `false.` A new rule can be built from **other rules**: `grandparent` does the family walking and `female` filters the result. (Samuel is also leo's grandparent, but not female.)

**Step 2:** `A = kemi ;` `A = grace ;` `A = samuel ;` `A = tunde ;` `false.` Yes: the **recursive** `ancestor` rule works for any number of generations. Notice the order: kemi (base case) comes first, then grace and samuel **before** tunde, because clause 2 checks the parent facts in **file order**, and the facts about grace and samuel come before `parent(tunde, kemi)`. Prolog's answer order follows the order of the program, not the order of the generations.

**Step 3:** one correct rule is
```prolog
aunt_or_uncle(A, N) :- parent(P, N), sibling(A, P).
```
`aunt_or_uncle(A, kemi).` gives `A = ada ;` `A = ada ;` `false.` (tested). P = tunde (kemi's parent), and ada is tunde's sibling, proved twice (via grace and via samuel), exactly like Q6. `setof(A, aunt_or_uncle(A, kemi), L).` gives `L = [ada].`

If you wrote the conditions the other way round, `sibling(A, P), parent(P, N)`, you get the same people, possibly in a different order. If you got `false.`, check for a lowercase `p` or `a` where you meant a variable (see Activity 3.5).
</details>

---

## [TRY IT] Activity 3.4: The robot troubleshooter (a tiny expert system)

**Goal:** See how a classic **expert system** works: human-written IF-THEN rules turn observed symptoms into a diagnosis, with a fallback when no rule applies.

**Preparation:** **Delete** the family program, then paste [`robot-troubleshooter.pl`](../activities/prolog/robot-troubleshooter.pl) (shown here without its comment box). Two new symbols: `\+ Goal` means "Goal **cannot be proved**" (negation as failure), and `_` means "anything, I don't care what".

```prolog
robot(pixel).
robot(widget).
robot(sprocket).
robot(gizmo).

% What the lab assistants observed today.
symptom(pixel, wont_power_on).
symptom(pixel, no_lights).
symptom(widget, drives_in_circles).
symptom(sprocket, bumps_into_walls).
symptom(sprocket, camera_blurry).
symptom(gizmo, squeaks).

% Dr. Okafor's diagnosis rules: IF symptoms THEN fault.
fault(Robot, flat_battery) :-
    symptom(Robot, wont_power_on),
    symptom(Robot, no_lights).
fault(Robot, loose_power_cable) :-
    symptom(Robot, wont_power_on),
    symptom(Robot, lights_on).
fault(Robot, stuck_wheel) :-
    symptom(Robot, drives_in_circles).
fault(Robot, dirty_sensor) :-
    symptom(Robot, bumps_into_walls),
    symptom(Robot, camera_blurry).

% What to do about each fault.
repair(flat_battery, charge_battery).
repair(loose_power_cable, reconnect_cable).
repair(stuck_wheel, clean_wheel_axle).
repair(dirty_sensor, wipe_camera_lens).

% Diagnosis with a FALLBACK when no fault can be proven.
diagnosis(Robot, Fault) :-
    fault(Robot, Fault).
diagnosis(Robot, no_diagnosis_ask_dr_okafor) :-
    robot(Robot),
    \+ fault(Robot, _).

% Chain two steps: diagnose, then look up the repair.
advice(Robot, Action) :-
    fault(Robot, Fault),
    repair(Fault, Action).
```

**Task:** **[PREDICT]** first, then run:

| # | Query | Think about |
|---|---|---|
| D1 | `symptom(pixel, S).` | What was observed? |
| D2 | `fault(pixel, F).` | Which rule fires? |
| D3 | `fault(R, stuck_wheel).` | Which robot? |
| D4 | `diagnosis(gizmo, D).` | Gizmo squeaks. Is there a rule for squeaks? |
| D5 | `diagnosis(R, D).` | All diagnoses: in which order? |
| D6 | `advice(sprocket, A).` | A chain: fault, then repair. |

Then **add expert knowledge**: put `fault(Robot, dry_joints) :- symptom(Robot, squeaks).` after the `dirty_sensor` rule, and `repair(dry_joints, oil_joints).` after `repair(dirty_sensor, wipe_camera_lens).` Run:

| # | Query |
|---|---|
| D7 | `diagnosis(gizmo, D).` |
| D8 | `advice(gizmo, A).` |

Finally, **start again from the original file**, add the fact `symptom(widget, lights_on).` after `symptom(gizmo, squeaks).`, and run D9 `fault(widget, F).` **[PREDICT]** Does widget now get a loose power cable?

**Observation:** Which queries used a single rule, which chained two steps, and which used the fallback?

**Reflection:** After D7, did Pixel get "smarter" by learning? Who supplied the new knowledge?

**Feedback:**

<details>
<summary>[DEBRIEF] Expected answers</summary>

| # | Expected answer | Why |
|---|---|---|
| D1 | `S = wont_power_on ;` `S = no_lights.` | Two symptom facts for pixel. |
| D2 | `F = flat_battery ;` `false.` | Pixel has both `wont_power_on` **and** `no_lights`. The loose-cable rule needs `lights_on`, which was not observed. |
| D3 | `R = widget.` | Widget drives in circles. |
| D4 | `D = no_diagnosis_ask_dr_okafor.` | No fault rule mentions `squeaks`, so `\+ fault(gizmo, _)` is true and the **fallback** answers. A good rule-based system admits it has no rule instead of guessing. |
| D5 | `R = pixel, D = flat_battery ;` `R = widget, D = stuck_wheel ;` `R = sprocket, D = dirty_sensor ;` `R = gizmo, D = no_diagnosis_ask_dr_okafor.` | The first `diagnosis` clause finds the three robots that have faults, in the order of the fault rules; the fallback clause then adds gizmo. |
| D6 | `A = wipe_camera_lens.` | `fault(sprocket, dirty_sensor)`, then `repair(dirty_sensor, wipe_camera_lens)`. |
| D7 | `D = dry_joints ;` `false.` | Now a fault **can** be proved, so the fallback no longer fires. |
| D8 | `A = oil_joints.` | The new fault chains to the new repair. |
| D9 | `F = stuck_wheel ;` `false.` | **No change.** The loose-cable rule needs `wont_power_on` **AND** `lights_on`, and widget only has `lights_on`. |

(The numbering D1 to D9 matches Part D of [`queries.md`](../activities/prolog/queries.md).)

**Reflection:** Pixel got "smarter" only because a human **wrote** new knowledge. Nothing was learned from data. This is the key difference from machine learning (Mission 04). It is also why the 1980s expert-system boom became expensive: every new case needs a new hand-written rule.
</details>

---

## [TRY IT] Activity 3.5: Find the bug

**Goal:** Debug rules that are grammatically correct but say the wrong thing, and learn why testing with known answers matters.

**Preparation:** **Delete** the troubleshooter and paste [`find-the-bug.pl`](../activities/prolog/find-the-bug.pl). It has the same family facts as Activity 3.2, but Pixel copied two rules with mistakes:

```prolog
% BUGGY RULE 1: Pixel thinks this finds brothers and sisters.
sibling(X, Y) :- parent(P, X), parent(P, Y).

% BUGGY RULE 2: Pixel thinks this finds mothers.
mother(X, Y) :- parent(X, Y), female(x).
```

The file loads with **no error message**.

**Task:** Run both queries and compare with what a correct program should say:

| # | Query | A correct program says | Pixel's buggy program says |
|---|---|---|---|
| E1 | `sibling(zara, S).` | `S = leo.` | `S = zara ;` `S = leo.` |
| E2 | `mother(M, zara).` | `M = ada.` | `false.` |

**[EXPLAIN]** Before opening the hints, write one sentence for each bug: what is wrong, and why does Prolog not complain? Then fix both rules and re-run E1 and E2.

**Observation:** Did your fixed program give `S = leo.` and `M = ada.`?

**Reflection:** Both bugs were silent. How did you discover them?

<details>
<summary>Hint 1</summary>
E1: Pixel thinks zara is her own sister. Which condition from the correct sibling rule in Activity 3.2 is missing?
</details>

<details>
<summary>Hint 2</summary>
E2: Compare <code>female(x)</code> with <code>female(X)</code>. What does a lowercase first letter mean in Prolog?
</details>

**Feedback:**

<details>
<summary>[DEBRIEF] Fixes and explanation</summary>

**Bug 1 (missing condition):** `sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.` Without `X \= Y`, `parent(ada, zara), parent(ada, zara)` proves `sibling(zara, zara)`: everyone becomes their own sibling (just like Pixel becoming its own friend in Activity 3.1).

**Bug 2 (an atom where a variable was meant):** `mother(X, Y) :- parent(X, Y), female(X).` Lowercase `x` is an **atom**, a fixed name like `grace`, so `female(x)` asks "is the thing called x female?". There is no such fact, so the rule always fails. Uppercase `X` is a **variable** that refers to the parent found by `parent(X, Y)`.

**After fixing** (tested): E1 gives `S = leo.` and E2 gives `M = ada.`

**Why no error message?** Both buggy rules are grammatically correct Prolog. Prolog checks the **form** of your rules, not whether they mean what you intended. That is why we test with cases whose answers we already know, a habit that matters for every AI system, not just Prolog.
</details>

---

## [OBSERVE] What kind of "thinking" was that?

Look back at Activities 3.1 to 3.5 and answer:

1. Where did every piece of Pixel's knowledge come from?
2. Could you explain **why** Prolog gave each answer, by pointing to the facts and rules it used?
3. What happened when a case came up that no rule covered (gizmo's squeak, zara's father)?

---

## [EXPLAIN] Rule-based systems and expert systems

### Facts, rules and queries

A **rule-based** (symbolic) system stores knowledge as explicit, human-readable statements:

- **Facts:** things that are simply true (`parent(grace, ada).`, `symptom(gizmo, squeaks).`).
- **Rules:** IF-THEN knowledge that lets the system derive new facts (`grandparent(X, Z) :- parent(X, Y), parent(Y, Z).`).
- **Queries:** questions the system answers by reasoning from facts and rules.

### How Prolog reaches a conclusion

Prolog proves a query by **matching** it against facts and the heads (left-hand sides) of rules. For a rule, it then tries to prove each condition in the body **from left to right**. If a condition fails, it **backtracks**: it goes back and tries the next possibility. It reports **every proof** it finds, which is why duplicates appear (Q6). A **recursive** rule uses itself, with a **base case** to stop. Because the order of facts and rules decides the search order, it also decides the order of answers.

Anything Prolog cannot prove counts as false: the **closed-world assumption**. A missing fact (zara's father) looks exactly the same as a fact that is really false.

> **Playful analogy:** Pixel is a very literal librarian with a box of index cards. Asked a question, it flips through the cards in order and follows any "see also" notes (rules), writing down every path that leads to an answer. If no card helps, it says "no", even when the truth is "nobody gave me that card".
>
> **Technically speaking:** Prolog uses resolution with depth-first search and backtracking over the clauses in program order, and treats failure to prove as falsity (negation as failure). This guide uses only a small part of Prolog: no lists, arithmetic or cut.

### Expert systems: rule-based AI at work

An **expert system** stores the knowledge of human specialists as many IF-THEN rules, just like the robot troubleshooter. A famous early example is **MYCIN**, developed at Stanford in the early 1970s to help doctors identify bacterial blood infections and choose antibiotics. It used roughly **600 rules** of the form "IF the organism is gram-negative AND rod-shaped AND anaerobic, THEN there is suggestive evidence that it is *Bacteroides*". MYCIN was tested on real cases but was not put into routine clinical use.

| Strengths of rule-based systems | Weaknesses |
|---|---|
| **Explainable:** they can show exactly which rules fired (MYCIN could explain its conclusions). | **Costly to build and maintain:** every rule must be written and checked by hand with experts. |
| **Precise and predictable:** the same input always gives the same answer. | **Brittle:** they fail (or fall back) on any case their rules do not cover. |
| **No training data needed.** | **Cannot learn:** they improve only when a person adds rules. |
| Ideal for clear, stable rules: tax calculations, eligibility checks, puzzles, route search. | Poor at messy patterns: faces, speech, spam that keeps changing. |

These weaknesses are part of why the 1980s expert-system boom ended in disappointment (Mission 08). They are also why the next mission turns the problem around: instead of writing the rules, **let the computer learn them from examples**.

For more depth, read [Topic 02, sections 2 and 4](../../task-1/topics/02-how-ai-operates.md).

---

## [LAB NOTE] What these activities leave out

- **Closed world:** Prolog treats anything it cannot prove as false. Real-world reasoning often needs "unknown".
- **Toy knowledge bases:** a 7-person family and 4 robots. Real expert systems had hundreds or thousands of rules, and experts often disagreed about them.
- **No uncertainty:** the troubleshooter's rules are all-or-nothing. Real diagnosis deals with "probably" and "sometimes"; some historical expert systems added certainty factors for this.
- **Display differs between Prolog systems** (SWISH's **Next** buttons, a terminal's `;`, a final `false.` or not). The answers and their order are the same.
- SWISH is a shared public server: it may occasionally be busy, and saved programs are public by default.

---

## [WATCH] No video this time

No curated video fits this mission; the activities are your demonstration.

## [OPTIONAL SIDE QUEST] More queries (about 20 minutes)

The complete [query worksheet](../activities/prolog/queries.md) has 31 tested queries with predictions and hidden, explained answers. Try the ones not used above: `ancestor(grace, D).` (all of grace's descendants), `father(X, Y).` (every father-child pair) and `setof(S, sibling(ada, S), Siblings).` (siblings without duplicates). Predict each answer first; the worksheet shows the expected output from SWI-Prolog.

---

## [APPLY] Rules or learning?

For each task, choose **rule-based** or **machine learning**, and justify your choice in one sentence using the strengths-and-weaknesses table.

1. Calculating sales tax at 8% on a shopping bill.
2. Recognizing spoken commands ("Call Mom") from many different voices and accents.
3. Checking that a new password has at least 8 characters.
4. Suggesting films a viewer might enjoy.
5. Finding the shortest sequence of moves to solve a sliding-tile puzzle.
6. Deciding whether a customer qualifies for a student discount (rule: under 26 with a valid student card).

<details>
<summary>[DEBRIEF] Apply: expected answers</summary>

1. **Rule-based.** The rule is exact and stable (multiply by 0.08); learning it from data would be pointless and less reliable.
2. **Machine learning.** Voices vary endlessly; no one could write rules for every voice, so the system must learn patterns from many recorded examples.
3. **Rule-based.** One simple, exact rule that never changes.
4. **Machine learning.** Tastes are messy and change; patterns are found in what many viewers watched.
5. **Rule-based (search).** States, moves and goal are fully known, so the computer can search for the shortest solution, as in Mission 02.
6. **Rule-based.** The rule is clear, stable and must be explainable to the customer.

Other well-justified answers can be accepted. The key test: **can the knowledge be written down exactly, and does it stay stable?** If yes, rules work well. If the pattern is messy or keeps changing, learning is usually better.
</details>

---

## [CHECK] Quick self-check

1. In Prolog, what is the difference between `ada` and `Ada`?
2. Translate into plain English: `father(X, Y) :- parent(X, Y), male(X).`
3. `sibling(ada, S).` returns tunde twice. Is that a bug? Explain.
4. True or false: "When Prolog answers `false` to `father(F, zara).`, it has found that zara has no father."
5. Give one strength and one weakness of expert systems such as MYCIN.

---

## [DEBRIEF] Check answers

<details>
<summary>Show answers with explanations</summary>

1. `ada` (lowercase) is an **atom**, a fixed name. `Ada` (uppercase) is a **variable**, a blank Prolog tries to fill. Mixing them up is exactly Bug 2 in Activity 3.5.
2. "X is the father of Y **if** X is a parent of Y **and** X is male."
3. **Not a bug.** Prolog lists every **proof**. Ada and tunde share two parents (grace and samuel), so there are two different proofs. `setof/3` collects the distinct people if that is what you want.
4. **False.** It means Prolog **cannot prove** who zara's father is from the facts it was given (the closed-world assumption). The program simply records only one parent for zara.
5. Strengths (any one): can explain its conclusions by showing the rules used; precise and predictable; no training data needed. Weaknesses (any one): rules must be written and maintained by hand by experts (costly); brittle when a case is not covered; cannot learn by itself.

**Now look back at your [PREDICT] answers.** The computer can work out grandparents **if** it has a rule linking two parent facts. And to "Is Pixel human?" it answers `false`, not "I don't know".
</details>

---

## Mission summary

- A **rule-based system** has **facts**, **rules** (IF-THEN) and **queries**; in Prolog, `:-` means IF, `,` means AND, lowercase words are **atoms** and Uppercase words are **variables**.
- Prolog derives new facts by matching and **backtracking**, reports **every proof** (hence duplicates), and handles any number of generations with a **recursive** rule.
- **Closed world:** whatever cannot be proved counts as false, so missing facts look like "no".
- **Expert systems** such as MYCIN (roughly 600 rules) are explainable and predictable, but costly to build, **brittle**, and unable to learn: they get smarter only when a human adds rules.
- Rules that load without errors can still be wrong: **test with cases whose answers you know**.

## Next mission

Writing rules for every spam trick or every face would never end. In [Mission 04: Learning from Examples](mission-04-learning-from-examples.md), Pixel stops being given rules and starts **learning them from labeled data**.
