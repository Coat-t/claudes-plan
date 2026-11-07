# 06: The History and Evolution of AI

**Module:** AI Overview · **Version:** 2.0 · **Status:** drafted (self-checked) · **Last updated:** 2026-11-06

## Learning goals

After this topic, you should be able to:

- **Place** at least ten key AI milestones (1950 to 2022) in the correct order and give the approximate date of each.
- **Distinguish** the three main phases of AI history: the Start (1950s–1960s), the Failures (the two "AI winters"), and the Big Comeback (1997 onwards).
- **Explain** the causes of each AI winter (over-promising, technical limits, cost) and of each comeback (data, computing power, better algorithms).
- **Trace** how one idea, the artificial neural network, fell out of favor and later returned to dominate AI.
- **Apply** the boom-and-bust pattern to judge whether a new AI claim shows warning signs of hype.

## Prerequisites

- [Topic 01: What is AI?](01-what-is-ai.md): the definition of AI and the "AI effect".
- [Topic 02: How AI operates](02-how-ai-operates.md): rule-based ("old") AI versus learning-based ("new") AI, and search.
- [Topic 03: ML, neural networks and deep learning](03-ml-neural-networks-deep-learning.md): what a neural network, training and deep learning are.
- [Topic 04: Generative AI and LLMs](04-generative-ai-and-llms.md): helpful for the last part of the timeline (transformer, ChatGPT), but not essential.

## Key terms

| Term | Plain-English definition |
|---|---|
| Turing test (imitation game) | A test proposed by Alan Turing in 1950: if a judge chatting by text cannot reliably tell a machine from a human, should we say the machine "thinks"? |
| Symbolic AI | "Old" AI that works by manipulating symbols with human-written rules and logic, e.g. "IF fever AND rash THEN consider measles". Also called rule-based AI or GOFAI ("good old-fashioned AI"). |
| Perceptron | An early, single-layer artificial neural network (1958) that could learn simple yes/no classifications from examples. |
| Expert system | A rule-based program that stores the knowledge of human experts as hundreds or thousands of IF–THEN rules, e.g. to configure computers or suggest diagnoses. |
| AI winter | A period when funding, business interest and public enthusiasm for AI fell sharply, usually after promises were not met. |
| Combinatorial explosion | The problem that the number of possibilities to check grows enormously as a problem gets bigger, so "try every option" methods become impossibly slow. |
| Backpropagation | A training method that tells every weight in a multi-layer neural network how to change to reduce the error. It made deep networks trainable. |
| Benchmark / dataset | A shared collection of examples (e.g. labeled images) used to train and compare AI systems. |
| GPU (graphics processing unit) | A computer chip originally designed for video-game graphics that turned out to be very good at the many simple calculations neural networks need. |
| Transformer | A neural-network design introduced in 2017 that uses "attention" to process whole sequences of tokens at once. It is the basis of today's large language models (LLMs). |
| Hype cycle | The repeating pattern of excitement, inflated promises, disappointment and (sometimes) steady recovery that new technologies often go through. |

## Explanation

### 1. Why study AI history at all?

AI is not a sudden invention of the 2020s. Researchers have been trying to build "thinking machines" for more than 70 years. Their story has a clear shape: **big promises, then disappointment, then a slower and more solid comeback**, and this happened more than once. Knowing this pattern helps you judge today's headlines. When someone says "AI will be able to do everything in five years", you can ask: *has a prediction like this been made before, and what happened?*

The history also explains *why* modern AI looks the way it does. Today's chatbots are built on neural networks, an idea from the 1950s that was nearly abandoned in the 1970s and only became dominant after 2012. To understand why, we need three ingredients that come up again and again:

1. **Data**: examples for a system to learn from.
2. **Computing power** (compute): fast enough hardware to process those examples.
3. **Algorithms**: good methods for learning from the data.

When all three were weak, learning-based AI struggled. When all three became strong at the same time (around 2010), AI took off.

We will tell the story in three phases: **The Start**, **The Failures** and **The Big Comeback**.

### 2. The Start (1950s–1960s): optimism and first programs

**1950: Alan Turing asks "Can machines think?"** The British mathematician Alan Turing published a paper called *Computing Machinery and Intelligence* in the journal *Mind* in 1950. Instead of arguing about what "thinking" means, he proposed a practical test he called the **imitation game**, now known as the **Turing test**: a human judge types questions to two hidden players, one human and one machine. If the judge cannot reliably tell which is the machine, Turing suggested we have good reason to call the machine intelligent. The paper also predicted that machines might one day *learn*, like a child, rather than be programmed with every fact.

**1955–1956: the name "artificial intelligence" and the Dartmouth workshop.** In August 1955 four researchers (John McCarthy, Marvin Minsky, Nathaniel Rochester and Claude Shannon) wrote a funding proposal for a "summer research project on artificial intelligence". This proposal is where the term **"artificial intelligence"** first appears. Its central idea was bold: that "every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it." The workshop itself took place at Dartmouth College in New Hampshire, USA, in the **summer of 1956**. It is usually treated as the birth of AI as a research field.

> **Correction note:** Many texts (including our earlier draft) say McCarthy "coined the term at the 1956 workshop". More precisely, the term was coined in the **1955 proposal**, and the workshop followed in 1956.

**1956: the Logic Theorist.** Allen Newell, Cliff Shaw and Herbert Simon built the **Logic Theorist**, often called the first AI program. It proved mathematical theorems by **searching** through possible chains of logical steps (exactly the kind of search you met in [Topic 02](02-how-ai-operates.md)). In runs reported in 1957 it proved 38 of the first 52 theorems in chapter 2 of the famous mathematics book *Principia Mathematica*, and found one proof shorter than the original. This was **symbolic AI**: no learning, just rules and search.

**1958: the perceptron.** Frank Rosenblatt published a paper describing the **perceptron**, a simple artificial neural network that *learned* from examples by adjusting its weights (see [Topic 03](03-ml-neural-networks-deep-learning.md)). This was the first big "learning-based" idea. The press got very excited: in July 1958 the *New York Times* reported that the US Navy expected the machine eventually to walk, talk, see, write and even be conscious of its own existence. It could, in reality, learn to sort simple patterns into two groups.

**1966: ELIZA.** Joseph Weizenbaum at MIT published a paper in 1966 about **ELIZA**, a program that held typed "conversations". Its most famous script, DOCTOR, imitated a therapist by turning the user's words back into questions (a simplified illustration of its style: "I feel sad" → "Why do you feel sad?"; the real script's replies depended on its keyword rules). ELIZA used simple pattern-matching rules and had no understanding at all, yet some users became emotionally attached to it. Weizenbaum was disturbed by this, and the effect of people reading understanding into fluent text is now sometimes called the **ELIZA effect**. It matters even more in the age of chatbots (see [Topic 09](09-limitations-and-misconceptions.md)).

**The mood of the time.** Early successes on small, tidy problems (logic puzzles, simple games, algebra) led researchers to predict that human-level AI was only a decade or two away. These predictions set expectations that the technology could not meet.

### 3. The Failures (late 1960s–early 1990s): two AI winters

**Why did early AI hit a wall?** Three problems appeared once researchers moved from toy problems to the real world:

1. **Combinatorial explosion.** Search works on a river-crossing puzzle with a few dozen states. Real problems (understanding a sentence, planning a day, playing a full board game) have astronomically many possibilities. Trying them all was far beyond the computers of the time.
2. **Common sense is huge.** Understanding even a simple story requires vast background knowledge ("people get wet in the rain", "you can't be in two places at once"). Nobody could write all of it down as rules.
3. **Weak hardware and little data.** Computers had tiny memories by modern standards, and there were no large digital datasets to learn from.

**1969: *Perceptrons*.** Marvin Minsky and Seymour Papert published a book, *Perceptrons*, that proved mathematically that a single-layer perceptron cannot learn certain simple patterns. The classic example is "exclusive OR" (XOR): output YES if exactly one of two inputs is on, but not both. Multi-layer networks could in principle solve this, but nobody yet had a good way to *train* them. The book is widely credited with turning researchers and funders away from neural networks for over a decade, although historians debate how much of the decline it caused on its own.

**1973: the Lighthill report.** The UK's Science Research Council asked the mathematician Sir James Lighthill to review AI research. His report, *Artificial Intelligence: A General Survey* (1973), concluded that AI had failed to deliver on its grand promises, and pointed especially to the combinatorial explosion. It was followed by deep cuts to AI funding in British universities. In the United States, funding agencies also became more demanding about practical, short-term results.

**The first AI winter (roughly 1974–1980).** Funding and interest fell. Dates vary between sources; the point is the pattern, not the exact year.

**The expert-systems boom (1980s).** AI recovered with a more modest goal: instead of general intelligence, capture *one expert's knowledge* in one narrow area as IF–THEN rules. Research systems such as MYCIN (Stanford, 1970s), which advised on antibiotics using roughly 600 rules (see [Topic 02](02-how-ai-operates.md)), had shown the idea could work in a lab. The best-known success was **R1, later called XCON**, developed by John McDermott at Carnegie Mellon University and used from 1980 by Digital Equipment Corporation (DEC) to configure orders for its VAX computers. Reported savings were in the tens of millions of dollars per year (estimates range from about $25 million to $40 million). Companies around the world built expert systems, and specialized "Lisp machine" computers were sold to run them. Japan launched a large national "Fifth Generation" computing project in 1982.

**Meanwhile, neural networks quietly returned.** In 1986 David Rumelhart, Geoffrey Hinton and Ronald Williams published a paper in *Nature* that popularized **backpropagation**, a way to train networks with hidden layers. (The mathematics had been discovered earlier by others; this paper made it widely known.) This solved the training problem that *Perceptrons* had highlighted, but computers and datasets were still too small for neural networks to beat other methods on most real tasks.

**The second AI winter (roughly 1987–1993).** Expert systems turned out to be:

- **Brittle**: they failed badly on any case slightly outside their rules.
- **Expensive to maintain**: every new product or situation needed experts and programmers to write and test new rules. XCON eventually needed thousands of rules.
- **Unable to learn**: they could not improve themselves from data.

In 1987 the market for specialized Lisp machines collapsed as ordinary desktop computers became powerful enough. Many AI companies failed, the Fifth Generation project ended without reaching its ambitious goals, and "AI" became an unfashionable word in business. Much useful work continued under other names, such as "machine learning", "data mining" or "decision support".

### 4. The Big Comeback (1997–today)

**1997: Deep Blue beats Kasparov.** In May 1997 IBM's chess computer Deep Blue defeated world champion Garry Kasparov 3.5–2.5 over six games in New York. (Kasparov had won their first match, in 1996, 4–2.) It was the first time a computer beat a reigning world champion in a match under standard tournament conditions. **Important:** Deep Blue was mostly *not* machine learning. It used special hardware to search about 200 million chess positions per second, guided by an evaluation function built with help from chess experts. It was a triumph of **search plus raw computing power**, i.e. "old" AI on very fast hardware.

**The 2000s: data arrives.** The internet, digital cameras and smartphones created enormous amounts of data. Researchers built large labeled datasets, most famously **ImageNet**, a collection of millions of labeled photos. Its annual competition (from 2010) asked systems to sort images into 1,000 categories after training on more than a million labeled examples. Statistical machine learning quietly powered spam filters, search engines and recommendation systems.

**2012: AlexNet and the deep-learning breakthrough.** Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton entered a deep neural network, later called **AlexNet**, in the 2012 ImageNet competition. Its top-5 error rate (the share of test images where the correct label was not among its five best guesses) was **15.3%**, compared with **26.2%** for the second-best entry. This huge margin convinced most of the field. AlexNet had about 60 million weights and was trained on **GPUs**. All three ingredients came together: **big data** (ImageNet), **compute** (GPUs) and **better algorithms** (backpropagation plus newer training tricks). From this point, deep learning spread to speech recognition, translation and much more.

**2016: AlphaGo beats Lee Sedol.** Go is a board game with far more possible positions than chess, so Deep Blue-style search alone could not master it. In March 2016 in Seoul, DeepMind's **AlphaGo** beat Lee Sedol, one of the world's strongest players, 4–1. AlphaGo combined deep neural networks with search. It first learned from many expert human games, then improved further by playing against versions of itself (**reinforcement learning**, see [Topic 03](03-ml-neural-networks-deep-learning.md)). Its "move 37" in game two surprised professional players because a human would almost never have played it.

**2017: the transformer.** A team at Google published *Attention Is All You Need*, introducing the **transformer**, a neural-network design that processes all the tokens of a text in parallel and uses "attention" to decide which other tokens matter for each one. Transformers could be trained efficiently on huge amounts of text, which led directly to large language models (LLMs).

**30 November 2022: ChatGPT.** OpenAI released ChatGPT as a free "research preview". It was an LLM fine-tuned to follow instructions and hold a conversation (see [Topic 04](04-generative-ai-and-llms.md)). It brought generative AI into everyday public use within weeks, and started the current wave of investment and debate.

### 5. What changed between the failures and the comeback?

| Ingredient | 1960s–1980s | 2010s onwards |
|---|---|---|
| Data | Small, hand-typed, expensive | Billions of web pages, photos and videos |
| Compute | Slow, expensive, small memory | GPUs and huge data centers; cloud computing |
| Algorithms | Hand-written rules; single-layer networks; no good way to train deep networks | Backpropagation plus many training improvements; transformers |
| Approach | Mostly **rule-based** (humans write the knowledge) | Mostly **learning-based** (the model learns from data) |

Notice that the big idea (neural networks that learn from examples) existed in 1958. It needed **data and compute** to catch up before it could work at scale.

### 6. The lesson: hype cycles

Every phase followed a similar loop:

1. **A real breakthrough** on a narrow problem (Logic Theorist, perceptron, XCON, ChatGPT).
2. **Over-generalized promises** ("human-level AI within a generation").
3. **Hitting hard limits** (combinatorial explosion, brittleness, cost, lack of data).
4. **Disappointment and funding cuts** (a "winter"), *or*, if the technology delivers real value, a calmer, steadier phase.

This does not mean today's AI will necessarily crash. Modern AI produces real economic value in many industries, which the 1970s systems did not. But the pattern reminds us to separate **what a system can demonstrably do today** from **what people predict it will do**.

## Worked example

**Tracing one idea through history: the long road of the neural network**

Goal: show how a single idea moved through all three phases, and why its fortunes changed each time. We trace it step by step, asking at each step: *What happened? Which ingredient was missing or newly present? What was the effect?*

| Step | Year | Event | Missing or new ingredient | Effect on neural-network research |
|---|---|---|---|---|
| 1 | 1958 | Rosenblatt's perceptron learns simple patterns from examples | New **algorithm** (a learning rule), but tiny data and compute | Boom: excitement and press hype |
| 2 | 1969 | *Perceptrons* proves single-layer networks cannot learn XOR | Missing **algorithm** for training multi-layer networks | Bust: funding and interest move to symbolic AI |
| 3 | 1986 | Backpropagation popularized | New **algorithm**: multi-layer networks can now be trained | Partial revival in research labs |
| 4 | 1990s–2000s | Networks work on small tasks (e.g. reading handwritten digits) but other methods often win | Still missing enough **data** and **compute** | Steady but niche |
| 5 | 2009–2012 | ImageNet dataset; GPUs used for training; AlexNet wins by a large margin | New **data** + new **compute**, combined with existing algorithms | Boom: deep learning becomes the main approach |
| 6 | 2017–2022 | Transformer; LLMs; ChatGPT | New **algorithm** (transformer) + even more data and compute | Neural networks dominate public attention |

**Reading the trace:** The same core idea was "failed" in 1969 and "triumphant" in 2012. The idea was not simply wrong in 1969; the other ingredients were not ready. This is why historians are careful about saying an approach "failed": sometimes it was early.

## Visual

![Timeline of AI from 1950 to 2025 with milestones (1950 Turing's paper, 1956 Dartmouth workshop, 1958 perceptron, 1966 ELIZA, 1980s expert systems boom, 1997 Deep Blue, 2012 AlexNet, 2016 AlphaGo, 2017 transformer, 2022 ChatGPT) and two shaded AI winters, about 1974-80 and 1987-93](../assets/images/ai-history-timeline.svg)

*Figure: Key milestones in AI history from Turing's 1950 paper to ChatGPT in 2022, with the two AI winters shaded. Winter dates are approximate.* (Original diagram created for this module.)

**Milestone table (the text version of the timeline)**

| Date | Milestone | Phase | Why it mattered |
|---|---|---|---|
| 1950 | Turing, *Computing Machinery and Intelligence* (imitation game) | Start | Framed the question "Can machines think?" and a way to test it |
| Aug 1955 | Dartmouth proposal (McCarthy, Minsky, Rochester, Shannon) | Start | First use of the term "artificial intelligence" |
| Summer 1956 | Dartmouth workshop | Start | Usually treated as the founding of AI as a field |
| 1956 (runs reported 1957) | Logic Theorist (Newell, Shaw, Simon) | Start | Early AI program; proved theorems by search |
| 1958 | Rosenblatt's perceptron | Start | First widely known learning neural network; heavy press hype |
| 1966 | Weizenbaum's ELIZA paper | Start | Rule-based chatbot; people read understanding into it |
| 1969 | Minsky & Papert, *Perceptrons* | Failures | Showed limits of single-layer networks; neural-network research declined |
| 1973 | Lighthill report (UK) | Failures | Criticized AI's unmet promises; UK funding cuts |
| ~1974–1980 | First AI winter | Failures | Reduced funding and interest |
| 1980 | XCON/R1 in use at DEC | Failures (boom within) | Commercial success of expert systems |
| 1986 | Backpropagation paper (Rumelhart, Hinton, Williams) | Failures (seeds of comeback) | Made multi-layer networks trainable |
| ~1987–1993 | Second AI winter | Failures | Expert systems brittle and costly; Lisp-machine market collapse |
| May 1997 | Deep Blue beats Kasparov 3.5–2.5 | Comeback | Search + fast hardware beats world chess champion |
| 2012 | AlexNet wins ImageNet (15.3% vs 26.2% top-5 error) | Comeback | Start of the deep-learning era |
| Mar 2016 | AlphaGo beats Lee Sedol 4–1 | Comeback | Deep learning + reinforcement learning + search masters Go |
| Jun 2017 | Transformer paper, *Attention Is All You Need* | Comeback | Architecture behind LLMs |
| 30 Nov 2022 | ChatGPT released | Comeback | Generative AI enters everyday use |

## Common mistakes

1. **"AI was invented recently, with ChatGPT."** Correction: the field was named in 1955, and chatbots go back to ELIZA in 1966. ChatGPT was a landmark in *public use*, built on decades of research.
2. **"Deep Blue learned to play chess like AlphaGo did."** Correction: Deep Blue relied mainly on hand-tuned evaluation and brute-force search (about 200 million positions per second). AlphaGo relied heavily on neural networks trained on data and self-play. They represent "old" and "new" AI respectively.
3. **"The AI winters happened because AI ideas were wrong."** Correction: some ideas were limited (single-layer perceptrons, brittle expert systems), but a major cause was **over-promising** relative to the data and computing power available. Neural networks, abandoned in the 1970s, became dominant once data and compute caught up.
4. **"McCarthy coined 'artificial intelligence' at the 1956 workshop."** Correction: the term appears in the **1955** proposal for the workshop.

## Try it yourself

### Activity 1: Order the milestones and explain the links (sequence + cause and effect)

The eight cards below are shuffled. **First try from memory**, then check against the milestone table.

- A. A rule-based program configures computer orders for a big company and saves it millions each year.
- B. A government-commissioned report says AI has not delivered on its promises; funding is cut.
- C. A deep neural network trained on GPUs wins an image-recognition competition by a huge margin.
- D. A paper proposes the "imitation game" to test whether machines can think.
- E. A book proves that single-layer perceptrons cannot learn certain simple patterns.
- F. A chess computer that searches 200 million positions per second beats the world champion.
- G. A new network design based on "attention" is published; it later powers LLMs.
- H. Specialized AI computers stop selling and many expert-system companies fail.

**Tasks:**
1. Put the cards in chronological order.
2. Label each card **Start**, **Failures** or **Comeback**.
3. Pick **two adjacent cards** and write one sentence explaining how the earlier event helped cause, or set up, the later one.

### Activity 2: Diagnose the winters and the comeback (explain + compare)

Use the explanation above. Copy and complete this table.

| Question | First AI winter (~1974–1980) | Second AI winter (~1987–1993) | Comeback after 2012 |
|---|---|---|---|
| What had been promised or hoped? | | | |
| What went wrong (or right)? | | | |
| Which of the three ingredients (data, compute, algorithms) was weak or strong? | | | |

Then answer: **What do the two winters have in common?** (2–3 sentences.)

### Activity 3: Boom or bust? (predict + justify)

The following scenario is **fictional** (made up for this activity).

> *"MindMesh", a startup, announces a new AI tutor in 2031. Its demo solves high-school maths problems perfectly. The founder says: "In three years, MindMesh will replace all teachers in every subject." Investors pour in money. Facts: (1) The demo used 50 problems chosen by the company. (2) Independent testers found it fails on about 30% of problems that are worded unusually. (3) Running it costs far more per student than the schools can pay. (4) Thousands of students who tried a free version say it is genuinely helpful for practicing algebra.*

1. Using the hype-cycle pattern from Section 6, identify **two warning signs** that resemble the run-up to an AI winter. Name the historical event each one resembles.
2. Identify **one sign** that MindMesh might survive in a smaller form instead of collapsing completely.
3. **Predict** what happens to MindMesh over the next five years, and justify your prediction in 3–4 sentences.

## Answers

<details>
<summary>Show answers</summary>

**Activity 1**

1. Order: **D** (1950, Turing) → **E** (1969, *Perceptrons*) → **B** (1973, Lighthill report) → **A** (1980, XCON at DEC) → **H** (1987, Lisp-machine collapse / second winter) → **F** (1997, Deep Blue) → **C** (2012, AlexNet) → **G** (2017, transformer).
2. Labels: D = Start; E, B, A, H = Failures (A is the expert-systems boom *inside* the Failures era, between the two winters); F, C, G = Comeback. Accept A labeled as "boom between winters". The key is recognizing it came before the second winter.
3. Example links (any accurate one is fine):
   - E → B: *Perceptrons* and other disappointments had already weakened confidence, so when the Lighthill report criticized AI's unmet promises, funders were ready to cut.
   - A → H: XCON's success started an expert-systems boom; when these systems proved brittle and costly to maintain, and the specialized hardware market collapsed, the boom turned into the second winter.
   - C → G: AlexNet showed deep neural networks trained on lots of data with GPUs work extremely well, which encouraged the research that produced new network designs like the transformer.

**Why:** Ordering checks recall, but the cause-and-effect sentence is the real goal: history is a chain of causes, not a list of dates.

**Activity 2** (model answer)

| Question | First AI winter | Second AI winter | Comeback after 2012 |
|---|---|---|---|
| Promised | Human-level reasoning, translation, general problem-solving within a generation | Expert systems in every business; Japan's Fifth Generation computers | (Less grand at first) better image, speech and language recognition |
| What went wrong / right | Combinatorial explosion; common-sense knowledge too large; Lighthill report; funding cuts | Systems brittle, costly to maintain, could not learn; Lisp-machine market collapsed | Deep learning delivered large, measurable improvements (e.g. AlexNet 15.3% vs 26.2%) and real products |
| Ingredients | Weak data, weak compute; algorithms for multi-layer networks missing | Learning not used much; knowledge hand-written; data and compute still limited | Strong data (ImageNet, internet), strong compute (GPUs), improved algorithms |

**In common:** Both winters followed promises that were much bigger than what the technology could deliver with the data, computing power and methods available. In both cases systems worked on narrow, tidy problems but broke when faced with messy real-world complexity, and funders withdrew when results did not match the hype.

**Activity 3** (model answer)

1. Warning signs (any two):
   - **Over-generalized promise**: "replace all teachers in every subject" from a maths demo resembles the 1950s–60s predictions of human-level AI within a generation, and the 1958 perceptron press hype.
   - **Works on tidy, chosen problems but fails on unusual ones** (30% failure on unusually worded problems): resembles brittleness of expert systems before the second winter, and early AI's success on toy problems.
   - **Too expensive to run at scale**: resembles expert systems being too costly to maintain, and Lisp machines losing out to cheaper computers.
2. Survival sign: users find genuine, measurable value in a **narrow** task (algebra practice). Like expert systems that survived inside businesses, or machine learning that continued under other names, a narrow useful product can outlive the hype.
3. Example prediction: "MindMesh will not replace all teachers. When schools test it widely, the failures on unusual problems and the high cost will disappoint investors, and funding will probably shrink. However, because students find it helpful for algebra practice, it may survive as a cheaper, narrower practice tool used alongside teachers. This matches history: after hype, the useful narrow part of a technology tends to remain while the grand promise fades." (Accept other predictions if they are justified with evidence from the scenario and a historical comparison.)

</details>

## Optional extension

*Optional: not required for the core module.*

- Read the opening section ("The Imitation Game") of Turing's 1950 paper (link in Sources). Turing listed objections people might raise against thinking machines and replied to each. Pick one objection and decide whether it applies to today's chatbots.
- Research the "ELIZA effect" and write three sentences on why it matters more now than in 1966.
- Look up what happened to AI after AlphaGo: AlphaGo Zero (2017) learned Go without any human games. What does that suggest about the role of human data?

## Connections

- **Back to [Topic 02](02-how-ai-operates.md):** the Logic Theorist and Deep Blue are rule-based/search systems; the perceptron, AlexNet and AlphaGo are learning-based.
- **Back to [Topic 03](03-ml-neural-networks-deep-learning.md):** the perceptron is the single artificial neuron you studied; backpropagation is how multi-layer ("deep") networks are trained.
- **Back to [Topic 04](04-generative-ai-and-llms.md):** the transformer and ChatGPT are the direct ancestors of today's LLMs.
- **Forward to [Topic 07](07-real-world-applications.md):** the comeback is why AI now appears in recommendations, healthcare and transport.
- **Forward to [Topic 09](09-limitations-and-misconceptions.md) and [Topic 10](10-future-of-ai.md):** the hype-cycle lesson helps you evaluate claims about AGI and AI taking all jobs.

## Sources

1. Turing, A. M. (1950). Computing Machinery and Intelligence. *Mind*, 59(236), 433–460. https://academic.oup.com/mind/article/LIX/236/433/986238 (accessed 2026-11-06). Supports: 1950 date, journal, the "imitation game".
2. Dartmouth College. *Artificial Intelligence (AI) Coined at Dartmouth*. https://home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth (accessed 2026-11-06). Supports: 1956 summer research project at Dartmouth organized by McCarthy; the "every aspect of learning..." conjecture. (The 31 August 1955 date of the proposal by McCarthy, Minsky, Rochester and Shannon is from the well-known proposal document; the original PDF at jmc.stanford.edu could not be fetched due to a certificate error.)
3. Wikipedia contributors. *Logic Theorist* (and search summary of Shrager, J. (2026), arXiv:2603.13514). https://en.wikipedia.org/wiki/Logic_Theorist (accessed 2026-11-06, via search result). Supports: Newell, Shaw and Simon; 38 of the first 52 theorems of *Principia Mathematica* ch. 2; 1956 program, runs reported 1957.
4. Rosenblatt, F. (1958). The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain. *Psychological Review*, 65(6), 386–408. Verified via search results (citation and July 1958 *New York Times* coverage), accessed 2026-11-06.
5. Weizenbaum, J. (1966). ELIZA: A computer program for the study of natural language communication between man and machine. *Communications of the ACM*, 9(1), 36–45. Hosted copy: https://courses.cs.umbc.edu/331/papers/eliza.html (verified via search result, accessed 2026-11-06). Supports: ELIZA, 1966 publication, DOCTOR script.
6. Minsky, M. & Papert, S. (1969). *Perceptrons: An Introduction to Computational Geometry*. MIT Press. Verified via search results (accessed 2026-11-06). Supports: 1969 date, single-layer limitation (XOR), debated role in the decline of neural-network research.
7. Lighthill, J. (1973). Artificial Intelligence: A General Survey. In *Artificial Intelligence: A Paper Symposium*. Science Research Council. Summary: https://en.wikipedia.org/wiki/Lighthill_report (verified via search result, accessed 2026-11-06). Supports: 1973 report, combinatorial explosion criticism, UK funding cuts.
8. Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 1 (history of AI). Pearson. Known stable reference (not fetched). Supports: overall narrative of early optimism, AI winters, expert-systems boom (R1/XCON), return of neural networks.
9. Wikipedia contributors. *Xcon* and course notes "Configuration with R1/XCon". https://en.wikipedia.org/wiki/Xcon ; https://cwa.mdx.ac.uk/bis2040/lect6ES2/xCon.html (verified via search results, accessed 2026-11-06). Supports: McDermott, CMU, DEC use from 1980 for VAX configuration; savings estimates (~$25M/year; higher estimates also reported).
10. Rumelhart, D. E., Hinton, G. E. & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, 323, 533–536. https://ui.adsabs.harvard.edu/abs/1986Natur.323..533R/abstract (verified via search result, accessed 2026-11-06). Supports: 1986 popularization of backpropagation.
11. IBM. *Deep Blue* (IBM History). https://www.ibm.com/history/deep-blue (fetched, accessed 2026-11-06). Supports: May 1997, 3.5–2.5, 1996 match 4–2 to Kasparov, 200 million positions per second.
12. Krizhevsky, A., Sutskever, I. & Hinton, G. E. (2012). ImageNet Classification with Deep Convolutional Neural Networks. *NeurIPS 25*. https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks (fetched, accessed 2026-11-06). Supports: 60 million parameters, GPU training; ILSVRC-2012 15.3% vs 26.2% top-5 error (confirmed via search of the abstract).
13. Google DeepMind. *AlphaGo*. https://deepmind.google/research/breakthroughs/alphago/ (fetched, accessed 2026-11-06). Supports: March 2016, Seoul, 4–1, move 37, learning from human games and self-play.
14. Vaswani, A. et al. (2017). Attention Is All You Need. arXiv:1706.03762. https://arxiv.org/abs/1706.03762 (fetched, accessed 2026-11-06). Supports: transformer, June 2017, attention without recurrence.
15. OpenAI (2022). *Introducing ChatGPT*, 30 November 2022. https://openai.com/index/chatgpt/ (page returned 403; date verified via multiple search results, accessed 2026-11-06). Supports: release date, research preview.
