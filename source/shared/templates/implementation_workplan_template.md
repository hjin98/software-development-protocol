---
kind: implementation-workplan
workplan_id: REPLACE_ME
plan_revision: 1
status: DRAFT
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
analysis_base_commit: REPLACE_ME
---

# <Task> Implementation Workplan

## Objective

<One concise outcome.>

## Diagnosis

<Evidence-grounded root cause/current limitation.>

## Frozen material design

- ...

## Acceptance-critical requirements

- A1. ...
- A2. ...

Write these in product/domain or material-execution language. Do not make administrative provenance fields, optional telemetry, or secondary diagnostics acceptance criteria unless they protect a concrete material boundary.

## Expected change surface / non-goals

- Change: ...
- Non-goal: ...

## Material execution constraints

- Production workload versus smallest materially sufficient validation workload: ...
- Resource/performance requirement when material: ...
- Full-production-scale qualification justification, if genuinely required: ...

## Gates

| Gate | Status | Purpose |
|---|---|---|
| G0 | PENDING | ... |

Use only `PENDING | PREPARED | PASS | FAIL | BLOCKED`.

## External qualification needs

<List workstation/HPC/production/external checks only when genuinely required. For expensive checks, prefer an autonomous resource-bounded qualifier that adapts to the target machine rather than freezing one machine's numerical limits here.>

## Design-revision triggers

Return to design only for material target/acceptance/scope contradictions, not command/path/report corrections, optional diagnostics, or safe adaptive benchmark sizing within frozen semantics.
