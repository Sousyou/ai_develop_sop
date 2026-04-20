# Example: Dev SOP Control Closeout Loop

> **This is an example spec** showing how a narrow task can update the minimal control surface without turning it into a project board.
> It is not a real task in this repository.

## Metadata

### Source Plan / Request
Copied-project example request: show one complete loop from current project state to a task spec to a stable control-surface update.

### Status
`done`

### Related Specs
- `20260104-001-example-first-copied-project-quickstart.md`

## Goal
Show how a team can start from `.dev_sop/control/CURRENT.md`, execute one narrow spec, and then update only the durable control artifacts that changed.

## In Scope
- read `.dev_sop/control/CURRENT.md` first to recover the active slice
- implement one narrow reviewable task from a dated spec
- update `.dev_sop/control/CURRENT.md` when the active slice changes
- route durable reusable decision rationale to facts only if the task froze a project-level choice

## Out of Scope
- writing a work log into `.dev_sop/control/CURRENT.md`
- copying task-local reasoning into facts
- creating a standing decision ledger for every implementation choice
- adding reports or archives

## Affected Area
- `.dev_sop/control/CURRENT.md`
- the active task spec in `.dev_sop/project-specs/*.md`
- optional `.dev_sop/project-facts/*`

## Task Checklist
- [x] recover the current state from `.dev_sop/control/CURRENT.md`
- [x] execute one narrow task from a dated spec
- [x] update `.dev_sop/control/CURRENT.md` only for durable state changes
- [x] route durable reusable decision rationale only when a project-level choice was frozen

## Done When
A returning reader can follow the path `.dev_sop/control/CURRENT.md` -> active task spec -> control-surface update and see how the minimal control surface stays current without becoming a second execution system.

## Validation

### Black-box Checks
- confirm the example starts from `.dev_sop/control/CURRENT.md` rather than a chat transcript or raw task list
- confirm the example keeps execution details in the spec rather than moving them into `.dev_sop/control/*`
- confirm the example updates only durable control-surface artifacts after the slice completes

### White-box Needed
No

### White-box Trigger
This is a usage example.

### Internal Logic To Protect
None.

## Write-back Needed
Yes

If yes, what stable information should be written back, where does it belong, and which type best fits?
- `.dev_sop/control/CURRENT.md` for active-slice and next-step changes
- `.dev_sop/project-facts/*` with `decision_rationale` only if the task froze a durable project-level choice and the rationale is reusable

## Risks / Notes
- The main risk is treating `.dev_sop/control/CURRENT.md` like a task log instead of a recovery artifact.
- If the example needs reports, archives, or ledgers to make sense, the slice is no longer minimal.
