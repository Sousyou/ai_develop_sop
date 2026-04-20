# Dev SOP Version

This file is authored in `product/VERSION.md`.
In a copied project, the same file is installed as `.dev_sop/VERSION.md`.

## Current Version
`1.8.0`

## Release Date
`2026-04-20`

## Source Of Truth

This file is the source of truth for the current Dev SOP package version in this repository or in a copied project.

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

## Upgrade Use

When upgrading SOP assets in a copied project:

1. read the copied project's `.dev_sop/VERSION.md`
2. compare it with the source starter's `product/VERSION.md`
3. apply each newer upgrade note in `.dev_sop/upgrades/*` in ascending version order
4. preserve project-local SOP customizations unless an upgrade note explicitly replaces them
5. update the copied project's `.dev_sop/VERSION.md` only after the upgrade lands and validates

## Notes

- this version tracks the SOP package, not the product or application
- upgrade notes describe SOP asset changes, not application-code changes
- `1.8.0` moves the source repository's canonical SOP product tree to `product/*` while keeping `.dev_sop/*` as the installed path in copied projects
