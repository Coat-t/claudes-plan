# AI Overview: Slide Outlines (one deck per topic)

**Module:** AI Overview · **Version:** 1.0 · **Last updated:** 2026-11-06 · **Adapted from:** topic files Version 2.0 in [../../topics/](../../topics/)

**Back to:** [Formats README](../README.md) · [Module outline](../../00-module-outline.md)

## How to use these outlines

- Each deck covers one topic file and has 6 to 9 slides. The topic file is the **authoritative source**: every definition, number and example below is copied from it. If you find an error, fix the topic file first, then this file (see the [consistency rule](../README.md#the-consistency-rule)).
- Each slide lists: a **title**, 2 to 4 **key points** (short enough to fit on a slide), the **visual** (an existing module diagram, linked, or a simple visual described in words) and **speaker notes** (2 to 4 sentences, ending with the source section).
- Each deck has exactly **one interaction slide**, marked `[INTERACTION]`: a poll or prediction question for the audience. The answer and explanation are in the speaker notes. Give the audience 30 to 60 seconds before revealing.
- Numbers labeled *illustrative (made-up)* in the topic files must keep that label on the slide.
- **Accessibility:** put the diagram's alt text (from the topic file) in the slide's alt-text field; read out every number shown on a slide; do not rely on color alone (the diagrams also use labels); keep the speaker notes available as a handout.
- Diagram paths are relative to this file: `../../assets/images/<file>.svg`.

## Contents

1. [Deck 01: What is AI?](#deck-01-what-is-ai)
2. [Deck 02: How AI operates](#deck-02-how-ai-operates)
3. [Deck 03: Machine learning, neural networks and deep learning](#deck-03-machine-learning-neural-networks-and-deep-learning)
4. [Deck 04: Generative AI and large language models](#deck-04-generative-ai-and-large-language-models)
5. [Deck 05: Types of AI](#deck-05-types-of-ai)
6. [Deck 06: The history and evolution of AI](#deck-06-the-history-and-evolution-of-ai)
7. [Deck 07: Real-world applications of AI](#deck-07-real-world-applications-of-ai)
8. [Deck 08: Ethics, risks and social impact of AI](#deck-08-ethics-risks-and-social-impact-of-ai)
9. [Deck 09: Limitations and common misconceptions](#deck-09-limitations-and-common-misconceptions)
10. [Deck 10: The future of AI](#deck-10-the-future-of-ai)

---

## Deck 01: What is AI?

**Source:** [Topic 01: What is AI?](../../topics/01-what-is-ai.md) · **Slides:** 9 · **Suggested time:** 20 minutes

### Slide 1.1: What is AI?

- Topic 1 of 10 in the AI Overview module.
- Goals: define AI with inputs and outputs; tell AI from ordinary software; explain the "AI effect".
- No programming or maths needed.

**Visual:** Simple described visual: a row of everyday icons (email envelope, map pin, phone with face outline, chat bubble) with a question mark above them: "Which of these use AI?"

**Speaker notes:** Introduce the module and ask the audience to keep the question on the slide in mind; we answer it with a test on slide 1.5. The learning goals are listed at the top of the topic file. Source: [Topic 01, Learning goals](../../topics/01-what-is-ai.md).

### Slide 1.2: A working definition

- **AI** is computer technology that performs tasks we would normally say need human intelligence: recognizing patterns, understanding language, making decisions or creating content.
- "Simulate" or "perform tasks" means the results *look* intelligent; it does not mean the computer thinks or feels.
- Today's AI is built for particular **tasks**.

**Visual:** The module definition in large text, with the words "tasks" and "need human intelligence" highlighted.

**Speaker notes:** There is no single definition every expert agrees on. IBM describes AI as technology that enables computers to "simulate human learning, comprehension, problem solving, decision making, creativity and autonomy"; the module uses the shorter version on the slide. Stress that a face-recognition system cannot, on its own, write a poem or drive a car. Source: [Topic 01, Explanation section 1](../../topics/01-what-is-ai.md).

### Slide 1.3: Inputs, inference, outputs

- OECD (updated late 2023): an AI system **infers from the input it receives how to generate outputs** such as predictions, content, recommendations or decisions.
- To **infer** = to work something out from evidence. A calculator does not infer; it applies one fixed procedure.
- Output types: prediction, classification, recommendation, decision, generated content.

**Visual:** Described chain diagram: `INPUT --> [ AI system: infers / works out an answer ] --> OUTPUT --> effect on the world`, with one example row underneath: "A new email --> spam filter --> 'Spam' --> email goes to the spam folder".

**Speaker notes:** The OECD is a group of 38 member countries; its definition is precise enough for laws, and it adds that AI systems differ in autonomy and in whether they keep adapting after deployment. Walk through the spam-filter row, then ask for another example (navigation app, predictive text, chatbot). These five output words come back in every later topic. Source: [Topic 01, Explanation section 2](../../topics/01-what-is-ai.md).

### Slide 1.4: Human intelligence vs today's AI

- **Breadth:** a person does many things in one day; each AI system usually does one task or a narrow family of tasks.
- **Learning:** people can learn from a few examples; most AI needs thousands to billions.
- **Feelings and awareness:** no accepted evidence that any current AI has them.
- **Speed and scale:** AI is extremely fast and does not tire.

**Visual:** Two-column comparison table, "Human intelligence" vs "Today's AI systems", with the four rows above.

**Speaker notes:** "Artificial intelligence" names the behavior (doing tasks that would need intelligence if a person did them), not a claim that the machine has a mind. Russell and Norvig's textbook frames AI around agents that perceive their environment and act to achieve goals, which is the same practical view. Whether AI "understands" anything is debated; Topic 09 returns to this. Source: [Topic 01, Explanation section 3](../../topics/01-what-is-ai.md).

### Slide 1.5: Is it AI? The three-question test

1. What is the input and what is the output?
2. Does the system **infer** a good output for new, varied inputs, or apply one fixed procedure written in advance?
3. Could a person write an **exact recipe for every possible input**? If yes, it is probably ordinary software.

**Visual:** Small table: Calculator app = No (fixed arithmetic rules) · Alarm clock at 07:00 = No (one fixed rule) · Photo app finding "all photos of my dog" = Yes (must recognize a dog in new photos) · Dictionary-lookup spell checker = Borderline / usually no.

**Speaker notes:** Borderline cases are normal because the boundary of "AI" is fuzzy. A modern spell checker that suggests the most likely intended word from context does use AI; a plain dictionary lookup does not. Ask the audience to apply the three questions on the next slide. Source: [Topic 01, Explanation section 4](../../topics/01-what-is-ai.md).

### Slide 1.6: [INTERACTION] Poll: AI or not?

- Which of these are AI? Vote for each: (A) a microwave that switches off when its timer reaches zero; (B) a banking app alert "Unusual payment detected - was this you?"; (C) a website form that rejects an email address with no "@"; (D) a phone keyboard that suggests the next word.

**Visual:** Four cards labeled A to D, each with a thumbs-up / thumbs-down voting area.

**Speaker notes:** **Answer:** B (usually) and D are AI; A and C are not. A and C each follow one exact rule that a person can write down completely. D infers likely continuations from patterns in large amounts of text; B usually uses a system that learns what "normal" spending looks like for each customer (if the bank used only one fixed rule such as "alert on any payment over 1,000", that part would not be AI). Source: [Topic 01, Activity 1 and Answers](../../topics/01-what-is-ai.md).

### Slide 1.7: Worked example: the self-checkout camera

- **Input:** camera image of what is on the scale, plus its weight.
- **Output:** "Bananas (loose)": a **classification** (a top-3 list would be a ranked recommendation).
- **Infers?** Yes: green or yellow, bagged or loose, any angle, any light; no exact rule is possible.
- **Effect:** item and price added to the bill **after the customer confirms**.

**Visual:** Described simple visual: a self-checkout screen showing a photo of bananas and the prompt "Bananas (loose)? Confirm", with the four chain labels (Input, Infers, Output, Effect) pointing at it.

**Speaker notes:** Asking the customer to confirm is sensible for a system that will sometimes be wrong. A child can recognize a banana after seeing a few; the checkout system needed many example images and cannot do anything else, such as judge ripeness. Conclusion: it is an AI system built for one specific task. Source: [Topic 01, Worked example](../../topics/01-what-is-ai.md).

### Slide 1.8: The "AI effect"

- Once something works reliably, people often stop calling it AI.
- "Tesler's Theorem", recorded by Douglas Hofstadter (1979): "AI is whatever hasn't been done yet."
- Former headline AI: route-finding in maps, beating a chess champion, reading handwritten postal codes.
- Judge by input → output, not by the label "AI-powered".

**Visual:** Described simple visual: three icons (map route, chess piece, envelope with postcode) moving from a box labeled "AI!" to a box labeled "just a program".

**Speaker notes:** A similar remark is often attributed to John McCarthy, but researchers who traced it found that attribution is second-hand and appeared only in 2011; the earliest verified version of the idea dates from 1971. The techniques in these examples are still AI; they just stopped feeling magical. Source: [Topic 01, Explanation section 5](../../topics/01-what-is-ai.md).

### Slide 1.9: A map of the terms ahead

- **Machine learning (ML):** learns patterns from data (Topics 02, 03).
- **Deep learning:** ML with large, many-layered neural networks (Topic 03).
- **Generative AI:** creates new content; almost all of today's prominent generative AI uses deep learning (Topic 04).
- Not all AI is ML: some AI follows expert rules or searches (Topic 02).

**Visual:** [Nested circles: AI ⊃ machine learning ⊃ deep learning ⊃ generative AI](../../assets/images/ai-ml-dl-genai-nested.svg)

**Speaker notes:** Read the diagram from the outside in: each inner circle is one part of the circle around it. Point out the footnote: the innermost circle is a simplification, because some older generative methods (such as Markov-chain text generators) did not use deep learning. Next topic: how the AI system in the middle of the chain actually works out its answer. Source: [Topic 01, Explanation section 6 and Visual](../../topics/01-what-is-ai.md).

---

## Deck 02: How AI operates

**Source:** [Topic 02: How AI operates](../../topics/02-how-ai-operates.md) · **Slides:** 9 · **Suggested time:** 25 minutes

### Slide 2.1: How AI operates

- Every AI system has three ingredients: **data**, **algorithms**, **models**.
- Two ways to build the model: write the knowledge in by hand (**rule-based AI**) or learn it from examples (**machine learning**).
- Today: rules, search, a spam filter you can train by hand.

**Visual:** Described simple visual: an open box labeled "AI system" between "Input" and "Output" arrows, with a question mark inside: "What happens in here?"

**Speaker notes:** Topic 01 looked at AI from the outside; this deck opens the box. Both approaches are AI and both are still used today. Source: [Topic 02, Learning goals and Explanation section 1](../../topics/02-how-ai-operates.md).

### Slide 2.2: Data, algorithms and models

- **Data:** the raw material (emails, face images, maps and traffic reports).
- **Algorithm:** a precise recipe of steps; in AI, either *reasoning/searching* with written knowledge or *learning* patterns from data.
- **Model:** the finished "decision-maker" that maps input to output; in ML it is created by training and holds **parameters (weights)**.

**Visual:** Three labeled boxes in a row: "Data (ingredients)" → "Learning algorithm (recipe for practicing)" → "Model (the trained cook)".

**Speaker notes:** The kitchen comparison: data is the ingredients, the learning algorithm is the recipe for practicing, and the model is the trained cook who can make the dish without the recipe book open. Point out that the analogy is imperfect: a model does not "know" it is cooking. In rule-based AI the model is the set of rules people wrote. Source: [Topic 02, Explanation section 1](../../topics/02-how-ai-operates.md).

### Slide 2.3: Rule-based (symbolic) AI: expert systems

- Knowledge written down as human-readable **IF-THEN rules**.
- **MYCIN** (Stanford, early 1970s): roughly 600 rules to help identify bacterial blood infections and choose antibiotics.
- Strength: can explain itself by showing which rules fired.
- Weaknesses: every rule written by hand; fails when no rule covers the case.

**Visual:** Described simple visual: a rule card reading "IF the organism is gram-negative AND rod-shaped AND anaerobic THEN there is suggestive evidence that it is *Bacteroides*".

**Speaker notes:** Symbolic AI dominated research from the 1950s to the 1980s. MYCIN was tested on real cases but was not put into routine clinical use. Source: [Topic 02, Explanation section 2](../../topics/02-how-ai-operates.md).

### Slide 2.4: Rule-based AI: search

- Describe the problem: **start state**, **actions**, **rules** (allowed states), **goal state**.
- **Breadth-first search** checks every state 1 move away, then 2 moves, and so on, so the first solution found uses the fewest moves.
- Farmer, wolf, goat, cabbage: 16 arrangements, only **10 safe**, minimum **7 crossings**, exactly **2** shortest solutions.
- The computer **learned nothing**: people described the problem; the algorithm searched.

**Visual:** [State graph of the farmer, wolf, goat and cabbage puzzle with the 7-crossing solution paths](../../assets/images/river-crossing-state-graph.svg)

**Speaker notes:** State notation is `left bank | right bank` with F, W, G, C; start `FWGC | -`, goal `- | FWGC`. The boat holds the farmer plus at most one item, and W must never be left with G, nor G with C, without F. The facts on the slide were checked with a short breadth-first search program written for the module. Source: [Topic 02, Explanation section 2, mini-trace](../../topics/02-how-ai-operates.md).

### Slide 2.5: [INTERACTION] Predict the first move

- Start: `FWGC | -`. The farmer has four options for the first crossing: alone, with the wolf, with the goat, or with the cabbage.
- **Which option is the only safe one? Why do the other three fail?**

**Visual:** Four option cards showing the resulting states: alone `WGC | F` · with W `GC | FW` · with G `WC | FG` · with C `WG | FC`.

**Speaker notes:** **Answer:** only "with the goat" (`WC | FG`) is safe. Alone leaves wolf with goat (wolf eats goat); with the wolf leaves goat with cabbage (goat eats cabbage); with the cabbage leaves wolf with goat. This is exactly what the search does at every step: try each option, reject unsafe states, skip states already seen. Source: [Topic 02, trace table move 1](../../topics/02-how-ai-operates.md).

### Slide 2.6: Machine learning turns the problem around

- **Traditional programming:** rules + data → answers.
- **Machine learning:** data + answers (labeled examples) → rules, in the form of a **model**.
- Gmail: about a decade of rule-based filtering, then machine-learning-generated rules from 2014.

**Visual:** [Traditional programming vs machine learning](../../assets/images/rules-vs-learning.svg)

**Speaker notes:** Writing exact rules for faces, speech or every spam email is hopeless, and spammers change tricks every week ("FR3E M0NEY!!"). Google said machine learning "finds new patterns and adapts far quicker than previous manual systems", and today Gmail uses "machine learning powered by user feedback". Source: [Topic 02, Explanation section 3](../../topics/02-how-ai-operates.md).

### Slide 2.7: Training vs inference

- **Training:** a learning algorithm adjusts the model's **parameters (weights)** so its outputs match the **labels** in the training data.
- **Inference (prediction):** the trained model gets a *new* input and produces an output, often millions of times a day.
- A **test set** is kept aside to check the model on data it never saw.

**Visual:** [The machine learning pipeline: training phase and inference phase](../../assets/images/ml-pipeline.svg)

**Speaker notes:** Training happens before use and is repeated now and then with fresh data; using the model does not normally change it. Each training example has **features** (measurable properties of the input) and a **label** (the correct answer). Source: [Topic 02, Explanation section 3 and Common mistake 2](../../topics/02-how-ai-operates.md).

### Slide 2.8: Worked example: training a spam filter

- *Illustrative (made-up) figures.* 10,000 training emails (4,000 spam, 6,000 not) + 2,000 test emails.
- Learned weights: "free" **+2**, "urgent" **+2**, "meeting" **-2**, "invoice" **0**, 3+ links **+1**. Threshold: score **2 or more** = spam.
- "Free pizza at the team meeting today!" (no links): +2 - 2 = **0** → not spam.
- Test: 720 of 800 spam caught, 60 of 1,200 genuine emails wrongly flagged → 1,860 / 2,000 = **93% accuracy**.

**Visual:** Weight table (feature, % of spam, % of not-spam, weight) with the "Free pizza" email scored underneath.

**Speaker notes:** "Free" is in 60% of spam but 5% of not-spam (12 times more common in spam), so it gets +2; "meeting" is 15 times more common in not-spam, so it gets -2. No person wrote "meeting emails are usually genuine"; the weights came from the data. The 80 missed spam emails are false negatives and the 60 genuine emails sent to spam are false positives. Source: [Topic 02, Worked example steps 1 to 5](../../topics/02-how-ai-operates.md).

### Slide 2.9: Comparing the two approaches

- Rule-based: knowledge from people; easy to explain; fails when no rule covers the case; best for clear, stable rules (tax, eligibility, puzzles, route search).
- Machine learning: knowledge from data; often harder to explain; handles cases like its training data; best for messy patterns (images, speech, spam, language).
- "Old" vs "new" is only a rough guide: AlphaGo (2016) "combines deep neural networks with advanced search algorithms".
- 93% accuracy still meant **140 mistakes** in 2,000 test emails.

**Visual:** Condensed two-column comparison table from the topic file.

**Speaker notes:** Rule-based reasoning and search are still widely used, often combined with machine learning. Which mistakes a model makes, and who they affect, matters as much as the overall percentage: a genuine job offer lost in the spam folder may be worse than one extra spam email. Source: [Topic 02, Explanation section 4 and Common mistakes 3 and 4](../../topics/02-how-ai-operates.md).

---

## Deck 03: Machine learning, neural networks and deep learning

**Source:** [Topic 03: ML, neural networks and deep learning](../../topics/03-ml-neural-networks-deep-learning.md) · **Slides:** 9 · **Suggested time:** 25 minutes

### Slide 3.1: Machine learning, neural networks and deep learning

- Three ways a machine can learn.
- Why we test on data the model never saw (overfitting).
- One artificial neuron, by hand; layers; what makes learning "deep".

**Visual:** [Nested circles](../../assets/images/ai-ml-dl-genai-nested.svg), with the "Machine learning" and "Deep learning" rings highlighted.

**Speaker notes:** Google's course defines ML as "the process of training a piece of software, called a model, to make useful predictions". This deck zooms into the two middle circles of the Topic 01 map. Source: [Topic 03, Explanation section 1](../../topics/03-ml-neural-networks-deep-learning.md).

### Slide 3.2: Three ways to learn

- **Supervised:** examples **with labels** → classification (a category) or regression (a number). Example: spam filter.
- **Unsupervised:** examples **without labels** → finds structure, e.g. clustering customers by buying habits.
- **Reinforcement:** an **agent** acts in an **environment** and gets **rewards or penalties**, often delayed. Example: a game-playing program.

**Visual:** Three-column table: training data / feedback / typical tasks / example, as in the topic file.

**Speaker notes:** Supervised learning is the most widely used kind, but labels can be expensive and label mistakes become model mistakes. "Unsupervised" does not mean "no humans involved": people choose the data and interpret the groups. In reinforcement learning nobody tells the agent the correct move at each step. Source: [Topic 03, Explanation section 2](../../topics/03-ml-neural-networks-deep-learning.md).

### Slide 3.3: [INTERACTION] Which kind of learning?

- Vote supervised, unsupervised or reinforcement for each:
- (A) A simulated robot dog gets +1 point per meter walked and -10 when it falls; after thousands of tries it walks smoothly.
- (B) A music service groups millions of listeners into "taste communities" without being given any names in advance.
- (C) A model predicts house prices, trained on 20,000 past sales with their final prices.

**Visual:** Three scenario cards with three voting buttons each.

**Speaker notes:** **Answers:** A = reinforcement (trial and error with rewards and penalties); B = unsupervised (no labels; clustering); C = supervised, specifically regression (each example has a label, the final price, and the output is a number). Ask voters to name the clue that decided it. Source: [Topic 03, Activity 1 items 3, 2 and 1, and Answers](../../topics/03-ml-neural-networks-deep-learning.md).

### Slide 3.4: Features, labels and the train/test split

- A dataset is a table: rows = **examples**, columns = **features**, one column = the **label**.
- **Training set:** what the model learns from. **Test set:** kept aside, used only at the end.
- The test set is like a new exam: it shows whether the model **generalizes**.

**Visual:** Fruit table excerpt (illustrative, made-up): weight (g), skin, color → label (apple / orange), with a line separating 8 training rows from 4 test rows.

**Speaker notes:** A model could ace its training data by memorizing it, like a student who memorized last year's exam answers. Google's course recommends shuffling before splitting and gives an example split of 70% training, 15% validation and 15% test; the module keeps it simple with training and test sets only. Source: [Topic 03, Explanation section 3](../../topics/03-ml-neural-networks-deep-learning.md).

### Slide 3.5: Overfitting: memorizing instead of learning

- *Illustrative (made-up) fruit data.* Model A (skin rule): training 8/8, test **4/4** → generalizes.
- Model B (memorizer): training 8/8, test **2/4** → **overfitting**.
- Model C (weight > 165 g): training 7/8, test 2/4 → **underfitting / weak feature**.
- Tell-tale sign of overfitting: excellent on training data, much worse on the test set.

**Visual:** Three-row results table: model / training score / test score / diagnosis.

**Speaker notes:** Judged only on training data, Model B would look as good as Model A; only the test set reveals the difference. Google compares an overfit model to "an invention that performs well in the lab but is worthless in the real world". Ways to reduce overfitting: more and more varied data, simpler models when they work about as well, and always judging on unseen data. Source: [Topic 03, Explanation section 4 and Worked example Part A](../../topics/03-ml-neural-networks-deep-learning.md).

### Slide 3.6: The artificial neuron

- 1. **Multiply** each input by its **weight** (positive pushes toward "yes", negative toward "no").
- 2. **Add** the results plus a **bias** (shifts how easily it "fires").
- 3. Apply an **activation function**: step (1 if sum > 0, else 0), sigmoid (0 to 1) or ReLU (0 for negatives, otherwise the sum).

**Visual:** [An artificial neuron with a worked numeric example](../../assets/images/artificial-neuron.svg)

**Speaker notes:** The idea goes back to Frank Rosenblatt's perceptron, published in 1958. Despite the name, an artificial neuron is just a small calculation, only loosely inspired by brain cells. "Bias" here is a number in the calculation, not unfair bias (that is Topic 08). Source: [Topic 03, Explanation section 5](../../topics/03-ml-neural-networks-deep-learning.md).

### Slide 3.7: One neuron, by hand

- *Illustrative (made-up) numbers.* Inputs: "free" x1 = 1, sender in contacts x2 = 0, 3+ links x3 = 1. Weights 0.6, -0.4, 0.3. Bias -0.5.
- 1 × 0.6 + 0 × (-0.4) + 1 × 0.3 + (-0.5) = **0.4** → greater than 0 → output **1 (spam)**.
- If the sender *is* a contact (x2 = 1): sum = **0.0** → not greater than 0 → output **0 (not spam)**.
- Same sum 0.4 with sigmoid ≈ **0.60**; with ReLU = **0.4**.

**Visual:** [Artificial neuron diagram](../../assets/images/artificial-neuron.svg) with the three calculation steps revealed one at a time.

**Speaker notes:** Pause after the first line and let the audience compute the sum before you reveal it. The negative weight on "sender in contacts" pulls the decision back exactly to the boundary. The weights are not chosen by a person: training starts with rough weights and nudges them, example after example, to reduce mistakes. Source: [Topic 03, Worked example Part B](../../topics/03-ml-neural-networks-deep-learning.md).

### Slide 3.8: Layers

- **Input layer:** receives the features. **Hidden layers:** in the middle. **Output layer:** gives the result.
- Each layer builds on the last: edges and color patches → shapes and parts → whole objects (**hierarchical features**).
- Nobody programs these intermediate patterns; they emerge during training.

**Visual:** [Layers of a small neural network: 3 inputs, two hidden layers of 4, 2 outputs](../../assets/images/neural-network-layers.svg)

**Speaker notes:** Hidden layers are "hidden" because we never see their outputs directly. The activation function matters: without it, stacking layers adds no power, because "linear operations performed on linear operations are still linear". Source: [Topic 03, Explanation section 6](../../topics/03-ml-neural-networks-deep-learning.md).

### Slide 3.9: What makes learning "deep"?

- **Deep learning** = machine learning with many-layered neural networks; "deep" means **many layers**, not deep understanding.
- Module rule of thumb: **more than one hidden layer** (IBM: "at least 4 layers", counting input and output).
- Deep networks learn their own features, need lots of data and GPUs, and are hard to explain ("black boxes").

**Visual:** [Neural network layers diagram](../../assets/images/neural-network-layers.svg) with the caption "2 hidden layers = deep (module rule of thumb)".

**Speaker notes:** The spam filter in Topic 02 needed hand-designed features; a deep network given raw pixels or text can discover features itself. Not all ML is deep (the Topic 02 spam filter had no neural network) and not all AI is ML (the river-crossing search learned nothing). The black-box problem returns in Topic 08 (accountability). Source: [Topic 03, Explanation section 7 and Common mistakes 1 and 2](../../topics/03-ml-neural-networks-deep-learning.md).

---

## Deck 04: Generative AI and large language models

**Source:** [Topic 04: Generative AI and LLMs](../../topics/04-generative-ai-and-llms.md) · **Slides:** 9 · **Suggested time:** 25 minutes

### Slide 4.1: Generative AI and large language models

- What makes AI "generative"?
- How a chatbot writes: **tokens** and **next-token prediction**.
- Why the same prompt gives different answers, and why fluent text can be false.

**Visual:** Described simple visual: a chat window with the prompt "Write a polite email asking to move our meeting to Friday" and a reply being typed word by word.

**Speaker notes:** This deck uses ideas from Topics 02 and 03: model, training, inference, labels, neural networks and deep learning. Source: [Topic 04, Learning goals and Prerequisites](../../topics/04-generative-ai-and-llms.md).

### Slide 4.2: Generative vs discriminative

- **Discriminative (predictive):** sorts or scores an input → a label, score or number (spam filter, face unlock, fraud alert).
- **Generative:** creates new content → text, images, audio, video or code (chatbot email, image generator, AI voice).
- A **prompt** is the request you give a generative system.

**Visual:** Two-column table: "Which category is this?" vs "What new content fits this request?"

**Speaker notes:** Google's course: "Discriminative models discriminate between different kinds of data instances" while "Generative models can generate new data instances". IBM defines generative AI as AI "that can create original content such as text, images, video, audio or software code in response to a user's prompt". Source: [Topic 04, Explanation section 1](../../topics/04-generative-ai-and-llms.md).

### Slide 4.3: Is all generative AI deep learning?

- **Almost all of today's prominent generative AI systems use deep learning** (LLM chatbots, modern image generators).
- But that is a simplification: **Markov-chain text generators** (Claude Shannon, 1948) choose each next word from simple counts, with no neural network.
- ELIZA (mid-1960s) produced text with hand-written pattern-matching rules.

**Visual:** [Nested circles](../../assets/images/ai-ml-dl-genai-nested.svg), zoomed on the footnote "Simplification: ... some older generative methods did not."

**Speaker notes:** Shannon's 1948 sample was English-like text in which "the word transition probabilities are correct but no further structure is included"; it looked like English in short stretches but made no overall sense. Learners run a tiny Markov-chain generator by hand in the topic's Activity 1. Source: [Topic 04, Explanation section 2](../../topics/04-generative-ai-and-llms.md).

### Slide 4.4: What is a large language model?

- A **language model** gives probabilities for what text comes next.
- An **LLM** is a deep neural network, almost always a **transformer** (Vaswani et al., 2017, "Attention Is All You Need").
- "Large" twice over: huge numbers of parameters and huge amounts of training text. GPT-3 (2020): **175 billion** parameters vs **5** weights in our spam filter.

**Visual:** Described simple visual: two labels side by side, "Spam filter (Topic 02): 5 weights" and "GPT-3 (2020): 175,000,000,000 parameters".

**Speaker notes:** A transformer's key trick, attention, lets the model weigh up all the earlier words, near and far, when predicting the next one; learners do not need the details. Source: [Topic 04, Explanation section 3](../../topics/04-generative-ai-and-llms.md).

### Slide 4.5: Tokens: how an LLM sees text

- A **token** = a whole word, part of a word, a punctuation mark or a single character.
- Rule of thumb for English: 1 token ≈ three-quarters of a word; **100 tokens ≈ 75 words**.
- Example (illustrative; real splits differ): "Unbelievably, the cat sat." → `[Un] [believ] [ably] [,] [ the] [ cat] [ sat] [.]` = 8 tokens.

**Visual:** The example sentence with each token in its own colored, labeled box.

**Speaker notes:** Each token is turned into numbers, because a neural network can only compute with numbers. Tokens are not the same as words. Source: [Topic 04, Explanation section 4 and Common mistake 4](../../topics/04-generative-ai-and-llms.md).

### Slide 4.6: Next-token prediction: the loop

1. **Input:** all the text so far.
2. **Predict:** a probability for every token in the vocabulary.
3. **Choose** one token (usually a likely one).
4. **Append** it to the text.
5. **Repeat** until an "end" token or a length limit.

**Visual:** [Next-token prediction: "The cat sat on the" → mat 0.41, floor 0.17, sofa 0.12, roof 0.06, all other tokens 0.24](../../assets/images/next-token-prediction.svg)

**Speaker notes:** A 300-word answer is built from roughly 400 of these steps. The model does not plan the whole answer and does not look it up in a database, which explains both its fluency and its confident mistakes. The context window limits how many tokens of earlier text it can take into account. The probabilities on the diagram are illustrative (made-up). Source: [Topic 04, Explanation section 5](../../topics/04-generative-ai-and-llms.md).

### Slide 4.7: [INTERACTION] Spin the next token

- Spinner slices (illustrative, made-up): mat 0.00 up to 0.41 · floor 0.41 up to 0.58 · sofa 0.58 up to 0.70 · roof 0.70 up to 0.76 · all other tokens 0.76 up to 1.00.
- **The computer draws the random number 0.63. Which token is chosen?**
- Bonus: in 100 runs, about how often would "mat" be chosen?

**Visual:** A spinner (pie) with five labeled slices sized by probability, and a pointer stopped at 0.63.

**Speaker notes:** **Answer:** **sofa**, because 0.63 lies in 0.58 up to 0.70. Bonus: about **41** times in 100 (probability 0.41), though one batch of 100 runs would be close to, not exactly, 41. This is sampling: random choice weighted by probability, which is why the same prompt can give different answers. Source: [Topic 04, Worked example step 2b](../../topics/04-generative-ai-and-llms.md).

### Slide 4.8: How an LLM is trained

- **1. Pre-training:** predict the next token on enormous amounts of text; the real next token is the label (**self-supervised**).
- **2. Fine-tuning:** supervised learning on prompts paired with good responses.
- **3. RLHF:** people rank answers; reinforcement learning makes preferred answers more likely.
- After training, every conversation is **inference**: the weights stay fixed.

**Visual:** Three-stage arrow: "Huge text → Pre-trained model → Fine-tuned model → RLHF → Assistant".

**Speaker notes:** A pre-trained model predicts text well but is not yet a helpful assistant; asked a question, it might continue with more questions. In OpenAI's 2022 InstructGPT study, people preferred a 1.3-billion-parameter model trained with human feedback over the original 175-billion-parameter GPT-3. Source: [Topic 04, Explanation section 6](../../topics/04-generative-ai-and-llms.md).

### Slide 4.9: Temperature and hallucinations

- **Low temperature:** sharper probabilities, predictable text (e.g. mat 0.80). **High:** flatter, more varied (mat 0.26; all other tokens 0.32). *Illustrative (made-up).*
- Outputs also vary with model updates, context and hidden settings: an answer is **one sample**, not *the* correct output.
- **Hallucination:** output that sounds plausible but is false or made up.

**Visual:** Temperature table from the worked example (low / normal / high columns for mat, floor, sofa, roof, others).

**Speaker notes:** Low temperature suits factual summaries or code; high temperature suits brainstorming. IBM's well-known hallucination example is a lawyer who submitted made-up case citations produced by a generative AI tool. Human feedback and connecting to trusted sources reduce hallucinations but do not eliminate them (Topic 09). Source: [Topic 04, Explanation sections 7 and 8, Worked example step 4](../../topics/04-generative-ai-and-llms.md).

---

## Deck 05: Types of AI

**Source:** [Topic 05: Types of AI](../../topics/05-types-of-ai.md) · **Slides:** 8 · **Suggested time:** 20 minutes

### Slide 5.1: Types of AI: two lenses, not one ladder

- Online "types of AI" lists mix **two different classifications**.
- **Lens 1, capability:** how broad and powerful is it?
- **Lens 2, functionality:** how does it use memory, and does it understand others or itself?
- Every system gets **one label from each lens**.

**Visual:** [Types of AI seen through two different lenses](../../assets/images/types-of-ai-two-lenses.svg)

**Speaker notes:** Use the vehicle analogy: you can sort vehicles by size (small, medium, large) or by fuel (gasoline, diesel, electric); a small car can be electric. IBM's explainer presents the two schemes separately and places ChatGPT under narrow AI in one and limited memory in the other. When reading the diagram, note that "memory" in Lens 2 means using the recent past while operating, not training data (slide 5.3). Source: [Topic 05, Explanation section 1](../../topics/05-types-of-ai.md).

### Slide 5.2: Lens 1: by capability

- **Narrow AI (ANI):** one task or a limited range; "the only type of AI that exists today" (IBM).
- **General AI (AGI):** hypothetical; would "match or exceed the cognitive abilities of human beings across any task" (IBM); no expert consensus on a definition.
- **Superintelligence (ASI):** speculative; "greatly exceeds the cognitive performance of humans in virtually all domains of interest" (Bostrom, 2014).

**Visual:** Three stacked boxes: Narrow (exists today) / General (hypothetical) / Superintelligence (speculative), with a line marking "today's AI ends here".

**Speaker notes:** A chess program is superhuman at chess but not superintelligent, because "virtually all" matters. On chatbots: they are much broader than older narrow AI, but the mainstream view (IBM: "current LLMs are not considered AGI") is that they are not AGI; this is debated and there is no agreed test. The module uses "narrow/general" rather than "weak/strong" because those words are used inconsistently. Source: [Topic 05, Explanation section 2](../../topics/05-types-of-ai.md).

### Slide 5.3: Lens 2: by functionality

- **Reactive machines:** no memory of earlier moments (Deep Blue, 1997).
- **Limited memory:** uses the recent past while working (self-driving car tracking nearby cars; chatbot using the conversation in its context window).
- **Theory of mind** and **self-aware AI:** hypothetical.
- "Memory" here means the **recent past while operating**, *not* training data.

**Visual:** Four boxes left to right, the first two marked "exists today", the last two "hypothetical".

**Speaker notes:** This scheme became popular through Arend Hintze's 2016 article in *The Conversation*; it is a popular-press taxonomy, not a formal scientific standard, and its boundaries are fuzzy. IBM notes "to date, Emotion AI is unable to understand and respond to human feelings"; a chatbot writing "I understand how you feel" is producing likely text, not modeling your mind. Source: [Topic 05, Explanation section 3](../../topics/05-types-of-ai.md).

### Slide 5.4: Putting the lenses together

- Only **two cells** of the grid contain real systems: **narrow + reactive** and **narrow + limited memory**.
- All AI that exists today is narrow, working as reactive or limited-memory systems.
- The lenses do not line up neatly: it is not agreed whether AGI would need theory of mind or self-awareness.

**Visual:** 3 × 4 grid (rows: Narrow, General, Super; columns: Reactive, Limited memory, Theory of mind, Self-aware). Narrow/Reactive: Deep Blue, spam filter, face unlock. Narrow/Limited memory: self-driving car perception, LLM chatbots, voice assistants. All other cells: "(nothing built)", "(hypothetical)" or "(speculative)".

**Speaker notes:** Because the lenses ask different questions, you cannot automatically convert "general" into a functionality type or the other way round. Source: [Topic 05, Explanation section 4](../../topics/05-types-of-ai.md).

### Slide 5.5: [INTERACTION] Poll: does a spam filter have "memory"?

- A spam filter was **trained on millions of old emails**. It judges each new email on its own features as it arrives.
- **Under Lens 2, is it (A) reactive, (B) limited memory, or (C) theory of mind?**

**Visual:** Three voting buttons A, B, C beside an envelope icon.

**Speaker notes:** **Answer: (A) reactive** (this is the module's own classification; no source classifies spam filters). Training on past data is not "memory" in this scheme; memory means using the recent past while operating. Many people pick B, which is Common mistake 3 in the topic file. Capability label: narrow. Source: [Topic 05, Worked example row 2 and Common mistake 3](../../topics/05-types-of-ai.md).

### Slide 5.6: Worked example: six systems, two lenses

- Deep Blue: narrow / reactive. Self-driving car: narrow / limited memory.
- LLM chatbot: narrow (mainstream view; debated) / limited memory. Voice assistant: narrow / limited memory.
- Spam filter: narrow / reactive (our classification).
- Netflix recommender: narrow / **disputed** (IBM: reactive; a reasonable argument for limited memory).

**Visual:** Six-row table: system / Lens 1 / why / Lens 2 / why.

**Speaker notes:** Ask the capability question first (how broad?), then the functionality question (does it use the recent past while operating? does it model minds?). The Netflix row shows why the functionality scheme is a popular taxonomy, not a standard: sources disagree, so **state your reason**; the reason matters more than the label. Source: [Topic 05, Worked example](../../topics/05-types-of-ai.md).

### Slide 5.7: Common mistakes

- Mixing the lenses into one ladder ("narrow, general, reactive, ...").
- "ChatGPT can talk about anything, so it is general AI."
- "Trained on past data, so it is limited memory."
- "Chatbots talk about feelings, so theory of mind exists."

**Visual:** Four "myth" cards, each flipping to a one-line correction.

**Speaker notes:** Corrections: keep the lenses separate; breadth of conversation is not human-level ability across any task; memory means the recent past while operating; talking about feelings is generating likely text, not evidence of understanding minds or of consciousness. Source: [Topic 05, Common mistakes](../../topics/05-types-of-ai.md).

### Slide 5.8: Why the two lenses matter

- Headlines say "AI that thinks like a human" or "the first general AI".
- Ask: *Which task is it narrow at? Does it use the recent past? Any evidence it understands people, or is it producing likely text?*
- Avoid both hype ("it's basically a person") and dismissal ("it's just autocomplete").

**Visual:** Described simple visual: a newspaper headline "New AI understands your emotions!" with the three questions as sticky notes around it.

**Speaker notes:** Software that labels a face photo "happy", "sad" or "angry" is narrow and reactive, and labeling an expression is not understanding feelings; a more accurate headline would be "New AI labels facial expressions in photos". Topic 09 tackles "AI is conscious"; Topic 10 returns to AGI. Source: [Topic 05, Explanation section 5 and Activity 3 answers](../../topics/05-types-of-ai.md).

---

## Deck 06: The history and evolution of AI

**Source:** [Topic 06: History of AI](../../topics/06-history-of-ai.md) · **Slides:** 9 · **Suggested time:** 25 minutes

### Slide 6.1: AI history in three phases

- **The Start** (1950s–1960s), **the Failures** (two "AI winters"), **the Big Comeback** (1997 onwards).
- Pattern: big promises → disappointment → slower, more solid comeback.
- Three ingredients explain the story: **data**, **computing power**, **algorithms**.

**Visual:** [Timeline of AI history, 1950 to 2025, with two shaded AI winters](../../assets/images/ai-history-timeline.svg)

**Speaker notes:** AI is not a sudden invention of the 2020s; researchers have tried to build thinking machines for more than 70 years. When all three ingredients were weak, learning-based AI struggled; when all three became strong at the same time (around 2010), AI took off. Source: [Topic 06, Explanation section 1](../../topics/06-history-of-ai.md).

### Slide 6.2: The Start (1950–1966)

- **1950:** Turing, *Computing Machinery and Intelligence*: the imitation game (Turing test).
- **Aug 1955:** proposal by McCarthy, Minsky, Rochester and Shannon first uses "artificial intelligence"; **summer 1956:** Dartmouth workshop.
- **1956:** Logic Theorist proves theorems by search; **1958:** Rosenblatt's perceptron learns from examples.
- **1966:** Weizenbaum's ELIZA: pattern-matching "conversations", no understanding.

**Visual:** Left third of the [timeline diagram](../../assets/images/ai-history-timeline.svg), milestones 1950–1966.

**Speaker notes:** Correct a common error: the term was coined in the **1955 proposal**, not at the 1956 workshop (the timeline label "AI named as a research field" refers to the workshop founding the field). In runs reported in 1957 the Logic Theorist proved 38 of the first 52 theorems in chapter 2 of *Principia Mathematica*. In July 1958 the *New York Times* reported Navy expectations that the perceptron would eventually walk, talk and even be conscious; in reality it sorted simple patterns into two groups. Source: [Topic 06, Explanation section 2](../../topics/06-history-of-ai.md).

### Slide 6.3: Why early AI hit a wall

- **Combinatorial explosion:** real problems have astronomically many possibilities.
- **Common sense is huge:** nobody could write it all down as rules.
- **Weak hardware, little data.**
- **1969** *Perceptrons* (single-layer networks cannot learn XOR); **1973** Lighthill report → UK funding cuts.

**Visual:** Described simple visual: a small branching tree (river-crossing puzzle, "a few dozen states") next to an enormous, fading tree labeled "real-world problems".

**Speaker notes:** XOR means output YES if exactly one of two inputs is on, but not both; multi-layer networks could solve it, but nobody yet had a good way to train them. Historians debate how much of the decline *Perceptrons* caused on its own. The first AI winter is roughly 1974–1980; dates vary between sources. Source: [Topic 06, Explanation section 3](../../topics/06-history-of-ai.md).

### Slide 6.4: Boom and second winter

- **1980s expert-systems boom:** R1/XCON at DEC from 1980; savings in the tens of millions of dollars a year (estimates about $25M to $40M).
- **1986:** backpropagation popularized (Rumelhart, Hinton, Williams): multi-layer networks become trainable.
- **Second winter (~1987–1993):** expert systems brittle, expensive to maintain, unable to learn; Lisp-machine market collapses in 1987.

**Visual:** Middle third of the [timeline diagram](../../assets/images/ai-history-timeline.svg), showing the 1980s boom between the two shaded winters.

**Speaker notes:** Japan launched its Fifth Generation project in 1982; it ended without reaching its goals. XCON eventually needed thousands of rules. Much useful work continued under other names such as "machine learning", "data mining" or "decision support". Source: [Topic 06, Explanation section 3](../../topics/06-history-of-ai.md).

### Slide 6.5: The Big Comeback (1997–2022)

- **May 1997:** Deep Blue beats Kasparov 3.5–2.5 (search, ~200 million positions per second).
- **2012:** AlexNet wins ImageNet: top-5 error **15.3%** vs **26.2%** for the runner-up; trained on GPUs.
- **Mar 2016:** AlphaGo beats Lee Sedol **4–1** (deep learning + reinforcement learning + search).
- **Jun 2017:** the transformer; **30 Nov 2022:** ChatGPT released.

**Visual:** Right third of the [timeline diagram](../../assets/images/ai-history-timeline.svg).

**Speaker notes:** AlexNet had about 60 million weights and brought all three ingredients together: big data (ImageNet), compute (GPUs) and better algorithms. AlphaGo's "move 37" in game two surprised professionals. ChatGPT was an LLM fine-tuned to follow instructions, released as a free "research preview". Source: [Topic 06, Explanation section 4](../../topics/06-history-of-ai.md).

### Slide 6.6: [INTERACTION] Poll: how did Deep Blue win?

- In 1997 Deep Blue beat the world chess champion. **Was it mainly (A) machine learning from millions of games, (B) deep learning on GPUs, or (C) fast search guided by an expert-built evaluation function?**

**Visual:** Three voting buttons and a chess-board icon.

**Speaker notes:** **Answer: (C).** Deep Blue was mostly *not* machine learning: special hardware searched about 200 million positions per second, guided by an evaluation function built with help from chess experts, so it was "old" AI on very fast hardware. AlphaGo (2016), by contrast, relied heavily on neural networks trained on data and self-play. Source: [Topic 06, Explanation section 4 and Common mistake 2](../../topics/06-history-of-ai.md).

### Slide 6.7: What changed?

- Data: small and hand-typed → billions of web pages, photos and videos.
- Compute: slow and expensive → GPUs, huge data centers, cloud.
- Algorithms: hand-written rules, single-layer networks → backpropagation plus training improvements; transformers.
- Approach: mostly **rule-based** → mostly **learning-based**.

**Visual:** Four-row table, "1960s–1980s" vs "2010s onwards".

**Speaker notes:** The big idea, neural networks that learn from examples, existed in 1958; it needed data and compute to catch up before it worked at scale. Source: [Topic 06, Explanation section 5](../../topics/06-history-of-ai.md).

### Slide 6.8: Worked example: the neural network's long road

- 1958 perceptron (new algorithm; tiny data) → **boom**.
- 1969 *Perceptrons* (no way to train multi-layer nets) → **bust**.
- 1986 backpropagation → partial revival; 1990s–2000s still short of data and compute → niche.
- 2009–2012 ImageNet + GPUs + AlexNet → **boom**; 2017–2022 transformer, LLMs, ChatGPT → dominance.

**Visual:** A single line rising and falling across the timeline, annotated with the missing or new ingredient at each step.

**Speaker notes:** The same core idea "failed" in 1969 and "triumphed" in 2012. It was not simply wrong in 1969; the other ingredients were not ready, which is why historians are careful about saying an approach "failed": sometimes it was early. Source: [Topic 06, Worked example](../../topics/06-history-of-ai.md).

### Slide 6.9: The lesson: hype cycles

1. A real breakthrough on a narrow problem.
2. Over-generalized promises ("human-level AI within a generation").
3. Hitting hard limits (combinatorial explosion, brittleness, cost, lack of data).
4. A "winter", or a calmer phase if the technology delivers real value.

**Visual:** Described simple visual: a looping arrow through the four numbered stages.

**Speaker notes:** This does not mean today's AI will necessarily crash; modern AI produces real economic value, which the 1970s systems did not. The habit to take away: separate what a system can demonstrably do today from what people predict it will do. Source: [Topic 06, Explanation section 6](../../topics/06-history-of-ai.md).

---

## Deck 07: Real-world applications of AI

**Source:** [Topic 07: Real-world applications](../../topics/07-real-world-applications.md) · **Slides:** 8 · **Suggested time:** 20 minutes

### Slide 7.1: The six-part framework

- **Input** · **Output** · **AI type** (rule-based, machine learning, deep learning, generative) · **Benefit** · **Risk** · **Human oversight**.
- Rule of thumb: **the higher the stakes, the more human oversight is needed.**
- Real products often combine types; choose the most specific type that fits, and justify it.

**Visual:** Six numbered boxes in a ring, one per question.

**Speaker notes:** A bad film suggestion wastes an evening; a missed tumor can cost a life. A self-driving car uses deep learning to see, rule-based safety logic and search-style route planning, all in one product. Source: [Topic 07, Explanation section 1](../../topics/07-real-world-applications.md).

### Slide 7.2: Recommendation systems

- Job: **rank** items from a huge catalog for each person, using behavioral data (watched, skipped, rated, searched).
- **Collaborative filtering:** people who agreed in the past will probably agree on items they haven't seen.
- Netflix (2015, company figures): the recommender "influences choice for about 80% of hours streamed"; saves more than $1 billion per year.
- Risks: filter bubbles, a goal (watch time) that may not match your well-being, privacy.

**Visual:** Described simple visual: a streaming home screen with rows of titles, one row labeled "Because you watched...".

**Speaker notes:** A recommender optimizes whatever target humans choose; if the goal is "maximize watch time", it may learn that sensational content keeps people watching. The AI is not "trying" to do harm; choosing the target is a human decision with ethical consequences (Topic 08). Source: [Topic 07, Explanation section 2](../../topics/07-real-world-applications.md).

### Slide 7.3: [INTERACTION] Predict: should Sam get Film D?

- *Illustrative (made-up) ratings, 1 to 5.* Sam: A 5, B 4, C 1, D not watched. Priya: A 5, B 5, C 1, D 5. Leo: A 1, B 2, C 5, D 1.
- **Whose taste is closest to Sam's? Should the service recommend Film D to Sam?** Vote: yes / no.

**Visual:** The 3 × 4 ratings table, with Sam's empty Film D cell marked "?".

**Speaker notes:** **Answer: yes.** Priya's ratings for A, B and C almost match Sam's, while Leo's are the opposite; Priya rated Film D 5, so Sam will probably like it. Leo's rating of 1 is not a warning, because his taste is the opposite of Sam's. The next slide shows the step-by-step trace. Source: [Topic 07, Worked example](../../topics/07-real-world-applications.md).

### Slide 7.4: Worked example: tracing the recommendation

- Step 1: add the rating differences on films both have rated (ignore minus signs): Sam vs Priya = 0 + 1 + 0 = **1**; Sam vs Leo = 4 + 2 + 4 = **10**.
- Steps 2 to 4: most similar user = Priya; she rated Film D 5 → predicted rating ≈ 5 → **recommend Film D**.
- Step 5: Sam's own rating of Film D becomes new training data (the feedback loop).
- New film nobody has rated? Nothing to compare: the **cold-start problem**.

**Visual:** The two-row "total difference" table, then an arrow from Priya's Film D rating to Sam's empty cell.

**Speaker notes:** The feedback loop is what makes recommenders learning systems. Real systems compare millions of users and items with many more signals (watch time, skips, searches) and learn how to combine them, rather than using our hand-written "add up the differences" rule. The cold-start problem is one reason popular items tend to get even more popular. Source: [Topic 07, Worked example](../../topics/07-real-world-applications.md).

### Slide 7.5: Healthcare: medical imaging

- Deep-learning models trained on thousands of labeled images, e.g. retina photos labeled by specialists.
- FDA list of AI-enabled devices: well over a thousand by end of 2025, about three-quarters in **radiology**.
- **IDx-DR** (April 2018): first AI device to give a screening result **without a specialist interpreting the image**; about **87%** sensitivity, about **90%** specificity.
- ~13 in 100 patients with the disease were missed → a **screening** tool, not a final diagnosis.

**Visual:** Described simple visual: a retina photo → "AI screening" box → two outcomes, "refer to an eye specialist" or "rescreen in 12 months".

**Speaker notes:** Sensitivity is the share of people who really have the condition that the test flags; specificity is the share without it that the test clears. Warning case: Obermeyer and colleagues (2019) found an algorithm that used past healthcare *costs* as a stand-in for health *need* cut the number of Black patients identified for extra care by more than half; what you ask the AI to predict matters as much as the data. LLM tools that draft clinical notes can hallucinate, so a clinician must check every note. Source: [Topic 07, Explanation section 3](../../topics/07-real-world-applications.md).

### Slide 7.6: Transportation

- **Navigation:** travel-time **prediction** is machine learning; finding the fastest route is **search** (like the river puzzle, much bigger).
- **Driver assistance:** deep learning recognizes cars, people and lane markings; the human driver stays responsible.
- **Robotaxis:** Waymo reports about 271 million rider-only miles by June 2026 and about 82% fewer injury crashes than human benchmarks (**company-reported**).
- Hardest problem: **rare situations** not in the training data.

**Visual:** Described simple visual: a map route with a predicted arrival time, beside a robotaxi with sensor cones labeled camera, radar, lidar.

**Speaker notes:** The Waymo comparison depends on assumptions (for example, how many human crashes are never reported) and on cities with little snow; independent studies are the best confirmation. In March 2018 an Uber self-driving test car struck and killed Elaine Herzberg in Tempe, Arizona; the NTSB found late detection, a distracted safety driver and inadequate safety culture and oversight, raising the question of who is accountable when AI and a human share control. Source: [Topic 07, Explanation section 4](../../topics/07-real-world-applications.md).

### Slide 7.7: Stakes and oversight side by side

- Streaming recommender: stakes **low** → goal-setting and testing.
- AI eye-disease screening: stakes **high** → specialist follow-up, regulator.
- Robotaxi: stakes **very high** → permits, remote staff, incident reporting.

**Visual:** The topic's comparison table (input, output, AI type, benefit, risk, stakes, oversight for the three applications).

**Speaker notes:** Read the "Stakes of one error" row first, then the "Human oversight" row, and point out that they rise together. The EU AI Act's risk tiers (Topic 10) formalize this same "stakes → oversight" idea. Source: [Topic 07, Visual](../../topics/07-real-world-applications.md).

### Slide 7.8: Common mistakes

- "Modern app = generative AI": most everyday AI is **predictive** (picks, ranks or labels).
- "High accuracy means no human is needed": about 87% sensitivity still misses patients.
- "Recommendations show what is best for me": they show what you are predicted to engage with.
- "Self-driving cars are totally safe / unsafe": evidence is mixed; ask who measured it and how.

**Visual:** Four myth/fact cards.

**Speaker notes:** Whether a human is needed depends on the stakes of an error and on how well the system was tested on the people it is used with, not on a single accuracy number. Source: [Topic 07, Common mistakes](../../topics/07-real-world-applications.md).

---

## Deck 08: Ethics, risks and social impact of AI

**Source:** [Topic 08: Ethics, risks and social impact](../../topics/08-ethics-risks-social-impact.md) · **Slides:** 9 · **Suggested time:** 30 minutes

### Slide 8.1: Why AI raises ethical questions

- AI works at **massive scale**, learns from **historical data**, can be **hard to inspect**, and can **create convincing content**.
- Four starter questions: **Who benefits? Who could be harmed? What could go wrong? Who is responsible if it does?**
- Six issues: bias · privacy · jobs · accountability and transparency · environmental cost · misinformation and deepfakes.

**Visual:** Six labeled icons in a row, one per issue.

**Speaker notes:** People choose what problem to solve, what data to use, what to predict and where to deploy; each choice can help or harm. Source: [Topic 08, Explanation section 1](../../topics/08-ethics-risks-social-impact.md).

### Slide 8.2: Where bias enters

- Seven life-cycle stages: problem definition, data collection, labeling, training, testing, deployment, feedback and monitoring.
- Bias is not only "bad data": a poor **proxy** target, biased labels, overall-only testing and use in a new setting all matter.

**Visual:** [Where bias can enter during the life cycle of an AI system](../../assets/images/ai-system-lifecycle-bias.svg)

**Speaker notes:** Walk once around the loop with one example per stage: predicting healthcare cost instead of need; a face dataset mostly of lighter-skinned men; past hiring decisions as the label; 95% overall accuracy hiding 65% for one group (illustrative made-up figures); a model trained in one country used in another; a recommender that makes popular items more popular. Source: [Topic 08, Explanation section 2](../../topics/08-ethics-risks-social-impact.md).

### Slide 8.3: Bias: real cases

- **Gender Shades (2018):** three commercial gender classifiers (IBM, Microsoft, Face++), new balanced test set of 1,270 parliamentarians; error up to **34.7%** for darker-skinned women vs at most **0.8%** for lighter-skinned men.
- Lesson: break results down by group (**disaggregated evaluation**).
- **Amazon hiring tool (Reuters, 2018):** learned to penalize resumes containing "women's"; abandoned.
- **Healthcare proxy (2019):** cost used as a stand-in for need under-identified Black patients.

**Visual:** Described bar pair: "lighter-skinned men: max 0.8% error" vs "darker-skinned women: up to 34.7% error".

**Speaker notes:** The companies' overall accuracy figures hid the gap because their test sets lacked darker-skinned women. Note the study's own limits: it tested gender *classification*, not recognition of individuals, and used a binary gender label. Amazon said its tool was never used by recruiters to evaluate candidates on its own. Source: [Topic 08, Explanation section 2](../../topics/08-ethics-risks-social-impact.md).

### Slide 8.4: Privacy

- **Collection without consent:** Dutch DPA fined Clearview AI **€30.5 million** (September 2024) for a database of scraped face photos.
- **Inference** of sensitive information you never shared.
- **Surveillance** with face recognition in public spaces.
- What you type into chatbots may be stored and used to improve models.

**Visual:** Described simple visual: a padlock over a face icon, with arrows labeled "scraped", "inferred", "tracked", "typed in".

**Speaker notes:** Safeguards: data minimization, clear consent, anonymizing data, strong security and laws such as the GDPR. Never paste other people's personal data or confidential information into a public chatbot unless you know how it will be handled. Source: [Topic 08, Explanation section 3](../../topics/08-ethics-risks-social-impact.md).

### Slide 8.5: Jobs: reading the WEF 2025 numbers

- WEF *Future of Jobs Report 2025* (1,000+ employers, 14M+ workers, 55 economies), for **2025–2030**:
- **170 million** jobs created · **92 million** displaced · **net +78 million**.
- Projections, not facts; several drivers, not only AI; "net" hides real losses (~22% churn).
- AI usually automates **tasks**, not whole jobs.

**Visual:** Described bar chart: 170M up, 92M down, 78M net, with the subtraction 170 − 92 = 78 written underneath.

**Speaker notes:** The earlier draft said 91 million displaced; the correct figure is 92 million. The new jobs are often in different places, sectors and skill levels: a cashier whose job disappears does not automatically become a data analyst. "AI will take all jobs" is a misconception (Topic 09); "AI will cause serious disruption for some workers" is a real concern. Source: [Topic 08, Explanation section 4](../../topics/08-ethics-risks-social-impact.md).

### Slide 8.6: [INTERACTION] What's wrong with this headline?

- Headline: **"AI to create 78 million new jobs by 2030."**
- **Find two ways it is misleading.** (Hint: check the WEF figures on the last slide.)

**Visual:** A mock newspaper headline with a red question mark.

**Speaker notes:** **Answer (any two):** (a) 78 million is the **net** figure; the report projects 170 million created and 92 million displaced; (b) the change is driven by **several trends**, not AI alone; (c) it is a **projection** from employer surveys, not a certainty. Follow-up: for every 10 jobs created, about 5 are displaced (92 ÷ 170 ≈ 0.54). Source: [Topic 08, Activity 2 and Answers](../../topics/08-ethics-risks-social-impact.md).

### Slide 8.7: Accountability and transparency

- *Mata v. Avianca* (June 2023): lawyers cited six non-existent cases generated by ChatGPT; fined **$5,000** in total.
- **The human who uses an AI output remains responsible.**
- Uber crash (2018): responsibility shared by software, safety driver, company culture and regulators.
- **Black box:** even designers cannot read off the reason for one decision; explainable AI and disclosure laws respond.

**Visual:** Described simple visual: a courtroom gavel beside a chat bubble labeled "the AI said so" crossed out.

**Speaker notes:** AI systems are not legal persons; the people and organizations that build, deploy and use them are responsible. Safeguards: clear responsibility rules, decision logs, a right to human review and independent audits. Source: [Topic 08, Explanation section 5 and Common mistake 4](../../topics/08-ethics-risks-social-impact.md).

### Slide 8.8: Environment, misinformation and deepfakes

- IEA (April 2025): data-center electricity to **more than double by 2030, to ~945 TWh** a year (slightly more than Japan uses today); AI-specific demand more than quadruples.
- LLM hallucinations spread **accidental misinformation**.
- **Deepfake fraud:** Arup, Hong Kong, early 2024: a video call of fake colleagues; 15 transfers totaling **HK$200 million (~US$25 million)**.

**Visual:** Two panels: a data-center icon with "~945 TWh by 2030"; a video-call grid with every face marked "deepfake".

**Speaker notes:** One query's energy is small; the impact comes from billions of queries and ever-larger models, and data centers affect local grids and water supplies. Safeguards for deepfakes: verify unexpected requests through a second channel, labeling and watermarking (the EU AI Act requires labeling of deepfakes), and media literacy. Source: [Topic 08, Explanation sections 6 and 7](../../topics/08-ethics-risks-social-impact.md).

### Slide 8.9: Analyzing a case in seven steps

1. Describe the system. 2. List stakeholders. 3. Benefits. 4. Harms (check all six issues). 5. Evidence. 6. Safeguards. 7. Judgment: use as is, with conditions, or not at all.

- Worked example *HireFast* (illustrative, made-up): label "was hired" + 85% of past hires were men → model learns "women's" = "not hired" → 90% overall accuracy hides the bias → **fix or do not deploy**.

**Visual:** Seven numbered steps down the left; the HireFast trace (collect → features → train → test → deploy) down the right.

**Speaker notes:** HireFast fixes: check data balance and whether "was hired" is a fair label; remove obvious proxies; compare selection rates by group (if 20% of men but only 10% of equally qualified women are invited, investigate); use AI only to assist, with human review. If bias cannot be reduced to an acceptable level, do not deploy, which is what Amazon eventually did. Source: [Topic 08, Explanation section 8 and Worked example](../../topics/08-ethics-risks-social-impact.md).

---

## Deck 09: Limitations and common misconceptions

**Source:** [Topic 09: Limitations and misconceptions](../../topics/09-limitations-and-misconceptions.md) · **Slides:** 8 · **Suggested time:** 25 minutes

### Slide 9.1: Limitations vs misconceptions

- **Limitation:** a real weakness of current AI → *manage it* (check outputs, add oversight).
- **Misconception:** a false belief people hold → *correct it*.
- Over-trust ("it's always right") and under-estimation ("it's just autocomplete") both cause problems.

**Visual:** Two columns: "Limitation: manage" (wrench icon) and "Misconception: correct" (eraser icon).

**Speaker notes:** Both matter: overestimating AI leads to over-trust; underestimating it leads people to ignore real benefits and real risks. Source: [Topic 09, Explanation section 1](../../topics/09-limitations-and-misconceptions.md).

### Slide 9.2: Hallucinations: why fluent text can be false

- An LLM generates **likely** text one token at a time; it has no built-in fact database.
- Common facts: likely = true. **Rare facts:** it still produces title-shaped titles and year-shaped numbers.
- Training and tests often **reward guessing** over "I don't know" (Kalai et al., 2025).
- Not lying: there is no intention to deceive.

**Visual:** [Next-token prediction diagram](../../assets/images/next-token-prediction.svg) with the caption "likely, not verified".

**Speaker notes:** Use the library comparison: a student who has read a whole library but has no notes in the exam writes something that sounds like an answer when they don't remember. Reducers (not cures): grounding in trusted documents or search results, asking for sources and checking they exist and say what is claimed, and using AI where errors are easy to spot. Source: [Topic 09, Explanation section 2.1](../../topics/09-limitations-and-misconceptions.md).

### Slide 9.3: Brittleness and other limitations

- **Distribution shift:** reliable mainly on inputs similar to training data (dusk photos, a new hospital's scanners, road works).
- **Adversarial examples** (Szegedy et al., 2013): tiny invisible image changes cause misclassification.
- **Knowledge cutoff**, **token-level blind spots** (counting letters), **black box**, **data quality**.
- Models are often **confidently** wrong.

**Visual:** Described simple visual: two photos of the same leaf, "daylight photo → correct" and "dusk photo → wrong, but stated just as confidently".

**Speaker notes:** Models do not reliably "know when they don't know". If you ask an LLM to explain its reasoning, the explanation is itself generated text and may not reflect what happened inside the model. Source: [Topic 09, Explanation sections 2.2 and 2.3](../../topics/09-limitations-and-misconceptions.md).

### Slide 9.4: Misconceptions 1–3

- **"AI is alive or conscious":** no scientific evidence; "I feel happy" is a likely continuation (ELIZA effect).
- **"AI understands like humans":** debated; judge it by how reliably it performs and check outputs.
- **"AI is always objective":** it can learn and scale human bias (Gender Shades: up to 34.7% vs at most 0.8% error).

**Visual:** Three myth cards, each with a one-line correction.

**Speaker notes:** In the 1960s people became emotionally attached to ELIZA, a simple rule-based program. Whether a future machine could be conscious is an open philosophical question, not a description of today's tools; "self-aware AI" is hypothetical (Topic 05). A computer applies its learned pattern consistently, but consistently applying a biased pattern is not fairness. Source: [Topic 09, Explanation section 3, misconceptions 1 to 3](../../topics/09-limitations-and-misconceptions.md).

### Slide 9.5: Misconceptions 4–6

- **"AI will take all our jobs":** WEF 2025 projects 92M displaced, 170M created, net +78M (2025–2030): large disruption, not total replacement.
- **"More data always fixes it":** only the **right** data (representative, well-labeled, right target).
- **"Confident means correct":** a hallucination sounds exactly as confident as a true answer (*Mata v. Avianca*, 2023).

**Visual:** Three myth cards with corrections.

**Speaker notes:** Keep the nuance on jobs: 92 million displaced jobs means many real people losing work, and outcomes depend on retraining, policy and how organizations use AI. Adding a million more resumes from the same male-dominated history would not have fixed the hiring tool, and the healthcare proxy case was fixed by changing what was predicted. Source: [Topic 09, Explanation section 3, misconceptions 4 to 6](../../topics/09-limitations-and-misconceptions.md).

### Slide 9.6: The four-step check

1. **Split** the answer into separate factual claims.
2. **Prioritize** risky claims: rare facts, exact numbers, quotations, references.
3. **Verify** each in an independent, reliable source; check cited sources exist and say what is claimed.
4. **Decide:** keep, correct, remove, or label as unverified.

**Visual:** Four numbered icons: scissors, flag, magnifying glass, checkmark.

**Speaker notes:** Do not ask the chatbot whether its own answer is correct and trust the reply: that check is generated by the same process. Source: [Topic 09, Explanation section 4 and Common mistake 4](../../topics/09-limitations-and-misconceptions.md).

### Slide 9.7: [INTERACTION] Spot the hallucination

- A chatbot says: (1) "Turing published 'Computing Machinery and Intelligence' in 1950." (2) "The term 'artificial intelligence' was first used at the Dartmouth workshop in 1962." (3) "ELIZA was created by Joseph Weizenbaum."
- **Which claim is false, and what is the correct fact?**

**Visual:** The three claims on cards, with vote buttons 1, 2, 3.

**Speaker notes:** **Answer: claim 2.** The term first appears in the **1955** proposal, and the workshop was held in **summer 1956**. Claims 1 and 3 are correct. The full worked example adds two more false claims (ELIZA "understood emotions", and an invented 1966 book *Machines That Feel* with a "90%" statistic); the invented source is the most dangerous because a reference makes a claim *look* checked. Source: [Topic 09, Worked example](../../topics/09-limitations-and-misconceptions.md).

### Slide 9.8: Summary: limitations vs misconceptions

- Limitations: hallucinations, brittleness, knowledge cutoff → verify, keep inputs similar to training data, connect to current sources.
- Misconceptions: conscious, understands like us, objective, takes all jobs, more data fixes it, confident = correct.
- Don't over-correct: "AI is useless because it makes mistakes" is also wrong; ask whether the error rate is acceptable *for this task with this level of checking*.

**Visual:** The topic's summary table (type / statement / accurate version).

**Speaker notes:** Not every AI error is a "hallucination": a spam filter misclassifying an email is an ordinary prediction error (a false positive). Grounding and better training reduce hallucinations, but users should still expect and check for them. Source: [Topic 09, Visual summary table and Common mistakes](../../topics/09-limitations-and-misconceptions.md).

---

## Deck 10: The future of AI

**Source:** [Topic 10: The future of AI](../../topics/10-future-of-ai.md) · **Slides:** 9 · **Suggested time:** 30 minutes

### Slide 10.1: Thinking about the future carefully

- Predictions about AI have a mixed record (two AI winters; few predicted 2023's fluent chatbots).
- Habit 1: **separate evidence from prediction.**
- Habit 2: **notice who is speaking and why.**
- Two big questions: *Will we build AGI?* *How will society govern AI?*

**Visual:** Described simple visual: two speech bubbles, "This system scored X on this test" (labeled EVIDENCE) and "This means human-level AI by 2030" (labeled PREDICTION).

**Speaker notes:** Companies raising money, researchers, journalists and campaigners may all have different incentives. The topic ends with what learners themselves can do. Source: [Topic 10, Explanation section 1](../../topics/10-future-of-ai.md).

### Slide 10.2: What is AGI, and is it here?

- **AGI:** hypothetical AI with human-like *generality*; **no single agreed definition** (tasks? learning ability? physical abilities?).
- Mainstream view: **current LLMs are not AGI**; debated; no agreed test.
- Google DeepMind "Levels of AGI" (Morris et al., 2023): 2023 chatbots = "Emerging AGI"; one proposal, not a standard.

**Visual:** [Two-lenses diagram](../../assets/images/types-of-ai-two-lenses.svg), with AGI and ASI on the capability lens marked "hypothetical".

**Speaker notes:** All AI in use today is narrow; even broad LLMs hallucinate, are brittle in unfamiliar situations and cannot reliably learn new skills from a few experiences. Because definitions differ, two people can disagree about whether AGI is "close" simply because they mean different things. Source: [Topic 10, Explanation section 2](../../topics/10-future-of-ai.md).

### Slide 10.3: What do researchers forecast?

- Grace et al. (2024): **2,778** AI researchers surveyed.
- **10%** chance machines outperform humans at every task by **2027**; **50%** by **2047** (13 years earlier than one year before).
- 50% chance all occupations fully automated only by **2116**.
- **Very wide disagreement**; these are opinions, not measurements.

**Visual:** Described simple visual: a horizontal year axis with markers at 2027 (10%), 2047 (50%) and 2116 (50%, all occupations), and a wide shaded band labeled "individual answers vary widely".

**Speaker notes:** The 13-year shift in a single year shows how quickly opinions moved after ChatGPT. Experts' forecasts have been wrong before in both directions. Source: [Topic 10, Explanation section 2](../../topics/10-future-of-ai.md).

### Slide 10.4: Four viewpoints on AGI

- **"AGI could arrive soon":** capabilities have grown fast with models, data and compute.
- **"Current methods are not enough":** hallucination, brittleness, data hunger; new ideas needed.
- **"Prepare for serious risks":** build safety research and oversight now.
- **"Focus on today's harms":** bias, privacy, misinformation, jobs, energy.

**Visual:** Four-quadrant grid, one viewpoint per quadrant, each with "What would change their mind?" in small text.

**Speaker notes:** These views are not mutually exclusive; many people hold parts of several. A reasonable summary in 2026: no consensus on what AGI is, whether current methods can reach it, or when it might arrive, while today's narrow AI already raises issues that need managing now. Source: [Topic 10, Explanation section 2, viewpoints table](../../topics/10-future-of-ai.md).

### Slide 10.5: The EU AI Act: four risk tiers

- Regulation (EU) 2024/1689; **in force 1 August 2024**; applies to anyone placing or using AI in the EU, even companies based outside it.
- **Unacceptable** (banned) · **High** (strict obligations) · **Transparency** (disclose / label) · **Minimal** (no specific new obligations).
- Separate rules for **general-purpose AI models**.
- Fines up to **€35 million or 7%** of worldwide turnover for banned practices; most other breaches up to €15 million or 3%.

**Visual:** Pyramid (from the topic's Visual table): top Unacceptable (social scoring; emotion recognition at work or school) → High (CV sorting, exam scoring, credit scoring) → Transparency (chatbots, deepfakes) → base Minimal (spam filters, video-game AI).

**Speaker notes:** Instead of regulating "AI" as one thing, the Act sets rules according to the risk a use poses: stricter where potential harm is greater. Most AI systems fall into the minimal tier; the Act does not "ban AI". Source: [Topic 10, Explanation section 4](../../topics/10-future-of-ai.md).

### Slide 10.6: The timeline, after the 2026 changes

- 2 Feb 2025: bans + AI literacy · 2 Aug 2025: general-purpose AI model rules + governance.
- 2 Aug 2026: general application, including **transparency** duties.
- 2 Dec 2026: new ban (non-consensual intimate content / child sexual abuse material).
- High-risk: **2 Dec 2027** stand-alone uses (was 2 Aug 2026); **2 Aug 2028** AI in regulated products (was 2 Aug 2027).

**Visual:** Horizontal timeline with the seven dates; the two high-risk dates shown with the original date struck through.

**Speaker notes:** The changes come from the **Digital Omnibus on AI**: proposed 19 November 2025, politically agreed in May 2026, in force from 27 July 2026 (per the European Commission). As of 6 November 2026, the bans, GPAI rules and transparency duties apply; the main high-risk obligations do not yet. Sources differ slightly on details (6 or 7 May 2026), so check the consolidated text on EUR-Lex for legal decisions. Source: [Topic 10, Explanation section 4, timeline and uncertainty note](../../topics/10-future-of-ai.md).

### Slide 10.7: [INTERACTION] Which tier?

- Use the four questions in order: *Banned? High-risk area? Interacts with people or generates content? Otherwise minimal.*
- **A company uses a chatbot in its CV-screening process: it asks applicants interview questions and scores their answers. Which tier or tiers?**

**Visual:** The four-question flowchart with the pyramid beside it.

**Speaker notes:** **Answer: High risk + Transparency (two tiers).** Step 2: it is used in employment to score applicants, so it is high risk; Step 3: it interacts directly with people, so applicants must be told they are talking to an AI. Tiers are not always exclusive. Source: [Topic 10, Worked example method and Activity 1 item 8 answer](../../topics/10-future-of-ai.md).

### Slide 10.8: Binding law vs soft law

- **EU AI Act:** binding law with fines; risk-based tiers.
- **OECD AI Principles** (2019, updated May 2024): 47 adherents; 5 values-based principles + 5 recommendations; non-binding.
- **UNESCO Recommendation on the Ethics of AI** (November 2021): 193 member states; 4 core values, 10 principles; non-binding.
- **Council of Europe Framework Convention** (opened for signature September 2024): first legally binding international AI treaty.

**Visual:** Three-row comparison table: framework / type / who / year / main approach.

**Speaker notes:** OECD's five principles: inclusive growth and well-being; human rights and democratic values; transparency and explainability; robustness, security and safety; accountability. OECD and UNESCO frameworks cannot fine anyone; they guide national laws and shape expectations. Source: [Topic 10, Explanation section 5](../../topics/10-future-of-ai.md).

### Slide 10.9: What you can do: AI literacy

- Verify before you trust · Match trust to stakes · Protect privacy.
- Be open about AI use · Watch for deepfakes and manipulation.
- Ask the governance questions (Who built it? What data? Who is accountable? Can I ask a human?) · Keep learning.

**Visual:** Seven-item checklist with tick boxes.

**Speaker notes:** Each item links back to a topic: verification to Topic 09, stakes to Topic 07, privacy and deepfakes to Topic 08. The concepts in this module (data, training, inference, bias, hallucination, risk) will help learners understand whatever comes next. Source: [Topic 10, Explanation section 6](../../topics/10-future-of-ai.md).
