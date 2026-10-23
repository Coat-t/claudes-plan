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

| # | Name   | Role                  | Student ID |
|---|--------|-----------------------|------------|
| 1 | Mukha  | CEO                   | 1820262197 |
| 2 | Hasnat | Content & Media Lead  | 1820262234 |
| 3 | Wasi   | Design & Quality Lead | 1820262191 |
| 4 |        |                       |            |

## Strengths and Experience

| Member | Strengths |
|--------|-----------|
| Mukha  | Familiar with a wide range of programming languages and tools |
| Hasnat | General programming skills; experienced video editor |
| Wasi   | Fluent in C++, studied since school |
|        |           |

## Responsibilities

| Member | Responsibility |
|--------|----------------|
| Mukha  | Coordinates the team, manages the repository and deadlines, and ensures assignments are completed and submitted properly |
| Hasnat | Leads the creation of learning materials (videos, presentations and written content) and supports research for the module |
| Wasi   | Oversees visual design and presentation, reviews the quality and accuracy of the team's work, and supports technical tasks |
|        |                |

## Collaboration and Workload

Each member leads the area that matches their strengths, while the core work of the module is shared evenly:

- **Ownership by strength:** Mukha coordinates the project and the repository, Hasnat leads learning materials and media, and Wasi oversees design, quality and technical support.
- **Shared content work:** Research and writing for the AI Overview module are split into sections, and each member takes an equal share alongside their lead role.
- **Peer review:** Nothing is submitted without review by at least one other member, and Wasi does a final quality pass before submission.
- **Transparent tracking:** Tasks are assigned and tracked in this repository, so everyone's contributions are visible and workload can be rebalanced if someone falls behind or is overloaded.
- **New members:** The fourth member will be given a role based on their strengths once they join.

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

### Handling Corrections

When an error is found, a `correction` issue is opened listing every deliverable it affects (Markdown, slides, study guide, test bank, videos). The fix is made in the Markdown first and then applied to each listed deliverable. The issue is closed only when every item on its checklist has been updated.

### Testing, Rehearsal, and Feedback

- Activities and test bank questions are tried out within the team, and with classmates where possible, before the Stage 2 deadline.
- The mini lecture is rehearsed at least twice, with full timed run-throughs, in the week before our scheduled delivery.
- Feedback from classmates and the instructor after Stage 2 is collected as issues and addressed during Stage 3.

---

## Master Task List

Status values: **Not started** · **In progress** · **Under review** · **Completed**

### Stage 1: Planning and Content Foundation (due October 24)

| ID | Task | Expected result | Responsible | Deadline | Status | Dependencies |
|----|------|-----------------|-------------|----------|--------|--------------|
| 1.1 | Set up the GitHub repository | Repository with README and license | Mukha | Oct 23 | Completed | — |
| 1.2 | Define team roles, strengths and responsibilities | Team sections of the README | All (lead: Mukha) | Oct 23 | Completed | 1.1 |
| 1.3 | Define target learners, learning goals, content outline and scope | Project Scope section of the README | All (lead: Hasnat) | Oct 23 | Under review | 1.1 |
| 1.4 | Plan learning resources and the mini lecture | Planned Learning Resources section of the README | All (lead: Hasnat) | Oct 24 | Under review | 1.3 |
| 1.5 | Confirm the mini lecture topic from the topic menu | Topic recorded in the README | All (lead: Mukha) | Oct 24 | In progress | 1.3 |
| 1.6 | Write the schedule, work plan and master task list | Schedule and Master Task List sections of the README | Mukha | Oct 24 | Under review | 1.3, 1.4 |
| 1.7 | Create the content folder structure and topic template | `content/` folder with a template file | Mukha | Oct 24 | Not started | 1.3 |
| 1.8 | Set up the GitHub project board, labels and milestones | Board populated with tasks from this list | Mukha | Oct 24 | Not started | 1.6 |
| 1.9 | Assign research topics to members | One issue per topic, each with an assignee | All (lead: Mukha) | Oct 24 | Not started | 1.3, 1.8 |
| 1.10 | Review and submit the Stage 1 plan | Final README reviewed by all members and submitted | All (lead: Mukha) | Oct 24 | Not started | 1.2–1.9 |
| 1.11 | Onboard the fourth member | Role assigned and README updated | Mukha | When they join | Not started | — |

### Stage 2: First Versions and Live Teaching (due November 7)

| ID | Task | Expected result | Responsible | Deadline | Status | Dependencies |
|----|------|-----------------|-------------|----------|--------|--------------|
| 2.1 | Research assigned topics and draft Markdown content | One Markdown file per topic, submitted as a pull request | All | Oct 31 | Not started | 1.7, 1.9 |
| 2.2 | Peer-review Markdown content | All topic files approved and merged | All (lead: Wasi) | Nov 2 | Not started | 2.1 |
| 2.3 | Create the slide template and first version of the slides | Slide deck v1 | Wasi | Nov 4 | Not started | 2.2 |
| 2.4 | Write the study guide and test bank v1 | Study guide and test bank files | Mukha | Nov 4 | Not started | 2.2 |
| 2.5 | Script and record the first video tutorials | Scripts and first video drafts | Hasnat (all contribute scripts) | Nov 6 | Not started | 2.2, 2.3 |
| 2.6 | Prepare the mini lecture slides, demo and audience activity | Mini lecture materials | All (lead: Mukha) | Nov 4 | Not started | 1.5, 2.3 |
| 2.7 | Rehearse the mini lecture and test activities | Two timed rehearsals and feedback notes | All | Before delivery | Not started | 2.6 |
| 2.8 | Deliver the mini lecture | Lecture delivered | All | Per class schedule | Not started | 2.7 |
| 2.9 | Submit Stage 2 first versions | All first-version deliverables submitted | Mukha | Nov 7 | Not started | 2.3–2.5 |

### Stage 3: Review, Revision, and Final Delivery (due November 28)

| ID | Task | Expected result | Responsible | Deadline | Status | Dependencies |
|----|------|-----------------|-------------|----------|--------|--------------|
| 3.1 | Collect and organise feedback | Feedback recorded as issues | All (lead: Mukha) | Nov 12 | Not started | 2.8, 2.9 |
| 3.2 | Revise Markdown content and apply corrections | Updated content; correction issues closed | All | Nov 19 | Not started | 3.1 |
| 3.3 | Finalise the slides | Final slide deck | Wasi | Nov 22 | Not started | 3.2 |
| 3.4 | Finalise the study guide and test bank | Final study guide and test bank | Mukha | Nov 22 | Not started | 3.2 |
| 3.5 | Finalise and edit the video tutorials | Final published videos | Hasnat | Nov 24 | Not started | 3.2, 3.3 |
| 3.6 | Final quality review of all deliverables | Review checklist completed | Wasi | Nov 26 | Not started | 3.3–3.5 |
| 3.7 | Final submission | All deliverables submitted | Mukha | Nov 28 | Not started | 3.6 |

---

## License

This project is licensed under the [MIT License](LICENSE).
