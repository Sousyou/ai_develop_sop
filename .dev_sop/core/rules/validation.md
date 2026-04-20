# Core Validation Rules

- Black-box validation is the default acceptance mechanism.
- Add white-box validation when logic is branch-heavy, stateful, regression-sensitive, or protected by an important internal contract.
- A deterministic bugfix regression path is a strong trigger for white-box protection.
- Validation must be concrete enough to review.
- Do not turn validation into a coverage-chasing workflow.
- Each task spec should name both the applicable project rules and the concrete validation gates that must pass.
- If validation exposes a missing policy, missing dependency choice, or broader-scope need, stop for `needs_decision` or `replan_required` instead of stretching the task.
