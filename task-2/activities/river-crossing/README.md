# Mission: Get Everyone Across the River (state-space search)

**Pixel's AI Field Guide: Missions for Curious Humans** · Supplement · Version 1.0 · 2026-11-06
Belongs to: Mission 02 (The River Problem: rule-based / symbolic AI, state-space search). Also connects to Mission 08 (Time Machine: early "good old-fashioned AI"). Optional follow-up: the side quest `../robot-maze/` compares search with a fixed rule and with reinforcement learning.

**[MISSION BRIEF]** A farmer must get a wolf (W), a goat (G) and a cabbage (C) across a river. The boat holds the farmer (F) plus **at most one** passenger, and only the farmer can row. If the farmer is not there, the wolf eats the goat and the goat eats the cabbage. Pixel refuses to guess, so it **searches** systematically. Can you solve it first?

| File | What it is |
|---|---|
| `river-crossing.html` | Interactive puzzle: play it, see the 16-state "state space", and watch Pixel's breadth-first search step by step. A single file that works offline. |
| `solver.py` | The same search in Python (standard library only). It prints every search step and all shortest solutions. |
| `solver-output.txt` | Full output of `solver.py`, usable as a printed trace. |
| `test_logic.mjs`, `test_logic-output.txt` | Automated tests of the game logic inside the HTML page (Node.js, no packages). |
| `test_ui.cjs`, `test_ui-output.txt` | Optional simulated-browser test that presses the real buttons (needs the `jsdom` package, which is **not** included in this folder). |

The state-space diagram `../../assets/images/river-crossing-state-graph.svg` shows the same 10 valid states and the solution path.

---

## Goal
- Describe a problem as a **state space**: **states**, allowed **actions**, **constraints** that make some states invalid, a **start state** and a **goal state**.
- Explain why tempting moves fail.
- Follow **breadth-first search (BFS)**: a frontier (queue), a visited set, and why BFS finds a plan with the **fewest** crossings.
- Recognize this as **rule-based, search-based AI**: no learning from data is involved.

## Preparation
- **Knowledge:** Mission 01 (what counts as AI). This page is the main hands-on activity of Mission 02. No programming is needed.
- **Tools (choose one):**
  - **Interactive page:** download `river-crossing.html` and open it in any modern web browser (Chrome, Edge, Firefox, Safari), on a computer or tablet. **No internet connection, account or installation needed.** The page loads nothing from the web. Every button works with the keyboard (Tab, then Enter or Space).
  - **Paper version:** 4 small cards labelled F, W, G, C, and a sheet of paper with a river drawn down the middle.
  - **Optional:** Python 3.8+ to run `python3 solver.py`.
- **Time:** about 30 to 40 minutes.

## Task (step by step)
1. **[PREDICT]** Before touching anything: which passenger should the farmer take first? Why?
2. **[TRY IT]** In section 1 of the page ("Play the puzzle"), click an item on the farmer's bank to put it in the boat (click it again to take it out), then click **Row the boat**. Try taking the **wolf** first. Read Pixel's message.
3. Keep playing until everyone is on the right bank. **Undo last crossing** and **Start over** are allowed. The **Move history** panel logs each crossing and the state after it. Copy your log onto paper.
4. **[OBSERVE]** In section 2 ("The state space"), click **Show state space**. Count the valid (solid border) and invalid (red, dashed) states. Which ones did you visit?
5. **[PREDICT]** In section 3 ("Watch Pixel search"), guess how many crossings Pixel's plan will need. Then click **Next search step** repeatedly (or **Play automatically**). At each step, watch which state leaves the **frontier** and which states join the **visited** set.
6. **[EXPLAIN]** For each of Pixel's rejected moves at step 1, explain **why** it is rejected.
7. **[APPLY]** The page says there is a **second** 7-crossing plan (hint: at step 3, take the cabbage instead of the wolf). Find it and write it in `(left | right)` notation.

## Observation questions
1. List the four actions that are possible in **every** state. Which of them are sometimes impossible, and why?
2. Of the 16 ways to place F, W, G and C on two banks, how many are valid? Write down two invalid ones and the rule each one breaks.
3. Which move is tempting but fails at the very start? Which move fails in the middle of the puzzle?
4. In the BFS trace, how many states did Pixel take from the frontier before reaching the goal?
5. Why does the solution need the goat to travel **back** to the left bank once?

## Reflection
- How is Pixel's search different from your own trial and error? What does the **visited** set stop Pixel from doing?
- Why does breadth-first search guarantee the **shortest** plan (fewest crossings)?
- This puzzle has only 16 states. A chess game has more possible positions than anyone could list. What would go wrong if Pixel tried BFS on chess?
- Is this "AI"? Which parts of an intelligent system does it show (planning, reasoning) and which does it lack (learning, perception)?

## Feedback: expected results
<details><summary>[DEBRIEF] Open after you have tried</summary>

**States:** 16 placements, of which **10 are valid**:
`(FWGC | -) (FWG | C) (FWC | G) (FGC | W) (FG | WC) (WC | FG) (W | FGC) (G | FWC) (C | FWG) (- | FWGC)`.
The **6 invalid** ones are `(WGC | F)`, `(GC | FW)`, `(WG | FC)` and their mirror images `(F | WGC)`, `(FW | GC)`, `(FC | WG)`: the farmer has left the wolf with the goat, or the goat with the cabbage.

**Actions:** farmer crosses alone, or with the wolf, the goat or the cabbage. Taking an item is only possible if it is on the **farmer's** bank.

**Tempting moves that fail:** at the start, taking the wolf leaves the goat with the cabbage `(GC | FW)`. Taking the cabbage leaves the wolf with the goat `(WG | FC)`. Crossing alone leaves all three together. Only **the goat first** works. In the middle, after the wolf is across `(C | FWG)`, rowing back alone would leave the wolf with the goat on the right bank. That is why the goat must come back.

**BFS result (Pixel's plan, 7 crossings, 10 valid states visited).** Pixel takes 10 states from the frontier; the 10th is the goal. In this puzzle BFS happens to find every valid state before it reaches the goal.
1. Farmer takes the goat to the right bank: (FWGC | -) -> (WC | FG)
2. Farmer crosses alone to the left bank: (WC | FG) -> (FWC | G)
3. Farmer takes the wolf to the right bank: (FWC | G) -> (C | FWG)
4. Farmer takes the goat to the left bank: (C | FWG) -> (FGC | W)
5. Farmer takes the cabbage to the right bank: (FGC | W) -> (G | FWC)
6. Farmer crosses alone to the left bank: (G | FWC) -> (FG | WC)
7. Farmer takes the goat to the right bank: (FG | WC) -> (- | FWGC)

**Second shortest plan:** identical except steps 3 to 5: take the **cabbage** across `(W | FGC)`, bring the goat back `(FWG | C)`, take the **wolf** across `(G | FWC)`. There are exactly **2** shortest plans (see `solver-output.txt`).

**Reflection key points:** the visited set prevents going round in circles. BFS explores all 1-crossing states, then all 2-crossing states, and so on, so the first time it reaches the goal it has used the fewest crossings. On huge problems such as chess, listing every state is impossible, so real systems use heuristics (informed guesses about which states look promising, as in A* search) or learning. This is **rule-based search**: the rules of the puzzle were written by a human, and Pixel learned nothing from data.
</details>

## [LAB NOTE] Limitations
- The page is a **toy model**: perfect information, instant crossings, animals that always behave the same way, one goal, and every crossing costing the same.
- BFS here looks at every state. That is fine for 10 states, but real planning problems (delivery routes, robot motion, games) have astronomically many states, uncertainty and different costs. They need smarter search (for example, A* with a heuristic) or other methods.
- Pixel is a fictional character. The "search" in the page is a real BFS algorithm, but the robot's personality is just for fun.

## Fallback if the page cannot be opened
- **Paper version:** use the four cards and act out each crossing. Record each state in `(left | right)` notation. Then compare your record with the trace in `solver-output.txt`, which lists every BFS step: which state leaves the frontier, which crossings are rejected and why, and the frontier and visited set after each step.
- **No device at all:** use the state-space diagram (`river-crossing-state-graph.svg`) printed on paper. Cross out invalid states, draw arrows for allowed crossings, and trace a path from start to goal.

## Test evidence
Run on 2026-11-06 (re-run in full after the activity was finished; outputs were identical to the saved files):
- `node test_logic.mjs`: **8 of 8 tests passed** (Node v26.10.0, no packages). It extracts the game logic from the HTML file, so it tests exactly the code learners run. It checks: 10 of 16 states valid, all 10 reachable, invalid moves rejected with explanations, BFS finds a working 7-crossing plan. Output: `test_logic-output.txt`.
- `NODE_PATH=<folder>/node_modules node test_ui.cjs`: **all UI checks passed** (jsdom 31.0.0, Node v26.10.0). To run it, install jsdom in any temporary folder (`npm install jsdom`) and point `NODE_PATH` at that folder's `node_modules`; jsdom is not shipped with this activity and learners never need it. It checks: the page has no external resources; the real buttons reject the wolf-first move; the 7-crossing solution plays through; undo, reset, state-space panel and BFS replay work; all 11 buttons have labels. Output: `test_ui-output.txt`.
- `python3 -I solver.py` (Python 3.14.7): output identical to `solver-output.txt`. It finds 2 shortest plans of 7 crossings after visiting 10 states.
- Not tested: every browser and screen reader individually. The page uses only standard HTML, CSS and JavaScript.
