# Skill: session-closeout

## Purpose
Close out a completed slice without turning the control surface, facts, or skills into an archive of task chatter.

This skill keeps the recovery/control surface current while preserving the existing `.dev_sop/*` execution model.
Use it after required validation and before reporting a task or slice as fully done when the repository uses `.dev_sop/control/*`.

## When to use
Use this skill when a task or slice is finishing and you need to decide what, if anything, should be updated after validation.

Typical triggers:
- the active slice changed or completed
- the current phase or current target shifted
- a project-level decision was frozen
- an experiment produced a readable result worth re-reading later
- stable reusable context emerged and may belong in facts or a skill

## Inputs
- current task spec or completed slice
- current `.dev_sop/control/CURRENT.md`
- any new decision or experiment outcome
- any candidate fact or reusable workflow learning

## Outputs
- updated `.dev_sop/control/CURRENT.md` when current operating state changed
- updated `.dev_sop/control/DOC_MAP.md` only when document roles or reading order changed
- a fact update when durable reusable decision rationale or experiment outcomes should be preserved
- a skill update only when the information is a repeatable workflow
- no write-back when nothing durable changed

## Workflow

### 1. Start with the control surface
Ask whether a returning human would be misled if `.dev_sop/control/CURRENT.md` stayed unchanged.
If yes, update it.
If no, leave it alone.

Update `.dev_sop/control/CURRENT.md` only when at least one of these changed:
- current phase
- current target
- active slice
- current source of truth
- frozen decision in force
- next durable actions
- top risk that could make the control surface misleading

Do not update `.dev_sop/control/CURRENT.md` for:
- step-by-step task progress
- validation logs
- implementation notes that already live in the spec
- file inventories or commit-style changelogs

Update `.dev_sop/control/DOC_MAP.md` only when at least one of these changed:
- normal start order for a returning reader
- which document family answers which question
- the priority rule when documents overlap

Do not update `.dev_sop/control/DOC_MAP.md` just because:
- a new spec was created
- a durable decision was made
- an experiment ran
- more files now live in the repository

### 2. Separate project-level decisions from task choices
When a choice changes the project's durable direction, scope boundary, control model, or repeatable operating rule, decide whether the rationale is reusable enough for facts.
If yes, route it to `.dev_sop/doc/facts/*`.
If no, keep it in the active spec or change summary.

### 3. Record experiments only when they are real experiments
If the work included explicit experiment setup, results, and a next decision worth re-reading later, decide whether the takeaway is reusable enough for facts.
If yes, route it to `.dev_sop/doc/facts/*`.
If no, keep it in the active spec or change summary.
Do not treat ordinary validation runs as reusable experiments.

### 4. Route stable reusable context deliberately
If the outcome is stable reusable context, route it to `.dev_sop/doc/facts/*`.
If the outcome is a repeatable workflow, route it to `.dev_sop/skill/*`.
Do not use the control surface as a substitute for facts or skills.

### 5. Prefer no write-back over noisy write-back
If the outcome is task-local, temporary, or obvious from the active spec, leave it out of `.dev_sop/control/*`, facts, and skills.

## Common failure modes
- updating `.dev_sop/control/CURRENT.md` like a running task log
- creating a shadow decision ledger instead of routing reusable rationale deliberately
- storing ordinary validation runs as reusable experiments
- writing task-local reasoning into facts
- promoting one-off tactics into a skill
- updating multiple layers with the same explanation instead of routing it once
