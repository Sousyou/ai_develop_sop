# Writeback Rules

- **Version**: `v2.1`
- **Status**: official rule
- **Role**: forces post-execution writeback checks so stable conclusions do not stay only in conversation

---

## Default Checks

After each closure, check:

1. whether facts must be written back
2. whether a `skill candidate` must be registered
3. whether an `SOP candidate` must be registered
4. whether rules or standards need updates

---

## Layer Expectations

- `task`: return result, unfinished work, exceptions, and candidate follow-ups
- `plan`: summarize results and decide whether they must rise upward
- `phase`: decide whether stable items have formed
- `project`: receive only cross-phase stable facts

---

## Fact Writeback Rules

1. confirmed conclusions that will keep affecting later judgment belong in `facts/*`
2. when adding or changing facts, update `facts/facts_index.md`
3. one-step-only notes should not be promoted into formal facts

---

## Goal Alignment Check

After each closure, also check:

1. does the change only affect the current high-frequency target
2. if yes, update `runtime/current_target.md` first
3. only update `runtime/project_charter.md` when the long-term goal, boundary, or top-level constraints have changed

---

## Runtime Digest Sync

If any of these changes in the current turn:

- `runtime/entry_state.md`
- `runtime/project_mount.md`
- `runtime/project_charter.md`
- `runtime/current_target.md`
- `ai_runtime_sop.md`
- `ai_runtime_standards.md`

then the same turn must also update:

- `runtime/session_brief.md`

`runtime/session_brief.md` is a derived digest. It must not depend on a separate refresh command and must not lag behind its source documents.
