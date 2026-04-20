# Project Rules Surface

This directory holds project-generated rules that stay active for the current project.

Use this surface for rules that tighten, specialize, or waive the starter-owned baseline rules under `.dev_sop/core/rules/*`.

## Boundary

- keep current-project rules here
- keep starter-owned baseline rules under `.dev_sop/core/rules/*`
- use natural filenames inside this directory
- use `rule-index.md` as the project rule entry
- use `exceptions.md` as the project exception registry
- do not populate this directory just because the directory exists
- keeping only `README.md`, `rule-index.md`, and `exceptions.md` is valid until the project needs more local rules

## Current Files

- `rule-index.md`
- `exceptions.md`
