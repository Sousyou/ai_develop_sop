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

After installation, use:

```bash
dev-sop version
dev-sop init /path/to/project
dev-sop update /path/to/project
```

`init` copies the packaged starter surface into the target directory and materializes it as `.dev_sop/*`. Existing files are skipped unless `--force` is provided.

`update` is safe by default:

- it creates missing starter files
- it updates starter-owned files only when there is no conflict
- it leaves conflicting starter-owned files in place unless `--force` is provided
- it leaves seed files such as control files and project-surface `README.md` files in place unless `--force-seed` is provided
- it does not update the target project's `.dev_sop/VERSION.md` when starter-owned conflicts remain

## Copy Into A Real Project

When using this repository as the source of a copied project or a packaged install:

- copy the packaged starter surface into the target project's `.dev_sop/`
- do not copy root `facts/*`
- do not copy packaging implementation files unless you are intentionally embedding the CLI source

The packaged CLI already follows this rule: it distributes only the starter surface.
