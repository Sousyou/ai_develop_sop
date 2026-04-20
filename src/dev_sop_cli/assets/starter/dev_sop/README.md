# Dev SOP Product

This directory is the source tree for the packaged SOP starter.

In this repository the source lives under `product/*`.
When copied or installed into another project, the same tree is materialized as `.dev_sop/*`.

## Namespace Map

- `core/rules/*`
  Starter-owned baseline rules that ship with the package.

- `core/templates/*`
  Starter-owned blank templates and prompt scaffolds.

- `core/guides/*`
  Starter-owned workflow guidance.

- `core/examples/*`
  Starter-owned filled-in reference artifacts.

- `core/skills/*`
  Starter-owned reusable workflows.

- `control/*`
  Starter seed recovery documents for copied projects.

- `project-rules/*`
  Starter seed project-rule surface for copied projects.

- `project-specs/*`
  Starter seed project-spec surface for copied projects.

- `project-facts/*`
  Starter seed project-fact surface for copied projects.

- `upgrades/*`
  SOP package upgrade notes.

## Precedence Contract

When documents overlap, use:

`approved exceptions > active task spec > project rules > core rules > entry adapter notes`

Additional routing rules:

- Use `VERSION.md` and `upgrades/*` for package version and migration questions.
- Use `project-rules/exceptions.md` when a spec needs an approved exception to a hard rule.
- When a document mentions `.dev_sop/*`, that refers to the installed path in a copied project.

## Placement Rule

Choose the destination by the question the file answers:

- Put it in `core/*` when it is starter-owned and cross-project reusable.
- Put it in `control/*` or `project-*` only when it is part of the packaged starter seed surface.
- Put it outside `product/*` when it documents repository-level facts, packaging code, or source-repo implementation.

## Maintenance Rule

- When starter-owned reusable skills under `core/skills/` change, update `core/skills/skill-registry.md`.
- When starter-owned example files under `core/examples/` change, update the matching example-surface `README.md`.
- If the starter package contract changes, update the root entry docs, `VERSION.md`, and the matching upgrade note in the same change.
