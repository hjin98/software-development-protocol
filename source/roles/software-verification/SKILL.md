---
name: software-verification
description: Independently verify a completed software candidate against its Protocol v3 workplan and qualification evidence. Use for branch/PR/diff conformance review, scientific/numerical/API/persistence/configuration/security/resource checks, evidence sufficiency and reuse audits, performance-claim scrutiny, release/documentation parity, scope-creep review, reopening gates, and final `MERGE_READY` / `NOT_READY` / `DESIGN_REVISION_REQUIRED` decisions. Do not repair substantial product source while reviewing.
---

# Software Verification

Use this skill as the **independent acceptance authority** of Software Development Protocol v3.

Verification answers:

> Does the exact candidate content plus executed evidence satisfy the frozen design and deserve acceptance?

## 1. Resolve exact identity

Read:

- `references/workplans-and-agent-handoff.md`;
- `references/protocol-versioning-and-compatibility.md`;
- governing workplan;
- exact candidate source/PR/diff;
- all mandatory Qualification Handoffs/Reports/evidence.

Establish:

```text
protocol_version
workplan_id/revision/SHA-256
candidate_commit provenance
candidate_content_identity
candidate_identity_policy
qualification handoff/report digests
```

Later evidence/coordination commits may change Git HEAD without changing the qualified candidate content identity. Verify those commits touch only declared excluded evidence/coordination surfaces.

For legacy completed v2 work, apply compatibility rules rather than rewriting history.

## 2. Review implementation conformance

Check frozen algorithm/architecture, scientific/numerical semantics, API/data/configuration behavior, persistence/schema/recovery compatibility, deterministic/fallback/error behavior, concurrency/cancellation/retry/idempotency, resource/performance/storage implications, security/trust boundaries, and unexpected scope/dependency growth.

Do not treat implementation convenience as authority over the workplan.

## 3. Review evidence sufficiency and identity

Read `references/testing-and-qualification.md`.

Verify each mandatory acceptance claim is supported by an actually executed check at the required capability/environment and that qualification pre/postflight established an unambiguous candidate:

- candidate content identity matched before and after execution;
- tracked/staged candidate surfaces were clean;
- undeclared untracked/shadowing execution source was absent or explicitly controlled;
- import/source origins were appropriate where material;
- tracked candidate outputs were not mutated during qualification.

Distinguish `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`, and `DEFERRED` honestly.

A Qualification Report is evidence, not self-validating authority.

## 4. Audit evidence reuse

For every reused qualification result, inspect:

- prior evidence identity;
- declared source/config/input/environment/upstream dependencies;
- candidate/config/input/environment deltas;
- implementation's invalidation/reuse decision.

Ambiguous dependency is not reusable evidence. Require rerun when dependency coverage is insufficient.

## 5. Review retry history

Confirm retries stayed within the declared `NONE | IDENTICAL_RETRY | CLEAN_RETRY | RESUME_RETRY` policy.

A policy-changing retry, undeclared cache cleanup, backend change, dataset reduction, changed resource/scientific configuration, or candidate mutation cannot be accepted as the same qualification attempt.

## 6. Review candidate closeout

Read `references/documentation-and-evidence.md`, `references/specification-and-implementation.md`, and `references/release-and-distribution.md` when applicable.

Verify the candidate content identity includes all product/release surfaces it claims to ship: specifications, architecture changes, history/version/release metadata, package/build state, and tracked generated product artifacts.

Do not fix substantial candidate defects during verification. Return them to implementation so a new candidate can be requalified as necessary.

## 7. Gate acceptance and derived lifecycle

Treat gate state as three-dimensional:

```text
implementation: PENDING/IN_PROGRESS/PREPARED/BLOCKED
qualification: NOT_REQUIRED/NOT_RUN/PASS/FAIL/BLOCKED/DEFERRED
acceptance: PENDING/PASS/FAIL/BLOCKED
```

For deferred checks, inspect `mandatory_for_current_acceptance` and `deferred_to`.

A mandatory blocking `DEFERRED`, `NOT RUN`, `FAIL`, or `BLOCKED` check cannot yield acceptance PASS or `READY_FOR_VERIFICATION`/`MERGE_READY`.

Verify workplan-level lifecycle status is consistent with gate states rather than merely trusting the label.

## 8. Independence metadata

Use `templates/verification_report_template.md` and record:

```yaml
independence:
  verifier_context: fresh | shared | unknown
  implementation_actor_same: true|false|unknown
  qualification_actor_same: true|false|unknown
```

Fresh verification context is preferred for substantial scientific/security/release-significant work and may be required by project policy. Do not imply independence that did not exist.

## 9. Decision and routing

Return exactly one final decision:

- `MERGE_READY` — no unresolved mandatory finding; candidate content/evidence identities are coherent.
- `NOT_READY` — implementation/evidence/closeout correction is needed under frozen design.
- `DESIGN_REVISION_REQUIRED` — acceptance requires changing frozen design/invariant/threshold.

For `NOT_READY`, route corrections to `software-implementation`. For design contradiction, route the exact decision to `software-design`.

Verification may update coordination/evidence status after acceptance, but does not repair substantial product source while reviewing.

## 10. Workplan completion

A substantial workplan becomes `COMPLETE` only after mandatory qualification for current acceptance is PASS, verification is `MERGE_READY`, candidate closeout is coherent, and final evidence binds candidate/workplan/protocol identities.

Evidence-only coordination commits after qualification do not require full requalification when they preserve candidate content identity under the declared policy.

## Completion report

Report blocking/high/non-blocking findings, gate acceptance, evidence reuse decisions, identity limitations, independence metadata, exact candidate content identity/commit provenance, and final decision.
