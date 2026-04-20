# AI Engineering SOP Starter

This repository can be copied into real projects as a reusable SOP starter for AI-assisted engineering.

## Starter Surface

- `AGENTS.md`
- `CLAUDE.md`
- `.dev_sop/README.md`
- `.dev_sop/VERSION.md`
- `.dev_sop/core/*`
- `.dev_sop/control/*`
- `.dev_sop/project-rules/*`
- `.dev_sop/project-specs/*`
- `.dev_sop/project-facts/*`
- `.dev_sop/upgrades/*`

## How To Use

1. Read `AGENTS.md` or `CLAUDE.md` first.
2. Read `.dev_sop/README.md` for the namespace map.
3. Read `.dev_sop/core/rules/rule-index.md` for baseline rules.
4. Use `.dev_sop/project-rules/*`, `.dev_sop/project-specs/*`, and `.dev_sop/project-facts/*` for project-local outputs after adoption.
5. Use `.dev_sop/upgrades/*` when upgrading the starter in an existing project.

## Notes

- `.dev_sop/core/*` contains starter-owned reusable assets.
- `.dev_sop/control/*` and `.dev_sop/project-*` are the starter seed surfaces that copied projects will adopt as their own runtime surfaces.
- This starter does not assume a specific application stack.
