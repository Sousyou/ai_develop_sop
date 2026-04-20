# Dev SOP Version

## Current Version
`1.6.0`

## Release Date
`2026-04-20`

## Source Of Truth

This file is the source of truth for the current Dev SOP package version in this repository or in a copied project.

## Current Contract

- the SOP namespace root is `.dev_sop/`
- starter-owned baseline rules live under `.dev_sop/core/rules/*`
- starter-owned templates live under `.dev_sop/core/templates/*`
- starter-owned guides live under `.dev_sop/core/guides/*`
- starter-owned examples live under `.dev_sop/core/examples/*`
- starter-owned reusable skills live under `.dev_sop/core/skills/*`
- project-generated rule files live under `.dev_sop/project-rules/*`
- project-generated task specs live under `.dev_sop/project-specs/*`
- project-generated facts live under `.dev_sop/project-facts/*`
- upgrade notes live under `.dev_sop/upgrades/*`
- repository-local backup and non-copyable project-produced artifacts may be retained under `.dev_sop/_backup/*`, but `_backup` is not part of the canonical starter surface
- tool-entry notes live only in `AGENTS.md` and `CLAUDE.md`
- the precedence contract is `approved exceptions > active task spec > project rules > core rules > entry adapter notes`
- a task spec may narrow work, but it may not silently relax hard rules
- any rule exception must be recorded in `.dev_sop/project-rules/exceptions.md` and referenced from the active spec
- if the shared SOP package itself changes, update `.dev_sop/core/*`; if the current project changes, update the project directories
- if an SOP upgrade changes `AGENTS.md`, `CLAUDE.md`, `.dev_sop/core/rules/*`, or `.dev_sop/project-rules/*`, continue in a fresh Codex or Claude Code thread before relying on the new instructions

## Upgrade Use

When upgrading SOP assets in a copied project:

1. read the copied project's `.dev_sop/VERSION.md`
2. compare it with the source starter's `.dev_sop/VERSION.md`
3. apply each newer upgrade note in `.dev_sop/upgrades/*` in ascending version order
4. preserve project-local SOP customizations unless an upgrade note explicitly replaces them
5. update the copied project's `.dev_sop/VERSION.md` only after the upgrade lands and validates

## Notes

- this version tracks the SOP package, not the product or application
- upgrade notes describe SOP asset changes, not application-code changes
- `1.6.0` restores starter-owned cross-project reusable assets to `.dev_sop/core/*` and reserves `.dev_sop/_backup/*` for repository-local backup or non-copyable project artifacts
