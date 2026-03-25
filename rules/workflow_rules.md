# Workflow Rules

- **Version**: `v2.0`
- **Status**: official rule
- **Role**: fixes the default execution order of the SOP workflow

---

## Default Order

1. align the current `project` and `phase`
2. define the current `plan item` or `task` goal
3. define in-scope and out-of-scope
4. define completion and validation
5. execute the minimum closed loop
6. run validation or review
7. return the result to the owning `plan`
8. let `plan` or `phase` decide the next step
9. check writeback for facts, rules, SOP, standards, and skills

## Rules

1. do not start implementation before goal, boundary, and validation are clear
2. do not auto-start the next task after finishing one task
3. if this order no longer fits the real problem, enter recovery or process-improvement handling explicitly
