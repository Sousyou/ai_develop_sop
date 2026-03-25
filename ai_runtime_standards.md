# AI Runtime Standards

- **Version**: `v2.0`
- **Status**: official runtime standards supplement
- **Role**: records project-specific hard standards added on top of formal standards
- **Scope**: only non-`sop_develop` projects

---

## Purpose

This file answers:

1. which hard standards must take effect immediately in the current project
2. which formal standards are inherited by default
3. which standard gaps or upgrade candidates were exposed in runtime

---

## Usage Principles

1. inherit formal `standards/*` first, then add project-only stricter standards
2. record standard content only, not process flow
3. items written here take effect immediately in the current project
4. this file may tighten the baseline, but must not relax formal standards
5. on conflict, follow: host `AGENTS.md` -> `project_entry.md` -> `standards/*` -> this file

---

## Formal Standards Inherited By Default

Current baseline:

1. `standards/standards_index.md`
2. `standards/naming_conventions.md`
3. `standards/path_conventions.md`
4. `standards/document_writing_conventions.md`
5. `standards/document_routing_matrix.md`

---

## Allowed Content

This file may record current-project hard constraints such as:

- stricter naming or path rules
- stricter structure or interface contracts
- project-specific directory or artifact boundaries

---

## Forbidden Content

Do not write these here:

- process flow or review order
- current phase plans or task lists
- stable facts or product status summaries
- long-term goals or current targets
- product docs

Route them instead to:

- `ai_runtime_sop.md`
- `facts/*`
- `runtime/project_charter.md`
- `runtime/current_target.md`
- product docs

---

## Runtime Standard Deltas

Current state:

- none

Recommended format:

```md
### <standard_name>

- content:
- effective scope:
- source: `runtime-only` / `derived-from-standards/...`
- candidate for upgrade: `yes / no`
```

---

## Standard Feedback And Upgrade Candidates

Current state:

- none

Promote a runtime standard only when it is:

1. stable in the current project
2. clear in boundary
3. reusable across projects
4. suitable for formal review into `standards/*`

---

## Conclusion

This file records only:

1. current-project hard standard deltas
2. runtime-exposed standard upgrade candidates
