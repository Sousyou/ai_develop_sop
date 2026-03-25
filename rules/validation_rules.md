# Validation Rules

- **Version**: `v2.0`
- **Status**: official rule
- **Role**: requires explicit validation before a task is treated as complete

---

## Default Rules

1. define validation before execution
2. do not treat implementation as completion without a validation method
3. if validation cannot be run, state that explicitly
4. task closure should return a result, remaining gaps, and known risks
5. validation evidence should be stable enough to support writeback when needed
