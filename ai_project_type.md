# Project Type Registry

- **Version**: `v2.0`
- **Status**: official
- **Role**: defines supported `project_type` values only

---

## Purpose

This file is the registry for valid `project_type` values.
It answers only:

1. which values are supported
2. what each value means
3. which entry contract each value should follow by default

It does not define:

- how project type is selected
- where project type is written back
- which file is authoritative in a concrete project instance

Those responsibilities belong to:

- `AGENTS.md` for the SOP engine source repository
- `project_entry.md` for injected host projects

---

## Supported Values

### `sop_develop`

Meaning:

- the repository primarily designs, revises, or maintains the SOP itself
- the repository works on rules, templates, facts, skills, and governance evolution

Default entry contract:

- use `AGENTS.md`
- continue into `ai_project_sop.md`

### `common`

Meaning:

- the repository is a normal product or engineering project using this SOP for execution

Default entry contract:

- use `project_entry.md`
- use `ai_project_quickstart.md` as the low-token runtime contract

Initialization note:

- for a newly injected project, `ai_sop_init.bat` initializes the host project directly as `common`

---

## Extension Rule

When adding a new `project_type`, add:

1. the type name
2. its meaning
3. its default entry contract
4. typical examples
5. any extra runtime requirements

---

## Conclusion

This file is a registry, not an instance-state protocol.
