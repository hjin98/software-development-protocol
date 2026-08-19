---
kind: implementation-workplan
workplan_id: REPLACE_ME
plan_revision: 1
status: DRAFT
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
analysis_base_ref: REPLACE_ME
analysis_base_commit: REPLACE_ME
assumption_paths: []
architecture_refs: []
spec_refs: []
expected_change_paths: []
default_gate_approval: AUTO
---

# <Task> Implementation Workplan

## Objective

<One concise outcome statement.>

## Current diagnosis

<Evidence-grounded root cause/current limitation.>

## Current authority references

- Architecture: ...
- Specifications: ...
- Source/tests/evidence: ...

## Frozen design decisions

- ...

## Invariants and acceptance semantics

- ...

## Expected change surface

- Source: ...
- Tests: ...
- Candidate specs/docs/release: ...
- Benchmarks/audits: ...

## Non-goals

- ...

## Execution and resource constraints

- ...

## Qualification capabilities

Use only capabilities actually required by this workplan:

- `SOURCE`
- `LOCAL_LIGHT`
- `TARGET_RUNTIME`
- `PRODUCTION_DATA`
- `TARGET_HARDWARE`
- `EXTERNAL_ACTION`

## Gate summary

| Gate | Approval | Implementation | Qualification | Acceptance | Barrier | Purpose |
|---|---|---|---|---|---|---|
| G0 | AUTO | PENDING | NOT_RUN | PENDING | no | ... |

## G0 — <name>

**Approval:** AUTO  
**Qualification barrier:** no

**Goal:** ...

**Prerequisites:** ...

**Work:**
- ...

**Acceptance:**
- ...

**Qualification:**
- Capability: `LOCAL_LIGHT`
- Required check/evidence: ...

**Evidence:**
- ...

**Fallback/rollback:** ...

**Excluded/deferred:** ...

## Design-revision triggers

Stop and report `DESIGN_REVISION_REQUIRED` if implementation would require changing:

- ...

## Final candidate closeout

Before qualification of a release-significant final candidate:

- [ ] Candidate current specifications match the candidate code.
- [ ] Candidate architecture is updated only for actual target architectural changes.
- [ ] Candidate history/changelog/version/release metadata is staged according to repository policy.
- [ ] Required generated permanent docs/artifacts are staged or their target-environment build is declared in the Qualification Handoff.

## Final acceptance closeout

- [ ] All mandatory qualification checks PASS.
- [ ] Verification report is `MERGE_READY`.
- [ ] Final evidence records `workplan_id`, `plan_revision`, `workplan_sha256`, source commit, and protocol version.
- [ ] Workplan is marked/archived only after acceptance.
