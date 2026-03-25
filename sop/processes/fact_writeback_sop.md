# Fact Writeback SOP

- **Version**: `v2.0`
- **Status**: official
- **Role**: defines how stable conclusions are promoted into formal facts

---

## Purpose

This SOP answers:

1. when a conclusion is stable enough to become a fact
2. where that fact should be written
3. how to avoid promoting temporary execution noise into long-term knowledge

---

## Basic Rule

A conclusion should be written back as a fact only when it is:

1. confirmed
2. stable enough to matter beyond the current step
3. likely to affect future judgment or future execution

---

## Writeback Order

1. decide whether the conclusion is truly stable
2. route it using `standards/document_routing_matrix.md`
3. if it is a fact, write it into the correct `facts/*` document
4. update `facts/facts_index.md`
5. if runtime source documents changed, co-update `runtime/session_brief.md` in the same turn

---

## Do Not Promote

Do not promote these into facts:

- one-off temporary plans
- raw process chatter
- implementation noise
- unstable hypotheses
- current-only urgency notes

---

## Conclusion

Write back only stable conclusions that will keep helping future judgment.
Everything else should stay in execution-layer records or temporary notes.
