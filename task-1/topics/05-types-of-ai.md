# 05: Types of AI

**Module:** AI Overview · **Version:** 2.0 · **Status:** drafted (self-checked) · **Last updated:** 2026-11-06

## Learning goals

After this topic, you should be able to:

- **Explain** the two separate ways of classifying AI: **by capability** (narrow, general, superintelligent) and **by functionality** (reactive machines, limited memory, theory of mind, self-aware).
- **Distinguish** which types exist today and which are hypothetical, and **explain** why the two classifications are different lenses rather than one ladder.
- **Classify** a real or imagined AI system under **both** lenses and **justify** each choice.
- **Identify and correct** common errors in claims about types of AI (for example, "chatbots are general AI").

## Prerequisites

- [Topic 01](01-what-is-ai.md): definition of AI; everyday AI systems; the observation that each is built for particular tasks.
- [Topic 02](02-how-ai-operates.md): rule-based AI and search (for example, game-playing programs); training versus inference.
- [Topic 03](03-ml-neural-networks-deep-learning.md): machine learning, neural networks and deep learning.
- [Topic 04](04-generative-ai-and-llms.md): large language models (LLMs), prompts and the **context window**.

## Key terms

| Term | Plain-English definition |
|---|---|
| Classification scheme (taxonomy) | A way of sorting things into groups according to one chosen question. |
| **Lens 1: by capability** | Sorts AI by **how broad and powerful** its abilities are compared with humans. |
| Narrow AI (artificial narrow intelligence, ANI) | AI built for one task or a limited range of tasks. All AI that exists today is narrow AI. Sometimes called "weak AI". |
| General AI (artificial general intelligence, AGI) | Hypothetical AI that could match (or exceed) human abilities across essentially any intellectual task, and learn new tasks as flexibly as a person. Sometimes called "strong AI". |
| Superintelligence (artificial superintelligence, ASI) | Speculative AI that would greatly exceed the best human abilities in virtually every area. |
| **Lens 2: by functionality** | Sorts AI by **how it works with memory and with understanding of others and itself**. |
| Reactive machine | AI that responds only to the current input, with no memory of earlier moments. |
| Limited memory AI | AI that uses information from the recent past (for example, the last few seconds of sensor data, or the conversation so far) while it is working, but does not build up lasting life experience. |
| Theory of mind AI | Hypothetical AI that would understand that people (and other agents) have their own thoughts, feelings, beliefs and intentions, and adjust its behavior accordingly. |
| Self-aware AI | Hypothetical AI that would have a sense of itself and awareness of its own internal states (consciousness). |
| Hypothetical / speculative | Imagined and discussed, but not built. "Speculative" suggests even more uncertainty about whether it is possible. |

## Explanation

### 1. Why there are "two lists" of AI types

If you search online for "types of AI", you will usually find two different lists mixed together:

- narrow AI, general AI, superintelligence; and
- reactive machines, limited memory, theory of mind, self-aware AI.

They are **not** one long list, and they are **not** steps on a single ladder. They answer **different questions**, in the same way that you could sort vehicles by *size* (small, medium, large) or by *fuel* (gasoline, diesel, electric). A small car can be electric; a large truck can be diesel. Each vehicle has a place in **both** schemes. IBM's explainer, for example, presents the two schemes separately and places the same system, ChatGPT, under narrow AI in one and under limited memory AI in the other [1].

| | Lens 1: by capability | Lens 2: by functionality |
|---|---|---|
| Question asked | How broad and powerful is the AI's ability, compared with humans? | How does the AI use memory, and does it understand others or itself? |
| Categories | Narrow (ANI), General (AGI), Superintelligence (ASI) | Reactive machines, Limited memory, Theory of mind, Self-aware |
| Exist today | Narrow only | Reactive and limited memory only |
| Hypothetical | General, Superintelligence | Theory of mind, Self-aware |
| Status of the scheme | Widely used in research, policy and the media; AGI has no agreed definition | A popular-science taxonomy (Hintze, 2016), not a formal scientific standard |

### 2. Lens 1: classifying by capability

**Narrow AI (ANI).** A narrow AI system is designed for a specific task or a limited set of tasks: recognizing faces, filtering spam, recommending films, translating text, driving in particular conditions, playing chess. It may be superhuman at that task, but it cannot transfer its skill to unrelated jobs: the chess program cannot drive a car. IBM states that narrow AI "is the only type of AI that exists today" [1]. Every example in Topics 01 to 04 is narrow AI.

**What about chatbots?** LLM-based chatbots (Topic 04) can write poems, summarize documents, explain science and produce code, so they seem much broader than a spam filter. Are they still narrow? IBM classes ChatGPT as narrow AI and states that "current LLMs are not considered AGI", while noting that some researchers argue that advanced LLMs have reached AGI and critics reply that breadth alone is not enough without reliable performance, common sense and real-world understanding [1][2]. A balanced summary for beginners: today's chatbots are **much broader than older narrow AI**, but they still work within limits (mostly text and images, frequent errors such as hallucinations, no ability to act reliably in the physical world, and no learning from experience after training unless they are retrained). The mainstream view is that **they are not AGI**, and there is no agreed test that would settle the question.

**General AI (AGI).** AGI is a hypothetical stage in which an AI system can "match or exceed the cognitive abilities of human beings across any task" [2]. Such a system could, for example, learn a new job from scratch, the way a person might move from working in a cafe to studying law. IBM notes that "there is no consensus among experts regarding what exactly should qualify as AGI" [2]. Predictions of *when* (or whether) AGI will arrive vary enormously; [Topic 10](10-future-of-ai.md) looks at this debate.

**Superintelligence (ASI).** Philosopher Nick Bostrom defined superintelligence as "any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest" [3]. The words "virtually all" matter: a chess program is far better than any human at chess, but it is not superintelligent, because it is not better at everything else. ASI is entirely speculative. It appears in discussions of long-term risks and safety, not in any existing product.

**Other names you may meet.** Some writers call narrow AI "weak AI" and general AI "strong AI" [1]. Because these words are used in different ways by different authors, this module uses *narrow* and *general*.

### 3. Lens 2: classifying by functionality

This scheme became popular through a 2016 article in *The Conversation* by Arend Hintze, a researcher at Michigan State University [4], and was later repeated by many industry explainers [1]. It is a helpful way to think about memory and understanding, but it is **a popular-press taxonomy, not a formal scientific standard**: definitions vary between sources, and the boundaries between categories are fuzzy (see the Netflix row in the worked example).

Important: in this scheme, "memory" means **using information about the recent past while the system is operating**. It does *not* refer to training data. Almost every modern AI system was trained on past data, but that alone does not make it "limited memory" in this scheme.

**Type 1: Reactive machines.** These have no memory of earlier moments: they respond only to the situation in front of them. Hintze's main example is IBM's Deep Blue, the chess computer that beat world champion Garry Kasparov in 1997. Deep Blue looked at the current board, predicted possible moves and chose the best one, ignoring everything that had happened before the current position [4]. Hintze discusses Google DeepMind's AlphaGo in the same section, as another game-playing system of this kind [4]. Reactive machines can be extremely good at their task and are predictable.

**Type 2: Limited memory.** These systems look a short way into the past while they work. Hintze's example is a self-driving car, which tracks the speed and direction of nearby cars over several moments and combines that with preprogrammed knowledge such as lane markings and traffic lights to decide, for instance, when to change lanes. That recent information is temporary: it is not saved as lasting experience the way a human driver learns over the years [4]. IBM also lists chatbots and virtual assistants here [1]: an LLM chatbot uses the conversation so far, within its context window (Topic 04), to choose its next reply.

**Type 3: Theory of mind (hypothetical).** "Theory of mind" is a term from psychology: the understanding that other people have their own thoughts, feelings, beliefs and intentions that shape their behavior. An AI with theory of mind would genuinely model the people around it and adjust its behavior accordingly, which Hintze argues would be essential for real social cooperation [4]. This does not exist yet. "Emotion AI" systems can label facial expressions or tone of voice, but IBM notes that "to date, Emotion AI is unable to understand and respond to human feelings" [1]. Note: a chatbot that writes "I understand how you feel" is producing likely text (Topic 04); that is not evidence that it models your mind.

**Type 4: Self-aware AI (hypothetical).** The final type would have a representation of itself and awareness of its own internal states, which Hintze links to consciousness. He describes such machines as probably far off [4]. No existing AI system is accepted as self-aware. [Topic 09](09-limitations-and-misconceptions.md) explains why claims that a chatbot is "alive" or "conscious" are a misconception.

### 4. Putting the two lenses together

Because the lenses ask different questions, the same system gets one label from each. The grid below shows where **today's** systems fall. Only two cells contain anything that exists.

| | Reactive | Limited memory | Theory of mind | Self-aware |
|---|---|---|---|---|
| **Narrow (ANI)** | Deep Blue; a spam filter judging each email; face unlock | Self-driving car perception; LLM chatbots; voice assistants | (nothing built) | (nothing built) |
| **General (AGI)** | (hypothetical) | (hypothetical) | (hypothetical) | (hypothetical) |
| **Super (ASI)** | (speculative) | (speculative) | (speculative) | (speculative) |

**Key point:** all AI that exists today is **narrow AI**, working as **reactive** or **limited-memory** systems. Theory of mind and self-awareness are research questions or science fiction, and AGI and ASI are not built.

Notice also that the lenses do not line up neatly. It is not agreed whether an AGI would need theory of mind or self-awareness, so you cannot automatically convert "general" into a functionality type, or the other way round.

### 5. Why this matters

Headlines often say things like "AI that thinks like a human" or "the first general AI". Knowing the two lenses lets you ask sharper questions: *Which task is it narrow at? Does it use memory of the recent past? Is there any evidence it understands people, or is it producing likely text?* That helps you avoid both hype ("it's basically a person") and dismissal ("it's just autocomplete, it can't do anything").

## Worked example

**Classifying six real systems under both lenses.** For each system, ask the capability question first (*how broad?*), then the functionality question (*does it use the recent past while operating? does it model minds?*).

| # | System | Lens 1: capability | Why | Lens 2: functionality | Why |
|---|---|---|---|---|---|
| 1 | IBM Deep Blue (chess, 1997) | Narrow | Plays chess only. | Reactive | Chooses moves from the current board position alone; Hintze's main example [4]. |
| 2 | An email spam filter (for example, Gmail's) | Narrow | Only sorts email. | Reactive (our classification) | Judges each new email on its own features as it arrives. It was *trained* on past emails, but in this scheme training data is not "memory". |
| 3 | A self-driving car's driving system | Narrow | Drives a car; cannot do other jobs. | Limited memory | Tracks nearby cars' speed and direction over recent moments; Hintze's example [4]; IBM agrees [1]. |
| 4 | An LLM chatbot (for example, ChatGPT) | Narrow (mainstream view; debated) | Broad within language tasks, but IBM classes it as narrow and states that current LLMs are not considered AGI [1][2]. | Limited memory | Uses the conversation so far, within its context window; IBM lists generative AI tools here [1]. |
| 5 | A voice assistant (for example, Siri or Alexa) | Narrow | Answers questions and controls apps and devices within set limits. | Limited memory | Keeps track of the recent request and context; IBM lists virtual assistants here [1]. |
| 6 | Netflix's recommendation engine | Narrow | Only recommends titles. | **Disputed**: IBM lists it as reactive [1]; a reasonable argument for limited memory | It uses your recent viewing to update recommendations, which looks like using the recent past. |

**Step-by-step reasoning for row 6 (the tricky one):**

1. *Capability:* it does one job, recommending titles, so it is **narrow**. Easy.
2. *Functionality:* IBM's explainer places it under reactive machines [1]. But the system uses what you watched recently, which matches the description of limited memory.
3. *Conclusion:* reasonable people (and sources) disagree. This is exactly why the functionality scheme is described as a popular taxonomy rather than a formal standard. When you classify with it, **state your reason**; the reason matters more than the label.

**Check your understanding of the pattern:** every row is **narrow** under Lens 1, and every row is **reactive or limited memory** under Lens 2. No real system lands in theory of mind or self-aware.

## Visual

![Two side-by-side panels. Lens 1, by capability: narrow AI (exists today), general AI (hypothetical), superintelligence (speculative). Lens 2, by functionality: reactive machines and limited memory (exist today), theory of mind and self-aware AI (hypothetical). A line in each panel marks where today's AI ends](../assets/images/types-of-ai-two-lenses.svg)

*Figure: Types of AI seen through two different lenses. The same system can be described with both. All AI that exists today is narrow, and works as a reactive or limited-memory system.* (Original diagram created for this module.)

## Common mistakes

1. **Mixing the two lenses into one ladder** (for example, "narrow, general, reactive, limited memory, superintelligent"). Fix: keep them separate. One lens asks *how broad*, the other asks *how it uses memory and understanding*. Every system gets a label from each.
2. **"ChatGPT can talk about anything, so it is general AI."** Fix: breadth of conversation is not the same as human-level ability across any task. The mainstream view, reflected in IBM's explainer, is that current LLMs are narrow AI and not AGI, although this is debated and there is no agreed test [1][2].
3. **"A system trained on past data has memory, so it is limited memory AI."** Fix: in the functionality scheme, "memory" means using the recent past *while operating* (like tracking nearby cars), not having been trained on old data.
4. **"Theory of mind and self-aware AI already exist, because chatbots talk about feelings."** Fix: both are hypothetical. Talking about feelings is generating likely text, not evidence of understanding minds or of consciousness.

## Try it yourself

### Activity 1: Classify with both lenses (apply + justify)

For each system, give a **capability** label and a **functionality** label, with a one-sentence reason for each. If a label cannot be decided from the description, say so and explain.

1. A robot vacuum cleaner that, during a cleaning session, builds a map of the room and avoids a chair leg it bumped into a minute ago.
2. A tic-tac-toe (noughts-and-crosses) program that looks at the current board and picks the best move.
3. A phone's face-unlock feature.
4. An imagined future robot that can learn any job a person can do (accountant, plumber, nurse) about as well as a person.
5. An imagined computer in a story that says "I know that I exist, and I feel lonely", and really does.

### Activity 2: Find and fix the errors (evaluate)

A classmate made this table. Find **four** errors and correct each one, explaining why.

| System | Capability | Functionality |
|---|---|---|
| Deep Blue | Superintelligence, because it beat the world chess champion | Reactive |
| Self-driving car | Narrow | Theory of mind, because it predicts what pedestrians will do |
| LLM chatbot | General AI, because it can write about any topic | Limited memory |
| Spam filter | Narrow | Limited memory, because it learned from millions of old emails |

### Activity 3: Two lenses, one system (compare + explain)

a) Explain to a friend, in three or four sentences, why "narrow" and "limited memory" are **not** competing answers to the same question. Use a self-driving car as your example.
b) A news headline says: **"New AI understands your emotions!"** The article describes software that looks at a photo of a face and outputs "happy", "sad" or "angry". Using both lenses, write two or three sentences classifying the software and explaining whether the headline is accurate.

## Answers

<details>
<summary>Show answers</summary>

**Activity 1**

1. **Narrow** (only cleans floors). **Limited memory**: it uses recent observations (the room map and the chair leg it bumped a minute ago) while it works.
2. **Narrow** (only plays one game). **Reactive**: it uses only the current board, like Deep Blue.
3. **Narrow** (only verifies a face). **Reactive**: it judges the current camera image. (It was trained on many faces and stores your enrolled face data, but it does not use a record of recent moments while deciding; accept "limited memory" only with a clear, reasoned argument.)
4. **General AI (AGI), hypothetical**: human-level ability across many different jobs. **Functionality: cannot be decided from the description.** It would at least need memory of the recent past to learn a job; whether it would need theory of mind or self-awareness is not agreed. Saying "cannot be decided, because the lenses ask different questions" is the best answer.
5. **Functionality: self-aware (hypothetical)**, because it is aware of its own existence and feelings. **Capability: cannot be decided from the description**: knowing it exists says nothing about how broad its abilities are. This system is fictional.

**Activity 2**

1. **Deep Blue is not superintelligence.** It was superhuman at one task (chess) only. Superintelligence means greatly exceeding humans in *virtually all* domains. Correct: **narrow**. (Its "reactive" label is correct.)
2. **The self-driving car is not theory of mind.** Predicting pedestrians' movement from their recent positions and speed is using the recent past, which is **limited memory**. Theory of mind would mean genuinely understanding the pedestrian's thoughts and intentions, which no current system does.
3. **The LLM chatbot is not general AI** under the mainstream view. Writing about any topic is breadth within language; it is classed as **narrow**, and current LLMs are not considered AGI (though this is debated and there is no agreed test). (Its "limited memory" label is correct.)
4. **The spam filter is not limited memory just because it was trained on old emails.** In the functionality scheme, memory means using the recent past while operating. A filter judging each email on its own features is **reactive**.

**Activity 3**

a) Example: "They answer different questions. 'Narrow' answers *how broad is it?*: a self-driving car only drives, so it is narrow. 'Limited memory' answers *does it use the recent past while working?*: the car tracks nearby cars over the last few moments, so it is limited memory. So the car is both narrow **and** limited memory, just as a car can be both small and electric."

b) Example: "By capability, it is **narrow** AI: it only labels facial expressions. By functionality, it is **reactive** (it judges one photo at a time), and it is **not** theory of mind: labeling an expression as 'sad' is not the same as understanding what the person feels or why. The headline is misleading; a more accurate one would be 'New AI labels facial expressions in photos'." (Accept "limited memory" if the learner argues it uses a sequence of recent video frames, as long as they say it is not theory of mind.)

</details>

## Optional extension

*Optional: not required for later topics.*

1. **Read the original.** Read Hintze's short 2016 article [4]. He writes that "the most basic types of AI systems are purely reactive". Do you agree that the four types form a progression from simple to advanced? What would a fifth type look like?
2. **Debate preparation.** Write two arguments for and two against the claim "Today's most advanced chatbots should count as general AI." Use the IBM page on AGI [2] as a starting point. Keep this for [Topic 10](10-future-of-ai.md), which discusses AGI and the future.

## Connections

- **Previous:** Topics [01](01-what-is-ai.md) to [04](04-generative-ai-and-llms.md) showed many AI systems, all built for particular tasks. This topic gave that observation a name (narrow AI) and added a second lens about memory and understanding.
- **Next:** [Topic 06](06-history-of-ai.md) tells the history of AI, including the 1997 Deep Blue match and the 2016 AlphaGo match mentioned here.
- **Later:** [Topic 09](09-limitations-and-misconceptions.md) tackles the misconceptions "AI is conscious" and "AI understands like humans"; [Topic 10](10-future-of-ai.md) returns to AGI and the debate about the future.

## Sources

1. IBM Data and AI Team (n.d.). *Understanding the different types of artificial intelligence.* IBM Think. https://www.ibm.com/think/topics/artificial-intelligence-types (accessed 2026-11-06). Supports: two classification schemes (capabilities: narrow, general, super; functionalities: reactive, limited memory, theory of mind, self-aware); narrow AI "is the only type of AI that exists today"; ChatGPT classed as narrow AI and as limited memory; Deep Blue and Netflix recommendation engine listed as reactive; generative AI tools, virtual assistants and self-driving cars listed as limited memory; "To date, Emotion AI is unable to understand and respond to human feelings"; weak AI / strong AI as alternative names.
2. IBM (n.d.). *What is artificial general intelligence (AGI)?* IBM Think. https://www.ibm.com/think/topics/artificial-general-intelligence (accessed 2026-11-06). Supports: AGI as a hypothetical stage able to "match or exceed the cognitive abilities of human beings across any task"; "no consensus among experts regarding what exactly should qualify as AGI"; "current LLMs are not considered AGI", with some researchers disagreeing.
3. Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies.* Oxford University Press. Supports: definition of superintelligence as "any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest". (Quotation confirmed via several independent search results quoting the book; the book itself was not re-read for this revision.)
4. Hintze, A. (2016, 14 November). *Understanding the four types of AI, from reactive robots to self-aware beings.* The Conversation. https://theconversation.com/understanding-the-four-types-of-ai-from-reactive-robots-to-self-aware-beings-67616 (accessed 2026-11-06). Supports: the four functionality types; Deep Blue (and AlphaGo) as reactive; self-driving cars as limited memory with temporary, unstored recent information; theory of mind as needed for social interaction; self-awareness linked to consciousness and probably far off.
