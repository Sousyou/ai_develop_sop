# CURRENT

## Current phase
Operate with the control surface rehomed into `.dev_sop/control/*` and keep the layout stable.

## Current target
Keep a recovery-first control surface inside `.dev_sop/` while preserving the spec-first execution model.

## Active slice
Use `.dev_sop/control/*` as the default recovery path and keep it small as later work lands.

## In scope now
- Keep `.dev_sop/control/CURRENT.md` as the recovery-first artifact
- Keep `.dev_sop/control/DOC_MAP.md` role-based and short
- Route durable reusable decisions and experiment takeaways to `.dev_sop/doc/facts/*`
- Maintain the supporting templates, worked example, and `session-closeout` workflow as lightweight sustaining assets
- Support optional batch-level release readiness without turning it into the default task path

## Out of scope now
- `reports/` or `archive/`
- Broad reporting, dashboard, or ADR systems
- turning `.dev_sop/control/*` into a project board or work log
- duplicating execution detail that already belongs in specs, facts, or skills

## Current source of truth
- `.dev_sop/control/DOC_MAP.md`
- `.dev_sop/VERSION.md`
- `AGENTS.md`
- `.dev_sop/doc/facts/project-scope.md` for stable scope and boundary context
- the current active task spec in `.dev_sop/doc/specs/*`, if implementation work is underway

## Frozen decisions
- `.dev_sop/control/` is the default recovery/control surface location.
- `.dev_sop/control/CURRENT.md` is the recovery-first artifact.
- `.dev_sop/control/` contains only `CURRENT.md` and `DOC_MAP.md`.
- `.dev_sop/VERSION.md` is the source of truth for the current Dev SOP version.
- The control surface stays intentionally narrow and does not become a broad documentation hub.
- Durable decision rationale and reusable experiment outcomes belong in facts rather than separate control ledgers.

## Latest experiment
None yet. Reusable experiment outcomes should be routed to facts; task-local runs stay in specs or change summaries.

## Next 3 actions
1. Keep `.dev_sop/control/CURRENT.md` and `.dev_sop/control/DOC_MAP.md` small as later changes land.
2. Use `session-closeout` when future slices may affect current state, decisions, experiments, facts, or skills.
3. Add new control-surface artifacts only when a repeated recovery problem appears.

## Risks to watch
- `.dev_sop/control/DOC_MAP.md` could grow into a duplicate navigation layer.
- `.dev_sop/control/CURRENT.md` could drift into a project board instead of staying recovery-focused.
- Entry wording could blur the boundary between project control and SOP execution assets.
- `.dev_sop/doc/facts/project-scope.md` could be treated like a live status file instead of a slower-moving scope fact.
