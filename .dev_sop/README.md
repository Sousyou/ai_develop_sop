# Dev SOP Namespace

This directory holds the repository's development SOP assets and recovery/control surface.

Use `.dev_sop/` to keep workflow assets and repo-local control-state artifacts separate from project-facing documentation and product artifacts.
This file is the namespace map for `.dev_sop/*`, not the main project entrypoint.
The human-facing project entrypoint remains the repository root `README.md`.
AI tools should enter through `AGENTS.md` or a tool adapter, then use this file to navigate `.dev_sop/*`.

## Namespace map

- `.dev_sop/VERSION.md`
  Canonical current Dev SOP version and upgrade-use contract.

- `.dev_sop/upgrades/*`
  Version-targeted upgrade notes for copied-project SOP upgrades.

- `.dev_sop/control/*`
  Recovery/control artifacts such as the current state and document routing.

- `.dev_sop/doc/*`
  Durable SOP documents such as guides, templates, task specs, and stable facts.

- `.dev_sop/skill/*`
  Reusable workflow assets that reduce repeated reasoning work.

## Boundary rule

Put content in `.dev_sop/` when it primarily exists to guide AI-assisted planning, execution, validation, write-back, reusable workflow behavior, or repo-local recovery/control state.

Do not put content in `.dev_sop/` when it is primarily project-facing documentation such as:
- product docs
- architecture docs for the shipped system
- ADRs
- runbooks
- user or operator documentation

Those project-facing materials should live outside `.dev_sop/` in the repository structure chosen by the project.
The `.dev_sop/control/*` exception is for the repository's own recovery/control surface rather than shipped-system docs.

## Placement rule

Choose the destination by the question the document answers:

- Put it in `.dev_sop/control/*` when it answers "what is current right now?" or "where should I re-enter?"
- Put it in `.dev_sop/VERSION.md` when it defines the current Dev SOP package version.
- Put it in `.dev_sop/upgrades/*` when it explains how to move from older SOP versions to a newer target version.
- Put it in `.dev_sop/doc/*` when it is a durable reference, guide, template, spec, fact, reusable decision rationale, or reusable experiment outcome worth re-reading later.
- Put it in `.dev_sop/skill/*` when it captures a repeatable workflow that reduces repeated reasoning.
- Put it outside `.dev_sop/` when it documents the shipped system, product behavior, architecture, operations, or other project-facing material.

## Naming convention

The canonical namespace roots are singular by design:
- `.dev_sop/control`
- `.dev_sop/doc`
- `.dev_sop/skill`

Do not create parallel roots such as `.dev_sop/controls`, `.dev_sop/docs`, or `.dev_sop/skills`.

## Use after AI-tool entry

1. Enter through `../AGENTS.md` or a tool adapter such as `../CLAUDE.md`. Codex can use `../AGENTS.md` directly.
2. Read `VERSION.md` when you need the current Dev SOP version or are checking upgrade compatibility.
3. Read `upgrades/README.md` and any relevant `upgrades/*.md` note when upgrading a copied project.
4. If you are handing that upgrade to another AI, use `doc/templates/sop-upgrade-agent-prompt-template.md`.
5. Read `doc/guides/new-project-sop.md` for the default workflow.
6. Read `doc/specs/README.md` before creating or refining specs.
7. Use `skill/plan-to-spec.md` when work is moving from plan to implementation.
8. When preparing a real product release, use `doc/guides/testing-strategy.md` and `doc/templates/release-batch-template.md` for the optional batch-level release check.

## Maintenance rule

- When adding, removing, or renaming fact files under `.dev_sop/doc/facts/`, update `.dev_sop/doc/facts/facts-index.md`.
- When adding, removing, or renaming skills under `.dev_sop/skill/`, update `.dev_sop/skill/skill-registry.md`.
