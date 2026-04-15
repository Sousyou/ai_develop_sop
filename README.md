# AI Engineering SOP Starter

A lightweight, tool-neutral SOP starter for AI-assisted engineering.

Use this repository when you want a project to move from planning to narrow execution without losing control of scope, validation, facts, or reusable workflows. It is intentionally not tied to a specific stack, app type, or framework.

## Choose Your Path

- `Small task / narrow change`
  Stay on the default lightweight path when the next slice is already clear and reviewable. Start with the [specs guide](.dev_sop/doc/specs/README.md) and the [task spec template](.dev_sop/doc/templates/task-spec-template.md).

- `Long task / multi-phase / multi-handoff`
  Use the phase-aware variant when the work needs explicit phase, plan, handoff, or failure-boundary structure. Start with the [phase-aware workflow guide](.dev_sop/doc/guides/phase-aware-workflow.md) and the [canonical example](.dev_sop/doc/guides/phase-aware-canonical-example.md).

Both paths still converge on one or more narrow task specs before implementation.

If you are returning to active work in a repository that uses `.dev_sop/control/*`, start with `.dev_sop/control/CURRENT.md` before diving into specs or guides.

## What this repository is for

This starter is for teams that want a practical default workflow for:

1. framing work with a plan
2. deriving one or more narrow task specs
3. implementing the smallest coherent change
4. validating explicitly, with black-box checks by default
5. writing back stable facts
6. promoting repeated workflows into reusable skills

It is suitable for new projects, existing projects, non-web projects, and mixed engineering environments.

## Core workflow

The intended workflow is:

1. create or refine a plan
2. derive one or more narrow task specs in `.dev_sop/doc/specs/`
3. implement narrowly
4. validate explicitly
5. write back stable facts when justified
6. promote repeated workflows into skills when they stabilize

See `AGENTS.md` for the full working model, including when plans should be persisted, when specs may be skipped, and how validation layers work.

The repository's SOP assets and recovery/control surface live under `.dev_sop/`.
This keeps workflow docs, control-state artifacts, templates, facts, specs, and skills separate from project-facing product documentation.
See `.dev_sop/README.md` for the Dev SOP namespace map and boundary rules.

When a repository uses `.dev_sop/control/*`, its recovery/control layer lives there.
Start with `.dev_sop/control/CURRENT.md` when you need to recover the current phase, active slice, next actions, or the current source of truth.

## Dev SOP Control Surface

When a repository uses `.dev_sop/control/*`, use it as the minimal recovery/control surface for people returning to the work.

- `.dev_sop/control/CURRENT.md`
  Recovery-first current state.

- `.dev_sop/control/DOC_MAP.md`
  Short explanation of which document answers which question.

Use `.dev_sop/control/*` for recovery and control.
Use `.dev_sop/doc/*` and `.dev_sop/skill/*` for durable execution assets and reusable workflows.

## Entrypoints

This repository intentionally uses split entrypoints:

- `README.md`
  Human-facing and project-facing entrypoint.

- `.dev_sop/control/CURRENT.md`
  Recovery-first entry for the current project state when the repository uses `.dev_sop/control/*`.

- `AGENTS.md` and adapter files such as `CLAUDE.md`
  AI-tool entrypoints.
  Codex reads `AGENTS.md` directly, so no separate Codex adapter is required.

- `.dev_sop/README.md`
  Namespace map for Dev SOP workflow assets after entering through the AI-tool guidance.

- `.dev_sop/VERSION.md`
  Canonical current Dev SOP version and upgrade-use contract.

- `.dev_sop/upgrades/*`
  Version-targeted upgrade notes for copied-project SOP upgrades.

## Repository roles

- `README.md`
  Human-facing entry point and adoption guide for this starter.

- `AGENTS.md`
  Canonical AI-tool operating rules for the repository.

- `CLAUDE.md`
  Lightweight AI-tool adapter that points back to `AGENTS.md`.

- `.dev_sop/README.md`
  Namespace map for Dev SOP workflow assets, boundaries, and navigation.

- `.dev_sop/VERSION.md`
  Canonical current Dev SOP version for this starter or a copied project.

- `.dev_sop/upgrades/*`
  Versioned SOP upgrade notes used when moving copied projects between Dev SOP versions.

- `.dev_sop/control/*`
  Recovery/control artifacts for current state and document routing.

- `.cursor/rules/*`
  Execution guardrails for Cursor.

- `.dev_sop/doc/guides/*`
  Practical workflow guidance for adopting and using the SOP.

- `.dev_sop/doc/templates/*`
  Reusable working artifacts such as plans, task specs, change summaries, and prompt scaffolds for multi-model handoff.

- `.dev_sop/doc/specs/*`
  Task specs used as the default execution artifact between plan and implementation.

- `.dev_sop/doc/facts/*`
  Stable reusable context, not an archive of task chatter.

- `.dev_sop/skill/*`
  Lightweight reusable workflow capabilities.

## Adopting this starter

Use this repository in one of two ways:

### Maintain the SOP starter itself
In this repository, `README.md` explains the SOP system.

### Copy it into a real project
Copy the relevant files into the project, initialize the facts and templates you actually need, and keep the operating rules in `AGENTS.md`, `.cursor/rules/*`, `.dev_sop/doc/*`, and `.dev_sop/skill/*`.

After copying, let `README.md` become the project's human-facing README.
Keep `AGENTS.md` plus any tool adapters as the AI-tool entrypoints.
Keep `.dev_sop/README.md` as the namespace map for Dev SOP workflow assets.
Keep `.dev_sop/VERSION.md` and `.dev_sop/upgrades/*` so future SOP upgrades can be applied deliberately.
Keep project-facing docs outside `.dev_sop/` so the namespace remains reserved for workflow and control artifacts rather than product docs.
When the copied project uses `.dev_sop/control/*`, use it as the recovery layer, with `.dev_sop/control/CURRENT.md` as the first file to read when returning to the project.

## Minimal adoption path

The smallest practical starting point is:

1. keep `AGENTS.md`
2. keep `.dev_sop/README.md`
3. keep `.dev_sop/VERSION.md`
4. keep `.dev_sop/upgrades/*`
5. keep `.cursor/rules/*`
6. keep `.dev_sop/doc/templates/*`
7. keep `.dev_sop/doc/specs/README.md`
8. keep `.dev_sop/doc/facts/facts-index.md`
9. keep the two initial skills: `.dev_sop/skill/plan-to-spec.md` and `.dev_sop/skill/design-whitebox-tests.md`
10. create a first plan in your planning workflow, then initialize `.dev_sop/doc/facts/project-scope.md` when stable scope is clear

That list is the bare minimum.
If you also want the recommended recovery-first control surface, keep:

- `.dev_sop/control/*`
- `.dev_sop/doc/templates/current-template.md`
- `.dev_sop/doc/templates/doc-map-template.md`
- `.dev_sop/skill/session-closeout.md`

If you want the guided first-use path to remain available after copying, also keep:

- `.dev_sop/doc/guides/new-project-sop.md`
- `.dev_sop/doc/guides/testing-strategy.md`
- `.dev_sop/doc/guides/task-lifecycle-and-escalation.md`
- `.dev_sop/doc/templates/release-batch-template.md` when the project will prepare real product releases and wants a lightweight batch-level release check
- `.dev_sop/doc/specs/20260104-001-example-first-copied-project-quickstart.md` when you want the small-task example
- `.dev_sop/doc/guides/phase-aware-workflow.md` when long-task guidance is needed
- `.dev_sop/doc/guides/phase-aware-canonical-example.md`, `.dev_sop/doc/guides/phase-aware-example-main-plan.md`, `.dev_sop/doc/guides/phase-aware-example-sub-plan.md`, and `.dev_sop/doc/specs/20260103-001-example-adoption-entrypoint-slice.md` when you want the closed long-task example

## Copy Into A Real Project In 10 Minutes

1. Copy the minimal adoption set into the real project. If you want this guided walkthrough to remain available inside the copied project, also copy the guided first-use files listed above. Keep the split entrypoints: root `README.md` for humans, `AGENTS.md` for AI tools, and `.dev_sop/README.md` for the `.dev_sop/*` namespace.
  If you want a recovery-first control surface, copy `.dev_sop/control/*` together with `.dev_sop/doc/templates/current-template.md`, `.dev_sop/doc/templates/doc-map-template.md`, and `.dev_sop/skill/session-closeout.md`, then start with `.dev_sop/control/CURRENT.md`.
  If you are upgrading an existing copied-project SOP instead of adopting fresh, compare `.dev_sop/VERSION.md` and apply `.dev_sop/upgrades/*.md` in ascending version order.
2. Decide whether the first slice is a `small task / narrow change` or a `long task / multi-phase / multi-handoff`.
3. Clarify the first reviewable slice in your normal planning workflow.
4. Persist a written plan only if the phase, handoff, or checkpoint structure is worth re-reading later. Otherwise move directly to the first spec.
5. Derive the first task spec with the [specs guide](.dev_sop/doc/specs/README.md) and the [task spec template](.dev_sop/doc/templates/task-spec-template.md).
6. Implement from the spec, validate explicitly, and write back only stable reusable context.

If you want the copied-project walkthrough, read the [new-project SOP guide](.dev_sop/doc/guides/new-project-sop.md).
If you want a copyable small-task reference, read [20260104-001-example-first-copied-project-quickstart.md](.dev_sop/doc/specs/20260104-001-example-first-copied-project-quickstart.md).
If you want a copyable example of the control-surface closeout loop, read [20260328-003-example-project-control-closeout-loop.md](.dev_sop/doc/specs/20260328-003-example-project-control-closeout-loop.md).
Then create the first real project spec from `.dev_sop/doc/templates/task-spec-template.md`.

## What this repository is not

This repository is not:

- a fixed web stack starter
- a product application
- a heavy process framework
- a documentation portal
- a requirement to write large documents before coding
- an archive for all historical discussion

## Where to look next

1. if the repository uses `.dev_sop/control/*` and you need the current project state, read `.dev_sop/control/CURRENT.md`
2. read `AGENTS.md`
3. if you are wiring Dev SOP workflow assets, read `.dev_sop/README.md`
4. read `.dev_sop/VERSION.md` when you need the current SOP version or upgrade contract
5. for a first copied-project run, read `.dev_sop/doc/guides/new-project-sop.md`
6. for the default lightweight path, read `.dev_sop/doc/specs/README.md`
7. for the phase-aware long-task path, read `.dev_sop/doc/guides/phase-aware-workflow.md` and `.dev_sop/doc/guides/phase-aware-canonical-example.md`
8. create or refine a first plan, using `.dev_sop/doc/templates/plan-template.md` only when you want a durable written plan
9. initialize `.dev_sop/doc/facts/project-scope.md` when stable scope is clear

When design, planning, and execution are split across different tools or roles, also see `.dev_sop/doc/guides/design-to-spec-handoff.md` and the prompt scaffolds in `.dev_sop/doc/templates/design-to-planner-prompt-template.md` and `.dev_sop/doc/templates/spec-to-executor-prompt-template.md`.

## Versioning

- current Dev SOP version: see `.dev_sop/VERSION.md`
- SOP upgrade notes: see `.dev_sop/upgrades/*`
- AI handoff template for copied-project SOP upgrades: see `.dev_sop/doc/templates/sop-upgrade-agent-prompt-template.md`
- copied projects should compare their local `.dev_sop/VERSION.md` against the source starter before applying SOP upgrades

---
