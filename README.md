# ai_develop_sop

> A structured SOP framework for AI-driven project development, governance, review, recovery, and knowledge writeback.

## Overview

`ai_develop_sop` is a documentation-first framework for building and governing AI-assisted engineering workflows.

It is designed to solve the real problems that appear when AI participates deeply in project work:

- scope drift
- execution losing the main line
- unstable task boundaries
- poor review and handoff quality
- facts not being written back
- difficult recovery after workflow instability

The framework is built around a four-layer model:

- **Decision Layer**: `project -> phase`
- **Execution Layer**: `plan -> task`

This separation is used to keep long-term goals, current-stage goals, execution orchestration, and minimal execution units clearly separated.

---

## Core Model

### `project`
Defines the final product goal, long-term boundaries, top-level constraints, and cross-phase stable facts.

### `phase`
Acts as the current stage controller. It defines stage goals, non-goals, delivery boundaries, and governs the lifecycle of the current `main plan`.

### `plan`
Acts as the execution orchestration layer under the current `phase`. It maintains the current main line, sequencing, ordering, and execution integration.

### `task`
Acts as the smallest controllable execution unit. It must have a single goal, explicit boundary, explicit validation, and explicit return-to-plan behavior.

---

## What This Repository Provides

This repository is not a prompt collection.

It is a complete SOP framework that includes:

- top-level workflow governance
- layer definitions
- transition rules
- execution templates
- initialization processes
- recovery processes
- fact writeback processes
- runtime supplements for real projects
- rules and standards systems
- skill accumulation structure

---

## Repository Structure

```text
.
├── ai_project_sop.md                 # Main project SOP entry
├── ai_runtime_sop.md                 # Runtime process supplement for real projects
├── ai_runtime_standards.md           # Runtime standards supplement for real projects
├── AGENTS.md                         # Project entry gate
│
├── sop/
│   ├── core/
│   │   ├── project_layer.md
│   │   ├── phase_layer.md
│   │   ├── plan_layer.md
│   │   ├── task_layer.md
│   │   └── workflow_transition_rules.md
│   │
│   ├── templates/
│   │   ├── phase_review_template.md
│   │   ├── next_phase_request_template.md
│   │   ├── plan_item_template.md
│   │   └── task_template.md
│   │
│   ├── design/
│   │   └── main_plan_state_design.md
│   │
│   └── processes/
│       ├── project_bootstrap_sop.md
│       ├── project_init_artifacts.md
│       ├── fact_writeback_sop.md
│       └── maintenance_recovery_sop.md
│
├── rules/                            # Execution guardrails
├── facts/                            # Stable facts and writeback layer
├── skills/                           # Skill policy / registry / template
└── standards/                        # Cross-project formal standards
