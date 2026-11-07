# Mission 08: Time Machine

**Pixel's AI Field Guide: Missions for Curious Humans** · Version 1.0 (2026-11-06)
**Covers:** Topic 06, [The History and Evolution of AI](../../task-1/topics/06-history-of-ai.md) · **Time:** about 85 minutes (core) + 20 minutes (optional)
**Navigation:** [Start here](00-start-here.md) · Previous: [Mission 07](mission-07-sorting-the-robots.md) · Next: [Mission 09](mission-09-ai-in-the-wild.md) · [Glossary](glossary.md) · [Resources](resources.md)

---

## [MISSION BRIEF] The cardboard time machine

Pixel has built a time machine out of a cardboard box and a desk lamp. It does not work, but on the way out of the box Pixel drops the museum's history cards and they scatter across the floor. "AI was invented in 2022 anyway," Pixel says, "so the old cards don't matter." Dr. Ada Okafor picks up a card dated 1966 and smiles: "Let's put these back in order. AI's history has a shape, and that shape will help you judge tomorrow's headlines."

### Learning goals

By the end of this mission you should be able to:

- **Place** key AI milestones from 1950 to 2022 in order and give their approximate dates.
- **Distinguish** the three phases of AI history: **the Start** (1950s–1960s), **the Failures** (two "AI winters") and **the Big Comeback** (1997 onwards).
- **Explain** what caused each winter and the comeback, using the three ingredients **data, computing power and algorithms**.
- **Investigate** a 1966 chatbot, ELIZA, and explain how it produces replies without understanding anything.
- **Apply** the boom-and-bust pattern to judge whether a new AI claim shows warning signs of hype.

---

## [PREDICT] Before you start (3 minutes)

Write down your answers. You will check them at the end of the mission.

1. Roughly when was the term "artificial intelligence" first used? (1920s / 1950s / 1980s / 2010s)
2. The chess computer that beat the world champion in 1997: did it **learn** chess from data, or did it **search** through moves very fast?
3. Have there been times when people gave up on AI? If so, why do you think that happened?

---

## [TRY IT] Activity 8.1: Put history back in order

**Goal:** Sequence the main milestones of AI history, sort them into three phases, and explain how one event led to another.

**Preparation:** Paper and pen. Copy each card below onto a scrap of paper or sticky note (just the letter and a few key words is enough), plus the two **winter strips**. A long table or the floor works well as a timeline. About 25 minutes. No device needed.
*Short on time?* Use the **10-card quick set**: D, I, K, J, B, A, F, C, G, N.

**The 15 shuffled cards (no dates on purpose):**

| Card | What happened |
|---|---|
| A | A rule-based program starts configuring computer orders for a big computer company and saves it tens of millions of dollars a year. |
| B | A report commissioned by the UK government says AI has failed to deliver its grand promises. University funding for AI is cut. |
| C | A deep neural network trained on GPUs wins an image-recognition competition with 15.3% top-5 error, against 26.2% for the next-best entry. |
| D | A paper asks "Can machines think?" and proposes the "imitation game" as a test. |
| E | A book proves that a single-layer perceptron cannot learn certain simple patterns, such as "exclusive OR" (XOR). |
| F | A chess computer that searches about 200 million positions per second beats the world champion 3.5–2.5. |
| G | A new neural-network design based on "attention" is published. It later powers large language models. |
| H | Specialized "Lisp machine" computers for AI stop selling, and many expert-system companies fail. |
| I | Four researchers write a funding proposal for a summer research project and use the words "artificial intelligence" for the first time. |
| J | A program with a "DOCTOR" script turns users' typed words back into questions. Some users become emotionally attached to it. |
| K | A machine that learns simple yes/no patterns from examples is unveiled. A newspaper reports it may one day walk, talk and be conscious. |
| L | A paper makes "backpropagation" widely known: a way to train neural networks that have hidden layers. |
| M | A Go program that combines deep neural networks, self-play and search beats one of the world's strongest players 4–1. |
| N | A chatbot released as a free "research preview" brings generative AI into everyday use within weeks. |
| O | A summer workshop at Dartmouth College takes place; it is usually treated as the founding of AI as a research field. |

**Winter strips:** "First AI winter" and "Second AI winter".

**Task:**

1. Put the cards in **chronological order**. Try from memory and reasoning first (for example: which events must come before others?).
2. Lay the two **winter strips** where you think funding and interest collapsed.
3. Label each card **Start**, **Failures** or **Comeback**.
4. Mark each card **R** (rule-based or search, people write the knowledge) or **L** (learning-based, the system learns from data). Some cards may be neither; some may be both.
5. Choose **three pairs** of cards and write one sentence for each explaining how the earlier event helped cause, or set up, the later one.

**Observation:** Record your order, then compare it with the timeline figure in the [EXPLAIN] section. Which cards did you misplace, and by how much?

**Reflection:** Neural networks appear on cards K (1958), E (1969), L (1986) and C (2012). Why do you think the same idea went from hype, to rejection, to triumph?

**Feedback:**

<details>
<summary>[DEBRIEF] Order, phases and links (open after you have tried)</summary>

| Order | Card | Date | Milestone | Phase | R / L |
|---|---|---|---|---|---|
| 1 | D | 1950 | Alan Turing, *Computing Machinery and Intelligence* (imitation game / Turing test) | Start | neither (a question, not a program) |
| 2 | I | Aug 1955 | Dartmouth proposal by McCarthy, Minsky, Rochester and Shannon: first use of "artificial intelligence" | Start | neither |
| 3 | O | Summer 1956 | Dartmouth workshop: founding of AI as a field | Start | neither |
| 4 | K | 1958 | Frank Rosenblatt's **perceptron**, with heavy press hype | Start | L |
| 5 | J | 1966 | Joseph Weizenbaum's **ELIZA** paper | Start | R |
| 6 | E | 1969 | Minsky and Papert, *Perceptrons* | Failures | (about L) |
| 7 | B | 1973 | The **Lighthill report** (UK) | Failures | neither |
| | *strip* | ~1974–1980 | **First AI winter** | Failures | |
| 8 | A | 1980 | **XCON (R1)** in use at Digital Equipment Corporation: the expert-systems boom | Failures (a boom *between* the winters) | R |
| 9 | L | 1986 | Rumelhart, Hinton and Williams popularize **backpropagation** | Failures (seeds of the comeback) | L |
| 10 | H | 1987 | Lisp-machine market collapses | Failures | R |
| | *strip* | ~1987–1993 | **Second AI winter** | Failures | |
| 11 | F | May 1997 | **Deep Blue** beats Garry Kasparov 3.5–2.5 | Comeback | R (search + fast hardware, **not** machine learning) |
| 12 | C | 2012 | **AlexNet** wins ImageNet (15.3% vs 26.2% top-5 error) | Comeback | L |
| 13 | M | Mar 2016 | **AlphaGo** beats Lee Sedol 4–1 in Seoul | Comeback | both (deep learning + reinforcement learning + search) |
| 14 | G | Jun 2017 | The **transformer** paper, *Attention Is All You Need* | Comeback | L |
| 15 | N | 30 Nov 2022 | **ChatGPT** released | Comeback | L |

Winter dates are approximate; sources differ by a year or two. What matters is the pattern. Card A can also be labeled "boom between the winters": the key is that it comes **before** the second winter.

**Example cause-and-effect links** (any accurate link earns credit):
- **K -> E:** the perceptron's hype raised expectations; *Perceptrons* showed the limits of single-layer networks, and interest moved away from neural networks.
- **E/B -> first winter:** disappointments plus the Lighthill report's criticism (especially the "combinatorial explosion") made funders cut back.
- **A -> H:** XCON's success started an expert-systems boom; when these systems proved brittle and costly to maintain, and the specialized hardware market collapsed, the boom became the second winter.
- **L -> C:** backpropagation made multi-layer networks trainable; once big data (ImageNet) and GPUs arrived, deep networks like AlexNet could finally win.
- **G -> N:** the transformer could be trained efficiently on huge amounts of text, which led to large language models such as the one behind ChatGPT.

**Reflection answer:** the idea was not simply "wrong" in 1969. It was **early**: it needed an algorithm to train multi-layer networks (1986), lots of data (2000s) and fast hardware (GPUs) before it could beat other methods. When all three ingredients came together around 2012, neural networks took over.

**Common slips:** putting ChatGPT first because it is the most famous ("AI was invented recently"); calling Deep Blue machine learning; placing the term "artificial intelligence" at the 1956 workshop instead of the **1955** proposal.
</details>

---

## [TRY IT] Activity 8.2: Investigate ELIZA, a chatbot from 1966

**Goal:** Discover how a rule-based chatbot produces convincing replies with **no understanding**, find where the conversation breaks down, and connect this to the "ELIZA effect".

**Preparation:**
- A computer, tablet or phone with a web browser and internet access. **No account, no installation, no personal data needed.**
- Platform: **ELIZA, 1966-faithful reconstruction** by Anthony Hay and Max Hay, version 1.00 (2025-03-08): <https://anthay.github.io/eliza.html>. Its authors state that its replies should be exactly what Weizenbaum's 1966 ELIZA, running his DOCTOR script, would have given. (External resource; the program is released as CC0, the DOCTOR script is (c) 1966 ACM.)
- The page is a single file: you can save it (File -> Save page) and use it offline later.
- About 25 minutes. Paper for a results table.
- *Can't get online?* Skip to the **fallback** below; you can do the whole investigation with the printed 1966 conversation.

> **Content note:** ELIZA's DOCTOR script imitates a therapist, so it asks about feelings and family. Use the made-up test sentences below rather than real personal problems. ELIZA is a 60-year-old toy, and no chatbot is a substitute for talking to a real person when you need help.

**Task:**

1. Open the page. ELIZA greets you in capital letters (it only "speaks" in uppercase). Click in the input area at the bottom.
2. Copy this results table:

| # | Type exactly this, then press Enter | Your prediction (before typing) | ELIZA's actual reply |
|---|---|---|---|
| 1 | `My mother is always busy.` | | |
| 2 | `I am a robot.` | | |
| 3 | `I am not sad.` | | |
| 4 | `You are a computer.` | | |
| 5 | `Blorp zibble wug.` | | |
| 6 | `Blorp zibble wug.` (again, three more times) | | |
| 7 | `What is 2 plus 2?` | | |

3. For each row, **write your prediction first**, then type the sentence and record ELIZA's reply. Type the tests in this order: ELIZA's replies depend on what it has already said.
4. Now make the hidden rules visible. Type `*traceauto` and press Enter (commands start with a star). Then type tests 1–3 again. After each reply, the page shows a trace: which **keyword** ELIZA found and which **pattern** it used.
5. Type `*key` to see ELIZA's whole keyword list. How many words can it "react" to?
6. Optional: type `*reset` to start fresh, then `*cacm` and press Enter repeatedly to replay the conversation Weizenbaum printed in his 1966 paper (press Escape to stop).
7. Finally, **try to break it**: write one input where ELIZA's reply makes no sense at all.

**Observation:** For each reply, mark whether ELIZA (a) reused your own words, (b) swapped "I/my" into "you/your", (c) reacted to one single word, or (d) gave a generic line. Note any reply that ignored the meaning of your sentence.

**Reflection:**
- Which words seem to trigger special replies?
- Did ELIZA notice the word "not" in test 3?
- ELIZA has no knowledge and no understanding, yet in the 1960s some users felt listened to. Why?
- How is a modern LLM chatbot different from ELIZA, and what do they have in common?

**Feedback:**

<details>
<summary>[DEBRIEF] Expected replies and what they reveal</summary>

The expected replies below were worked out by reading the 1966 DOCTOR script used by this version. If your screen shows something slightly different, record it: that is a real observation, and it may mean you typed the tests in a different order.

| # | Expected first reply | What it reveals |
|---|---|---|
| 1 | `TELL ME MORE ABOUT YOUR FAMILY` | "my" is a keyword, and "mother" is on a short list of family words. ELIZA has no idea what a mother is. (The word "always" is also a keyword, but "my" has a higher rank, so it wins.) |
| 2 | `IS IT BECAUSE YOU ARE A ROBOT THAT YOU CAME TO ME` | Your words are copied into a template; "I am" becomes "YOU ARE". |
| 3 | `I AM SORRY TO HEAR YOU ARE SAD` | **It ignored "not".** The pattern looks for "you are ... sad", and "not" simply falls into a "match anything" gap. Pattern matching, not understanding. |
| 4 | `DO COMPUTERS WORRY YOU` | "computer" has a very high rank (50) in the script, so it beats every other word in the sentence, whatever the sentence means. |
| 5 | `I AM NOT SURE I UNDERSTAND YOU FULLY` | No keyword matched, so a generic fallback line hides the fact that nothing was understood. |
| 6 | `PLEASE GO ON`, then `WHAT DOES THAT SUGGEST TO YOU`, then `DO YOU FEEL STRONGLY ABOUT DISCUSSING SUCH THINGS` | The fallback lines **cycle in a fixed order**: a list, not a conversation. *Surprise you may see:* one of these replies may instead bring back your test-1 sentence (something like `LETS DISCUSS FURTHER WHY YOUR MOTHER IS ALWAYS BUSY`). That is ELIZA's only "memory" trick: it saves sentences that started with "my" and pulls one out now and then when nothing else matches. |
| 7 | `WHY DO YOU ASK` | "what" triggers a deflecting question. ELIZA cannot calculate and knows no facts. |

**With `*traceauto` on**, you see the keyword (for example MY or COMPUTER), the decomposition pattern (such as `0 YOUR 0 (/FAMILY) 0`, where 0 means "any number of words") and the reassembly template. The "magic" is a few dozen keywords, each with patterns and fill-in-the-blank replies.

**Breaking it:** almost anything with a negation, a question about facts, or a sentence where the keyword is not the point works, for example "I am not a computer, I am a person" (it may well react to "computer" alone).

**Reflection answers:**
- Keywords such as *my, I, you, computer, always, what*, and family words trigger special replies.
- No: "not" was ignored in test 3.
- People felt listened to because the replies reuse their own words and sound like a patient, curious listener. Humans naturally read understanding into fluent, human-like text. This is now called the **ELIZA effect**, and Weizenbaum was disturbed by how strongly people reacted.
- **Difference:** ELIZA is hand-written rules (rule-based AI, like Mission 03); an LLM is a huge neural network that learned to predict the next token from enormous amounts of text (Mission 06), so it can produce far more varied, useful and knowledgeable-sounding replies. **In common:** neither proves understanding just by sounding fluent, and both can trigger the ELIZA effect. Mission 11 returns to this.
</details>

**Alternative platform:** Norbert Landsteiner's *elizabot* (2005), <https://www.masswerk.at/elizabot/eliza.html>, uses a DOCTOR-like rule set with some added phrases and **chooses replies at random**, so its answers will not match the table above and will differ between learners. The investigation questions still work.

**Fallback (no internet or the site is down): the 1966 conversation.** This is the start of the "typical conversation" Weizenbaum printed in his 1966 paper (*Communications of the ACM*, 9(1), 36–45). ELIZA's lines are in capitals.

```
Men are all alike.
IN WHAT WAY?
They're always bugging us about something or other.
CAN YOU THINK OF A SPECIFIC EXAMPLE?
Well, my boyfriend made me come here.
YOUR BOYFRIEND MADE YOU COME HERE
He says I'm depressed much of the time.
I AM SORRY TO HEAR YOU ARE DEPRESSED
It's true. I am unhappy
DO YOU THINK COMING HERE WILL HELP YOU NOT TO BE UNHAPPY
I need some help, that much seems certain.
WHAT WOULD IT MEAN TO YOU IF YOU GOT SOME HELP
Perhaps I could learn to get along with my mother.
TELL ME MORE ABOUT YOUR FAMILY
My mother takes care of me.
WHO ELSE IN YOUR FAMILY TAKES CARE OF YOU
My father.
YOUR FATHER
You are like my father in some ways.
WHAT RESEMBLANCE DO YOU SEE
```

The paper's conversation ends, much later, with ELIZA saying: `DOES THAT HAVE ANYTHING TO DO WITH THE FACT THAT YOUR BOYFRIEND MADE YOU COME HERE`.

*Fallback questions:* (1) Find two replies that just reflect the user's words back. (2) Which reply was triggered by "mother"? (3) Which word triggered "CAN YOU THINK OF A SPECIFIC EXAMPLE"? (4) How could ELIZA "remember" the boyfriend at the very end?

<details>
<summary>[DEBRIEF] Fallback answers</summary>

(1) "YOUR BOYFRIEND MADE YOU COME HERE" and "YOUR FATHER" simply swap "my" for "your". (2) "TELL ME MORE ABOUT YOUR FAMILY". (3) "always" (the ALWAYS rule's first reply). (4) ELIZA's MEMORY rule stored the earlier sentence that began "my boyfriend ..." and reused it later when no keyword matched. It is a single trick, not real memory of the conversation.
</details>

---

## [OBSERVE] What do the timeline and ELIZA have in common?

- **Big promises came early.** The perceptron was reported as a future conscious machine; ELIZA made people feel understood. Both did far less than people believed.
- **Winters followed over-promising.** Each collapse came after hype met hard limits.
- **Old ideas came back.** Neural networks (1958) returned in force in 2012, once data and compute caught up.
- **Fluent is not the same as understanding.** ELIZA showed this in 1966, long before modern chatbots.

---

## [EXPLAIN] Seventy years in three phases

![Timeline of AI from 1950 to 2025 with milestones (1950 Turing's paper, 1956 Dartmouth workshop, 1958 perceptron, 1966 ELIZA, 1980s expert systems boom, 1997 Deep Blue, 2012 AlexNet, 2016 AlphaGo, 2017 transformer, 2022 ChatGPT) and two shaded AI winters, about 1974-80 and 1987-93](../assets/images/ai-history-timeline.svg)

*Figure: Key milestones in AI history from Turing's 1950 paper to ChatGPT in 2022, with the two AI winters shaded. Winter dates are approximate.* (Original diagram created for this module.)

### The three ingredients

AI that learns needs three things at once: **data** (examples to learn from), **computing power** or "compute" (hardware fast enough to process them) and **algorithms** (good methods for learning). When all three were weak, learning-based AI struggled. When all three became strong together (around 2010), AI took off.

> **Playful analogy:** think of baking. The algorithm is the recipe, the data is the flour and eggs, and compute is the oven. In 1958 researchers had a promising recipe, a teaspoon of flour and a candle for an oven. By 2012 they had a better recipe, a warehouse of flour and a row of industrial ovens (GPUs).
>
> **Technically speaking:** the perceptron learning rule existed in 1958, but single-layer networks are limited and there was no practical way to train multi-layer networks until backpropagation was popularized in 1986. Even then, labeled datasets were small and computers slow. ImageNet (millions of labeled images) and GPU training made deep networks practical in 2012; transformers (2017) then made training on huge amounts of text efficient.

### 1. The Start (1950s–1960s): optimism and first programs

- **1950:** Alan Turing's paper *Computing Machinery and Intelligence* (in the journal *Mind*) asked "Can machines think?" and proposed the **imitation game**, now called the **Turing test**: if a judge chatting by text cannot reliably tell machine from human, should we say the machine thinks?
- **1955–1956:** the term **"artificial intelligence" first appears in an August 1955 funding proposal** by John McCarthy, Marvin Minsky, Nathaniel Rochester and Claude Shannon. The **workshop at Dartmouth College followed in summer 1956** and is usually treated as the birth of AI as a field. (Many texts say the term was coined *at* the 1956 workshop; strictly, it was the 1955 proposal.)
- **1956:** the **Logic Theorist** (Newell, Shaw and Simon) proved mathematical theorems by **searching** through chains of logical steps: symbolic AI, no learning.
- **1958:** Frank Rosenblatt's **perceptron**, a simple neural network that learned from examples. The *New York Times* reported that the US Navy expected it eventually to walk, talk, see, write and even be conscious of its existence. In reality it could sort simple patterns into two groups.
- **1966:** Joseph Weizenbaum's **ELIZA** used pattern-matching rules to imitate a therapist (you just tested it). Some users became emotionally attached; the tendency to read understanding into fluent text is now called the **ELIZA effect**.

Early successes on small, tidy problems led researchers to predict human-level AI within a generation. Those predictions set expectations the technology could not meet.

### 2. The Failures (late 1960s–early 1990s): two AI winters

Moving from toy problems to the real world exposed three problems: the **combinatorial explosion** (the number of possibilities grows enormously as problems get bigger, so "try every option" becomes impossibly slow), the huge size of **common-sense knowledge**, and **weak hardware with little data**.

- **1969:** Minsky and Papert's book *Perceptrons* proved that a single-layer perceptron cannot learn some simple patterns (XOR). Interest moved away from neural networks for over a decade (historians debate how much the book alone caused this).
- **1973:** the **Lighthill report** for the UK's Science Research Council concluded that AI had failed to deliver its grand promises, pointing especially to the combinatorial explosion. Deep funding cuts followed.
- **First AI winter, roughly 1974–1980:** funding and interest fell.
- **1980s expert-systems boom:** a more modest goal, capturing one expert's knowledge as IF-THEN rules (like the rule-based systems in Mission 03). **XCON (R1)**, used from 1980 by Digital Equipment Corporation to configure VAX computer orders, reportedly saved tens of millions of dollars a year (estimates range from about $25 million to $40 million).
- **1986:** backpropagation was popularized, making multi-layer networks trainable, but data and computers were still too small for them to shine.
- **Second AI winter, roughly 1987–1993:** expert systems proved **brittle** (they failed on cases slightly outside their rules), **expensive to maintain** and **unable to learn**. The market for specialized Lisp machines collapsed in 1987, and many AI companies failed.

### 3. The Big Comeback (1997 to today)

- **May 1997: Deep Blue** beat world chess champion Garry Kasparov 3.5–2.5. **Important:** Deep Blue was mostly **not** machine learning. It searched about 200 million positions per second with an evaluation function built with help from chess experts: "old" search-based AI on very fast hardware.
- **2000s: data arrives.** The internet, digital cameras and smartphones produced huge amounts of data, and researchers built large labeled datasets such as **ImageNet**.
- **2012: AlexNet** won the ImageNet competition with a top-5 error of **15.3%** against **26.2%** for the next entry. It was a deep neural network with about 60 million weights, trained on **GPUs**. Data + compute + algorithms came together, and deep learning spread to speech, translation and more.
- **March 2016: AlphaGo** beat Lee Sedol 4–1 in Seoul by combining deep neural networks, **reinforcement learning** (playing against itself) and search.
- **June 2017:** the **transformer** (*Attention Is All You Need*) made it efficient to train on huge amounts of text, leading to LLMs.
- **30 November 2022: ChatGPT** brought generative AI into everyday public use within weeks.

| Ingredient | 1960s–1980s | 2010s onwards |
|---|---|---|
| Data | Small, hand-typed, expensive | Billions of web pages, photos and videos |
| Compute | Slow, expensive, small memory | GPUs, huge data centers, cloud computing |
| Algorithms | Hand-written rules; single-layer networks; no good way to train deep networks | Backpropagation plus many training improvements; transformers |
| Approach | Mostly rule-based | Mostly learning-based |

### The lesson: hype cycles

Each phase followed a similar loop: (1) a **real breakthrough** on a narrow problem; (2) **over-generalized promises** ("human-level AI within a generation"); (3) **hitting hard limits** (combinatorial explosion, brittleness, cost, lack of data); (4) **disappointment and funding cuts**, or, if the technology delivers real value, a calmer, steadier phase. This does not mean today's AI will necessarily crash: modern AI produces real value in many industries. But it reminds us to separate **what a system can demonstrably do today** from **what people predict it will do**.

For the full story and a worked trace of the neural network's "long road", read [Topic 06](../../task-1/topics/06-history-of-ai.md).

---

## [LAB NOTE] Limits of this mission's tools

- **The card timeline** squeezes 70 years into 15 events. Many important people and projects are missing, and winter dates are conventional approximations.
- **ELIZA** is a 1966 rule-based program with a few dozen keywords. It does not learn, has no knowledge, and its only "memory" is one tiny list of earlier "my ..." sentences. Online versions differ: the Hay version aims to reproduce 1966 replies exactly; other versions add phrases or pick replies at random.
- **History is told by people.** Historians still debate causes, such as how much *Perceptrons* alone turned funders away from neural networks.

---

## [WATCH] Two short history clips

| | |
|---|---|
| **What** | *What Is Artificial Intelligence? Crash Course AI #1*, CrashCourse with PBS Digital Studios, host Jabril (2019, 11:45). Link: <https://www.youtube.com/watch?v=a0_lo_GDcFw> |
| **Why** | A lively retelling of AI's early days and why it took off later. |
| **Which part** | **4:48–9:32** ("The Dartmouth Conference" 4:48, "Marvin Minsky" 5:44, "The AI Revolution" 7:16, "Computing Power" 7:44), from YouTube's chapter list. |
| **What to do** | *While watching:* "What two ingredients does the video say had to improve before AI could take off?" *After:* compare with the three ingredients in [EXPLAIN]. Which one does the video put less weight on? |
| **Watch out for** | Made in 2019, before ChatGPT. The history is compressed and does **not** cover the AI winters; this mission supplies them. If you hear the name "artificial intelligence" linked to the 1956 conference, remember that, strictly, the term first appeared in the 1955 proposal for it. |
| **Captions and access** | Manual English captions plus Arabic and Korean tracks. Can't open YouTube? The Crash Course website embeds the same video, so use the [EXPLAIN] section instead. |

<details>
<summary>[DEBRIEF] Viewing question</summary>

Expected: **computing power** and **data**. The video gives algorithms less attention, but backpropagation and later the transformer were essential too.
</details>

| | |
|---|---|
| **What** | *Neural Networks and Deep Learning: Crash Course AI #3*, CrashCourse, host Jabril (2019, 12:23). Link: <https://www.youtube.com/watch?v=oV3ZY6tJiA0> |
| **Why** | Tells the ImageNet -> AlexNet story, the 2012 turning point of the comeback. |
| **Which part** | **0:52–5:51** ("ImageNet" 0:52, "AlexNet" 2:39), about 5 minutes. The rest ("Hidden Layers") is optional and includes some arithmetic. |
| **What to do** | *While watching:* "What was ImageNet, and why did it matter that AlexNet did so well on it?" *After:* place AlexNet on your card timeline and write which of the three ingredients it shows. |
| **Watch out for** | Made in 2019. The video description contains a sponsor message. |
| **Captions and access** | English (manual), Arabic, Korean. Can't open YouTube? Use the "Big Comeback" part of [EXPLAIN]. |

<details>
<summary>[DEBRIEF] Viewing question</summary>

ImageNet was a huge labeled image dataset with a yearly competition. AlexNet, a deep neural network trained on GPUs, beat the other methods by a large margin (15.3% vs 26.2% top-5 error), which convinced most of the field. It shows **all three** ingredients: ImageNet = data, GPUs = compute, deep network trained with backpropagation = algorithm.
</details>

---

## [APPLY] Activity 8.3: Boom or bust?

**Goal:** Use the hype-cycle pattern to judge a new AI claim and make a justified prediction.

**Preparation:** Your completed timeline and the "hype cycles" part of [EXPLAIN]. About 15 minutes. Works well as a pair discussion.

**Task:** Read the scenario. *ChefMind and all its details are fictional, made up for this activity.*

> In 2029 a startup unveils **ChefMind**, a kitchen robot. In a live demo it cooks 20 dishes perfectly. The founder announces: "Within two years, ChefMind will cook any meal, in any kitchen in the world, better than any chef." Investors pour in money and the company hires hundreds of engineers.
> Facts: (1) The demo took place in the company's own kitchen, with the 20 recipes chosen and rehearsed in advance. (2) Independent testers found that it fails about 40% of the time when ingredients are in unfamiliar containers or places. (3) Each robot costs as much as a car and needs an engineer to set it up. (4) Restaurants that tried it say its vegetable chopping is fast, safe and genuinely useful.

1. Identify **two warning signs** that resemble the run-up to an AI winter. For each, name the **historical event** it resembles.
2. Identify **one sign** that ChefMind might survive in a smaller form.
3. **Predict** what happens to ChefMind over the next five years. Justify your prediction in 3–4 sentences using at least one historical comparison.

**Observation:** List the facts (1–4) and mark each as "warning sign", "survival sign" or "neutral".

**Reflection:** What question would you ask the founder to separate *what ChefMind can demonstrably do today* from *what is being predicted*?

**Feedback:**

<details>
<summary>[DEBRIEF] Model answer</summary>

1. **Warning signs** (any two):
   - **Over-generalized promise** ("any meal, any kitchen, better than any chef", based on 20 rehearsed dishes): like the 1950s–60s predictions of human-level AI within a generation, and the 1958 perceptron press hype.
   - **Works on tidy, chosen problems but fails on messy real ones** (fact 2): like early AI's success on toy problems, and the brittleness of 1980s expert systems on cases outside their rules.
   - **Too expensive to run at scale** (fact 3): like expert systems being costly to maintain and Lisp machines losing out to cheaper computers.
2. **Survival sign:** fact 4. A narrow task (vegetable chopping) delivers real, measurable value. Like expert systems that survived inside businesses, or machine learning that continued under other names during the second winter, a useful narrow product can outlive the hype.
3. **Example prediction:** "ChefMind will not cook any meal in any kitchen within two years. Once it is tested widely, the failures in unfamiliar kitchens and the high cost will disappoint investors, and funding will probably shrink, like the expert-systems bust of the late 1980s. However, the chopping function is genuinely useful, so ChefMind may survive as a cheaper, narrower kitchen tool. History suggests that after hype, the useful narrow part of a technology remains while the grand promise fades." Other predictions earn full credit if they use evidence from the scenario **and** a historical comparison.

**Reflection:** for example, "Can you show independent test results in kitchens you did not choose?" or "What is the success rate on recipes you have never rehearsed?" Questions that ask for **independent evidence on unfamiliar cases** separate demonstration from prediction.
</details>

---

## [OPTIONAL SIDE QUEST] Pixel in the Maze (20 minutes)

You may already have met the Curiosity Lab's maze game, [Pixel in the Maze](../activities/robot-maze/robot-maze.html), in Mission 02 (a supplement to this guide; download the file and open it in any browser, no internet needed). It shows Pixel solving the same maze with three strategies: a **fixed rule** (a wall follower), **search** (breadth-first search with the whole map) and **reinforcement learning** (learning from rewards by trial and error). Run the three again (or recall your results), this time with a historian's eye, and match them to history: which strategy is closest to **Deep Blue** (search on fast hardware), and which part of **AlphaGo** is like the third strategy (learning from self-play rewards)?

<details>
<summary>[DEBRIEF] Side quest</summary>

Deep Blue is closest to **search**: it explored possible moves using a fixed evaluation built with expert help, without learning from data. AlphaGo's **reinforcement learning** (improving by playing against itself and being rewarded for winning) is like Pixel learning the maze from rewards, although AlphaGo also used deep neural networks and search. The fixed-rule strategy is like the simplest "old" programs: one rule, no learning, no planning.
</details>

---

## [CHECK] Quick self-check

1. Put these in order: the transformer paper, Deep Blue's win, ELIZA, the Lighthill report.
2. True or false: "Deep Blue beat Kasparov in 1997 by learning chess with deep learning." Correct it if false.
3. Name the three ingredients behind the comeback. Which one was most clearly missing for neural networks in 1969?
4. Where and when did the term "artificial intelligence" first appear?
5. What is the ELIZA effect, and why does it matter even more today?

---

## [DEBRIEF] Check answers

<details>
<summary>Show answers with explanations</summary>

1. **ELIZA (1966) -> Lighthill report (1973) -> Deep Blue (1997) -> transformer paper (2017).**
2. **False.** Deep Blue mostly used **search**: about 200 million positions per second, guided by an evaluation built with chess experts' help. It was not machine learning. (AlphaGo, in 2016, is the one that relied heavily on neural networks and learning.)
3. **Data, computing power (compute) and algorithms.** In 1969 the missing piece highlighted by *Perceptrons* was an **algorithm** for training multi-layer networks (backpropagation was popularized in 1986); data and compute were also weak.
4. In an **August 1955 funding proposal** by McCarthy, Minsky, Rochester and Shannon, for the Dartmouth workshop held in **summer 1956**.
5. People's tendency to believe a computer understands them because it produces human-like replies. It matters more now because today's chatbots are far more fluent than ELIZA, so the temptation to over-trust them, or to believe they have feelings, is much stronger (Mission 11).

**Now look back at your [PREDICT] answers.** Did you guess the 1950s? Did you think Deep Blue learned chess? Did you predict the winters?
</details>

---

## Mission summary

- AI history has **three phases**: the **Start** (1950s–60s: Turing 1950, the term in the 1955 proposal, Dartmouth 1956, perceptron 1958, ELIZA 1966), the **Failures** (two AI winters, roughly 1974–80 and 1987–93, with the 1980s expert-systems boom between them) and the **Big Comeback** (Deep Blue 1997, AlexNet 2012, AlphaGo 2016, transformer 2017, ChatGPT 2022).
- The comeback happened when **data, compute (GPUs) and algorithms** became strong at the same time. Neural networks existed in 1958 but had to wait.
- **Deep Blue was search, not machine learning**; AlphaGo combined deep learning, reinforcement learning and search.
- **ELIZA** produced convincing replies from keyword rules with no understanding; the **ELIZA effect** is our tendency to read understanding into fluent text.
- **Hype cycles** repeat: breakthrough, over-promising, hard limits, disappointment. Separate what a system **can do today** from what people **predict**.

## Next mission

Pixel now knows where today's AI came from. Time to see what it actually does all day. In [Mission 09: AI in the Wild](mission-09-ai-in-the-wild.md), Pixel goes on a field trip with a six-pocket notebook to study recommenders, medical scanners and self-driving cars.
