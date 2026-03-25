# Plan Layer Definition

- **Version**: `v2.0`
- **Status**: official definition
- **Layer**: execution layer
- **Role**: defines the orchestration behavior of the `plan` layer

---

## Purpose

This file answers:

1. what a `plan` owns and does not own
2. how `main plan` and `sub plan` relate
3. how external plans are accepted
4. how plan state controls execution order and return flow

---

## Position In The Model

`plan` is the execution orchestration layer under the current `phase`.
It does not define long-term direction or phase boundary.
It arranges execution inside the current stage.

---

## What Plan Owns

The `plan` layer owns:

1. the active `main plan`
2. plan-item ordering and state
3. acceptance and review of external plans
4. plan-level reordering and replanning
5. creation of `sub plan` when useful
6. collecting task return flow and deciding the next execution step

---

## What Plan Does Not Own

The `plan` layer does not own:

1. long-term project goals
2. phase boundary definition
3. single-task implementation details

---

## External-Plan Preference

The default mode is `external_plan_preferred`.
That means:

1. if a useful external plan exists, review it first
2. trim, patch, and adapt it before generating a new plan
3. generate a new plan only when the external plan is missing or insufficient

This rule exists to reduce token cost and match real collaborative workflows.

---

## Main Plan And Sub Plan

### Main Plan

The active primary execution line under the current phase.
There may be only one active `main plan`.

### Sub Plan

A bounded local execution branch created only when it helps control complexity.
A sub plan must still return to the main plan and must not silently become a second mainline.

---

## Plan Item Expectations

A plan item should be:

1. ordered
2. stateful
3. bounded enough to produce one or more tasks
4. able to return clear progress or blockage back to the plan

Use `sop/templates/plan_item_template.md` when needed.

---

## Return-Flow Rule

After a task closes, the result must return to the owning plan.
The plan then decides whether to:

1. mark the plan item complete
2. schedule a follow-up task
3. reorder the plan
4. create a sub plan
5. escalate to phase review or correction

---

## Main Risks

1. plan tries to redefine phase boundary
2. plan becomes a task log instead of an execution controller
3. external plans are ignored even when good enough
4. sub plans become silent competing mainlines
5. tasks do not return to plan, so execution fragments

---

## Conclusion

`plan` is the execution orchestrator.
It accepts or shapes the mainline, prefers external plans when possible, controls ordering and state, and absorbs task return flow into the next execution decision.
