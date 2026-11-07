# Task 2: *Pixel's AI Field Guide: Missions for Curious Humans* (Version 1.0, 2026-11-06)

An active study guide and a separate test bank for complete beginners learning about AI. The guide is built on the Task 1 core content ([../task-1/](../task-1/README.md)) and keeps the same definitions, numbers and terms. **Learners start at [study-guide/00-start-here.md](study-guide/00-start-here.md).**

Learners join **Pixel**, an eager and very literal lab robot, and **Dr. Ada Okafor** at the Curiosity Lab for 12 missions. Each mission starts from a problem and follows the same cycle: *predict or try → observe → explain → apply → check*. Every activity can be completed from the guide alone. Online platforms and videos are optional extras, and each one has an offline fallback.

## Folder map

| Path | What it contains |
|---|---|
| [study-guide/00-start-here.md](study-guide/00-start-here.md) | Title and version, table of contents, how to use the guide, the characters, learning goals, prerequisites, suggested route and timings (core path about 15–16 hours), activity-label legend, access and accessibility notes |
| `study-guide/mission-01` … `mission-12` | The 12 missions (see the table below) |
| [study-guide/glossary.md](study-guide/glossary.md) | 144 terms A–Z, each linked to the mission where it first appears |
| [study-guide/resources.md](study-guide/resources.md) | 12 curated videos and 6 platforms, each with what, why, which part, what to do, what to watch out for, access requirements and a fallback |
| [test-bank/test-bank.md](test-bank/test-bank.md) | 115 questions (40 true/false, 45 multiple choice, 30 open-ended), grouped by mission, with a separate answer key afterward |
| [activities/](activities/README.md) | Four tested hands-on supplements (two offline HTML pages, Prolog programs for SWISH, and a Python spam filter with a matching notebook), each with a README, expected outputs and tests |
| [assets/images/](assets/images/) | The module's original SVG diagrams (identical copies of `../task-1/assets/images/`) |

## Missions

| Mission | Core activity | Task 1 topic |
|---|---|---|
| [01 Is It AI?](study-guide/mission-01-is-it-ai.md) | "AI or not?" card sort; AI in Your Day | 01 |
| [02 The River Problem](study-guide/mission-02-the-river-problem.md) | Farmer–wolf–goat–cabbage puzzle, the state space and a breadth-first search trace ([interactive page](activities/river-crossing/)); optional robot maze | 02 |
| [03 Pixel's Rulebook](study-guide/mission-03-pixels-rulebook.md) | Prolog family tree and robot troubleshooter in SWISH; find the bug | 02 |
| [04 Learning from Examples](study-guide/mission-04-learning-from-examples.md) | "Be the spam filter"; Pixel's 12-email filter; Teachable Machine | 02–03 |
| [05 Inside the Neuron](study-guide/mission-05-inside-the-neuron.md) | A neuron by hand; TensorFlow Playground presets | 03 |
| [06 The Word-Guessing Machine](study-guide/mission-06-the-word-guessing-machine.md) | Markov-chain card game; next-token spinner and temperature | 04 |
| [07 Sorting the Robots](study-guide/mission-07-sorting-the-robots.md) | Two-lens card sort; headline fixer | 05 |
| [08 Time Machine](study-guide/mission-08-time-machine.md) | Timeline ordering; ELIZA investigation; boom or bust? | 06 |
| [09 AI in the Wild](study-guide/mission-09-ai-in-the-wild.md) | Be the recommender; six-part application framework | 07 |
| [10 The Fairness Files](study-guide/mission-10-the-fairness-files.md) | Five detective case files; Teachable Machine imbalance lab; structured case analysis | 08 |
| [11 Myth Busters](study-guide/mission-11-myth-busters.md) | Misconception Court; spot the hallucination; predict the failure | 09 |
| [12 Tomorrow's Rulebook](study-guide/mission-12-tomorrows-rulebook.md) | EU AI Act tier sorting and timeline; AGI claims debate; **final capstone review** with model answer and rubric | 10 |

## How the parts fit together

- **Study guide ↔ Task 1:** each mission's [EXPLAIN] section is a short, self-contained version of its topic file and links to it for more depth.
- **Test bank ↔ guide:** every question is tagged with its mission and topic. Many questions build on mission activities (river-crossing plans, Prolog queries, neuron sums, train/test tables, next-token tables, EU AI Act tiers). All questions can be answered without opening any platform.
- **Supplements ↔ guide:** each activity folder names its mission, and the guide reproduces the expected outputs so learners can check their results.

## Verification (2026-11-06)

- **Supplements:** all tests pass (river-crossing and robot-maze logic and UI tests, all Prolog queries, spam-filter output). Commands and versions are listed in [activities/README.md](activities/README.md).
- **Test bank:** every calculation was re-computed by script, and every Prolog answer was run in two Prolog engines (SWI-Prolog and Tau Prolog), which agreed.
- **Links:** relative links and anchors in all Task 1 and Task 2 Markdown files were checked by script. External URLs were checked when they were written.
- **Still needs a person:** clicking through Teachable Machine, Survival of the Best Fit and the TensorFlow Playground presets on a real device; typing the ELIZA test inputs once; watching the chosen video segments; and trying the guide with real learners. See [../task-1/gaps-and-open-issues.md](../task-1/gaps-and-open-issues.md).

**Sources:** [../sources.md](../sources.md).
