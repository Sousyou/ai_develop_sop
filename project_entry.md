# Injected Project Entry

- **Version**: `v2.0`
- **Status**: official entry
- **Role**: entry for ordinary projects after `ai_develop_sop/` is injected

---

## Purpose

This file answers:

1. what AI should read first in an injected host project
2. where host-project instance state lives
3. how to distinguish product space from SOP governance space

---

## First-Priority Rule

When the host-project bootstrap `AGENTS.md` points here, AI must follow the low-token entry path first:

1. `runtime/entry_state.md`
2. `runtime/session_brief.md`

Only continue deeper when needed:

- if `project_type == None`: read `ai_project_type.md`
- if runtime work rules are needed: read `ai_project_quickstart.md`
- if `session_brief` is insufficient: read the corresponding source documents on demand

Before establishing this entry understanding, do not jump into formal implementation, analysis, or modification.

---

## Authoritative Instance State

In injected mode, host-project instance state is defined by `runtime/entry_state.md`, not by `ai_develop_sop/AGENTS.md`.

This means:

1. `project_type` is taken from `runtime/entry_state.md`
2. initialization time, runtime mode, and default plan source are also taken from `runtime/entry_state.md`
3. `ai_develop_sop/AGENTS.md` remains the source-repository entry only
4. re-running `ai_sop_init.bat` resets host bootstrap/runtime entry files, not the SOP engine source entry

---

## Authoritative Mount Boundary

In injected mode, mount boundaries are defined by `runtime/project_mount.md`.

AI must use it to distinguish:

- product roots
- product-doc roots
- SOP governance roots
- scratch-only files

To reduce startup cost, prefer `runtime/session_brief.md` first and open `runtime/project_mount.md` only when exact boundaries matter.

---

## Project-Type Branch

If `runtime/entry_state.md` contains `project_type == None`, AI must pause the formal workflow and:

1. explain that project type has not been selected
2. read `ai_project_type.md`
3. ask for a valid type value
4. write the confirmed value back to `runtime/entry_state.md`
5. only then continue

For newly injected projects initialized by `ai_sop_init.bat`, this branch is normally not hit because init writes `project_type == common` directly.

---

## Formal Entry Order

After `project_type` is clear:

1. read `runtime/session_brief.md`
2. if `project_type == common`, read `ai_project_quickstart.md`
3. only when needed, expand into `runtime/project_mount.md`, `runtime/project_charter.md`, `runtime/current_target.md`, `ai_runtime_sop.md`, `ai_runtime_standards.md`, or `ai_project_sop.md`
4. continue into `project / phase / plan / task`

If runtime source documents change, the same turn must also update `runtime/session_brief.md`.

---

## Conclusion

In injected mode:

1. the host bootstrap `AGENTS.md` only routes AI here
2. `runtime/entry_state.md` is the instance-state entry
3. `runtime/session_brief.md` is the low-token digest entry
4. `runtime/project_mount.md` is the mount-boundary entry
5. `runtime/project_charter.md` is the long-term goal entry
6. `runtime/current_target.md` is the high-frequency goal entry
7. `ai_project_quickstart.md` is the default runtime contract and `ai_project_sop.md` remains the full master spec
