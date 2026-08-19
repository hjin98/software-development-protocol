---
kind: qualification-handoff
handoff_id: REPLACE_ME
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
workplan_id: REPLACE_ME
candidate_commit: REPLACE_ME
status: PREPARED_FOR_QUALIFICATION
---

# Qualification Run Card

Use this artifact only when execution crosses a real environment boundary.

## Objective

<What must be demonstrated.>

## Material candidate/inputs/environment

- Candidate commit/source: ...
- Dataset/input: ...
- Configuration semantics: ...
- Backend/hardware/resource conditions when material: ...

## Checks

### Q1 — <name>

- Acceptance requirement: ...
- Expected result/threshold: ...
- Suggested command/method: ...
- Material constraints that must not change: ...

Equivalent cwd, activation, quoting, scratch/log paths, and unambiguous path corrections are operationally flexible unless explicitly material.

## Forbidden material changes

Do not change product code, scientific/dataset/config/backend semantics, material resource policy, or acceptance thresholds to obtain PASS.

## Routing

- Product/material failure -> `RETURN_TO_IMPLEMENTATION`
- Frozen target contradiction -> `DESIGN_REVISION_REQUIRED`
- Missing required environment/input -> `BLOCKED`
- Harness/report defect -> correct locally, record actual execution, continue
