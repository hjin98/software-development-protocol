---
name: software-implementation
description: Implement a specified software change, especially from an approved Protocol v3 Implementation Workplan. Use for code edits, bounded refactoring within frozen design, test/oracle/property construction, benchmark/instrumentation harnesses, persistence/storage/recovery implementation, concurrency/resource/security hardening, candidate specification/documentation/version/release closeout, candidate-content identity preparation, and creation of a source-bound Qualification Handoff. Run cheap/available checks, but do not claim target-environment qualification that was not executed. Escalate frozen-design contradictions rather than redesigning.
---

# Software Implementation

Use this skill as the **implementation authority** of Software Development Protocol v3.

The normal output for substantial work is a prepared candidate plus a **Qualification Handoff**, not a self-declared final acceptance.

## 1. Bounded workplan preflight

Read the complete governing workplan, `references/workplans-and-agent-handoff.md`, `references/protocol-versioning-and-compatibility.md`, and repository/project/Git instructions.

Require `READY_FOR_IMPLEMENTATION` or explicitly resumable `IN_PROGRESS`.

Record workplan ID/revision/SHA-256, protocol version, analyzed base, and current HEAD. Perform bounded stale-plan revalidation only across assumption paths/current authority/target interfaces. If assumptions materially changed, return `BLOCKED: STALE_WORKPLAN`.

## 2. Respect frozen design

You own local implementation details such as helpers, internal naming, bounded refactors, test fixtures, vectorization mechanics, instrumentation, and equivalent implementation techniques.

Return `DESIGN_REVISION_REQUIRED` rather than changing scientific/numerical semantics, chosen architecture, public/API/data/config target semantics, persistence/schema/recovery architecture, trust model, mandatory thresholds, or material non-goals.

## 3. Implement efficiently across gates

Default gates are `AUTO`.

For each gate:

1. implement the smallest coherent capability;
2. preserve required compatibility/fallback/oracle paths;
3. author focused regression/boundary/property tests;
4. run structural/light checks available in the current environment;
5. record check status honestly;
6. prepare later independent gates when barriers allow.

A mandatory target-environment check being `NOT RUN` does not make the gate PASS. It may leave implementation `PREPARED` while qualification remains pending.

Do not cross `qualification_barrier: yes` until mandatory qualification for that barrier passes.

## 4. Validation available to implementation

Read `references/testing-and-qualification.md`.

Normally execute what is cheap/available:

```text
structural sanity
-> focused unit/regression
-> local oracle/property checks
-> local consumer/integration checks
```

Author but do not fabricate results for unavailable `TARGET_RUNTIME`, `PRODUCTION_DATA`, `TARGET_HARDWARE`, or `EXTERNAL_ACTION` checks.

## 5. Freeze the candidate identity before handoff

Read `references/protocol-versioning-and-compatibility.md`.

Before qualification, establish:

```text
candidate_ref
candidate_commit
candidate_content_identity
candidate_identity_policy
```

The policy must include all product-relevant source/tests/spec/package/build/config/schema/tracked generated product surfaces and exclude only declared evidence/coordination-only paths.

Do not exclude a file that can affect build, runtime, scientific result, packaging, policy, or shipped product merely to avoid requalification.

Ensure the qualification starting state can be proven clean: no staged/tracked candidate changes and no undeclared untracked/shadowing source expected to affect execution.

## 6. Candidate closeout before target qualification

For release-significant final candidates, stage the exact source state qualification should test:

- candidate specification-code parity;
- architecture changes only where target architecture changed;
- history/changelog/version/release metadata;
- package/build state;
- tracked generated product artifacts.

Tracked candidate outputs must be created/committed **before** qualification. If target environment is required to generate one, qualification may produce only a proposed ephemeral artifact; adopt it here, commit a new candidate, and requalify affected checks.

## 7. Prepare the Qualification Handoff

Use `templates/qualification_handoff_template.md`.

Bind protocol/workplan identity, candidate ref/commit/content identity/policy, prepared gates, capabilities, exact command/cwd, environment/input prerequisites, expected result, evidence paths, output class/write paths, evidence dependencies, and retry policy.

Default:

```text
product_source_mutation: FORBIDDEN
```

Batch independent expensive checks into the smallest target-environment session consistent with fault isolation.

Do not give qualification a broad instruction such as "finish the workplan".

## 8. Evidence dependencies and invalidation

For each expensive check, declare source/config/input/environment/upstream dependencies sufficiently to evaluate reuse after a correction.

When candidate content changes:

1. preserve old evidence as historical evidence for the old candidate;
2. compute the changed candidate/config/input/environment dimensions;
3. invalidate every check whose dependency set intersects the change;
4. if dependency is ambiguous, invalidate by default;
5. issue a new candidate-bound handoff for required reruns.

Verification audits nontrivial reuse decisions.

## 9. Qualification failures returning to implementation

When qualification returns `RETURN_TO_IMPLEMENTATION`:

- consume the exact failing command/log/environment/candidate identity;
- diagnose the smallest implementation defect;
- patch candidate/tests/handoff;
- recompute candidate content identity;
- invalidate affected evidence only when dependencies justify reuse of the rest;
- issue a new Qualification Handoff.

If resolution changes frozen design, route to `software-design`.

## 10. Retry policy ownership

Implementation may select among workplan-permitted retry mechanics when they do not change frozen semantics:

- `NONE`
- `IDENTICAL_RETRY`
- `CLEAN_RETRY`
- `RESUME_RETRY`

Specify allowed cleanup/resume state. A change to scientific/config/resource/backend/dataset policy or candidate content is a new handoff/design decision, not a retry.

## 11. Workplan status

Typical substantial lifecycle:

```text
READY_FOR_IMPLEMENTATION
-> IN_PROGRESS
-> PREPARED_FOR_QUALIFICATION
```

Treat workplan-level status as derived from actual gate states where structured. Do not mark `READY_FOR_VERIFICATION` while any current mandatory qualification is `NOT RUN`, `FAIL`, `BLOCKED`, or blocking `DEFERRED`.

Do not mark the workplan `COMPLETE`; final acceptance belongs to verification.

## Completion report

Report workplan identity/digest, candidate commit/content identity/policy, gates prepared vs blocked, local checks actually run, mandatory qualification pending, candidate closeout surfaces staged, evidence dependency/retry declarations, Qualification Handoff path/digest, and repository branch/worktree state.
