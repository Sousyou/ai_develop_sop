<!-- bootstrap_generated_by_ai_develop_sop -->
# AGENTS

## AI SOP Bootstrap

- `bootstrap_generated_at`: `{{GENERATED_AT}}`
- `sop_enabled`: `true`
- `sop_root`: `./{{SOP_DIR_NAME}}`
- `sop_entry`: `./{{SOP_DIR_NAME}}/project_entry.md`
- `project_mount`: `./{{SOP_DIR_NAME}}/runtime/project_mount.md`
- `entry_state`: `./{{SOP_DIR_NAME}}/runtime/entry_state.md`
- `session_brief`: `./{{SOP_DIR_NAME}}/runtime/session_brief.md`

These path-valued fields point to host-project files. They are field names, not literal file names.

## Required Behavior

1. AI must first read the file referenced by `sop_entry` (`./{{SOP_DIR_NAME}}/project_entry.md`).
2. AI must use the file referenced by `project_mount` to distinguish product roots, product docs, governance roots, and scratch space.
3. AI must use the file referenced by `entry_state` to determine the current project type and runtime state.
4. AI should prefer the file referenced by `session_brief` as the low-token startup digest.
5. All SOP governance content must stay under `sop_root`.
6. Product code and product docs should not be written into `sop_root` unless they are SOP assets themselves.
