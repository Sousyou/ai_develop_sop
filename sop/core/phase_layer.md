# Phase Layer Definition

- **Version**: `v2.0`
- **Status**: official definition
- **Layer**: decision layer
- **Role**: defines the ownership and control behavior of the `phase` layer

---

## Purpose

This file answers:

1. what the current `phase` owns and does not own
2. how `phase` aligns the current project target with real execution
3. how `phase` controls `main plan`
4. when `phase` should continue, correct, pause, exit, or escalate

---

## Position In The Model

`phase` is the current controller under `project`.
It is the only active decision controller for the current stage.

The default chain is:

`project -> current phase -> current main plan -> task`

There must be only one active current phase at a time.

---

## What Phase Owns

The `phase` layer owns:

1. the current stage goal
2. the current stage non-goals
3. the current stage delivery boundary
4. alignment with `runtime/current_target.md`
5. the active `main plan`
6. `Phase Review`
7. the decision to continue, correct, pause, exit, or escalate
8. the decision to register facts, skill candidates, or SOP candidates upward

---

## What Phase Does Not Own

`phase` does not own:

1. long-term project definition
2. top-level project constraints
3. plan-item ordering details inside a single plan beyond its controller role
4. single-task implementation details

---

## Core Responsibilities

### Stage Definition

A phase must define:

- what this stage is trying to achieve
- what it explicitly will not do
- what counts as delivery within this stage

### Current Target Alignment

`phase` is the place where high-frequency target changes are absorbed and made executable.
If the target changes but remains local, phase should absorb it.
If the change affects long-term direction, raise it upward to `project`.

### Main-Plan Control

A phase may start or accept one active `main plan`.
It does not perform every execution detail itself, but it remains the controller of the mainline.

### Review And Decision

After meaningful plan closure, phase should decide:

- continue in the same phase
- correct the current phase
- pause the phase
- exit the phase
- escalate a project-level change

---

## Main-Plan Rule

A phase may have many candidate ideas, but only one active `main plan`.
If the current mainline breaks, phase must explicitly correct, replace, or pause it instead of letting parallel mainlines silently form.

---

## Phase Review

A `Phase Review` should answer:

1. what was achieved in the current mainline
2. what remains unstable or blocked
3. whether the current phase is still valid
4. whether the phase should continue, change shape, or end
5. whether anything must be written upward or outward

Use `sop/templates/phase_review_template.md`.

---

## Escalation Conditions

Raise upward from `phase` when:

1. long-term project direction changed
2. top-level constraints are now wrong or incomplete
3. repeated plan failure shows a project-level mismatch
4. stable cross-phase facts have formed
5. a candidate skill or SOP upgrade has become clear

---

## Main Risks

1. phase becomes too wide and tries to absorb unrelated large goals
2. phase forgets to define non-goals and scope starts drifting
3. phase allows multiple silent mainlines
4. phase rewrites project definition instead of escalating
5. phase keeps running after its boundary is already invalid

---

## Conclusion

`phase` is the current-stage controller.
It aligns current targets, owns the active mainline, reviews outcomes, and decides whether execution should continue, correct, pause, or rise upward.
