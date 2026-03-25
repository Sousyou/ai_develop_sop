# AGENTS

- **Version**: `v2.0`
- **Status**: official entry
- **Role**: fixed entry for the `ai_develop_sop` source repository itself
- **Scope**: only this repository: `f:\ai_develop_sop`

---

## Purpose

This file answers only:

1. how this repository should be classified
2. how this source repository differs from an injected host project
3. where AI should continue after recognizing this repository

---

## Fixed Entry Result

This repository is fixed as:

- `repository_role`: `sop_engine_source`
- `project_type_behavior`: `fixed_sop_develop`

This means:

1. this repository always follows the `sop_develop` path
2. this file does not handle project-type selection or host runtime state
3. this repository does not use `runtime/entry_state.md` as its own entry state

---

## First-Priority Rule

AI must read this file first when entering this repository.

Before confirming that this repository is the SOP engine source repository, AI must not jump into formal editing, analysis, or maintenance work.

After confirmation, continue through:

1. `ai_project_sop.md`
2. the corresponding definitions, rules, facts, standards, templates, and child SOPs

---

## Boundary Against Injected Projects

When `ai_develop_sop/` is injected into another repository:

1. the host-project root `AGENTS.md` only bootstraps AI into `project_entry.md`
2. host-project runtime state is defined by the host-project file `runtime/entry_state.md`
3. the host low-token digest is defined by the host-project file `runtime/session_brief.md`
4. host-project type selection and writeback are handled by `project_entry.md`, not by this file

In short:

- this file serves only the SOP engine source repository
- injected host projects use `project_entry.md + runtime/*`

---

## Default Behavior In This Repository

AI should treat this repository as:

1. an SOP design and maintenance repository
2. a governance-system repository for rules, templates, facts, skills, and standards
3. not a `common` host-project instance

---

## Related Documents

- project type registry: `ai_project_type.md`
- master navigation: `ai_project_sop.md`
- injected-project entry: `project_entry.md`
- injected-project instance entry: host-project `runtime/entry_state.md`
- injected-project low-token digest: host-project `runtime/session_brief.md`

---

## Conclusion

This file is only the source-repository entry gate.
It does not store writable host-project `project_type` fields and does not handle injected-project type-selection protocol.
