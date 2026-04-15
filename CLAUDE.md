# CLAUDE.md

This repository uses `AGENTS.md` as the canonical source of repository-level guidance.

## Source of truth

- Use `AGENTS.md` as the primary AI-tool entrypoint for repository-level behavior.
- Use `.dev_sop/README.md` for the `.dev_sop/*` namespace map and boundary rules.
- Use `.dev_sop/VERSION.md` and `.dev_sop/upgrades/*` when upgrading SOP assets in a copied project.
- Follow `.cursor/rules/*`, `.dev_sop/doc/*`, and `.dev_sop/skill/*` as referenced by `AGENTS.md`.
- If `CLAUDE.md` and `AGENTS.md` differ, `AGENTS.md` wins.

This file is an adapter entry point, not a second rule system.
