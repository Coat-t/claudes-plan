# Pixel's AI Field Guide: Missions for Curious Humans

**Version 1.0** · 2026-11-06 · A hands-on study guide for the module *AI Overview*
**Start here.** This page explains what the guide is, how to use it, and which route to take.

Welcome to the Curiosity Lab. In twelve short **missions** you will find out what artificial intelligence (AI) is, how it works, where it came from, what it is used for, what can go wrong, and where it is heading. You will not just read about AI: you will solve puzzles, become a spam filter, write rules for a robot, train a classifier, compute a neuron by hand, and play a word-guessing game that works like a tiny chatbot.

---

## Table of contents

| # | Mission | Big question | Covers | Core time |
|---|---|---|---|---|
| 01 | [Is It AI?](mission-01-is-it-ai.md) | How do you tell whether something is AI? | Topic 01 What is AI? | 50 min |
| 02 | [The River Problem](mission-02-the-river-problem.md) | How can a computer solve a puzzle without guessing? | Topic 02 (search) | 60 min |
| 03 | [Pixel's Rulebook](mission-03-pixels-rulebook.md) | What can a computer conclude from facts and rules? | Topic 02 (rule-based AI, expert systems) | 75 min |
| 04 | [Learning from Examples](mission-04-learning-from-examples.md) | How does a machine learn rules from labeled data? | Topics 02–03 (machine learning) | 80 min |
| 05 | [Inside the Neuron](mission-05-inside-the-neuron.md) | What is actually inside a neural network? | Topic 03 (neural networks, deep learning) | 70 min |
| 06 | [The Word-Guessing Machine](mission-06-the-word-guessing-machine.md) | How does a chatbot write, and why can it be wrong? | Topic 04 (generative AI, LLMs) | 70 min |
| 07 | [Sorting the Robots](mission-07-sorting-the-robots.md) | What kinds of AI exist, and which are still science fiction? | Topic 05 (types of AI) | 50 min |
| 08 | [Time Machine](mission-08-time-machine.md) | Why did AI boom, bust and boom again? | Topic 06 (history) | 85 min |
| 09 | [AI in the Wild](mission-09-ai-in-the-wild.md) | What does AI do in the real world, and at what risk? | Topic 07 (applications) | 70 min |
| 10 | [The Fairness Files](mission-10-the-fairness-files.md) | How can AI be unfair, invasive or misleading? | Topic 08 (ethics, risks, social impact) | 100 min (two sessions) |
| 11 | [Myth Busters](mission-11-myth-busters.md) | Which popular beliefs about AI are wrong? | Topic 09 (limitations, misconceptions) | 75 min |
| 12 | [Tomorrow's Rulebook](mission-12-tomorrows-rulebook.md) | How is AI being governed, and what can you do? + final capstone | Topic 10 (future of AI) | 80 min + capstone 60–90 min |

**Reference and practice:**

- [Glossary](glossary.md): every key term in plain English, A to Z.
- [Resources](resources.md): the curated videos and platforms, with what to watch, why, and access notes.
- [Test bank](../test-bank/test-bank.md): true/false, multiple-choice and open questions for every mission, with an answer key.
- [Hands-on activities](../activities/README.md): the supplements used in the missions (river-crossing puzzle, Prolog files, spam-filter code, robot maze).
- [Module outline (Task 1)](../../task-1/00-module-outline.md) and the [topic files](../../task-1/topics/01-what-is-ai.md): the full reference text behind each mission.

---

## How to use this guide

Every mission follows the same pattern, so you always know what comes next:

**Encounter a problem → predict or try → observe → explain → apply → check.**

1. **Read the [MISSION BRIEF]**: a short story beat that sets up the problem.
2. **Make your [PREDICT]ions on paper before you do anything else.** Wrong predictions are useful: they show exactly what you have just learned.
3. **Do the [TRY IT] activities.** Each substantial activity lists its **Goal**, **Preparation**, **Task**, **Observation**, **Reflection** and **Feedback**.
4. **Open the feedback boxes only after you have tried.** Answers are hidden in collapsible boxes (click "[DEBRIEF] ..." to open them). They explain the reasoning and the common mistakes, not just the answer.
5. **Read the [EXPLAIN] section.** It is short and self-contained; each one links to its Task 1 topic file if you want more depth.
6. **Use the idea in [APPLY]**, then test yourself with **[CHECK]** and compare with the **[DEBRIEF]**.
7. **Finish with the mission summary** (five bullets) and follow the "Next mission" link.

**Tips:** keep a "lab notebook" (paper or a document) for predictions, tables and reflections. Work alone, in pairs or as a class: every activity can be done together, and several have group variants. After a few missions, use the [test bank](../test-bank/test-bank.md) to review.

---

## Meet the team

**Pixel** is a small, enthusiastic and *very* literal lab robot who learns alongside you. Pixel makes mistakes, and those mistakes are deliberate: each one shows a common misconception about AI (for example, deciding that "a" is a spam word after seeing too few emails, or announcing that a chatbot keeps its answers in a giant fact book). When Pixel gets something wrong, ask yourself *why* it seemed reasonable.

**Dr. Ada Okafor** is the calm lead researcher at the **Curiosity Lab**. She sets the missions, asks the awkward questions and gives the explanations and feedback.

Both are **fictional characters** created for this guide. Pixel is not a real AI system, and nothing Pixel "thinks" describes how real AI works, unless the guide says so in a "Technically speaking" box.

### "Playful analogy" vs "Technically speaking"

Analogies make ideas memorable, but every analogy is wrong somewhere. Whenever the guide uses one, it is labeled and followed by the technical version:

> **Playful analogy:** an overfit model is like a student who memorizes last year's exam.
>
> **Technically speaking:** the model fits its training examples (including noise and coincidences) instead of the general pattern, so it does worse on new data.

Trust the **Technically speaking** part when the two seem to disagree. **[LAB NOTE]** boxes do the same job for simulations and games: they say what each activity leaves out.

---

## Learning goals

After completing the guide you should be able to (these match the module learning outcomes LO1–LO9 in the [module outline](../../task-1/00-module-outline.md)):

| # | You will be able to ... | Missions |
|---|---|---|
| LO1 | **Define** AI in your own words as a system that infers outputs (predictions, recommendations, decisions, content) from inputs, and **recognize** AI in everyday tools, justifying why a tool does or does not count as AI. | 01 |
| LO2 | **Distinguish** rule-based AI (including search) from learning-based AI, and AI from machine learning, deep learning and generative AI. | 02, 03, 04, 05, 06 |
| LO3 | **Describe and trace** how a model learns from labeled data (training) and makes predictions on new inputs (inference), including how a single artificial neuron computes its output and how a language model generates text token by token. | 04, 05, 06 |
| LO4 | **Classify** AI systems by capability (narrow, general, superintelligent) and by functionality (reactive, limited memory, theory of mind, self-aware), and explain which types exist today. | 07 |
| LO5 | **Outline** the key milestones of AI history and **explain** the causes of the AI winters and of the deep-learning comeback. | 08 |
| LO6 | **Analyze** real AI applications by input, output, AI type, benefit, risk and needed human oversight. | 09 |
| LO7 | **Discuss** the main ethical risks and social impacts of AI (bias, privacy, jobs, accountability, environmental cost, misinformation) using real cases and correctly interpreted evidence. | 10 |
| LO8 | **Identify and correct** common misconceptions about AI and **check** AI output for hallucinations. | 11 (preview in 06) |
| LO9 | **Explain** the AGI debate fairly and **describe** how AI is being regulated, classifying example systems into EU AI Act risk tiers. | 12 |

## Prerequisites

- **Basic computer skills:** using apps, a web browser and email, and a general idea of what a computer program is.
- **No programming and no mathematics background needed.** The only arithmetic is adding and multiplying small decimals (Missions 04 to 06) and reading percentages. The Prolog and Python activities are fully guided: you copy, run and change small pieces, and every expected result is printed in the guide.
- **Within the guide:** each mission builds on the earlier ones. Missions 01 to 06 should be done in order. Missions 07 to 12 assume Missions 01 to 06, and Mission 10 also uses Mission 04's Teachable Machine setup.

---

## Suggested route and timings

The **core path** is everything not marked optional: about **15 to 16 hours** in total (about 13 hours for Missions 01 to 11, plus about 80 minutes for Mission 12 and 60 to 90 minutes for the capstone), best spread over 10 to 13 sessions of 1 to 2 hours. **Optional side quests** add about 3 to 4 hours. Times are estimates for a beginner working at a steady pace; your times will vary.

| Session | Core path | Optional side quests |
|---|---|---|
| 1 | Mission 01: Is It AI? (50 min) | none |
| 2 | Mission 02: The River Problem (60 min) | Pixel in the Maze: fixed rule vs search vs reinforcement learning (30 min) |
| 3 | Mission 03: Pixel's Rulebook (75 min) | Extra queries in the [Prolog worksheet](../activities/prolog/queries.md) (20 min) |
| 4 | Mission 04: Learning from Examples (80 min) | Run Pixel's spam filter in Python or Colab (30 min) |
| 5 | Mission 05: Inside the Neuron (70 min) | 3Blue1Brown video; watch a neuron learn by hand; Playground spiral (30 min) |
| 6 | Mission 06: The Word-Guessing Machine (70 min) | Same prompt, three answers in a real chatbot (15 min) |
| 7 | Mission 07: Sorting the Robots (50 min) + start Mission 08 | Mission 07 optional (10 min) |
| 8 | Mission 08: Time Machine (85 min) | Mission 08 optional (20 min) |
| 9 | Mission 09: AI in the Wild (70 min) | Mission 09 optional (10 min) |
| 10–11 | Mission 10: The Fairness Files (100 min, two parts) | Mission 10 optional (15 min) |
| 12 | Mission 11: Myth Busters (75 min) | Mission 11 optional (15 min) |
| 13–14 | Mission 12: Tomorrow's Rulebook (80 min) + final capstone (60–90 min) | none |

**Short on time?** Do each mission's [MISSION BRIEF], one [TRY IT] activity, the [EXPLAIN] and the [CHECK]. Every mission's [EXPLAIN] section is self-contained.

---

## Activity labels

Every activity carries one of these text labels, always written in square brackets:

| Label | What it means | What you do |
|---|---|---|
| **[MISSION BRIEF]** | The story beat and the problem for this mission | Read it and keep the mission question in mind |
| **[PREDICT]** | Commit to a guess before you see the answer | Write your prediction down; check it later |
| **[TRY IT]** | A hands-on activity (paper, cards, a platform or code) | Follow Goal / Preparation / Task / Observation / Reflection / Feedback |
| **[OBSERVE]** | Questions about what you noticed | Compare results and look for a pattern |
| **[EXPLAIN]** | The core explanation of the mission's ideas | Read it; check it against what you observed |
| **[APPLY]** | Use the idea on a new case | Solve it before opening the debrief |
| **[CHECK]** | 3 to 5 quick self-check questions | Answer without looking back |
| **[DEBRIEF]** | Answers and feedback, hidden in a collapsible box | Open only after trying; read the reasoning and common mistakes |
| **[WATCH]** | A curated video with what, why, which part, what to do and what to watch out for | Watch only the named part; do the viewing task |
| **[LAB NOTE]** | What a simulation, game or analogy leaves out | Read it before you draw conclusions |
| **[OPTIONAL SIDE QUEST]** | Extra depth or practice; not needed for later missions | Do it if you have time or curiosity |

---

## Access and accessibility

**Every core activity can be done offline with paper.** Online platforms make processes visible, but each one has a fallback in the guide (sample results, traces or printed outputs from tested runs).

| What | Used in | Account? | Online? | Offline / no-device fallback |
|---|---|---|---|---|
| River-crossing page (`river-crossing.html`) | Mission 02 | No | **No**: a single file that loads nothing from the web | Paper cards F, W, G, C; printed BFS trace |
| Robot maze page (`robot-maze.html`) | Mission 02 side quest | No | **No**: a single file | Paper mazes printed in the mission |
| SWISH (Prolog in the browser) | Mission 03 | No (login optional, only to save) | Yes | Install SWI-Prolog; or trace the printed programs on paper |
| Pixel's spam filter (Python / notebook) | Mission 04 side quest | Colab needs a Google account; Python/Jupyter need none | Colab yes; Python/Jupyter no | All outputs printed in the mission |
| Google Teachable Machine | Missions 04 and 10 | No | Yes; webcam or image files | Results table to analyze in the mission |
| TensorFlow Playground | Mission 05 | No | Yes | Expected-results table in the mission |
| Videos (YouTube) | Several missions | No | Yes | Direct MP4 or text versions where available; otherwise the [EXPLAIN] section covers the content |

- **Devices:** a laptop or desktop is recommended for SWISH, Teachable Machine and TensorFlow Playground (wide layouts; phones were not tested). The river-crossing and robot-maze pages work on a computer or tablet.
- **Keyboard and screen readers:** the river-crossing and robot-maze pages work fully with the keyboard (Tab, then Enter or Space), and their buttons are labeled. Every diagram in this guide has a text description (alt text), and the important numbers in each diagram also appear in a table in the text.
- **Captions:** all recommended videos have captions; the number of caption languages is listed in each [WATCH] box and in [Resources](resources.md). Timestamps come from YouTube's chapter lists.
- **Privacy:** Teachable Machine keeps your webcam images in your browser tab unless you save to Google Drive or upload a model (don't, for these activities). SWISH saves programs as public by default: you do not need to save. Never type personal information into online tools or chatbots.
- **Print:** the guide is plain Markdown and prints cleanly. Collapsible answer boxes may print open or closed depending on the viewer; print the [test bank](../test-bank/test-bank.md) separately.
- **External links** were checked on 2026-11-06. Websites change; if a platform looks different from the instructions, use the fallback in the mission.

---

## Credits

- **Characters:** Pixel and Dr. Ada Okafor, the Curiosity Lab, and all story beats are original and fictional, created for this guide.
- **Diagrams:** all diagrams in `../assets/images/` are original diagrams created for this module.
- **Supplements:** the river-crossing puzzle, robot maze, Prolog files and spam-filter code in `../activities/` were written and tested for this guide; their READMEs record the tests.
- **Data:** all emails, families, robots, fruit and probabilities in the activities are **illustrative (made-up)**, as labeled where they appear.
- **External resources:** videos and platforms are linked, not copied, and belong to their creators (CrashCourse/PBS Digital Studios, Code.org, 3Blue1Brown, TED, Google Teachable Machine, TensorFlow Playground, SWI-Prolog/SWISH and others). Each is credited where it is used and in [Resources](resources.md).
- **Content sources:** the facts in each mission come from the cited sources in the matching [Task 1 topic file](../../task-1/topics/01-what-is-ai.md) (see each file's Sources section).

**Version history:** 1.0 (2026-11-06): first complete release.
