# Project Specs Surface

Task specs are the default execution artifact between planning and implementation.
That remains true even when longer work is tracked with explicit phases, main plans, or sub-plans.

## Purpose

Use `.dev_sop/project-specs/*` to hold project-generated narrow task specs that:
- bridge plans and implementation
- keep execution reviewable
- bind the current slice to the applicable baseline and project rules
- stay small enough to refine during iteration

This directory is for live or historical real specs produced by the project.
It is not the place for backup references or starter-only examples.

## Starter Contract

In this starter, `.dev_sop/project-specs/` should contain only:

- this `README.md`
- real project-generated specs when the starter repository is being actively used

## Naming

Store each real project-generated spec as:

`.dev_sop/project-specs/YYYYMMDD-NNN-task-slug.md`

- `YYYYMMDD` is the spec creation date
- `NNN` is the same-day sequence, starting at `001`
- choose the next available same-day sequence by scanning existing spec filenames
- never renumber existing specs
- `task-slug` is lowercase kebab-case

## Create Or Refine

- if a plan or phase slice exists, derive one or more specs before editing
- if iterating within the same reviewable slice, refine the existing spec
- if the primary outcome, boundary, or validation path changes, create a new dated spec first
- only tiny task requests that are already effectively spec-complete and trivially narrow may skip spec creation
- treat `trivially narrow` as requiring all of:
  - one primary reviewable outcome
  - obvious and tightly bounded allowed edits
  - obvious lightweight validation
  - no unresolved phase, dependency, or decision boundary
  - no meaningful write-back or closeout ambiguity

## Rule Binding

Every live task spec should name:

- the applicable project rule files under `.dev_sop/project-rules/*`
- any baseline rule files under `.dev_sop/core/rules/*` that materially constrain the slice
- the authoritative references it depends on
- any approved exceptions that relax a hard rule
- the project validation gates that must pass

The active task spec is the highest-precedence execution document after approved exceptions, but it may not silently relax hard rules.
