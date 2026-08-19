---
name: software-implementation
description: Implement a specified software change, especially from an approved Protocol v3 Implementation Workplan. Use for code edits, bounded refactoring within frozen design, test/oracle/property construction, benchmark/instrumentation harnesses, persistence/storage/recovery implementation, concurrency/resource/security hardening, candidate specification/documentation/version/release closeout, and preparation of a source-bound Qualification Handoff. Run cheap/available checks, but do not claim target-environment qualification that was not executed. Escalate frozen-design contradictions rather than redesigning.
---

# Software Implementation

Use this skill as the **implementation authority** of Software Development Protocol v3.

The normal output for substantial work is a candidate source revision plus a **Qualification Handoff**, not a self-declared final acceptance.

## 1. Bounded workplan preflight

Read:

- the complete governing workplan;
- `references/workplans-and-agent-handoff.md`;
- `references/protocol-versioning-and-compatibility.md`;
- repository/project/Git instructions.

Require `READY_FOR_IMPLEMENTATION` or explicitly resumable `IN_PROGRESS`.

Record:

```text
workplan_id
plan_revision
workplan_sha256
protocol_version
analysis_base_commit
current HEAD
```

Perform bounded stale-plan revalidation only across assumption paths/current authority/target interfaces. Do not repeat repository-wide design merely because HEAD advanced.

If assumptions materially changed, return `BLOCKED: STALE_WORKPLAN`.

## 2. Respect frozen design

You own local implementation details such as helpers, internal naming, bounded refactors, test fixtures, vectorization mechanics, instrumentation, and equivalent implementation techniques.

Return `DESIGN_REVISION_REQUIRED` rather than changing:

- scientific/numerical semantics;
- chosen algorithm/architectural ownership;
- public/API/data/configuration target semantics;
- persistence/schema/recovery architecture;
- trust/security model;
- mandatory resource/acceptance thresholds;
- material non-goals.

## 3. Implement efficiently across gates

Default gates are `AUTO`.

For each gate:

1. implement the smallest coherent capability;
2. preserve required compatibility/fallback/oracle paths;
3. author focused regression/boundary/property tests;
4. run structural and light checks available in the current environment;
5. record check status honestly;
6. prepare later independent gates when the workplan permits batching.

A mandatory target-environment check being `NOT RUN` does **not** make the gate PASS. It may leave the gate implementation `PREPARED` while qualification remains pending.

Do not cross a gate with `qualification_barrier: yes` until its mandatory qualification has passed.

## 4. Validation available to implementation

Read `references/testing-and-qualification.md`.

Implementation should normally execute what is cheap and available:

```text
structural sanity
-> focused unit/regression
-> local oracle/property checks
-> local consumer/integration checks
```

Author but do not fabricate results for:

```text
TARGET_RUNTIME
PRODUCTION_DATA
TARGET_HARDWARE
EXTERNAL_ACTION
```

when unavailable.

Reuse authenticated baselines where the workplan permits and their identity remains applicable.

## 5. Candidate closeout before target qualification

For release-significant final candidates, stage the exact source state that qualification should test:

- candidate specification-code parity;
- candidate architecture changes only where target architecture changed;
- candidate history/changelog/version/release metadata;
- required generated permanent docs/artifacts when buildable locally;
- packaging/build changes and tests.

These candidate documents are not accepted current authority merely because they exist on the feature branch. Verification decides whether the candidate may be accepted/merged.

Avoid post-qualification candidate mutations that would invalidate evidence.

## 6. Prepare the Qualification Handoff

Use `templates/qualification_handoff_template.md`.

Bind:

```text
protocol_version
workplan_id/revision/SHA-256
source ref/commit
implemented/prepared gates
required capability per check
exact command and working directory
environment/data/hardware prerequisites
expected result
evidence/output paths
allowed retries/side effects
allowed write paths
```

Default `product_source_mutation: FORBIDDEN`.

Batch independent expensive checks into the smallest target-environment session consistent with fault isolation.

Do not hand the qualification role a broad instruction such as “finish the workplan.” Give it the exact remaining execution contract.

## 7. Qualification failures returning to implementation

When qualification returns `RETURN_TO_IMPLEMENTATION`:

- consume the exact failing command/log/environment/source identity;
- diagnose the smallest implementation defect;
- patch source/tests/handoff;
- invalidate only evidence affected by the source delta;
- issue a new source-bound Qualification Handoff.

If resolution requires changing frozen design, route to `software-design`.

## 8. Workplan status

Typical substantial lifecycle:

```text
READY_FOR_IMPLEMENTATION
-> IN_PROGRESS
-> PREPARED_FOR_QUALIFICATION
```

Do not mark the workplan `COMPLETE`; final acceptance belongs to verification after mandatory qualification.

## Completion report

Report:

- workplan identity/digest consumed;
- source commit produced;
- gates implementation-prepared vs blocked;
- local checks actually run;
- mandatory qualification still pending;
- candidate docs/release surfaces staged;
- Qualification Handoff path/digest;
- repository branch/worktree state.
