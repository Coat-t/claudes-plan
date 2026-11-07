# AI Overview: Module Outline (Version 2.0)

**Last updated:** 2026-11-06 · **Replaces:** `content/00-module-outline.md` (V1.0, 2026-10-25)
**Related files:** [README](README.md) · [Revision log](revision-log.md) · [Gaps and open issues](gaps-and-open-issues.md) · [Adapted formats](formats/README.md) · [All sources](../sources.md)

## 1. Overview

This module is a beginner's introduction to artificial intelligence (AI). It answers four questions, in this order:

1. **What is AI, and how does it work?** (Topics 01–04: from the definition, through rule-based and learning-based AI, to neural networks and the generative AI behind chatbots.)
2. **What kinds of AI are there, and where did they come from?** (Topics 05–06: the two ways of classifying AI, and its 75-year history of booms and "winters".)
3. **What is AI used for, and what can go wrong?** (Topics 07–09: applications, ethical risks, limitations and common misconceptions.)
4. **Where is AI heading?** (Topic 10: the AGI debate and the rules being written to govern AI.)

Each topic file contains an explanation, key terms, a worked example, a visual, common mistakes, two or three activities with explained answers, an optional extension, connections to other topics, and its sources.

## 2. Intended learners and prerequisites

- **Learners:** complete beginners (for example, first-year students from any discipline or interested adults).
- **Prerequisites:** basic computer skills (using apps, a browser and email) and a general idea of what a computer program is. **No programming or mathematics background is required.** The only arithmetic in the module is adding and multiplying small decimal numbers (Topic 03) and reading percentages (Topics 02, 07, 08, 10).
- **Section-level prerequisites** are listed at the start of every topic file and summarised in the table in section 4 (fixes the old gap 9, which said they had not been identified).

## 3. Module learning outcomes

After completing the module, learners should be able to:

| # | Outcome | Main topics |
|---|---|---|
| LO1 | **Define** AI in their own words as a system that infers outputs (predictions, recommendations, decisions, content) from inputs, and **recognize** AI in everyday tools, justifying why a tool does or does not count as AI. | 01 |
| LO2 | **Distinguish** rule-based AI (including search) from learning-based AI, and AI from machine learning, deep learning and generative AI. | 02, 03, 04 |
| LO3 | **Describe and trace**, in simple terms, how a model learns from labeled data (training) and then makes predictions on new inputs (inference), including how a single artificial neuron computes its output and how a language model generates text token by token. | 02, 03, 04 |
| LO4 | **Classify** AI systems by capability (narrow, general, superintelligent) and by functionality (reactive, limited memory, theory of mind, self-aware), and explain which types exist today. | 05 |
| LO5 | **Outline** the key milestones of AI history and **explain** the causes of the AI winters and of the deep-learning comeback. | 06 |
| LO6 | **Analyze** real AI applications by input, output, AI type, benefit, risk and needed human oversight. | 07 |
| LO7 | **Discuss** the main ethical risks and social impacts of AI (bias, privacy, jobs, accountability, environmental cost, misinformation) using real cases and correctly interpreted evidence. | 08 |
| LO8 | **Identify and correct** common misconceptions about AI and **check** AI output for hallucinations. | 09 |
| LO9 | **Explain** the AGI debate fairly and **describe** how AI is being regulated, classifying example systems into EU AI Act risk tiers. | 10 |

## 4. Learning sequence and development status

The order was changed from V1.0 so that every idea is taught before it is used (old gap 1): ethics now comes **after** machine learning and generative AI, because AI bias is explained in terms of training data; history comes after "how AI works", so that learners can understand *why* rule-based AI hit limits and why neural networks returned.

| # | Topic file | Subtopics | Depth | Key prerequisite topics | Worked example / visual | Activities | Status |
|---|---|---|---|---|---|---|---|
| 01 | [What is AI?](topics/01-what-is-ai.md) | Definition; intelligence vs AI; everyday AI; the AI effect | Detailed | None | Input → output analysis of everyday tools; nested-circles diagram | AI or not?; AI-effect explanation; AI in Your Day | drafted (self-checked) |
| 02 | [How AI operates](topics/02-how-ai-operates.md) | Data, algorithms, models; rule-based ("old") vs learning ("new"); search; training vs inference | Detailed | 01 | Spam filter (illustrative figures); river-crossing search trace; rules-vs-learning and ML-pipeline diagrams | Trace the spam filter; rules or learning?; find the error in a plan | drafted (self-checked) |
| 03 | [ML, neural networks and deep learning](topics/03-ml-neural-networks-deep-learning.md) | Supervised / unsupervised / reinforcement learning; features and labels; train/test; overfitting; neuron; layers; "deep" | Detailed (neural networks: intuition only) | 01, 02 | Fruit classifier with three models; one neuron by hand; neuron and layer diagrams | Which kind of learning?; be the neuron; find and fix | drafted (self-checked) |
| 04 | [Generative AI and LLMs](topics/04-generative-ai-and-llms.md) | Generative vs discriminative; tokens; next-token prediction; training stages; temperature; hallucination preview | Brief → developed | 01–03 | Next-token walkthrough; next-token diagram | Markov-chain text by hand; temperature prediction; classify tasks | drafted (self-checked) |
| 05 | [Types of AI](topics/05-types-of-ai.md) | By capability (ANI, AGI, ASI); by functionality (reactive, limited memory, theory of mind, self-aware) | Detailed | 01–04 | Six real systems under both lenses; two-lenses diagram | Classify under both lenses; correct claims | drafted (self-checked) |
| 06 | [History of AI](topics/06-history-of-ai.md) | The Start; the Failures (AI winters); the Big Comeback | Detailed | 01–03 (04 helpful) | 17-row milestone table; neural-network "fall and return" trace; timeline diagram | Order milestones; diagnose winters; boom-or-bust prediction | drafted (self-checked) |
| 07 | [Real-world applications](topics/07-real-world-applications.md) | Recommendation systems; healthcare; transportation; others | Brief, shown through examples | 01–04 | Collaborative-filtering trace (illustrative ratings); six-part framework | Analyze a new app; rank by stakes; find errors | drafted (self-checked) |
| 08 | [Ethics, risks and social impact](topics/08-ethics-risks-social-impact.md) | Bias; privacy; jobs; accountability and transparency; environment; misinformation and deepfakes | Detailed | 02–04, 07 | Gender Shades case; bias life-cycle diagram; WEF 2025 figures | Name the issue; check the jobs numbers; SafeStation case study | drafted (self-checked) |
| 09 | [Limitations and misconceptions](topics/09-limitations-and-misconceptions.md) | Hallucinations; brittleness; six misconceptions incl. "AI is alive" and "AI will take all jobs" | Brief → developed | 03–06 | Four-step checking routine applied to a chatbot answer | Find and fix; spot the hallucinations; predict failures | drafted (self-checked) |
| 10 | [The future of AI](topics/10-future-of-ai.md) | AGI debate; rules (EU AI Act, OECD, UNESCO, Council of Europe); AI literacy | Brief → developed | 05–08 | Classifying systems into EU AI Act tiers | Classify 8 systems; which rules apply when?; judge AGI claims | drafted (self-checked) |

**Status labels** (unchanged from V1.0): *outline only* · *drafted* (learning content written) · *checked* (claims, examples and sources verified by a second team member) · *needs revision*. "Self-checked" means the author verified claims against the cited sources and checked every calculation, but a **second human reviewer has not yet checked it**, so no topic is marked *checked*.

## 5. Scope

| Essential (in every topic file) | Optional extensions (clearly marked "Optional extension") | Out of scope |
|---|---|---|
| Definitions, explanations, worked examples, visuals, activities and answers listed above | Deeper material at the end of each topic (for example, regression vs classification, attention in transformers, EU AI Act details) and the hands-on code / Prolog activities in the study guide (Task 2) | The mathematics behind AI (beyond adding and multiplying), programming or building production models, technical comparisons of algorithms, reviews of commercial products |

## 6. How the core content becomes learning resources

| Core content | Resource | Location |
|---|---|---|
| Concepts and explanations | Topic files (reference) and the study guide *Pixel's AI Field Guide* | [topics/](topics/), [../task-2/study-guide/](../task-2/study-guide/00-start-here.md) |
| Practice tasks and answers | Topic activities and the test bank | each topic's "Try it yourself"/"Answers"; [../task-2/test-bank/test-bank.md](../task-2/test-bank/test-bank.md) |
| Key ideas and diagrams | Slide outlines | [formats/slides/slide-outlines.md](formats/slides/slide-outlines.md) |
| Step-by-step demonstrations | Video scripts | [formats/video-scripts/video-scripts.md](formats/video-scripts/video-scripts.md) |

Consistency rule: if an error is found in any adapted resource, the topic file is corrected first and then every affected resource is updated (see [formats/README.md](formats/README.md)).

## 7. Gaps and uncertainties

The nine gaps listed in V1.0 have been resolved or reduced; remaining open issues (for example, very recent EU AI Act amendments, a few facts confirmed only through secondary sources, and the need for a second human reviewer and learner testing) are tracked in [gaps-and-open-issues.md](gaps-and-open-issues.md).
