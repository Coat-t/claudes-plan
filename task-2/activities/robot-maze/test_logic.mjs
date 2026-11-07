// Tests for the maze logic inside robot-maze.html.
// Run with:  node test_logic.mjs      (Node.js 18 or newer, no packages needed)
// The test extracts the code between "BEGIN MAZE LOGIC" and "END MAZE LOGIC" from the HTML file,
// so it tests exactly the code learners run in the browser.
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';

const here = dirname(fileURLToPath(import.meta.url));
const html = readFileSync(join(here, 'robot-maze.html'), 'utf8');
const m = html.match(/\/\* BEGIN MAZE LOGIC \*\/([\s\S]*?)\/\* END MAZE LOGIC \*\//);
assert.ok(m, 'maze logic markers found in HTML');
const sandbox = { module: { exports: {} } };
vm.runInNewContext(m[1], sandbox);
const L = sandbox.module.exports;

let passed = 0;
function test(name, fn) { fn(); passed++; console.log('PASS  ' + name); }
const fmt = (path) => path.map((p) => '(' + p.r + ',' + p.c + ')').join(' ');
// Independent checker: is this a legal route from S to G (adjacent, no walls)?
function legalRoute(mz, path) {
  assert.deepEqual(path[0], mz.start);
  assert.deepEqual(path[path.length - 1], mz.goal);
  for (let i = 1; i < path.length; i++) {
    const a = path[i - 1], b = path[i];
    assert.equal(Math.abs(a.r - b.r) + Math.abs(a.c - b.c), 1, 'one square per move');
    assert.ok(!L.isWall(mz, b.r, b.c), 'never inside a wall');
  }
}
const classic = L.parseMaze(L.MAZES.classic);
const island = L.parseMaze(L.MAZES.island);

test('both mazes are 9x9 with one S and one G', () => {
  for (const mz of [classic, island]) {
    assert.equal(mz.h, 9); assert.equal(mz.w, 9);
    assert.ok(mz.start && mz.goal);
    assert.ok(mz.rows.every((r) => r.length === 9));
  }
});

test('A. wall follower reaches G in Maze 1 (28 moves, not the shortest)', () => {
  const w = L.wallFollower(classic);
  assert.equal(w.outcome, 'goal');
  assert.equal(w.moves, 28);
  legalRoute(classic, w.path);
  console.log('      route: ' + fmt(w.path));
});

test('A. wall follower loops forever in Maze 2 (detected after 25 moves, never reaches G)', () => {
  const w = L.wallFollower(island);
  assert.equal(w.outcome, 'loop');
  assert.equal(w.moves, 25);
  assert.ok(!w.path.some((p) => p.r === island.goal.r && p.c === island.goal.c));
  // Even with a huge move limit it never gets there:
  const long = L.wallFollower(island, 100000);
  assert.notEqual(long.outcome, 'goal');
});

test('B. BFS finds shortest routes: 16 moves (Maze 1, 23 squares explored), 12 moves (Maze 2, 27 explored)', () => {
  const b1 = L.bfs(classic), b2 = L.bfs(island);
  assert.equal(b1.moves, 16); assert.equal(b1.order.length, 23); legalRoute(classic, b1.path);
  assert.equal(b2.moves, 12); assert.equal(b2.order.length, 27); legalRoute(island, b2.path);
  console.log('      Maze 1 route: ' + fmt(b1.path));
  console.log('      Maze 2 route: ' + fmt(b2.path));
});

test('B. BFS really is shortest: brute-force check with an independent distance flood', () => {
  for (const mz of [classic, island]) {
    // Flood fill distances (Dijkstra with unit costs written differently, as a cross-check).
    const dist = new Map([[mz.start.r + ',' + mz.start.c, 0]]);
    let changed = true;
    while (changed) {
      changed = false;
      for (let r = 0; r < mz.h; r++) for (let c = 0; c < mz.w; c++) {
        if (L.isWall(mz, r, c)) continue;
        for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
          const k = (r + dr) + ',' + (c + dc);
          if (dist.has(k) && (!dist.has(r + ',' + c) || dist.get(k) + 1 < dist.get(r + ',' + c))) { dist.set(r + ',' + c, dist.get(k) + 1); changed = true; }
        }
      }
    }
    assert.equal(dist.get(mz.goal.r + ',' + mz.goal.c), L.bfs(mz).moves);
  }
});

test('C. environment rewards: -1 per move, -5 for bumping a wall (stay put), +10 at G', () => {
  const a = L.createAgent(classic);
  const bump = L.envStep(a, classic.start, 0);              // north of S is a wall
  assert.equal(bump.next, classic.start); assert.equal(bump.reward, -5); assert.equal(bump.done, false);
  const move = L.envStep(a, classic.start, 1);              // east is open
  assert.equal(move.reward, -1); assert.equal(move.done, false);
  const g = L.envStep(a, { r: 6, c: 7 }, 2);               // from just above G, move south
  assert.equal(g.reward, 10); assert.equal(g.done, true);
});

test('C. Q-learning (seed 2026): early episodes long, best route not found after 10 episodes', () => {
  for (const [name, mz] of [['Maze 1', classic], ['Maze 2', island]]) {
    const a = L.createAgent(mz);
    for (let i = 0; i < 10; i++) L.runEpisode(a);
    assert.equal(L.greedyRoute(a).reached, false);
    console.log('      ' + name + ' moves in episodes 1-10: ' + a.history.join(', '));
  }
});

test('C. Q-learning learns the shortest route and keeps it from episode 25 to 300 (both mazes)', () => {
  for (const [name, mz, best] of [['Maze 1', classic, 16], ['Maze 2', island, 12]]) {
    const a = L.createAgent(mz);
    let first = null;
    for (let ep = 1; ep <= 300; ep++) {
      L.runEpisode(a);
      const g = L.greedyRoute(a);
      if (g.reached && g.moves === best && first === null) first = ep;
      if (ep >= 25) { assert.ok(g.reached, name + ' episode ' + ep); assert.equal(g.moves, best); legalRoute(mz, g.path); }
    }
    const h = a.history;
    const avg = (xs) => (xs.reduce((s, x) => s + x, 0) / xs.length).toFixed(1);
    assert.ok(Number(avg(h.slice(0, 10))) > 2 * Number(avg(h.slice(-50))), 'episodes get much shorter');
    console.log('      ' + name + ': shortest route (' + best + ' moves) first found after episode ' + first +
      '; average moves per episode: episodes 1-10 = ' + avg(h.slice(0, 10)) + ', episodes 251-300 = ' + avg(h.slice(-50)) +
      ' (still above ' + best + ' because 20% of moves are random exploration)');
  }
});

test('C. same seed gives the same experiment (reset replays identically)', () => {
  const a = L.createAgent(classic), b = L.createAgent(classic);
  for (let i = 0; i < 50; i++) { L.runEpisode(a); L.runEpisode(b); }
  assert.deepEqual(a.history, b.history);
});

test('C. learned table is maze-specific: Maze 1 table does not solve Maze 2', () => {
  const a = L.createAgent(classic);
  for (let i = 0; i < 100; i++) L.runEpisode(a);
  a.maze = island;                                         // same table, different maze
  assert.equal(L.greedyRoute(a).reached, false);
});

console.log('\nAll ' + passed + ' tests passed (Node ' + process.version + ').');
