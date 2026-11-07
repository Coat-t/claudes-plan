"""
Pixel's AI Field Guide - River-crossing solver (Version 1.0, 2026-11-06)

What this does
--------------
Solves the farmer-wolf-goat-cabbage puzzle with BREADTH-FIRST SEARCH (BFS)
and prints every step: which state Pixel looks at, which crossings are
rejected and why, the FRONTIER (queue of states still to look at) and the
VISITED set (states already found). Then it lists ALL shortest solutions.

Run it:   python3 solver.py        (Python 3.8+, standard library only)

Notation: a state is written (left bank | right bank), e.g. (WC | FG)
means wolf and cabbage on the left; farmer and goat on the right.
"-" means an empty bank.
"""
from collections import deque

ITEMS = "FWGC"                      # Farmer, Wolf, Goat, Cabbage
NAMES = {"F": "farmer", "W": "wolf", "G": "goat", "C": "cabbage"}
PASSENGERS = [None, "W", "G", "C"]  # None = farmer rows alone
START = "LLLL"                      # one letter per item: L = left bank, R = right bank
GOAL = "RRRR"


def notation(state):
    """Turn 'LLRL' into '(FWC | G)'."""
    left = "".join(i for i, side in zip(ITEMS, state) if side == "L") or "-"
    right = "".join(i for i, side in zip(ITEMS, state) if side == "R") or "-"
    return f"({left} | {right})"


def dangers(state):
    """Return a list of problems in this state (empty list = safe)."""
    f, w, g, c = state
    bank = {"L": "left", "R": "right"}
    problems = []
    if w == g and f != w:
        problems.append(f"wolf eats goat on the {bank[w]} bank")
    if g == c and f != g:
        problems.append(f"goat eats cabbage on the {bank[g]} bank")
    return problems


def try_move(state, passenger):
    """Return (new_state, None) if the crossing is allowed, else (None, reason)."""
    s = dict(zip(ITEMS, state))
    if passenger and s[passenger] != s["F"]:
        return None, f"{NAMES[passenger]} is not on the farmer's bank"
    other = "R" if s["F"] == "L" else "L"
    s["F"] = other
    if passenger:
        s[passenger] = other
    new_state = "".join(s[i] for i in ITEMS)
    problems = dangers(new_state)
    if problems:
        return None, f"{notation(new_state)} invalid: " + " and ".join(problems)
    return new_state, None


def describe(state, passenger):
    to = "right" if state[0] == "L" else "left"
    who = f"takes the {NAMES[passenger]}" if passenger else "crosses alone"
    return f"Farmer {who} to the {to} bank"


def show(states):
    return "  ".join(notation(s) for s in states) if states else "(empty)"


def bfs_with_trace():
    """Plain BFS with a visited set, printing a trace. Returns the first plan found."""
    frontier = deque([START])
    visited = [START]
    parent = {START: None}
    step = 0
    print("BREADTH-FIRST SEARCH TRACE")
    print("==========================")
    print(f"Start: frontier = {show(frontier)}   visited = {show(visited)}\n")
    while frontier:
        state = frontier.popleft()
        step += 1
        print(f"Step {step}: take {notation(state)} from the front of the frontier")
        if state == GOAL:
            print("  -> This is the GOAL. Search stops.\n")
            break
        for p in PASSENGERS:
            new_state, reason = try_move(state, p)
            label = f"with the {NAMES[p]}" if p else "alone"
            if new_state is None:
                print(f"  farmer {label:16} rejected ({reason})")
            elif new_state in parent:
                print(f"  farmer {label:16} skipped  ({notation(new_state)} already visited)")
            else:
                print(f"  farmer {label:16} NEW      {notation(new_state)} -> added to back of frontier")
                parent[new_state] = (state, p)
                visited.append(new_state)
                frontier.append(new_state)
        print(f"  frontier = {show(frontier)}")
        print(f"  visited  = {show(visited)}  ({len(visited)} states)\n")
    # Rebuild the path by following parent links back from the goal.
    path, s = [], GOAL
    while parent[s] is not None:
        prev, p = parent[s]
        path.append((prev, p, s))
        s = prev
    return list(reversed(path)), len(visited)


def all_shortest_plans():
    """Find EVERY shortest plan: BFS by layers, remembering all parents one layer up."""
    depth = {START: 0}
    parents = {START: []}
    layer = [START]
    while layer and GOAL not in depth:
        next_layer = []
        for state in layer:
            for p in PASSENGERS:
                new_state, _ = try_move(state, p)
                if new_state is None:
                    continue
                if new_state not in depth:
                    depth[new_state] = depth[state] + 1
                    parents[new_state] = []
                    next_layer.append(new_state)
                if depth[new_state] == depth[state] + 1:
                    parents[new_state].append((state, p))
        layer = next_layer

    def paths_to(s):
        if s == START:
            return [[]]
        return [path + [(prev, p, s)] for prev, p in parents[s] for path in paths_to(prev)]

    return paths_to(GOAL)


def print_plan(plan):
    for n, (before, p, after) in enumerate(plan, 1):
        print(f"  {n}. {describe(before, p):42} {notation(before)} -> {notation(after)}")


if __name__ == "__main__":
    all_states = [f + w + g + c for f in "LR" for w in "LR" for g in "LR" for c in "LR"]
    valid = [s for s in all_states if not dangers(s)]
    print(f"There are {len(all_states)} possible placements; {len(valid)} are valid (safe):")
    print("  " + show(valid) + "\n")

    plan, n_visited = bfs_with_trace()
    print(f"Plan found by BFS ({len(plan)} crossings, {n_visited} states visited):")
    print_plan(plan)

    plans = all_shortest_plans()
    print(f"\nALL SHORTEST SOLUTIONS: {len(plans)} plans, each with {len(plans[0])} crossings")
    for k, pl in enumerate(plans, 1):
        print(f"Solution {k}:")
        print_plan(pl)
