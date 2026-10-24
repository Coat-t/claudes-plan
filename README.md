# Claude's Plan

Working repository for team **Claude's Plan** in the AI and Computer Science class.

**Selected module:** AI Overview

## Contents

- [Team Members](#team-members)
- [Strengths and Experience](#strengths-and-experience)
- [Responsibilities](#responsibilities)
- [Collaboration and Workload](#collaboration-and-workload)
- [Project Scope and Learning Goals](#project-scope-and-learning-goals)
- [Planned Learning Resources and Mini Lecture](#planned-learning-resources-and-mini-lecture)
- [Schedule](#schedule)
- [Master Task List](#master-task-list)
- [License](#license)

---

## Team Members

| # | Name   | Role                  | Student ID |GitHub Username |
|---|--------|-----------------------|------------|-|
| 1 | Mukha  | CEO                   | 1820262197 | Coat-t |
| 2 | Hasnat | Content & Media Lead  | 1820262234 | Hasnat-cell |
| 3 | Wasi   | Design & Quality Lead | 1820262191 | AbdulWasii |
| 4 | Liyi    | Research & assessment lead | 1820262281 | keonricecake-dotcom |

## Strengths and Experience

| Member | Strengths |
|--------|-----------|
| Mukha  | Familiar with a wide range of programming languages and tools |
| Hasnat | General programming skills; experienced video editor |
| Wasi   | Fluent in C++, studied since school |
| Liyi   | Good at researching and fact-checking information |

## Responsibilities

| Member | Responsibility |
|--------|----------------|
| Mukha  | Coordinates the team, manages the repository and deadlines, and ensures assignments are completed and submitted properly |
| Hasnat | Leads the creation of learning materials (videos, presentations and written content) and supports research for the module |
| Wasi   | Oversees visual design and presentation, reviews the quality and accuracy of the team's work, and supports technical tasks |
| Liyi   | Gathering information, data and evaluating project quality|

## Collaboration and Workload

Each member leads the area that matches their strengths, while the core work of the module is shared evenly:

- **Ownership by strength:** Mukha coordinates the project and the repository, Liyi gathers important information and sources, Hasnat leads learning materials and media, and Wasi oversees design, quality and technical support.
- **Shared content work:** Research and writing for the AI Overview module are split into sections, and each member takes an equal share alongside their lead role.
- **Peer review:** Nothing is submitted without review by at least one other member, and Wasi does a final quality pass before submission.
- **Transparent tracking:** Tasks are assigned and tracked in this repository, so everyone's contributions are visible and workload can be rebalanced if someone falls behind or is overloaded.

---

## Project Scope and Learning Goals

### Target Learners

Beginners who have basic computer skills and a general idea of how computers work. No programming or mathematics background is required.

### Learning Goals

After using our materials, learners should be able to explain how AI developed and how it works. Specifically, they should be able to:

- Define AI in their own words and recognise it in everyday tools
- Distinguish between AI, machine learning and deep learning, and between the main types of AI
- Describe in simple terms how a model learns from data and makes predictions
- Outline the key milestones in the history of AI
- Discuss the main ethical risks, limitations and social impacts of AI

### Content Outline

- Core Definition
- Types of AI
- How AI Operates
- History and Evolution of AI
- Ethics, Risks, and Social Impact
- Machine Learning, Deep Learning, and Neural Networks
- Generative AI and Large Language Models
- Real-World Applications of AI
- Limitations and Common Misconceptions
- The Future of AI

### Scope Boundaries

| Depth | Topics |
|-------|--------|
| **Explained in detail** | Core definition · Types of AI · How AI operates (data, training, models, predictions) · Machine learning and deep learning concepts · History and evolution (key milestones and turning points) · Ethics, risks, and social impact |
| **Brief introduction** | Neural networks (intuition only) · Generative AI and large language models · Limitations and common misconceptions · The future of AI · Real-world applications (shown through examples throughout rather than as a separate deep dive) |
| **Out of scope** | The mathematics behind AI (calculus, linear algebra, statistics) · Programming or building models · Technical comparisons of specific algorithms and architectures · Reviews of specific commercial AI products |

---

## Planned Learning Resources and Mini Lecture

> These are initial plans and may be revised as the project progresses.

### Shared Markdown Content

The Markdown content is the **single source of truth** for the project: the study guide, slides, videos and mini lecture are all built from it. Each topic in the content outline gets its own file, and every file follows the same template:

1. **Learning objectives:** what the learner should be able to do after the topic
2. **Explanation:** the concept in plain language, avoiding unnecessary jargon
3. **Examples:** everyday, relatable cases (recommendation systems, voice assistants, spam filters, chatbots)
4. **Activity:** a short exercise, discussion question or "spot the AI" task
5. **Key terms:** definitions that are also collected into a shared glossary
6. **References:** the sources used, so every claim can be checked

Proposed repository structure:

```
content/        One Markdown file per topic, plus glossary.md and references.md
study-guide/    Study guide and test bank
slides/         Slide decks and diagram source files
videos/         Video scripts, storyboards and links to published tutorials
```

### Study Guide and Test Bank

- **Study guide:** One section per topic containing a short summary, key terms, a diagram or example, and "check yourself" questions. It suggests a study order that follows the content outline.
- **Test bank:** Questions for every topic, tagged by topic and difficulty (basic / intermediate). Question types include multiple choice, true/false, short answer and scenario-based questions (for example, *"Is this an example of AI? Why or why not?"*). Every question has an answer key with a short explanation.
- **How learners use it:** Read the study guide section, watch the matching video, answer the practice questions, check the explanations, then revisit any topics where they made mistakes.

### PPT Slides

The slides follow the content outline, with one main idea per slide and a consistent visual template maintained by Wasi. Planned visuals include:

- A **nested-circles diagram** showing how AI, machine learning and deep learning relate
- A **flowchart** of the learning process: data → training → model → prediction
- A **timeline** of key milestones in AI history
- A **comparison table** of the types of AI (narrow vs. general, by capability)
- A **worked example** of training a simple classifier (e.g. a spam filter), step by step
- **Case studies** illustrating ethical risks such as biased training data

### Video Tutorials

Short tutorials (around 3–6 minutes each), led by Hasnat and focused on concepts that benefit from narration and demonstration:

| # | Proposed tutorial | Why video works well |
|---|-------------------|----------------------|
| 1 | What is AI? | Introduces the topic with everyday examples learners can see in action |
| 2 | How does a machine learn? | Animating the training process makes an abstract idea concrete |
| 3 | A short history of AI | An animated timeline is easier to follow than a list of dates |
| 4 | How do AI chatbots generate text? | A live demonstration of next-word prediction shows the process clearly |
| 5 | Bias in AI | Walking through a real example shows how bad data leads to unfair results |

### Live Mini Lecture

- **Proposed topic:** *How do machines learn from examples?*
- **Why it matters:** Learning from data is the core idea behind almost all modern AI. Understanding it demystifies AI for beginners and directly explains why data quality causes problems like bias.
- **Demonstration:** A live demo with [Teachable Machine](https://teachablemachine.withgoogle.com/), where we train a simple image classifier in front of the audience (e.g. thumbs up vs. thumbs down) and then test it. We then show it failing on examples unlike its training data.
- **Audience activity:** "Be the model". The audience is shown labelled pictures of two made-up categories and must classify new pictures without being told the rule. This shows that, like a model, they learn patterns from examples. A final tricky example reveals the limits of learning from limited data.

### How the Resources Support One Another

The Markdown content provides accurate, reviewed explanations that every other resource is built from. The **slides** turn that content into visual explanations, the **videos** reuse those visuals and add narration for processes that are hard to follow on paper, and the **study guide and test bank** let learners practise and check their understanding. The **mini lecture** focuses on one manageable question from the broader project: it reuses the slides and the "How does a machine learn?" video material, and its activity is later added to the study guide.

---

## Schedule

| Stage | Deadline | Focus |
|-------|----------|-------|
| 1 | October 24, 2026 | Planning and content foundation |
| 2 | November 7, 2026 | First versions, and live teaching preparation/delivery according to the class schedule |
| 3 | November 28, 2026 | Review, revision, and final delivery |

### Studying the Content

Each member is assigned topics from the content outline to research. Research uses course materials and reliable sources such as textbooks, university course material and reputable publications. Sources are recorded in the topic file's references so other members can verify them.

### Developing and Checking Markdown

Each topic is drafted on its own branch and submitted as a pull request. At least one other member reviews it for accuracy and clarity, and Wasi checks consistency with the template. Content is merged into `main` only after approval, and slides, videos and study materials are produced only from merged content.

### Using GitHub

- **Issues:** one issue per task in the master task list, with an assignee and a deadline
- **Project board:** columns for *Not started*, *In progress*, *Under review* and *Completed*
- **Milestones:** one per stage, so progress towards each deadline is visible
- **Pull requests:** linked to their issues, so the commit and review history records each member's contributions

### Communication, Meetings, and Review

Day-to-day communication happens in the team group chat. The team holds a weekly check-in meeting to review progress, rebalance tasks and agree on next steps. Reviews of written work happen through pull request comments so feedback is recorded alongside the work.

### Risks and Mitigation

We review risks weekly and before each milestone. Each risk has owner, an early-warning signal, and a planned response. If a risk blocks progress for more than 2 working days, it is raised in the team sync. If a milestone is at risk by more than 1 week, we reassign work, descope non-criminal items, or adjust the milestone.

| Risk | Impact | Likelihood | Early warning | Response / Mitigation |
|---|---|---|---|---|
| **Unfamiliar tools or frameworks** | High | Medium | Setup problems, slow PRs, repeated questions | Run a timebox spike, write onboarding/setup notes, pair-program, assign a tool owner, and identify a fallback approach | 
| **Difficult technical/content material** | High | Medium |Repeated blockers, unclear requirements, slow progress on one task | Break work into smaller tasks, do a research spike, consult docs/mentor, build a small proof of concept, and descope non-essential parts |
| **Uneven workload across team** | Medium-High | High | Some members idle while others are overloaded | Weekly capacity check,, visible task board, rebalance tasks, pair on critical items, rotate roles, and escalate persistent imbalance | 
| **Delayed tasks or missed milestones** | High | Medium | Missed checkpoints, long-running blockers, dependencies not ready | Track critical path, add buffer to milestones, keep a blocker log, triage weekly, reassign work, and descope/defer lower-priority tasks |
| **Integration or merge conflicts** | Medium | Medium | Frequent conflicts, failing CI, late integration problems | Use small PRs, merge frequently, require CI checks, review early, and assign integration owner | 
| **Communication gasps** | Medium | Medium | Decisions not documented, duplicate work, unclear ownership | Use one main channel, keep meeting notes and a decision log, post async updates, and make task ownership explicit |
| **AI output quality** | High | Medium | Hallucinated content, unverified code, unclear sources | Require human review, tests, source checks, and an evaluation/prompt log; do not merge unreviewed AI-generated output |
| **Data privacy, security, or licensing** | High | Low-Medium | Unclear data sources, secrets in repo, unclear licenses | Use tasks approved data, never commit secrets, check licenses, apply | least privilege, and review before sharing | 
| **Scope Creep** | Medium | High | New features added''' mid-task, changing requirements | Freeze an MVP scope, move new ideas to backlog, require change review,  and prioritize explicitly |
| **Bus factor/key-person dependency** | High | Medium | Only one person understands a critical part | Document key decisions, pair/rotate ownership, do code walkthroughs, and share critical

### Handling Corrections

When an error is found, a `correction` issue is opened listing every deliverable it affects (Markdown, slides, study guide, test bank, videos). The fix is made in the Markdown first and then applied to each listed deliverable. The issue is closed only when every item on its checklist has been updated.

### Testing, Rehearsal, and Feedback

- Activities and test bank questions are tried out within the team, and with classmates where possible, before the Stage 2 deadline.
- The mini lecture is rehearsed at least twice, with full timed run-throughs, in the week before our scheduled delivery.
- Feedback from classmates and the instructor after Stage 2 is collected as issues and addressed during Stage 3.

---

## Master Task List

Tasks are tracked as [GitHub issues](https://github.com/Coat-t/claudes-plan/issues) on the [project board](https://github.com/users/Coat-t/projects/2), grouped by stage milestones.

---

## License

This project is licensed under the [MIT License](LICENSE).
