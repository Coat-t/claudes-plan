# Pixel's Prolog Missions: Query Sheet

**Pixel's AI Field Guide: Missions for Curious Humans** · Prolog supplement · Version 1.0 · 2026-11-06

This sheet goes with `family.pl`, `robot-troubleshooter.pl` and `find-the-bug.pl`. Every query below was run on 2026-11-06. The expected answers come from **SWI-Prolog 10.1.20** (the Prolog system behind SWISH) running through swipl-wasm 8.3.0. They were cross-checked with **Tau Prolog 0.3.4**. The full raw log is in [`test-output.txt`](test-output.txt).

> **How to use this sheet.** For each query: (1) read it, (2) **write down your prediction**, (3) run it, (4) compare. A wrong prediction is useful because it shows you exactly which rule you misread.

---

## 0. Setting up SWISH (about 3 minutes)

SWISH ("SWI-Prolog for SHaring") is a free website at <https://swish.swi-prolog.org> that runs Prolog in your browser. You do **not** need an account to run programs. A Google or StackOverflow login is optional and is only needed if you want to save programs on the site. You do need an internet connection.

1. Open <https://swish.swi-prolog.org>.
2. In the program panel, make sure **Empty** is selected, then click **Program**. A blank program editor opens on the left.
3. Open `family.pl` in any text editor (Notepad, TextEdit, or the browser). Copy **everything** and paste it into the SWISH program editor. You do not need to save before running.
4. Type a query in the **query box** (bottom right). Type it **without** the `?-` and **with** the final period, for example `parent(ada, Child).`
5. Click **Run!** (or press Enter). The first answer appears in the results panel (top right).
6. If more answers are possible, SWISH shows a **Next** button (plus buttons for 10, 100 or 1,000 more answers, and **Stop**). Click **Next** until SWISH says `false` or the buttons disappear.
7. To switch programs (for Part D), select all the text in the editor, delete it, and paste the next file. Pasting two files into the same editor causes errors.

**How to read the answers in this sheet.** They are written the way the SWI-Prolog terminal prints them:

| You see | Meaning |
|---|---|
| `Child = zara ;` | An answer. The `;` means "Prolog may have more answers. Ask for the next one." In SWISH you click **Next**. |
| `Child = leo.` | An answer ending in `.` is the **last** answer. Prolog knows nothing else can match. |
| `false.` | No (more) answers. After other answers, it means Prolog searched again and found nothing new. That is **not** an error. |
| `true.` | A yes/no question whose answer is yes. |

> **[LAB NOTE] SWISH and Tau Prolog look a little different.** SWISH shows each answer in its own box and uses **Next** buttons instead of `;`. It may or may not show a final `false` after the last answer. Tau Prolog (and some other Prologs) **always** ends with `false.` because it checks one more time before stopping. These are display differences only. **The answers themselves, and their order, are the same** in every query below (see `test-output.txt`). If your screen differs only in this way, your result is correct.

---

## Part A: Facts only (`family.pl`)

The family tree, for reference (a made-up family):

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

### A1. Is grace a parent of ada?
```prolog
?- parent(grace, ada).
```
**[PREDICT]** true or false?
<details><summary>Expected answer</summary>

```
true.
```
The fact `parent(grace, ada).` is written in the file word for word, so Prolog finds it straight away. (Tau Prolog prints `true ; false.`)
</details>

### A2. Who are ada's children?
```prolog
?- parent(ada, Child).
```
**[PREDICT]** How many answers? In which order?
<details><summary>Expected answer</summary>

```
Child = zara ;
Child = leo.
```
`Child` starts with a capital letter, so it is a **variable**, a blank for Prolog to fill. Prolog reads the facts **from top to bottom**, so zara (written first) comes before leo.
</details>

### A3. Who are ada's parents?
```prolog
?- parent(Who, ada).
```
<details><summary>Expected answer</summary>

```
Who = grace ;
Who = samuel.
```
The variable can go in **any** position. The same fact can answer "who are the children?" and "who are the parents?".
</details>

### A4. Is ada male?
```prolog
?- male(ada).
```
<details><summary>Expected answer</summary>

```
false.
```
There is no fact `male(ada).`, so Prolog answers false. Careful: false here means **"I cannot prove it from what I was told"**, not "I checked the real world". This is called the **closed-world assumption**: anything not in the program counts as false.
</details>

---

## Part B: Rules (`family.pl`)

### B1. Who is ada's father?
```prolog
?- father(F, ada).
```
**[PREDICT]** Look at the rule `father(X, Y) :- parent(X, Y), male(X).` Which person passes **both** tests?
<details><summary>Expected answer</summary>

```
F = samuel.
```
Prolog tries `parent(X, ada)`: first X = grace, but `male(grace)` fails, so it **backtracks** (goes back and tries the next possibility). Next X = samuel, and `male(samuel)` succeeds. The comma means AND, so both conditions must hold.
</details>

### B2. Who is zara's mother?
```prolog
?- mother(M, zara).
```
<details><summary>Expected answer</summary>

```
M = ada.
```
</details>

### B3. Who is zara's father?
```prolog
?- father(F, zara).
```
**[PREDICT]** Zara obviously has a father in real life. What will Prolog say?
<details><summary>Expected answer</summary>

```
false.
```
The program only records **one** parent for zara (ada, who is female). Prolog knows only what it is told. Missing data gives "false", not "unknown". Expert systems have the same weakness: missing facts look like "no".
</details>

### B4. Who are zara's grandparents?
```prolog
?- grandparent(G, zara).
```
<details><summary>Expected answer</summary>

```
G = grace ;
G = samuel ;
false.
```
The rule `grandparent(X, Z) :- parent(X, Y), parent(Y, Z).` uses `Y` as the **link** (the middle generation). For G = grace, Prolog tries Y = ada, and `parent(ada, zara)` is true. The final `false.` only means Prolog checked the remaining parent facts and found no more grandparents.
</details>

### B5. Who are grace's grandchildren?
```prolog
?- grandparent(grace, GC).
```
<details><summary>Expected answer</summary>

```
GC = zara ;
GC = leo ;
GC = kemi.
```
</details>

### B6. Who are ada's siblings? (Pixel's favorite surprise)
```prolog
?- sibling(ada, S).
```
**[PREDICT]** Ada has exactly one brother. How many answers will Prolog give?
<details><summary>Expected answer and why there is a duplicate</summary>

```
S = tunde ;
S = tunde.
```
**tunde appears twice. This is not a bug in Prolog.** The rule is `sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.` Prolog lists every **way of proving** the query (every proof), not every distinct person:

| Try | P (shared parent) | Y | `X \= Y` (ada different from Y?) | Result |
|---|---|---|---|---|
| 1 | grace | ada | ada \= ada fails | rejected |
| 2 | grace | tunde | ada \= tunde succeeds | **S = tunde** (proof via grace) |
| 3 | samuel | ada | fails | rejected |
| 4 | samuel | tunde | succeeds | **S = tunde** (proof via samuel) |

Ada and tunde share **two** parents, so there are two separate proofs. `\=` means "cannot be made equal". Here it stops Prolog from saying ada is her own sibling (rows 1 and 3). If you want each sibling only once, see B12.
</details>

### B7. Who are zara's siblings?
```prolog
?- sibling(zara, S).
```
**[PREDICT]** Will leo appear once or twice? Why is this different from B6?
<details><summary>Expected answer</summary>

```
S = leo.
```
Only **one** parent (ada) is recorded for zara and leo, so there is only one proof.
</details>

### B8. Who are kemi's siblings?
```prolog
?- sibling(kemi, S).
```
<details><summary>Expected answer</summary>

```
false.
```
Tunde has only one child in the program. Kemi's cousins zara and leo are **not** siblings, because they do not share a parent.
</details>

### B9. Who are kemi's ancestors? (recursion)
```prolog
?- ancestor(A, kemi).
```
**[PREDICT]** List the ancestors you expect, then guess the order.
<details><summary>Expected answer</summary>

```
A = tunde ;
A = grace ;
A = samuel ;
false.
```
`ancestor/2` is **recursive**: one of its clauses uses `ancestor` again.
- Clause 1 (the **base case**): `ancestor(X, Y) :- parent(X, Y).` This gives tunde (kemi's parent).
- Clause 2 (the **recursive case**): `ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).` Prolog walks through the parent facts. grace is a parent of ada, but is ada an ancestor of kemi? No. grace is a parent of tunde, and tunde **is** an ancestor of kemi, so grace is too. samuel is found the same way.

The base case is the bottom step of the staircase. Without it, the recursion would never stop.
</details>

### B10. Who are grace's descendants?
```prolog
?- ancestor(grace, D).
```
<details><summary>Expected answer</summary>

```
D = ada ;
D = tunde ;
D = zara ;
D = leo ;
D = kemi ;
false.
```
Clause 1 finds grace's children first (ada, tunde). Clause 2 then finds their descendants: ada's children (zara, leo), then tunde's child (kemi).
</details>

### B11. List every father-child pair
```prolog
?- father(X, Y).
```
<details><summary>Expected answer</summary>

```
X = samuel,
Y = ada ;
X = samuel,
Y = tunde ;
X = tunde,
Y = kemi.
```
When both arguments are variables, Prolog lists every pair that makes the rule true. (Leo is male but has no children in the program.)
</details>

### B12. Collect siblings without duplicates (optional)
```prolog
?- setof(S, sibling(ada, S), Siblings).
```
<details><summary>Expected answer</summary>

```
Siblings = [tunde].
```
`setof/3` collects all answers for `S` into a **sorted list without duplicates**. This is one way to fix B6's double answer when you only care about the people, not the proofs. (Tau Prolog prints `Siblings = [tunde] ; false.`)
</details>

---

## Part C: Your turn (extend `family.pl`)

### C1. Write a `grandmother` rule
Add this line to the **end** of `family.pl` (after the two `ancestor` lines):
```prolog
grandmother(X, Z) :- grandparent(X, Z), female(X).
```
Then run:
```prolog
?- grandmother(G, leo).
```
<details><summary>Expected answer</summary>

```
G = grace ;
false.
```
A new rule can be built from **other rules**: `grandparent` does the family walking and `female` filters the result. Rules stack up like building blocks.
</details>

### C2. Add a new baby
Kemi has a baby called tayo. Add `parent(kemi, tayo).` directly **after** the line `parent(tunde, kemi).`, and add `male(tayo).` directly **after** `male(leo).` (Keep clauses with the same name together. SWI-Prolog warns about "discontiguous" clauses if you scatter them.) Then run:
```prolog
?- ancestor(A, tayo).
```
**[PREDICT]** You did not write any new rule. Will Prolog find tayo's great-grandparents?
<details><summary>Expected answer</summary>

```
A = kemi ;
A = grace ;
A = samuel ;
A = tunde ;
false.
```
Yes. The recursive rule works for **any** number of generations, so one new fact gives four ancestors. Notice the order: kemi (base case) comes first, then grace and samuel **before** tunde. Clause 2 checks the parent facts in file order, and the facts about grace and samuel come before `parent(tunde, kemi)`. Prolog's answer order follows the **order of the program**, not the order of the generations.
</details>

---

## Part D: The robot troubleshooter (`robot-troubleshooter.pl`)

Replace the program in SWISH with `robot-troubleshooter.pl`. It is a tiny **expert system**: human-written IF-THEN rules diagnose made-up faults in the Curiosity Lab's robots.

| Query | **[PREDICT]** first, then check | Expected answer |
|---|---|---|
| D1 `symptom(pixel, S).` | What was observed? | `S = wont_power_on ;` `S = no_lights.` |
| D2 `fault(pixel, F).` | Which rule fires? | `F = flat_battery ;` `false.` |
| D3 `fault(R, stuck_wheel).` | Which robot has a stuck wheel? | `R = widget.` |
| D4 `diagnosis(gizmo, D).` | Gizmo squeaks. Is there a rule for squeaks? | `D = no_diagnosis_ask_dr_okafor.` |
| D5 `diagnosis(R, D).` | All diagnoses | `R = pixel, D = flat_battery ;` `R = widget, D = stuck_wheel ;` `R = sprocket, D = dirty_sensor ;` `R = gizmo, D = no_diagnosis_ask_dr_okafor.` |
| D6 `advice(sprocket, A).` | Chain: fault, then repair | `A = wipe_camera_lens.` |

<details><summary>Why these answers?</summary>

- **D2:** Pixel has both `wont_power_on` **and** `no_lights`, so the flat-battery rule fires. The loose-cable rule needs `lights_on`, which was not observed, so it fails. The final `false.` is Prolog checking the remaining fault rules.
- **D4:** No fault rule mentions `squeaks`, so `\+ fault(gizmo, _)` ("no fault can be proven") is true and the **fallback** clause answers. A good rule-based system admits when it has no rule instead of guessing.
- **D5:** The first `diagnosis` clause finds the three robots that have faults, in the order of the fault rules. The second (fallback) clause then adds gizmo.
- **D6:** `advice` **chains** two steps: `fault(sprocket, dirty_sensor)`, then `repair(dirty_sensor, wipe_camera_lens)`.
</details>

### D7 to D9. Add expert knowledge
1. Add `fault(Robot, dry_joints) :- symptom(Robot, squeaks).` **after** the dirty-sensor rule (the last `fault` rule), and add `repair(dry_joints, oil_joints).` **after** `repair(dirty_sensor, wipe_camera_lens).` Then ask:

| Query | Expected answer |
|---|---|
| D7 `diagnosis(gizmo, D).` | `D = dry_joints ;` `false.` |
| D8 `advice(gizmo, A).` | `A = oil_joints.` |

The fallback no longer fires, because now a fault **can** be proven. The program got "smarter" only because a human **wrote** new knowledge. Nothing was learned from data. This is the key difference from machine learning (see the spam-filter activity).

2. Start again from the original file. Add the fact `symptom(widget, lights_on).` after `symptom(gizmo, squeaks).` and ask:

| Query | **[PREDICT]** Does widget now get a loose power cable? | Expected answer |
|---|---|---|
| D9 `fault(widget, F).` | | `F = stuck_wheel ;` `false.` |

No change. The loose-cable rule needs `wont_power_on` **AND** `lights_on`, and widget only has `lights_on`. The comma means **both** conditions must be true.

---

## Part E: Find the bug (`find-the-bug.pl`)

Pixel copied two rules but made two mistakes. **The file loads with no error message.** Load `find-the-bug.pl` into SWISH and run:

| Query | What a correct program should say | What Pixel's buggy program says |
|---|---|---|
| E1 `sibling(zara, S).` | `S = leo.` | `S = zara ;` `S = leo.` |
| E2 `mother(M, zara).` | `M = ada.` | `false.` |

**[EXPLAIN]** Before opening the hints, write one sentence for each bug: what is wrong, and why does Prolog not complain?

<details><summary>Hint 1</summary>
E1: Pixel thinks zara is her own sister. Which condition in `family.pl`'s sibling rule is missing?
</details>

<details><summary>Hint 2</summary>
E2: Compare <code>female(x)</code> with <code>female(X)</code>. What does a lowercase first letter mean in Prolog?
</details>

<details><summary>Fixes and explanation</summary>

**Bug 1 (missing condition):**
```prolog
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
```
Without `X \= Y`, `parent(ada, zara), parent(ada, zara)` proves `sibling(zara, zara)`. Everyone becomes their own sibling.

**Bug 2 (an atom where a variable was meant):**
```prolog
mother(X, Y) :- parent(X, Y), female(X).
```
`x` (lowercase) is an **atom**, a fixed name like `grace`. So `female(x)` asks "is the thing called x female?". There is no such fact, so the rule always fails. `X` (uppercase) is a **variable** that refers to the parent found by `parent(X, Y)`.

**After fixing**, the queries give the correct answers (tested):

| Query | Expected answer |
|---|---|
| E3 `sibling(zara, S).` | `S = leo.` |
| E4 `mother(M, zara).` | `M = ada.` |

**Why no error message?** Both buggy rules are grammatically correct Prolog. Prolog checks the **form** of your rules, not whether they mean what you intended. That is why we test with cases whose answers we already know.
</details>

---

## Test record

- **Date:** 2026-11-06
- **Engines:** SWI-Prolog 10.1.20 (swipl-wasm 8.3.0, the same Prolog system SWISH runs) and Tau Prolog 0.3.4 (npm package `tau-prolog`), on Node v26.10.0.
- **Script:** `test_queries.cjs` loads each `.pl` file (and, for Parts C, D7 to D9 and E3/E4, the edited versions described above) and runs every query in this sheet with both engines. The answers matched in all 31 cases. The only differences were the display differences explained in the LAB NOTE (Tau Prolog ends with `; false.`).
- **Not tested:** the live SWISH web page itself was not driven by the test script, so the button names come from SWISH's help page and a published tutorial. If SWISH changes its layout, the steps in Section 0 may look slightly different.
