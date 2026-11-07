"""Build the three teaching decks for "Pixel's AI Field Guide" (Task 3).

Run:  python build_slides.py        (needs: pip install python-pptx)
Input:  assets/png/*.png  (rendered from ../task-1/assets/images/*.svg with
        rsvg-convert -z 2 -b white <file>.svg -o assets/png/<file>.png)
Output: part-1-how-machines-learn.pptx, part-2-chatbots-types-history.pptx,
        part-3-ai-in-the-world.pptx  (slides + presenter notes)

All facts, numbers and examples come from the Task 1 topic files
(../task-1/topics/). If a fact changes, fix the topic file first, then this
script, then rebuild (see README.md).
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

HERE = os.path.dirname(os.path.abspath(__file__))
PNG = os.path.join(HERE, "assets", "png")
NAVY, TEAL, AMBER, CORAL = (RGBColor(0x1F, 0x3A, 0x5F), RGBColor(0x1F, 0x7A, 0x70),
                            RGBColor(0xE9, 0xC4, 0x6A), RGBColor(0xC4, 0x4B, 0x2C))
GREY, WHITE, PALE = RGBColor(0x55, 0x55, 0x55), RGBColor(0xFF, 0xFF, 0xFF), RGBColor(0xF4, 0xF4, 0xF4)
FONT = "Arial"
W, H = Inches(13.333), Inches(7.5)
LABEL_COLOR = {"MISSION BRIEF": CORAL, "PREDICT": AMBER, "TRY IT": AMBER, "DEBRIEF": TEAL,
               "EXPLAIN": NAVY, "LAB NOTE": GREY, "WATCH": NAVY, "APPLY": AMBER,
               "CHECK": AMBER, "DEMO": TEAL, "NEXT STEPS": TEAL, "TAKEAWAY": CORAL}

# ---------------------------------------------------------------- helpers
def _text(slide, x, y, w, h, paras, size=30, color=NAVY, bold=False, align=PP_ALIGN.LEFT,
          anchor=MSO_ANCHOR.TOP, bullets=False, spacing=10):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, p in enumerate(paras):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = align
        para.space_after = Pt(spacing)
        segs = p if isinstance(p, list) else [p]
        if bullets:
            segs = [("•  ", False)] + [s if isinstance(s, tuple) else (s, False) for s in segs]
        for s in segs:
            t, b = s if isinstance(s, tuple) else (s, False)
            r = para.add_run()
            r.text = t
            r.font.size, r.font.name, r.font.color.rgb = Pt(size), FONT, color
            r.font.bold = bold or b
    return box

def _rich(s):
    """'plain **bold** plain' -> list of (text, bold) tuples."""
    parts = s.split("**")
    return [(t, i % 2 == 1) for i, t in enumerate(parts) if t]

def _label(slide, label):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.2), Inches(0.35), Inches(2.8), Inches(0.6))
    shp.fill.solid(); shp.fill.fore_color.rgb = LABEL_COLOR.get(label, AMBER)
    shp.line.fill.background()
    tf = shp.text_frame
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    r = tf.paragraphs[0].add_run(); r.text = label
    dark = LABEL_COLOR.get(label, AMBER) in (AMBER,)
    r.font.size, r.font.bold, r.font.name = Pt(20), True, FONT
    r.font.color.rgb = NAVY if dark else WHITE

def _header(slide, title, label=None):
    # one line only: long titles get a smaller (still >= 32 pt) size
    _text(slide, Inches(0.6), Inches(0.3), Inches(9.5 if label else 12.1), Inches(1.0), [title],
          size=40 if len(title) <= 30 else 32, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(1.35), Inches(1.6), Inches(0.08))
    bar.fill.solid(); bar.fill.fore_color.rgb = TEAL; bar.line.fill.background()
    if label:
        _label(slide, label)

def _footer(slide, part, n, dark=False):
    _text(slide, Inches(0.6), Inches(6.95), Inches(12.1), Inches(0.4),
          [f"Pixel's AI Field Guide  ·  {part}  ·  {n}"], size=16,
          color=WHITE if dark else GREY, align=PP_ALIGN.RIGHT)

def _bg(slide, color):
    f = slide.background.fill; f.solid(); f.fore_color.rgb = color

def _picture(slide, name, x, y, w, h):
    from PIL import Image
    path = os.path.join(PNG, name + ".png")
    im = Image.open(path).convert("RGB")
    from PIL import ImageOps
    box = ImageOps.invert(im).getbbox()          # trim white margins so the diagram is as large as possible
    if box:
        pad = 12
        box = (max(box[0] - pad, 0), max(box[1] - pad, 0), min(box[2] + pad, im.width), min(box[3] + pad, im.height))
        trimmed = os.path.join(PNG, "_trim_" + name + ".png")
        im.crop(box).save(trimmed)
        path = trimmed
    iw, ih = Image.open(path).size
    scale = min(w / iw, h / ih)
    pw, ph = int(iw * scale), int(ih * scale)
    pic = slide.shapes.add_picture(path, x + (w - pw) // 2, y + (h - ph) // 2, pw, ph)
    return pic

def build(part_name, slides, filename):
    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    blank = prs.slide_layouts[6]
    for n, s in enumerate(slides, 1):
        sl = prs.slides.add_slide(blank)
        kind = s.get("kind", "bullets")
        if kind in ("title", "section"):
            _bg(sl, NAVY)
            _text(sl, Inches(0.9), Inches(1.6 if kind == "title" else 2.2), Inches(11.5), Inches(1.9),
                  [s["title"]], size=54 if kind == "title" else 48, color=WHITE, bold=True,
                  anchor=MSO_ANCHOR.BOTTOM)
            bar = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(3.75 if kind == "title" else 4.25),
                                      Inches(2.2), Inches(0.1))
            bar.fill.solid(); bar.fill.fore_color.rgb = AMBER; bar.line.fill.background()
            if s.get("sub"):
                _text(sl, Inches(0.9), Inches(4.0 if kind == "title" else 4.5), Inches(11.5), Inches(2.4),
                      [_rich(x) for x in s["sub"]], size=30, color=WHITE)
            _footer(sl, part_name, n, dark=True)
        else:
            _header(sl, s["title"], s.get("label"))
            top = Inches(1.7)
            if kind == "bullets":
                _text(sl, Inches(0.8), top, Inches(11.8), Inches(5.1),
                      [_rich(b) for b in s["bullets"]], size=s.get("size", 30), bullets=True, spacing=16)
            elif kind == "big":
                _text(sl, Inches(0.8), top, Inches(11.8), Inches(2.2), [_rich(s["big"])], size=40,
                      bold=False, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
                if s.get("bullets"):
                    _text(sl, Inches(1.5), Inches(4.0), Inches(10.4), Inches(2.9),
                          [_rich(b) for b in s["bullets"]], size=30, spacing=12)
            elif kind == "image":
                side = s.get("bullets")
                iw = Inches(7.6) if side else Inches(12.1)
                ih = Inches(4.6) if s.get("caption") else Inches(5.15)
                _picture(sl, s["image"], Inches(0.6), top, iw, ih)
                if side:
                    _text(sl, Inches(8.5), top, Inches(4.4), Inches(5.1), [_rich(b) for b in side],
                          size=s.get("size", 28), bullets=True, spacing=14)
                if s.get("caption"):
                    _text(sl, Inches(0.6), Inches(6.35), Inches(12.1), Inches(0.6), [_rich(s["caption"])],
                          size=24, color=GREY, align=PP_ALIGN.CENTER)
            elif kind == "table":
                rows = s["rows"]
                ncol = len(rows[0])
                th = Inches(min(4.55 if s.get("caption") else 5.1, 0.62 * len(rows)))
                tbl = sl.shapes.add_table(len(rows), ncol, Inches(0.6), top, Inches(12.1), th).table
                for c, cw in enumerate(s.get("widths", [12.1 / ncol] * ncol)):
                    tbl.columns[c].width = Inches(cw)
                for r, row in enumerate(rows):
                    for c, val in enumerate(row):
                        cell = tbl.cell(r, c)
                        cell.text = ""
                        p = cell.text_frame.paragraphs[0]
                        for t, b in _rich(str(val)):
                            run = p.add_run(); run.text = t
                            run.font.size, run.font.name = Pt(s.get("size", 26)), FONT
                            run.font.bold = b or r == 0
                            run.font.color.rgb = WHITE if r == 0 else NAVY
                        cell.fill.solid()
                        cell.fill.fore_color.rgb = NAVY if r == 0 else (PALE if r % 2 else WHITE)
                if s.get("caption"):
                    _text(sl, Inches(0.6), Inches(6.35), Inches(12.1), Inches(0.6), [_rich(s["caption"])],
                          size=24, color=GREY, align=PP_ALIGN.CENTER)
            elif kind == "compare":
                for i, (head, items) in enumerate(s["cols"]):
                    x = Inches(0.6 + i * 6.2)
                    box = sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, top, Inches(5.9), Inches(5.0))
                    box.fill.solid(); box.fill.fore_color.rgb = PALE
                    box.line.color.rgb = TEAL if i == 0 else CORAL; box.line.width = Pt(3)
                    _text(sl, x + Inches(0.3), top + Inches(0.2), Inches(5.3), Inches(0.8), [head], size=32, bold=True,
                          color=TEAL if i == 0 else CORAL)
                    _text(sl, x + Inches(0.3), top + Inches(1.1), Inches(5.3), Inches(3.8),
                          [_rich(b) for b in items], size=28, bullets=True, spacing=12)
            _footer(sl, part_name, n)
        notes = s.get("notes")
        if notes:
            sl.notes_slide.notes_text_frame.text = notes.strip()
        # alt text for pictures (accessibility)
        for shp in sl.shapes:
            if shp.shape_type == 13:  # picture
                shp._element.nvPicPr.cNvPr.set("descr", s.get("alt", s.get("title", "")))
    prs.save(os.path.join(HERE, filename))
    return len(slides)

SG = "../task-2/study-guide/"   # used only in notes text (paths relative to result/task-3/)
TB = "../task-2/test-bank/test-bank.md"

# ================================================================ PART 1
P1 = "Part 1: How Machines Learn"
part1 = [
 dict(kind="title", title="Part 1: How Does a Machine Learn?",
      sub=["Pixel's AI Field Guide · Live session 1 of 3", "Topics 01–03 · about 60 minutes"],
      notes="""
WELCOME (1 min). Introduce yourself and Pixel, the very literal lab robot from the study guide, and Dr. Ada Okafor, who runs the Curiosity Lab. Pixel learns alongside the audience and makes the mistakes beginners make.
Series: Part 1 = how AI works and learns (Topics 01-03). Part 2 = chatbots, types of AI, history (Topics 04-06). Part 3 = AI in the world: uses, harms, rules (Topics 07-10).
No programming or maths needed; the only arithmetic is adding small decimals.
Materials needed: projector; optional internet for the TensorFlow Playground demo (fallback slides included). Paper and pen for the audience help."""),
 dict(kind="big", label="MISSION BRIEF", title="A rule nobody wrote",
      big="Your inbox just blocked a spam email it had **never seen before**.",
      bullets=["Who wrote the rule that caught it?", "Hands up: a programmer?  The computer?  Nobody?"],
      notes="""
OPENING (2 min). Ask for a show of hands for each option. Do NOT give the answer; say "we'll find out by the end of this session".
Expected: most people say "a programmer". The resolution (slide "Back to the inbox") is: nobody wrote that exact rule; the filter learned it from labeled examples.
Fact for the presenter: Gmail moved from hand-written rules to machine-learning-generated rules from 2014 (Topic 02)."""),
 dict(title="Today's route", label="EXPLAIN", bullets=[
      "**1. What counts as AI?**  A test you can use on any app",
      "**2. Two ways to build AI**  Following rules vs learning from examples",
      "**3. Inside learning**  Training, testing, and one artificial neuron",
      "By the end: explain how a spam filter **learns** its rule"],
      notes="""
ROADMAP (1 min). Keep it brief. Learning goals for this part (from the module outline LO1-LO3): define AI as inputs -> inferred outputs; distinguish rule-based AI from machine learning; trace training vs inference; compute one neuron's output.
Transition: "Let's start with the most basic question: what even counts as AI?" """),
 dict(kind="big", label="EXPLAIN", title="What is AI?",
      big="**Input**  →  system **infers**  →  **output**",
      bullets=["AI performs tasks we would say need human intelligence",
               "Outputs: prediction, classification, recommendation, decision, content",
               "To **infer** = to work something out from evidence"],
      notes="""
DEFINITION (3 min). Module definition: "AI is computer technology that performs tasks we would normally say need human intelligence, such as recognizing patterns, understanding language, making decisions or creating content."
OECD (updated Nov 2023): an AI system infers from the input it receives how to generate outputs (predictions, content, recommendations, decisions).
Emphasize: "perform tasks" means results LOOK intelligent; it does not mean the computer thinks or feels. Today's AI is built for particular tasks.
A calculator does not infer: it applies one fixed procedure to every input.
Source: Topic 01, Explanation sections 1-2 (../task-1/topics/01-what-is-ai.md)."""),
 dict(title="AI or not?", label="PREDICT", bullets=[
      "A. Calculator", "B. Spam filter", "C. Alarm clock", "D. Photo app that finds your dog",
      "E. Thermostat with one fixed rule", "F. Predictive text on your phone"],
      notes="""
ACTIVITY (2 min). "Decide for each: AI or not? Discuss with a neighbor for 60 seconds." Then count hands for each letter.
Do not reveal yet; the next slide gives the test and the answers.
Study guide link: Mission 01 Activity 1.1 is the full 12-card version of this sort (../task-2/study-guide/mission-01-is-it-ai.md)."""),
 dict(kind="table", title="The three-question test", label="DEBRIEF",
      rows=[["Question", "AI if…"],
            ["1. Does it turn inputs into outputs?", "yes (all software does)"],
            ["2. Does it infer for new, varied inputs?", "yes, not one fixed rule"],
            ["3. Could a person write an exact recipe for every input?", "no"]],
      widths=[8.1, 4.0],
      caption="AI: B spam filter, D photo app, F predictive text  ·  Not AI: A, C, E",
      notes="""
ANSWER (2 min). Walk through the test with one AI example (photo app: no one can write an exact recipe for recognizing YOUR dog in every lighting and pose) and one non-AI example (alarm clock: one fixed rule, "ring at 7:00").
Common misconception: "anything automatic or smart-sounding is AI". The test is about inferring outputs for new inputs.
Optional aside, the AI effect: once AI works, people stop calling it AI ("AI is whatever hasn't been done yet", Tesler's Theorem as reported by Hofstadter 1979).
Practice: test bank Q1-Q8 (Mission 01) in ../task-2/test-bank/test-bank.md.
Transition: "So how do people build systems that infer? There are two very different ways." """),
 dict(kind="section", title="Two ways to build AI", sub=["Follow rules and search  ·  or learn from examples"]),
 dict(kind="image", title="Rules in, or rules out?", label="EXPLAIN", image="rules-vs-learning",
      alt="Traditional programming: rules plus data go in, answers come out. Machine learning: data plus answers (labeled examples) go in, rules (a model) come out.",
      caption="People write the rules  ·  or the rules are learned from examples",
      notes="""
KEY CONTRAST (3 min). Point to the top row: a person writes the rules (rule-based or "symbolic" AI). Example: MYCIN (Stanford, early 1970s), about 600 IF-THEN rules giving antibiotic advice.
Bottom row: we give examples with the right answers (labels) and a learning algorithm produces the rules, called a model. This is machine learning (ML).
"Old vs new" is rough: both are still used, and hybrids exist (AlphaGo combined deep neural networks with search, 2016).
Diagram credit: original diagram created for this module (framing commonly attributed to F. Chollet, Deep Learning with Python, 2017).
Source: Topic 02, Explanation sections 2-4. Transition: "First, rules. Here is a puzzle that rule-based AI solves perfectly." """),
 dict(kind="big", label="TRY IT", title="Pixel's river problem",
      big="Farmer, wolf, goat, cabbage. Boat holds the farmer + **one** item.",
      bullets=["Never leave wolf + goat alone. Never leave goat + cabbage alone.",
               "**What must the first crossing be?**  (30 seconds)"],
      notes="""
PUZZLE (2 min). Read the rules aloud. Give 30 seconds of silent thinking, then take answers.
Expected answer (next slide): the farmer must take the goat. Taking the wolf leaves goat + cabbage; taking the cabbage leaves wolf + goat; going alone leaves everything.
Live option: open ../task-2/activities/river-crossing/river-crossing.html (works offline) and let a volunteer try a wrong move; the page explains why it fails. Fallback: this slide and the next."""),
 dict(title="Why only the goat works", label="DEBRIEF", bullets=[
      "Take the wolf → goat eats cabbage", "Take the cabbage → wolf eats goat",
      "Go alone → both pairs are left together", "Take the goat → **the only safe state**",
      "Pixel's lesson: describe the problem precisely, then check every move"],
      notes="""
DEBRIEF (1 min). Each tempting move breaks a rule. This is exactly how a computer checks moves: it tests each possible action against the rules.
Transition: "To let a computer solve the whole puzzle, we describe it as a set of states and moves." """),
 dict(kind="table", title="The puzzle as states", label="EXPLAIN",
      rows=[["Crossings", "New safe states reached  (left bank | right bank)"],
            ["0", "FWGC |"], ["1", "WC | FG"], ["2", "FWC | G"], ["3", "C | FWG     or     W | FGC"],
            ["4", "FGC | W     or     FWG | C"], ["5", "G | FWC"], ["6", "FG | WC"], ["7", "| FWGC   goal!"]],
      widths=[2.6, 9.5], size=24,
      caption="F farmer · W wolf · G goat · C cabbage  ·  10 safe states, 7 crossings",
      notes="""
STATE SPACE (3 min). Vocabulary: a STATE is one arrangement (who is on which bank), e.g. "FWGC |" = everyone on the left. ACTIONS are crossings. RULES say which states are allowed. The GOAL is "| FWGC".
This table is exactly what breadth-first search discovers, level by level: all states 1 crossing away, then 2, and so on, never revisiting a state. At level 3 the search splits into two equally short routes (wolf first or cabbage first), which rejoin at level 5.
Facts verified by script (Topic 02): 16 possible arrangements, 10 safe, minimum 7 crossings, exactly 2 shortest solutions.
The full state-graph diagram (../task-2/assets/images/river-crossing-state-graph.svg) is too detailed to project; use it as a handout or point learners to Mission 02 Activity 2.2."""),
 dict(kind="table", title="The two shortest plans", label="EXPLAIN",
      rows=[["Crossing", "Plan A (wolf first)", "Plan B (cabbage first)"],
            ["1", "take goat →", "take goat →"], ["2", "← return alone", "← return alone"],
            ["3", "take wolf →", "take cabbage →"], ["4", "← bring goat back", "← bring goat back"],
            ["5", "take cabbage →", "take wolf →"], ["6", "← return alone", "← return alone"],
            ["7", "take goat →", "take goat →"]],
      widths=[2.3, 4.9, 4.9], size=24,
      notes="""
SEARCH TRACE (3 min). Breadth-first search (BFS) explores all states 1 crossing away, then all states 2 crossings away, and so on, skipping states it has already visited. So the first time it reaches the goal, it has found a plan with the fewest crossings.
Reveal rows one by one if you like (or point down the table). Ask: "Why does the goat come BACK at crossing 4?" Answer: otherwise the goat is left with the item just delivered.
Full trace with frontier and visited set: ../task-2/activities/river-crossing/solver-output.txt; study guide Mission 02 Activity 2.3."""),
 dict(kind="compare", title="Search: strengths and limits", label="EXPLAIN", cols=[
      ("Strengths", ["Guaranteed correct plan", "BFS finds the shortest plan", "Every step can be explained"]),
      ("Limits", ["Needs exact rules written by people", "States can explode in number", "Learns nothing from experience"])],
      notes="""
WRAP-UP OF RULES (2 min). Rule-based AI shines when the world can be described exactly (puzzles, route planning, games like chess).
"Combinatorial explosion": in big problems the number of states grows so fast that searching them all is impossible; this helped cause the first AI winter (Part 2).
Transition: "Now try writing exact rules for spam. 'Contains the word free'? Your friend writes 'free for lunch?'. We need another approach: learning." """),
 dict(kind="section", title="Learning from examples", sub=["Training, testing, and Pixel's spam filter"]),
 dict(kind="image", title="Two phases: training and inference", label="EXPLAIN", image="ml-pipeline",
      alt="Machine-learning pipeline. Training phase: collect data, prepare features and labels, train, model, test and evaluate, with a loop back if results are poor. Inference phase: new input goes into the trained model, which outputs a prediction.",
      notes="""
PIPELINE (3 min). TRAINING: the algorithm adjusts the model's parameters (weights) using labeled training data. FEATURES are the measurable inputs (e.g. "contains free", number of links); the LABEL is the right answer (spam / not spam).
TEST: we keep some labeled examples aside (the test set) and check the model on them, because doing well on examples you have already seen proves little.
INFERENCE (prediction): the finished model is used on new emails; it no longer changes while it predicts.
Source: Topic 02 Explanation section 3; Topic 03 section 3."""),
 dict(kind="table", title="What Pixel's filter learned", label="EXPLAIN",
      rows=[["Feature", "Weight"], ["contains \"free\"", "+2"], ["contains \"urgent\"", "+2"],
            ["contains \"meeting\"", "−2"], ["contains \"invoice\"", "0"], ["3 or more links", "+1"]],
      widths=[7.1, 5.0],
      caption="Rule: score of 2 or more → spam  ·  illustrative (made-up) figures",
      notes="""
WORKED EXAMPLE (2 min). These weights came from counting words in 10,000 labeled training emails (4,000 spam, 6,000 not spam): words much more common in spam get positive weights, words more common in normal email get negative weights. All figures are illustrative (made-up), as in Topic 02.
Nobody typed "+2 for free"; the counts produced it. This is the answer to our opening question taking shape."""),
 dict(kind="big", label="PREDICT", title="Spam or not?",
      big="Score each email (threshold: 2)",
      bullets=["**Email 1:** \"URGENT: claim your free gift\" + 4 links",
               "**Email 2:** \"Meeting moved, free coffee provided\""],
      notes="""
ACTIVITY (2 min). Give 45 seconds; neighbors compare. Weights are on the previous slide (go back if needed or leave it printed on a handout).
Answers (next slide): Email 1 = urgent +2, free +2, 3+ links +1 = 5 -> spam. Email 2 = meeting -2, free +2 = 0 -> not spam.
Point: one word ("free") does not decide; the combination does."""),
 dict(title="Answers", label="DEBRIEF", bullets=[
      "**Email 1:** +2 urgent +2 free +1 links = **5** → spam",
      "**Email 2:** −2 meeting +2 free = **0** → not spam",
      "On 2,000 test emails: **93% correct**",
      "60 false positives (good mail blocked) · 80 false negatives (spam got through)"],
      notes="""
DEBRIEF (2 min). Test set (illustrative): 2,000 emails = 800 spam + 1,200 not spam. Caught 720 of 800 spam (80 false negatives); 60 genuine emails wrongly blocked (false positives); 1,860 / 2,000 = 93% accuracy.
FALSE POSITIVE = a wrong "yes" (genuine email sent to spam). FALSE NEGATIVE = a wrong "no" (spam reaches the inbox).
Quick question: "If we lower the threshold from 2 to 1, what happens?" Expected: more emails flagged -> more false positives, fewer false negatives. Every threshold is a trade-off.
Practice: Mission 04 Activity 4.1 "Be the spam filter"; runnable version ../task-2/activities/spam-filter/ (Python or Colab)."""),
 dict(kind="table", title="Which fruit model would you trust?", label="PREDICT",
      rows=[["Model", "Training set", "Test set"], ["A: skin rule (bumpy = orange)", "8 / 8", "?"],
            ["B: memorizer (exact weight match)", "8 / 8", "?"], ["C: weight rule (> 165 g = orange)", "7 / 8", "?"]],
      widths=[7.3, 2.4, 2.4],
      caption="Predict: which model does best on 4 new fruits?  ·  illustrative (made-up) data",
      notes="""
ACTIVITY (2 min). Ask for a hand vote: A, B or C? Many pick B because it is "perfect".
Answer (next slide): A 4/4, B 2/4, C 2/4. Source: Topic 03 Worked example Part A."""),
 dict(title="Perfect on practice, poor on new data", label="DEBRIEF", bullets=[
      "Test scores: **A 4/4** · B 2/4 · C 2/4",
      "B memorized the examples: **overfitting**",
      "C was too simple: **underfitting**",
      "Only the test set revealed the difference"],
      notes="""
DEBRIEF (2 min). OVERFITTING: a model matches its training data so closely that it fails on new data; the warning sign is a big gap between training and test results. UNDERFITTING: too simple to capture the real pattern, poor even on training data.
Pixel joke from the guide: Pixel memorized every answer in last year's quiz and was baffled when the questions changed.
Reduce overfitting (intuition): more varied data; simpler models when they work as well; always test on unseen data.
Practice: test bank Mission 04 questions Q28-Q39."""),
 dict(kind="table", title="Three ways a machine can learn", label="EXPLAIN",
      rows=[["Kind", "Learns from", "Example"], ["Supervised", "labeled examples", "spam filter"],
            ["Unsupervised", "unlabeled data (finds groups)", "grouping customers"],
            ["Reinforcement", "rewards and penalties", "game-playing agent, robot maze"]],
      widths=[3.3, 4.6, 4.2],
      notes="""
KINDS OF LEARNING (2 min). Supervised: the right answers (labels) are given; classification = a category, regression = a number. Unsupervised: no labels; the algorithm finds structure such as clusters. Reinforcement: an agent acts in an environment and learns from rewards and penalties.
Optional demo/side quest: ../task-2/activities/robot-maze/robot-maze.html compares a fixed rule, search (BFS) and Q-learning (reinforcement learning) in the same maze.
Transition: "Many of today's most impressive models are neural networks. Let's open one up." """),
 dict(kind="section", title="Inside a neural network", sub=["One artificial neuron, then layers"]),
 dict(kind="table", title="Be the neuron", label="TRY IT",
      rows=[["Input", "Value", "Weight"], ["x1: contains \"free\"", "1", "0.6"],
            ["x2: sender in contacts", "0", "−0.4"], ["x3: 3 or more links", "1", "0.3"],
            ["bias", "", "−0.5"]],
      widths=[6.5, 2.4, 3.2],
      caption="Multiply, add, add the bias. Output 1 (spam) if the sum is greater than 0.",
      notes="""
ACTIVITY (2 min). The neuron is a tiny spam detector (illustrative numbers, identical to Topic 03 Part B and the neuron diagram on the next slide).
Steps: multiply each input by its weight; add them and the bias; apply the step function (1 if the sum is greater than 0, otherwise 0).
Give 60 seconds. Answer on the next slide: 0.6 + 0 + 0.3 - 0.5 = 0.4 > 0 -> output 1 (spam)."""),
 dict(kind="image", title="The neuron's answer", label="DEBRIEF", image="artificial-neuron",
      alt="Artificial neuron: inputs 1, 0, 1 multiplied by weights 0.6, -0.4 and 0.3, plus bias -0.5, give a sum of 0.4; the step activation outputs 1.",
      caption="Sum = **0.4** > 0 → output **1** (spam)  ·  if x2 = 1, sum = 0.0 → 0",
      notes="""
DEBRIEF (2 min). With x2 = 1: 0.6 - 0.4 + 0.3 - 0.5 = 0.0, which is not greater than 0, so output 0 (not spam): the negative weight pulled the decision back exactly to the boundary.
Other activations: sigmoid(0.4) is about 0.60; ReLU gives 0.4.
Where do weights come from? Nobody sets them by hand: training starts with rough weights and nudges them, example after example. The perceptron (Rosenblatt, 1958) was the first famous version.
Misconception: neuron "bias" is a parameter; unfair bias is Part 3 (Topic 08).
Practice: Mission 05 Activity 5.1; test bank Q40-Q49."""),
 dict(kind="image", title="Layers make it deep", label="EXPLAIN", image="neural-network-layers",
      alt="Neural network with 3 input nodes, two hidden layers of 4 nodes each, and 2 output nodes, fully connected between consecutive layers.",
      caption="**Deep** = more than one hidden layer · learns its own features · hard to explain",
      notes="""
LAYERS (3 min). Say aloud: deep networks need lots of data and computing power (GPUs) and are hard to explain, often called "black boxes" (accountability, Part 3). Each neuron takes all outputs of the previous layer as inputs. In image recognition, early layers respond to edges and color patches, later layers to shapes, the last to whole objects; nobody programs these features, they emerge in training.
Module rule of thumb: deep = more than one hidden layer (IBM: at least 4 layers counting input and output). "Deep" means many layers, NOT deep understanding.
Without activation functions, stacking layers adds nothing ("linear operations performed on linear operations are still linear", Google ML course)."""),
 dict(kind="bullets", title="Live demo: TensorFlow Playground", label="DEMO", bullets=[
      "Question: can a network with **no hidden layer** separate a circle?",
      "Run 1: circle data, 0 hidden layers → predict, then press play",
      "Run 2: add 1 hidden layer of 4 neurons → compare",
      "Notice: the boundary bends only when hidden neurons exist"],
      notes="""
DEMO (4 min). Before class open both presets in tabs (internet needed; no account):
Preset P1 (0 hidden layers): https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false
Preset P2 (1 hidden layer, 4 neurons): same URL with networkShape=4.
Steps: 1) ask the question; 2) press play on P1 for about 10 seconds: the boundary stays a straight line and test loss stays high; 3) switch to P2: the boundary curves around the circle and loss drops.
Results vary a little each run because starting weights are random. LAB NOTE: the Playground uses tiny 2-D toy datasets; real networks have millions of weights.
FALLBACK (no internet): describe the expected outcomes above and use Mission 05's simulated-results table (../task-2/study-guide/mission-05-inside-the-neuron.md)."""),
 dict(kind="image", title="Back to the inbox", label="TAKEAWAY", image="ai-ml-dl-genai-nested",
      alt="Nested circles: artificial intelligence contains machine learning, which contains deep learning, which contains generative AI.",
      caption="Who wrote the spam rule? **Nobody**: it was learned from labeled examples",
      notes="""
CONCLUSION (3 min). Resolve the opening: the filter's rule was produced by training on labeled examples and checked on a test set; no person typed it.
Connect the nest: AI includes rule-based systems like the river-crossing search; machine learning is the part that learns from data (the spam filter); deep learning uses many-layered neural networks; generative AI (next session) sits inside deep learning, with the caveat that some older generative methods were not deep learning.
Take-away sentence: "Rule-based AI follows rules people write; machine learning writes its own rules from examples, and we must test it on data it has never seen." """),
 dict(title="Next steps", label="NEXT STEPS", bullets=[
      "Study guide: **Missions 01–05**  (start at 00-start-here.md)",
      "Practice: test bank **Q1–Q49**",
      "Try: river-crossing page · Prolog in SWISH · Teachable Machine",
      "Next session: **how chatbots write**, types of AI, history"],
      notes="""
NEXT STEPS (1 min). Files (relative to result/task-3/):
- Study guide start: ../task-2/study-guide/00-start-here.md; Missions 01 Is It AI?, 02 The River Problem, 03 Pixel's Rulebook (Prolog rule-based systems, not covered live), 04 Learning from Examples, 05 Inside the Neuron.
- Test bank: ../task-2/test-bank/test-bank.md, Mission 01-05 sections (Q1-Q49), answer key at the end.
- Videos: study guide resources page (../task-2/study-guide/resources.md), e.g. V2 Code.org "What is Machine Learning?" and V3 "How Neural Networks Work".
- Video scripts for replayable demos: ../task-1/formats/video-scripts/video-scripts.md (V02 spam filter, V03 neuron by hand)."""),
]

# ================================================================ PART 2
P2 = "Part 2: Chatbots, Types and History"
part2 = [
 dict(kind="title", title="Part 2: How Does a Chatbot Write?",
      sub=["Pixel's AI Field Guide · Live session 2 of 3", "Topics 04–06 · about 60 minutes"],
      notes="""
WELCOME (1 min). Recap Part 1 in one sentence: machine learning writes its own rules from examples and is checked on a test set; deep learning uses many-layered neural networks.
Today: generative AI and large language models (LLMs), the two ways of classifying AI, and 75 years of AI booms and winters, ending with "why now?"."""),
 dict(kind="big", label="MISSION BRIEF", title="Finish the sentence",
      big="\"The cat sat on the ___\"",
      bullets=["Shout out the next word", "How did you choose it so fast?"],
      notes="""
OPENING (2 min). Take a few answers: most people say "mat"; some say "floor" or "sofa".
Say: "You just did what a large language model does, one word-piece at a time, billions of times." Promise to explain how, and why it sometimes says things that are false.
Resolution at the end: a chatbot builds every reply by repeatedly predicting a likely next token; it was trained on huge amounts of text, it is narrow AI, and it is the product of a 70-year story."""),
 dict(title="Today's route", label="EXPLAIN", bullets=[
      "**1. Generative AI**  How an LLM writes, one token at a time",
      "**2. Types of AI**  Two different ways to classify AI",
      "**3. History**  The start, the AI winters and the big comeback",
      "Finale: **why did AI explode now?**"],
      notes="""
ROADMAP (1 min). Goals (LO2-LO5): distinguish generative from discriminative AI; trace next-token prediction; classify systems by capability and by functionality; explain the causes of the AI winters and the comeback."""),
 dict(kind="compare", title="Create, or decide?", label="EXPLAIN", cols=[
      ("Generative AI", ["Creates **new content**", "Text, images, audio, code", "e.g. chatbot reply, image generator"]),
      ("Discriminative AI", ["Labels, scores or predicts", "Chooses among answers", "e.g. spam filter, face unlock"])],
      notes="""
CONTRAST (2 min). Google's ML course: "Generative models can generate new data instances. Discriminative models discriminate between different kinds of data instances."
Link back: the Part 1 spam filter is discriminative (it outputs a label).
Quick check: "Is a house-price predictor generative?" No: it predicts a number."""),
 dict(title="Tokens: the pieces an LLM reads and writes", label="EXPLAIN", bullets=[
      "A **token** = a word, part of a word, punctuation or a character",
      "\"unbelievable\" might be 2–3 tokens",
      "Rule of thumb: 100 tokens ≈ 75 English words",
      "An **LLM** is a huge neural network trained to predict the next token"],
      notes="""
TOKENS (2 min). LLM = large language model: a very large deep neural network, usually a transformer (Vaswani et al., 2017), trained on huge amounts of text to predict the next token. GPT-3 (2020) had 175 billion parameters.
Rule of thumb from OpenAI/Google: about 3/4 of an English word per token.
Context window = the maximum number of tokens the model can consider at once."""),
 dict(kind="image", title="Next-token prediction", label="EXPLAIN", image="next-token-prediction",
      alt="The prompt 'The cat sat on the' goes into a language model, which gives probabilities: mat 0.41, floor 0.17, sofa 0.12, roof 0.06, other 0.24. The chosen token is appended and the loop repeats.",
      caption="Probabilities are illustrative (made-up)",
      notes="""
THE LOOP (3 min). Step through slowly:
1) The model reads all the text so far. 2) It gives EVERY possible next token a probability. 3) It chooses one, usually by SAMPLING (a weighted random pick), not always the most likely. 4) It appends the token. 5) It repeats until it produces an end token.
Point at the bars: mat 0.41, floor 0.17, sofa 0.12, roof 0.06, other 0.24 (sum 1.00).
Misconception: the model does not look up a stored answer; it builds the reply piece by piece."""),
 dict(title="Same prompt, different answers?", label="PREDICT", bullets=[
      "**Temperature** controls how adventurous the choice is",
      "Low temperature: \"mat\" chosen… more often or less often?",
      "High temperature: what happens to \"roof\"?",
      "Vote, then discuss with a neighbor (45 s)"],
      notes="""
ACTIVITY (2 min). Let people vote by hand: low temperature -> "mat" more often? Answer on next slide.
Study guide link: Mission 06 Activity 6.2 (next-token spinner and temperature tally with 20 fixed random numbers)."""),
 dict(title="Why outputs vary", label="DEBRIEF", bullets=[
      "**Low** temperature: sharper odds → \"mat\" almost every time",
      "**High** temperature: flatter odds → \"roof\" appears more",
      "Sampling explains why the same prompt gives different replies",
      "Likely ≠ true: fluent text can be false (**hallucination**)"],
      notes="""
DEBRIEF (2 min). Low temperature = predictable, repetitive; high = varied, surprising, more errors. Outputs can also change because models are updated and because of context.
HALLUCINATION = plausible but false output. It follows directly from the loop: the model produces likely-sounding text and has no built-in fact check. Full treatment in Part 3 (Topic 09).
Practice: test bank Q50-Q59 (Mission 06)."""),
 dict(kind="table", title="How a chatbot is trained", label="EXPLAIN",
      rows=[["Stage", "What happens"], ["1. Pre-training", "predict the next token in huge amounts of text"],
            ["2. Fine-tuning", "learn from example prompts and good replies"],
            ["3. Human feedback (RLHF)", "people rank replies; the model is rewarded"]],
      widths=[4.6, 7.5],
      caption="InstructGPT (2022): a 1.3B RLHF model beat the 175B GPT-3",
      notes="""
TRAINING (2 min). Pre-training is self-supervised: the real next token in the text is the label, so no one has to label data by hand. Fine-tuning is supervised. RLHF = reinforcement learning from human feedback, linking back to "reinforcement learning" in Part 1.
Point of the caption: how a model is trained matters, not only its size.
Caveat: "almost all of today's prominent generative AI systems use deep learning; earlier generative methods such as Markov-chain text generators (Shannon, 1948) did not." Mission 06 Activity 6.1 lets learners run a Markov-chain generator with cards."""),
 dict(kind="section", title="Types of AI", sub=["Two different lenses, not one ladder"]),
 dict(kind="image", title="Two ways to classify AI", label="EXPLAIN", image="types-of-ai-two-lenses",
      alt="Two panels. By capability: narrow AI exists today; general AI (AGI) is hypothetical; superintelligence is speculative. By functionality: reactive machines and limited memory exist today; theory of mind and self-aware are hypothetical.",
      notes="""
TWO LENSES (3 min). Analogy: you can sort cars by size AND by fuel type; these are different questions, not one ladder.
Lens 1, capability: narrow AI (ANI, the only kind that exists), general AI (AGI, hypothetical: matching human abilities across any task), superintelligence (ASI, speculative; Bostrom 2014).
Lens 2, functionality (a popular-press taxonomy, Hintze 2016, not a formal scientific standard): reactive machines (e.g. Deep Blue), limited memory (uses recent observations while it works, e.g. a self-driving car tracking nearby cars, a chatbot using the conversation in its context window), theory of mind and self-aware (hypothetical).
Misconception: "memory" here is NOT training data."""),
 dict(title="Classify a chatbot", label="PREDICT", bullets=[
      "Capability lens: narrow, general or super?",
      "Functionality lens: reactive or limited memory?",
      "Write down both answers and one reason each (60 s)"],
      notes="""
ACTIVITY (2 min). Answer on the next slide. Expect some people to say "general" because chatbots discuss many topics: that is the misconception to address."""),
 dict(kind="table", title="Both lenses at once", label="DEBRIEF",
      rows=[["System", "Capability", "Functionality"], ["Deep Blue (1997)", "narrow", "reactive"],
            ["Self-driving car", "narrow", "limited memory"], ["Chatbot (LLM)", "narrow (debated)", "limited memory"],
            ["Netflix recommender", "narrow", "disputed"]],
      widths=[5.0, 3.6, 3.5],
      notes="""
DEBRIEF (2 min). Chatbot: mainstream view is that current LLMs are NOT AGI; this is debated and there is no agreed test or definition. It uses the conversation so far (context window) -> limited memory.
Netflix: IBM lists recommendations as reactive; others argue limited memory, so learners should justify their choice.
Everything that exists today is narrow AND either reactive or limited memory.
Practice: Mission 07 two-lens card sort; test bank Q60-Q68."""),
 dict(kind="section", title="75 years of AI", sub=["The start · the failures · the big comeback"]),
 dict(kind="image", title="The AI timeline", label="EXPLAIN", image="ai-history-timeline",
      alt="Timeline 1950 to 2025: 1950 Turing paper; 1956 Dartmouth workshop; 1958 perceptron; 1966 ELIZA; first AI winter about 1974 to 1980; 1980s expert systems boom; second AI winter about 1987 to 1993; 1997 Deep Blue; 2012 AlexNet; 2016 AlphaGo; 2017 transformer; 2022 ChatGPT.",
      caption="Winter dates are approximate",
      notes="""
OVERVIEW (2 min). Three phases: the Start (1950s-60s), the Failures (two AI winters with the 1980s expert-systems boom between them), the Big Comeback (1997 on; deep learning from 2012). Don't read every date now; the next slides zoom in."""),
 dict(kind="table", title="The start: big ideas, big promises", label="EXPLAIN",
      rows=[["Year", "Milestone"], ["1950", "Turing asks \"Can machines think?\" (imitation game)"],
            ["1955", "Dartmouth proposal coins \"artificial intelligence\""],
            ["1956", "Dartmouth workshop; Logic Theorist proves theorems"],
            ["1958", "Rosenblatt's perceptron (a learning neuron)"], ["1966", "Weizenbaum's ELIZA chatbot"]],
      widths=[1.8, 10.3],
      notes="""
THE START (3 min). Correction to a common error: the term "artificial intelligence" first appears in the August 1955 proposal (McCarthy, Minsky, Rochester, Shannon); the workshop took place in summer 1956.
The perceptron is the neuron from Part 1. Newspapers hyped it as a machine that would one day be conscious.
ELIZA (1966) used simple pattern matching with its DOCTOR script, yet people felt understood: the "ELIZA effect".
Optional demo: ELIZA web version listed in ../task-2/study-guide/resources.md (Mission 08 Activity 8.2 has test inputs and a fallback). Type "I am worried about my exams" and show that it reflects your words back without understanding."""),
 dict(title="The failures: two AI winters", label="EXPLAIN", bullets=[
      "**~1974–1980:** promises outran results; funding cut (Lighthill report, 1973)",
      "Problems: too many states to search; single-layer perceptrons were limited (1969)",
      "**1980s boom:** expert systems such as XCON saved companies millions",
      "**~1987–1993:** expert systems proved brittle and costly; market collapsed"],
      notes="""
WINTERS (3 min). An AI winter = a period of reduced funding and interest. Causes: over-promising, technical limits (combinatorial explosion from Part 1's search; Minsky & Papert's Perceptrons, 1969, showed single-layer limits such as XOR), and cost.
XCON (DEC, from 1980) configured computer orders; savings estimates range from about $25M to $40M a year. Expert systems could not learn and broke outside their rules; the Lisp-machine market collapsed in 1987.
1986: backpropagation popularized (Rumelhart, Hinton, Williams) - neural networks quietly improved."""),
 dict(kind="big", label="PREDICT", title="Deep Blue beats Kasparov (1997)",
      big="Did Deep Blue **learn** chess, or **search**?",
      bullets=["Use Part 1: rules + search, or learning from examples?"],
      notes="""
ACTIVITY (1 min). Hand vote. Most people guess "learned".
Answer next slide: it searched, about 200 million positions per second, using rules and evaluation written with experts; it was not machine learning."""),
 dict(kind="table", title="The big comeback", label="DEBRIEF",
      rows=[["Year", "Milestone", "Approach"], ["1997", "Deep Blue beats Kasparov 3.5–2.5", "search"],
            ["2012", "AlexNet: 15.3% vs 26.2% error on ImageNet", "deep learning"],
            ["2016", "AlphaGo beats Lee Sedol 4–1", "deep learning + RL + search"],
            ["2017", "Transformer architecture", "deep learning"], ["2022", "ChatGPT released (30 Nov)", "LLM"]],
      widths=[1.6, 6.9, 3.6], size=24,
      notes="""
DEBRIEF + COMEBACK (3 min). Deep Blue = search, not ML. AlexNet (about 60 million weights, trained on GPUs) cut the top-5 error from 26.2% to 15.3% and launched the deep-learning era. AlphaGo combined deep neural networks, reinforcement learning and search (famous move 37). The transformer (2017, "Attention Is All You Need") underlies today's LLMs.
Practice: Mission 08 timeline card sort; test bank Q69-Q78."""),
 dict(title="Why did AI explode now?", label="TAKEAWAY", bullets=[
      "Neural networks existed since **1958**",
      "They waited for three ingredients at once:",
      "**Data** (the internet) · **Compute** (GPUs) · **Better algorithms**",
      "Hype pattern: breakthrough → big promises → hard limits → winter?"],
      notes="""
FINALE (3 min). The "best for last" insight: the comeback was not a sudden invention. The 1958 neuron idea needed huge datasets, GPU computing power and better training methods, all strong at the same time around 2012.
Hype cycle lesson (Topic 06): breakthrough -> over-generalized promises -> hard limits -> winter, unless the technology delivers real value (then a steady phase).
Discussion (90 s, neighbors): "A start-up says its AI will replace all doctors by next year. Which warning signs from history do you see?" Expected: sweeping promise, short timeline, one success generalized to everything, no evidence on real patients."""),
 dict(title="Answering the opening", label="TAKEAWAY", bullets=[
      "A chatbot writes by **predicting the next token**, again and again",
      "Trained on huge text, then fine-tuned with human feedback",
      "It is **narrow AI** with limited memory (mainstream view)",
      "Built on 70 years of ideas, data and compute"],
      notes="""
CONCLUSION (2 min). Link back to "The cat sat on the ___": the audience predicted a likely word; an LLM does the same with probabilities over tokens and sampling. Because "likely" is not "true", chatbots can hallucinate, which leads into Part 3."""),
 dict(title="Next steps", label="NEXT STEPS", bullets=[
      "Study guide: **Missions 06–08**",
      "Practice: test bank **Q50–Q78**",
      "Watch: 3Blue1Brown \"Large Language Models explained briefly\"",
      "Next session: **AI in the world**: uses, harms and rules"],
      notes="""
NEXT STEPS (1 min). Files (relative to result/task-3/):
- ../task-2/study-guide/mission-06-the-word-guessing-machine.md, mission-07-sorting-the-robots.md, mission-08-time-machine.md
- ../task-2/test-bank/test-bank.md, Missions 06-08 (Q50-Q78)
- Video V6 (3Blue1Brown, "Large Language Models explained briefly") and V5 (Crash Course AI #3) are introduced with viewing questions in ../task-2/study-guide/resources.md
- Video scripts V04 (next-token loop), V05 (two lenses), V06 (timeline): ../task-1/formats/video-scripts/video-scripts.md"""),
]

# ================================================================ PART 3
P3 = "Part 3: AI in the World"
part3 = [
 dict(kind="title", title="Part 3: Who Is Responsible When AI Gets It Wrong?",
      sub=["Pixel's AI Field Guide · Live session 3 of 3", "Topics 07–10 · about 60 minutes"],
      notes="""
WELCOME (1 min). Recap: Part 1 = how machines learn; Part 2 = how chatbots write (next-token prediction, hallucination) and AI's history. Today: real applications, ethical risks, limitations and myths, and the rules being written."""),
 dict(kind="big", label="MISSION BRIEF", title="A real court case (2023)",
      big="A lawyer filed a brief citing **six court cases** found with ChatGPT. None of them existed.",
      bullets=["Who is responsible: the lawyer, the chatbot, or its maker?"],
      notes="""
OPENING (2 min). Case: Mata v. Avianca (US federal court, June 2023). The lawyers were sanctioned $5,000. Ask for hands for each option; don't resolve yet.
Resolution at the end: the human user stays accountable for checking AI output; makers and regulators also carry responsibilities, which is what the new rules address."""),
 dict(title="Today's route", label="EXPLAIN", bullets=[
      "**1. AI at work**  A six-part way to analyze any application",
      "**2. What can go wrong**  Bias, jobs, privacy and more",
      "**3. Limits and myths**  Why AI makes things up",
      "**4. The rules**  The EU AI Act and the AGI debate"],
      notes="ROADMAP (1 min). Goals LO6-LO9: analyze applications; discuss ethical risks with evidence; correct misconceptions and check for hallucinations; classify systems into EU AI Act risk tiers and explain the AGI debate fairly."),
 dict(kind="table", title="Analyze any AI application", label="EXPLAIN",
      rows=[["Ask", "Example: film recommender"], ["Input", "your ratings and viewing history"],
            ["Output", "a ranked list of films"], ["AI type", "machine learning"],
            ["Benefit / risk", "find films fast / filter bubbles, privacy"], ["Human oversight", "low stakes: little needed"]],
      widths=[4.0, 8.1],
      notes="""
FRAMEWORK (3 min). Six parts: input, output, AI type (rule-based / ML / deep learning / generative), benefit, risk, human oversight. Rule: the higher the stakes of an error, the more human oversight is needed.
Netflix (company figures, 2015 paper): the recommender influences about 80% of hours streamed.
How a recommender works: collaborative filtering = "people with similar taste liked this". Mission 09 Activity 9.1 traces one by hand."""),
 dict(kind="table", title="Should Sam watch Film D?", label="TRY IT",
      rows=[["User", "Film A", "Film B", "Film C", "Film D"], ["Sam", "5", "4", "1", "?"],
            ["Priya", "5", "5", "1", "5"], ["Leo", "1", "2", "5", "1"]],
      widths=[3.3, 2.2, 2.2, 2.2, 2.2],
      caption="Whose taste is closest to Sam's?  ·  illustrative (made-up) ratings",
      notes="""
ACTIVITY (2 min). Ask: add up the rating differences on Films A-C. Sam vs Priya: 0 + 1 + 0 = 1. Sam vs Leo: 4 + 2 + 4 = 10. Priya is most similar and rated Film D 5 -> recommend Film D.
Risk to raise: a brand-new film nobody has rated cannot be recommended (cold-start problem), so popular items get more popular.
Source: Topic 07 Worked example."""),
 dict(title="Rank by stakes", label="PREDICT", bullets=[
      "A. Song recommendations", "B. Navigation app route",
      "C. AI eye-disease screening", "D. Self-driving taxi",
      "Order from lowest to highest stakes. How much human checking does each need?"],
      notes="""
ACTIVITY (2 min). Neighbors agree on an order (60 s). Answer on the next slide."""),
 dict(title="Higher stakes, more oversight", label="DEBRIEF", bullets=[
      "**A → B → C / D**: annoyance → delay → health and life",
      "Eye screening: IDx-DR (2018), ~87% sensitivity, ~90% specificity",
      "Self-driving: Uber test car killed a pedestrian (Tempe, 2018)",
      "Ask: who checks the AI, and who answers for errors?"],
      notes="""
DEBRIEF (2 min). C and D can be argued either way at the top; what matters is the reasoning about the consequence of an error.
IDx-DR (April 2018) was the first FDA-authorized autonomous AI screening system (diabetic retinopathy). Sensitivity = share of real cases caught; specificity = share of healthy people correctly cleared.
Uber, Tempe, March 2018: the NTSB found late detection, a distracted safety driver and poor safety culture -> accountability.
Waymo publishes safety figures; they are company-reported, so treat with care.
Practice: test bank Q79-Q86."""),
 dict(kind="section", title="What can go wrong?", sub=["Bias · privacy · jobs · accountability · environment · misinformation"]),
 dict(kind="image", title="Where bias gets in", label="EXPLAIN", image="ai-system-lifecycle-bias",
      alt="Cycle of seven stages: problem definition, data collection, labeling, training, testing, deployment, feedback and monitoring, with callouts showing where bias can enter at each stage.",
      notes="""
BIAS LIFE CYCLE (3 min). Bias can enter at every stage: wrong proxy target (problem definition), unrepresentative data, biased labels, the model learning unfair patterns or ignoring small groups, a test set missing groups, use on a different population, feedback loops.
Examples: Amazon's experimental hiring tool penalized CVs containing "women's" (Reuters 2018); a US healthcare algorithm used cost as a proxy for need and under-served Black patients (Obermeyer et al., 2019).
Link to Part 1: a model learns whatever patterns are in its training data."""),
 dict(kind="table", title="Gender Shades (2018)", label="EXPLAIN",
      rows=[["Group", "Highest error rate"], ["Lighter-skinned men", "0.8%"], ["Darker-skinned women", "34.7%"]],
      widths=[7.1, 5.0],
      caption="1,270 parliamentarians \u00b7 Buolamwini & Gebru, 2018",
      notes="""
CASE (2 min). Joy Buolamwini and Timnit Gebru tested gender classifiers from IBM, Microsoft and Face++ on photos of 1,270 parliamentarians from three African and three European countries. Error rates reached 34.7% for darker-skinned women compared with at most 0.8% for lighter-skinned men.
Lesson: one overall accuracy number can hide big differences; test results separately for each group (disaggregated evaluation).
Video: V9 Joy Buolamwini TED talk, introduced in ../task-2/study-guide/resources.md."""),
 dict(title="Unbalanced training data", label="PREDICT", bullets=[
      "Teachable Machine: train to recognize two people",
      "Person A: 50 photos · Person B: 5 photos",
      "Who gets misrecognized more often? Why?"],
      notes="""
ACTIVITY (2 min). Hand vote: A or B?
Answer: usually person B, because the model has seen far fewer examples of B and tends to favor the class it saw more often. This is a typical tendency, not a guarantee: results vary by photos, lighting and backgrounds.
Live option (webcam + internet, no account): Teachable Machine image project (https://teachablemachine.withgoogle.com/); Mission 10 Activity 10.2 has exact steps and a made-up fallback results table. Use volunteers only with consent."""),
 dict(title="Jobs: find the error", label="CHECK", bullets=[
      "Claim: \"The WEF says AI will destroy **92 million** jobs by 2030.\"",
      "Report (2025): **170M** jobs created, **92M** displaced, net **+78M**",
      "What is wrong with the claim? What does \"net\" hide?"],
      notes="""
ACTIVITY (2 min). Expected answers: (1) 92M is displacement, not the net change; the same report projects 170M new jobs, net +78M (2025-2030). (2) The figures cover several drivers, not only AI. (3) "Net" hides real hardship: the displaced workers are not automatically the people who get the new jobs, so retraining matters.
Source: WEF Future of Jobs Report 2025 (more than 1,000 employers, 14 million workers, 55 economies). This corrects the "91 million" figure in an earlier draft of the module."""),
 dict(kind="table", title="Three more risks, three real cases", label="EXPLAIN",
      rows=[["Risk", "Case"], ["Privacy", "Clearview AI fined €30.5M by the Dutch regulator (2024)"],
            ["Deepfake fraud", "Arup staff tricked by a deepfake video call: HK$200M (~US$25M), 2024"],
            ["Environment", "IEA: data-center electricity to ~945 TWh by 2030 (more than double)"]],
      widths=[3.4, 8.7], size=24,
      notes="""
RISKS (2 min). Clearview AI scraped billions of face images from the internet to build a face-recognition database. Arup (Hong Kong, January 2024): an employee joined a video call where every other participant was a deepfake. IEA (April 2025): data-center electricity use projected to more than double to about 945 TWh by 2030, more than Japan uses today.
Full case analysis method (7 steps: describe, stakeholders, benefits, harms, evidence, safeguards, judgment): Mission 10 Activity 10.3; Topic 08."""),
 dict(kind="section", title="Limits and myths", sub=["Why AI makes things up, and what it is not"]),
 dict(title="Why chatbots hallucinate", label="EXPLAIN", bullets=[
      "An LLM predicts **likely** text, not checked facts",
      "Rare facts → plausible inventions (names, dates, citations)",
      "Training often rewards a confident guess over \"I don't know\"",
      "It is not lying: there is no intent"],
      notes="""
HALLUCINATION (2 min). Link to Part 2's next-token loop. Kalai et al. (2025) argue that training and benchmarks reward guessing. Mitigations: grounding the model in retrieved documents (RAG), and checking sources yourself.
This explains the opening case: the fake citations looked exactly like real ones."""),
 dict(title="Spot the hallucinations", label="TRY IT", bullets=[
      "A chatbot says:",
      "1. \"ELIZA was created by Alan Turing in 1956.\"",
      "2. \"ChatGPT was released in November 2022.\"",
      "3. \"Deep Blue learned chess from millions of games.\"",
      "Which claims are false? Use Part 2."],
      notes="""
ACTIVITY (2 min). 60 seconds, neighbors. Answer next slide."""),
 dict(title="The four-step check", label="DEBRIEF", bullets=[
      "False: ELIZA = **Weizenbaum, 1966** · Deep Blue = **search**",
      "True: ChatGPT, 30 November 2022",
      "**1** Split into claims → **2** Prioritize risky ones",
      "**3** Verify independently → **4** Decide or rewrite"],
      notes="""
DEBRIEF (2 min). The four-step routine from Topic 09. Emphasize step 3: check against an independent, reliable source, not by asking the same chatbot.
Practice: Mission 11 Activity 11.2 (with a supplied fact box); test bank Q97-Q105."""),
 dict(kind="table", title="Myth or fact?", label="EXPLAIN",
      rows=[["Myth", "Better statement"], ["AI is alive or conscious", "no evidence; it imitates human-like text"],
            ["AI is always objective", "it learns biases in its data"],
            ["AI will take all jobs", "it changes tasks; jobs are both lost and created"],
            ["Confident means correct", "fluent output can be false"]],
      widths=[5.2, 6.9], size=24,
      notes="""
MISCONCEPTIONS (2 min). Six misconceptions in Topic 09; four shown here. The other two: "AI understands like humans" (debated; judge systems by reliability, not by how human they sound) and "more data always fixes it" (the right data and the right target matter).
Pixel's line from Mission 11: "I said it confidently, so it must be true!" Dr. Ada: "Confidence is a tone of voice, not evidence." """),
 dict(kind="section", title="The rules", sub=["The EU AI Act and the AGI debate"]),
 dict(kind="table", title="EU AI Act: four risk tiers", label="EXPLAIN",
      rows=[["Tier", "Meaning", "Example"], ["Unacceptable", "banned", "social scoring"],
            ["High", "strict duties", "hiring, credit, exam scoring"],
            ["Transparency", "must tell people", "chatbots, deepfake labels"], ["Minimal", "no new duties", "spam filters, games"]],
      widths=[3.3, 3.8, 5.0],
      notes="""
EU AI ACT (3 min). Regulation (EU) 2024/1689, in force 1 August 2024; applies to anyone placing or using AI in the EU. It is risk-based: the stricter the risk, the stricter the rules. There are separate rules for general-purpose AI models. Fines up to EUR 35M or 7% of worldwide turnover for banned practices.
Banned practices include social scoring, emotion recognition in workplaces and schools, and untargeted scraping of faces to build databases.
Other frameworks: OECD AI Principles (2019, updated 2024) and UNESCO Recommendation on the Ethics of AI (2021) are non-binding; the Council of Europe Framework Convention (2024) is the first legally binding international AI treaty."""),
 dict(title="Which tier?", label="PREDICT", bullets=[
      "A. Emotion recognition used in a school classroom", "B. CV-screening tool for hiring",
      "C. Customer-service chatbot", "D. Email spam filter"],
      notes="ACTIVITY (2 min). Neighbors classify each (60 s). Ask for a show of fingers 1-4 for each system (1 = unacceptable ... 4 = minimal). Answer on next slide."),
 dict(kind="table", title="Tiers and dates", label="DEBRIEF",
      rows=[["System", "Tier", "Rules apply from"], ["A. School emotion recognition", "unacceptable", "2 Feb 2025"],
            ["B. CV screening", "high", "2 Dec 2027"], ["C. Chatbot", "transparency", "2 Aug 2026"],
            ["D. Spam filter", "minimal", "no new duties"]],
      widths=[5.2, 3.3, 3.6],
      caption="High-risk dates changed in 2026: re-check before teaching",
      notes="""
DEBRIEF (2 min). Timeline (Topic 10): bans and AI-literacy duty from 2 Feb 2025; general-purpose AI model rules from 2 Aug 2025; general application including transparency from 2 Aug 2026; high-risk rules for stand-alone uses such as hiring, credit and education from 2 Dec 2027 (originally 2 Aug 2026) and for AI built into regulated products such as medical devices from 2 Aug 2028 (originally 2 Aug 2027).
UNCERTAINTY: the 2026 Digital Omnibus amendment is very recent (political agreement May 2026, in force 27 July 2026 per the Commission). Check the official EU pages before each teaching period.
Practice: Mission 12 Activities 12.1-12.2; test bank Q106-Q115."""),
 dict(title="AGI: what do experts actually say?", label="EXPLAIN", bullets=[
      "No agreed definition, no agreed test",
      "Mainstream view: today's LLMs are **not** AGI (debated)",
      "2023 survey of 2,778 researchers: 50% chance by 2047 machines beat humans at every task",
      "Huge disagreement: treat dates as opinions, not facts"],
      notes="""
AGI (3 min). Survey: Grace et al. (published 2024): 10% chance by 2027 and 50% by 2047 that unaided machines outperform humans at every task; 13 years earlier than the previous survey; wide spread of answers. Google DeepMind's "Levels of AGI" (Morris et al., 2023) rated 2023 chatbots as "Emerging AGI" on its own scale, showing that definitions change the answer.
Four viewpoints to present fairly: AGI is coming soon; current methods are not enough; prepare now for serious risks; focus on today's harms first.
Link to Part 2's hype pattern: predictions about AI have often been wrong in both directions."""),
 dict(title="Back to the courtroom", label="TAKEAWAY", bullets=[
      "The **human user** stayed responsible for checking",
      "Makers and deployers carry duties too: that is what the rules add",
      "The chatbot did what LLMs do: produce **likely**, not **true**, text",
      "Your job: match trust to stakes, and verify"],
      notes="""
CONCLUSION (3 min). Resolve the opening: the court held the lawyers responsible; AI does not remove human accountability. The EU AI Act adds duties for providers and deployers, such as transparency for chatbots.
Pull the three sessions together: (1) machine learning learns patterns from data and must be tested on new data; (2) generative AI predicts likely tokens, so it can hallucinate; (3) the same learning from data can copy bias, so we analyze stakes, test by group and keep humans in charge."""),
 dict(title="Your AI-literacy checklist", label="TAKEAWAY", bullets=[
      "**Verify** important claims with independent sources",
      "**Match trust to stakes**: more checking when errors hurt",
      "**Protect privacy**: think before you upload",
      "**Disclose** when you used AI; watch for deepfakes"],
      notes="""
FINAL TAKEAWAY (1 min). From Topic 10's AI-literacy checklist (also: ask governance questions; keep learning). Invite the audience to pick one habit to start this week."""),
 dict(title="Next steps", label="NEXT STEPS", bullets=[
      "Study guide: **Missions 09–12** + the final capstone",
      "Practice: test bank **Q79–Q115**",
      "Capstone: review the fictional product \"MarkMate\"",
      "Whole series: missions 01–12 · 115 practice questions"],
      notes="""
NEXT STEPS (1 min). Files (relative to result/task-3/):
- ../task-2/study-guide/mission-09-ai-in-the-wild.md, mission-10-the-fairness-files.md, mission-11-myth-busters.md, mission-12-tomorrows-rulebook.md (ends with the capstone, model answer and rubric)
- ../task-2/test-bank/test-bank.md (Q79-Q115; answer key at the end)
- Videos V9 (Joy Buolamwini, TED), V11 (Janelle Shane, TED, humorous), V12 (Code.org, privacy and the future of work): ../task-2/study-guide/resources.md
- Video scripts V07-V10: ../task-1/formats/video-scripts/video-scripts.md"""),
]

if __name__ == "__main__":
    for name, slides, fn in ((P1, part1, "part-1-how-machines-learn.pptx"),
                             (P2, part2, "part-2-chatbots-types-history.pptx"),
                             (P3, part3, "part-3-ai-in-the-world.pptx")):
        print(fn, build(name, slides, fn), "slides")
