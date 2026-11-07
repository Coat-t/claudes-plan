# Sources Used

Consolidated list of every source checked while producing **Task 1** (core learning content), **Task 2** (study guide, test bank and supplements) and **Task 3** (teaching slides, which use only sources already listed here). All online sources were accessed on 2026-11-06 unless stated. Entries are grouped by where they were first used and **duplicates are merged** (same URL); "Also logged as" shows other keys. Each topic file also lists its own sources in a "Sources" section, and the study guide's [resources page](task-2/study-guide/resources.md) introduces the learner-facing videos and platforms.

**Reading the "Verified" field:** it says how each source was checked (page fetched, official listing, search results, or secondary source when the primary page blocked automated access). Facts confirmed only through secondary sources are also listed in [task-1/gaps-and-open-issues.md](task-1/gaps-and-open-issues.md).

**Original material:** all diagrams, the characters Pixel and Dr. Ada Okafor, the fictional companies and products in activities, and all "illustrative (made-up)" figures were created for this module.

## Contents

- [Task 1 core content (topics 01–05)](#task-1-core-content-topics-0105)
- [Task 1 core content (topics 06–10)](#task-1-core-content-topics-0610)
- [Diagrams](#diagrams)
- [Task 2 supplements (activities)](#task-2-supplements-activities)
- [Task 2 study guide: videos, platforms and reading](#task-2-study-guide-videos-platforms-and-reading)
- [Task 2 test bank](#task-2-test-bank)

## Task 1 core content (topics 01–05)

1. **IBM (n.d.). *What is artificial intelligence (AI)?* IBM Think.**
   - URL: <https://www.ibm.com/think/topics/artificial-intelligence>
   - Key: `IBM-AI` (also logged as: IBM-WHAT-IS-AI)
   - Accessed: 2026-11-06
   - Verified: fetched page; first sentence quoted verbatim | HTTP 200 re-checked 2026-11-06; "Weak AI vs. Strong AI" section per resources agent
   - Supports: AI definition ("simulate human learning, comprehension, problem solving, decision making, creativity and autonomy"); AI > ML > DL > GenAI as nested concepts | optional reading for capability lens
   - Used in: topics/01-what-is-ai.md (Explanation 1, Sources 1) | task-2/study-guide/mission-07-sorting-the-robots.md [WATCH] note; task-2/study-guide/resources.md C2

2. **OECD.AI (2023, 29 Nov). *Updates to the OECD's definition of an AI system explained.* OECD.AI Policy Observatory.**
   - URL: <https://oecd.ai/en/wonk/ai-system-definition-update>
   - Key: `OECD-AI-DEF-2023`
   - Accessed: 2026-11-06
   - Verified: fetched page (definition shown as tracked changes; paraphrased, not quoted in full)
   - Supports: updated OECD AI-system definition (objectives; infers from input how to generate outputs: predictions, content, recommendations, decisions; varying autonomy and adaptiveness)
   - Used in: topics/01-what-is-ai.md (Explanation 2)

3. **Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.**
   - URL: <https://aima.cs.berkeley.edu/>
   - Key: `AIMA-4`
   - Accessed: 2026-11-06
   - Verified: official book website (title, edition, authors, TOC incl. Ch. 2 "Intelligent Agents"); agent framing confirmed via university lecture notes summarising Ch. 1 (e.g. NUS CS3243); book text not read directly
   - Supports: AI framed around agents that perceive and act
   - Used in: topics/01-what-is-ai.md (Explanation 3)

4. **Kumaran, N. (2022, 28 May). *Understanding Gmail's spam filters.* Google Workspace Blog.**
   - URL: <https://workspace.google.com/blog/identity-and-security/an-overview-of-gmails-spam-filters>
   - Key: `GOOGLE-GMAIL-SPAM-2022`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: Gmail uses "machine learning powered by user feedback"; blocks >99.9% of spam, phishing, malware (Google's own claim)
   - Used in: topics/01-what-is-ai.md (Explanation 4); topics/02-how-ai-operates.md (Explanation 3)

5. **Google (2017, 4 May). *How machine learning in G Suite makes people more productive.* The Keyword.**
   - URL: <https://blog.google/products-and-platforms/products/workspace/how-machine-learning-g-suite-makes-people-more-productive/>
   - Key: `GOOGLE-GSUITE-ML-2017`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: Gmail moved from ~a decade of rule-based filtering to ML-generated rules from 2014; ML "continually regenerate[s] the spam filter"
   - Used in: topics/02-how-ai-operates.md (Explanation 3)

6. **O'Toole, G. (2024, 20 June). *Quote origin: As soon as it works, no one calls it AI anymore.* Quote Investigator.**
   - URL: <https://quoteinvestigator.com/2024/06/20/not-ai/>
   - Key: `QI-AI-EFFECT-2024`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: AI effect history; Tesler's Theorem via Hofstadter 1979; earliest verified version Raphael 1971; McCarthy attribution second-hand (2011)
   - Used in: topics/01-what-is-ai.md (Explanation 5)

7. **Yale University Dept. of Computer Science (2015). *Expert Systems* (CS 458 lecture notes).**
   - URL: <https://zoo.cs.yale.edu/classes/cs458/lectures/old2015/ExpertSystems.html>
   - Key: `YALE-EXPERT-SYSTEMS`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: MYCIN (Shortliffe, Stanford, early 1970s; ~600 IF-THEN rules; example Bacteroides rule; not used in practice)
   - Used in: topics/02-how-ai-operates.md (Explanation 2)

8. **Google DeepMind (n.d.). *AlphaGo.***
   - URL: <https://deepmind.google/research/breakthroughs/alphago/>
   - Key: `DEEPMIND-ALPHAGO`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: AlphaGo "combines deep neural networks with advanced search algorithms"; March 2016 Seoul match vs Lee Sedol (4-1) | March 2016 Seoul 4-1; move 37; human games + self-play + search
   - Used in: topics/02-how-ai-operates.md (Explanation 4) | topics/06, 09

9. **Microsoft (n.d.). *AI for Beginners: 12 Weeks, 24 Lessons.* GitHub.**
   - URL: <https://github.com/microsoft/AI-For-Beginners>
   - Key: `MS-AI-BEGINNERS`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: symbolic AI (knowledge representation, expert systems) and neural networks (perceptron, MLP) as curriculum strands; further study
   - Used in: topics/02-how-ai-operates.md (Sources); topics/03-ml-neural-networks-deep-learning.md (Optional extension)

10. **Google for Developers (n.d.). *Supervised Learning* (Intro to ML course).**
   - URL: <https://developers.google.com/machine-learning/intro-to-ml/supervised>
   - Key: `GOOGLE-ML-SUPERVISED`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: definitions of features, label, labeled examples, training, evaluation, inference
   - Used in: topics/02-how-ai-operates.md; topics/03-ml-neural-networks-deep-learning.md (Explanation 2)

11. **Google for Developers (n.d.). *What is machine learning?* (Intro to ML course).**
   - URL: <https://developers.google.com/machine-learning/intro-to-ml/what-is-ml>
   - Key: `GOOGLE-ML-WHAT-IS-ML`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: definitions of ML, supervised, unsupervised, reinforcement learning, generative AI
   - Used in: topics/03-ml-neural-networks-deep-learning.md (Explanation 1-2)

12. **Google for Developers (n.d.). *Overfitting* (Machine Learning Crash Course).**
   - URL: <https://developers.google.com/machine-learning/crash-course/overfitting/overfitting>
   - Key: `GOOGLE-MLCC-OVERFITTING`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: overfitting definition and lab-invention analogy; training/validation/test sets; shuffle before split; 70/15/15 example
   - Used in: topics/03-ml-neural-networks-deep-learning.md (Explanation 3-4)

13. **Google for Developers (n.d.). *Neural networks: Activation functions* (Machine Learning Crash Course).**
   - URL: <https://developers.google.com/machine-learning/crash-course/neural-networks/activation-functions>
   - Key: `GOOGLE-MLCC-ACTIVATION`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: sigmoid (0-1), ReLU max(0,x); nonlinearity needed ("linear operations performed on linear operations are still linear")
   - Used in: topics/03-ml-neural-networks-deep-learning.md (Explanation 5-6)

14. **Rosenblatt, F. (1958). The perceptron: A probabilistic model for information storage and organization in the brain. *Psychological Review*, 65(6), 386-408. doi:10.1037/h0042519**
   - URL: <https://doi.org/10.1037/h0042519>
   - Key: `ROSENBLATT-1958`
   - Accessed: 2026-11-06
   - Verified: search results (PubMed PMID 13602029 listing, bibliographic records); full text not read
   - Supports: perceptron published 1958
   - Used in: topics/03-ml-neural-networks-deep-learning.md (Explanation 5)

15. **IBM (n.d.). *What is deep learning?* IBM Think.**
   - URL: <https://www.ibm.com/think/topics/deep-learning>
   - Key: `IBM-DL`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: DL = "subset of machine learning driven by multilayered neural networks"; "at least 4 layers"; hidden layers learn hierarchical features; "black boxes"; vs manual feature engineering
   - Used in: topics/03-ml-neural-networks-deep-learning.md (Explanation 6-7)

16. **Google for Developers (n.d.). *Background: What is a generative model?* (GAN course).**
   - URL: <https://developers.google.com/machine-learning/gan/generative>
   - Key: `GOOGLE-GAN-GENERATIVE`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: generative vs discriminative definitions and examples
   - Used in: topics/04-generative-ai-and-llms.md (Explanation 1)

17. **IBM (n.d.). *What is generative AI?* IBM Think.**
   - URL: <https://www.ibm.com/think/topics/generative-ai>
   - Key: `IBM-GENAI`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: GenAI definition; relies on deep learning; ELIZA as pattern-matching chatbot; training stages (foundation model pre-training, tuning, RLHF); hallucination definition + lawyer example. (NOT used: page's claim that Markov chains underpinned Google autocomplete 2004 - unverified.)
   - Used in: topics/04-generative-ai-and-llms.md (Explanation 1, 2, 6, 8)

18. **Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27, 379-423, 623-656.**
   - URL: <https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf>
   - Key: `SHANNON-1948`
   - Accessed: 2026-11-06
   - Verified: downloaded PDF and read Section 3 text directly (pdftotext)
   - Supports: 1948 word-level Markov approximation of English ("word transition probabilities are correct but no further structure is included") - pre-DL generative method (gap 6)
   - Used in: topics/04-generative-ai-and-llms.md (Explanation 2)

19. **Vaswani, A., et al. (2017). *Attention Is All You Need.* arXiv:1706.03762.**
   - URL: <https://arxiv.org/abs/1706.03762>
   - Key: `VASWANI-2017`
   - Accessed: 2026-11-06
   - Verified: fetched arXiv abstract page | fetched arXiv page (v1 12 June 2017)
   - Supports: transformer introduced June 2017; "based solely on attention mechanisms" | transformer 2017
   - Used in: topics/04-generative-ai-and-llms.md (Explanation 3) | topics/06

20. **Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., et al. (2022). *Training language models to follow instructions with human feedback.* arXiv:2203.02155.**
   - URL: <https://arxiv.org/abs/2203.02155>
   - Key: `OUYANG-2022`
   - Accessed: 2026-11-06
   - Verified: fetched arXiv abstract page
   - Supports: SFT on demonstrations then RLHF from rankings; 1.3B InstructGPT preferred over 175B GPT-3, 100x fewer parameters
   - Used in: topics/04-generative-ai-and-llms.md (Explanation 6)

21. **Brown, T. B., et al. (2020). *Language Models are Few-Shot Learners.* arXiv:2005.14165.**
   - URL: <https://arxiv.org/abs/2005.14165>
   - Key: `BROWN-2020-GPT3`
   - Accessed: 2026-11-06
   - Verified: fetched arXiv abstract page
   - Supports: GPT-3 (May 2020) has 175 billion parameters
   - Used in: topics/04-generative-ai-and-llms.md (Explanation 3)

22. **Google for Developers (n.d.). *Introduction to Large Language Models.***
   - URL: <https://developers.google.com/machine-learning/resources/intro-llms>
   - Key: `GOOGLE-INTRO-LLM`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: token = word/subword/character; ~3/4 of a word per English token; LM assigns probabilities to completions
   - Used in: topics/04-generative-ai-and-llms.md (Explanation 4-5)

23. **OpenAI (n.d.). *What are tokens and how to count them?* OpenAI Help Center.**
   - URL: <https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them>
   - Key: `OPENAI-TOKENS`
   - Accessed: 2026-11-06
   - Verified: direct fetch blocked (HTTP 403); rules of thumb confirmed via search-result extracts of the same page
   - Supports: 1 token ~ 4 characters ~ 3/4 word; 100 tokens ~ 75 words (English)
   - Used in: topics/04-generative-ai-and-llms.md (Explanation 4)

24. **IBM Data and AI Team (n.d.). *Understanding the different types of artificial intelligence.* IBM Think.**
   - URL: <https://www.ibm.com/think/topics/artificial-intelligence-types>
   - Key: `IBM-AI-TYPES`
   - Accessed: 2026-11-06
   - Verified: fetched page (twice)
   - Supports: capability vs functionality schemes; narrow AI only type existing; ChatGPT narrow + limited memory; Deep Blue & Netflix recommendation reactive; GenAI tools, assistants, self-driving cars limited memory; Emotion AI can't understand feelings; weak/strong AI synonyms
   - Used in: topics/05-types-of-ai.md (throughout)

25. **IBM (n.d.). *What is artificial general intelligence (AGI)?* IBM Think.**
   - URL: <https://www.ibm.com/think/topics/artificial-general-intelligence>
   - Key: `IBM-AGI`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: AGI definition; no expert consensus; "current LLMs are not considered AGI" with dissent
   - Used in: topics/05-types-of-ai.md (Explanation 2)

26. **Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies.* Oxford University Press.**
   - Location: (book; no URL)
   - Key: `BOSTROM-2014`
   - Accessed: 2026-11-06
   - Verified: definition wording confirmed via multiple independent search results quoting the book; book not read directly
   - Supports: superintelligence = "any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest"
   - Used in: topics/05-types-of-ai.md (Explanation 2)

27. **Hintze, A. (2016, 14 Nov). *Understanding the four types of AI, from reactive robots to self-aware beings.* The Conversation.**
   - URL: <https://theconversation.com/understanding-the-four-types-of-ai-from-reactive-robots-to-self-aware-beings-67616>
   - Key: `HINTZE-2016`
   - Accessed: 2026-11-06
   - Verified: fetched page (twice; exact phrases checked)
   - Supports: four functionality types; Deep Blue reactive; AlphaGo discussed in reactive section; self-driving cars limited memory; theory of mind; self-awareness; "The most basic types of AI systems are purely reactive"
   - Used in: topics/05-types-of-ai.md (Explanation 3, worked example, optional extension)

28. **Own verification script (breadth-first search) written for this module.**
   - Location: n/a (a temporary working file (not included))
   - Key: `FWGC-BFS-CHECK`
   - Accessed: 2026-11-06
   - Verified: ran script: 16 arrangements, 10 safe, minimum 7 crossings, exactly 2 shortest solutions
   - Supports: river-crossing facts
   - Used in: topics/02-how-ai-operates.md (Explanation 2 mini-trace, Activity 3)

## Task 1 core content (topics 06–10)

29. **Turing, A. M. (1950). *Computing Machinery and Intelligence*. Mind, 59(236), 433-460.**
   - URL: <https://academic.oup.com/mind/article/LIX/236/433/986238>
   - Key: `TURING-1950`
   - Accessed: 2026-11-06
   - Verified: fetched publisher page
   - Supports: 1950, Mind, imitation game
   - Used in: topics/06 (Start, timeline), 09 (worked example)

30. **Dartmouth College (n.d.). *Artificial Intelligence (AI) Coined at Dartmouth*.**
   - URL: <https://home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth>
   - Key: `DARTMOUTH-COINED`
   - Accessed: 2026-11-06
   - Verified: fetched page (no proposal date on page; 31 Aug 1955 proposal date is known stable fact; jmc.stanford.edu PDF failed with TLS cert error)
   - Supports: summer 1956 Dartmouth project; McCarthy; "every aspect of learning..." conjecture
   - Used in: topics/06

31. **Wikipedia contributors. *Logic Theorist*; Shrager, J. (2026) arXiv:2603.13514 (search summary only)**
   - URL: <https://en.wikipedia.org/wiki/Logic_Theorist>
   - Key: `LOGIC-THEORIST`
   - Accessed: 2026-11-06
   - Verified: search results only
   - Supports: Newell/Shaw/Simon 1956; 38 of first 52 theorems of Principia ch.2; runs reported 1957
   - Used in: topics/06

32. **Rosenblatt, F. (1958). The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain. Psychological Review, 65(6), 386-408.**
   - Location: (none fetched; bibliographic data via search results)
   - Key: `ROSENBLATT-1958`
   - Accessed: 2026-11-06
   - Verified: search results (citation; July 1958 Navy press event and NYT coverage)
   - Supports: perceptron 1958; press hype
   - Used in: topics/06

33. **Weizenbaum, J. (1966). ELIZA - a computer program for the study of natural language communication between man and machine. Communications of the ACM, 9(1), 36-45.**
   - URL: <https://courses.cs.umbc.edu/331/papers/eliza.html>
   - Key: `WEIZENBAUM-1966`
   - Accessed: 2026-11-06
   - Verified: search results (DOI 10.1145/365153.365168) | transcript as cross-checked by resources agent (UMBC copy and masswerk test page); first lines also present in the Hay page's CACM_1966_CONVERSATION constant (read by me)
   - Supports: ELIZA 1966 paper, DOCTOR script, pattern matching | fallback transcript in Mission 08
   - Used in: topics/06, 09 | task-2/study-guide/mission-08-time-machine.md Activity 8.2 fallback

34. **Minsky, M. & Papert, S. (1969). *Perceptrons*. MIT Press.**
   - Location: (secondary pages via search)
   - Key: `MINSKY-PAPERT-1969`
   - Accessed: 2026-11-06
   - Verified: search results; publisher MIT Press is known stable fact
   - Supports: 1969; single-layer limitation (XOR); debated role in decline
   - Used in: topics/06

35. **Lighthill, J. (1973). Artificial Intelligence: A General Survey. In Artificial Intelligence: A Paper Symposium. Science Research Council.**
   - URL: <https://en.wikipedia.org/wiki/Lighthill_report>
   - Key: `LIGHTHILL-1973`
   - Accessed: 2026-11-06
   - Verified: search results
   - Supports: 1973; SRC-commissioned; combinatorial explosion; UK funding cuts
   - Used in: topics/06

36. **Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.**
   - Location: (book; not fetched)
   - Key: `AIMA-4`
   - Accessed: 2026-11-06
   - Verified: known stable reference, not fetched
   - Supports: general history narrative (winters, expert systems); general application descriptions
   - Used in: topics/06, 07

37. **Wikipedia contributors. *Xcon*; Middlesex Univ. course notes "Configuration with R1/XCon"**
   - URL: <https://en.wikipedia.org/wiki/Xcon>
   - Key: `XCON`
   - Accessed: 2026-11-06
   - Verified: search results
   - Supports: McDermott/CMU; DEC use from 1980 for VAX configuration; savings ~$25M/yr (estimates up to $40M)
   - Used in: topics/06

38. **Rumelhart, D. E., Hinton, G. E. & Williams, R. J. (1986). Learning representations by back-propagating errors. Nature, 323, 533-536.**
   - URL: <https://ui.adsabs.harvard.edu/abs/1986Natur.323..533R/abstract>
   - Key: `BACKPROP-1986`
   - Accessed: 2026-11-06
   - Verified: search results (ADS abstract)
   - Supports: 1986 popularization of backpropagation
   - Used in: topics/06

39. **IBM (n.d.). *Deep Blue*. IBM History.**
   - URL: <https://www.ibm.com/history/deep-blue>
   - Key: `IBM-DEEPBLUE`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: May 1997, 3.5-2.5; 1996 match 4-2 Kasparov; 200 million positions/s
   - Used in: topics/06, 09

40. **Krizhevsky, A., Sutskever, I. & Hinton, G. E. (2012). ImageNet Classification with Deep Convolutional Neural Networks. NeurIPS 25.**
   - URL: <https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks>
   - Key: `ALEXNET-2012`
   - Accessed: 2026-11-06
   - Verified: fetched page (60M params, GPU); 15.3% vs 26.2% confirmed via search of abstract text
   - Supports: AlexNet results, ImageNet 1,000 classes
   - Used in: topics/06, 09

41. **OpenAI (2022). *Introducing ChatGPT* (30 November 2022).**
   - URL: <https://openai.com/index/chatgpt/>
   - Key: `OPENAI-CHATGPT-2022`
   - Accessed: 2026-11-06
   - Verified: page returned 403; date confirmed via multiple search results
   - Supports: release 30 Nov 2022 as research preview
   - Used in: topics/06, 09

42. **Gomez-Uribe, C. A. & Hunt, N. (2015). The Netflix Recommender System: Algorithms, Business Value, and Innovation. ACM TMIS 6(4), Art. 13.**
   - URL: <https://gwern.net/doc/reinforcement-learning/exploration/2015-gomezuribe.pdf>
   - Key: `NETFLIX-2015`
   - Accessed: 2026-11-06
   - Verified: fetched PDF and grepped extracted text
   - Supports: "influences choice for about 80% of hours streamed"; ">$1B per year"; 2 of 3 hours on homepage
   - Used in: topics/07

43. **US FDA (n.d.). *Artificial Intelligence-Enabled Medical Devices* (list).**
   - URL: <https://www.fda.gov/medical-devices/artificial-intelligence-enabled-medical-devices/list-artificial-intelligence-enabled-medical-devices>
   - Key: `FDA-AI-DEVICES`
   - Accessed: 2026-11-06
   - Verified: fetched (truncated; radiology dominates; "not a comprehensive resource")
   - Supports: existence of list; radiology most common
   - Used in: topics/07

44. **AuntMinnie (2026). *Radiology dominates thirty years of FDA AI device approvals*.**
   - URL: <https://www.auntminnie.com/imaging-informatics/artificial-intelligence/article/15830219/radiology-dominates-thirty-years-of-fda-ai-device-approvals>
   - Key: `AUNTMINNIE-FDA-2026`
   - Accessed: 2026-11-06
   - Verified: search result only
   - Supports: ~1,430 AI devices by end 2025; ~76% radiology
   - Used in: topics/07

45. **MobiHealthNews (2018). *FDA permits marketing of AI software that autonomously detects diabetic retinopathy*; BioSpace (2018).**
   - URL: <https://www.mobihealthnews.com/news/fda-permits-marketing-ai-software-autonomously-detects-diabetic-retinopathy>
   - Key: `IDX-DR-2018`
   - Accessed: 2026-11-06
   - Verified: search results
   - Supports: April 2018; first autonomous AI screening device; ~87.4% / ~89.5%
   - Used in: topics/07

46. **Obermeyer, Z., Powers, B., Vogeli, C. & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. Science, 366(6464), 447-453.**
   - URL: <https://chmi.berkeley.edu/news/dissecting-racial-bias-in-an-algorithm-used-to-manage-the-health-of-populations>
   - Key: `OBERMEYER-2019`
   - Accessed: 2026-11-06
   - Verified: fetched Berkeley summary (science.org 403); 17.7%->46.5% seen only in search snippets (NOT used in text)
   - Supports: cost proxy; Black patients identified for extra care cut by more than half; reformulation removes bias
   - Used in: topics/07, 08, 09

47. **Waymo (2026). *Safety Impact* data hub.**
   - URL: <https://waymo.com/safety/impact/>
   - Key: `WAYMO-SAFETY`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: 271.3M rider-only miles through June 2026, 5 metros; -82% any-injury crashes vs benchmark; caveats
   - Used in: topics/07

48. **CNN (2019). NTSB findings on Uber self-driving crash; Engadget (2019).**
   - URL: <https://www.cnn.com/2019/11/19/tech/uber-crash-ntsb>
   - Key: `NTSB-UBER-2019`
   - Accessed: 2026-11-06
   - Verified: search results
   - Supports: March 2018 Tempe fatality; late detection; distracted safety driver; safety culture and regulators
   - Used in: topics/07, 08

49. **Buolamwini, J. & Gebru, T. (2018). Gender Shades. PMLR 81:77-91.**
   - URL: <https://proceedings.mlr.press/v81/buolamwini18a.html>
   - Key: `GENDER-SHADES-2018`
   - Accessed: 2026-11-06
   - Verified: fetched abstract page
   - Supports: 3 commercial classifiers; IJB-A/Adience 79.6%/86.2% lighter; up to 34.7% vs max 0.8% error
   - Used in: topics/08, 09

50. **MIT Media Lab (n.d.). *Gender Shades* project overview.**
   - URL: <https://www.media.mit.edu/projects/gender-shades/overview/>
   - Key: `GENDER-SHADES-MIT`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: 1,270 faces; parliamentarians of 3 African + 3 European countries (vendor names IBM/Microsoft/Face++ from paper body, known stable fact)
   - Used in: topics/08

51. **Dastin, J. (2018, 10 Oct). Amazon scraps secret AI recruiting tool that showed bias against women. Reuters (via CNBC).**
   - URL: <https://www.cnbc.com/2018/10/10/amazon-scraps-a-secret-ai-recruiting-tool-that-showed-bias-against-women.html>
   - Key: `REUTERS-AMAZON-2018`
   - Accessed: 2026-11-06
   - Verified: search results (syndicated copies)
   - Supports: penalized "women's"; 10 yrs mostly male resumes; never used alone by recruiters
   - Used in: topics/08, 09

52. **Hunton Andrews Kurth (2024). Dutch Regulator Fines Clearview AI 30.5 Million Euros; JURIST (2024).**
   - URL: <https://www.hunton.com/privacy-and-cybersecurity-law-blog/dutch-regulator-fines-clearview-ai-30-5-million-euros>
   - Key: `CLEARVIEW-NL-2024`
   - Accessed: 2026-11-06
   - Verified: search results
   - Supports: EUR 30.5M fine (announced 3 Sep 2024), scraped faces, GDPR
   - Used in: topics/08

53. **World Economic Forum (2025, 8 Jan). Future of Jobs Report 2025 press release.**
   - URL: <https://www.weforum.org/press/2025/01/future-of-jobs-report-2025-78-million-new-job-opportunities-by-2030-but-urgent-upskilling-needed-to-prepare-workforces/>
   - Key: `WEF-FOJ-2025`
   - Accessed: 2026-11-06
   - Verified: WEF pages 403 to fetch; figures via multiple consistent search results
   - Supports: 170M created (14%), 92M displaced (8%), net 78M, 2025-2030; 22% churn; >1,000 employers, >14M workers, 55 economies; multiple macro drivers; ~two-fifths skills change
   - Used in: topics/08, 09

54. **Mata v. Avianca, Inc., No. 1:22-cv-01461 (S.D.N.Y. 22 June 2023); Bloomberg Law report.**
   - URL: <https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54>
   - Key: `MATA-AVIANCA-2023`
   - Accessed: 2026-11-06
   - Verified: Justia 403; search results (Reuters syndicated, Bloomberg Law)
   - Supports: six fake ChatGPT citations; $5,000 total sanction; bad faith
   - Used in: topics/08, 09

55. **International Energy Agency (2025, 10 April). AI is set to drive surging electricity demand from data centres... (Energy and AI press release)**
   - URL: <https://www.iea.org/news/ai-is-set-to-drive-surging-electricity-demand-from-data-centres-while-offering-the-potential-to-transform-how-the-energy-sector-works>
   - Key: `IEA-ENERGY-AI-2025`
   - Accessed: 2026-11-06
   - Verified: fetched page (415 TWh 2024 baseline NOT on page; not used)
   - Supports: ~945 TWh by 2030 (> Japan today); AI-optimised DC demand >4x; emissions small/possibly offset
   - Used in: topics/08

56. **CNN (2024, 16 May). Arup revealed as victim of $25 million deepfake scam; SCMP (2024).**
   - URL: <https://edition.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk>
   - Key: `ARUP-DEEPFAKE-2024`
   - Accessed: 2026-11-06
   - Verified: search results
   - Supports: deepfake video call; 15 transfers HK$200M (~US$25M); Jan 2024
   - Used in: topics/08

57. **Kalai, A. T., Nachum, O., Vempala, S. S. & Zhang, E. (2025). Why Language Models Hallucinate. arXiv:2509.04664.**
   - URL: <https://arxiv.org/abs/2509.04664>
   - Key: `KALAI-2025`
   - Accessed: 2026-11-06
   - Verified: fetched arXiv page
   - Supports: training/evaluation reward guessing over admitting uncertainty
   - Used in: topics/09

58. **Szegedy, C. et al. (2013). Intriguing properties of neural networks. arXiv:1312.6199.**
   - URL: <https://arxiv.org/abs/1312.6199>
   - Key: `SZEGEDY-2013`
   - Accessed: 2026-11-06
   - Verified: fetched arXiv page
   - Supports: adversarial examples; transfer across networks
   - Used in: topics/09

59. **European Commission (n.d.). AI Act - Shaping Europe's digital future (regulatory framework for AI).**
   - URL: <https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai>
   - Key: `EC-AI-ACT` (also logged as: EC-AI-ACT-PAGE)
   - Accessed: 2026-11-06
   - Verified: fetched twice | HTTP 200 re-checked 2026-11-06; content (tiers, dates, Omnibus) taken from Topic 10, which fetched it
   - Supports: entry into force 1 Aug 2024; four risk levels + examples; 9 prohibited practices; high-risk areas; dates 2 Feb 2025, 2 Aug 2025, Aug 2026 (general/transparency), Dec 2026 (nudification/CSAM ban), 2 Dec 2027 (Annex III), 2 Aug 2028 (Annex I); AI Omnibus adopted by EC 19 Nov 2025, political agreement 7 May 2026, in force 27 July 2026 | further reading link; Mission 12 content via Topic 10
   - Used in: topics/10 | task-2/study-guide/resources.md C6; task-2/study-guide/mission-12 (content via topic 10)

60. **Regulation (EU) 2024/1689 of 13 June 2024 (Artificial Intelligence Act). OJ L, 12.7.2024.**
   - URL: <https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng>
   - Key: `EU-AI-ACT-OJ`
   - Accessed: 2026-11-06
   - Verified: fetched first 100k chars (title, dates)
   - Supports: official title, adoption and publication dates
   - Used in: topics/10

61. **Future of Life Institute. EU AI Act Explorer, Articles 99 and 113 (unofficial consolidated text)**
   - URL: <https://artificialintelligenceact.eu/article/99/>
   - Key: `FLI-AIACT-ART99-113`
   - Accessed: 2026-11-06
   - Verified: fetched pages
   - Supports: fines EUR 35M/7% and 15M/3%; amended application dates
   - Used in: topics/10

62. **Gibson Dunn (2026, 27 May). EU AI Act Omnibus Agreement - Postponed High-Risk Deadlines and Other Key Changes.**
   - URL: <https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/>
   - Key: `GIBSONDUNN-OMNIBUS-2026`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: original dates (2 Aug 2026 / 2 Aug 2027) vs new; Art 50 unchanged; watermark grace to 2 Dec 2026; AI literacy softened; new prohibition; provisional agreement 6 May 2026
   - Used in: topics/10

63. **Sidley Austin Data Matters (2026, 22 June). EU Lawmakers Reach Provisional Agreement to Delay Key EU AI Act Obligations.**
   - URL: <https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/>
   - Key: `SIDLEY-OMNIBUS-2026`
   - Accessed: 2026-11-06
   - Verified: fetched page
   - Supports: EP vote 16 June 2026; adoption steps; same dates
   - Used in: topics/10

64. **OECD.AI (n.d.). OECD AI Principles overview.**
   - URL: <https://oecd.ai/en/ai-principles>
   - Key: `OECD-AI-PRINCIPLES`
   - Accessed: 2026-11-06
   - Verified: fetched page | HTTP 200 re-checked 2026-11-06
   - Supports: adopted 2019, updated May 2024; 5 principles + 5 recommendations; 47 adherents | further reading link
   - Used in: topics/10 | task-2/study-guide/resources.md C6

65. **UNESCO (n.d.). Recommendation on the Ethics of Artificial Intelligence.**
   - URL: <https://www.unesco.org/en/artificial-intelligence/recommendation-ethics>
   - Key: `UNESCO-REC-2021` (also logged as: UNESCO-AI-ETHICS)
   - Accessed: 2026-11-06
   - Verified: fetched page | HTTP 200 re-checked 2026-11-06
   - Supports: Nov 2021, 193 member states, first global standard, 4 values, 10 principles, policy areas | further reading link
   - Used in: topics/10 | task-2/study-guide/resources.md C6

66. **Grace, K. et al. (2024). Thousands of AI Authors on the Future of AI. arXiv:2401.02843.**
   - URL: <https://arxiv.org/abs/2401.02843>
   - Key: `GRACE-2024-SURVEY`
   - Accessed: 2026-11-06
   - Verified: fetched arXiv page
   - Supports: 2,778 respondents; 10% by 2027 / 50% by 2047; 13 years earlier; full labor automation 50% by 2116; wide disagreement
   - Used in: topics/10

67. **Morris, M. R. et al. (2023). Levels of AGI. arXiv:2311.02462.**
   - URL: <https://arxiv.org/abs/2311.02462>
   - Key: `MORRIS-LEVELS-AGI-2023`
   - Accessed: 2026-11-06
   - Verified: search results and coverage (not fetched directly)
   - Supports: performance x generality levels; 2023 chatbots = Emerging AGI
   - Used in: topics/10

68. **Council of Europe (2024). Council of Europe opens first ever global treaty on AI for signature.**
   - URL: <https://www.coe.int/it/web/portal/-/council-of-europe-opens-first-ever-global-treaty-on-ai-for-signature>
   - Key: `COE-AI-CONVENTION-2024`
   - Accessed: 2026-11-06
   - Verified: search results
   - Supports: Framework Convention adopted 17 May 2024, opened for signature 5 Sep 2024, first legally binding international AI treaty
   - Used in: topics/10

## Diagrams

69. **Chollet, F. (2017). *Deep Learning with Python* (1st ed.), section 1.1.2 and Figure 1.2 "Machine learning: a new programming paradigm". Manning Publications.**
   - URL: <https://www.perlego.com/book/1469354/deep-learning-with-python-pdf>
   - Key: `CHOLLET-DLWP-2017`
   - Accessed: 2026-11-06
   - Verified: web search returned the book's own text via Perlego listing: "humans input rules (a program) and data ... and out come answers"; "with machine learning, humans input data as well as the answers expected from the data, and out come the rules". Publisher page not fetched.
   - Supports: the "rules + data -> answers" vs "data + answers -> rules" framing of traditional programming vs machine learning
   - Used in: task-1/assets/images/rules-vs-learning.svg (and the task-2 copy)

70. **Hintze, A. (2016, November 14). *Understanding the four types of AI, from reactive robots to self-aware beings*. The Conversation (republished by TechXplore and Robohub).**
   - URL: <https://techxplore.com/news/2016-11-ai-reactive-robots-self-aware.pdf>
   - Key: `HINTZE-2016`
   - Accessed: 2026-11-06
   - Verified: web search; republications list the four types (reactive machines, limited memory, theory of mind, self-awareness) under Hintze's name, TechXplore dated 14 Nov 2016. Original Conversation page not fetched.
   - Supports: the functionality lens (four types; Deep Blue as a reactive machine; self-driving cars as limited memory); the note that it is a popular-press taxonomy
   - Used in: task-1/assets/images/types-of-ai-two-lenses.svg (and the task-2 copy)

71. **Original computation (diagrams agent). Breadth-first search over the 16 farmer/wolf/goat/cabbage states.**
   - Location: n/a (script: a temporary working file (not included))
   - Key: `RIVER-BFS-COMPUTED`
   - Accessed: 2026-11-06
   - Verified: ran with python3 -I; result: 10 safe states, 6 unsafe (FW|GC, FC|WG, F|WGC, WGC|F, WG|FC, GC|FW), 10 edges, exactly two shortest solutions of 7 crossings
   - Supports: every state, edge and the "two 7-crossing solutions" claim in the river-crossing diagram
   - Used in: task-1/assets/images/river-crossing-state-graph.svg (and the task-2 copy)

72. **Timeline dates (Turing 1950, Dartmouth 1956, perceptron 1958, ELIZA 1966, winters ~1974-80 and ~1987-93, Deep Blue 1997, AlexNet 2012, AlphaGo 2016, Transformer 2017, ChatGPT 2022) taken from SPEC.md topic 06.**
   - Location: n/a
   - Key: `TIMELINE-FROM-SPEC`
   - Accessed: 2026-11-06
   - Verified: NOT independently re-verified by the diagrams agent (well-known dates); the topic-06 author should cite primary/authoritative sources for them
   - Supports: ai-history-timeline.svg labels
   - Used in: task-1/assets/images/ai-history-timeline.svg (and the task-2 copy)

## Task 2 supplements (activities)

73. **Alcuin of York (attributed) (c. 800; oldest surviving manuscript late 9th century). *Propositiones ad acuendos juvenes* (Problems to sharpen the young), Problem 18 "De lupo et capra et fasciculo cauli" (the wolf, the goat and the bundle of cabbages).**
   - URL: <https://en.wikipedia.org/wiki/Propositiones_ad_Acuendos_Juvenes>
   - Key: `ALCUIN-PROPOSITIONES`
   - Accessed: 2026-11-06
   - Verified: fetched both pages. They say the text is "attributed to Alcuin of York" (died 804), the oldest known copy "dates from the late 9th century", Problem 18 is the wolf, goat and cabbage problem, it is the "earliest known occurrence" of the puzzle, the puzzle "dates back to at least the 9th century AD", and the solution takes "seven crossings: four forward and three back" with two solutions (wolf or cabbage first). Web search results (ProofWiki Problem 18 page, bosburyhistoryresource.org.uk: "Alcuin of York (735-804) produced his puzzle book for the Emperor") agree. The date "c. 800" is an inference from Alcuin's lifetime (d. 804), NOT stated on the fetched pages; the attribution is traditional, not certain. Safe wording: "a puzzle attributed to Alcuin of York (died 804); the oldest surviving copy is from the late 800s".
   - Supports: origin of the river-crossing puzzle; 7 crossings; exactly two shortest solutions
   - Used in: task-2/activities/river-crossing/ (puzzle used; origin may be cited in study-guide/mission-02-the-river-problem.md)

74. **Watkins, C. J. C. H. (1989). *Learning from Delayed Rewards* (PhD thesis). King's College, University of Cambridge.**
   - URL: <https://www.cs.rhul.ac.uk/~chrisw/thesis.html>
   - Key: `WATKINS-1989`
   - Accessed: 2026-11-06
   - Verified: fetched the author's own thesis page ("my PhD thesis ... Cambridge, 1989"; Q-learning is among the algorithms; only "a sketch of a proof of convergence" given). Web search (cs.utexas.edu bibliography, mlanthology.org) gives "King's College, Cambridge, May 1989".
   - Supports: Q-learning was introduced by Watkins in 1989
   - Used in: task-2/activities/robot-maze/ (strategy C, tabular Q-learning)

75. **Watkins, C. J. C. H., & Dayan, P. (1992). Technical Note: Q-Learning. *Machine Learning*, 8, 279-292. https://doi.org/10.1007/BF00992698**
   - URL: <https://mlanthology.org/mlj/1992/watkins1992mlj-technical>
   - Key: `WATKINS-DAYAN-1992`
   - Accessed: 2026-11-06
   - Verified: fetched the MLAnthology record (title, authors, vol. 8, pp. 279-292, 1992, DOI 10.1007/BF00992698). Springer page redirects to a login and was not read. Web search: the paper proves Q-learning converges to optimal action-values with probability 1 if all actions are repeatedly sampled in all states and values are stored in a table (discrete representation). One bibliography lists an alternative DOI 10.1023/A:1022676722315; the 10.1007 DOI is the one given by the anthology record.
   - Supports: the Q-learning update and the idea that a table of Q-values learned by trial and error can converge to the best moves (tabular Q-learning, as in the robot maze)
   - Used in: task-2/activities/robot-maze/ (strategy C; README "What kind of method" table and LAB NOTE)

76. **SWI-Prolog project (2026). *SWISH: SWI-Prolog for SHaring* (web service).**
   - URL: <https://swish.swi-prolog.org>
   - Key: `SWISH-SITE` (also logged as: RES-B4-SWISH, SWISH)
   - Accessed: 2026-11-06
   - Verified: fetched the home page and the examples notebook page: title "SWISH -- SWI-Prolog for SHaring", a web interface with "Login with Google" / "Login with StackOverflow" links. The fetched pages do not state that login is optional; the "no account needed to run programs" claim in prolog/README.md comes from the earlier prolog agent's check of the SWISH help and was not re-tested with a live query in this pass. | resources.md B4 (help page; preload link fetched; queries run on live server). Extra queries (aunt_or_uncle, kb + likes(bolt,puzzles)) run by this agent locally with SWI-Prolog 10.1.20 (swipl-wasm 8.3.0) and Tau Prolog 0.3.4 using a temporary working file (not included) | HTTP 200 re-checked 2026-11-06; saving/privacy behaviour from official help (resources agent); activities/prolog/test-output.txt read (SWI-Prolog via swipl-wasm + Tau Prolog)
   - Supports: SWISH is a free online Prolog environment; login options exist | Activity 3.1-3.5 setup and results | resource description
   - Used in: task-2/activities/prolog/README.md (Preparation); task-2/activities/README.md (access table) | study-guide/mission-03-pixels-rulebook.md | task-2/study-guide/resources.md B3

77. **Wielemaker, J., Lager, T., & Riguzzi, F. (2015). *SWISH: SWI-Prolog for Sharing*. International Workshop on User-Oriented Logic Programming (IULP 2015). arXiv:1511.00915.**
   - URL: <https://arxiv.org/abs/1511.00915>
   - Key: `SWISH-PAPER-2015`
   - Accessed: 2026-11-06
   - Verified: web search result (arXiv and VU Amsterdam research portal): SWISH is a web front-end for SWI-Prolog, used to run small programs for teaching; the server side is SWI-Prolog. Paper PDF not read in full.
   - Supports: SWISH runs real SWI-Prolog on a server, so answers match a local SWI-Prolog
   - Used in: task-2/activities/prolog/README.md (Preparation, Test evidence)

78. **SWI-Prolog project (2026). *SWI-Prolog* (free Prolog system), version 10.1.20 shown on the site.**
   - URL: <https://www.swi-prolog.org>
   - Key: `SWI-PROLOG` (also logged as: SWIPL-DOWNLOAD)
   - Accessed: 2026-11-06
   - Verified: fetched home page: "Robust, mature, free", "a comprehensive free Prolog environment", in development since 1987; footer "Powered by SWI-Prolog 10.1.20" (same version as used in the tests via swipl-wasm). | taken from activities/prolog/README.md (offline alternative); not re-fetched
   - Supports: free offline alternative to SWISH; engine version used in testing | offline install option
   - Used in: task-2/activities/prolog/README.md (Preparation, Fallback, Test evidence) | study-guide/mission-03-pixels-rulebook.md "Setting up"

79. **SWI-Prolog project. *swipl-wasm* (npm package), version 8.3.0, bundling SWI-Prolog 10.1.20.**
   - URL: <https://github.com/SWI-Prolog/npm-swipl-wasm>
   - Key: `SWIPL-WASM`
   - Accessed: 2026-11-06
   - Verified: fetched repository page ("SWI-Prolog compiled to WebAssembly ... run in both Node.js and browsers"); version 8.3.0 read from the installed package.json in a temporary working file (not included)
   - Supports: automated testing of all Prolog queries with the same engine as SWISH
   - Used in: task-2/activities/prolog/test_queries.cjs, README.md (Test evidence); task-2/activities/README.md (tests table)

80. **Tau Prolog contributors. *Tau Prolog: an open source Prolog interpreter in JavaScript* (npm package `tau-prolog`), version 0.3.4. BSD-3-Clause.**
   - URL: <https://github.com/tau-prolog/tau-prolog>
   - Key: `TAU-PROLOG`
   - Accessed: 2026-11-06
   - Verified: fetched the GitHub repository page (description and BSD-3-Clause licence); the project site tau-prolog.org failed with a TLS certificate error. Version 0.3.4 read from a temporary working file (not included)
   - Supports: independent cross-check engine for the Prolog queries
   - Used in: task-2/activities/prolog/test_queries.cjs, README.md (Test evidence)

81. **jsdom contributors. *jsdom: a JavaScript implementation of various web standards, for use with Node.js* (npm package), version 31.0.0.**
   - URL: <https://github.com/jsdom/jsdom>
   - Key: `JSDOM`
   - Accessed: 2026-11-06
   - Verified: fetched repository page (description quoted); version 31.0.0 read from a temporary working file (not included) and printed by both UI tests.
   - Supports: simulated-browser UI tests of river-crossing.html and robot-maze.html (not shipped; not needed by learners)
   - Used in: task-2/activities/river-crossing/test_ui.cjs, task-2/activities/robot-maze/test_ui.cjs, their READMEs, task-2/activities/README.md

82. **Google (2026). *Google Colaboratory: Frequently Asked Questions*.**
   - URL: <https://research.google.com/colaboratory/faq.html>
   - Key: `COLAB-FAQ`
   - Accessed: 2026-11-06
   - Verified: fetched page: "Colab is free of charge to use"; resources not guaranteed and limits not published; "Colab notebooks are stored in Google Drive, or can be loaded from GitHub"; to import a notebook choose "Upload notebook" from the File menu. The page does not literally say "a Google account is required"; that follows from storage in Google Drive and the sign-in step.
   - Supports: Colab access requirements and upload steps for the spam-filter notebook
   - Used in: task-2/activities/spam-filter/README.md (Preparation, Fallback); task-2/activities/README.md (access table)

83. **Project Jupyter (2026). *Jupyter* (Jupyter Notebook and JupyterLab).**
   - URL: <https://jupyter.org>
   - Key: `JUPYTER`
   - Accessed: 2026-11-06
   - Verified: fetched page: Jupyter Notebook and JupyterLab are web-based interactive computing environments; "free software, open standards"; open JSON-based notebook format.
   - Supports: offline Option B for the spam-filter notebook
   - Used in: task-2/activities/spam-filter/README.md (Preparation)

84. **Project Jupyter. *The Notebook file format* (nbformat documentation), format version 4 (cell IDs since the 4.5 schema).**
   - URL: <https://nbformat.readthedocs.io/en/latest/format_description.html>
   - Key: `NBFORMAT`
   - Accessed: 2026-11-06
   - Verified: fetched page: "The official Jupyter Notebook format is defined with this JSON schema", major version 4, cell IDs "since the 4.5 schema release". The nbformat 5.11.1 validation run was done by the earlier spam-filter agent (nbformat is not installed in this environment now, so it was not re-run in this pass).
   - Supports: tiny_spam_filter.ipynb uses the nbformat 4.5 structure
   - Used in: task-2/activities/spam-filter/README.md (Test evidence)

85. **Python Software Foundation (2026). *Download Python*.**
   - URL: <https://www.python.org/downloads/>
   - Key: `PYTHON`
   - Accessed: 2026-11-06
   - Verified: fetched page: "All Python releases are Open Source"; latest 3.15.2; 3.14 in bugfix status. Tests here ran on Python 3.14.7 (python3 --version).
   - Supports: free download for the optional spam filter and river-crossing solver; Python version used in testing
   - Used in: task-2/activities/spam-filter/README.md, river-crossing/README.md, task-2/activities/README.md

86. **OpenJS Foundation (2026). *Node.js*.**
   - URL: <https://nodejs.org/en>
   - Key: `NODEJS`
   - Accessed: 2026-11-06
   - Verified: fetched page: "free, open-source, cross-platform JavaScript runtime"; latest LTS v26.13.0. Tests here ran on Node v26.10.0 (node --version).
   - Supports: test runner for all logic and UI tests (maintainers only)
   - Used in: task-2/activities/*/test_*.mjs, *.cjs, their READMEs, task-2/activities/README.md

87. **Original test runs (supplements agent), 2026-11-06.**
   - Location: n/a (outputs saved next to each test in task-2/activities/)
   - Key: `SUPPLEMENT-TEST-RUNS`
   - Accessed: 2026-11-06
   - Verified: re-ran all seven test commands; every exit code 0 and every output byte-identical to the saved files (river-crossing logic/UI/solver, robot-maze logic/UI, prolog queries, spam filter). An extra script (a temporary working file (not included)) found that Q-learning's best route stays shortest from episode 19 (Maze 1) and episode 22 (Maze 2).
   - Supports: all "expected results" figures in the four supplement READMEs
   - Used in: task-2/activities/*/README.md (Feedback, Test evidence)

## Task 2 study guide: videos, platforms and reading

88. **CrashCourse / PBS Digital Studios (2019). *What Is Artificial Intelligence? Crash Course AI #1*. YouTube.**
   - URL: <https://www.youtube.com/watch?v=a0_lo_GDcFw>
   - Key: `RES-V1-CRASHCOURSE-AI1` (also logged as: YT-CRASHCOURSE-AI1)
   - Accessed: 2026-11-06
   - Verified: taken from resources.md V1 (oEmbed + chapter list checked by resources agent); not re-fetched | YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: [WATCH] box; segments 0:00-4:48 and 6:37-7:16 | Mission 01 overview; history segment 4:48-9:32 (Dartmouth, computing power, data)
   - Used in: study-guide/mission-01-is-it-ai.md [WATCH] | task-2/study-guide/mission-08-time-machine.md [WATCH]; task-2/study-guide/resources.md V1

89. **Code.org (2019). *AI: What is Machine Learning?* How AI Works series. YouTube (+ direct MP4).**
   - URL: <https://www.youtube.com/watch?v=OeU5m6vRyCk>
   - Key: `RES-V2-CODEORG-ML` (also logged as: YT-CODEORG-ML)
   - Accessed: 2026-11-06
   - Verified: resources.md V2; not re-fetched | YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: [WATCH] box (whole video, 2:56) | ML = finding patterns in data
   - Used in: study-guide/mission-04-learning-from-examples.md [WATCH] | task-2/study-guide/resources.md V2

90. **Code.org (2020). *How Neural Networks Work*. YouTube (+ direct MP4).**
   - URL: <https://www.youtube.com/watch?v=JrXazCEACVo>
   - Key: `RES-V3-CODEORG-NN` (also logged as: YT-CODEORG-NN)
   - Accessed: 2026-11-06
   - Verified: resources.md V3; not re-fetched | YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: [WATCH] box 0:58-3:59 | single neuron, training by adjusting weights
   - Used in: study-guide/mission-05-inside-the-neuron.md [WATCH] | task-2/study-guide/resources.md V3

91. **3Blue1Brown (2017). *But what is a neural network? | Deep learning chapter 1*. YouTube; text lesson at 3blue1brown.com/lessons/neural-networks.**
   - URL: <https://www.youtube.com/watch?v=aircAruvnKk>
   - Key: `RES-V4-3B1B-NN` (also logged as: YT-3B1B-NN)
   - Accessed: 2026-11-06
   - Verified: resources.md V4; not re-fetched | YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: optional [WATCH] 0:00-8:38 | layers, activations (0:00-8:38)
   - Used in: study-guide/mission-05-inside-the-neuron.md [OPTIONAL SIDE QUEST] | task-2/study-guide/resources.md V4

92. **3Blue1Brown (2024). *Large Language Models explained briefly*; Code.org (2023). *How Chatbots and Large Language Models Work*.**
   - URL: <https://www.youtube.com/watch?v=LPZh9BOjkQs>
   - Key: `RES-V6-3B1B-LLM / RES-V7-CODEORG-LLM` (also logged as: YT-3B1B-LLM)
   - Accessed: 2026-11-06
   - Verified: resources.md V6, V7; not re-fetched | YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: [WATCH] core 0:00-4:15; alternative 0:38-3:34 + 5:00-5:55 | next-token prediction, pre-training, RLHF
   - Used in: study-guide/mission-06-the-word-guessing-machine.md [WATCH] | task-2/study-guide/resources.md V6

93. **Google (n.d.). *Teachable Machine* (v2.4.18 observed).**
   - URL: <https://teachablemachine.withgoogle.com/>
   - Key: `RES-B1-TEACHABLE-MACHINE` (also logged as: TEACHABLE-MACHINE)
   - Accessed: 2026-11-06
   - Verified: resources.md B1 (source/string inspection; click-through NOT verified) | HTTP 200 re-checked 2026-11-06; labels, defaults, FAQ privacy statements from resources agent's source inspection; not clicked through
   - Supports: Activity 4.3 steps, no-account and data-stays-in-browser claims, fallback table (illustrative) | Activity 10.2 steps, privacy statements, defaults
   - Used in: study-guide/mission-04-learning-from-examples.md Activity 4.3; 00-start-here access table | task-2/study-guide/mission-10-the-fairness-files.md Activity 10.2; task-2/study-guide/resources.md B1

94. **TensorFlow (n.d.). *A Neural Network Playground*.**
   - URL: <https://playground.tensorflow.org/>
   - Key: `RES-B2-TF-PLAYGROUND` (also logged as: TF-PLAYGROUND)
   - Accessed: 2026-11-06
   - Verified: resources.md B2 (source read; presets P1-P10 constructed from state.ts; results from offline re-implementation; preset links NOT clicked) | HTTP 200 re-checked 2026-11-06; settings and simulated results from resources agent
   - Supports: Activity 5.2 presets P1-P10 and expected-results table | resource description only (used in Mission 05 by other agent)
   - Used in: study-guide/mission-05-inside-the-neuron.md Activity 5.2 | task-2/study-guide/resources.md B2

95. **Google (n.d.). *Colaboratory*.**
   - URL: <https://colab.research.google.com/>
   - Key: `RES-B5C-COLAB` (also logged as: COLAB)
   - Accessed: 2026-11-06
   - Verified: resources.md B5c + activities/spam-filter/README.md; not re-fetched | HTTP 200 re-checked (main URL); FAQ per resources agent
   - Supports: optional notebook side quest | access requirements for optional notebook
   - Used in: study-guide/mission-04-learning-from-examples.md side quest Computed by this agent (not external): temperature tally in Mission 06 Activity 6.2 (20 fixed random numbers; tallies computed with a temporary working file (not included), seed 1151, and checked by hand). | task-2/study-guide/resources.md B6

96. **CrashCourse (2019). *Neural Networks and Deep Learning: Crash Course AI #3*. YouTube.**
   - URL: <https://www.youtube.com/watch?v=oV3ZY6tJiA0>
   - Key: `YT-CRASHCOURSE-AI3`
   - Accessed: 2026-11-06
   - Verified: YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: ImageNet/AlexNet 2012 story (0:52-5:51)
   - Used in: task-2/study-guide/mission-08-time-machine.md [WATCH]; task-2/study-guide/resources.md V5

97. **Code.org (2023). *How Chatbots and Large Language Models Work*. YouTube (CodeAI).**
   - URL: <https://www.youtube.com/watch?v=X-AWdfSFCHQ>
   - Key: `YT-CODEORG-LLM`
   - Accessed: 2026-11-06
   - Verified: YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: gentler LLM explanation
   - Used in: task-2/study-guide/resources.md V7

98. **CrashCourse (2019). *How YouTube knows what you should watch: Crash Course AI #15*. YouTube.**
   - URL: <https://www.youtube.com/watch?v=kiInh5STnyQ>
   - Key: `YT-CRASHCOURSE-AI15`
   - Accessed: 2026-11-06
   - Verified: YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: recommenders, collaborative filtering, drawbacks, privacy
   - Used in: task-2/study-guide/mission-09-ai-in-the-wild.md [WATCH]; task-2/study-guide/resources.md V8

99. **Buolamwini, J. (2016/2017). *How I'm fighting bias in algorithms*. TED (TEDxBeaconStreet). YouTube and TED.com.**
   - URL: <https://www.youtube.com/watch?v=UG_X_7g63rY>
   - Key: `TED-BUOLAMWINI-2016`
   - Accessed: 2026-11-06
   - Verified: YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: face-detection failure; root cause non-diverse training sets (0:00-4:13)
   - Used in: task-2/study-guide/mission-10-the-fairness-files.md [WATCH]; task-2/study-guide/resources.md V9

100. **Code.org (2019). *AI: Training Data & Bias*. YouTube (CodeAI).**
   - URL: <https://www.youtube.com/watch?v=x2mRoFNm22g>
   - Key: `YT-CODEORG-BIAS`
   - Accessed: 2026-11-06
   - Verified: YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: model only as good as its training data
   - Used in: task-2/study-guide/mission-10-the-fairness-files.md [WATCH]; task-2/study-guide/resources.md V10

101. **Shane, J. (2019). *The danger of AI is weirder than you think*. TED2019. YouTube and TED.com.**
   - URL: <https://www.youtube.com/watch?v=OhCzX0iLnOc>
   - Key: `TED-SHANE-2019`
   - Accessed: 2026-11-06
   - Verified: YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: AI does what we ask not what we mean; ice cream, fish/fingers examples; content note ~5:29
   - Used in: task-2/study-guide/mission-11-myth-busters.md [WATCH]; task-2/study-guide/resources.md V11

102. **Code.org (2020). *Ethics & AI: Privacy & the Future of Work*. YouTube (CodeAI).**
   - URL: <https://www.youtube.com/watch?v=zNxw5gJtHLc>
   - Key: `YT-CODEORG-ETHICS`
   - Accessed: 2026-11-06
   - Verified: YouTube oEmbed endpoint re-queried 2026-11-06: title and channel match; durations/chapters/captions from resources agent (watch-page player data); not watched by eye/ear
   - Supports: researchers on jobs, privacy, youth (0:37-1:21, 2:14-3:27)
   - Used in: task-2/study-guide/mission-12-tomorrows-rulebook.md [WATCH]; task-2/study-guide/resources.md V12

103. **Hay, A. & Hay, M. (2025). *ELIZA* (1966 CACM DOCTOR script reconstruction), version 1.00 (2025-03-08). GitHub Pages.**
   - URL: <https://anthay.github.io/eliza.html>
   - Key: `ELIZA-HAY-2025`
   - Accessed: 2026-11-06
   - Verified: HTTP 200; page downloaded and its source read statically (version string, command handlers *traceauto/*key/*reset/*cacm/*help, DOCTOR script rules MY rank 2, COMPUTER rank 50, ALWAYS rank 1, I/YOU/WHAT/NONE/MEMORY rules, memory used every 4th no-match). Executing the page code headlessly was blocked by the sandbox, so expected replies are derived from the rules, not observed
   - Supports: Activity 8.2 expected replies and commands; claim of 1966 fidelity (authors' statement)
   - Used in: task-2/study-guide/mission-08-time-machine.md Activity 8.2; task-2/study-guide/resources.md B4

104. **Landsteiner, N. (2005). *elizabot.js* (ELIZA terminal). mass:werk.**
   - URL: <https://www.masswerk.at/elizabot/eliza.html>
   - Key: `ELIZA-MASSWERK`
   - Accessed: 2026-11-06
   - Verified: HTTP 200 (2026-11-06); random-choice behaviour per resources agent (elizadata.js read)
   - Supports: alternative ELIZA with randomised replies
   - Used in: task-2/study-guide/mission-08-time-machine.md; task-2/study-guide/resources.md B4

105. **Csapo, G., Kim, J., Klasinc, M. & ElKattan, A. (2019). *Survival of the Best Fit*.**
   - URL: <https://www.survivalofthebestfit.com/>
   - Key: `SURVIVAL-BEST-FIT`
   - Accessed: 2026-11-06
   - Verified: HTTP 200 re-checked 2026-11-06; content per resources agent (text read, not played)
   - Supports: optional hiring-bias game
   - Used in: task-2/study-guide/mission-10-the-fairness-files.md side quest; task-2/study-guide/resources.md B5

106. **Google (n.d.). *Quick, Draw!* and *Quick, Draw! The Data*.**
   - URL: <https://quickdraw.withgoogle.com/>
   - Key: `QUICKDRAW`
   - Accessed: 2026-11-06
   - Verified: HTTP 200 re-checked 2026-11-06; public-dataset statement per resources agent
   - Supports: reason for exclusion (doodles added to public dataset)
   - Used in: task-2/study-guide/resources.md section D

107. **MinnaLearn & University of Helsinki (n.d.). *Elements of AI*.**
   - URL: <https://www.elementsofai.com/>
   - Key: `ELEMENTS-OF-AI`
   - Accessed: 2026-11-06
   - Verified: HTTP 200 re-checked 2026-11-06; account requirement per resources agent (not verified)
   - Supports: further reading
   - Used in: task-2/study-guide/resources.md C1

108. **3Blue1Brown (n.d.). *But what is a Neural Network?* and *Large Language Models explained briefly* (written lessons).**
   - URL: <https://www.3blue1brown.com/lessons/neural-networks>
   - Key: `3B1B-LESSONS`
   - Accessed: 2026-11-06
   - Verified: HTTP 200 re-checked 2026-11-06
   - Supports: text alternatives to V4/V6
   - Used in: task-2/study-guide/resources.md C3

109. **Code.org (n.d.). *How AI Works* video series and curriculum.**
   - URL: <https://code.org/ai/how-ai-works>
   - Key: `CODEORG-HUB`
   - Accessed: 2026-11-06
   - Verified: HTTP 200 re-checked 2026-11-06 (redirects to code.org curriculum page); direct MP4 fallbacks re-checked (HTTP 200/206 on ranged GET)
   - Supports: video series hub and MP4 alternatives for V2, V3, V7, V10, V12
   - Used in: task-2/study-guide/resources.md; task-2/study-guide/mission-10, mission-12 [WATCH] alternatives

110. **Internet Archive (n.d.). *Wayback Machine*.**
   - URL: <https://web.archive.org/>
   - Key: `WAYBACK`
   - Accessed: 2026-11-06
   - Verified: HTTP 200 (2026-11-06)
   - Supports: "if a link breaks" advice
   - Used in: task-2/study-guide/resources.md section E

111. **Ronkowitz, K. (n.d.). ELIZA page at NJIT.**
   - URL: <https://web.njit.edu/~ronkowit/eliza.html>
   - Key: `NJIT-ELIZA-DEAD`
   - Accessed: 2026-11-06
   - Verified: HTTP 404 per resources agent (2026-11-06); not linked, mentioned as unusable
   - Supports: note that a commonly cited ELIZA page is dead
   - Used in: task-2/study-guide/resources.md B4 (unlinked mention)

## Task 2 test bank

112. **Pixel's AI Field Guide supplement (2026). *River-crossing solver output* (solver-output.txt, from solver.py, breadth-first search). Original module material.**
   - Location: n/a (task-2/activities/river-crossing/solver-output.txt)
   - Key: `TB-RIVER-SOLVER`
   - Accessed: 2026-11-06
   - Verified: read the file; BFS steps 4-5 (options rejected/skipped/added and frontier order), 10 safe states, 2 shortest 7-crossing solutions match Q13, Q16, Q17
   - Supports: Q10, Q12-Q17 answers (states, safe/unsafe, BFS frontier trace)
   - Used in: task-2/test-bank/test-bank.md (Mission 02 questions and answer key)

113. **Pixel's AI Field Guide supplement (2026). *family.pl, robot-troubleshooter.pl, find-the-bug.pl, queries.md, test-output.txt, test_queries.cjs*. Original module material.**
   - Location: n/a (task-2/activities/prolog/)
   - Key: `TB-PROLOG-SUPPLEMENT`
   - Accessed: 2026-11-06
   - Verified: read files; adapted the family program and a trimmed troubleshooter into the questions; re-ran every test-bank query with my own script (see TB-PROLOG-RUN)
   - Supports: Mission 03 question design (syntax box, programs, closed-world assumption, duplicate proofs)
   - Used in: test-bank.md Q18-Q26

114. **Original verification run (test-bank agent). SWI-Prolog 10.1.20 via swipl-wasm and Tau Prolog 0.3.4 on Node, running the exact programs printed in the questions.**
   - Location: n/a (script: a temporary working file (not included); output: a temporary working file (not included))
   - Key: `TB-PROLOG-RUN`
   - Accessed: 2026-11-06
   - Verified: both engines agree on all 18 queries: grandparent(G, kemi) -> grace, samuel; ancestor(A, leo) -> ada, grace, samuel; parent(ada, Child) -> zara, leo; parent(ada, child) -> false; parent(Child, ada) -> grace, samuel; parent(ada, zara) -> true; male(ada) -> false; buggy grandparent(grace, GC) -> ada, tunde, ada, tunde (SWI also warns "Singleton variables: [Y]"); buggy grandparent(G, kemi) -> tunde; uncle(U, zara) -> tunde, tunde (two orderings of the rule tested); uncle(U, kemi) -> false; troubleshooter diagnosis(gizmo, D) -> no_diagnosis; fault(gizmo, F) -> false
   - Supports: answers to Q21-Q26
   - Used in: test-bank.md Mission 03 answer key

115. **Original verification run (test-bank agent). Python 3 script using exact fractions.**
   - Location: n/a (script: a temporary working file (not included); output: a temporary working file (not included))
   - Key: `TB-CALC-RUN`
   - Accessed: 2026-11-06
   - Verified: python3 -I tb_calc.py; spam-filter scores (Q32 = 2 spam; Q37 F1 3, F2 -2, F3 0, F4 0; threshold 4 changes only F1); tiny spam filter product 4/3 (Q38, reproducing tiny_spam_filter.py's training formula); recharge neuron sums (Q44 0.1; Q47 0.1, -0.2, 0.6; bias -0.5 gives 0.0 and 0.0; w3 = 0.2 gives -0.2 and 0.1); next-token ranges (Q54 0.62 -> sofa; Q59 door/box/window/fridge, 200 x 0.20 = 40); Markov chain follower table and three generated sentences (Q58); collaborative-filtering differences 2 and 10 (Q82); WEF 170 - 92 = 78, 92/170 = 0.54 (Q96); 45,000 x 0.2% = 90/day, 630/week (Q95); EU AI Act obligations applying on 1 Jan 2025, 1 Sep 2025, 6 Nov 2026, 1 Jan 2027, 1 Sep 2028 (Q112, Q113)
   - Supports: every calculation and trace in the answer key
   - Used in: test-bank.md answer key (Q32, Q37, Q38, Q44, Q47, Q54, Q58, Q59, Q82, Q95, Q96, Q112, Q113)

116. **Pixel's AI Field Guide supplement (2026). *tiny_spam_filter.py, expected-output.txt, README.md* (spam-filter activity). Original module material.**
   - Location: n/a (task-2/activities/spam-filter/)
   - Key: `TB-SPAM-SUPPLEMENT`
   - Accessed: 2026-11-06
   - Verified: read the script's scoring formula ((spam count + 1)/(6 + 2) divided by (not-spam count + 1)/(6 + 2); multiply; > 1 = spam) and expected output ("Are you free for lunch today?" scores 1.333 -> spam, WRONG)
   - Supports: Q38 word-score table and answer
   - Used in: test-bank.md Q38

117. **Pixel's AI Field Guide supplement (2026). *Robot maze test output* (test_logic-output.txt, test_ui-output.txt). Original module material.**
   - Location: n/a (task-2/activities/robot-maze/)
   - Key: `TB-MAZE-SUPPLEMENT`
   - Accessed: 2026-11-06
   - Verified: read test outputs: wall follower 28 moves in Maze 1 and loops forever in Maze 2; BFS 16 and 12 moves; Q-learning episodes 1-3 = 117, 98, 88 moves, later learns 16- and 12-move routes; Maze 1 table does not solve Maze 2; rewards -1/-5/+10
   - Supports: Q35 data table and answer
   - Used in: test-bank.md Q35

118. **Resource-curation notes for Pixel's AI Field Guide (2026), sections B1 (Teachable Machine v2.4.18), B2 (TensorFlow Playground, simulated preset results) and B3 (ELIZA). Internal module notes.**
   - Location: n/a (a temporary working file (not included))
   - Key: `TB-PLATFORM-NOTES`
   - Accessed: 2026-11-06
   - Verified: read the notes. Used only qualitative, documented behaviors: a classifier must split confidence among its defined classes; confidence bars are not calibrated; imbalanced classes often pull ambiguous inputs toward the larger class (typical, not guaranteed); circle dataset with 0 hidden layers stays near test loss 0.5 while one hidden layer of 4 solves it; learning rate 3 makes loss jump; overfitting preset shows training loss falling while test loss rises; results vary with random initial weights and data. All numbers in Q39, Q48, Q92 are labeled illustrative; Q75 uses self-contained simplified ELIZA-style rules, not predictions about a live ELIZA site.
   - Supports: Q39, Q43, Q45, Q46, Q48, Q75, Q92 scenarios and answers
   - Used in: test-bank.md Missions 04, 05, 08, 10
