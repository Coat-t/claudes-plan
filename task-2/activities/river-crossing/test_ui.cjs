// Optional user-interface smoke test for river-crossing.html (simulated browser).
// Needs the "jsdom" package. Example:
//   npm install jsdom            (in any folder, e.g. a temporary one)
//   NODE_PATH=/that/folder/node_modules node test_ui.cjs
// It presses the real buttons in the page and checks what the page shows.
const fs = require('fs');
const path = require('path');
const assert = require('assert/strict');
const { JSDOM } = require('jsdom');

const html = fs.readFileSync(path.join(__dirname, 'river-crossing.html'), 'utf8');

// 1. Self-contained check: no external scripts, stylesheets, images or fonts.
assert.ok(!/<script[^>]+src=/i.test(html), 'no external <script src>');
assert.ok(!/<link[^>]+href=/i.test(html), 'no external <link href>');
assert.ok(!/<img/i.test(html), 'no <img> tags');
assert.ok(!/url\(/i.test(html), 'no CSS url()');
console.log('PASS  page is self-contained (no external resources)');

const dom = new JSDOM(html, { runScripts: 'dangerously' });
const { document } = dom.window;
const $ = (id) => document.getElementById(id);
const click = (el) => el.dispatchEvent(new dom.window.MouseEvent('click', { bubbles: true }));
const itemBtn = (letter) => [...document.querySelectorAll('.item')].find((b) => b.dataset.item === letter);

assert.match($('state-line').textContent, /\(FWGC \| -\)/);
console.log('PASS  start state shown: ' + $('state-line').textContent.trim());

// Invalid move: take the wolf first.
click(itemBtn('W'));
click($('row-btn'));
assert.match($('message').textContent, /goat eats the cabbage because the farmer left them alone on the left bank/);
assert.equal($('log').children.length, 0);
console.log('PASS  invalid move rejected: ' + $('message').textContent);

// Play the 7-crossing solution by pressing buttons.
const plan = ['G', null, 'W', 'G', 'C', null, 'G'];
// first take the wolf back out of the boat
click(itemBtn('W'));
for (const p of plan) {
  if (p) click(itemBtn(p));
  click($('row-btn'));
}
assert.equal($('log').children.length, 7);
assert.match($('state-line').textContent, /\(- \| FWGC\)/);
assert.match($('message').textContent, /Mission complete in 7 crossings/);
console.log('PASS  solution played through the buttons; log:');
[...$('log').children].forEach((li, i) => console.log('      ' + (i + 1) + '. ' + li.textContent));

// Undo
click($('undo-btn'));
assert.equal($('log').children.length, 6);
assert.match($('state-line').textContent, /\(FG \| WC\)/);
console.log('PASS  undo returns to ' + $('state-line').textContent.trim());

// Item on the wrong bank
click(itemBtn('C')); // cabbage is on the right, farmer is on the left
assert.match($('message').textContent, /farmer can only take something from his own side/);
console.log('PASS  wrong-bank item explained');

// State space toggle
click($('space-btn'));
assert.equal($('space-panel').hidden, false);
assert.equal($('space-btn').getAttribute('aria-expanded'), 'true');
assert.equal($('space-grid').children.length, 16);
assert.equal(document.querySelectorAll('.st.invalid').length, 6);
console.log('PASS  state space: ' + $('space-summary').textContent);

// Reset
click($('reset-btn'));
assert.equal($('log').children.length, 0);
assert.match($('state-line').textContent, /\(FWGC \| -\)/);
console.log('PASS  reset');

// Watch Pixel search
click($('bfs-step'));
assert.match($('bfs-box').textContent, /Step 1 of 10/);
assert.match($('bfs-box').textContent, /\(WC \| FG\)/);
click($('bfs-all'));
assert.match($('bfs-plan').textContent, /Pixel's plan: 7 crossings/);
assert.equal($('bfs-plan').querySelectorAll('li').length, 7);
assert.equal($('bfs-step').disabled, true);
console.log('PASS  BFS replay reaches the goal with a 7-crossing plan');

// Accessibility basics: every button has visible text or an aria-label.
const unlabeled = [...document.querySelectorAll('button')].filter((b) => !(b.textContent.trim() || b.getAttribute('aria-label')));
assert.equal(unlabeled.length, 0);
console.log('PASS  all ' + document.querySelectorAll('button').length + ' buttons have labels');
console.log('\nAll UI smoke tests passed (jsdom ' + require('jsdom/package.json').version + ', Node ' + process.version + ').');
