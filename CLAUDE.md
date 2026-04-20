# CLAUDE.md

This repository uses `CLAUDE.md` as the Claude Code entry adapter for the Dev SOP.

## Claude Code Reading Order

1. Read `AGENTS.md` for the shared operating contract.
2. Read `.dev_sop/control/CURRENT.md` if you are recovering active work.
3. Read the active task spec in `.dev_sop/project-specs/*.md` before implementation work.
4. Read `.dev_sop/core/*` only when the current slice needs a rule, template, guide, example, or reusable skill.

## Claude Code Notes

- Claude Code should enter through this file, then follow `AGENTS.md` and the `.dev_sop/*` package.
- Use the same precedence contract defined in `AGENTS.md`.
- If `CLAUDE.md` or `AGENTS.md` changes during an active Claude Code session, restart from the updated entrypoint before relying on the new instructions.
- If `CLAUDE.md` and `AGENTS.md` diverge, fix the adapter drift in the same change and treat `.dev_sop/core/rules/*` plus `.dev_sop/project-rules/*` as authoritative.
- Ignore `.dev_sop/_backup/*` unless you are intentionally recovering repository-local backup material.
