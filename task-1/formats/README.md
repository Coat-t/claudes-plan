# Adapted Formats: Slides and Video Scripts

**Module:** AI Overview · **Version:** 1.0 · **Last updated:** 2026-11-06

**Back to:** [Module outline](../00-module-outline.md) · [Revision log](../revision-log.md) · [Gaps and open issues](../gaps-and-open-issues.md)

This folder holds the module's core content adapted into two presentation formats. The **topic files** in [../topics/](../topics/) are the single source of truth; every format here is derived from them and must stay consistent with them.

## What is in this folder

| File | What it is | Size |
|---|---|---|
| [slides/slide-outlines.md](slides/slide-outlines.md) | One slide-deck outline per topic (6 to 9 slides each): title, 2 to 4 key points, the visual, speaker notes linked to the source section, and one interaction (poll / predict) slide per deck with the answer in the notes | 10 decks, 87 slides |
| [video-scripts/video-scripts.md](video-scripts/video-scripts.md) | One 3 to 5 minute tutorial script per topic, each built on a step-by-step demonstration of the topic's worked example: numbered segments with time range, on-screen visual, narration and pause / predict prompts, plus accessibility notes | 10 scripts, 3:30 to 4:25 each |

Diagrams are not copied into this folder: both files link to the shared originals in [../assets/images/](../assets/images/) (`../../assets/images/<file>.svg` from inside `slides/` and `video-scripts/`).

## How each format maps to the core content

| Core content (brief, section 7) | Where it lives | How it is used | Link |
|---|---|---|---|
| Concepts and explanations | Topic files (reference) and the study guide *Pixel's AI Field Guide* (Task 2) | Full explanations, key terms, worked examples, activities with answers | [../topics/](../topics/) · [../../task-2/study-guide/00-start-here.md](../../task-2/study-guide/00-start-here.md) |
| Practice tasks and answers | Each topic's "Try it yourself" / "Answers", and the test bank (Task 2) | Self-study practice, quizzes, assessment | [../../task-2/test-bank/test-bank.md](../../task-2/test-bank/test-bank.md) |
| Key ideas and diagrams | Slide outlines (this folder) | Live teaching: key points, the module diagrams, one audience interaction per topic | [slides/slide-outlines.md](slides/slide-outlines.md) |
| Step-by-step demonstrations | Video scripts (this folder) | Recorded tutorials that walk through one worked example per topic, with pause-and-predict moments | [video-scripts/video-scripts.md](video-scripts/video-scripts.md) |

### What each format takes from a topic file

| Topic file section | Slides | Video script |
|---|---|---|
| Learning goals | Title slide of each deck | "Goal" line of each script |
| Key terms, Explanation | Condensed into 2 to 4 key points per slide; details in the speaker notes | Only what the demonstration needs, explained in the narration |
| Worked example | One or two slides | The backbone of the script, step by step |
| Visual | Linked SVG on the relevant slide | Shown on screen and **described in the narration** |
| Common mistakes | Myth / correction slides and speaker notes | Pause prompts that target the common mistake |
| Try it yourself / Answers | Interaction slide (answer in the notes); some reuse an activity item | "Your turn" pointer at the end of the script |
| Sources | Each speaker note names the source section of the topic file | "Source" line names the sections used |

### Worked-example demonstration used in each video

| Topic | Demonstration | Topic file section |
|---|---|---|
| 01 | Self-checkout produce recognition through the input-to-output chain and three-question test | Worked example |
| 02 | Training a spam filter: labeled data → counts → weights → inference → test → improve (the river-crossing search is covered in slides 2.4 and 2.5) | Worked example |
| 03 | One artificial neuron by hand, then the "sender in contacts" variant | Worked example Part B |
| 04 | The next-token loop: probabilities → greedy vs sampling → append → temperature | Worked example |
| 05 | Six real systems classified under both lenses | Worked example |
| 06 | Building the timeline milestone by milestone; tracing the neural network's fall and return | Milestone table; Worked example |
| 07 | Collaborative-filtering trace (Sam, Priya, Leo), then the six-part framework | Worked example; Explanation section 2; Visual |
| 08 | Seven-step case analysis applied to the HireFast hiring model | Explanation section 8; Worked example |
| 09 | Four-step check on a chatbot answer about AI's beginnings | Worked example |
| 10 | Four-question EU AI Act classification of Examples A, B and C, then the timeline | Worked example; Explanation section 4 |

## The consistency rule

**Fix the topic file first, then every affected format.** If an error is found anywhere (in a slide, a script, the study guide or the test bank):

1. **Check the topic file.** If the error is in the topic file, correct it there first (smallest change that fixes it), and record what was changed, why and where in [Fixes made to the core content while adapting](#fixes-made-to-the-core-content-while-adapting) below and in the [revision log](../revision-log.md).
2. **Search every format for the affected term, number or example** (for example, search for "92 million", "0.41" or "Topic 03") in: `formats/slides/slide-outlines.md`, `formats/video-scripts/video-scripts.md`, the study guide (`../../task-2/study-guide/`), the glossary and the test bank (`../../task-2/test-bank/`).
3. **Update each match** so that explanations, examples and answers agree with the corrected topic file.
4. **Re-run the consistency check** for that topic (table below) and update its status and date.

Never fix an error only in an adapted format: the next adaptation would copy the error back.

## Adaptation consistency check

Each row lists the key numbers, definitions and examples used in the slides and video for that topic, checked against the topic file (Version 2.0, 2026-11-06). "Consistent" means every listed item in both formats matches the topic file word-for-word or as a faithful condensation, and every illustrative figure keeps its "made-up" label.

| Topic | Key items checked against the source | Slides | Video | Status |
|---|---|---|---|---|
| [01](../topics/01-what-is-ai.md) | Module definition of AI; IBM quote; OECD "infers from the input ... how to generate outputs", 38 member countries, late 2023; five output types; three-question test; Activity 1 answers (microwave, "@" check = not AI; bank alert = usually AI; next-word = AI); self-checkout chain; Tesler's Theorem (Hofstadter 1979), McCarthy attribution second-hand (2011), earliest version 1971; nested-circles simplification | 1.1–1.9 | V01 | Consistent |
| [02](../topics/02-how-ai-operates.md) | Data / algorithm / model; MYCIN (Stanford, early 1970s, roughly 600 rules, not in routine use); search elements; BFS; river puzzle (16 arrangements, 10 safe, 7 crossings, 2 shortest solutions; only safe first move = goat); traditional vs ML; Gmail ML from 2014; spam example (12,000 = 10,000 + 2,000; 4,000 / 6,000; 60%/5% = 12x, 40%/2% = 20x, 2%/30% = 15x, 10%/8% = 1.25x, 50%/20% = 2.5x; weights +2, +2, -2, 0, +1; threshold 2; emails A = 5, B = -2, C = 0; 720/800, 80 FN, 60 FP, 1,140, 1,860/2,000 = 93%, 140 mistakes); AlphaGo hybrid 2016 | 2.1–2.9 | V02 | Consistent (arithmetic re-checked) |
| [03](../topics/03-ml-neural-networks-deep-learning.md) | Supervised / unsupervised / reinforcement definitions; Activity 1 items 1–3 answers; Google 70/15/15 split; fruit models A 8/8 & 4/4, B 8/8 & 2/4 (overfitting), C 7/8 & 2/4 (underfitting); neuron x = (1, 0, 1), w = (0.6, -0.4, 0.3), b = -0.5 → 0.4 → 1; x2 = 1 → 0.0 → 0; sigmoid ≈ 0.60, ReLU 0.4; perceptron 1958; layers 3-4-4-2; "deep" = more than one hidden layer (IBM: at least 4 layers) | 3.1–3.9 | V03 | Consistent (sigmoid(0.4) = 0.599 re-checked) |
| [04](../topics/04-generative-ai-and-llms.md) | Generative vs discriminative (Google quotes); "almost all of today's prominent generative AI" wording; Shannon 1948; ELIZA mid-1960s; transformer 2017; GPT-3 175 billion vs 5 weights; token definition, 3/4 word, 100 tokens ≈ 75 words, 8-token example; five-step loop; 300 words ≈ 400 steps; probabilities 0.41/0.17/0.12/0.06/0.24 and cumulative ranges; runs 0.27 → mat, 0.63 → sofa, 0.45 → floor; second table 0.52/0.20/0.15/0.05/0.08; temperature columns (0.80 … 0.32); pre-training / fine-tuning / RLHF; InstructGPT 1.3B vs 175B | 4.1–4.9 | V04 | Consistent |
| [05](../topics/05-types-of-ai.md) | Two lenses (vehicle analogy); ANI / AGI / ASI definitions and quotes (IBM, Bostrom 2014); "current LLMs are not considered AGI", debated, no agreed test; four functionality types; Hintze 2016, popular-press taxonomy; memory ≠ training data; grid (two occupied cells); six-system table incl. spam filter = reactive (our classification) and Netflix = disputed | 5.1–5.8 | V05 | Consistent (O1 resolved) |
| [06](../topics/06-history-of-ai.md) | Three phases; three ingredients; 1950 Turing; Aug 1955 proposal coins the term; summer 1956 workshop; Logic Theorist 38 of 52 (runs reported 1957); 1958 perceptron; 1966 ELIZA; 1969 *Perceptrons* (XOR); 1973 Lighthill; winters ~1974–80 and ~1987–93; XCON from 1980 ($25M–$40M); 1986 backpropagation; 1987 Lisp collapse; Deep Blue May 1997 3.5–2.5, ~200M positions/s, not ML; AlexNet 15.3% vs 26.2%, ~60M weights; AlphaGo Mar 2016 4–1; transformer Jun 2017; ChatGPT 30 Nov 2022; neural-network trace; hype loop | 6.1–6.9 | V06 | Consistent (O2 resolved) |
| [07](../topics/07-real-world-applications.md) | Six-part framework; stakes → oversight; Netflix ~80% of hours, >$1B/yr (2015, company figures); FDA list > 1,000, ~3/4 radiology; IDx-DR April 2018, ~87% sensitivity, ~90% specificity, ~13 in 100 missed; Obermeyer 2019 (cut by more than half); navigation = ML prediction + search; Waymo ~271M rider-only miles to June 2026, ~82% fewer injury crashes (company-reported); Uber Tempe March 2018; ratings trace (differences 1 and 10 → recommend Film D); cold start; three-application comparison | 7.1–7.8 | V07 | Consistent after fix F1 |
| [08](../topics/08-ethics-risks-social-impact.md) | Four questions; six issues; seven bias stages (match SVG); Gender Shades (IBM, Microsoft, Face++; 1,270; up to 34.7% vs max 0.8%; disaggregated evaluation; study limits); Amazon 2018 "women's"; Clearview €30.5M Sept 2024; WEF 2025 (>1,000 employers, >14M workers, 55 economies; 170M / 92M / +78M, 2025–2030; ~22% churn; 92 ÷ 170 ≈ 5 per 10); Mata v. Avianca (six cases, $5,000, June 2023); IEA ~945 TWh by 2030; Arup HK$200M (~US$25M), 15 transfers, early 2024; seven-step case method; HireFast (10,000 applications, 80% / 85% men, 90% accuracy, top 20%, 20% vs 10% check) | 8.1–8.9 | V08 | Consistent |
| [09](../topics/09-limitations-and-misconceptions.md) | Limitation vs misconception; hallucination mechanism; Kalai et al. 2025; not lying; grounding; distribution shift; Szegedy et al. 2013; other limitations; six misconceptions with evidence (34.7% / 0.8%; 92M / 170M / +78M); four-step check; worked example claims C1–C7 and verdicts; corrected rewrite | 9.1–9.8 | V09 | Consistent after fix F2 |
| [10](../topics/10-future-of-ai.md) | Two habits; AGI: no agreed definition, mainstream view not AGI (same wording as Topic 05); Levels of AGI (2023, "Emerging AGI"); Grace et al. 2024 (2,778; 10% by 2027; 50% by 2047; 13 years earlier; all occupations 50% by 2116); four viewpoints; EU AI Act 2024/1689, in force 1 Aug 2024, extraterritorial; four tiers and examples; GPAI rules; fines €35M/7%, €15M/3%; timeline (2 Feb 2025; 2 Aug 2025; 2 Aug 2026; 2 Dec 2026; 2 Dec 2027 was 2 Aug 2026; 2 Aug 2028 was 2 Aug 2027); Omnibus (19 Nov 2025; May 2026; 27 Jul 2026); Examples A–C; Activity 1 item 8 (high + transparency); OECD (2019/2024, 47, 5 + 5), UNESCO (Nov 2021, 193, 4 values, 10 principles), Council of Europe (Sept 2024); literacy checklist | 10.1–10.9 | V10 | Consistent; time-sensitive (see open issue O4) |

**Checked by:** formats adaptation pass, 2026-11-06 (self-check; not yet reviewed by a second person).

## Fixes made to the core content while adapting

| # | What was fixed | Why | Where |
|---|---|---|---|
| F1 | The sentence introducing the pipeline diagram said "see the training-vs-inference pipeline diagram in Topic 03"; changed to "... from [Topic 02](../topics/02-how-ai-operates.md)" (with a link). | Wrong cross-reference: `ml-pipeline.svg` is the Visual of Topic 02; Topic 03's visuals are the neuron and layer diagrams. A learner following the reference would not find the diagram. | [Topic 07](../topics/07-real-world-applications.md), Visual section. Formats affected: none (the slides and video for Topic 07 do not repeat the reference). |
| F2 | Key-term definitions of **Next-token prediction** and **Token** aligned with Topic 04. Old: "it repeatedly predicts which token is most likely to come next" and "a word or part of a word". New: "given all the text so far, it works out the probability of each possible next token, picks one (usually a likely one), adds it to the text and repeats" and "a word, part of a word, a punctuation mark or a single character". | The old definition contradicted Topic 04, which teaches that the model scores every token and usually *samples* rather than always taking the most likely one (the reason outputs vary). The token definition omitted punctuation and characters, unlike Topic 04's key term. | [Topic 09](../topics/09-limitations-and-misconceptions.md), Key terms table. Formats affected: slides 4.5, 4.6, 9.2 and videos V04, V09 already used the Topic 04 wording; no change needed. The Task 2 glossary (not yet written at the time of this check) should use the Topic 04 wording. |

## Open issues found while adapting

| # | Issue | Suggested action |
|---|---|---|
| O1 | In `types-of-ai-two-lenses.svg`, the Limited memory box says "Uses recent data or past examples". "Past examples" can be read as training data, which Topic 05 says is **not** "memory" in this scheme (Common mistake 3). | **Resolved 2026-11-06:** diagram now reads "Uses recent observations while it works" (revision log R28). |
| O2 | In `ai-history-timeline.svg`, the 1956 label "AI named as a research field" could be read as "the term was coined in 1956", the error corrected in Topic 06 (term coined in the August 1955 proposal). | **Resolved 2026-11-06:** label now reads "AI launched as a research field" (revision log R29). |
| O3 | The study guide and test bank links in the mapping table ([00-start-here.md](../../task-2/study-guide/00-start-here.md), [test-bank.md](../../task-2/test-bank/test-bank.md)) did not resolve when this README was written because those Task 2 files were not yet created. | Re-check the links once Task 2 is written. |
| O4 | Deck 10 and video V10 depend on the EU AI Act timeline as amended by the 2026 Digital Omnibus (status 6 November 2026), which Topic 10 flags as recent and partly confirmed only through law-firm summaries. | Re-check Topic 10 against the consolidated text on EUR-Lex before each delivery, then apply the consistency rule. |
| O5 | The slides and scripts are outlines and scripts, not produced slide files or recorded videos. Timings assume about 145 spoken words per minute plus 5-second pauses; they have not been tested with a real presenter or learners. | Pilot one deck and one video with learners; adjust timings and pause prompts. |
