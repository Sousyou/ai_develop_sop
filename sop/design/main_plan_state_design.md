# Main Plan State Design

- **Version**: `v2.0`
- **Status**: design note
- **Role**: describes a practical state model for `main plan`

---

## Purpose

This file gives a compact state model for the active `main plan` so plan status stays readable and cheap to maintain.

---

## Recommended Main Plan Fields

- `plan id`
- `parent phase`
- `plan status`
- `goal`
- `non-goals`
- `ordered plan items`
- `current item`
- `known blockers`
- `next review trigger`

---

## Recommended Plan Statuses

- `draft`
- `ready`
- `in_progress`
- `blocked`
- `review_pending`
- `completed`
- `cancelled`
- `replaced`

---

## Design Rules

1. there should be one clearly active main plan per current phase
2. plan status should make blockage and review visible
3. plan items should be ordered and stateful
4. the plan should stay compact enough to re-read cheaply
5. deep execution detail belongs in tasks, not in the plan state itself
