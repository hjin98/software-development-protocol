---
kind: implementation-workplan
workplan_id: REPLACE_ME
plan_revision: 1
status: DRAFT
protocol_version: 2.0.1
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
- Specs/docs: ...
- Benchmarks/audits: ...

## Non-goals

- ...

## Execution and resource constraints

- ...

## Gate summary

| Gate | Approval | Status | Purpose | Evidence |
|---|---|---|---|---|
| G0 | AUTO | PENDING | ... | - |

## G0 — <name>

**Approval:** AUTO

**Goal:** ...

**Prerequisites:** ...

**Work:**
- ...

**Acceptance:**
- ...

**Evidence:**
- ...

**Fallback/rollback:** ...

**Excluded/deferred:** ...

## Design-revision triggers

Stop and report `DESIGN_REVISION_REQUIRED` if implementation would require changing:

- ...

## Final closeout

- [ ] Current specifications match accepted code.
- [ ] Architecture updated only for actual accepted architectural changes.
- [ ] History/changelog/version updated according to repository policy.
- [ ] Permanent Markdown docs regenerated/verified as PDF where required.
- [ ] Broad/release qualification completed or explicitly blocked/deferred.
- [ ] Final evidence records `workplan_id`, `plan_revision`, and `workplan_sha256`.
