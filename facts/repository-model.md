# Repository Model

This source repository keeps a light root and stores the SOP product source in one dedicated directory.

## Root Surfaces

- `AGENTS.md`
  Lightweight root entrypoint.

- `CLAUDE.md`
  Claude Code entry adapter.

- `facts/*`
  Root facts for fast orientation.

- `product/*`
  The SOP product source tree. This content becomes `.dev_sop/*` in copied projects.

- `src/`, `scripts/`, `pyproject.toml`
  Packaging and CLI implementation.

## Rule Of Thumb

- If the file is part of the reusable SOP product, it belongs in `product/*`.
- If the file is a lightweight root fact for orientation, it belongs in `facts/*`.
- If the file is packaging or CLI code, it belongs in `src/` or `scripts/`.
- If the file documents how this source repository must maintain the packaged SOP contract, keep it in `facts/*` rather than in the packaged starter tree.
- Do not confuse this source repository's `product/*` tree with the copied-project root `product/` directory created by `dev-sop init` or `dev-sop update`.
- In copied projects, if isolated filesystem testing is needed, use the root `sandbox/` workspace rather than scattering ad hoc `test*` directories at the repository root.
