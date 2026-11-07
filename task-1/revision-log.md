# Revision Log: AI Overview Module

Records significant changes made in Version 2.0 (2026-11-06) compared with Version 1.0 (`content/00-module-outline.md` and `content/01-overview-of-ai.md`, 2026-10-25): **what** changed, **why**, and **where** it appears. Old gap numbers refer to the "Gaps and uncertainties" list in the V1.0 outline.

## Structure

| # | What changed | Why | Where |
|---|---|---|---|
| R1 | The single draft file `01-overview-of-ai.md` was replaced by ten topic files, one per outline section, each following the extended template (learning goals, prerequisites, key terms, explanation, worked example, visual, common mistakes, activities, answers, optional extension, connections, sources). | Six of the ten outline sections were "outline only"; the old file mixed four sections and had no per-topic prerequisites, misconceptions or answers. | [topics/](topics/) |
| R2 | Topic order changed: How AI operates → ML/DL → Generative AI → Types → History → Applications → **Ethics** → Limitations → Future. | Old gap 1: bias is explained through training data, so ethics must come after ML and generative AI. History now follows "how AI works" so the causes of the AI winters and the comeback can be explained. | [00-module-outline.md §4](00-module-outline.md#4-learning-sequence-and-development-status) |
| R3 | Section-level prerequisites added to every topic and summarized in the outline. | Old gap 9. | "Prerequisites" in every topic; outline §4 |
| R4 | Uncredited nested-circles PNG replaced by original SVG diagrams (10 in total) created for this module. | Old gap 4: the image's source was never recorded, so it could not be credited. | [assets/images/](assets/images/) |

## Accuracy corrections

| # | What changed | Why | Where |
|---|---|---|---|
| R5 | "91 million jobs displaced" → WEF *Future of Jobs Report 2025*: 170 million jobs created, 92 million displaced, net +78 million (2025–2030), with caveats on what a "net" figure hides. | Old gap 3: wrong figure. | [08 §Jobs](topics/08-ethics-risks-social-impact.md), [09 Misconception 4](topics/09-limitations-and-misconceptions.md) |
| R6 | "McCarthy coined the term at the 1956 Dartmouth Workshop" → the term first appears in the August 1955 proposal (McCarthy, Minsky, Rochester, Shannon); the workshop took place in summer 1956. | Old draft conflated the proposal and the workshop. | [06 Explanation](topics/06-history-of-ai.md) |
| R7 | "All generative AI is deep learning" → "almost all of today's prominent generative AI systems use deep learning; earlier generative methods, such as Markov-chain text generators (Shannon 1948), did not." Learners run a Markov-chain generator by hand. | Old gap 6: oversimplification. | [01](topics/01-what-is-ai.md), [04 Explanation and Activity 1](topics/04-generative-ai-and-llms.md), nested-circles diagram footnote |
| R8 | Types of AI rewritten as **two explicitly separate classifications** (by capability; by functionality), with a grid, six real systems classified under both, and a note that the functionality scheme is a popular-press taxonomy (Hintze 2016). | Old gap 2: the outline mixed two schemes and the table used a third. | [05](topics/05-types-of-ai.md) |
| R9 | Spam-filter worked example rebuilt (counting → weights → threshold → inference → test-set evaluation, with false positives/negatives); every number labelled "illustrative (made-up)". The unsourced "95% of spam" claim removed. | Old gap 7; the old example did not show where weights come from. | [02 Worked example](topics/02-how-ai-operates.md) |
| R10 | "Job taking" rewritten as the misconception "AI will take all jobs", corrected with evidence and nuance (displacement is real hardship). | Old gap 8: listed as a misconception but worded as a fact. | [09](topics/09-limitations-and-misconceptions.md) |
| R11 | Deep Blue described as search (not machine learning). | Common confusion; supports the rule-based vs learning distinction. | [06](topics/06-history-of-ai.md), [05](topics/05-types-of-ai.md) |
| R12 | The "AI effect" quotation attributed correctly (Tesler's Theorem as reported by Hofstadter 1979; the McCarthy version flagged as a second-hand attribution). | Commonly misattributed. | [01](topics/01-what-is-ai.md) |

## New or expanded learning content

| # | What changed | Why | Where |
|---|---|---|---|
| R13 | Definitions sourced (IBM; OECD 2023 "infers from input how to generate outputs") and turned into a three-question "Is it AI?" test; intelligence vs AI; the AI effect. | Old definitions unsourced; learners needed a way to decide what counts as AI. | [01](topics/01-what-is-ai.md) |
| R14 | "AI in Your Day" activity kept and improved: structured table (input, output type, AI test, stakes, how much to check); the narrow/general question removed because types are taught later (foreshadowed instead); expected outcome extended. | It asked learners to use concepts before they were taught. | [01 Activity 3 and Answers](topics/01-what-is-ai.md) |
| R15 | Rule-based AI explained with MYCIN and with search: a full breadth-first trace of the farmer–wolf–goat–cabbage puzzle (16 arrangements, 10 safe states, 7 crossings, 2 shortest solutions, verified by script). | "Old vs new" was one sentence. | [02](topics/02-how-ai-operates.md) |
| R16 | Training vs inference and the role of a test set made explicit. | Old pipeline blurred the two phases. | [02](topics/02-how-ai-operates.md), [03](topics/03-ml-neural-networks-deep-learning.md) |
| R17 | New content: three kinds of learning, features/labels, train/test, overfitting (fruit example), artificial neuron by hand (numbers match the diagram), layers, meaning of "deep". | Outline section 6 had only key terms and a diagram. | [03](topics/03-ml-neural-networks-deep-learning.md) |
| R18 | New content: generative vs discriminative, tokens, next-token walkthrough, pre-training / fine-tuning / RLHF, sampling and temperature, hallucination. | Outline section 7 was "outline only". | [04](topics/04-generative-ai-and-llms.md) |
| R19 | History expanded into Start / Failures / Big Comeback with a dated 17-row milestone table and causes of each winter and comeback. | Outline section 4 was one paragraph. | [06](topics/06-history-of-ai.md) |
| R20 | Applications analyzed with a six-part framework (input, output, AI type, benefit, risk, human oversight); collaborative-filtering trace; unsourced "how AI helps society" paragraph replaced by sourced cases (Netflix, FDA device list, IDx-DR, Waymo with company-reported caveats, Uber 2018 crash). | Outline section 8 had examples only, unsourced. | [07](topics/07-real-world-applications.md) |
| R21 | Ethics developed into six issues with real cases (Gender Shades, Amazon hiring tool, Obermeyer 2019, Clearview AI, *Mata v. Avianca*, IEA 2025, Arup deepfake), a bias life-cycle aligned with the diagram, and a structured case-analysis method. | Outline section 5 was one sentence. | [08](topics/08-ethics-risks-social-impact.md) |
| R22 | Limitations and misconceptions: six misconceptions stated and corrected; why hallucinations happen; brittleness; four-step checking routine. | Outline section 9 not started. | [09](topics/09-limitations-and-misconceptions.md) |
| R23 | Future of AI: AGI viewpoints presented fairly (no agreed definition or timeline; survey evidence); EU AI Act tiers and timeline including the 2026 "Digital Omnibus" changes; OECD, UNESCO, Council of Europe; AI-literacy checklist. Wording on AGI made consistent with Topic 05. | Outline section 10 was one paragraph. | [10](topics/10-future-of-ai.md) |

## References

| # | What changed | Why | Where |
|---|---|---|---|
| R24 | All references rewritten with author/organization, year, title, URL, access date and the claims each supports; Zenodo upload of Russell & Norvig removed; sources not actually checked (two Taylor & Francis books, the ITU 2026 article, the ISO page) not reused. A consolidated list was created. | Old gap 5. | "Sources" in every topic; [../sources.md](../sources.md) |
| R25 | US spelling and one set of terms used throughout (AI, machine learning (ML), deep learning, neural network, model, training, inference/prediction, training data, features, labels, parameters/weights, generative AI, LLM, token, hallucination, bias). "Bias" in a neuron is explicitly distinguished from unfair bias. | Consistency. | all topics |

## Changes made while adapting to other formats

Changes found while building the slide outlines, video scripts, study guide and test bank are listed in [formats/README.md](formats/README.md#fixes-made-to-the-core-content-while-adapting) and below when they affect the topic files.

| # | What changed | Why | Where |
|---|---|---|---|
| R26 | Topic 07's Visual section pointed to "the pipeline diagram in Topic 03"; corrected to Topic 02, with a link. | Wrong cross-reference, found while writing the slide outlines. | [07 Visual](topics/07-real-world-applications.md) |
| R27 | Topic 09 Key terms: "Next-token prediction" said the model picks "the most likely" token, and "Token" left out punctuation and characters; both now use Topic 04's wording (the model gives every token a probability and usually *samples* one). | It contradicted Topic 04's explanation of sampling and temperature. | [09 Key terms](topics/09-limitations-and-misconceptions.md) |
| R28 | Two-lenses diagram: the limited-memory box said "Uses recent data or past examples"; now "Uses recent observations while it works". | "Past examples" suggested training data, which Topic 05 says is not what "memory" means in this classification. | `assets/images/types-of-ai-two-lenses.svg` (both copies) |
| R29 | Timeline diagram: "1956 Dartmouth workshop: AI named as a research field" → "AI launched as a research field". | The term was coined in the 1955 proposal (Topic 06), not in 1956. | `assets/images/ai-history-timeline.svg` (both copies) |
| R30 | Robot-maze debrief: Q-learning keeps the 12-move route in Maze 2 "from about episode 22" (was 21). | Re-run of the test output showed episode 22. | `../task-2/activities/robot-maze/robot-maze.html` |
| R31 | Topic 06's ELIZA example ("I feel sad" → "Why do you feel sad?") is now labeled as a simplified illustration of its style. | It was presented as if it were a real reply from the 1966 script. | [06 Explanation](topics/06-history-of-ai.md) |
| R32 | Bias life-cycle diagram changed to US spelling ("Labeling", "judgments"). | Consistency with the module's US spelling. | `assets/images/ai-system-lifecycle-bias.svg` (both copies) |
