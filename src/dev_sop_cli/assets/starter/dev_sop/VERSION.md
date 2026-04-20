# Dev SOP Version

## Current Version
`1.0.0`

## Release Date
`2026-04-20`

## Source Of Truth

This file is the source of truth for the current installed Dev SOP package version.

## Current Contract

- the product root becomes `.dev_sop/` when installed into a copied project
- starter-owned baseline rules live under `core/rules/*`
- starter-owned templates live under `core/templates/*`
- starter-owned guides live under `core/guides/*`
- starter-owned examples live under `core/examples/*`
- starter-owned reusable skills live under `core/skills/*`
- project-generated rule files live under `project-rules/*`
- project-generated task specs live under `project-specs/*`
- project-generated facts live under `project-facts/*`
- upgrade notes live under `upgrades/*`
- tool-entry notes live only in `AGENTS.md` and `CLAUDE.md`
- the precedence contract is `approved exceptions > active task spec > project rules > core rules > entry adapter notes`
- a task spec may narrow work, but it may not silently relax hard rules
- any rule exception must be recorded in `project-rules/exceptions.md` and referenced from the active spec
- if the shared SOP package itself changes, update `core/*`; if the current project changes, update the project directories
- if an SOP upgrade changes `AGENTS.md`, `CLAUDE.md`, `core/rules/*`, or `project-rules/*`, continue in a fresh Codex or Claude Code thread before relying on the new instructions

## Pure CLI Update Boundary

The pure command-line update path assumes:

- root `README.md` is project-owned and is not managed by the SOP package
- `AGENTS.md` and `CLAUDE.md` are updated by section merge, preserving `Project Local Notes`
- `AGENTS.md` and `CLAUDE.md` still use the canonical heading structure shipped by the starter
- `.dev_sop/README.md`, `.dev_sop/core/*`, and `.dev_sop/upgrades/*` are starter-managed and may be replaced by the CLI
- `.dev_sop/project-rules/README.md`, `.dev_sop/project-specs/README.md`, and `.dev_sop/project-facts/README.md` are starter-managed surface guides
- `.dev_sop/control/*`, `.dev_sop/project-rules/rule-index.md`, and `.dev_sop/project-rules/exceptions.md` are project-owned after adoption and are not rewritten by default

Future SOP changes that must be delivered by CLI should stay inside the starter-managed surfaces above.
After this `1.0.0` baseline is frozen, any starter-managed content change must ship as a new version with a new upgrade note.

## Upgrade Use

When upgrading SOP assets in a copied project:

1. read the copied project's `.dev_sop/VERSION.md`
2. compare it with the source starter's current package version
3. apply each newer upgrade note in `.dev_sop/upgrades/*` in ascending version order
4. preserve project-local SOP customizations unless an upgrade note explicitly replaces them
5. update the copied project's `.dev_sop/VERSION.md` only after the upgrade lands and validates

## Notes

- this version tracks the SOP package, not the product or application
- upgrade notes describe SOP asset changes, not application-code changes
- `1.0.0` is the stable CLI baseline for the current installed SOP structure
