# SOP Maintenance Rules

These rules apply to this source repository when maintaining the packaged SOP product.

They are source-repository rules, not copied-project starter content.

## Entrypoint Rule

For standardized copied projects:

- project-local additions to installed `AGENTS.md` and `CLAUDE.md` must live under `## Project Local Notes` or under separate custom headings
- do not mix project-local notes into starter-managed sections such as `## Codex Reading Order`, `## Precedence Contract`, `## Source Of Truth`, `## Codex Notes`, `## Claude Code Reading Order`, or `## Claude Code Notes`

When changing the packaged entrypoint templates or the merge logic in this repository, preserve that contract.

## Versioning Rule

After the `1.0.0` standardized baseline:

- do not mutate starter-managed package content in place under the same published version
- if starter-managed surfaces change, bump the package version
- add a matching upgrade note under `product/upgrades/`
- keep the version bump and upgrade note in the same change as the starter-managed content update

Starter-managed surfaces include:

- packaged root `AGENTS.md` and `CLAUDE.md`
- `product/README.md`
- `product/core/*`
- `product/upgrades/*`
- starter-managed surface guides under `product/project-rules/README.md`, `product/project-specs/README.md`, and `product/project-facts/README.md`

## Scope Reminder

- source-repository rules belong in `facts/*`
- packaged reusable SOP assets belong in `product/*`
- packaging code belongs in `src/*` and `scripts/*`
