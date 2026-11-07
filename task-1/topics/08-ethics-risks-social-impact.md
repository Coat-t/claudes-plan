# 08: Ethics, Risks and Social Impact of AI

**Module:** AI Overview · **Version:** 2.0 · **Status:** drafted (self-checked) · **Last updated:** 2026-11-06

## Learning goals

After this topic, you should be able to:

- **Explain** how bias can enter an AI system at each stage of its life cycle (data, labels, design, deployment), using a real case as evidence.
- **Distinguish** six major ethical issues in AI: bias, privacy, jobs, accountability and transparency, environmental cost, and misinformation (including deepfakes).
- **Interpret** the World Economic Forum's 2025 job projections correctly, including what a "net" figure hides.
- **Analyze** a case study with a structured method: stakeholders, benefits, harms, evidence and safeguards.
- **Propose and justify** practical safeguards for a given AI system.

## Prerequisites

- [Topic 02: How AI operates](02-how-ai-operates.md): training data, training vs inference.
- [Topic 03: ML, neural networks and deep learning](03-ml-neural-networks-deep-learning.md): features, labels, supervised learning, why deep networks are hard to inspect.
- [Topic 04: Generative AI and LLMs](04-generative-ai-and-llms.md): how generative AI creates text, images and audio.
- [Topic 07: Real-world applications](07-real-world-applications.md): the six-part framework (input, output, AI type, benefit, risk, human oversight).

## Key terms

| Term | Plain-English definition |
|---|---|
| Ethics | Thinking carefully about what is right and fair, and about who is helped or harmed by a choice. |
| Bias (in AI) | When an AI system's outputs are systematically less accurate or less fair for some groups of people than for others. |
| Training data | The examples a model learns from. If they are unbalanced or reflect past unfairness, the model can learn that pattern. |
| Proxy | A measurable stand-in for something hard to measure, e.g. using "past healthcare spending" as a stand-in for "how sick someone is". A poor proxy can create bias. |
| Stakeholder | Anyone affected by a system: users, the people it makes decisions about, the company, workers, society. |
| Privacy | People's control over information about themselves: what is collected, how it is used, and who sees it. |
| Personal data | Information that identifies a person or can be linked to them: name, face, location, voice, browsing history. |
| Accountability | Being clearly responsible for a decision and its consequences, and able to be held to account (e.g. by a court or regulator). |
| Transparency | Being open about when AI is used, what data it uses, and how it reaches its outputs. |
| Explainability | The ability to give a human-understandable reason for a specific AI output ("why was my loan refused?"). |
| Black box | A system whose internal workings are too complex for people to inspect directly. Large neural networks are often described this way. |
| Deepfake | Realistic fake audio, image or video of a real person, made with generative AI. |
| Misinformation / disinformation | False information. *Misinformation* is spread by mistake; *disinformation* is spread deliberately to deceive. |
| Job displacement | Existing jobs disappearing or changing so much that the workers need to move to other work. |

## Explanation

### 1. Why AI raises ethical questions

An AI system is built by people who choose **what problem to solve, what data to use, what to predict, and where to deploy it**. Each choice can help or harm people. AI raises special concerns because it:

- works at **massive scale**: one flawed model can affect millions of decisions;
- learns from **historical data**, which can carry past unfairness into the future;
- can be **hard to inspect** (a "black box"), so errors are harder to spot and challenge;
- can **create convincing content**, which can be used to deceive.

A simple way to start any ethical analysis is to ask four questions: **Who benefits? Who could be harmed? What could go wrong? Who is responsible if it does?** This topic covers the six issues that come up most often.

### 2. Bias: when AI is less fair for some groups

**Where does bias come from?** A model learns patterns from its training data, so problems in the data, or in the choices people make around the model, become problems in the outputs. Bias can enter at every stage of an AI system's life cycle (see also the Visual section):

| Stage | How bias can enter | Example |
|---|---|---|
| 1. Problem definition (what to predict) | A convenient proxy is chosen instead of the real goal | Predicting healthcare *cost* instead of health *need* |
| 2. Data collection | Some groups are missing or under-represented, or data reflect past discrimination | A face dataset that is mostly lighter-skinned men |
| 3. Labeling | The "answers" come from human judgments that may carry prejudice; categories may be too simple | Past hiring decisions used as the label "good candidate"; gender labeled as only two options |
| 4. Training | The model copies patterns in the data, unfair ones too; small groups can be ignored | A resume model learns that "women's" predicts "not hired" |
| 5. Testing | Accuracy is checked only overall, so poor results for some groups stay hidden | 95% overall accuracy hiding 65% for one group (illustrative made-up figures) |
| 6. Deployment | The system is used on different people or in a different setting than it was built for | A model trained in one country used in another |
| 7. Feedback and monitoring | Biased outputs shape the new data that trains the next model, so bias can grow | A recommender that shows mostly popular items makes them even more popular, so they dominate the next round of training data |

**Case 1: Gender Shades (2018).** Researchers Joy Buolamwini and Timnit Gebru tested three commercial **gender classification** systems (AI services that look at a face photo and output "male" or "female"), from IBM, Microsoft and the Chinese company Face++. First they noticed that two popular face datasets used to build and test such systems were mostly lighter-skinned people (about 80% and 86%). So they built a new, balanced test set of 1,270 photos of members of parliament from three African and three European countries, and labeled each face by gender and by skin type.

Results: all three systems were most accurate for **lighter-skinned men** (worst error rate 0.8%) and least accurate for **darker-skinned women**, with error rates of up to **34.7%**. The overall accuracy figures that companies reported had hidden this gap, because the test sets did not contain enough darker-skinned women to show the problem. The study shows two lessons:

1. **Unrepresentative data** produces unequal performance.
2. **Test results must be broken down by group** (this is called a **disaggregated evaluation**), or the gap stays invisible.

(Note the limitations of the study itself: it tested gender *classification*, not face *recognition* of individuals, and used a binary gender label, which the authors acknowledged as a simplification.)

**Case 2: biased hiring (2018).** Reuters reported in 2018 that Amazon had abandoned an experimental AI tool for rating job applicants' resumes. It had been trained on resumes submitted over about ten years, mostly from men, and it learned to **penalize resumes containing the word "women's"** (as in "women's chess club captain"). Nobody programmed it to discriminate; it learned the pattern from past hiring. Amazon said the tool was never used by recruiters to evaluate candidates on its own.

**Case 3: a biased proxy in healthcare (2019).** As described in [Topic 07](07-real-world-applications.md), a widely used algorithm predicted *healthcare spending* as a stand-in for *health need*. Because less had historically been spent on Black patients with the same illness, the algorithm under-identified them for extra care. The bias came from a **design choice**, not just the data.

**What helps:** more representative data; testing performance separately for different groups; choosing targets carefully; diverse development teams; independent audits; and the ability for affected people to challenge decisions.

### 3. Privacy: what data, whose consent?

AI depends on data, and much of that data is about people. Privacy concerns include:

- **Collection without consent.** Many AI models are trained on material collected (scraped) from the internet, including personal photos and posts. In September 2024 the Dutch Data Protection Authority fined the facial-recognition company **Clearview AI** €30.5 million under European data-protection law (GDPR) for building a database of billions of face photos scraped from the internet without people's knowledge or consent.
- **Inference of sensitive information.** AI can *guess* things you never shared, such as health conditions or political views, from patterns in shopping, location or "likes".
- **Surveillance.** Face recognition in public spaces can track people's movements. (The EU AI Act bans some uses of this; see [Topic 10](10-future-of-ai.md).)
- **What you type into chatbots.** Conversations with AI services may be stored and, depending on the provider's settings, used to improve models. Never paste other people's personal data or confidential information into a public chatbot unless you know how it will be handled.

**What helps:** collecting only the data that is needed (data minimization), clear consent, anonymizing data, strong security, and laws such as the EU's GDPR that give people rights over their data.

### 4. Jobs: displacement, creation and change

**The best-known projection.** The World Economic Forum (WEF) *Future of Jobs Report 2025* (published January 2025) surveyed more than 1,000 large employers, representing over 14 million workers in 55 economies. Their combined expectation for **2025–2030**:

- about **170 million** new jobs created (about 14% of today's jobs),
- about **92 million** jobs displaced (about 8%),
- a **net gain of about 78 million** jobs (170 − 92 = 78).

> **Correction note:** our earlier draft said "91 million" jobs displaced. The correct WEF 2025 figure is **92 million**.

**How to read these numbers carefully:**

1. **They are projections, not facts.** They are what employers *expect*, and expectations can be wrong.
2. **They are not only about AI.** The WEF attributes the change to several trends together: technology (including AI), the green energy transition, economic pressures and population changes.
3. **"Net gain" hides real losses.** The new jobs are often in *different* places, sectors and skill levels from the lost ones. A cashier whose job disappears does not automatically become a data analyst. Around 22% of jobs are expected to be affected by this churn (created or destroyed), and employers expect a large share of workers' core skills (nearly two-fifths) to change by 2030.

**Tasks vs jobs.** AI usually automates **tasks**, not whole jobs. A radiologist's job includes reading images, talking to patients, consulting colleagues and deciding treatments; AI may speed up one task. Some jobs mostly made of automatable tasks (e.g. routine data entry) are at high risk; many others will change rather than vanish. This is why "AI will take all jobs" is a **misconception** (see [Topic 09](09-limitations-and-misconceptions.md)), while "AI will cause serious disruption for some workers" is a real concern.

**What helps:** retraining and education, social safety nets, and involving workers in decisions about how AI is introduced.

### 5. Accountability and transparency

**Accountability: who is responsible?** When an AI system causes harm, responsibility can be unclear: the company that built the model? The organization that deployed it? The person who relied on it? Two examples:

- **The lawyers and the invented cases (2023).** In the US case *Mata v. Avianca*, lawyers submitted a court brief citing six court decisions that did not exist. They had been generated by ChatGPT. In June 2023 a federal judge fined the lawyers and their firm $5,000 in total. The lesson: **the human who uses an AI output remains responsible for it.** "The AI said so" is not a defense.
- **The self-driving test car (2018).** In the Uber crash described in [Topic 07](07-real-world-applications.md), investigators found failures in the software, the distracted safety driver, the company's safety culture *and* the regulators. Responsibility was shared, which makes accountability harder.

**Transparency and explainability.** People affected by AI decisions should be able to know *that* AI was used, and ideally *why* it produced a particular output. Large neural networks contain millions or billions of learned weights (see [Topic 03](03-ml-neural-networks-deep-learning.md)), so even their designers cannot simply read off the reason for one decision. This is the **black box** problem. Researchers work on **explainable AI** methods, and laws increasingly require disclosure, for example telling people when they are talking to a chatbot.

**What helps:** clear rules about who is responsible; keeping records (logs) of how decisions were made; a right to human review of important automated decisions; and independent audits.

### 6. Environmental cost

Training and running large AI models requires huge **data centers** full of powerful chips, which use electricity (and often water for cooling). The International Energy Agency (IEA) projected in April 2025 that electricity use by data centers worldwide will **more than double by 2030, to around 945 terawatt-hours (TWh) a year**, slightly more than the whole of Japan uses today. Demand from data centers specially designed for AI is projected to **more than quadruple** in the same period. The IEA also noted that the extra emissions could be small compared with the whole energy sector, and might be offset if AI is used to make energy systems more efficient, but that is not guaranteed.

Two points for learners:

- Every AI query has a real-world energy cost, though one query is small; the impact comes from **billions** of queries and from training ever-larger models.
- The environmental cost is unequal: data centers affect local electricity grids and water supplies in the places where they are built.

**What helps:** more efficient models and chips, renewable energy, reporting energy use, and choosing a smaller tool when a big one is not needed.

### 7. Misinformation and deepfakes

Generative AI (see [Topic 04](04-generative-ai-and-llms.md)) can produce realistic text, images, audio and video in seconds. That brings two risks:

- **Accidental misinformation**: LLMs can **hallucinate**, producing fluent but false statements (see [Topic 09](09-limitations-and-misconceptions.md)), which people then repeat.
- **Deliberate disinformation and fraud**: **deepfakes** of real people. In early 2024, an employee at the Hong Kong office of the engineering firm **Arup** joined a video call with people who looked and sounded like the company's chief financial officer and other colleagues. All of them were deepfakes. The employee made 15 transfers totaling HK$200 million (about US$25 million) to the criminals.

Deepfakes can also be used to fake statements by politicians, harass people with fake intimate images, or create "plausible deniability", letting someone dismiss a *real* recording as fake.

**What helps:** checking unexpected requests through a second channel (call the person back on a known number); labeling and watermarking AI-generated content (the EU AI Act requires labeling of deepfakes; see [Topic 10](10-future-of-ai.md)); media literacy; and laws against harmful uses.

### 8. Putting it together: a structured way to analyze a case

When you meet a new AI case, work through these steps:

1. **Describe the system** (input → output, AI type, who uses it, on whom).
2. **List the stakeholders**, including people who don't use the system but are affected by it.
3. **Benefits**: who gains, and how much?
4. **Harms**: check each of the six issues (bias, privacy, jobs, accountability/transparency, environment, misinformation). Which apply?
5. **Evidence**: is there data (e.g. error rates by group) or a similar real case?
6. **Safeguards**: what would reduce the harms? Who is accountable?
7. **Judgment**: should it be used as is, used with conditions, or not used? Justify.

## Worked example

**Tracing how bias enters a hiring model, and how to fix it**

*The company and all figures below are illustrative (made-up) figures, inspired by the real Amazon case.*

"HireFast Ltd" wants an AI to score job applications for software engineering roles.

| Step | What HireFast does | What happens inside | Bias check |
|---|---|---|---|
| 1. Collect training data | Uses 10,000 past applications from the last 10 years; **label** = "was hired" (yes/no) | 80% of past applicants and 85% of past hires were men | **Problem**: the labels reflect past hiring decisions, which may themselves have been biased |
| 2. Extract features | Turns each resume into features: words used, university, years of experience, clubs | Words such as "women's" (e.g. "women's coding society") appear mostly on women's resumes | **Problem**: some features act as **proxies** for gender |
| 3. Train | The model learns which features predict "was hired" | Because fewer women were hired, it learns that "women's" is linked with "not hired" and gives it a negative weight | Nobody wrote "prefer men", but the model learned it |
| 4. Test | Overall accuracy at predicting past hires: 90% | Looks excellent, but it is excellent at copying the *past* | **Problem**: no separate results by gender |
| 5. Deploy | Scores new applicants; top 20% invited to interview | Equally qualified women receive lower scores | Harm at scale: thousands of applicants affected |

**Fixes, step by step:**

1. **Data**: check how balanced the data are; think about whether "was hired" is a fair label at all (perhaps "performed well after one year" is better, though that may also carry bias).
2. **Features**: remove obvious proxies (club names, gendered words), knowing that subtle proxies can remain.
3. **Testing**: measure performance and selection rates *separately* for men and women (and other groups). Compare: if 20% of men but only 10% of equally qualified women are invited, investigate.
4. **Deployment**: use the AI only to assist; humans review decisions; applicants can request human review; audit regularly.
5. **Judgment**: if bias cannot be reduced to an acceptable level, **do not deploy**. This is what Amazon eventually did with its tool.

## Visual

![The AI system life cycle as a loop of seven stages (problem definition, data collection, labeling, training, testing, deployment, feedback and monitoring) with warning boxes showing where bias can enter: wrong proxy target, unrepresentative data, biased labels, learning unfair patterns, test set missing groups, different population, feedback loops](../assets/images/ai-system-lifecycle-bias.svg)

*Figure: Bias can enter an AI system at every stage of its life cycle, not only through the training data.* (Original diagram created for this module.)

**Summary table: six issues at a glance**

| Issue | Core question | Real example | One safeguard |
|---|---|---|---|
| Bias | Is it equally accurate and fair for everyone? | Gender Shades: up to 34.7% vs 0.8% error | Test results separately for each group |
| Privacy | Whose data, with what consent? | Clearview AI fined €30.5M (2024) | Data minimization and consent |
| Jobs | Who loses work, who gains it? | WEF: 170M created, 92M displaced (2025–2030) | Retraining and safety nets |
| Accountability & transparency | Who is responsible, and can we see why? | *Mata v. Avianca*: lawyers fined for fake AI citations | Human remains responsible; logs; right to review |
| Environmental cost | What energy and water does it use? | IEA: data-center electricity to ~945 TWh by 2030 | Efficient models, renewable power |
| Misinformation & deepfakes | Can people tell what is real? | Arup deepfake video-call fraud (HK$200M) | Verify through a second channel; labeling |

## Common mistakes

1. **"Computers are neutral, so AI can't be biased."** Correction: AI learns from data created by people and is designed by people. Gender Shades and the Amazon tool show that AI can copy and even scale up human bias.
2. **"Bias only comes from bad data."** Correction: it can also come from labels, from choosing a poor proxy target (the healthcare cost example), from testing only overall accuracy, and from deploying a system in a setting it wasn't built for.
3. **"The WEF says AI will create 78 million jobs, so nobody will lose out."** Correction: 78 million is a *net* figure (170 million created minus 92 million displaced), it covers several trends besides AI, and the new jobs often need different skills in different places. Many individual workers will need support.
4. **"If the AI made the mistake, the AI is responsible."** Correction: AI systems are not legal persons. People and organizations that build, deploy and use them are responsible, as the *Mata v. Avianca* sanctions show.

## Try it yourself

### Activity 1: Name the issue (apply + justify)

For each short scenario, name the **main** ethical issue from the six in this topic and justify your choice in one sentence. Some have a second issue too; name it if you spot it.

1. A photo app's "beautify" filter consistently lightens darker skin tones.
2. A fitness app sells users' location histories to advertisers without telling them clearly.
3. A bank's AI refuses a loan, and nobody at the bank can tell the customer why.
4. A fake audio clip of a mayor "admitting" to a crime spreads on social media the day before an election.
5. A company trains a new, much larger chatbot model, increasing its data center's electricity use sharply.
6. A call center replaces most of its human agents with an AI voice system.

### Activity 2: Check the numbers (interpret data)

Use the WEF *Future of Jobs Report 2025* figures from Section 4.

1. Show the calculation for the net change in jobs.
2. For every 10 jobs created, about how many are displaced? (Round to the nearest whole number.)
3. A news headline says: **"AI to create 78 million new jobs by 2030."** Identify **two** ways this headline is misleading.
4. Explain in 2–3 sentences why a net gain can still mean serious hardship for some people.

### Activity 3: Case study: "SafeStation" face recognition (structured analysis)

*SafeStation is a fictional scenario made up for this activity. Use only the facts given.*

> The city of Rivertown wants to install **SafeStation** at its central train station. Cameras film everyone entering. A deep-learning face-recognition system compares each face with a police "watch list" of 500 wanted people and alerts officers when it finds a possible match. Officers then stop and question the person. Facts: (a) about 60,000 people pass through each day; (b) the vendor reports 99% accuracy but tested mainly on photos of lighter-skinned adults; (c) images of all passers-by are stored for 30 days; (d) passengers are not told about the system; (e) the vendor will not explain how the model works, calling it a trade secret; (f) the city says it will reduce the number of security guards needed.

Complete the structured analysis from Section 8:

1. Describe the system (input → output, AI type).
2. List at least **four** stakeholders.
3. State at least **two** benefits.
4. Identify at least **four** possible harms, each linked to one of the six issues and to a specific fact (a–f).
5. Use **evidence from this topic** to explain why fact (b) is a concern.
6. Do a quick calculation: if the system wrongly flags just 0.1% of innocent passers-by (a made-up rate), how many false alerts would officers receive per day?
7. Propose **at least four** safeguards.
8. Give your **judgment**: deploy as is, deploy with conditions, or do not deploy? Justify in 3–4 sentences.

## Answers

<details>
<summary>Show answers</summary>

**Activity 1**

1. **Bias**: the filter treats darker skin as something to "fix", probably because its training data or its designers' idea of "beautiful" favored lighter skin. (Second issue: social harm to self-image.)
2. **Privacy**: personal location data is sold without clear consent. (Second: transparency, because users aren't told.)
3. **Accountability and transparency**: the decision cannot be explained, so the customer cannot challenge it. (Possibly bias too, if it can't be checked.)
4. **Misinformation / deepfakes**: a fabricated recording of a real person is used to deceive voters (disinformation).
5. **Environmental cost**: a larger model increases electricity use (and possibly water use).
6. **Jobs**: the human agents' jobs are displaced. (Second: accountability, if callers can no longer reach a human for complex problems.)

**Activity 2**

1. 170 million − 92 million = **78 million** net new jobs.
2. 92 ÷ 170 ≈ 0.54, so about **5 jobs displaced for every 10 created**.
3. Misleading because: (a) 78 million is the **net** figure; the report actually projects 170 million *created* and 92 million *displaced*; (b) the change is driven by **several trends**, not AI alone; (c) it is a **projection** from employer surveys, not a certainty. (Any two.)
4. The people who lose jobs are often not the people who get the new ones: new jobs may be in different industries, places or skill levels. Without retraining and support, displaced workers can face unemployment or lower pay even while the overall total grows.

**Activity 3: model answer**

1. **System:** input = live camera video of faces; output = an alert "possible match with person X on the watch list"; AI type = **deep learning** (computer vision/face recognition), used for **inference** on each new face.
2. **Stakeholders:** passengers (all 60,000 a day); people on the watch list; police officers; the city council; the vendor; security guards whose jobs may go; groups at higher risk of misidentification (e.g. darker-skinned passengers); civil-liberties organizations.
3. **Benefits:** may help catch wanted people faster; may deter crime; may reduce costs for the city.
4. **Harms** (any four, each linked to a fact):
   - **Bias** (b): tested mainly on lighter-skinned adults, so it may produce more false matches for darker-skinned people and children, who would then be wrongly stopped.
   - **Privacy** (c, d): everyone's face is filmed and stored for 30 days without being told, so innocent people are under surveillance.
   - **Transparency/accountability** (d, e): passengers are not informed and the vendor refuses to explain the model, so wrongful stops are hard to challenge, and it is unclear who is responsible: vendor, city or police.
   - **Jobs** (f): security guards may lose their jobs.
   - (Also acceptable: wrongful stops causing fear and loss of trust in police; data breach risk from stored images.)
5. **Evidence:** Gender Shades (2018) found commercial face-analysis systems had error rates up to 34.7% for darker-skinned women but at most 0.8% for lighter-skinned men, and that overall accuracy figures hid this gap because test sets were unbalanced. A "99% accuracy" claim from tests on mainly lighter-skinned adults tells us little about accuracy for everyone else.
6. **Calculation:** 0.1% of 60,000 = 60,000 × 0.001 = **60 false alerts per day**, so 60 innocent people stopped every day (about 420 a week), even with a seemingly tiny error rate. If errors are concentrated in one group, that group bears most of the stops. *(The 0.1% rate is made up for this activity.)*
7. **Safeguards** (any four): independent testing of accuracy **separately for different skin types, ages and genders** before use; clear signs informing passengers; delete non-matching images immediately instead of storing them for 30 days; a trained human must confirm every match before anyone is stopped; publish usage statistics and false-alert rates; a clear complaint and appeal process; vendor must allow independent audits (no "trade secret" refusal); limit the watch list to serious crimes; legal review. (In the EU, real-time remote biometric identification in public spaces for law enforcement is prohibited except in narrow, legally authorized cases; see [Topic 10](10-future-of-ai.md).)
8. **Judgment (example):** "Do not deploy as is. The system would film tens of thousands of innocent people daily without telling them, the accuracy claim is based on unrepresentative testing, and the vendor's refusal to explain the model makes errors impossible to challenge. Even a small error rate produces dozens of wrongful stops per day, likely concentrated on darker-skinned passengers. It should only be considered after independent group-by-group testing, a legal basis, public notice, immediate deletion of non-matches and human confirmation of every alert." (Other judgments, including "deploy with strict conditions", are acceptable if justified with the facts and evidence.)

</details>

## Optional extension

*Optional: not required for the core module.*

- Read the Gender Shades paper's abstract (link in Sources). Why did the authors build a new dataset instead of using existing ones?
- Find out how one AI chatbot you use handles your conversation data (look for "data controls" or "privacy" in its settings). Can you opt out of your chats being used for training?
- Search for "AI Incident Database" and read one reported incident. Classify it using the six issues from this topic.

## Connections

- **Back to [Topic 03](03-ml-neural-networks-deep-learning.md):** bias is learned the same way any pattern is learned, from features and labels in training data.
- **Back to [Topic 04](04-generative-ai-and-llms.md):** generative AI makes deepfakes possible and produces hallucinations.
- **Back to [Topic 07](07-real-world-applications.md):** the "risk" and "human oversight" rows of the framework are expanded here.
- **Forward to [Topic 09](09-limitations-and-misconceptions.md):** "AI is objective" and "AI will take all jobs" are examined as misconceptions.
- **Forward to [Topic 10](10-future-of-ai.md):** laws and principles (EU AI Act, OECD, UNESCO) are society's response to these risks.

## Sources

1. Buolamwini, J. & Gebru, T. (2018). Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification. *Proceedings of the 1st Conference on Fairness, Accountability and Transparency*, PMLR 81:77–91. https://proceedings.mlr.press/v81/buolamwini18a.html (fetched, accessed 2026-11-06). Supports: three commercial systems; IJB-A and Adience mostly lighter-skinned (79.6% and 86.2% per the paper; abstract summarized as ~80%/86%); new balanced dataset; error rates up to 34.7% (darker-skinned females) vs max 0.8% (lighter-skinned males).
2. MIT Media Lab. *Gender Shades* project overview. https://www.media.mit.edu/projects/gender-shades/overview/ (fetched, accessed 2026-11-06). Supports: 1,270 faces; parliamentarians from three African and three European countries. (Vendor names IBM, Microsoft, Face++ are from the paper's body; known stable reference.)
3. Dastin, J. (2018, 10 October). Amazon scraps secret AI recruiting tool that showed bias against women. Reuters. Syndicated copy: https://www.cnbc.com/2018/10/10/amazon-scraps-a-secret-ai-recruiting-tool-that-showed-bias-against-women.html (search result, accessed 2026-11-06). Supports: penalized "women's"; trained on ~10 years of mostly male resumes; Amazon said never used by recruiters to evaluate candidates.
4. Obermeyer, Z. et al. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science*, 366(6464), 447–453. Summary: https://chmi.berkeley.edu/news/dissecting-racial-bias-in-an-algorithm-used-to-manage-the-health-of-populations (fetched, accessed 2026-11-06). Supports: cost-as-proxy bias case.
5. Hunton Andrews Kurth (2024). *Dutch Regulator Fines Clearview AI 30.5 Million Euros*. https://www.hunton.com/privacy-and-cybersecurity-law-blog/dutch-regulator-fines-clearview-ai-30-5-million-euros ; JURIST (2024): https://www.jurist.org/news/2024/09/netherlands-data-protection-authority-fines-us-ai-company-30-5-million-euros-over-facial-recognition-database (search results, accessed 2026-11-06). Supports: €30.5M fine announced 3 Sept 2024; scraped database built without consent; GDPR.
6. World Economic Forum (2025, 8 January). *Future of Jobs Report 2025: 78 Million New Job Opportunities by 2030 but Urgent Upskilling Needed to Prepare Workforces* (press release). https://www.weforum.org/press/2025/01/future-of-jobs-report-2025-78-million-new-job-opportunities-by-2030-but-urgent-upskilling-needed-to-prepare-workforces/ (page returned 403 to automated fetch; figures verified via search results and multiple consistent reports, accessed 2026-11-06). Supports: 170M created, 92M displaced, net 78M (2025–2030); 22% churn; >1,000 employers, >14M workers, 55 economies; several macro-trends as drivers; ~two-fifths of skills changing.
7. *Mata v. Avianca, Inc.*, No. 1:22-cv-01461 (S.D.N.Y. 22 June 2023), opinion and order on sanctions. https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54 (403 to automated fetch); Reuters report (Merken, S., 22 June 2023) via syndicated copy and Bloomberg Law: https://news.bloomberglaw.com/financial-accounting/fake-chatgpt-cases-costs-lawyers-5-000-plus-embarrassment (search results, accessed 2026-11-06). Supports: six fictitious ChatGPT-generated citations; $5,000 total fine; bad faith finding.
8. International Energy Agency (2025, 10 April). *AI is set to drive surging electricity demand from data centres while offering the potential to transform how the energy sector works* (press release for *Energy and AI* report). https://www.iea.org/news/ai-is-set-to-drive-surging-electricity-demand-from-data-centres-while-offering-the-potential-to-transform-how-the-energy-sector-works (fetched, accessed 2026-11-06). Supports: ~945 TWh by 2030, slightly more than Japan's consumption; AI-optimized data center demand more than quadruples; emissions increase small and potentially offset.
9. CNN (2024, 16 May). *Arup revealed as victim of $25 million deepfake scam involving Hong Kong employee*. https://edition.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk ; South China Morning Post (2024): https://scmp.com/news/hong-kong/law-and-crime/article/3263151/uk-multinational-arup-confirmed-victim-hk200-million-deepfake-scam-used-digital-version-cfo-dupe (search results, accessed 2026-11-06). Supports: deepfake video call; 15 transfers totaling HK$200M (~US$25M); January 2024.
10. NTSB findings on the 2018 Uber crash as reported by CNN (2019): https://www.cnn.com/2019/11/19/tech/uber-crash-ntsb (search result, accessed 2026-11-06). Supports: shared responsibility (software, safety driver, company safety culture, regulators).
