# Task 3: Teaching Slides for *Pixel's AI Field Guide* (Version 1.0, 2026-11-06)

Three PowerPoint decks for teaching the AI Overview module live to a large group of beginners. Each deck is one session of about 60 minutes, and all three together tell one story: **how machines learn → how chatbots write → who is responsible when AI gets it wrong**. Every slide that needs explanation has presenter notes with key points, timings, questions with expected answers, demo steps with fallbacks, common misconceptions, sources, and the related study-guide and test-bank sections.

| File | Session | Opening question, resolved at the end | Topics → missions | Practice |
|---|---|---|---|---|
| [part-1-how-machines-learn.pptx](part-1-how-machines-learn.pptx) | 1 (28 slides) | "Your inbox blocked spam it had never seen. Who wrote the rule?" → *nobody: it was learned from labeled examples* | 01–03 → Missions 01–05 | Q1–Q49 |
| [part-2-chatbots-types-history.pptx](part-2-chatbots-types-history.pptx) | 2 (22 slides) | "The cat sat on the ___" → *a chatbot predicts likely tokens; why AI took off now* | 04–06 → Missions 06–08 | Q50–Q78 |
| [part-3-ai-in-the-world.pptx](part-3-ai-in-the-world.pptx) | 3 (26 slides) | A lawyer cited six fake cases found with ChatGPT → *the human user stays accountable; what the rules add* | 07–10 → Missions 09–12 | Q79–Q115 |

Missions are in [../task-2/study-guide/](../task-2/study-guide/00-start-here.md) and questions in [../task-2/test-bank/test-bank.md](../task-2/test-bank/test-bank.md). Mission 03 (Prolog) is not taught live; the Part 1 "Next steps" slide points learners to it.

## How the decks are built

- **Story in each part:** opening problem (`MISSION BRIEF`) → brief roadmap → core ideas in order, with section slides between them → audience tasks (`PREDICT` / `TRY IT` / `CHECK`) → answers on the **following** slide (`DEBRIEF`) → final insight (`TAKEAWAY`) → `NEXT STEPS` with exact file names and question numbers. Each part saves its strongest moment for the end: the spam-filter resolution and neural-network demo in Part 1, "why did AI explode now?" in Part 2, and the courtroom resolution plus an AI-literacy checklist in Part 3.
- **Show, not tell:** worked examples are spread over several slides:
  - river-crossing states reached at each search level, then the two 7-crossing plans
  - scoring spam emails, then the false-positive / false-negative trade-off
  - the fruit models' training vs test scores (overfitting)
  - one neuron by hand
  - the next-token loop and temperature
  - the collaborative-filtering trace
  - EU AI Act tiers with their dates
- **Audience participation:** 20 activities that work with a large group (hand votes, 30–60 seconds with a neighbor, quick calculations). Answers are never on the same slide as the question.
- **Identity:** the same name, characters (Pixel and Dr. Ada Okafor), colors, labels and examples as the study guide, test bank, diagrams and video scripts.
- **Readability:**
  - 16:9 slides with dark navy text on a white background.
  - Titles are 32–40 pt, body text 28–30 pt, and tables and captions at least 24 pt. Only the footer and activity labels are smaller, and this was checked by script.
  - Each slide has one purpose and at most 4–6 short lines.
  - Pictures have alt text.

## Demonstrations (all optional; each has a fallback)

| Slide | Demo | Needs | Fallback |
|---|---|---|---|
| Part 1 "Pixel's river problem" | [river-crossing.html](../task-2/activities/river-crossing/river-crossing.html) | nothing (works offline) | the next three slides |
| Part 1 "Live demo: TensorFlow Playground" | presets P1 and P2 (URLs in the notes) | internet, no account | expected results in the notes; Mission 05 simulated results |
| Part 2 "The start" | ELIZA web version (listed in [resources](../task-2/study-guide/resources.md)) | internet | Mission 08 Activity 8.2 sample transcript |
| Part 3 "Unbalanced training data" | Teachable Machine | internet, webcam, volunteers who consent | Mission 10 Activity 10.2 made-up results table |

## Rebuilding and keeping slides consistent

All slide text and notes are in [build_slides.py](build_slides.py). To rebuild:

1. Run `pip install python-pptx`.
2. Run `python build_slides.py`.

The diagrams in `assets/png/` are rendered from `../task-1/assets/images/*.svg` with `rsvg-convert -z 2 -b white`. The `_trim_*.png` files are cropped copies that the script creates automatically.

Every fact and number comes from the Task 1 topic files. **If something changes, fix the topic file first, then this script, then rebuild**, as described in [../task-1/formats/README.md](../task-1/formats/README.md). Sources are the ones already listed in [../sources.md](../sources.md); no new sources were used.

The decks replace the earlier text outlines in `../task-1/formats/slides/`. Those outlines remain as a one-deck-per-topic reference.

## Review and rehearsal (2026-11-06)

**Checked:**
- All three decks were converted to PDF with LibreOffice and inspected as rendered pages. Fixes made after that check:
  - Titles that wrapped onto two lines were shortened or reduced in size.
  - Captions that ran into the footer were shortened.
  - The neuron diagram moved from the question slide to the answer slide, because it showed the result.
  - The river-crossing state graph was too dense to project, so it is now a large table. The full graph is offered as a handout.
- Numbers in the slides were cross-checked against the topic files and the study guide. These include the spam weights and 93% test accuracy, the neuron sum of 0.4, the next-token probabilities, the WEF figures, Gender Shades, and the EU AI Act dates.

**Still open:**
- **Diagram labels:** some module diagrams (two lenses, timeline, bias life cycle, ML pipeline) still have small labels when projected. Their key points are repeated in large text on the slide or in the notes for the presenter to say aloud. Drawing simplified slide-only versions would make them easier to read at the back of a room.
- **No real-room test:** the decks have not been shown on a projector, timed in a real rehearsal, or tested in PowerPoint itself; only the LibreOffice rendering was checked. The demos need a live check on the day: Playground presets, ELIZA and Teachable Machine.
- **EU AI Act dates:** these reflect the 2026 changes and should be re-checked before each teaching period (gap G1 in [../task-1/gaps-and-open-issues.md](../task-1/gaps-and-open-issues.md)).
