---
kind: verification-report
report_id: REPLACE_ME
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
workplan_id: REPLACE_ME
plan_revision: REPLACE_ME
workplan_sha256: REPLACE_ME
source_commit: REPLACE_ME
decision: NOT_READY
---

# Verification Report

## Reviewed evidence

- Implementation Workplan:
- Candidate source/diff:
- Qualification Handoff/report digest(s):
- Architecture/specification/release surfaces:

## Gate acceptance

| Gate | Implementation | Qualification | Acceptance | Evidence |
|---|---|---|---|---|
| G0 | PREPARED | PASS | PASS | ... |

## Findings

### Blocking

- ...

### Non-blocking

- ...

## Decision

One of:

```text
MERGE_READY
NOT_READY
DESIGN_REVISION_REQUIRED
```

For `NOT_READY`, route each mandatory correction to `software-implementation` unless the correction changes frozen design. For `DESIGN_REVISION_REQUIRED`, identify the exact frozen decision/invariant requiring `software-design`.

Verification does not repair substantial product source while reviewing.
