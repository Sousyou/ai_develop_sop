# AI Project Quickstart

- **Version**: `v2.0`
- **Status**: official runtime entry
- **Role**: low-token runtime contract for non-`sop_develop` projects

---

## Purpose

This file answers only:

1. what minimum rules the current session must follow
2. when AI can start work directly
3. when AI must continue reading deeper documents

---

## Default Entry Order

For injected `common` projects, the default order is:

1. `runtime/entry_state.md`
2. `runtime/session_brief.md`
3. `ai_project_quickstart.md`
4. deeper documents only on demand

Only when `project_type == None` should AI additionally read `ai_project_type.md`.

---

## Minimum Runtime Rules

1. align boundaries before implementation
2. align validation before execution
3. prefer external plans first; review, trim, and patch them before generating a new plan yourself
4. update `runtime/current_target.md` before rewriting long-term `project_charter`
5. write stable facts into `facts/*`
6. write runtime flow deltas into `ai_runtime_sop.md`
7. write runtime standard deltas into `ai_runtime_standards.md`
8. if entry understanding drifts, correct the entry before continuing

---

## When AI Can Start Directly

AI may start work without reading the full spec when all are true:

1. `project_type` is clear
2. `session_brief` is enough to explain product roots, current goal, and current phase
3. the task does not introduce a new process, new standard, layer redesign, or entry correction

---

## When AI Must Read Deeper

Continue reading when any of these apply:

1. exact product-vs-governance boundaries are needed -> `runtime/project_mount.md`
2. long-term direction or top-level constraints matter -> `runtime/project_charter.md`
3. current high-frequency goal or validation target matters -> `runtime/current_target.md`
4. runtime flow deltas matter -> `ai_runtime_sop.md`
5. runtime standard deltas matter -> `ai_runtime_standards.md`
6. document routing is unclear -> `standards/document_routing_matrix.md`
7. the full model or cross-layer rules matter -> `ai_project_sop.md`
8. layer details matter -> `sop/core/*`

---

## Conclusion

For most sessions, `entry_state + session_brief + quickstart` should be enough to start.
Read deeper only when the current problem truly needs more context.
