# Project Bootstrap SOP

- **Version**: `v2.1`
- **Status**: official
- **Role**: defines how a project becomes ready to enter the SOP workflow

---

## Purpose

Bootstrap is the step that makes a project operational under this SOP.
It must leave the project ready to accept the first concrete development task.

---

## Bootstrap Principles

1. establish project direction before execution detail
2. create only the minimum skeleton needed now
3. keep the host-project root bootstrap thin
4. make initialization zero-touch for a newly injected project

---

## Standard Bootstrap Result

After bootstrap, the project should have:

1. a host-project bootstrap `AGENTS.md`
2. a usable runtime instance state
3. a short `session_brief`
4. governance directories for `rules`, `facts`, and `skills`
5. a readable `README.md`

If the host project already has a `README.md`, preserve it.
If it does not, `ai_sop_init.bat` must generate a thin bootstrap README.

---

## Runtime Requirements

Bootstrap must produce a runtime state that is immediately usable:

- `project_type = common`
- `runtime_mode = active`
- `current_phase = bootstrap_ready`
- `default_plan_source = external_plan_preferred`

It must also create:

- `runtime/project_mount.md`
- `runtime/project_charter.md`
- `runtime/current_target.md`
- `runtime/session_brief.md`

---

## Completion Rule

Bootstrap is complete only when the injected project can enter:

`host AGENTS.md -> project_entry.md -> runtime/entry_state.md -> runtime/session_brief.md -> ai_project_quickstart.md`

without extra manual setup.
