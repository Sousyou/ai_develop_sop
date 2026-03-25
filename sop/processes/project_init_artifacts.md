# Project Init Artifacts

- **Version**: `v2.1`
- **Status**: official
- **Role**: defines the minimum artifacts a project should have after initialization

---

## Required Artifacts

### Host-project entry artifacts

- `README.md`
- `AGENTS.md`

Rules:

1. `AGENTS.md` must exist and stay thin
2. if the host project already has a `README.md`, init preserves it
3. if the host project has no `README.md`, init generates a thin bootstrap placeholder

### Runtime instance artifacts

- `runtime/entry_state.md`
- `runtime/project_mount.md`
- `runtime/project_charter.md`
- `runtime/current_target.md`
- `runtime/session_brief.md`

Rules:

1. these are host-project runtime artifacts generated from `runtime/templates/*`
2. `session_brief.md` is derived and must be co-updated with its source runtime documents

### Governance artifacts

- `rules/`
- `facts/`
- `skills/skill_policy.md`
- `skills/skill_registry.md`
- `skills/skill_template.md`

---

## Recommended Early Fact Artifacts

These may exist immediately or be added in the first real execution loop:

- `facts/project_scope.md`
- `facts/facts_index.md`
- `facts/golden_cases.md`

---

## Minimal Completion Standard

Initialization is minimally complete when the host project has:

1. a readable outer entry
2. a bootstrap `AGENTS.md`
3. the runtime instance files
4. the governance directories
5. enough default content to enter the first concrete task without extra manual setup
