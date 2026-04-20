# DOC MAP

This file explains which document answers which question.
Keep it short and role-based.

## Start order

1. `.dev_sop/control/CURRENT.md` for the current state and recovery path.
2. `.dev_sop/core/rules/rule-index.md` for the starter-owned baseline rules.
3. `.dev_sop/project-rules/rule-index.md` for any active project-local rule layer.
4. `AGENTS.md` for Codex or `CLAUDE.md` for Claude Code.
5. the active task spec in `.dev_sop/project-specs/*.md` for execution scope.
6. `.dev_sop/VERSION.md` and `.dev_sop/upgrades/*` when the question is about SOP contract or migration.

## Document roles

- `.dev_sop/core/*`
  Starter-owned baseline rules, templates, examples, guides, and reusable skills.

- `.dev_sop/project-rules/*`
  Project-generated rules, waivers, and local constraints.
  A newly copied project may keep only `rule-index.md` and `exceptions.md` until it needs more local rules.

- `.dev_sop/control/*`
  Recovery-first current state and document routing.

- `.dev_sop/project-specs/*`
  Project-generated execution contracts between planning and implementation.

- `.dev_sop/project-facts/*`
  Project-generated stable reusable context.

- `.dev_sop/upgrades/*`
  Version-targeted SOP upgrade notes.

- `.dev_sop/_backup/*`
  Backup storage for repository-local snapshots or project-produced files that should not ship with the starter.

## Priority rule

When documents overlap, use:

1. approved exceptions recorded in `.dev_sop/project-rules/exceptions.md`
2. the active task spec in `.dev_sop/project-specs/*.md` for task scope, allowed edits, done conditions, and task validation
3. `.dev_sop/project-rules/*` for project rules
4. `.dev_sop/core/rules/*` for baseline rules
5. `AGENTS.md` or `CLAUDE.md` for tool-entry behavior
6. `.dev_sop/core/*` for starter-owned reusable templates, guides, examples, and skills
7. `.dev_sop/VERSION.md` and `.dev_sop/upgrades/*` for version and migration questions
