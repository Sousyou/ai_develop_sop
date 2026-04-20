# Dev SOP Namespace

This directory holds the SOP package for the repository.

The namespace root stays `.dev_sop/`.
The canonical starter surface keeps the cross-project reusable assets that help bootstrap new projects:

- starter-owned baseline rules under `.dev_sop/core/rules/*`
- starter-owned templates under `.dev_sop/core/templates/*`
- starter-owned guides under `.dev_sop/core/guides/*`
- starter-owned examples under `.dev_sop/core/examples/*`
- starter-owned reusable skills under `.dev_sop/core/skills/*`
- project-generated rule, spec, and fact surfaces
- the control surface
- migration notes under `.dev_sop/upgrades/*`

Use this file as the namespace map after entering through `AGENTS.md` or `CLAUDE.md`.

## Namespace Map

- `.dev_sop/core/rules/*`
  Starter-owned baseline rules that ship with the SOP package.

- `.dev_sop/core/templates/*`
  Starter-owned blank templates and prompt scaffolds.

- `.dev_sop/core/guides/*`
  Starter-owned workflow guidance.

- `.dev_sop/core/examples/*`
  Starter-owned filled-in reference artifacts.

- `.dev_sop/core/skills/*`
  Starter-owned reusable workflows.

- `.dev_sop/project-rules/*`
  Project-generated rule files that tighten, specialize, or waive the baseline rules.
  Starter copies may keep only `README.md`, `rule-index.md`, and `exceptions.md` until the project needs more.

- `.dev_sop/control/*`
  Recovery-first current state and document routing.

- `.dev_sop/project-specs/*`
  Project-generated task specs used as the default execution artifact between planning and implementation.

- `.dev_sop/project-facts/*`
  Project-generated stable reusable context.

- `.dev_sop/upgrades/*`
  SOP package upgrade notes.

- `.dev_sop/_backup/*`
  Non-canonical backup storage for repository-local snapshots and project-produced artifacts that should not ship with the starter.
  Do not treat this directory as part of the active SOP contract or default copyable surface.

## Precedence Contract

When documents overlap, use:

`approved exceptions > active task spec > project rules > core rules > entry adapter notes`

Additional routing rules:

- Use `.dev_sop/control/CURRENT.md` for current-state recovery.
- Use `.dev_sop/VERSION.md` and `.dev_sop/upgrades/*` for version and migration questions.
- Use `.dev_sop/project-rules/exceptions.md` when a spec needs an approved exception to a hard rule.

## Placement Rule

Choose the destination by the question the file answers:

- Put it in `.dev_sop/core/*` when it is starter-owned and cross-project reusable.
- Put it in `.dev_sop/_backup/*` when it is repository-local backup or project-produced content that should not remain on the copyable starter surface.
- Put it in `.dev_sop/project-rules/*` when it is a project-generated rule or exception that should stay active in the current project.
- Put it in `.dev_sop/project-specs/*` when it is a real project-generated task spec.
- Put it in `.dev_sop/project-facts/*` when it is a real project-generated fact.
- Put it in `.dev_sop/control/*` when it is part of current-state recovery.
- Put it in `.dev_sop/upgrades/*` when it explains how to move from one SOP package version to another.
- Put it outside `.dev_sop/` when it documents the shipped system, product behavior, architecture, operations, or user-facing material.

## Use After Entry

1. Enter through `../AGENTS.md` for Codex or `../CLAUDE.md` for Claude Code.
2. Read `VERSION.md` when you need the current SOP package contract.
3. Read `core/rules/rule-index.md` for the baseline rules.
4. Read `project-rules/rule-index.md` for the project-generated rule layer.
5. Read `control/CURRENT.md` to recover current state.
6. Read `project-specs/README.md` and `core/templates/task-spec-template.md` before creating or refining specs.
7. Read `project-facts/README.md` before writing back a new project fact.
8. Read `core/guides/*`, `core/examples/*`, or `core/skills/*` when the current slice benefits from them.
9. Ignore `_backup/*` unless you are intentionally recovering repository-local backup material.

## Maintenance Rule

- When adding, removing, or renaming project spec files under `.dev_sop/project-specs/`, update `.dev_sop/project-specs/README.md`.
- When adding, removing, or renaming project fact files under `.dev_sop/project-facts/`, update `.dev_sop/project-facts/README.md`.
- When adding, removing, or renaming project rule files under `.dev_sop/project-rules/`, update `.dev_sop/project-rules/README.md` and `.dev_sop/project-rules/rule-index.md`.
- When adding, removing, or renaming starter-owned reusable skills under `.dev_sop/core/skills/`, update `.dev_sop/core/skills/skill-registry.md`.
- When adding, removing, or renaming starter-owned example files under `.dev_sop/core/examples/`, update the matching example-surface `README.md`.
- If the namespace contract changes, update the root entry docs, `.dev_sop/VERSION.md`, and the matching upgrade note in the same change.
