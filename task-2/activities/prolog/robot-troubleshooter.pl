% =====================================================================
%  robot-troubleshooter.pl - Pixel's AI Field Guide (v1.0, 2026-11-06)
%  A tiny EXPERT SYSTEM: Dr. Ada Okafor's rules for diagnosing faults
%  in the Curiosity Lab's robots. All robots and faults are made up.
% =====================================================================
%
%  HOW IT WORKS
%  ------------
%  - FACTS record what the lab assistants OBSERVED (symptoms).
%  - RULES encode the expert's knowledge: "IF these symptoms THEN this fault".
%  - A FALLBACK rule says "no diagnosis" when no rule matches, so Pixel
%    admits it does not know instead of guessing.
%  This is how 1980s "expert systems" worked: knowledge written by hand by
%  human experts, not learned from data.
%
%  SYNTAX REMINDERS
%  ----------------
%  fact.                      something that is true. Ends with a period.
%  head :- cond1, cond2.      rule: head is true IF cond1 AND cond2.
%  lowercase words            atoms (fixed names): pixel, flat_battery
%  Uppercase words            variables (blanks to fill): Robot, Fault
%  \+ Goal                    "NOT provable": true when Prolog CANNOT
%                             prove Goal from the facts and rules.
%                             (Prolog assumes anything it cannot prove is
%                             false. This is called "negation as failure".)
%  _                          anonymous variable: "anything, I don't care what".
% =====================================================================

% ---------------------------------------------------------------------
% FACTS: robot(Name) - the robots in the lab.
% ---------------------------------------------------------------------
robot(pixel).
robot(widget).
robot(sprocket).
robot(gizmo).

% ---------------------------------------------------------------------
% FACTS: symptom(Robot, Symptom) - what the lab assistants observed today.
% ---------------------------------------------------------------------
symptom(pixel, wont_power_on).
symptom(pixel, no_lights).
symptom(widget, drives_in_circles).
symptom(sprocket, bumps_into_walls).
symptom(sprocket, camera_blurry).
symptom(gizmo, squeaks).

% ---------------------------------------------------------------------
% RULES: fault(Robot, Fault) - Dr. Okafor's diagnosis rules.
% Each rule: IF the robot shows these symptoms THEN it probably has Fault.
% ---------------------------------------------------------------------

% No power AND no lights at all -> the battery is flat.
fault(Robot, flat_battery) :-
    symptom(Robot, wont_power_on),
    symptom(Robot, no_lights).

% Lights work but it will not start -> a loose power cable.
fault(Robot, loose_power_cable) :-
    symptom(Robot, wont_power_on),
    symptom(Robot, lights_on).

% Driving in circles -> one wheel is stuck.
fault(Robot, stuck_wheel) :-
    symptom(Robot, drives_in_circles).

% Bumping into walls AND blurry camera -> the camera sensor is dirty.
fault(Robot, dirty_sensor) :-
    symptom(Robot, bumps_into_walls),
    symptom(Robot, camera_blurry).

% ---------------------------------------------------------------------
% FACTS: repair(Fault, Action) - what to do about each fault.
% ---------------------------------------------------------------------
repair(flat_battery, charge_battery).
repair(loose_power_cable, reconnect_cable).
repair(stuck_wheel, clean_wheel_axle).
repair(dirty_sensor, wipe_camera_lens).

% ---------------------------------------------------------------------
% RULES: diagnosis(Robot, Result) - with a FALLBACK.
% Clause 1: if some fault rule matches, the diagnosis is that fault.
% Clause 2 (fallback): if the robot exists but NO fault can be proven,
%           the result is no_diagnosis_ask_dr_okafor.
% ---------------------------------------------------------------------
diagnosis(Robot, Fault) :-
    fault(Robot, Fault).
diagnosis(Robot, no_diagnosis_ask_dr_okafor) :-
    robot(Robot),
    \+ fault(Robot, _).

% advice(Robot, Action): chain two steps - diagnose, then look up the repair.
advice(Robot, Action) :-
    fault(Robot, Fault),
    repair(Fault, Action).

% ---------------------------------------------------------------------
% YOUR TURN (see queries.md, Part D):
%  1. gizmo squeaks and gets "no diagnosis". Add a rule
%       fault(Robot, dry_joints) :- symptom(Robot, squeaks).
%     and a fact  repair(dry_joints, oil_joints).  Put each new line next
%     to the other clauses of the same predicate. Then ask diagnosis(gizmo, D).
%  2. Add the fact  symptom(widget, lights_on).  Does anything change? Why?
% ---------------------------------------------------------------------
