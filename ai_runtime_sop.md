# AI Runtime SOP

- **Version**: `v2.0`
- **Status**: official runtime flow supplement
- **Role**: records project-specific runtime flow deltas relative to the master SOP
- **Scope**: only non-`sop_develop` projects

---

## Purpose

This file answers:

1. which project-specific flow deltas are active now
2. why those deltas must take effect immediately in the current project
3. which SOP gaps or upgrade candidates were exposed in runtime

---

## Usage Principles

1. inherit the master SOP first, then add project runtime deltas
2. record flow-only content here, not standards
3. record current-project runtime deltas here, not cross-project policy
4. verify in the project first, then decide whether to upgrade into the formal SOP
5. on conflict, follow: host `AGENTS.md` -> `project_entry.md` -> `ai_project_sop.md` -> this file

---

## Allowed Content

This file may record:

- how external plans are accepted by default in the current project
- extra review, validation, writeback, or closure steps required in the current project
- temporary narrowing or supplementation of a formal flow for the current project
- confirmed SOP gaps and runtime upgrade candidates

---

## Forbidden Content

Do not write these here:

- hard standards, naming rules, path rules, or format contracts
- stable facts
- long-term project goals or current targets
- product architecture, API, or runtime instructions

Route them instead to:

- `ai_runtime_standards.md`
- `facts/*`
- `runtime/project_charter.md`
- `runtime/current_target.md`
- product docs

---

## Intake Rule

A flow item belongs here only when all are true:

1. it is a process rule, not a standard
2. it is currently valid for this project
3. it changes execution order, review order, or writeback behavior now
4. without writing it down, the project workflow would drift or become unstable

---

## Runtime Flow Deltas

Current state:

- none

Recommended delta format:

```md
### <delta_name>

- scope:
- trigger:
- flow change:
- why this project uses it:
- exit or upgrade condition:
- candidate for formal SOP: `yes / no`
```

---

## SOP Feedback And Upgrade Candidates

Current state:

- confirmed SOP gaps: none
- candidate upgrade items: none

Suggested fields:

1. issue description
2. exposure scenario
3. current temporary handling
4. whether it has cross-project value

---

## Conclusion

This file records only two things:

1. current-project flow deltas
2. runtime-exposed SOP upgrade candidates
