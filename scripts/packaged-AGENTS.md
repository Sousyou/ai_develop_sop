# AGENTS.md

This repository uses `AGENTS.md` as the Codex entry adapter for the Dev SOP.

## Codex Reading Order

1. Read `.dev_sop/README.md` for the namespace map and layer boundaries.
2. Read `.dev_sop/core/rules/rule-index.md` for the starter-owned baseline rules.
3. Read `.dev_sop/project-rules/rule-index.md` for the project-generated rule layer.
4. Read `.dev_sop/control/CURRENT.md` for the current recovery state.
5. Read the active task spec in `.dev_sop/project-specs/*.md` before implementation work.
6. Read `.dev_sop/core/templates/*`, `.dev_sop/core/guides/*`, `.dev_sop/core/examples/*`, or `.dev_sop/core/skills/*` only when the current slice needs them.

## Precedence Contract

- `approved exceptions > active task spec > project rules > core rules > entry adapter notes`
- The active task spec may narrow work inside the rule set, but it must not silently relax hard rules.
- Any rule relaxation must be recorded in `.dev_sop/project-rules/exceptions.md` and referenced from the active spec.

## Source Of Truth

- `README.md`
  Human-facing project entrypoint.

- `.dev_sop/README.md`
  Canonical namespace map for the SOP package.

- `.dev_sop/VERSION.md`
  Source of truth for the current SOP package contract.

- `.dev_sop/upgrades/*`
  Version-targeted SOP upgrade procedures.

- `CLAUDE.md`
  Claude Code entry adapter.

## Codex Notes

- Codex should enter through this file directly.
- If `AGENTS.md`, `CLAUDE.md`, `.dev_sop/core/rules/*`, or `.dev_sop/project-rules/*` changes during an active Codex thread, start a fresh Codex thread before relying on the updated instructions.
- In copied projects, use root `product/` for final outputs and root `dev/` for in-progress development artifacts.
- Use root `sandbox/` only when disposable tests or experiments need an isolated workspace.
- When isolated test directories are needed, route them into `sandbox/` instead of creating ad hoc root `test*` directories.
- When documents overlap, apply the precedence contract before inventing a local interpretation.

## Project Local Notes

Use this optional section for repository-specific entrypoint notes that should survive SOP upgrades.
Future SOP upgrades should preserve this section unless a project-local rule explicitly replaces it.
