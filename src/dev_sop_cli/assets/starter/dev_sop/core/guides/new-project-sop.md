# New Project SOP

Use this guide when starting a new project or when introducing this SOP into an existing project.

## First Use In A Copied Project

Use this as the copied-project quickstart:

1. keep the split entrypoints: root `README.md` for humans, `AGENTS.md` for Codex, `CLAUDE.md` for Claude Code, and `.dev_sop/README.md` for the SOP namespace
2. keep the baseline rule layer, the project rule layer, and the control surface
3. define the first reviewable slice in the planning workflow you already use
4. write a durable plan only if the phase or handoff structure is worth re-reading later
5. derive the first narrow task spec before implementation
6. bind that spec to the applicable baseline and project rules plus validation gates
7. validate explicitly and write back only stable reusable context

The starter should stay lightweight on day one.
Do not create every optional artifact up front.

## What To Keep On Day One

The smallest practical copied-project set is:

- `AGENTS.md`
- `CLAUDE.md`
- `.dev_sop/README.md`
- `.dev_sop/VERSION.md`
- `.dev_sop/upgrades/*`
- `.dev_sop/core/rules/*`
- `.dev_sop/core/templates/*`
- `.dev_sop/project-rules/README.md`
- `.dev_sop/project-rules/rule-index.md`
- `.dev_sop/project-rules/exceptions.md`
- `.dev_sop/control/*`
- `.dev_sop/project-specs/README.md`
- `.dev_sop/project-facts/README.md`
- `.dev_sop/core/skills/plan-to-spec.md`
- `.dev_sop/core/skills/design-whitebox-tests.md`

Add `.dev_sop/core/examples/*` only when the copied project wants bundled writing references.

## Rule Setup

At the start of a copied project, establish:

- `.dev_sop/core/rules/rule-index.md` for the baseline rules
- `.dev_sop/control/CURRENT.md` for recovery-first state
- `.dev_sop/control/DOC_MAP.md` for reading order
- `.dev_sop/project-rules/rule-index.md` for the project-generated rule layer
- `.dev_sop/project-rules/exceptions.md` for explicit waivers

Add project-local rule files such as `engineering.md`, `validation.md`, or release/compliance rules only when the copied project actually needs them.

This is where the copied project should express its own operating changes.
Do not spread project-local rule fragments across guides, random facts, or root entry docs.

## Derive Task Specs

Use `.dev_sop/core/skills/plan-to-spec.md`, `.dev_sop/project-specs/README.md`, and `.dev_sop/core/templates/task-spec-template.md`.
Use `.dev_sop/core/examples/specs/*` only as optional reference material.

A task spec should shrink the plan into a narrow implementation contract.
For longer-running work, also use `.dev_sop/core/guides/task-lifecycle-and-escalation.md` so repair, rollback, replan, and escalation stay explicit.

For the first copied-project slice:

- start with one spec, not a batch of specs
- make the first spec small enough to review in one pass
- name the real spec on the `YYYYMMDD-NNN-task-slug.md` pattern
- list the applicable project rules explicitly
- list approved exceptions only when they actually exist

## Validate And Write Back

- use black-box validation by default
- add white-box validation when internal complexity or regression sensitivity demands it
- apply any local gates declared in the active project-rule files
- update `.dev_sop/control/*` only for durable recovery-state changes
- write stable reusable context to `.dev_sop/project-facts/*`
- update `.dev_sop/project-rules/*` when the project's operating contract changes
- update `.dev_sop/core/*` only when the shared SOP package itself changed
