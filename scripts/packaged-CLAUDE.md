# CLAUDE.md

This repository uses `CLAUDE.md` as the Claude Code entry adapter for the Dev SOP.

## Claude Code Reading Order

1. Read `AGENTS.md` for the shared entry contract and precedence rules.
2. Read `.dev_sop/README.md` for the namespace map and layer boundaries.
3. Read `.dev_sop/core/rules/rule-index.md` for the starter-owned baseline rules.
4. Read `.dev_sop/project-rules/rule-index.md` for the project-generated rule layer.
5. Read `.dev_sop/control/CURRENT.md` for the current recovery state.
6. Read the active task spec in `.dev_sop/project-specs/*.md` before implementation work.

## Claude Code Notes

- Claude Code should enter through this file or through `AGENTS.md`.
- If `CLAUDE.md`, `AGENTS.md`, `.dev_sop/core/rules/*`, or `.dev_sop/project-rules/*` changes during an active Claude Code session, start a fresh Claude Code session before relying on the updated instructions.
- In copied projects, use root `product/` for final outputs and root `dev/` for in-progress development artifacts.
- Use root `sandbox/` only when disposable tests or experiments need an isolated workspace.
- When isolated test directories are needed, route them into `sandbox/` instead of creating ad hoc root `test*` directories.
- When documents overlap, apply the precedence contract described in `AGENTS.md` before inventing a local interpretation.

## Project Local Notes

Use this optional section for repository-specific Claude Code notes that should survive SOP upgrades.
Future SOP upgrades should preserve this section unless a project-local rule explicitly replaces it.
