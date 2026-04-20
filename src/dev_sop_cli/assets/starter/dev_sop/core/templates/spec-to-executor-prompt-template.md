# Spec To Executor Prompt Template

Use this template to hand a single task spec to an executor.
This is a prompt scaffold, not a durable project document.

## Input

### Target Spec Path
Which single spec should be executed?

### Applicable Project Rules
Which project rule files under `.dev_sop/project-rules/*` and which baseline rule files under `.dev_sop/core/rules/*` must remain in force during execution?

### Approved Exceptions
Which approved exception IDs, if any, may the executor rely on?

### Allowed Scope
What work inside the spec is allowed?

### Forbidden Scope
What must remain out of scope for this execution pass?

### Validation Expectations
What validation is required before this work can be reported as done?

### Escalation Expectations
When should the executor return `needs_decision` or `replan_required` instead of continuing?

### Completion Reporting Format
How should the executor report completed work, validation, blockers, escalation outcomes, and follow-ups?

## Execution Contract

The executor should:
- consume one spec at a time
- stay inside the current spec boundary
- follow the listed project rules, baseline rules, and approved exceptions
- validate against the spec before reporting completion
- make the spec's write-back and closeout decision explicit before reporting `done`
- return blockers, ambiguity, scope pressure, and escalation outcomes to the planner / specifier

The executor should not:
- re-open the high-level design
- merge multiple specs into one execution pass
- rewrite `Goal`, `In Scope`, `Out of Scope`, `Done When`, `Validation`, or `Write-back Needed`
- invent a project-rule exception that is not already approved

The executor may update only:
- `Status`
- `Task Checklist`
- `Risks / Notes`
