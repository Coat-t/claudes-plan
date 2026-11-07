// Optional user-interface smoke test for robot-maze.html (simulated browser).
// Needs the "jsdom" package. Example:
//   npm install jsdom            (in any folder, e.g. a temporary one)
//   NODE_PATH=/that/folder/node_modules node test_ui.cjs
// It presses the real buttons in the page and checks what the page shows.
const fs = require('fs');
const path = require('path');
const assert = require('assert/strict');
const { JSDOM } = require('jsdom');

const html = fs.readFileSync(path.join(__dirname, 'robot-maze.html'), 'utf8');
assert.ok(!/<script[^>]+src=/i.test(html), 'no external <script src>');
assert.ok(!/<link[^>]+href=/i.test(html), 'no external <link href>');
assert.ok(!/<img/i.test(html), 'no <img> tags');
assert.ok(!/url\(/i.test(html), 'no CSS url()');
console.log('PASS  page is self-contained (no external resources)');

const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true });
const { document } = dom.window;
const $ = (id) => document.getElementById(id);
const click = (el) => el.dispatchEvent(new dom.window.MouseEvent('click', { bubbles: true }));
const text = (id) => $(id).textContent.replace(/\s+/g, ' ').trim();

assert.equal(document.querySelectorAll('#maze .cell').length, 81);
assert.equal(document.querySelectorAll('#maze .cell.wall').length, 50);  // 31 open squares
console.log('PASS  Maze 1 drawn: 81 squares');

$('instant').checked = true;                 // no animation in the test
click($('btn-rule'));
assert.match(text('status'), /Reached G after 28 moves \(the shortest route is 16 moves\)/);
assert.equal(text('res-rule'), 'Reached G in 28 moves (shortest: 16)');
console.log('PASS  wall follower, Maze 1: ' + text('status'));

click($('btn-bfs'));
assert.match(text('status'), /BFS explored 23 squares .* found a 16-move route/);
assert.equal(document.querySelectorAll('#maze .cell.path').length, 17);
console.log('PASS  BFS, Maze 1: ' + text('res-bfs'));

click($('btn-train10'));
assert.match(text('rl-stats'), /Episodes trained: 10\. Last episode: 42 moves\. Best route so far: not found yet\./);
click($('btn-greedy'));
assert.match(text('status'), /does not yet lead all the way to G/);
console.log('PASS  Q-learning after 10 episodes: ' + text('rl-stats'));
click($('btn-train10'));
click($('btn-train10'));
assert.match(text('rl-stats'), /Episodes trained: 30\..*Best route so far: 16 moves\./);
click($('btn-greedy'));
assert.match(text('status'), /reaches G in 16 moves \(after 30 episodes/);
assert.equal(text('res-rl'), 'After 30 episodes: route of 16 moves');
assert.equal($('chart').children.length, 30);
console.log('PASS  Q-learning after 30 episodes: ' + text('rl-stats'));

click($('btn-arrows'));
assert.equal($('btn-arrows').getAttribute('aria-pressed'), 'true');
const arrows = [...document.querySelectorAll('#maze .cell')].filter((c) => /[←-↓]/.test(c.textContent)).length;
assert.ok(arrows > 10);
console.log('PASS  learned arrows shown in ' + arrows + ' squares');

click($('btn-rlreset'));
assert.match(text('rl-stats'), /Episodes trained: 0/);
click($('btn-train10'));
assert.match(text('rl-stats'), /Last episode: 42 moves/);   // same seed -> same experiment
console.log('PASS  reset replays the same experiment');

const island = document.querySelector('input[value="island"]');
island.checked = true;
island.dispatchEvent(new dom.window.Event('change', { bubbles: true }));
assert.match(text('rl-stats'), /Episodes trained: 0/);
assert.equal(text('res-rule'), 'not run yet');
click($('btn-rule'));
assert.match(text('status'), /Stopped after 25 moves/);
assert.match(text('res-rule'), /Never reaches G/);
console.log('PASS  wall follower, Maze 2: ' + text('res-rule'));
click($('btn-bfs'));
assert.match(text('res-bfs'), /Shortest route: 12 moves \(after exploring 27 squares\)/);
console.log('PASS  BFS, Maze 2: ' + text('res-bfs'));
click($('btn-train100'));
assert.match(text('res-rl'), /After 100 episodes: route of 12 moves/);
console.log('PASS  Q-learning, Maze 2: ' + text('res-rl'));

// Accessibility basics: every button has a visible label; inputs are inside labels.
const buttons = [...document.querySelectorAll('button')];
assert.ok(buttons.every((b) => b.textContent.trim().length > 0));
assert.ok([...document.querySelectorAll('input')].every((i) => i.closest('label')));
console.log('PASS  all ' + buttons.length + ' buttons have labels; all inputs are labelled');

console.log('\nAll UI smoke tests passed (jsdom ' + require('jsdom/package.json').version + ', Node ' + process.version + ').');
