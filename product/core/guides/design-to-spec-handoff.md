# Design-To-Spec Handoff

Use this guide when design discussion, planning, spec derivation, and execution are handled by different models or different people.

This is a recommended extension of the default SOP, not a replacement for it.
The core rule still applies: when work is ready for implementation, the durable execution artifact should be one or more task specs.

## Role Contracts

### Design Partner
- discuss the high-level design
- clarify goals, non-goals, constraints, and risks
- produce a design summary when the discussion needs to be handed off
- do not implement from the design discussion alone

### Planner / Specifier
- combine the design input with actual repository context
- turn the current design into a clarified plan or phase slice
- decide when the work is implementation-ready
- derive one or more narrow task specs when implementation is ready
- bind each spec to the applicable project rules and validation gates

### Executor
- implement and validate one spec at a time
- stay within the current spec boundary
- report blockers, ambiguity, validation gaps, and escalation outcomes back to the planner / specifier
- do not expand scope or invent missing design

## Default Flow

1. Discuss the high-level design and summarize it if handoff is needed.
2. Let the planner / specifier inspect the repository and refine the plan or current phase slice.
3. When the work is implementation-ready, derive one or more narrow specs.
4. Hand one spec at a time to the executor.
5. Validate the completed work against the spec and project rules.
6. If boundaries change, repair is exhausted, or a decision boundary appears, return to the planner / specifier with `replan_required` or `needs_decision`.

## Example Mapping

This mapping is illustrative, not required:

- `Codex` can act as `design partner`, `planner / specifier`, or `executor`
- `Claude Code` can act as `design partner`, `planner / specifier`, or `executor`

Common pairings include:

- `Claude Code` for design discussion and `Codex` for repository-aware planning plus execution
- `Codex` for planning and `Claude Code` for execution from a finished spec

The important invariant is the role contract, not the fixed tool assignment.
