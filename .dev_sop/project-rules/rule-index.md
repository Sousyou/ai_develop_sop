# Project Rule Index

This file is the authoritative entry for the current project's rule layer.

Read `.dev_sop/core/rules/rule-index.md` first.
Then use this file to list any project-specific deltas that remain in force during active work.
If the current project has no extra local rules beyond baseline defaults, say so here instead of inventing files.

## Start order

1. Read `../core/rules/rule-index.md` for the baseline rules.
2. Read `exceptions.md` for approved waivers and the exception recording format.
3. Read any additional project-local rule files listed below.
4. Read the active task spec in `../project-specs/*.md`.

## Precedence

- `approved exceptions > active task spec > project rules > core rules > entry adapter notes`
- The active task spec may narrow the work inside the current rule set.
- A spec that needs an exception must list it under `Approved Exceptions`.

## Active Project Rules

- No additional project-local rules are required in the starter by default.
- If the current project later needs local engineering, validation, release, or compliance rules, add those files here and list them explicitly in this section.

## Exceptions
- `exceptions.md`
  Approved waivers plus the format for requesting and recording future exceptions.
