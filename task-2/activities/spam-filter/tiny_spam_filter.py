"""
Pixel's AI Field Guide - Tiny Spam Filter (Version 1.0, 2026-11-06)

Pixel learns to spot spam from 12 labelled example emails.
ALL emails below are MADE-UP examples written for this activity.

How Pixel learns (a simplified "naive Bayes" idea, no maths needed):
  1. For every word, count how many SPAM emails contain it and how many
     NOT-SPAM emails contain it.
  2. Turn the counts into a WORD SCORE:
        score above 1  -> the word appears more in spam   (spammy)
        score below 1  -> the word appears more in not-spam (safe)
        score of 1     -> no evidence either way (or a word never seen)
  3. To judge a new email, MULTIPLY the scores of its words.
     Final score above 1 -> "SPAM", otherwise -> "NOT SPAM".

Run it:   python3 tiny_spam_filter.py   (Python 3.8+, standard library only)
"""
import re

# ======================= EXPERIMENT ZONE (change me!) =======================
# Each training example is (email text, label). Labels: "spam" or "not spam".
# Try: add an email, delete one, or swap a label, then run again and compare.
TRAINING_DATA = [
    ("WIN a FREE prize now! Click here", "spam"),
    ("Cheap pills, buy now, limited offer", "spam"),
    ("You are a winner! Claim your cash prize today", "spam"),
    ("Free money!!! Click the link to claim", "spam"),
    ("Limited time offer: win a free phone", "spam"),
    ("Urgent: your account wins cash, click now", "spam"),
    ("Lab meeting moved to Tuesday at 10", "not spam"),
    ("Can you send me the robot battery report?", "not spam"),
    ("Lunch today? The cafe has soup", "not spam"),
    ("Dr. Okafor shared the meeting notes", "not spam"),
    ("Reminder: return the library book on Friday", "not spam"),
    ("Thanks for fixing the robot wheel today", "not spam"),
]

# Test emails Pixel has NEVER seen. The label is the right answer, used
# only to CHECK Pixel afterwards (Pixel does not get to peek).
TEST_DATA = [
    ("Claim your free prize now", "spam"),
    ("Click here for cheap cash", "spam"),
    ("Buy a cheap phone now, limited offer", "spam"),
    ("Congratulations, you have been selected", "spam"),
    ("Meeting notes for the robot lab", "not spam"),
    ("Please send the battery report by Friday", "not spam"),
    ("Are you free for lunch today?", "not spam"),
    ("You won a prize in the lab quiz", "not spam"),
]

# Type your own message here and see how Pixel scores every word.
MY_MESSAGE = "Free lunch in the lab today, click here to sign up"
# ============================================================================


def words_in(text):
    """Split text into lowercase words, e.g. 'WIN a FREE prize!' ->
    {'win', 'a', 'free', 'prize'}. A set ignores repeats in one email."""
    return set(re.findall(r"[a-z]+", text.lower()))


def train(examples):
    """TRAINING: count, for every word, how many spam and how many
    not-spam emails contain it, then turn counts into word scores."""
    n_spam = sum(1 for _, label in examples if label == "spam")
    n_ham = len(examples) - n_spam                 # "ham" = not spam
    spam_count, ham_count = {}, {}
    for text, label in examples:
        counts = spam_count if label == "spam" else ham_count
        for w in words_in(text):
            counts[w] = counts.get(w, 0) + 1
    scores = {}
    for w in set(spam_count) | set(ham_count):
        # Share of spam emails containing w, divided by the share of
        # not-spam emails containing w. The "+ 1" and "+ 2" (called
        # smoothing) stop a word seen only once from getting a score of 0
        # or "infinity", which would overrule every other word.
        in_spam = (spam_count.get(w, 0) + 1) / (n_spam + 2)
        in_ham = (ham_count.get(w, 0) + 1) / (n_ham + 2)
        scores[w] = in_spam / in_ham
    return scores, spam_count, ham_count


def classify(text, scores):
    """INFERENCE: multiply the scores of the words in the email.
    Unknown words get score 1, so they change nothing."""
    total = 1.0
    for w in sorted(words_in(text)):
        total *= scores.get(w, 1.0)
    total = round(total, 6)   # remove tiny computer rounding errors (1.0000000002)
    # A score of exactly 1 means "no evidence": Pixel then says NOT spam.
    return ("spam" if total > 1.0 else "not spam"), total


# ---- 1. Training ------------------------------------------------------------
scores, spam_count, ham_count = train(TRAINING_DATA)
print("Trained on", len(TRAINING_DATA), "made-up emails;", len(scores), "different words.\n")

# ---- 2. Show what Pixel learned (most spammy and most safe words) -----------
ranked = sorted(scores, key=lambda w: (-scores[w], w))
print("Most SPAMMY words   (score | in spam | in not-spam)")
for w in ranked[:6]:
    print(f"  {w:<10} {scores[w]:5.2f} | {spam_count.get(w, 0)} | {ham_count.get(w, 0)}")
print("Most SAFE words")
for w in sorted(scores, key=lambda w: (scores[w], w))[:6]:
    print(f"  {w:<10} {scores[w]:5.2f} | {spam_count.get(w, 0)} | {ham_count.get(w, 0)}")

# ---- 3. Test on emails Pixel has never seen ---------------------------------
print("\nTEST RESULTS (final score above 1 means spam)")
correct = 0
for text, true_label in TEST_DATA:
    guess, total = classify(text, scores)
    ok = guess == true_label
    correct += ok
    mark = "correct" if ok else "WRONG  "
    print(f"  {mark} score {total:9.3f} -> {guess:<8} | {text}")
print(f"\nAccuracy: {correct} of {len(TEST_DATA)} correct "
      f"({100 * correct / len(TEST_DATA):.1f}%)")

# ---- 4. Your own message, word by word --------------------------------------
guess, total = classify(MY_MESSAGE, scores)
print(f'\nYOUR MESSAGE: "{MY_MESSAGE}"')
for w in sorted(words_in(MY_MESSAGE)):
    print(f"  {w:<10} {scores.get(w, 1.0):5.2f}" + ("" if w in scores else "  (never seen)"))
print(f"  Final score {total:.3f} -> Pixel says: {guess.upper()}")
