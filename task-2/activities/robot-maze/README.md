# [OPTIONAL SIDE QUEST] Pixel in the Maze: Fixed Rule vs Search vs Reinforcement Learning

**Pixel's AI Field Guide: Missions for Curious Humans** · Supplement · Version 1.0 · 2026-11-06
Belongs to: Mission 02 (The River Problem) as an optional side quest. It reuses the breadth-first search from the river-crossing activity and previews reinforcement learning, one of the three kinds of machine learning explained in [Topic 03](../../../task-1/topics/03-ml-neural-networks-deep-learning.md).

**[MISSION BRIEF]** Dr. Ada Okafor has built two practice mazes. Pixel starts at **S** and must reach its charging station **G**, moving one square north, east, south or west, never through walls. You will watch Pixel try three very different strategies and decide which one deserves to be called "search", which one "learning", and which one neither.

| File | What it is |
|---|---|
| `robot-maze.html` | Interactive page: two 9 x 9 mazes, three strategies, a comparison table and a debrief. A single file that works offline. |
| `test_logic.mjs`, `test_logic-output.txt` | Automated tests of the maze logic inside the HTML page (Node.js, no packages). |
| `test_ui.cjs`, `test_ui-output.txt` | Optional simulated-browser test that presses the real buttons (needs the `jsdom` package, which is **not** included in this folder). |

## What kind of method is each strategy? (stated precisely)

| Strategy in the page | Kind of method | Needs the map? | Learns? | What it is technically |
|---|---|---|---|---|
| A. Right-hand wall follower | **Fixed rule** (no search, no learning) | No, only the four neighboring squares | No | One hand-written rule repeated: turn right if possible, else straight, else left, else back. |
| B. Breadth-first search (BFS) | **Search / planning** (rule-based, symbolic AI) | Yes, the whole map | No | Explores all squares 1 move away, then 2 moves away, and so on, with a frontier (queue) and a visited record; then follows the route it found. |
| C. Tabular Q-learning | **Reinforcement learning** (a kind of machine learning) | No | Yes, from rewards | Keeps a table of scores ("Q-values"), one per square and move, and updates them after every move from the rewards it receives. The table is **specific to one maze**. |

---

## Goal
- Distinguish three ways a machine can solve the same problem: a **fixed rule**, **search** and **reinforcement learning**, and label each one correctly.
- Explain why BFS always finds a **shortest** route when every move costs the same, and why a simple rule can fail.
- Describe reinforcement learning in plain words: **trial and error, rewards, many episodes**, and a learned table that fits only the maze it was trained on.

## Preparation
- **Knowledge:** Mission 01 (what counts as AI) and the BFS part of Mission 02 (`../river-crossing/`). No programming or maths is needed.
- **Tool:** download `robot-maze.html` and open it in any modern web browser (Chrome, Edge, Firefox, Safari) on a computer or tablet. **No internet connection, account or installation is needed.** The page loads nothing from the web. Every button and option works with the keyboard (Tab to move, Enter or Space to press). If your device asks for reduced motion, the page shows results instantly instead of animating.
- **Paper:** a sheet for your predictions and a copy of the comparison table at the bottom of the page.
- **Time:** about 25 to 35 minutes.

## Task (step by step)
1. **[PREDICT]** Read the three strategy descriptions on the page. For Maze 1, write down: Will the wall follower reach G? Will BFS's route be the shortest? How many moves will Q-learning's first episode take (10? 50? 100?)?
2. **[TRY IT] Fixed rule:** with **Maze 1** selected, click **Run the wall follower**. Watch where Pixel goes. Note the number of moves and the shortest route given in the message.
3. **[TRY IT] Search:** click **Run BFS**. The light-blue squares are the squares BFS explored; the orange squares are the route. Note both numbers.
4. **[TRY IT] Reinforcement learning:** click **Train 1 episode** once, then **Train 10 episodes**. After each, click **Show Pixel's best route so far**. Keep training 10 episodes at a time until Pixel's best route reaches G. Watch the bar chart: each bar is one episode, and shorter bars mean fewer moves.
5. **[OBSERVE]** Click **Show learned arrows**. Each arrow is the move with the best score in Pixel's table for that square. Do the arrows near G make sense? Are there squares with no arrow?
6. Click **Forget everything (reset)** and train 10 episodes again. Is the result the same as before? (Hint: the page uses a fixed random seed so the experiment can be replayed.)
7. **[PREDICT]** Switch to **Maze 2** (goal on an island). Before running anything, predict what the wall follower will do. Then run all three strategies again and fill in the comparison table.
8. **[EXPLAIN]** Answer the [EXPLAIN] questions on the page, then open the [DEBRIEF] there or below.

## Observation questions
1. In Maze 1, where does the wall follower waste moves? How many extra moves does it make compared with the shortest route?
2. In Maze 2, why does the page stop the wall follower? Would giving Pixel more moves help?
3. How many squares did BFS explore in each maze before finding G? Is that more or fewer than the number of moves in its route? Why?
4. How many moves did Q-learning's first episode take? After how many episodes was Pixel's best route the shortest one?
5. Even after many episodes, the bars in the chart do not all drop to the shortest length. Why not? (Hint: 20% of moves are random.)
6. Which strategies needed the map, and which did not?

## Reflection
- Which strategy would you trust to deliver a parcel in a new building you have no map of? Which in a building you have a perfect map of? Explain.
- The wall follower and BFS were both written completely by a human. What makes BFS "search" and the wall follower "just a rule"?
- Nobody told Pixel the route in Q-learning. Where did its knowledge come from? Who chose the reward numbers (-1, -5, +10), and could a different choice change what Pixel learns?
- Pixel's Q-table from Maze 1 does not solve Maze 2. What does that tell you about what a learned model "knows"? Compare with the spam filter (`../spam-filter/`), which also only knows its training examples.

## Feedback: expected results
<details><summary>[DEBRIEF] Open after you have tried</summary>

These numbers come from the automated tests (`test_logic-output.txt`, `test_ui-output.txt`) and are what the unchanged page shows. Coordinates are `(row, column)`, counted from 0 at the top-left corner of the 9 x 9 grid, so S is `(1,1)`.

**Maze 1: corridors and dead ends**
- **A. Wall follower: reaches G in 28 moves** (the shortest route is 16). Page message: *"Reached G after 28 moves (the shortest route is 16 moves). The rule worked, but Pixel's route was not the shortest, because it followed the wall into a dead end."* The rule takes Pixel from `(3,3)` left into the long dead-end corridor, down to `(7,1)` and all the way back to `(3,3)`: exactly the 12 extra moves.
- **B. BFS: explores 23 squares, finds the 16-move route** `(1,1) (1,2) (1,3) (2,3) (3,3) (3,4) (3,5) (2,5) (1,5) (1,6) (1,7) (2,7) (3,7) (4,7) (5,7) (6,7) (7,7)`. An independent distance check in the tests confirms 16 is the shortest possible.
- **C. Q-learning:** moves in episodes 1 to 10: `117, 98, 88, 70, 76, 47, 71, 50, 78, 42`. After 10 episodes the page shows *"Episodes trained: 10. Last episode: 42 moves. Best route so far: not found yet."* Pixel's best route first reaches the shortest length (16 moves) after episode 16, and stays at 16 from episode 19 onwards. After 30 episodes the page shows *"Best route so far: 16 moves"*. Average moves per episode drop from 73.7 (episodes 1 to 10) to 20.2 (episodes 251 to 300), still above 16 because one move in five is a random exploration move.

**Maze 2: goal on an island**
- **A. Wall follower: never reaches G.** The walls around G do not touch the outer wall, so a right hand kept on the outer wall goes round and round the outside. The page stops it when Pixel is back on a square it already visited, facing the same way: *"Never reaches G: loops forever (stopped after 25 moves)"*. More moves would not help: the tests ran it for 100,000 moves and it still never arrived.
- **B. BFS: explores 27 squares, finds the 12-move route** `(1,1) (2,1) (3,1) (4,1) (5,1) (6,1) (7,1) (7,2) (7,3) (7,4) (6,4) (5,4) (4,4)`, in through the gap at the bottom of the island.
- **C. Q-learning:** moves in episodes 1 to 10: `105, 75, 104, 48, 63, 23, 37, 74, 32, 30`. The best route first reaches 12 moves after episode 11 (then loses it again for a while) and stays at 12 from episode 22 onwards. After 100 episodes the page shows *"After 100 episodes: route of 12 moves"*. Averages: 59.1 moves per episode (episodes 1 to 10), 16.0 (episodes 251 to 300).

**Other checks:** with the same random seed, a reset replays exactly the same experiment (10 episodes later the last episode again takes 42 moves in Maze 1). A Q-table trained for 100 episodes on Maze 1 does **not** lead to G when used in Maze 2.

**Answers to the observation questions (short):** 1. The left dead end: 28 - 16 = 12 extra moves. 2. It is repeating a loop that never passes G, so more moves cannot help. 3. 23 and 27 squares explored, more than the 16 and 12 route moves, because BFS checks every route of length 1, 2, 3, ... before committing; that is the price of the guarantee. 4. 117 moves (Maze 1) or 105 (Maze 2); shortest route from about episode 16 to 19 (Maze 1) and 11 to 22 (Maze 2), depending on whether you count the first time or the time it stays. 5. During training Pixel keeps exploring at random 20% of the time; "best route" ignores that exploration. 6. Only BFS needed the map.

**Reflection key points:** a fixed rule is cheap and needs no map, but it works only in some mazes (a wall follower is guaranteed to reach a goal on the wall it follows when all walls are connected to each other; when the goal sits on a separate "island" of walls, it can circle forever, as in Maze 2). Search needs a complete, correct map and, when every move costs the same, guarantees a shortest route. Reinforcement learning needs no map but many trial runs and a human-chosen reward; what it learns is a table for **this** maze, so if the maze or the goal changes Pixel must learn again. BFS and the wall follower are rule-based (symbolic) AI; Q-learning is machine learning.
</details>

## [LAB NOTE] Limitations
- **Accurate labels:** the wall follower is a **fixed rule**, BFS is **search**, and Q-learning is **reinforcement learning**. Only Q-learning learns. None of the three uses a neural network or "understands" the maze.
- **Toy world:** a 9 x 9 grid, perfect sensors, moves that always succeed, and the same maze in every episode. Real robots have noisy sensors, slipping wheels and changing surroundings.
- **Q-table is maze-specific:** the table stores one score per square and move of this maze. It does not transfer to another maze (tested). Real reinforcement-learning systems usually replace the table with a neural network (deep reinforcement learning) and need far more training, and even then they can fail when the world changes.
- **Human choices shape the result:** the rewards (-1 per move, -5 for bumping a wall, +10 at G) and the settings (learning rate 0.5, discount 0.9, 20% random exploration, random seed 2026) were chosen by a human. Different choices can lead to faster, slower or different learning. Exact episode numbers depend on the seed; with another seed, the overall pattern (long early episodes, a shortest route after a few dozen episodes) is what to expect, not the exact numbers.
- **BFS's guarantee has conditions:** it finds the shortest route only because every move costs the same and the map is complete and correct. On huge maps it explores far too much; real route planners use informed search (for example A*) instead.
- Pixel is a fictional character. The three algorithms in the page are real.

## Fallback if the page cannot be opened
Use the paper version. The two mazes are below (`#` wall, `.` floor, `S` start, `G` goal).

```
Maze 1 (corridors and dead ends)     Maze 2 (goal on an island)
#########                            #########
#S..#...#                            #S......#
###.#.#.#                            #.#####.#
#.....#.#                            #.#...#.#
#.#####.#                            #.#.G.#.#
#.#...#.#                            #.#...#.#
#.#.#.#.#                            #.##.##.#
#.#.#..G#                            #.......#
#########                            #########
```

1. **Fixed rule:** start at S facing east. At every step, turn right if the square is free, otherwise go straight, otherwise turn left, otherwise turn back. Trace Pixel's moves with a pencil and count them. Compare with the route listed in `test_logic-output.txt` (Maze 1, 28 moves).
2. **Search:** write 0 in S, then 1 in every free neighbor, 2 in their free unnumbered neighbors, and so on until you write a number in G. That number is the shortest route length (16 and 12). Walk back from G by decreasing numbers to find the route.
3. **Reinforcement learning:** use the episode lengths in the DEBRIEF above as your data. Plot them as a bar chart and answer observation questions 4 and 5.

## Test evidence
Run on 2026-11-06 (re-run in full after the activity was finished; outputs were identical to the saved files):
- `node test_logic.mjs`: **10 of 10 tests passed** (Node v26.10.0, no packages). It extracts the maze logic from the HTML file, so it tests exactly the code learners run. It checks: both mazes are 9 x 9; the wall follower reaches G in 28 moves in Maze 1 and loops in Maze 2 (even with 100,000 moves); BFS finds 16- and 12-move routes, confirmed by an independent distance flood; the rewards are -1, -5 and +10; Q-learning has no complete route after 10 episodes, then keeps the shortest route in every episode from 25 to 300 in both mazes; a reset replays identically; a Maze 1 table does not solve Maze 2. Output: `test_logic-output.txt`.
- `NODE_PATH=<folder>/node_modules node test_ui.cjs`: **all UI checks passed** (jsdom 31.0.0, Node v26.10.0). To run it, install jsdom in any temporary folder (`npm install jsdom`) and point `NODE_PATH` at that folder's `node_modules`; jsdom is not shipped with this activity and learners never need it. It checks: the page has no external resources; the real buttons produce the messages quoted in the DEBRIEF; arrows, reset, maze switching and the comparison table work; all 8 buttons have labels and all inputs are labelled. Output: `test_ui-output.txt`.
- Additional check (not saved as a file): following Pixel's best route after every episode shows the shortest route held from episode 19 (Maze 1) and episode 22 (Maze 2) onwards, as stated in the DEBRIEF.
- Not tested: every browser and screen reader individually. The page uses only standard HTML, CSS and JavaScript.
