# Gaps and Open Issues (updated 2026-11-06)

This file tracks what remains uncertain or untested across the module (Task 1) and the study guide, test bank and supplements (Task 2), so that uncertain material is never presented as established fact.

## 1. V1.0 gaps: status

| Old gap | Status | Where fixed |
|---|---|---|
| 1 Learning order | Resolved: ethics moved to Topic 08, after ML and generative AI | [outline §4](00-module-outline.md#4-learning-sequence-and-development-status) |
| 2 Types of AI | Resolved: two separate classifications | [05](topics/05-types-of-ai.md) |
| 3 WEF statistic | Resolved: 170M created / 92M displaced / net +78M | [08](topics/08-ethics-risks-social-impact.md) |
| 4 Image credit | Resolved: replaced by original SVG diagrams | [assets/images/](assets/images/) |
| 5 References | Resolved: full citations in every topic, plus a consolidated, de-duplicated list | [../sources.md](../sources.md) |
| 6 "All generative AI is deep learning" | Resolved: stated as a simplification | [04](topics/04-generative-ai-and-llms.md) |
| 7 Made-up figures | Resolved: labeled "illustrative (made-up)" | [02](topics/02-how-ai-operates.md) |
| 8 "Job taking" wording | Resolved: rewritten as a misconception | [09](topics/09-limitations-and-misconceptions.md) |
| 9 Coverage, prerequisites, adaptation | Resolved: all ten topics written; prerequisites listed; slides, video scripts, study guide and test bank produced | [formats/](formats/README.md), [../task-2/](../task-2/README.md) |

## 2. Content that may change or rests on secondary sources

| # | Issue | Where | How to address |
|---|---|---|---|
| G1 | The EU AI Act's 2026 "Digital Omnibus" changes are very recent. Sources disagree on the date of political agreement (6 or 7 May 2026), and the changes to the AI-literacy duty come only from law-firm summaries. | [10](topics/10-future-of-ai.md); Mission 12; test bank Q112–Q114; slide deck 10; video 10 | Re-check the official EC / EUR-Lex text before each teaching period, then update the topic file first and every adapted resource after it. |
| G2 | Some facts were confirmed only through secondary sources because the primary page blocked automated access: WEF 2025 figures, the ChatGPT launch date, *Mata v. Avianca*, FDA device counts, the Dartmouth proposal date, Russell & Norvig, Bostrom 2014, Rosenblatt 1958, and the OpenAI token rule of thumb. | topic Sources sections; [../sources.md](../sources.md) "Verified" fields | A team member opens each primary source in a browser and confirms the wording. |
| G3 | Classifying the spam filter and face unlock as "reactive" machines is the module's own judgment, and Netflix's classification is disputed. | [05](topics/05-types-of-ai.md); Mission 07; test bank Q65 | Kept, labeled as a judgment, and learners are asked to justify their own answer. |
| G4 | The ELIZA example in Topic 06 is a simplified illustration, and the ELIZA replies predicted in Mission 08 were worked out from its rules, not observed. | [06](topics/06-history-of-ai.md); Mission 08 Activity 8.2 | Type the seven test inputs into the ELIZA page listed in the resources once, and correct the predicted replies if they differ. |

## 3. Activities and resources not yet tried hands-on

| # | Issue | How to address |
|---|---|---|
| T1 | Teachable Machine (Missions 04 and 10) and Survival of the Best Fit (Mission 10) were checked from page content and documentation only, not clicked through. | Run each on a typical learner device and add screenshots. |
| T2 | The TensorFlow Playground preset links were built from the Playground's source code. The expected results come from a simulated re-implementation, and real runs vary because the starting weights are random. | Open each preset once and confirm the stated outcomes. |
| T3 | The video titles, links and chapters were verified through YouTube's own data, but the chosen segments have not been watched. | Watch each segment once, especially the content note in V11. |
| T4 | The SWISH start-screen wording, and whether it works without an account, were not re-tested in a browser. | Confirm and update Mission 03 if needed. |
| T5 | The UI tests for the two HTML activities need the `jsdom` package, which is not shipped with the activities. | Documented in [../task-2/activities/README.md](../task-2/activities/README.md). |

## 4. Review and usability

- **No second reviewer yet:** a second team member has not reviewed the material, so every topic remains "drafted (self-checked)" (see the status labels in the [outline](00-module-outline.md)).
- **No learner trial yet:** no learners have used the guide or test bank. Plan one trial session (for example, Missions 01–02) and note where learners get confused.
- **Length:** topics run longer than first planned (about 3,200–4,300 words of prose each) because they include full worked examples and answers. The slide outlines and video scripts provide shorter routes through the same content.
