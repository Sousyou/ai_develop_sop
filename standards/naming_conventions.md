# Naming Conventions Standard

- **Version**: `v2.0`
- **Status**: official standard
- **Role**: defines the cross-project naming baseline

---

## Goal

This standard unifies naming for:

1. files
2. directories
3. documents
4. layer objects

---

## Principles

1. semantic clarity first
2. consistency within the same layer first
3. stability first once a naming pattern becomes formal
4. avoid low-information abbreviations unless they are stable shared terms

---

## File And Directory Naming

Default style:

- lowercase English
- underscore-separated words: `_`

Examples:

- `ai_project_sop.md`
- `project_bootstrap_sop.md`
- `facts_index.md`
- `naming_conventions.md`

Do not mix styles casually within one document system.

---

## Document Naming Patterns

1. SOP process docs: `<subject>_sop.md`
2. template docs: `<subject>_template.md`
3. rules docs: `<subject>_rules.md`
4. standards docs: direct topical names such as `naming_conventions.md`
5. AI-owned entry docs may keep the `ai_` prefix

---

## Layer Object Naming

Formal layer objects use these names:

1. `project`
2. `phase`
3. `plan`
4. `task`

Derived objects extend them with qualifiers instead of replacing them, for example:

- `main plan`
- `sub plan`
- `plan item`
- `phase review`
- `next phase request`

---

## Upgrade Rule

If a project needs stricter naming rules, write them first into `ai_runtime_standards.md`.
Promote them into formal `standards/*` only after they are verified, clear, and reusable.
