# Project Layer Definition

- **Version**: `v2.0`
- **Status**: official definition
- **Layer**: decision layer
- **Role**: defines the ownership, structure, and governance boundary of the `project` layer

---

## Purpose

This file answers:

1. what the `project` layer owns and does not own
2. how AI keeps alignment with long-term goals instead of being dragged by local tasks
3. when a change must rise to `project`
4. which information belongs to `project` versus `current_target`

---

## Position In The Model

The full model is:

- decision layer: `project -> phase`
- execution layer: `plan -> task`

Within that model:

- `project` is the highest, lowest-frequency authority
- `phase` is the current controller under `project`
- `plan` and `task` execute under the current phase

The job of `project` is not to schedule work. Its job is to preserve:

- `project_charter`
- long-term boundary
- top-level constraints
- cross-phase stable facts
- a single entry for project-level adjustment

---

## What Project Owns

The `project` layer owns five categories:

1. long-term stable `project_charter`
2. long-term do / do-not-do boundary
3. top-level constraints and tradeoff preferences
4. cross-phase stable project facts
5. project-level adjustment intake when local execution no longer matches the real direction

---

## What Project Does Not Own

The `project` layer does not own:

1. current phase delivery details
2. current plan ordering
3. single-task implementation details
4. temporary execution notes or one-off experiments
5. high-frequency current goals and current validation targets

Those belong to `phase`, `plan`, `task`, or `runtime/current_target.md`.

---

## Core Information Categories

### `project_charter`

Answers:

- what the product is trying to become in the long run
- who it serves and what problem it solves
- what success looks like at a high level
- what major route the project is taking

### Long-Term Boundary

Answers:

- what the project is meant to do
- what it is explicitly not meant to do
- which directions are outside the long-term product scope

### Top-Level Constraints

Answers:

- what tradeoffs matter most
- how conflicting options should be cut down
- which top-level priorities stay valid across phases

### Cross-Phase Facts

Answers:

- which capabilities are already stable enough to count as baseline
- which directions were tried and proven not viable
- which external constraints are confirmed to exist
- which facts will keep affecting later decisions across multiple phases

### What Is Not Project

The following should normally not be recorded as `project` content:

- current phase goals
- current round validation targets
- current temporary in-scope and out-of-scope
- short-term urgency changes

Those belong to `current_target` and `phase`.

---

## Single-Entry Rule

The `project` layer must follow a single-entry rule:

1. it must have one authoritative primary entry
2. other documents may reference or summarize it, but should not redefine it in parallel
3. if documents conflict, the `project` primary entry wins

This rule prevents high-level project meaning from fragmenting across README, ad-hoc notes, facts, and conversation.

---

## Adjustment Triggers

AI should not rewrite the `project` layer casually.
But AI should explicitly raise a project-level adjustment proposal when any of these happen:

1. the user changes long-term product direction or long-term constraints
2. the change affects multiple phases, not just the current phase
3. current execution repeatedly conflicts with top-level goals or boundaries
4. multiple plans are drifting because top-level judgment is missing
5. the change has clearly moved beyond `current_target`

AI may propose project-level adjustment.
AI should not silently rewrite formal project definition without confirmation.

---

## Main Risks

1. if `project` is too abstract, it becomes useless for real decisions
2. if `project` changes too often, downstream phases and plans lose stability
3. if multiple documents redefine project meaning, AI judgment becomes inconsistent
4. if execution details leak into `project`, it invades `phase` and `plan`
5. if every note is promoted into project facts, the layer collapses into a project log

---

## Conclusion

The `project` layer is the highest judgment layer, not the execution scheduler.
It exists to keep long-term direction, long-term boundary, top-level constraints, and cross-phase facts stable enough that downstream execution does not forget what the project is actually trying to become.
