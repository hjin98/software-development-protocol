---
name: software-verification
description: Independently verify a completed software candidate against its Protocol v3 workplan and qualification evidence. Use for branch/PR/diff conformance review, scientific/numerical/API/persistence/configuration/security/resource checks, evidence sufficiency, performance-claim scrutiny, release/documentation parity, scope-creep review, reopening gates, and final `MERGE_READY` / `NOT_READY` / `DESIGN_REVISION_REQUIRED` decisions. Do not repair substantial product source while reviewing.
---

# Software Verification

Use this skill as the **independent acceptance authority** of Software Development Protocol v3.

Verification answers:

> Does the exact candidate plus its executed evidence satisfy the frozen design and deserve acceptance?

## 1. Resolve exact identity

Read:

- `references/workplans-and-agent-handoff.md`
- `references/protocol-versioning-and-compatibility.md`
- governing workplan;
- exact candidate source/PR/diff;
- all mandatory Qualification Handoffs/Reports/evidence.

Establish:

```text
protocol_version
workplan_id/revision/SHA-256
candidate source commit
qualification handoff/report digests
```

Reject evidence bound to another source unless explicit dependency analysis justifies reuse.

For legacy completed v2 work, apply the compatibility rules rather than rewriting history.

## 2. Review implementation conformance

Check:

- frozen algorithm/architecture;
- scientific/numerical semantics and tolerances;
- API/data/configuration behavior;
- persistence/schema/recovery compatibility;
- deterministic/fallback/error behavior;
- concurrency/cancellation/retry/idempotency;
- resource/performance/storage scaling implications;
- security/trust boundaries;
- unexpected scope/dependency growth.

Do not treat implementation-local convenience as authority over the workplan.

## 3. Review evidence sufficiency

Read `references/testing-and-qualification.md`.

Verify that each mandatory acceptance claim is supported by an actually executed check at the required capability/environment.

Distinguish:

```text
PASS
FAIL
BLOCKED
NOT RUN
DEFERRED
```

Check benchmark comparability, source/environment identity, restart semantics, backend qualification, clean-install evidence, and production scale where required.

A Qualification Report is evidence, not self-validating authority.

## 4. Review candidate closeout

Read:

- `references/documentation-and-evidence.md`
- `references/release-and-distribution.md` when applicable
- `references/specification-and-implementation.md`

Verify the exact candidate already contains the release/current-state surfaces it claims to ship:

- specification-code parity;
- architecture only for actual accepted structural changes;
- correct history/changelog/version/release notes;
- generated Markdown/PDF/provenance parity;
- package/build/install contents;
- no temporary workplan/evidence leakage into runtime distribution.

Do not fix substantial product-source/doc defects during verification. Return them to implementation so the new source can be requalified as necessary.

## 5. Gate acceptance

Treat gate state as three-dimensional:

```text
implementation: PREPARED or BLOCKED
qualification: PASS/FAIL/BLOCKED/NOT_RUN/DEFERRED/NOT_REQUIRED
acceptance: PENDING/PASS/FAIL/BLOCKED
```

A gate may be implementation-prepared without being accepted.

Only verification may mark final acceptance PASS after all mandatory design and evidence requirements are satisfied.

## 6. Decision and routing

Use `templates/verification_report_template.md`.

Return exactly one final decision:

- `MERGE_READY` — no unresolved mandatory finding; candidate/evidence identities are coherent.
- `NOT_READY` — implementation/evidence/closeout correction is needed under the frozen design.
- `DESIGN_REVISION_REQUIRED` — acceptance would require changing a frozen design decision/invariant/threshold.

For `NOT_READY`, route concrete corrections to `software-implementation`.
For design contradiction, route the exact decision to `software-design`.

Verification may update coordination/evidence status (verification report, workplan lifecycle/archive) after acceptance, but does not repair substantial product source while reviewing.

## 7. Workplan completion

A substantial workplan becomes `COMPLETE` only after:

- mandatory qualification is PASS;
- verification is `MERGE_READY`;
- candidate closeout is coherent;
- final evidence binds source/workplan/protocol identities.

Archive/delete the completed coordination artifact according to repository policy.

## Completion report

Report blockers/high/non-blocking findings, gate acceptance, evidence limitations, exact candidate SHA, and final decision.
