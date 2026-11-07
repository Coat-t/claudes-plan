# [OPTIONAL SIDE QUEST] Pixel's Tiny Spam Filter

**Pixel's AI Field Guide: Missions for Curious Humans** · Supplement · Version 1.0 · 2026-11-06
Belongs to: Mission 04 (Learning from Examples: training vs inference, supervised learning, features and labels, training/test split, overfitting), building on the spam-filter worked example in Topic 02. Contrasts with the hand-written rules of Mission 03.

**[MISSION BRIEF]** Dr. Ada Okafor's inbox is full of junk. Nobody writes rules for Pixel this time. Pixel must **learn** what spam looks like from 12 labelled example emails, then face 8 emails it has never seen.

| File | What it is |
|---|---|
| `tiny_spam_filter.py` | The whole activity as one short, heavily commented Python script (standard library only) |
| `tiny_spam_filter.ipynb` | The same code split into notebook cells, with explanations and **[PREDICT]** prompts (for Google Colab or Jupyter) |
| `expected-output.txt` | Exactly what the unchanged script prints, for checking or for use without a computer |
| `test-log.txt` | Record of the tests run on these files |

All emails are **made-up examples**. All scores and accuracy figures are **illustrative (made-up) figures** from a toy model, not measurements of any real spam filter.

---

## Goal
- See **supervised learning** happen: a program builds its own "rules" (word scores) from **labelled examples** instead of being given rules by a human.
- Tell **training** (counting words in labelled emails) apart from **inference** (scoring a new email).
- Explain why we test on **unseen** data, and how small or biased training data leads to mistakes (overgeneralizing).

## Preparation
- **Knowledge:** Missions 02 and 03 of the guide, and the start of Mission 04. No programming or maths is needed. You only change text between quotation marks.
- **Choose ONE way to run it:**

| Option | Needs | Online? |
|---|---|---|
| A. Google Colab | A web browser and a **Google account** (free). Colab is a Google service; Google's usage limits apply. | Online |
| B. Jupyter Notebook / JupyterLab on your computer | Jupyter already installed (for example via Anaconda) | Offline |
| C. Plain Python | Python 3.8 or newer. Nothing else to install. | Offline |
| D. No computer | A printout of `expected-output.txt` and this README | Offline |

**Opening the notebook in Colab (Option A):**
1. Download `tiny_spam_filter.ipynb`.
2. Go to <https://colab.research.google.com> and sign in.
3. Choose **File -> Upload notebook** and select the file. Colab keeps your copy in **your own Google Drive**, so your experiments do not change anyone else's copy. If a teacher shares the notebook as a Colab link instead, use **File -> Save a copy in Drive** before editing.
4. Run cells in order with **Shift+Enter**, or use **Runtime -> Run all**.

**Option C:** open a terminal in this folder and run `python3 tiny_spam_filter.py`. To change the data, open the file in any text editor and edit only the **EXPERIMENT ZONE** near the top.

## Task (about 30 minutes)
1. **[PREDICT]** Read the 12 training emails in the EXPERIMENT ZONE. Write down three words you expect to be "spammy" and three you expect to be "safe".
2. **[TRY IT]** Run the code (all cells, or the script).
3. **[OBSERVE]** Compare the "Most SPAMMY words" and "Most SAFE words" lists with your prediction.
4. **[PREDICT]** Before reading the TEST RESULTS, cover them and guess Pixel's answer for each of the 8 test emails.
5. **[OBSERVE]** Read the results and the accuracy. For each **WRONG** line, find the word scores that caused the mistake.
6. **[TRY IT] Experiment A (better data):** add these two lines inside `TRAINING_DATA`, just before the closing `]`:
   ```python
       ("Congratulations! You have been selected to win cash", "spam"),
       ("Are you free for a chat on Friday?", "not spam"),
   ```
   Predict the new accuracy, then run everything again.
7. **[TRY IT] Experiment B (fool Pixel):** set `MY_MESSAGE` to a message you think Pixel will get wrong. Run it and read the word-by-word scores.
8. **[TRY IT] Experiment C (a labelling mistake):** undo Experiment A, change one training email's label from `"not spam"` to `"spam"`, and see which word scores change.

## Observation questions
1. Which word on the spammy list is surprising? Why did Pixel learn it?
2. Which test emails did Pixel get wrong, and which words pushed each one the wrong way?
3. In Experiment A, how many training emails did you add, and how much did the accuracy change?
4. In `MY_MESSAGE`, which words are "never seen"? What score do they get?

## Reflection
- **[EXPLAIN]** Nobody told Pixel "the word *free* means spam". Where did this "rule" come from? How is that different from the Prolog troubleshooter, where Dr. Okafor wrote every rule by hand?
- Why is accuracy on **unseen** test emails a more honest measure than accuracy on the training emails?
- In Experiment A we chose new training emails **after** looking at the test mistakes. Why does that make the new 100% less trustworthy?
- Name two things a human understands about "Are you free for lunch?" that word scores cannot capture.

## Feedback: expected results
<details><summary>[DEBRIEF] Open after you have made your predictions</summary>

**Learned word scores (unchanged script).** A score above 1 is spammy, below 1 is safe. The first number after the bar is how many spam emails contain the word; the second is how many not-spam emails contain it.
```
Most SPAMMY words: a 4.00 | 3 | 0, click 4.00, free 4.00, now 4.00, cash 3.00, claim 3.00
Most SAFE words:   meeting 0.33 | 0 | 2, robot 0.33, the 0.33 | 1 | 5, at 0.50, battery 0.50, book 0.50
```
The surprise is **`a`**. By coincidence it appears in three spam emails and in no normal email, so Pixel treats an ordinary word as evidence of spam. This is **overgeneralizing from a small dataset**, the same mistake Pixel makes in Mission 04.

**Test results: 5 of 8 correct (62.5%).**

| Test email | True label | Pixel | Why |
|---|---|---|---|
| Claim your free prize now | spam | spam (432.000) | many spammy words |
| Click here for cheap cash | spam | spam (24.000) | |
| Buy a cheap phone now, limited offer | spam | spam (1152.000) | |
| Congratulations, you have been selected | spam | **not spam (1.000), WRONG** | almost every word is new to Pixel (score 1), so there is no evidence and Pixel defaults to "not spam" |
| Meeting notes for the robot lab | not spam | not spam (0.005) | many safe words |
| Please send the battery report by Friday | not spam | not spam (0.021) | |
| Are you free for lunch today? | not spam | **spam (1.333), WRONG** | Pixel only ever saw `free` in spam; it cannot tell "free for lunch" from "free money" |
| You won a prize in the lab quiz | not spam | **spam (2.000), WRONG** | `prize` and `a` look spammy; to Pixel, `won` and `win` are unrelated strings of letters |

**Your message** (default `"Free lunch in the lab today, click here to sign up"`): final score 1.778, so **SPAM**. `free` and `click` (4.00 each) outweigh `lab`, `lunch`, `the` and `today`. Is it really spam? Even humans might disagree. That is a labelling problem too.

**Experiment A:** accuracy rises to **8 of 8 (100.0%)**. But *"You won a prize in the lab quiz"* now scores **exactly 1.000**: a tie that only counts as correct because ties go to "not spam". And because we picked the new emails after seeing the test mistakes, the test set is no longer truly "unseen". Real projects keep an untouched test set for exactly this reason.

**Experiment B:** a message made only of words Pixel has never seen always scores 1.000 (not spam). Surrounding one spammy word with several safe words (`meeting`, `robot`, `the`) usually gets it classed as not spam.

**Experiment C:** every word in the relabelled email moves toward "spammy", because Pixel trusts its labels completely. Bad labels lead to bad learning ("garbage in, garbage out").

**Reflection key points:** the "rules" came from counting labelled examples (learning-based AI), not from a human expert (rule-based AI). Unseen test data checks whether Pixel learned general patterns or just memorized its examples. Word scores ignore word order, meaning, context and word families (`won`/`win`).
</details>

## [LAB NOTE] Limitations
- **Toy data:** 12 made-up training emails and 8 test emails. Accuracy figures based on 8 emails swing wildly: one email changes the score by 12.5 percentage points.
- **Simplified method:** this is a cut-down **naive Bayes**-style classifier. It only checks whether a word is present (not how often), uses only the words that appear in an email, ignores word order and meaning, and works best with equal numbers of spam and not-spam examples. With unequal numbers, all scores shift slightly (for example, a word found once in each group no longer scores exactly 1).
- **Real spam filters** learn from millions of emails and use many more signals (sender reputation, links, attachments, user reports) and often more complex models. This activity shows the **idea** of learning from labelled data, not how any particular product works.
- **"Accuracy" is not the whole story:** in real life, wrongly binning an important email is usually worse than letting one spam through. The two kinds of mistake have different costs.

## Fallback if the tools are unavailable
- **No Google account or no internet:** use Option B or C, which run offline.
- **No computer or no Python:** use Option D. Do Task steps 1 and 4 (predictions) on paper, then check them against `expected-output.txt` and the DEBRIEF table above. For Experiment A, use the results in the DEBRIEF ("8 of 8"). To work out a score by hand, take one email from `expected-output.txt`'s word lists and multiply the word scores (for example "Are you free for lunch today?": free 4 x lunch 0.5 x today 0.667 x for 0.5 x are 2 x you 1 = about 1.33, so spam).
- **Colab interface looks different:** if the menu names (File, Runtime) change, look for "Upload" or "Open notebook" and "Run all". Or switch to Option C, which gives identical results.

## Test evidence
- **Date:** 2026-11-06. **Python:** 3.14.7 (the code uses only the standard library module `re` and should work with Python 3.8 or newer).
- `python3 -I tiny_spam_filter.py`: output saved as `expected-output.txt`. Re-running with five different `PYTHONHASHSEED` values gave identical output, so the result does not depend on Python's internal word ordering.
- `tiny_spam_filter.ipynb` was generated from the script with Python's `json` module (nbformat 4.5 structure). It **passed `nbformat.validate`** (nbformat 5.11.1, installed outside this folder). Its 6 code cells, joined in order and executed, printed output **identical** to `expected-output.txt`.
- Re-checked on 2026-11-06 after all supplements were finished: `python3 -I tiny_spam_filter.py` output was still identical to `expected-output.txt`. There is no UI test for this activity (it has no web page); `nbformat` is only needed to validate the notebook, is not shipped, and learners never need it.
- Experiment A was run with exactly the two lines above (results in `test-log.txt`). The Colab upload steps follow the Colab FAQ ("Choose 'Upload notebook' from the File menu"). The notebook was **not** uploaded to a live Colab session during testing.
