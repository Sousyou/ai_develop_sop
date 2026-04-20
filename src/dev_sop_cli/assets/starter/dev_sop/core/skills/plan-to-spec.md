# Skill: plan-to-spec

## Purpose
Convert a plan or phase slice into one or more narrow, reviewable task specs.

This skill is the default bridge between planning and implementation.
It keeps implementers from working directly from a broad plan.

## When to use
Use this skill by default when:
- a plan or phase slice is already available
- work is about to move into implementation
- task boundaries, validation, or rule binding are still implicit

See `.dev_sop/core/rules/workflow.md` for when spec creation may be skipped.

## Inputs
- current plan or phase slice
- current phase context
- known constraints
- known risks
- known reusable project facts or starter-owned example cases
- baseline rules under `.dev_sop/core/rules/*`
- current project rules under `.dev_sop/project-rules/*`

## Outputs
- one or more task specs in `.dev_sop/project-specs/*`
- clear in-scope / out-of-scope boundaries
- applicable rules and authoritative references
- approved exceptions, if any
- black-box validation guidance
- project validation gates
- white-box trigger judgment
- write-back guidance

## Workflow

### 1. Start from the current slice
Turn broad plan statements into the next smallest reviewable slice or slices that still move the phase forward.

### 2. One spec, one primary outcome
A spec should produce one primary reviewable outcome.
If a candidate spec mixes design, implementation, migration, cleanup, or unrelated follow-up work, split it.

### 3. Bind the rule set explicitly
List the project rule files that apply to the slice, plus any baseline rule file that materially constrains it.
If the slice needs a rule exception, stop until that exception is approved and recorded.

### 4. Make validation explicit
Every task spec should define how completion is verified, with black-box checks as the default acceptance path plus any project validation gates.

### 5. Decide write-back deliberately
Only mark write-back as needed when the task is expected to clarify stable, reusable context.
If write-back is needed, name the destination.
