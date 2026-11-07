# Activities: Hands-On Supplements

**Pixel's AI Field Guide: Missions for Curious Humans** · Supplements · Version 1.0 · 2026-11-06

This folder holds the four hands-on supplements used by the study guide. Each one has its own README with the full activity (Goal, Preparation, Task, Observation questions, Reflection, expected results in a [DEBRIEF], a [LAB NOTE] on limitations, a fallback, and test evidence). The missions in `../study-guide/` contain the essential instructions and expected outcomes too, so a learner who cannot open a supplement can still follow the mission.

## The four supplements

| Folder | What learners do | Kind of AI it shows | Belongs to | Time |
|---|---|---|---|---|
| [`river-crossing/`](river-crossing/README.md) | Solve the farmer, wolf, goat and cabbage puzzle, see the 16-state "state space", and step through Pixel's breadth-first search. | Rule-based (symbolic) AI: **search** | **Mission 02** (The River Problem) | 30-40 min |
| [`robot-maze/`](robot-maze/README.md) | Compare three strategies in two mazes: a right-hand wall follower, breadth-first search, and Q-learning that improves over many episodes. | **Fixed rule** vs **search** vs **reinforcement learning** (labelled in the page) | **Mission 02**, [OPTIONAL SIDE QUEST] | 25-35 min |
| [`prolog/`](prolog/README.md) | Write and query a Prolog family tree, run a tiny robot "expert system", extend it with a new rule, and fix two silent bugs. | Rule-based AI: **facts, rules and queries** (expert systems) | **Mission 03** (Pixel's Rulebook) | 45-60 min |
| [`spam-filter/`](spam-filter/README.md) | Train a tiny word-counting spam filter on 12 labelled emails, test it on 8 unseen ones, and run experiments on data and labels. | Learning-based AI: **supervised machine learning** | **Mission 04** (Learning from Examples), [OPTIONAL SIDE QUEST] | about 30 min |

Suggested order: river-crossing, then (optionally) robot-maze, then prolog, then spam-filter. Together they move from "a human writes every rule" to "the machine learns its own rules from data", which is the central contrast of Topic 02.

## Access requirements

| Supplement | Needs | Online? | Account? | Installation? |
|---|---|---|---|---|
| river-crossing | Any modern web browser (computer or tablet). Download `river-crossing.html` and open it. | **No** (works offline; loads nothing from the web) | No | No |
| robot-maze | Any modern web browser. Download `robot-maze.html` and open it. | **No** (works offline) | No | No |
| prolog | SWISH, the free browser-based SWI-Prolog at <https://swish.swi-prolog.org> | **Yes** | **No** account needed to run programs (login is optional, only for saving on the server) | No. Offline alternative: install the free SWI-Prolog. |
| spam-filter | **One of:** Google Colab (online, free **Google account**), Jupyter on your own computer, or plain **Python 3.8+** | Colab: yes. Jupyter / Python: no | Colab only | Python (or Jupyter) only if you choose the offline route |

**No installation is needed for learners**, except Python (or Jupyter) for the optional spam filter if you do not want to use Colab. Every supplement also has a no-device fallback (paper version, printed trace or saved output) described in its README.

Accessibility: both HTML pages are self-contained, work with the keyboard only (Tab, Enter, Space), follow the system light/dark setting, and adapt to narrow screens. Neither page animates on its own: the river-crossing page only moves when you press **Play automatically**, and the robot-maze page shows results instantly when the device asks for reduced motion (or when you tick "Show results instantly"). The Prolog and spam-filter activities use plain text files that work with any text editor or screen reader.

## How to run the tests (for teachers and maintainers)
Learners do not need any of this. Commands are run from this `activities/` folder. Tested on 2026-11-06 with Node v26.10.0 and Python 3.14.7; all tests passed and the outputs matched the saved files.

| What | Command | Needs | Saved output |
|---|---|---|---|
| River-crossing logic | `node river-crossing/test_logic.mjs` | Node.js 18+ only | `river-crossing/test_logic-output.txt` |
| River-crossing page (simulated browser) | `NODE_PATH=<dir>/node_modules node river-crossing/test_ui.cjs` | jsdom | `river-crossing/test_ui-output.txt` |
| River-crossing solver | `cd river-crossing && python3 -I solver.py` | Python 3.8+ | `river-crossing/solver-output.txt` |
| Robot-maze logic | `node robot-maze/test_logic.mjs` | Node.js 18+ only | `robot-maze/test_logic-output.txt` |
| Robot-maze page (simulated browser) | `NODE_PATH=<dir>/node_modules node robot-maze/test_ui.cjs` | jsdom | `robot-maze/test_ui-output.txt` |
| Prolog queries (two engines) | `NODE_PATH=<dir>/node_modules node prolog/test_queries.cjs` | swipl-wasm, tau-prolog | `prolog/test-output.txt` |
| Spam filter | `python3 -I spam-filter/tiny_spam_filter.py` | Python 3.8+ | `spam-filter/expected-output.txt` |

The npm packages (`jsdom`, `swipl-wasm`, `tau-prolog`) are **not shipped** in this folder. Install them once in any temporary folder `<dir>` with `npm install jsdom swipl-wasm tau-prolog`, then point `NODE_PATH` at `<dir>/node_modules` as shown. Versions used for the recorded results: jsdom 31.0.0, swipl-wasm 8.3.0 (SWI-Prolog 10.1.20), tau-prolog 0.3.4. To compare a fresh run with a saved output, redirect it to a file and use `diff`, for example `node robot-maze/test_logic.mjs > /tmp/out.txt && diff /tmp/out.txt robot-maze/test_logic-output.txt`.

What the tests cannot show: every browser and screen reader individually, and the live SWISH and Colab services (their steps were checked against their own help pages, not driven automatically).
