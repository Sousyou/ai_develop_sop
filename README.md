# AI Engineering SOP Starter

This repository is the source repository for a reusable SOP starter.

The source tree is intentionally split so the repository root stays light:

- `AGENTS.md`, `CLAUDE.md`
  Lightweight AI entrypoints.

- `facts/*`
  Source-repository facts for fast orientation.

- `product/*`
  The SOP product source tree. This is the content that gets packaged and copied into other projects as `.dev_sop/*`.

- `src/`, `scripts/`, `pyproject.toml`
  The pip-installable CLI implementation.

## Product Layout

`product/*` is the canonical source for the SOP package and contains:

- `product/README.md`
- `product/VERSION.md`
- `product/core/*`
- `product/control/*`
- `product/project-rules/*`
- `product/project-specs/*`
- `product/project-facts/*`
- `product/upgrades/*`

When the starter is copied into a real project, `product/*` is installed as `.dev_sop/*`.

## CLI Install

This repository can be packaged as a pip-installable CLI for bootstrapping or updating the starter in other projects.

Install locally from this repository:

```bash
python -m pip install .
```

Or install editable while developing the CLI itself:

```bash
python -m pip install -e .
```

On Windows, you can also use the helper batch files in `scripts/`:

```bat
scripts\install-dev-sop.bat
scripts\install-dev-sop.bat editable
scripts\uninstall-dev-sop.bat
```

After installation, use:

```bash
dev-sop version
dev-sop init /path/to/project
dev-sop update /path/to/project
```

For non-interactive use:

```bash
dev-sop init /path/to/project --yes
dev-sop update /path/to/project --yes
```

`init` copies the packaged starter surface into the target directory and materializes it as `.dev_sop/*`. It also installs root `AGENTS.md` and `CLAUDE.md`. It does not create or overwrite the target project's root `README.md` by default.

Before `init` writes anything, it shows:

- the target path
- the packaged starter SOP version
- the target project's current SOP version, if one already exists
- whether `--force` or `--dry-run` is active

Then it requires an explicit confirmation unless `--yes` is provided.

`update` is safe by default:

- it creates missing starter files
- it replaces starter-owned files under `.dev_sop/README.md`, `.dev_sop/core/*`, and `.dev_sop/upgrades/*`
- it replaces starter-owned project-surface guides such as `.dev_sop/project-rules/README.md`, `.dev_sop/project-specs/README.md`, and `.dev_sop/project-facts/README.md`
- it merges root `AGENTS.md` and `CLAUDE.md` by section, preserving `Project Local Notes`
- it leaves project-owned seed files such as `.dev_sop/control/*`, `.dev_sop/project-rules/rule-index.md`, and `.dev_sop/project-rules/exceptions.md` in place unless `--force-seed` is provided
- it uses `--force` only as a fallback when entrypoint merge cannot be applied cleanly
- it does not update the target project's `.dev_sop/VERSION.md` when entrypoint conflicts remain

Before `update` runs, it shows:

- the target path
- the packaged starter SOP version
- the target project's current SOP version
- whether `--force`, `--force-seed`, or `--dry-run` is active

Then it requires an explicit confirmation unless `--yes` is provided.

The pure command-line update guarantee applies to standardized projects only:

- `AGENTS.md` and `CLAUDE.md` keep the canonical heading structure shipped by the starter
- repository-specific entrypoint notes live under `## Project Local Notes`
- the project's own SOP state lives in `.dev_sop/control/*`, `.dev_sop/project-rules/rule-index.md`, `.dev_sop/project-rules/exceptions.md`, `.dev_sop/project-specs/*`, and `.dev_sop/project-facts/*`
- if a project drifts outside that structure, normalize it first before relying on `dev-sop update`

## Copy Into A Real Project

When using this repository as the source of a copied project or a packaged install:

- copy the packaged starter surface into the target project's `.dev_sop/`
- keep the target project's own root `README.md`
- do not copy root `facts/*`
- do not copy packaging implementation files unless you are intentionally embedding the CLI source

The packaged CLI already follows this rule: it distributes only the starter surface.
