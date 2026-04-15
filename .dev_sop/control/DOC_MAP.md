# DOC MAP

This file explains which document answers which question.
It is intentionally short.

## Start order

1. `.dev_sop/control/CURRENT.md` for current status, active slice, next actions, and recovery context.
2. `README.md` for the repository purpose, adoption model, and top-level navigation.
3. `AGENTS.md` for repository-level AI operating rules.
4. `.dev_sop/README.md` for the Dev SOP namespace map.

## Document roles

- `.dev_sop/control/CURRENT.md`
  Current recovery/control state.

- `.dev_sop/doc/specs/*`
  Narrow execution contracts between planning and implementation.

- `.dev_sop/VERSION.md`
  Current Dev SOP version and upgrade contract.

- `.dev_sop/upgrades/*`
  Version-targeted upgrade notes used when upgrading copied-project SOP assets.

- `.dev_sop/doc/facts/*`
  Stable reusable context, including reusable decision rationale or experiment outcomes when they are worth preserving.

- `.dev_sop/skill/*`
  Repeatable workflows that reduce repeated reasoning.

## Priority rule

When documents appear to overlap, choose the layer that matches the question:

1. For current project state, recovery context, and next durable actions, prefer `.dev_sop/control/CURRENT.md`.
2. For task execution scope, validation, allowed edits, and done conditions, prefer the active task spec in `.dev_sop/doc/specs/*`.
3. For SOP version and upgrade questions, prefer `.dev_sop/VERSION.md` and `.dev_sop/upgrades/*`.
4. For repository-wide operating rules and routing boundaries, prefer `README.md`, `AGENTS.md`, and `.dev_sop/README.md`.
5. For stable reusable context, prefer `.dev_sop/doc/facts/*`.
6. For task-local delivery detail, prefer the change summary or handoff notes.
