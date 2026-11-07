# AI Overview: Module Outline (V1.0)

**Team:** Claude's Plan - **Last updated:** 2026-10-25

This outline covers the whole module. The learning outcomes, prerequisites, topics, scope and planned resources come from the team's project plan in the [README](../README.md). The developed content is in [01-overview-of-ai.md](01-overview-of-ai.md).

## Intended learning outcomes

After using our materials, learners should be able to explain how AI developed and how it works. Specifically, they should be able to:

- Define AI in their own words and recognise it in everyday tools
- Distinguish between AI, machine learning and deep learning, and between the main types of AI
- Describe in simple terms how a model learns from data and makes predictions
- Outline the key milestones in the history of AI
- Discuss the main ethical risks, limitations and social impacts of AI

## Prerequisites

Beginners who have basic computer skills and a general idea of how computers work. No programming or mathematics background is required.

## Status labels

| Label | Meaning |
|---|---|
| outline only | Subtopics are listed; no learning content yet |
| drafted | Learning content is written and has been through a pull-request review |
| checked | Claims, examples and sources have been verified by a second member |
| needs revision | Content exists, but a review found problems that still have to be fixed |

## Learning sequence and development status

| # | Topic | Subtopics | Depth | Planned examples, visuals and activities | Developed in | Status |
|---|---|---|---|---|---|---|
| 1 | Core Definition | What is AI? - How it works | Detailed | Video 1 "What is AI?"; everyday examples; "AI in Your Day" activity | 01 §1, §4, §5 | drafted |
| 2 | Types of AI | Narrow AI - General AI - Limited Memory - Reactive Machines | Detailed | Comparison table of the types of AI | 01 §1 (table) | needs revision (gap 2) |
| 3 | How AI Operates | Data - Algorithms - Old vs. New | Detailed | Flowchart data → training → model → prediction; spam-filter worked example; Video 2 "How does a machine learn?"; mini lecture demo and "Be the model" activity | 01 §1, §2 | drafted |
| 4 | History and Evolution of AI | The Start - The Failures - The Big Comeback | Detailed | Timeline of key milestones; Video 3 "A short history of AI" | One paragraph in 01 §1 | outline only |
| 5 | Ethics, Risks, and Social Impact | AI Bias - Privacy - Jobs | Detailed | Case studies of biased training data; Video 5 "Bias in AI" | One sentence in 01 §1 | outline only |
| 6 | Machine Learning, Deep Learning, and Neural Networks | Machine Learning - Neural Networks - Deep Learning | Detailed (neural networks: intuition only) | Nested-circles diagram | 01 §1 (key terms), §3 (visual) | needs revision (gaps 4, 6) |
| 7 | Generative AI and Large Language Models | Generative AI - LLMs | Brief | Video 4 "How do AI chatbots generate text?" | Mentioned in 01 §1, §3 | outline only |
| 8 | Real-World Applications of AI | Recommendation Systems - Healthcare - Transportation | Brief, shown through examples | Examples throughout the module | Examples in 01 §1, §5 | outline only |
| 9 | Limitations and Common Misconceptions | AI is not alive - Hallucinations - Job taking | Brief | None planned yet | Not started | outline only (gap 8) |
| 10 | The Future of AI | AGI - Rules | Brief | None planned yet | One paragraph in 01 §1 | outline only (gap 3) |

Sections 1, 2, 3 and 6 are covered by one connected topic file, [01-overview-of-ai.md](01-overview-of-ai.md), which includes explanations, key terms, a worked example, a visual, a learner activity, an expected outcome and references. Out of scope (from the README): the mathematics behind AI, programming or building models, technical comparisons of algorithms, and reviews of commercial products.

## Gaps and uncertainties

Items 1 to 8 were found during the resubmission check on 2026-10-25. That check was AI-assisted (see `logs/ai-use.md`), and the team has not yet confirmed or fixed these items.

1. **Learning order:** Ethics (5) comes before Machine Learning (6) and Generative AI (7), but AI bias is explained in terms of training data. The team still needs to decide whether to move Ethics after section 7.
2. **Types of AI:** The README outline mixes two different classifications: by capability (narrow and general) and by functionality (reactive machines and limited memory). The developed table uses a third set (narrow, general and superintelligent). One consistent explanation is needed.
3. **Statistic:** The *Future impact* paragraph in 01 §1 says the World Economic Forum expects 91 million jobs to be displaced by 2030. The WEF *Future of Jobs Report 2025* (press release, 8 January 2025) gives 92 million displaced, 170 million created and a net gain of 78 million.
4. **Image credit:** The nested-circles diagram in 01 §3 came from an external source that was not recorded. The source must be found and credited, or the image must be replaced with the team's own diagram.
5. **References:** The references in 01 §6 have no authors, URLs or access dates. Reference 1 points to a Zenodo upload of Russell and Norvig's textbook rather than to the book itself. Reference 7 (ISO) is missing from the README source list, and some README sources are not cited anywhere in the content.
6. **Simplification:** 01 §3 says "all generative AI is deep learning". This is true of today's main systems (such as ChatGPT), but it is a simplification. The team should decide whether to say so.
7. **Worked example:** The figures in 01 §2 (10,000 emails, 95% of spam) are illustrative and not taken from a source. They should be labelled as a made-up example.
8. **Misconceptions:** In section 9, "Job taking" is listed as a misconception but is worded as a fact.
9. **Coverage:** Sections 4, 5, 7, 8, 9 and 10 are still outlines. Section-level prerequisites have not been identified yet. Issue #6 (how each topic becomes study-guide, slide and video material) is still open.
