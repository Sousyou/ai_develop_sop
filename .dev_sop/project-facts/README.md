# Project Facts Surface

This directory holds project-generated facts that are stable enough to re-read later.

Use this surface for information that is:
- stable enough to keep
- reusable across tasks
- useful to future readers or future AI runs

Project facts are not an archive of every discussion.

## Boundary

- keep project-generated fact files here
- keep this surface guide at `README.md`
- use natural descriptive filenames inside this directory
- do not create fact files unless the context is stable enough to deserve write-back
- it is valid for this directory to contain only `README.md` until real facts exist

## Current Files
- None yet.

## Routing Rule

Follow `.dev_sop/core/rules/writeback.md`, `.dev_sop/core/rules/rule-index.md`, and `.dev_sop/project-rules/rule-index.md` before adding content here.
There is no standing decision or experiment ledger in this starter.
Route only durable reusable decision rationale or experiment outcomes into project facts.

When a task or plan names a write-back type, use it as a routing hint rather than a reason to create a new file type:

- `facts_update`: stable project context or validation references under `.dev_sop/project-facts/*`
- `rule_update`: durable project-local operating rules under `.dev_sop/project-rules/*`
- `skill_update`: reusable shipped workflow changes under `.dev_sop/core/skills/*`
- `decision_rationale`: only when the decision is stable and reusable; otherwise leave it in task-local artifacts
- `phase_lesson`: only when the lesson should influence later phases or future runs
- `task_pattern`: reusable execution pattern worth preserving, usually in an existing project fact file unless it later justifies a shared skill
- `anti_pattern`: repeated pitfall worth preserving, not one-off frustration
