# Task Layer Definition

- **Version**: `v2.0`
- **Status**: official definition
- **Layer**: execution layer
- **Role**: defines the smallest controllable execution unit

---

## Purpose

This file answers:

1. what a `task` is
2. what a task must contain to stay controllable
3. how a task closes and returns to plan

---

## Position In The Model

A task is the smallest controllable execution unit under a plan.
It is not a phase, not a plan, and not a review document.

---

## What Task Owns

A task owns:

1. one concrete goal
2. explicit non-goals
3. explicit boundary
4. completion criteria
5. validation method
6. current result summary
7. rollback guidance when needed
8. explicit return-to-plan action

---

## What Task Does Not Own

A task does not own:

1. phase boundary
2. main-plan ordering
3. long-term strategy
4. silent expansion into neighboring work

---

## Closure Rule

A task is not complete merely because code changed.
It closes only when:

1. the concrete goal is addressed
2. validation has run or the missing validation is stated explicitly
3. remaining gaps are stated explicitly
4. the result is returned to the owning plan

---

## Minimum Task Contract

Every task should make the following visible:

- what it is trying to achieve
- what it will not do
- what it may touch
- how completion will be judged
- how validation will be performed
- what happened
- what remains out of scope or unfinished
- how control returns to plan

Use `sop/templates/task_template.md`.

---

## Main Risks

1. tasks without non-goals drift in scope
2. tasks without validation become pseudo-complete
3. tasks without return-flow stay isolated from the mainline
4. tasks without explicit unfinished items hide real gaps

---

## Conclusion

A task is the smallest closed execution loop.
It must keep one goal, one boundary, one validation story, and one clear return path back to the plan.
