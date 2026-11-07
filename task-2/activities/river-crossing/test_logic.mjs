// Tests for the game logic inside river-crossing.html.
// Run with:  node test_logic.mjs      (Node.js 18 or newer, no packages needed)
// The test extracts the code between "BEGIN GAME LOGIC" and "END GAME LOGIC" from the HTML file,
// so it tests exactly the code learners run in the browser.
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';

const here = dirname(fileURLToPath(import.meta.url));
const html = readFileSync(join(here, 'river-crossing.html'), 'utf8');
const m = html.match(/\/\* BEGIN GAME LOGIC \*\/([\s\S]*?)\/\* END GAME LOGIC \*\//);
assert.ok(m, 'game logic markers found in HTML');
const sandbox = { module: { exports: {} } };
vm.runInNewContext(m[1], sandbox);
const L = sandbox.module.exports;

let passed = 0;
function test(name, fn) { fn(); passed++; console.log('PASS  ' + name); }

test('start state is (FWGC | -) and is not the goal', () => {
  const s = L.startState();
  assert.equal(L.notation(s), '(FWGC | -)');
  assert.equal(L.isGoal(s), false);
  assert.equal(L.notation(L.goalState()), '(- | FWGC)');
});

test('exactly 10 of the 16 placements are valid', () => {
  assert.equal(L.allStates().length, 16);
  const valid = L.validStates().map(L.notation).sort();
  console.log('      valid states: ' + valid.join(' '));
  assert.equal(valid.length, 10);
});

test('all 10 valid states are reachable from the start (graph search)', () => {
  const seen = new Set([L.stateKey(L.startState())]);
  const queue = [L.startState()];
  while (queue.length) {
    const s = queue.shift();
    for (const n of L.neighbours(s)) {
      const k = L.stateKey(n.next);
      if (!seen.has(k)) { seen.add(k); queue.push(n.next); }
    }
  }
  assert.equal(seen.size, 10);
});

test('invalid first moves are rejected with an explanation', () => {
  const s = L.startState();
  const alone = L.tryMove(s, null);
  assert.equal(alone.ok, false);
  assert.match(alone.reason, /wolf eats the goat because the farmer left them alone on the left bank/);
  assert.match(alone.reason, /goat eats the cabbage/);
  const wolf = L.tryMove(s, 'W');
  assert.equal(wolf.ok, false);
  assert.match(wolf.reason, /goat eats the cabbage because the farmer left them alone on the left bank/);
  const cabbage = L.tryMove(s, 'C');
  assert.equal(cabbage.ok, false);
  assert.match(cabbage.reason, /wolf eats the goat because the farmer left them alone on the left bank/);
  const goat = L.tryMove(s, 'G');
  assert.equal(goat.ok, true);
  assert.equal(L.notation(goat.next), '(WC | FG)');
  console.log('      example message: ' + wolf.reason);
});

test('farmer cannot take an item from the other bank', () => {
  const s = L.fromKey('RRRL'); // (C | FWG): farmer right, cabbage left
  const r = L.tryMove(s, 'C');
  assert.equal(r.ok, false);
  assert.match(r.reason, /farmer can only take something from his own side/);
});

test('a later tempting move is rejected: leaving wolf and goat on the right bank', () => {
  const s = L.fromKey('RRRL'); // (C | FWG)
  const r = L.tryMove(s, null);
  assert.equal(r.ok, false);
  assert.match(r.reason, /wolf eats the goat because the farmer left them alone on the right bank/);
});

test('BFS finds a 7-crossing plan that really works', () => {
  const steps = L.bfsTrace(L.startState());
  const last = steps[steps.length - 1];
  assert.equal(last.found, true);
  const plan = L.planFromPath(last.path);
  console.log('      BFS steps (states taken from frontier): ' + steps.length + ', visited: ' + last.visited.length);
  plan.forEach((p, i) => console.log('      ' + (i + 1) + '. ' + p));
  assert.equal(plan.length, 7);
  // Replay the path with tryMove to make sure every crossing is legal.
  let s = L.startState();
  for (let i = 1; i < last.path.length; i++) {
    const r = L.tryMove(s, last.path[i].passenger);
    assert.equal(r.ok, true);
    assert.equal(L.stateKey(r.next), last.path[i].key);
    s = r.next;
  }
  assert.equal(L.isGoal(s), true);
  assert.equal(last.visited.length, 10);
});

test('BFS first step: from start only the goat crossing is new', () => {
  const steps = L.bfsTrace(L.startState());
  assert.deepEqual(Array.from(steps[0].added, k => L.notation(L.fromKey(k))), ['(WC | FG)']); // Array.from: the array comes from another JS realm
  assert.equal(steps[0].rejected.length, 3);
});

console.log(`\nAll ${passed} tests passed (Node ${process.version}).`);
