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
