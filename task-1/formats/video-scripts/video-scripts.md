# AI Overview: Video Tutorial Scripts (one per topic)

**Module:** AI Overview · **Version:** 1.0 · **Last updated:** 2026-11-06 · **Adapted from:** topic files Version 2.0 in [../../topics/](../../topics/)

**Back to:** [Formats README](../README.md) · [Slide outlines](../slides/slide-outlines.md) · [Module outline](../../00-module-outline.md)

## How to use these scripts

- Each script is a **3 to 5 minute tutorial** built on a **step-by-step demonstration** of the topic's worked example. Videos do not replace the topic file; they show one process in motion. Concepts are explained in full in the topic files and the study guide.
- Each script is split into **numbered segments**. Every segment gives: the **time range**, what is **on screen**, the **narration** (to be read word for word, about 145 words per minute) and a **pause / predict** prompt where the viewer should stop the video and think. Pause prompts show the on-screen text "Pause and predict" for about 5 seconds; the answer is given in the next segment's narration.
- The topic file is the **authoritative source**: every definition, number and example below comes from it. If you find an error, fix the topic file first, then this file (see the [consistency rule](../README.md#the-consistency-rule)). Numbers labeled *illustrative (made-up)* in the topic files are said aloud as "made-up numbers" in the narration and shown with that label on screen.
- Diagram paths are relative to this file: `../../assets/images/<file>.svg`.

## Accessibility notes (apply to every video)

- **Captions:** publish closed captions for every video, produced from the narration below (not only automatic captions), and offer the narration as a downloadable transcript.
- **Describe visuals verbally:** the narration is written so that a viewer who cannot see the screen still gets every number, label and result. When producing a video, do not add on-screen information that the narration does not say. Each script's own accessibility note lists the visuals that need particular care.
- **Pace:** leave at least 5 seconds of silence at each pause prompt; reveal table rows one at a time, in the order they are narrated.
- **Color:** highlights always come with a label or an arrow (for example "spam" / "not spam" text, not just red / green). Use the colors of the module diagrams, which do not rely on color alone.
- **Readable screens:** large text (at least 24 pt equivalent at 1080p), high contrast, no flashing animations, no more than one table on screen at a time.
- **Audio:** music, if any, stays well below the narration and stops during calculations.

## Contents

| # | Video | Demonstration | Length |
|---|---|---|---|
| 01 | [Is it AI? The self-checkout test](#video-01-is-it-ai-the-self-checkout-test) | Input-to-output chain applied step by step | 3:40 |
| 02 | [Train a spam filter by hand](#video-02-train-a-spam-filter-by-hand) | Counting → weights → inference → test | 4:25 |
| 03 | [One artificial neuron, by hand](#video-03-one-artificial-neuron-by-hand) | Multiply, add the bias, activate | 3:35 |
| 04 | [Watch a language model write](#video-04-watch-a-language-model-write) | The next-token loop with a spinner | 4:05 |
| 05 | [Two lenses, six systems](#video-05-two-lenses-six-systems) | Classifying real systems under both lenses | 3:30 |
| 06 | [Build the AI timeline](#video-06-build-the-ai-timeline) | Placing milestones and shading the winters | 4:15 |
| 07 | [Trace a recommendation](#video-07-trace-a-recommendation) | Collaborative filtering + six-part framework | 3:35 |
| 08 | [Analyze an AI case in seven steps](#video-08-analyze-an-ai-case-in-seven-steps) | Case analysis of the HireFast hiring model | 4:10 |
| 09 | [Catch a hallucination](#video-09-catch-a-hallucination) | The four-step check on a chatbot answer | 4:15 |
| 10 | [Sort AI into EU AI Act tiers](#video-10-sort-ai-into-eu-ai-act-tiers) | The four-question classification method | 4:25 |

---

## Video 01: Is it AI? The self-checkout test

**Source:** [Topic 01: What is AI?](../../topics/01-what-is-ai.md) (Explanation sections 2 and 4; Worked example) · **Length:** about 3:40
**Goal:** Viewers can apply the input-to-output chain and the three-question test to decide whether a tool is AI.

**Segment 1 (0:00–0:25): Hook**
- **On screen:** A simple illustration of a self-checkout: loose bananas on the scale; the screen asks "Bananas (loose)? Confirm".
- **Narration:** "You put some loose bananas on the scale at a supermarket self-checkout, and before you type anything, the screen asks: 'Bananas, loose?' Is that AI? In the next few minutes we'll decide, step by step, using a test you can use on any app."
- **Pause / predict:** "Pause and guess: AI or not? Keep your guess for the end."

**Segment 2 (0:25–1:05): The tool: inputs, inference, outputs**
- **On screen:** The chain `INPUT --> [ AI system: infers / works out an answer ] --> OUTPUT --> effect on the world`, drawn one box at a time.
- **Narration:** "In this module, AI is computer technology that performs tasks we would normally say need human intelligence, such as recognizing patterns, understanding language, making decisions or creating content. The OECD, a group of 38 countries, adds a precise test: an AI system infers from its input how to generate outputs such as predictions, content, recommendations or decisions. To infer means to work something out from evidence. A calculator doesn't infer: it applies one fixed procedure. On screen is a four-part chain: input, the AI system working out an answer, the output, and the effect on the world."
- **Pause / predict:** None.

**Segment 3 (1:05–1:25): Step 1, the input**
- **On screen:** The checkout illustration with the "Input" box empty.
- **Narration:** "Step one: what goes in?"
- **Pause / predict:** "Pause and list the inputs the checkout uses." (5 seconds)
- **Narration (after pause):** "There are two inputs: a camera image of whatever is on the scale, and the weight from the scale itself." On screen, the Input box fills in: "Camera image + weight".

**Segment 4 (1:25–1:45): Step 2, the output and its type**
- **On screen:** Output box: "Bananas (loose)"; below it, the five output types (prediction, classification, recommendation, decision, generated content) with "classification" highlighted and labeled.
- **Narration:** "Step two: what comes out, and what type of output is it? The output is a suggested product: 'Bananas, loose'. That's a classification: the system picks one category from a fixed list of products. If it shows its top three guesses, that ranked list is a recommendation."
- **Pause / predict:** None.

**Segment 5 (1:45–2:35): Step 3, does it infer? The three-question test**
- **On screen:** The three questions appear one by one: 1. What is the input and output? 2. Does it infer a good output for new, varied inputs, or apply one fixed procedure? 3. Could a person write an exact recipe for every possible input? Then four small banana pictures: green, yellow, in a bag, at an angle in dim light.
- **Narration:** "Step three is the heart of the test. We've answered question one. Question two: does it have to work out an answer for new, varied inputs? Question three: could a person write an exact recipe for every possible input?"
- **Pause / predict:** "Pause: could you write one exact rule that recognizes every banana photo?" (5 seconds)
- **Narration (after pause):** "Look at the four pictures: a green bunch, a yellow bunch, bananas in a bag, and bananas at an angle in dim light. Bananas can be green or yellow, bagged or loose, at any angle, under any lighting. No one could write an exact rule for every possible image. So the system must work out the most likely product from patterns it learned from many example images. Yes, it infers."

**Segment 6 (2:35–2:55): Step 4, the effect on the world**
- **On screen:** Effect box: "Item and price added to bill after customer confirms"; a "Confirm" button is highlighted with an arrow.
- **Narration:** "Step four: the effect. The product and its price are added to your bill, but only after you confirm. If the output were wrong, you could pay for the wrong item, so asking you to confirm is a sensible design for a system that will sometimes make mistakes."
- **Pause / predict:** None.

**Segment 7 (2:55–3:15): Step 5, compare with human intelligence**
- **On screen:** Two columns: "Child: recognizes a banana after seeing a few" vs "Checkout AI: needed many example images; only does this one task".
- **Narration:** "Step five: compare with human intelligence. A child can recognize a banana after seeing a few. The checkout system needed many example images, and it can't do anything else: it can't tell you whether the banana is ripe enough for banana bread unless it was specifically built for that."
- **Pause / predict:** None.

**Segment 8 (3:15–3:40): Verdict and your turn**
- **On screen:** The completed chain table: Input = camera image + weight; AI system infers = most likely product from learned patterns; Output = "Bananas (loose)", a classification; Effect = item and price added after confirmation. Then the text "Your turn: Activity 3, AI in Your Day (Topic 01)".
- **Narration:** "Verdict: it's an AI system. Input: an image and a weight. Output: a classification. And it infers from varied inputs. It's also built for one specific task, which Topic 05 will call narrow AI. Compare an alarm clock that rings at seven: one fixed rule, nothing inferred, not AI. Your turn: find three AI systems in your own day and run them through the same chain."
- **Pause / predict:** None.

**Accessibility note:** Segment 5's four banana pictures are described in the narration; the completed table in Segment 8 is read aloud row by row.

---

## Video 02: Train a spam filter by hand

**Source:** [Topic 02: How AI operates](../../topics/02-how-ai-operates.md) (Explanation section 3; Worked example steps 1 to 6) · **Length:** about 4:25
**Goal:** Viewers can trace how labeled data becomes weights (training) and how the weights score new emails (inference), and read test results.
**Note on numbers:** every figure in this video is an *illustrative (made-up)* figure from the topic file, not data from a real email service. Keep the label "Made-up numbers for teaching" on screen throughout.

**Segment 1 (0:00–0:25): Hook**
- **On screen:** An inbox with two emails: "URGENT: claim your FREE prize" and "Team meeting moved to 3pm".
- **Narration:** "How does a spam filter know that 'claim your free prize' is spam and 'team meeting moved to 3pm' isn't? Nobody typed in a rule saying 'meeting emails are genuine'. Today we'll train a tiny spam filter by hand and watch the rules come out of the data. All the numbers are made up for teaching."
- **Pause / predict:** None.

**Segment 2 (0:25–0:40): Step 1, collect labeled data**
- **On screen:** A bar of 12,000 emails split into 10,000 "training" (4,000 spam, 6,000 not spam) and 2,000 "test (kept aside)".
- **Narration:** "Step one: collect labeled data. We have 12,000 emails that people already labeled 'spam' or 'not spam'. We put 2,000 aside as a test set and don't touch them. The other 10,000 are training data: 4,000 spam and 6,000 not spam."
- **Pause / predict:** None.

**Segment 3 (0:40–0:55): Step 2, choose features**
- **On screen:** Five yes/no questions: contains "free"? "urgent"? "meeting"? "invoice"? 3 or more links?
- **Narration:** "Step two: choose features. The model can't read like a person, so each email becomes five yes-or-no answers: does it contain 'free'? 'urgent'? 'meeting'? 'invoice'? Does it have three or more links?"
- **Pause / predict:** None.

**Segment 4 (0:55–1:45): Step 3, count the patterns**
- **On screen:** The counting table, revealed row by row: free 2,400 of 4,000 spam (60%) vs 300 of 6,000 not-spam (5%); urgent 40% vs 2%; meeting 2% vs 30%; invoice 10% vs 8%; 3+ links 50% vs 20%.
- **Narration:** "Step three is training: the learning algorithm counts. 'Free' appears in 2,400 of the 4,000 spam emails, that's 60 percent, but in only 300 of the 6,000 genuine emails, 5 percent. 60 divided by 5 is 12: 'free' is 12 times more common in spam. 'Urgent': 40 percent of spam, 2 percent of not-spam, 20 times more common in spam. Now 'meeting': 2 percent of spam, 30 percent of genuine email."
- **Pause / predict:** "Pause: which way does 'meeting' point, and how many times more common is it?" (5 seconds)
- **Narration (after pause):** "'Meeting' is 15 times more common in genuine email. 'Invoice' is about the same in both, 1.25 times. Three or more links: 50 percent versus 20 percent, 2.5 times more common in spam."

**Segment 5 (1:45–2:25): Turning patterns into weights**
- **On screen:** The weight recipe (at least 5 times more common in spam: +2; 2 to 5 times: +1; under 2 times either way: 0; 2 to 5 times in not-spam: -1; at least 5 times in not-spam: -2), then the learned weights: free +2, urgent +2, meeting -2, invoice 0, 3+ links +1. Threshold: score 2 or more = spam.
- **Narration:** "Our simple algorithm turns each pattern into points. At least five times more common in spam: plus two. Two to five times: plus one. Less than two times either way: zero. And the same on the not-spam side, with minus one and minus two. So: free plus two, urgent plus two, meeting minus two, invoice zero, three or more links plus one. The designers add a threshold: a total of 2 or more means spam. Notice that no person wrote 'meeting emails are usually genuine'. That weight came out of the data."
- **Pause / predict:** None.

**Segment 6 (2:25–3:05): Step 4, inference on new emails**
- **On screen:** Three new emails scored one at a time. A: "URGENT: claim your FREE prize" (4 links). B: "Team meeting moved to 3pm" (no links). C: "Free pizza at the team meeting today!" (no links).
- **Narration:** "Step four is inference: the trained model meets new emails. Email A: urgent, free, four links. Plus two, plus two, plus one: five. Five is at least two, so: spam. Email B: 'meeting', minus two, no links. Score minus two: not spam. Email C: 'Free pizza at the team meeting today!', no links."
- **Pause / predict:** "Pause and score email C. Spam or not?" (5 seconds)
- **Narration (after pause):** "'Free' gives plus two, 'meeting' gives minus two: total zero. Zero is below two, so not spam. Features work together: one pushes toward spam, the other pulls back."

**Segment 7 (3:05–3:40): Step 5, test before deployment**
- **On screen:** Test results on 2,000 unseen emails (800 spam, 1,200 not spam): 720 spam caught, 80 missed (false negatives); 60 genuine emails sent to spam (false positives), 1,140 correctly left in the inbox; 720 + 1,140 = 1,860 of 2,000 = 93%.
- **Narration:** "Step five: test on the 2,000 emails the model never saw: 800 spam and 1,200 genuine. It catches 720 of the 800 spam emails, so 80 get through. Those are false negatives: wrong 'no' answers. It wrongly sends 60 of the 1,200 genuine emails to spam. Those are false positives: wrong 'yes' answers. Correct answers: 720 plus 1,140 is 1,860 out of 2,000, which is 93 percent accuracy."
- **Pause / predict:** "Pause: how many mistakes did it make in total?" (5 seconds)

**Segment 8 (3:40–4:25): Step 6, decide and improve; recap**
- **On screen:** "80 + 60 = 140 mistakes". Then the [machine learning pipeline diagram](../../assets/images/ml-pipeline.svg) with "Training" and "Inference" phases highlighted in turn.
- **Narration:** "140 mistakes: 80 plus 60. Is 93 percent good enough? It depends on the cost of each mistake: a genuine job offer lost in the spam folder may be worse than one extra spam email. If results aren't good enough, the team improves the data or features, for example adding the word 'prize', and trains again. And after launch, every 'Report spam' click becomes new labeled data for the next round. On screen is the whole pipeline. Top row, training: collect data, prepare features and labels, train, get a model, test. Bottom row, inference: a new email goes into the trained model and out comes a prediction."
- **Pause / predict:** None.

**Accessibility note:** The counting table (Segment 4) and the test results (Segment 7) are read aloud in full; the pipeline diagram in Segment 8 is described in the narration. Keep the "made-up numbers" label visible and say it aloud in Segment 1.

---

## Video 03: One artificial neuron, by hand

**Source:** [Topic 03: ML, neural networks and deep learning](../../topics/03-ml-neural-networks-deep-learning.md) (Explanation sections 5 to 7; Worked example Part B) · **Length:** about 3:35
**Goal:** Viewers can calculate one neuron's output (multiply, add the bias, apply a step activation) and explain what a weight and a bias do.
**Note on numbers:** all values are *illustrative (made-up)* and match [artificial-neuron.svg](../../assets/images/artificial-neuron.svg).

**Segment 1 (0:00–0:15): Hook**
- **On screen:** A large neural network fades into a single circle labeled "one neuron".
- **Narration:** "Deep learning systems contain millions or billions of tiny units called artificial neurons. Each one is just a small calculation. Grab a pencil: we'll do one by hand. The numbers are made up for teaching."
- **Pause / predict:** None.

**Segment 2 (0:15–0:45): What a neuron does**
- **On screen:** [An artificial neuron diagram](../../assets/images/artificial-neuron.svg) with the numbers hidden; three labels appear: 1. Multiply, 2. Add + bias, 3. Activate.
- **Narration:** "An artificial neuron does three things. One: it multiplies each input by a weight. Two: it adds the results together, plus an extra number called the bias. Three: it applies an activation function to get the output. The idea goes back to Frank Rosenblatt's perceptron in 1958. On screen: three inputs on the left, each with an arrow carrying a weight into a circle, and an output on the right."
- **Pause / predict:** None.

**Segment 3 (0:45–1:30): Our neuron: a tiny spam detector**
- **On screen:** Table: x1 email contains "free" = 1, weight 0.6; x2 sender in your contacts = 0, weight -0.4; x3 3 or more links = 1, weight 0.3; bias -0.5. Activation: output 1 (spam) if the sum is greater than 0, otherwise 0 (not spam).
- **Narration:** "Our neuron is a tiny spam detector with three yes-or-no inputs, where 1 means yes. Input one: does the email contain 'free'? Yes, 1, with weight 0.6. Input two: is the sender in your contacts? No, 0, with weight minus 0.4. Input three: three or more links? Yes, 1, with weight 0.3. The bias is minus 0.5. A positive weight pushes toward 'spam', a negative weight pushes toward 'not spam', and the negative bias means the neuron needs real evidence before it fires. The activation is a step: output 1, spam, if the sum is greater than zero; otherwise 0."
- **Pause / predict:** "Pause and multiply each input by its weight." (5 seconds)

**Segment 4 (1:30–1:45): Step 1, multiply**
- **On screen:** 1 × 0.6 = 0.6; 0 × (-0.4) = 0; 1 × 0.3 = 0.3, written one line at a time.
- **Narration:** "Step one. One times 0.6 is 0.6. Zero times minus 0.4 is zero: the sender isn't a contact, so that input contributes nothing. One times 0.3 is 0.3."
- **Pause / predict:** None.

**Segment 5 (1:45–2:00): Step 2, add the products and the bias**
- **On screen:** 0.6 + 0 + 0.3 + (-0.5) = 0.4.
- **Narration:** "Step two: add them up, and add the bias. 0.6 plus zero plus 0.3 is 0.9; plus minus 0.5 gives 0.4."
- **Pause / predict:** "Pause: is the output 1 or 0?" (5 seconds)

**Segment 6 (2:00–2:15): Step 3, activate**
- **On screen:** A number line with 0 marked; 0.4 placed to its right; label "greater than 0 → output 1: spam".
- **Narration:** "Step three: the step rule. 0.4 is greater than zero, so the output is 1: spam. That matches the diagram from the module: inputs 1, 0, 1; weights 0.6, minus 0.4, 0.3; bias minus 0.5; sum 0.4; output 1."
- **Pause / predict:** None.

**Segment 7 (2:15–2:45): What if the sender is in your contacts?**
- **On screen:** x2 changes from 0 to 1; the sum recalculates: 0.6 + (-0.4) + 0.3 + (-0.5) = 0.0.
- **Narration:** "Now change one thing: the sender *is* in your contacts, so input two becomes 1."
- **Pause / predict:** "Pause and predict the new sum and output." (5 seconds)
- **Narration (after pause):** "0.6, minus 0.4, plus 0.3, minus 0.5: exactly zero. The step rule needs a sum *greater than* zero, and zero is not greater than zero, so the output is 0: not spam. The negative weight on 'sender in contacts' pulled the decision back, right onto the boundary."

**Segment 8 (2:45–3:00): Other activation functions**
- **On screen:** Same sum 0.4 → step: 1; sigmoid: about 0.60; ReLU: 0.4.
- **Narration:** "Modern networks usually use smoother activations. With the same sum of 0.4, a sigmoid gives about 0.60, which you can read as '60 percent spam-like'. ReLU gives 0.4. The multiply-and-add part is identical; only the final rule changes."
- **Pause / predict:** None.

**Segment 9 (3:00–3:35): Where the weights come from, and layers**
- **On screen:** [Neural network layers diagram](../../assets/images/neural-network-layers.svg): 3 inputs, two hidden layers of 4, 2 outputs; caption "more than one hidden layer = deep (module rule of thumb)".
- **Narration:** "Where did the weights come from? Not from a person. Training starts with rough weights and nudges them, example after example, to reduce mistakes on labeled data. On screen is a small network: three inputs, two hidden layers of four neurons each, and two outputs, every neuron connected to every neuron in the next layer. With more than one hidden layer, it counts as 'deep' in this module. 'Deep' means many layers, not deep understanding. Try Activity 2 in Topic 3 to score four more emails."
- **Pause / predict:** None.

**Accessibility note:** Read every number aloud with its sign ("minus 0.4"); write negative numbers with a clear minus sign and brackets on screen. Describe the layer diagram's structure (counts of neurons per layer) in words, as in Segment 9.

---

## Video 04: Watch a language model write

**Source:** [Topic 04: Generative AI and LLMs](../../topics/04-generative-ai-and-llms.md) (Explanation sections 4, 5 and 7; Worked example steps 1 to 4) · **Length:** about 4:05
**Goal:** Viewers can trace the next-token loop, use cumulative ranges to sample a token, and predict the effect of temperature.
**Note on numbers:** all probabilities are *illustrative (made-up)* and match [next-token-prediction.svg](../../assets/images/next-token-prediction.svg).

**Segment 1 (0:00–0:15): Hook**
- **On screen:** The same question typed into a chatbot twice; two different answers appear.
- **Narration:** "Ask a chatbot the same question twice and you often get two different answers. Is it broken? No. Let's watch a language model write, one small step at a time, and you'll see exactly why."
- **Pause / predict:** None.

**Segment 2 (0:15–0:45): Tokens**
- **On screen:** "Unbelievably, the cat sat." split into boxes: [Un] [believ] [ably] [,] [ the] [ cat] [ sat] [.] → 8 tokens. Caption: "Illustrative; real splits differ between models."
- **Narration:** "First, a large language model doesn't see letters or whole words. It sees tokens: a token can be a word, part of a word, a punctuation mark or a single character. 'Unbelievably, the cat sat' with its full stop could become eight tokens: 'Un', 'believ', 'ably', the comma, 'the', 'cat', 'sat', and the full stop. In English, a token is about three-quarters of a word on average."
- **Pause / predict:** None.

**Segment 3 (0:45–1:10): The loop**
- **On screen:** The [next-token prediction diagram](../../assets/images/next-token-prediction.svg), with the five loop steps listed beside it: Input → Predict → Choose → Append → Repeat.
- **Narration:** "The model repeats one small loop. Input: all the text so far. Predict: a probability for every possible next token. Choose one. Append it to the text. Repeat, until it produces a special end token. On screen, the prompt 'The cat sat on the' goes into the model, and out comes a list of probabilities."
- **Pause / predict:** None.

**Segment 4 (1:10–1:30): Step 1, the probabilities**
- **On screen:** Table: mat 0.41, floor 0.17, sofa 0.12, roof 0.06, all other tokens together 0.24; total 1.00.
- **Narration:** "Here are made-up probabilities for the next token after 'The cat sat on the'. Mat: 0.41. Floor: 0.17. Sofa: 0.12. Roof: 0.06. And all the thousands of other tokens together: 0.24. They add up to exactly 1."
- **Pause / predict:** "Pause: which token would you bet on, and how sure would you be?" (5 seconds)

**Segment 5 (1:30–1:45): Step 2a, the greedy choice**
- **On screen:** "mat" highlighted → "The cat sat on the mat".
- **Narration:** "If the model always takes the most likely token, called the greedy choice, it picks 'mat', with 0.41. But that would give the same, often dull, text every time. So most systems do something else."
- **Pause / predict:** None.

**Segment 6 (1:45–2:40): Step 2b, sampling with a spinner**
- **On screen:** A spinner with slices labeled with their cumulative ranges: mat 0.00 up to 0.41; floor 0.41 up to 0.58; sofa 0.58 up to 0.70; roof 0.70 up to 0.76; others 0.76 up to 1.00. Three runs: random numbers 0.27, 0.63, 0.45.
- **Narration:** "They sample: choose at random, but weighted by probability. Picture a spinner, with each token's slice as big as its probability. Laid end to end from 0 to 1: mat from 0 up to 0.41; floor from 0.41 up to 0.58; sofa from 0.58 up to 0.70; roof from 0.70 up to 0.76; and all other tokens from 0.76 up to 1. The computer draws a random number. Run one: 0.27. That lands in mat's slice: 'The cat sat on the mat'. Run two: 0.63."
- **Pause / predict:** "Pause: which slice does 0.63 land in?" (5 seconds)
- **Narration (after pause):** "Sofa: 0.63 is between 0.58 and 0.70. Run three: 0.45, which is floor. Same prompt, same model, three different continuations. Over many runs, 'mat' would win about 41 percent of the time."

**Segment 7 (2:40–3:20): Step 3, append and repeat**
- **On screen:** New input "The cat sat on the mat" → new table: full stop 0.52, "and" 0.20, comma 0.15, "while" 0.05, all others 0.08.
- **Narration:** "Step three: append and repeat. Take run one. The new input is 'The cat sat on the mat', and the model produces a new table: a full stop, 0.52; 'and', 0.20; a comma, 0.15; 'while', 0.05; everything else, 0.08. If the full stop is chosen, the sentence ends, and the model might then produce the end token. If 'and' is chosen, the sentence carries on, perhaps 'mat and purred', and every later step is different. That's how one small random choice early on leads to a very different final answer. A 300-word reply takes roughly 400 of these steps."
- **Pause / predict:** None.

**Segment 8 (3:20–3:45): Step 4, temperature**
- **On screen:** Three columns for the first step: low temperature (mat 0.80, floor 0.09, sofa 0.05, roof 0.01, others 0.05); normal (0.41, 0.17, 0.12, 0.06, 0.24); high (0.26, 0.18, 0.15, 0.09, 0.32).
- **Narration:** "Temperature controls how adventurous the sampling is. At low temperature, the probabilities are sharpened: mat rises to 0.80. At high temperature, they're flattened: mat drops to 0.26, and all the other tokens together rise to 0.32, so odd choices like 'keyboard' or 'moon' turn up about a third of the time."
- **Pause / predict:** "Pause: low or high temperature for summarizing a rental agreement?" (5 seconds)

**Segment 9 (3:45–4:05): Wrap-up**
- **On screen:** Two take-away lines: "An answer is one sample, not the single correct output." and "Likely is not the same as true."
- **Narration:** "Low: you want accurate, predictable wording, and you'd still check it against the agreement. Two take-aways. An LLM's answer is one sample from many possible answers. And because it picks likely tokens rather than checked facts, fluent text can still be false: that's a hallucination, which Topic 9 explores."
- **Pause / predict:** None.

**Accessibility note:** The spinner (Segment 6) must not rely on slice colors: label each slice with its token and range, and say the ranges aloud. Read every probability table in full, top to bottom.

---

## Video 05: Two lenses, six systems

**Source:** [Topic 05: Types of AI](../../topics/05-types-of-ai.md) (Explanation sections 1 to 4; Worked example) · **Length:** about 3:30
**Goal:** Viewers can classify a system under both the capability lens and the functionality lens, and justify each label.

**Segment 1 (0:00–0:15): Hook**
- **On screen:** Two search-result lists side by side: "narrow, general, superintelligence" and "reactive, limited memory, theory of mind, self-aware".
- **Narration:** "Search 'types of AI' and you'll find two different lists mixed together. They aren't one long ladder. They're two separate lenses, and every AI system gets a label from each. Let's classify six real systems and watch how it works."
- **Pause / predict:** None.

**Segment 2 (0:15–0:55): The two lenses**
- **On screen:** [Types of AI seen through two different lenses](../../assets/images/types-of-ai-two-lenses.svg). Then a car icon with two tags: "small" and "electric".
- **Narration:** "You can sort vehicles by size, or by fuel. A small car can also be electric. AI is the same. Lens one, capability, asks: how broad is its ability compared with humans? Narrow, general, or superintelligent. Only narrow AI exists today; general and superintelligent AI are hypothetical. Lens two, functionality, asks: does it use the recent past while it's working, and does it understand others or itself? Reactive machines and limited memory exist today; theory of mind and self-aware AI are hypothetical. On screen, each lens is a panel with a line marking where today's AI ends."
- **Pause / predict:** None.

**Segment 3 (0:55–1:15): System 1, Deep Blue**
- **On screen:** Classification table, row 1: IBM Deep Blue (chess, 1997).
- **Narration:** "System one: IBM's Deep Blue, which beat the world chess champion in 1997. Capability: it plays chess only, so it's narrow. Functionality: it chose moves from the current board position alone, ignoring what came before. That's reactive, and it's the main example in Arend Hintze's 2016 article that popularized this lens."
- **Pause / predict:** None.

**Segment 4 (1:15–1:50): System 2, a spam filter**
- **On screen:** Row 2: an email spam filter.
- **Narration:** "System two: a spam filter. Capability: it only sorts email, so it's narrow. Now the tricky part: it was trained on millions of old emails."
- **Pause / predict:** "Pause: does that make it limited memory?" (5 seconds)
- **Narration (after pause):** "No. In this lens, memory means using the recent past while the system is operating, not training data. The filter judges each new email on its own features, so we classify it as reactive. That's our module's own classification; no source classifies it."

**Segment 5 (1:50–2:15): Systems 3 and 4, a self-driving car and a voice assistant**
- **On screen:** Rows 3 and 4.
- **Narration:** "System three: a self-driving car's driving system. Narrow: it drives and does nothing else. Limited memory: it tracks the speed and direction of nearby cars over the last few moments. That information is temporary, not saved as lasting experience. System four: a voice assistant such as Siri or Alexa. Narrow, and limited memory: it keeps track of your recent request and context."
- **Pause / predict:** None.

**Segment 6 (2:15–2:45): System 5, an LLM chatbot**
- **On screen:** Row 5: an LLM chatbot (for example, ChatGPT).
- **Narration:** "System five: an LLM chatbot like ChatGPT. It writes poems, summaries and code."
- **Pause / predict:** "Pause: narrow or general?" (5 seconds)
- **Narration (after pause):** "The mainstream view is narrow: IBM classes it as narrow AI and states that current LLMs are not considered AGI. This is debated, and there is no agreed test that would settle it. Functionality: limited memory, because it uses the conversation so far, within its context window."

**Segment 7 (2:45–3:10): System 6, the Netflix recommender**
- **On screen:** Row 6: Netflix's recommendation engine, with "Lens 2: DISPUTED" highlighted.
- **Narration:** "System six: Netflix's recommendation engine. Capability: narrow, it only recommends titles. Functionality: IBM lists it as reactive, but it uses your recent viewing to update recommendations, which looks like limited memory. Sources disagree. That's why this lens is called a popular-press taxonomy, not a scientific standard. When you classify with it, state your reason: the reason matters more than the label."
- **Pause / predict:** None.

**Segment 8 (3:10–3:30): The pattern**
- **On screen:** The grid: rows Narrow / General / Super; columns Reactive / Limited memory / Theory of mind / Self-aware. Only the Narrow-Reactive and Narrow-Limited memory cells contain systems.
- **Narration:** "Put all six on the grid and a pattern appears. Every one is narrow, and every one is either reactive or limited memory. Only those two cells of the grid contain anything real. Everything else, including general AI and theory of mind, is hypothetical."
- **Pause / predict:** None.

**Accessibility note:** The two-lenses diagram and the final grid are described in words (Segments 2 and 8). Reveal one table row at a time and read both labels and both reasons.

---

## Video 06: Build the AI timeline

**Source:** [Topic 06: History of AI](../../topics/06-history-of-ai.md) (Explanation sections 2 to 6; milestone table; Worked example) · **Length:** about 4:15
**Goal:** Viewers can place the key milestones in order, explain both AI winters, and trace why neural networks fell and returned.

**Segment 1 (0:00–0:15): Hook**
- **On screen:** An empty horizontal axis from 1950 to 2025.
- **Narration:** "Was AI invented with ChatGPT? Not even close. Let's build AI's 75-year timeline together, milestone by milestone, and look for the pattern behind its booms and busts."
- **Pause / predict:** None.

**Segment 2 (0:15–0:30): Three ingredients**
- **On screen:** Three labels pinned above the axis: Data, Compute, Algorithms.
- **Narration:** "Keep three ingredients in mind. Data: examples to learn from. Computing power. And algorithms: good methods for learning. When all three were weak, learning-based AI struggled. When all three became strong at the same time, around 2010, AI took off."
- **Pause / predict:** None.

**Segment 3 (0:30–1:35): The Start, 1950 to 1966**
- **On screen:** Milestones dropped onto the axis one by one: 1950 Turing; Aug 1955 proposal; summer 1956 Dartmouth workshop; 1956 Logic Theorist; 1958 perceptron; 1966 ELIZA.
- **Narration:** "1950: Alan Turing publishes 'Computing Machinery and Intelligence' and proposes the imitation game, now called the Turing test. Next: the name 'artificial intelligence'."
- **Pause / predict:** "Pause: was the term first used in 1955 or 1956?" (5 seconds)
- **Narration (after pause):** "1955. In August 1955, John McCarthy, Marvin Minsky, Nathaniel Rochester and Claude Shannon wrote a proposal for a summer research project on artificial intelligence. The workshop itself followed at Dartmouth in the summer of 1956, usually treated as the birth of the field. Also from 1956: the Logic Theorist, which proved theorems by searching; in runs reported in 1957 it proved 38 of the first 52 theorems in a chapter of *Principia Mathematica*. 1958: Frank Rosenblatt's perceptron, a simple neural network that learned from examples, and the press predicted it would one day walk, talk and even be conscious. 1966: Joseph Weizenbaum's ELIZA, a pattern-matching chatbot with no understanding, which some users still became attached to."

**Segment 4 (1:35–2:10): Hitting the wall, and the first winter**
- **On screen:** 1969 *Perceptrons*; 1973 Lighthill report; a shaded band "1st AI winter, ~1974–80".
- **Narration:** "Early successes on tidy problems led to predictions of human-level AI within a generation. Then reality: combinatorial explosion, where real problems have astronomically many possibilities; common sense too huge to write down; and weak hardware with little data. 1969: Minsky and Papert's book *Perceptrons* proves single-layer networks can't learn a simple pattern called XOR. 1973: Britain's Lighthill report says AI has failed its grand promises, and funding is cut. We shade the first AI winter: roughly 1974 to 1980."
- **Pause / predict:** None.

**Segment 5 (2:10–2:50): Boom, then the second winter**
- **On screen:** 1980 XCON at DEC; "1980s expert systems boom"; 1986 backpropagation; 1987 Lisp-machine collapse; a second shaded band "2nd AI winter, ~1987–93".
- **Narration:** "The 1980s bring a boom in expert systems: hand-written IF-THEN rules for one narrow job. From 1980, a system called XCON configured computer orders at Digital Equipment Corporation, with reported savings in the tens of millions of dollars a year. Quietly, in 1986, backpropagation is popularized, making multi-layer networks trainable."
- **Pause / predict:** "Pause: predict why the expert-systems boom turned into a bust." (5 seconds)
- **Narration (after pause):** "They were brittle, failing on cases just outside their rules; expensive to maintain; and unable to learn. In 1987 the market for specialized Lisp machines collapsed. Shade the second winter: roughly 1987 to 1993."

**Segment 6 (2:50–3:25): The Big Comeback**
- **On screen:** May 1997 Deep Blue 3.5–2.5; 2012 AlexNet 15.3% vs 26.2%; Mar 2016 AlphaGo 4–1; Jun 2017 transformer; 30 Nov 2022 ChatGPT.
- **Narration:** "May 1997: IBM's Deep Blue beats world champion Garry Kasparov, 3.5 to 2.5. But careful: Deep Blue was mostly not machine learning. It searched about 200 million positions per second. 2012: AlexNet, a deep neural network trained on GPUs, wins the ImageNet competition with a top-5 error of 15.3 percent, against 26.2 percent for the runner-up. March 2016: AlphaGo beats Lee Sedol 4 to 1, combining deep learning, reinforcement learning and search. June 2017: the transformer. And 30 November 2022: ChatGPT is released."
- **Pause / predict:** None.

**Segment 7 (3:25–3:50): Trace one idea: the neural network**
- **On screen:** A line rising and falling across the timeline through 1958, 1969, 1986, 1990s–2000s, 2012 and 2017–2022, each point labeled with the missing or new ingredient.
- **Narration:** "Now trace one idea along the timeline. 1958, the perceptron: a new algorithm, a boom. 1969: no way to train multi-layer networks, a bust. 1986, backpropagation: a partial revival, but still not enough data or compute, so it stays niche. 2012, ImageNet plus GPUs: new data and new compute, and deep learning takes over. Then transformers. The idea wasn't wrong in 1969. It was early."
- **Pause / predict:** None.

**Segment 8 (3:50–4:15): The lesson**
- **On screen:** The finished [timeline diagram](../../assets/images/ai-history-timeline.svg), then the hype loop: breakthrough → over-generalized promises → hard limits → winter or steady phase.
- **Narration:** "Here's the finished timeline, from Turing in 1950 to ChatGPT in 2022, with the two winters shaded. The repeating loop: a real breakthrough, over-generalized promises, hard limits, and then a winter, or a steadier phase if the technology delivers real value. So when you hear a big prediction, separate what a system can do today from what people predict it will do."
- **Pause / predict:** None.

**Accessibility note:** Say every date and score aloud as the milestone appears; describe the shaded winter bands in words ("shaded band from about 1974 to 1980"). The rising-and-falling line in Segment 7 is fully narrated.

---

## Video 07: Trace a recommendation

**Source:** [Topic 07: Real-world applications](../../topics/07-real-world-applications.md) (Explanation sections 1 and 2; Worked example; Visual) · **Length:** about 3:35
**Goal:** Viewers can trace collaborative filtering on a small ratings table and analyze a recommender with the six-part framework.
**Note on numbers:** the names and ratings are *illustrative (made-up)*. The Netflix figure is the company's own 2015 figure.

**Segment 1 (0:00–0:20): Hook**
- **On screen:** A streaming home screen with a row titled "Because you watched...".
- **Narration:** "Where do 'Because you watched' rows come from? In a 2015 paper, two Netflix leaders wrote that their recommender influences choice for about 80 percent of hours streamed. That's the company's own figure. Let's trace how a simple recommender decides, using made-up ratings."
- **Pause / predict:** None.

**Segment 2 (0:20–0:55): The ratings table**
- **On screen:** Ratings, 1 to 5: Sam: A 5, B 4, C 1, D not watched. Priya: A 5, B 5, C 1, D 5. Leo: A 1, B 2, C 5, D 1.
- **Narration:** "A tiny streaming service has three users and four films, rated from 1, hated it, to 5, loved it. Sam gave Film A 5, Film B 4, Film C 1, and hasn't watched Film D. Priya: 5, 5, 1, and Film D 5. Leo: 1, 2, 5, and Film D 1. The question: should the service recommend Film D to Sam? This is collaborative filtering: people who agreed in the past will probably agree on things they haven't seen."
- **Pause / predict:** None.

**Segment 3 (0:55–1:25): Step 1, compare Sam with Priya**
- **On screen:** Sam vs Priya: Film A 5 − 5 = 0; Film B 5 − 4 = 1; Film C 1 − 1 = 0.
- **Narration:** "Step one: compare Sam with each other user on the films they've both rated. We add up the differences between their ratings, ignoring minus signs. A smaller total means more similar taste. Sam versus Priya: Film A, 5 and 5, difference 0. Film B, 4 and 5, difference 1. Film C, 1 and 1, difference 0."
- **Pause / predict:** "Pause: what's the total? Then do Sam versus Leo." (5 seconds)

**Segment 4 (1:25–1:40): Compare Sam with Leo**
- **On screen:** Sam vs Priya total = 1. Sam vs Leo: 4 + 2 + 4 = 10.
- **Narration:** "Sam and Priya: a total of 1, very similar. Sam versus Leo: Film A, 5 and 1, difference 4. Film B, 4 and 2, difference 2. Film C, 1 and 5, difference 4. Total 10: very different."
- **Pause / predict:** None.

**Segment 5 (1:40–2:05): Steps 2 to 4, predict and act**
- **On screen:** Priya's row highlighted; an arrow from her Film D rating (5) to Sam's empty Film D cell: "predicted ≈ 5 → recommend".
- **Narration:** "Step two: the most similar user is Priya. Step three: what did she think of Film D? She gave it 5. What about Leo's 1? Leo's taste is the opposite of Sam's, so his low rating isn't a warning. Step four: predict Sam's rating at about 5, and put Film D near the top of Sam's list."
- **Pause / predict:** None.

**Segment 6 (2:05–2:30): Step 5 and the cold-start problem**
- **On screen:** A loop arrow "Sam rates Film D → new training data"; then a new column "Film E: no ratings yet" with a question mark.
- **Narration:** "Step five: if Sam watches Film D and rates it, that rating becomes new training data, so future comparisons improve. That feedback loop is what makes recommenders learning systems. But suppose a brand-new film that nobody has rated yet. There's nothing to compare, so collaborative filtering can't recommend it. That's the cold-start problem, and it's one reason popular items tend to get even more popular."
- **Pause / predict:** None.

**Segment 7 (2:30–3:10): The six-part framework**
- **On screen:** The six-part table for a streaming recommender, filled in row by row: Input; Output; AI type; Benefit; Risk; Human oversight.
- **Narration:** "Real recommenders compare millions of users and use many more signals, like watch time and skips, combined by machine learning rather than our hand-written rule. Let's analyze one with the module's six questions. Input: your viewing history, ratings and searches, plus the behavior of millions of others. Output: a personalized ranked list. AI type: machine learning, often deep learning. Benefit: finding things you enjoy in a huge catalog. Risk: filter bubbles, a goal like watch time that may not match your well-being, and privacy."
- **Pause / predict:** "Pause: how serious is one bad recommendation, and how much human oversight does it need?" (5 seconds)

**Segment 8 (3:10–3:35): Stakes and oversight**
- **On screen:** Three columns: streaming recommender (stakes low), AI eye-disease screening (high), robotaxi (very high), with the oversight row beneath.
- **Narration:** "Low stakes: a bad suggestion wastes an evening. So nobody checks each recommendation; humans set the goals and test changes. Compare AI eye-disease screening, where stakes are high and a specialist follows up, or a robotaxi, where stakes are very high and permits, remote staff and incident reporting are needed. The rule of thumb: the higher the stakes, the more human oversight."
- **Pause / predict:** None.

**Accessibility note:** Read each user's ratings aloud in film order (A, B, C, D) and say "not watched" for empty cells; read each subtraction aloud. The three-column comparison in Segment 8 is read row by row.

---

## Video 08: Analyze an AI case in seven steps

**Source:** [Topic 08: Ethics, risks and social impact](../../topics/08-ethics-risks-social-impact.md) (Explanation sections 2 and 8; Worked example; related real case in section 2) · **Length:** about 4:10
**Goal:** Viewers can apply the seven-step case analysis, trace where bias enters a hiring model, and propose safeguards.
**Note on the case:** "HireFast Ltd" and all its figures are *illustrative (made-up)*, inspired by the real Amazon case reported by Reuters in 2018. Show "Made-up company for teaching" on screen whenever HireFast is shown.

**Segment 1 (0:00–0:25): Hook**
- **On screen:** A stack of resumes feeding into a box labeled "AI score", with a label "HireFast Ltd (made-up company)".
- **Narration:** "A company wants AI to score job applications. What could go wrong, and how would you know? Today we analyze a case in seven steps. The company, HireFast, is made up, but it's inspired by a real case: in 2018 Reuters reported that Amazon abandoned an experimental resume-rating tool that had learned to penalize the word 'women's'."
- **Pause / predict:** None.

**Segment 2 (0:25–0:40): The seven-step method**
- **On screen:** The seven steps listed: 1 Describe, 2 Stakeholders, 3 Benefits, 4 Harms, 5 Evidence, 6 Safeguards, 7 Judgment.
- **Narration:** "Here's the method. One: describe the system. Two: list the stakeholders. Three: benefits. Four: harms, checking all six issues: bias, privacy, jobs, accountability and transparency, environment, and misinformation. Five: evidence. Six: safeguards. Seven: a judgment."
- **Pause / predict:** None.

**Segment 3 (0:40–1:05): Step 1, describe the system**
- **On screen:** The HireFast trace table, rows 1 and 2: training data = 10,000 past applications from 10 years; label = "was hired" (yes/no); features = words used, university, years of experience, clubs; deployment = top 20% invited to interview.
- **Narration:** "Step one: describe it. HireFast trains a model on 10,000 past applications from the last ten years. The label, the answer the model learns to predict, is 'was hired', yes or no. Each resume becomes features: words used, university, years of experience, clubs. That makes it supervised machine learning. In use, it scores new applicants, and the top 20 percent are invited to interview."
- **Pause / predict:** None.

**Segment 4 (1:05–1:30): Steps 2 and 3, stakeholders and benefits**
- **On screen:** Stakeholder icons: applicants, HireFast's recruiters, the company, society. A star on "applicants: affected but not the user".
- **Narration:** "Step two: stakeholders. Anyone affected: the applicants, the recruiters, the company, and society."
- **Pause / predict:** "Pause: which stakeholder is affected by the system but doesn't use it?" (5 seconds)
- **Narration (after pause):** "The applicants. They bear the consequences and usually can't see how it works. Step three: benefits. The company wants faster scoring of many applications; the scenario gives no figures, so we note the benefit without exaggerating it."

**Segment 5 (1:30–2:45): Step 4, harms: trace the bias**
- **On screen:** [Where bias can enter during the life cycle of an AI system](../../assets/images/ai-system-lifecycle-bias.svg), with the HireFast steps highlighted on the loop as they are narrated.
- **Narration:** "Step four: harms. Bias is the big one, so let's trace it around the AI life cycle on screen: a loop of seven stages from problem definition to feedback. Data collection: 80 percent of past applicants and 85 percent of past hires were men. Labeling: 'was hired' reflects past hiring decisions, which may themselves have been biased. Features: words like 'women's', as in 'women's coding society', appear mostly on women's resumes, so they act as a proxy for gender. Training: because fewer women were hired, the model links 'women's' with 'not hired' and gives it a negative weight. Nobody wrote 'prefer men'; the model learned it. Testing: overall accuracy at predicting past hires is 90 percent."
- **Pause / predict:** "Pause: 90 percent sounds excellent. Why isn't it reassuring?" (5 seconds)
- **Narration (after pause):** "Because it's excellent at copying the past, and there are no separate results by gender. Deployment: equally qualified women get lower scores, at scale, affecting thousands of applicants. Also check the other issues: accountability and transparency, if applicants can't find out why they were rejected."

**Segment 6 (2:45–3:10): Step 5, evidence**
- **On screen:** Two evidence cards: "Amazon (Reuters, 2018): penalized 'women's'" and "Gender Shades (2018): error up to 34.7% vs at most 0.8%; overall figures hid the gap".
- **Narration:** "Step five: evidence. Is there a similar real case? Yes: Amazon's tool, trained on about ten years of mostly male resumes, did exactly this. And the Gender Shades study in 2018 showed why overall accuracy can mislead: commercial face-analysis systems had error rates up to 34.7 percent for darker-skinned women but at most 0.8 percent for lighter-skinned men, and overall figures hid that gap."
- **Pause / predict:** None.

**Segment 7 (3:10–3:50): Step 6, safeguards**
- **On screen:** Four fixes, one per stage: Data; Features; Testing (example: "20% of men vs 10% of equally qualified women invited → investigate"); Deployment.
- **Narration:** "Step six: safeguards, matched to where the bias entered. Data: check the balance, and ask whether 'was hired' is a fair label at all. Perhaps 'performed well after one year' is better, though that may carry bias too. Features: remove obvious proxies such as club names and gendered words, knowing subtle proxies can remain. Testing: measure results separately for men and women and other groups. If 20 percent of men but only 10 percent of equally qualified women are invited, investigate. Deployment: use the AI only to assist, have humans review decisions, let applicants request a human review, and audit regularly."
- **Pause / predict:** None.

**Segment 8 (3:50–4:10): Step 7, judgment**
- **On screen:** Three options: "Use as is" (crossed out), "Use with conditions", "Do not deploy", with the condition "if bias can't be reduced to an acceptable level".
- **Narration:** "Step seven: judgment. Use as is? No. Use with conditions, only if group-by-group testing shows the bias has been reduced to an acceptable level. And if it can't be, don't deploy. That's what Amazon eventually did with its tool. Try the same seven steps on the SafeStation face-recognition case in Topic 8's Activity 3."
- **Pause / predict:** None.

**Accessibility note:** The bias life-cycle diagram (Segment 5) is described as a loop and each stage is named aloud as it is highlighted; do not use color alone to mark the problem stages. Say "made-up" whenever HireFast figures appear.

---

## Video 09: Catch a hallucination

**Source:** [Topic 09: Limitations and misconceptions](../../topics/09-limitations-and-misconceptions.md) (Explanation sections 2.1 and 4; Worked example) · **Length:** about 4:15
**Goal:** Viewers can apply the four-step check (split, prioritize, verify, decide) to a chatbot answer and explain why hallucinations happen.
**Note on the example:** the chatbot answer was written for the module and deliberately contains errors; show "Example answer with deliberate errors" on screen.

**Segment 1 (0:00–0:45): Hook**
- **On screen:** A chat window. Question: "Briefly, how did AI start?" The answer appears, labeled "Example answer with deliberate errors".
- **Narration:** "A learner asks a chatbot: 'Briefly, how did AI start?' Here's the answer: 'AI began in 1950 when Alan Turing published Computing Machinery and Intelligence, proposing the imitation game. The term artificial intelligence was first used at the Dartmouth workshop in 1962, organized by John McCarthy. The first chatbot, ELIZA, created by Joseph Weizenbaum, understood users' emotions and gave therapy. According to Weizenbaum's 1966 book Machines That Feel, over 90 percent of users believed ELIZA was human.' It sounds confident. Some of it is false. Let's find out which parts."
- **Pause / predict:** "Pause: does anything already sound wrong to you?" (5 seconds)

**Segment 2 (0:45–1:25): Why this happens**
- **On screen:** The [next-token prediction diagram](../../assets/images/next-token-prediction.svg) with the caption "likely, not verified".
- **Narration:** "Why would a chatbot invent things? It writes one token at a time, choosing likely tokens. It's trained to produce likely text, not to check that it's true, and it has no built-in fact database. For common facts, likely and true usually match. For rare details, it still produces the kind of text that belongs there: a title-shaped title, a year-shaped number. And a 2025 paper by Kalai and colleagues argues that training and tests often reward guessing over saying 'I don't know'. This isn't lying: there's no intention. It's a side effect of how text is generated."
- **Pause / predict:** None.

**Segment 3 (1:25–2:05): Step 1, split into claims**
- **On screen:** Seven numbered claims, C1 to C7, appearing one at a time.
- **Narration:** "Step one: split the answer into separate claims. C1: Turing published 'Computing Machinery and Intelligence' in 1950. C2: the paper proposed the imitation game. C3: the term 'artificial intelligence' was first used at the Dartmouth workshop in 1962. C4: the workshop was organized by John McCarthy. C5: ELIZA was created by Joseph Weizenbaum. C6: ELIZA understood users' emotions and gave therapy. C7: Weizenbaum's 1966 book *Machines That Feel* says over 90 percent of users believed ELIZA was human."
- **Pause / predict:** "Pause: which three claims are the riskiest to trust without checking?" (5 seconds)

**Segment 4 (2:05–2:20): Step 2, prioritize**
- **On screen:** C3, C6 and C7 flagged, with tags "exact date", "claim about understanding", "named source + precise statistic".
- **Narration:** "Step two: prioritize the claims that matter most and are most likely to be hallucinated: rare facts, exact numbers, quotations and references. That's C3, an exact date; C6, a claim about understanding; and C7, a named source plus a precise statistic."
- **Pause / predict:** None.

**Segment 5 (2:20–3:15): Step 3, verify**
- **On screen:** A verification table filling in, one row per claim, with "Correct" or "Wrong" written in words.
- **Narration:** "Step three: verify each important claim in an independent, reliable source. Here we use Topic 6 and its sources. C1 and C2: Turing's paper appeared in the journal *Mind* in 1950 and introduces the imitation game. Correct. C3: the term actually appears in a 1955 proposal, and the workshop was held in summer 1956. 1962 is wrong: a hallucinated date. C4: McCarthy was a lead organizer, with Minsky, Rochester and Shannon on the proposal. Correct, if simplified. C5: Weizenbaum did create ELIZA. Correct. C6: ELIZA used simple pattern-matching rules and had no understanding; its DOCTOR script imitated a therapist. Wrong. C7: Weizenbaum's 1966 publication was a journal paper in *Communications of the ACM*, not a book called *Machines That Feel*, and no such book or 90 percent figure can be found. An invented source and an invented statistic."
- **Pause / predict:** None.

**Segment 6 (3:15–3:50): Step 4, decide and rewrite**
- **On screen:** The corrected answer, with the changed phrases underlined.
- **Narration:** "Step four: decide. Keep what's verified, correct what's wrong, and remove anything you can't verify. The rewrite: 'AI's roots go back to 1950, when Alan Turing published Computing Machinery and Intelligence, proposing the imitation game. The term artificial intelligence first appeared in a 1955 proposal by John McCarthy and colleagues for a workshop held at Dartmouth in summer 1956. In 1966 Joseph Weizenbaum published a paper describing ELIZA, a rule-based program that imitated a therapist by pattern-matching, without any real understanding, though some users still became emotionally attached to it.'"
- **Pause / predict:** None.

**Segment 7 (3:50–4:15): What to notice**
- **On screen:** Three take-aways: "False claims look exactly like true ones." "An invented source is the most dangerous." "Don't ask the chatbot to check itself."
- **Narration:** "What to notice. The false claims were mixed in with true ones, in exactly the same confident style. The invented source was the most dangerous, because a reference makes a claim look checked. And don't ask the chatbot whether its own answer is right: that check comes from the same process. Use an independent source."
- **Pause / predict:** None.

**Accessibility note:** The chatbot answer and the corrected answer are read aloud in full. The verification table uses the words "Correct" and "Wrong", not only check marks or colors.

---

## Video 10: Sort AI into EU AI Act tiers

**Source:** [Topic 10: The future of AI](../../topics/10-future-of-ai.md) (Explanation section 4; Worked example; Visual) · **Length:** about 4:25
**Goal:** Viewers can classify an AI system into an EU AI Act risk tier with the four-question method and say which rules apply on a given date.
**Note on currency:** dates reflect the Act as amended by the 2026 Digital Omnibus on AI, as described in the topic file (status 6 November 2026). If the topic file is updated, update this script.

**Segment 1 (0:00–0:15): Hook**
- **On screen:** Headline "Does the EU ban AI?" with a large "No" stamped on it.
- **Narration:** "Does the European Union ban AI? No. Its AI Act sorts AI uses by risk, and the rules get stricter as the risk rises. Let's learn a four-question method and use it on three real-world-style examples."
- **Pause / predict:** None.

**Segment 2 (0:15–0:55): The Act in brief**
- **On screen:** The four-tier pyramid from the topic's Visual: top Unacceptable (banned: social scoring; emotion recognition at work or school); High (strict obligations: CV sorting, exam scoring, credit scoring); Transparency (disclose or label: chatbots, deepfakes); base Minimal (no specific new obligations: spam filters, video-game AI).
- **Narration:** "The EU AI Act, Regulation 2024/1689, entered into force on 1 August 2024. It applies to anyone placing AI on the EU market or using it in the EU, even companies based outside it. Picture a pyramid with four tiers. Top, with the fewest systems: unacceptable risk, banned, like social scoring or emotion recognition at work or school. Next, high risk: strict obligations, like CV sorting, exam scoring or credit scoring. Then transparency risk: chatbots must say they're AI, and deepfakes must be labeled. Base, with most systems: minimal risk, like spam filters and video-game AI."
- **Pause / predict:** None.

**Segment 3 (0:55–1:25): The four questions**
- **On screen:** A flowchart: 1 Banned practice? → Unacceptable. 2 High-risk area or safety component of a regulated product? → High. 3 Interacts with people or generates synthetic content? → Transparency duties (can be added to High). 4 None of these → Minimal.
- **Narration:** "Ask four questions, in order. One: is it a banned practice? Two: is it used in a high-risk area, such as education, employment, credit, law enforcement, migration, justice or critical infrastructure, or is it a safety component of a regulated product? Three: does it interact directly with people, or generate synthetic content? Then transparency duties apply, and they can come on top of high-risk rules. Four: none of these? Minimal risk."
- **Pause / predict:** None.

**Segment 4 (1:25–2:10): Example A, exam grading**
- **On screen:** "Example A: A university uses AI to grade students' final exams, and the grades decide whether students pass."
- **Narration:** "Example A: a university uses AI to grade final exams, and the grades decide whether students pass."
- **Pause / predict:** "Pause and run the four questions. Which tier?" (5 seconds)
- **Narration (after pause):** "Question one: it isn't on the banned list. Question two: education is a high-risk area, and the system decides students' results. So: high risk. The provider must manage risks, use high-quality, representative training data, document the system, log its operation, ensure accuracy, and design it for human oversight; the university must use it as instructed, with human oversight. When? From 2 December 2027, after the 2026 delay. Why so strict? A biased grading model could unfairly fail students."

**Segment 5 (2:10–2:30): Example B, a delivery chatbot**
- **On screen:** "Example B: An online shop's customer-service chatbot answers questions about deliveries."
- **Narration:** "Example B: an online shop's chatbot answers delivery questions. Not banned. Customer service for deliveries isn't a high-risk area. But it interacts directly with people, so it has transparency duties: customers must be told they're chatting with an AI. That has applied since 2 August 2026."
- **Pause / predict:** None.

**Segment 6 (2:30–3:00): Example C, webcam "engagement" monitoring**
- **On screen:** "Example C: An employer installs software that reads employees' facial expressions on webcams to judge whether they're 'engaged' at work."
- **Narration:** "Example C: an employer installs software that reads employees' facial expressions on webcams to judge whether they're engaged."
- **Pause / predict:** "Pause: which question decides this one?" (5 seconds)
- **Narration (after pause):** "Question one. Emotion recognition in the workplace is on the banned list, so it's prohibited, and has been since 2 February 2025. Emotion recognition is scientifically unreliable, and using it on employees creates a big power imbalance and privacy intrusion."

**Segment 7 (3:00–3:55): Which rules apply when?**
- **On screen:** Timeline: 2 Feb 2025 bans + AI literacy; 2 Aug 2025 general-purpose AI model rules + governance; 2 Aug 2026 general application incl. transparency; 2 Dec 2026 new ban on generating non-consensual intimate content or child sexual abuse material; 2 Dec 2027 stand-alone high-risk (originally 2 Aug 2026); 2 Aug 2028 high-risk AI in regulated products (originally 2 Aug 2027). A marker at "today: 6 Nov 2026".
- **Narration:** "The Act applies in stages. Bans and AI literacy: 2 February 2025. General-purpose AI models: 2 August 2025. General application, including transparency duties: 2 August 2026. A new ban on AI that generates non-consensual intimate content or child sexual abuse material: 2 December 2026. In 2026 an amending law, the Digital Omnibus on AI, delayed the high-risk rules: stand-alone uses like education, employment and credit now from 2 December 2027, originally 2 August 2026; and AI built into regulated products, like medical devices, from 2 August 2028, originally 2 August 2027. So on 6 November 2026, the bans, the general-purpose AI rules and the transparency duties apply, but the main high-risk obligations don't yet. These changes are recent, so for real decisions always check the current official text."
- **Pause / predict:** None.

**Segment 8 (3:55–4:25): Binding law and soft law; wrap-up**
- **On screen:** Three rows: EU AI Act = binding law with fines (up to €35 million or 7% of worldwide turnover for banned practices); OECD AI Principles = non-binding, 47 adherents; UNESCO Recommendation = non-binding, 193 member states.
- **Narration:** "Breaking the bans can cost up to 35 million euros or 7 percent of worldwide annual turnover, whichever is higher. That's binding law. The OECD AI Principles and UNESCO's Recommendation on the Ethics of AI are different: non-binding guidance that steers national laws but can't fine anyone. Your turn: Activity 1 in Topic 10 has eight systems to classify, and one of them belongs in two tiers."
- **Pause / predict:** None.

**Accessibility note:** Describe the pyramid's four levels from top to bottom (Segment 2) and read every date in the timeline aloud, including the "originally" dates; use text labels ("originally 2 Aug 2026"), not only strike-through formatting.
