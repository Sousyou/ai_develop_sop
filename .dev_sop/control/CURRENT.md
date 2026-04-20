# CURRENT

## Current phase
Bootstrap or refine the SOP inside the current project without losing the starter's shared operating model.

## Current target
Use the starter as a copyable baseline with:
- baseline rules under `.dev_sop/core/rules/*`
- starter-owned templates, guides, examples, and skills under `.dev_sop/core/*`
- a project-local rule surface under `.dev_sop/project-rules/*`
- real task specs under `.dev_sop/project-specs/*`
- real stable facts under `.dev_sop/project-facts/*`

## Active slice
Establish or maintain the smallest working plan -> spec -> implementation -> validation loop for the current project.

## In scope now

- keep `.dev_sop/core/*` as starter-owned cross-project reusable SOP content
- keep `AGENTS.md` and `CLAUDE.md` as the only tool-entry adapters
- keep `.dev_sop/project-rules/*` for current-project operating rules only
- keep `.dev_sop/control/*` recovery-first and small
- keep `.dev_sop/project-specs/*` and `.dev_sop/project-facts/*` for real project outputs
- keep `.dev_sop/upgrades/*` explicit enough for copied-project migrations from older layouts
- keep `.dev_sop/_backup/*` non-canonical and repository-local

## Out of scope now

- reintroducing removed legacy adapters into the mainline package
- putting shipped-system or product docs under `.dev_sop/`
- turning `.dev_sop/control/*` into a project board or work log
- treating repository-local backup as part of the copyable starter package

## Current source of truth

- `.dev_sop/control/DOC_MAP.md`
- `.dev_sop/core/rules/rule-index.md`
- `.dev_sop/project-rules/rule-index.md`
- `.dev_sop/README.md`
- `.dev_sop/VERSION.md`
- `AGENTS.md` for Codex entry
- `CLAUDE.md` for Claude Code entry
- the active task spec in `.dev_sop/project-specs/*.md`, if implementation work is underway

## Frozen decisions

- `.dev_sop/` remains the namespace root.
- Starter-owned baseline rules live under `.dev_sop/core/rules/*`.
- Starter-owned reusable assets live under `.dev_sop/core/*`.
- Project-generated rules live under `.dev_sop/project-rules/*`.
- Project-generated specs live under `.dev_sop/project-specs/*`.
- Project-generated facts live under `.dev_sop/project-facts/*`.
- Repository-local backup and non-copyable project artifacts may be retained under `.dev_sop/_backup/*`, but `_backup` is non-canonical.
- `AGENTS.md` is the Codex entry adapter and `CLAUDE.md` is the Claude Code entry adapter.
- The precedence contract is `approved exceptions > active task spec > project rules > core rules > entry adapter notes`.
- Hard rules may be relaxed only through `.dev_sop/project-rules/exceptions.md` plus an explicit spec reference.

## Latest experiment
None. Keep experiments task-local unless they become stable enough to deserve facts, rules, or reusable starter assets.

## Next 3 actions

1. Keep root entry docs and layer docs aligned whenever the namespace contract changes.
2. Keep starter-owned reusable assets under `.dev_sop/core/*` and keep current-project outputs under the project surfaces.
3. Keep copied-project upgrade notes explicit enough that older layouts still have a clear migration path.

## Risks to watch

- repo-specific project artifacts could reappear under `.dev_sop/core/*` and muddy the starter boundary
- repository-local backup could be mistaken for copyable starter content
- `.dev_sop/project-rules/*` could drift from `.dev_sop/core/rules/*` and make precedence ambiguous
- `.dev_sop/control/*` could still drift into status reporting instead of recovery routing
