// Runs every query listed in queries.md against the .pl files in this folder,
// using TWO Prolog engines:
//   1. SWI-Prolog compiled to WebAssembly (npm package "swipl-wasm") - the same
//      Prolog system that powers SWISH, so answer order and "false." endings match.
//   2. Tau Prolog (npm package "tau-prolog") - a separate JavaScript Prolog, as a cross-check.
// Usage (packages installed in some folder, e.g. a temporary one):
//   npm install swipl-wasm tau-prolog
//   NODE_PATH=/that/folder/node_modules node test_queries.cjs > test-output.txt
const fs = require('fs');
const path = require('path');

const here = __dirname;
const read = (f) => fs.readFileSync(path.join(here, f), 'utf8');

// Insert extra lines directly after the last line that starts with `after`
// (keeps clauses of the same predicate together, as queries.md tells learners to do).
function addAfter(src, after, lines) {
  const arr = src.split('\n');
  let idx = -1;
  arr.forEach((l, i) => { if (l.startsWith(after)) idx = i; });
  if (idx < 0) throw new Error('anchor not found: ' + after);
  arr.splice(idx + 1, 0, ...lines);
  return arr.join('\n');
}

const family = read('family.pl');
const robot = read('robot-troubleshooter.pl');
const bug = read('find-the-bug.pl');
const familyC1 = addAfter(family, 'ancestor(X, Y) :- parent(X, Z)', ['grandmother(X, Z) :- grandparent(X, Z), female(X).']);
const familyC2 = addAfter(addAfter(family, 'parent(tunde, kemi).', ['parent(kemi, tayo).']), 'male(leo).', ['male(tayo).']);
const robotD1 = addAfter(addAfter(robot, '    symptom(Robot, camera_blurry).', ['', 'fault(Robot, dry_joints) :- symptom(Robot, squeaks).']),
  'repair(dirty_sensor', ['repair(dry_joints, oil_joints).']);
const robotD2 = addAfter(robot, 'symptom(gizmo, squeaks).', ['symptom(widget, lights_on).']);
const bugFixed = bug.replace('sibling(X, Y) :- parent(P, X), parent(P, Y).', 'sibling(X, Y) :- parent(P, X), parent(P, Y), X \\= Y.')
  .replace('female(x).', 'female(X).');

const cases = [
  ['A1', 'family.pl', family, 'parent(grace, ada).'],
  ['A2', 'family.pl', family, 'parent(ada, Child).'],
  ['A3', 'family.pl', family, 'parent(Who, ada).'],
  ['A4', 'family.pl', family, 'male(ada).'],
  ['B1', 'family.pl', family, 'father(F, ada).'],
  ['B2', 'family.pl', family, 'mother(M, zara).'],
  ['B3', 'family.pl', family, 'father(F, zara).'],
  ['B4', 'family.pl', family, 'grandparent(G, zara).'],
  ['B5', 'family.pl', family, 'grandparent(grace, GC).'],
  ['B6', 'family.pl', family, 'sibling(ada, S).'],
  ['B7', 'family.pl', family, 'sibling(zara, S).'],
  ['B8', 'family.pl', family, 'sibling(kemi, S).'],
  ['B9', 'family.pl', family, 'ancestor(A, kemi).'],
  ['B10', 'family.pl', family, 'ancestor(grace, D).'],
  ['B11', 'family.pl', family, 'father(X, Y).'],
  ['B12', 'family.pl', family, 'setof(S, sibling(ada, S), Siblings).'],
  ['C1', 'family.pl + grandmother rule', familyC1, 'grandmother(G, leo).'],
  ['C2', 'family.pl + parent(kemi, tayo), male(tayo)', familyC2, 'ancestor(A, tayo).'],
  ['D1', 'robot-troubleshooter.pl', robot, 'symptom(pixel, S).'],
  ['D2', 'robot-troubleshooter.pl', robot, 'fault(pixel, F).'],
  ['D3', 'robot-troubleshooter.pl', robot, 'fault(R, stuck_wheel).'],
  ['D4', 'robot-troubleshooter.pl', robot, 'diagnosis(gizmo, D).'],
  ['D5', 'robot-troubleshooter.pl', robot, 'diagnosis(R, D).'],
  ['D6', 'robot-troubleshooter.pl', robot, 'advice(sprocket, A).'],
  ['D7', 'robot-troubleshooter.pl + dry_joints rule', robotD1, 'diagnosis(gizmo, D).'],
  ['D8', 'robot-troubleshooter.pl + dry_joints rule', robotD1, 'advice(gizmo, A).'],
  ['D9', 'robot-troubleshooter.pl + symptom(widget, lights_on)', robotD2, 'fault(widget, F).'],
  ['E1', 'find-the-bug.pl (buggy)', bug, 'sibling(zara, S).'],
  ['E2', 'find-the-bug.pl (buggy)', bug, 'mother(M, zara).'],
  ['E3', 'find-the-bug.pl (fixed)', bugFixed, 'sibling(zara, S).'],
  ['E4', 'find-the-bug.pl (fixed)', bugFixed, 'mother(M, zara).'],
];

// Prolog driver that prints answers the way the swipl terminal toplevel does:
//   X = a ;      (more answers may follow)
//   X = b.       (last answer, no choice points left)
//   false.       (no (more) answers)
const DRIVER = `
show_bindings([]) :- write(true).
show_bindings([B|Bs]) :- show_b(B), ( Bs == [] -> true ; write(','), nl, show_bindings(Bs) ).
show_b(N = V) :- format("~w = ~q", [N, V]).
run_query(M, S) :-
    term_string(G, S, [variable_names(Bs0)]),
    exclude([N=_]>>sub_atom(N, 0, 1, _, '_'), Bs0, Bs),
    (   call_cleanup(M:G, Det = true),
        exclude([_=V]>>var(V), Bs, Shown),   % like the swipl toplevel: hide still-unbound variables
        show_bindings(Shown),
        (   Det == true -> write('.'), nl, !
        ;   write(' ;'), nl, fail
        )
    ;   write('false.'), nl
    ).
`;

async function runSwipl() {
  const SWIPL = require('swipl-wasm');
  const results = {};
  let out = '';
  const swipl = await SWIPL({ arguments: ['-q'], print: (t) => { out += t + '\n'; }, printErr: (t) => { out += '[stderr] ' + t + '\n'; } });
  const version = swipl.prolog.query('current_prolog_flag(version, V).').once().V;
  swipl.FS.writeFile('/driver.pl', DRIVER);
  swipl.prolog.query("consult('/driver.pl').").once();
  let n = 0;
  for (const [id, , src, q] of cases) {
    const mod = 'm' + (n++);
    const file = '/' + mod + '.pl';
    swipl.FS.writeFile(file, ':- module(' + mod + ', []).\n' + src);
    out = '';
    swipl.prolog.query('consult(' + JSON.stringify(file).replace(/"/g, "'") + ').').once();
    const loadMsgs = out;
    out = '';
    swipl.prolog.query('run_query(' + mod + ', ' + JSON.stringify(q) + ').').once();
    swipl.prolog.query('flush_output.').once();
    results[id] = { load: loadMsgs.trim(), answer: out.trimEnd() };
  }
  return { version, results };
}

async function runTau() {
  const pl = require('tau-prolog');
  require('tau-prolog/modules/lists')(pl);
  const results = {};
  for (const [id, , src, q] of cases) {
    const session = pl.create(10000);
    const lines = [];
    await new Promise((resolve) => {
      session.consult(src, {
        success: () => {
          session.query(q, {
            success: () => {
              const next = () => session.answer({
                success: (ans) => { lines.push(session.format_answer(ans)); next(); },
                fail: () => { lines.push('false.'); resolve(); },
                error: (err) => { lines.push('ERROR ' + session.format_answer(err)); resolve(); },
                limit: () => { lines.push('LIMIT'); resolve(); },
              });
              next();
            },
            error: (err) => { lines.push('QUERY ERROR ' + session.format_answer(err)); resolve(); },
          });
        },
        error: (err) => { lines.push('CONSULT ERROR ' + session.format_answer(err)); resolve(); },
      });
    });
    results[id] = lines.join(' ; ');
  }
  return { version: require('tau-prolog/package.json').version, results };
}

(async () => {
  const swi = await runSwipl();
  const tau = await runTau();
  const v = swi.version;
  console.log('Prolog query test run, ' + new Date().toISOString().slice(0, 10));
  console.log('Engine 1: SWI-Prolog ' + Math.floor(v / 10000) + '.' + Math.floor((v % 10000) / 100) + '.' + (v % 100) +
    ' via swipl-wasm ' + require('swipl-wasm/package.json').version);
  console.log('Engine 2: Tau Prolog ' + tau.version);
  console.log('Node ' + process.version + '\n');
  for (const [id, prog, , q] of cases) {
    console.log('[' + id + '] program: ' + prog);
    console.log('?- ' + q);
    if (swi.results[id].load) console.log('(load messages) ' + swi.results[id].load);
    console.log(swi.results[id].answer);
    console.log('  Tau Prolog answers: ' + tau.results[id]);
    console.log('');
  }
})();
