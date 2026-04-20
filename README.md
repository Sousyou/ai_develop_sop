# AI Engineering SOP Starter

A reusable SOP starter for AI-assisted engineering with `Codex` and `Claude Code` as the mainline entry surfaces.

This repository is meant to be copied into real projects.
The starter distinguishes between:

- starter-owned cross-project reusable assets under `.dev_sop/core/*`
- project-generated rule/spec/fact surfaces under `.dev_sop/project-*`
- the control surface under `.dev_sop/control/*`
- upgrade notes under `.dev_sop/upgrades/*`

The only material that belongs in `.dev_sop/_backup/*` is repository-local backup or project-produced content that should not ship as part of the starter surface.

## Starter Surface

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.dev_sop/README.md`
- `.dev_sop/VERSION.md`
- `.dev_sop/control/CURRENT.md`
- `.dev_sop/control/DOC_MAP.md`
- `.dev_sop/core/rules/*`
- `.dev_sop/core/templates/*`
- `.dev_sop/core/guides/*`
- `.dev_sop/core/examples/*`
- `.dev_sop/core/skills/*`
- `.dev_sop/project-rules/README.md`
- `.dev_sop/project-rules/rule-index.md`
- `.dev_sop/project-rules/exceptions.md`
- `.dev_sop/project-specs/README.md`
- `.dev_sop/project-facts/README.md`
- `.dev_sop/upgrades/*`

## Active Surfaces

- `.dev_sop/core/rules/*`
  Starter-owned baseline operating rules.

- `.dev_sop/core/templates/*`
  Starter-owned reusable templates.

- `.dev_sop/core/guides/*`
  Starter-owned workflow guidance.

- `.dev_sop/core/examples/*`
  Starter-owned reference examples.

- `.dev_sop/core/skills/*`
  Starter-owned reusable workflows.

- `.dev_sop/project-rules/*`
  The project rule surface.
  Add project-local rules here only when the copied project actually needs them.

- `.dev_sop/project-specs/*`
  The project spec surface.
  This should contain only `README.md` until real specs exist.

- `.dev_sop/project-facts/*`
  The project fact surface.
  This should contain only `README.md` until real facts exist.

- `.dev_sop/control/*`
  Recovery-first current state and document routing.

- `.dev_sop/upgrades/*`
  SOP package upgrade notes.

- `.dev_sop/_backup/*`
  Non-canonical backup storage for repository-local snapshots and project-produced artifacts removed from the starter surface.
  Do not treat this directory as part of the copyable starter package.

## Default Flow

1. Start from a plan, a phase slice, or a clearly scoped task request.
2. Derive one or more narrow task specs in `.dev_sop/project-specs/`.
3. Implement the smallest coherent change.
4. Validate explicitly.
5. Write back only stable reusable context.
6. Update core assets only when the shared SOP package itself changed.

## Where To Start

- If you are returning to active work, read `.dev_sop/control/CURRENT.md`.
- If you are entering from Codex, read `AGENTS.md`.
- If you are entering from Claude Code, read `CLAUDE.md`.
- If you need the full namespace map, read `.dev_sop/README.md`.
- If you need baseline rules, read `.dev_sop/core/rules/rule-index.md`.
- If you need reusable templates, guides, examples, or skills, read `.dev_sop/core/*`.
- If you need the current SOP package contract or upgrade path, read `.dev_sop/VERSION.md` and `.dev_sop/upgrades/*`.
- Ignore `.dev_sop/_backup/*` unless you are intentionally recovering repository-local backup material.

## Canonical Structure

- `README.md`
  Human-facing project entrypoint.

- `AGENTS.md`
  Codex entry adapter.

- `CLAUDE.md`
  Claude Code entry adapter.

- `.dev_sop/README.md`
  Namespace map and layer boundaries.

- `.dev_sop/VERSION.md`
  Current SOP package contract.

- `.dev_sop/core/rules/*`
  Starter-owned baseline rules.

- `.dev_sop/core/templates/*`
  Starter-owned templates.

- `.dev_sop/core/guides/*`
  Starter-owned guides.

- `.dev_sop/core/examples/*`
  Starter-owned examples.

- `.dev_sop/core/skills/*`
  Starter-owned reusable workflows.

- `.dev_sop/project-rules/*`
  Project-generated rule files.

- `.dev_sop/control/*`
  Recovery-first current state and document routing.

- `.dev_sop/project-specs/*`
  Project-generated task specs.

- `.dev_sop/project-facts/*`
  Project-generated stable facts.

- `.dev_sop/upgrades/*`
  Version-targeted SOP upgrade notes.

- `.dev_sop/_backup/*`
  Repository-local backup storage, not part of the copyable starter surface.

## Copy Into A Real Project

Keep the split entrypoints:

- root `README.md` for humans
- `AGENTS.md` for Codex
- `CLAUDE.md` for Claude Code
- `.dev_sop/README.md` for the SOP namespace

By default, copy the full starter surface and omit `.dev_sop/_backup/*`.

For a lean adoption set, keep at minimum:

1. `AGENTS.md`
2. `CLAUDE.md`
3. `.dev_sop/README.md`
4. `.dev_sop/VERSION.md`
5. `.dev_sop/upgrades/*`
6. `.dev_sop/core/rules/*`
7. `.dev_sop/core/templates/task-spec-template.md`
8. `.dev_sop/project-rules/README.md`
9. `.dev_sop/project-rules/rule-index.md`
10. `.dev_sop/project-rules/exceptions.md`
11. `.dev_sop/control/*`
12. `.dev_sop/project-specs/README.md`
13. `.dev_sop/project-facts/README.md`

The rest of `.dev_sop/core/*` remains cross-project useful starter content and is safe to keep when the copied project wants the fuller package.

## Current Mainline

- The mainline entry surfaces are `Codex` and `Claude Code` via the root adapters only.
- Cross-project reusable templates, guides, examples, and skills stay on the mainline starter surface.
- Legacy adapter migrations are documented only in `.dev_sop/upgrades/*`.
- `_backup` content is intentionally non-canonical.

## Versioning

- Current SOP package contract: `.dev_sop/VERSION.md`
- Upgrade notes: `.dev_sop/upgrades/*`
- Upgrade prompt scaffold: `.dev_sop/core/templates/sop-upgrade-agent-prompt-template.md`
