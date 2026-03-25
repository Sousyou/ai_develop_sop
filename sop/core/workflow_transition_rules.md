# Workflow Transition Rules

- **Version**: `v2.0`
- **Status**: official definition
- **Role**: defines cross-layer transition constraints

---

## Core Rules

1. only one `current phase` may be active at a time
2. one phase may have only one active `main plan` at a time
3. tasks must return to plan before phase-level decisions continue
4. project-level changes should pass through phase review rather than punch directly into execution
5. parallelism belongs to the execution layer, not to competing project or phase controllers

---

## Default Transition Chain

Forward:

`project -> phase -> main plan -> task`

Return:

`task -> plan -> phase -> project`

---

## Transition Expectations

### Project To Phase

Project defines long-term direction.
Phase turns that direction into the current-stage controller.

### Phase To Plan

Phase defines the stage boundary.
Plan turns that boundary into an execution mainline.

### Plan To Task

Plan defines ordering and execution intent.
Task performs a minimal closed loop.

### Task Back To Plan

Task returns a result, not just a code change.
Plan decides the next execution move.

### Plan Back To Phase

Plan closure or failure returns to phase for current-stage judgment.

### Phase Back To Project

Only cross-phase stable facts or real long-term changes should rise back to project.

---

## Drift Warnings

1. if multiple active phases appear, the decision layer is drifting
2. if multiple active main plans appear, the execution mainline is drifting
3. if tasks keep chaining themselves without returning, execution control is drifting
4. if project changes skip phase review, governance is drifting
