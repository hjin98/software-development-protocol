---
kind: verification-report
report_id: REPLACE_ME
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
workplan_id: REPLACE_ME
plan_revision: REPLACE_ME
workplan_sha256: REPLACE_ME
candidate_commit: REPLACE_ME
candidate_content_identity: REPLACE_ME
candidate_identity_policy: REPLACE_ME
decision: NOT_READY
---

# Verification Report

## Reviewed identity

- Implementation Workplan/digest:
- Candidate commit provenance:
- Candidate content identity/policy:
- Candidate diff/product surfaces:
- Qualification Handoff/report digest(s):
- Architecture/specification/release surfaces:
- Evidence-only/coordination commits after candidate commit:

## Independence

```yaml
independence:
  verifier_context: fresh | shared | unknown
  implementation_actor_same: true | false | unknown
  qualification_actor_same: true | false | unknown
```

State any project policy requiring stronger independence and whether it was met.

## Candidate/evidence identity review

- Current candidate content identity equals qualified identity: ...
- Later commits change only declared evidence/coordination surfaces: ...
- Dirty/untracked/source-origin qualification evidence sufficient: ...
- Any reused qualification evidence has explicit dependency justification: ...

## Gate acceptance

| Gate | Implementation | Qualification | Acceptance | Deferred-current-blocking? | Evidence |
|---|---|---|---|---|---|
| G0 | PREPARED | PASS | PASS | no | ... |

A blocking deferred/not-run/failed/blocked mandatory check cannot yield acceptance PASS.

## Evidence reuse audit

For every reused expensive check:

- prior evidence identity:
- dependency set:
- candidate/config/input/environment deltas:
- reuse decision and rationale:

Ambiguous dependency => reject reuse and require rerun.

## Findings

### Blocking

- ...

### High/non-blocking

- ...

## Decision

One of:

```text
MERGE_READY
NOT_READY
DESIGN_REVISION_REQUIRED
```

`MERGE_READY` requires that the exact candidate content identity is supported by complete mandatory qualification and coherent candidate closeout, even if later evidence-only commits changed Git HEAD.

For `NOT_READY`, route mandatory corrections to `software-implementation` unless they change frozen design. For `DESIGN_REVISION_REQUIRED`, identify the exact frozen decision/invariant requiring `software-design`.

Verification does not repair substantial product source while reviewing.
