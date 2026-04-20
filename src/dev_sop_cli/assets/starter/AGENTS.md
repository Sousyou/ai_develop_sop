# AGENTS.md

This repository keeps the SOP product source under `product/`.

## Start Order

1. Read `facts/README.md` for repository-level orientation.
2. Read `product/README.md` for the SOP product map.
3. Read `product/core/rules/rule-index.md` for baseline rules.
4. Read `product/project-rules/rule-index.md` for the seed project-rule layer.
5. Read `product/control/CURRENT.md` for recovery state.
6. Read the active task spec in `product/project-specs/*.md` before implementation work.

## Surface Meanings

- `facts/*`
  Lightweight source-repository facts exposed at the root.

- `product/*`
  The SOP product source tree. When copied or installed into another project, this tree becomes `.dev_sop/*`.

- `src/`, `scripts/`, `pyproject.toml`
  Packaging and CLI implementation for distributing the SOP product.

## Notes

- `Codex` should enter through this file directly.
- Product documents may describe installed paths as `.dev_sop/*`; in this source repository, edit the corresponding file under `product/*`.
- Ignore `build/*` and other generated packaging artifacts unless you are validating packaging behavior.
