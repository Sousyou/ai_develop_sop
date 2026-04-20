# Dev SOP Namespace

This directory defines the installed SOP namespace for copied projects.

When the starter is adopted in a project, this tree is materialized as `.dev_sop/*`.

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
- Put it outside the installed SOP namespace when it documents repository-level facts, packaging code, or product implementation.

## Copied Project Workspace Convention

The installed SOP namespace still lives under `.dev_sop/*`, but copied-project working directories stay at the repository root:

- `product/`
  Final product outputs, deliverables, or reviewed release-ready artifacts.

- `dev/`
  In-progress development outputs, drafts, notes, and intermediate build artifacts.

- `sandbox/`
  Optional isolated workspace for disposable tests, experiments, or temporary validation environments.

`dev-sop init` and `dev-sop update` ensure that root `product/` and `dev/` exist.
Use `--with-sandbox` when the copied project also needs a root `sandbox/`.
When isolated filesystem testing is needed during development, route it into `sandbox/` instead of creating ad hoc root `test*`, `tmp*`, or `playground*` directories.

## Maintenance Rule

- When starter-owned reusable skills under `core/skills/` change, update `core/skills/skill-registry.md`.
- When starter-owned example files under `core/examples/` change, update the matching example-surface `README.md`.
- If the starter package contract changes, update the root entry docs, `VERSION.md`, and the matching upgrade note in the same change.
- Once a version is published as a standardized CLI baseline, any later starter-managed change must bump `VERSION.md` and add a new upgrade note.
