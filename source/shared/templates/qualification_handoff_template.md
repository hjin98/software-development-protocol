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

## Resource-bounded execution

For potentially expensive checks describe only what is material:

- smallest materially sufficient representative workload or calibration rule: ...
- effective-resource discovery / explicit project or user caps: ...
- hard safety containment: ...
- planned operating-envelope/adaptation rule: ...
- full-production-scale justification, if required: ...
- owned scratch/evidence separation and cleanup/scavenging behavior: ...
- autonomous/restart behavior when execution is nontrivial: ...

Do not freeze universal machine numbers when the qualifier can safely discover and adapt to the target allocation.

## Checks

### Q1 — <name>

- Acceptance requirement: ...
- Expected result/threshold: ...
- Suggested command/method: ...
- Material constraints that must not change: ...

Equivalent cwd, activation, quoting, scratch/log paths, safe representative sizing, and unambiguous path corrections are operationally flexible unless explicitly material.

Optional telemetry/secondary diagnostics are advisory unless required to execute safely or interpret the material claim.

## Forbidden material changes

Do not change product code, scientific/dataset/config/backend semantics, workload representativeness, material product resource policy, or acceptance thresholds to obtain PASS.

## Routing

- Product/material failure -> `RETURN_TO_IMPLEMENTATION`
- Frozen target contradiction -> `DESIGN_REVISION_REQUIRED`
- Minimum materially sufficient check cannot execute safely / required environment unavailable -> `BLOCKED`
- Harness/resource-model/report/secondary diagnostic defect -> correct, resize, degrade, record, or skip as appropriate and continue
