# Path Conventions Standard

- **Version**: `v2.0`
- **Status**: official standard
- **Role**: defines default path and directory conventions for the SOP system

---

## Principles

1. product space and SOP governance space must be distinguishable
2. entry files must be stable and easy to locate
3. runtime host-project state must live under `runtime/`
4. cross-project governance assets must stay under their dedicated top-level directories

---

## Top-Level Governance Paths

Recommended top-level paths:

- `sop/`
- `rules/`
- `facts/`
- `skills/`
- `standards/`
- `runtime/`

---

## Entry Paths

Source repository entry:

- `AGENTS.md`

Injected host-project entry path:

- host root `AGENTS.md`
- `project_entry.md`
- `runtime/entry_state.md`
- `runtime/session_brief.md`

---

## Runtime Paths

Host-project runtime instance files belong under `runtime/`.

Required runtime paths:

- `runtime/entry_state.md`
- `runtime/project_mount.md`
- `runtime/project_charter.md`
- `runtime/current_target.md`
- `runtime/session_brief.md`

Templates belong under:

- `runtime/templates/`

---

## Boundary Rule

Product code and product docs should stay outside the SOP governance root unless they are intentionally SOP assets.
