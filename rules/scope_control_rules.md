# Scope Control Rules

- **Version**: `v2.0`
- **Status**: official rule
- **Role**: prevents silent scope expansion during execution

---

## Default Rules

1. every concrete task must have explicit non-goals
2. if a request exceeds the current phase, plan, or task boundary, do not absorb it silently
3. phase-level changes must go through phase control, not task-level improvisation
4. long-term goal changes belong to `project_charter`, not to ad-hoc execution notes
5. if scope drift is discovered, correct it before continuing deeper execution
