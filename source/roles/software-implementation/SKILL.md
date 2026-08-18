---
name: software-implementation
description: Implement and qualify a specified software change, especially from an approved Implementation Workplan. Use for code edits, refactoring within a frozen design, focused tests, correctness/oracle checks, performance benchmarking, CPU/GPU/concurrency/resource implementation, persistence/storage/recovery work, security hardening, specification/documentation/version closeout, and clean-install/release qualification. When a READY_FOR_IMPLEMENTATION workplan exists, perform bounded stale-plan revalidation and execute it gate by gate instead of repeating repository-wide diagnosis or architectural redesign. Escalate material semantic/architecture/contract/persistence/security/acceptance contradictions as DESIGN_REVISION_REQUIRED rather than silently redesigning.
---

# Software Implementation and Qualification

Use this skill as the **implementation/test/qualification role** of the shared Software Development Protocol. The canonical cross-role contract is `references/workplans-and-agent-handoff.md`.

## Role objective

When an approved workplan exists:

```text
verify handoff -> implement -> test -> measure -> close out
```

Do not spend implementation context repeating design work that has already been frozen unless evidence shows the workplan is stale or impossible.

## Task classification

- **Trivial/local change:** inspect the affected surface, edit, run focused tests, review diff, report. A workplan is not required.
- **Substantial change with approved workplan:** follow the bounded workplan workflow below.
- **Substantial change without resolved design:** do not launch a repository-wide architecture investigation by default. If the user's request already provides a sufficiently frozen design/contract, create only the minimum local gate structure needed to execute it. Otherwise report `DESIGN_REQUIRED`/`WORKPLAN_REQUIRED` with the concrete unresolved design question rather than silently inventing architecture.

## 1. Bounded preflight and stale-plan check

Read repository/project/agent instructions and `references/git-and-version-control.md` before tracked-file changes.

When a workplan exists:

1. read it completely;
2. require `READY_FOR_IMPLEMENTATION` or an explicitly resumable `IN_PROGRESS` state;
3. compute/record `workplan_id`, `plan_revision`, and `workplan_sha256`;
4. verify `analysis_base_commit` exists and compare it with current `HEAD`;
5. inspect changes since the analyzed base only where they intersect `assumption_paths`, referenced current architecture/specifications, target interfaces, and other design-critical surfaces;
6. if assumptions remain valid, record bounded revalidation and proceed;
7. if a material assumption changed, mark `BLOCKED: STALE_WORKPLAN` with concise evidence.

Do **not** automatically repeat repo-wide reconnaissance, algorithm comparison, or architecture planning merely because `HEAD` advanced.

Use `references/repository-intake.md` for the affected subsystem/change surface, but keep intake proportional to the accepted workplan.

## 2. Respect frozen design authority

Read `references/workplans-and-agent-handoff.md` for the authority matrix.

You may decide local implementation details such as helper placement, internal naming, bounded refactoring needed to realize the design, test fixture construction, vectorization mechanics, instrumentation, and equivalent implementation techniques.

Stop the affected gate as `DESIGN_REVISION_REQUIRED` rather than silently changing:

- scientific/numerical semantics;
- chosen algorithm/architectural ownership;
- public API/data/configuration target semantics;
- persistence/schema/recovery architecture;
- security/trust model;
- resource-policy semantics or mandatory thresholds;
- mandatory acceptance criteria;
- material non-goals/scope boundaries.

Return the earliest violated assumption/invariant plus focused evidence and the specific design decision needed.

## 3. Implement one workplan gate at a time

For each gate:

1. inspect the named implementation/test/current-contract surfaces;
2. implement the smallest coherent change satisfying that gate;
3. preserve compatibility/fallback/oracle paths required by the workplan;
4. add focused regression/boundary tests with the implementation;
5. run gate acceptance immediately;
6. fix gate-local implementation/test problems before widening scope;
7. record PASS/FAIL/BLOCKED/NOT RUN/DEFERRED honestly and link evidence rather than pasting large logs into the workplan.

Do not advance past a mandatory FAIL/BLOCKED result unless the design/review role revises the workplan.

Read as applicable:

- `references/specification-and-implementation.md`;
- `references/testing-and-qualification.md`;
- `references/scientific-software.md`;
- `references/performance-and-parallelism.md`;
- `references/storage-and-io.md`;
- `references/concurrency-and-orchestration.md`;
- `references/configuration-and-policy.md`;
- `references/security-and-trust-boundaries.md`;
- `references/debugging-and-state-recovery.md`.

## 4. Correctness before optimization/default policy

Retain a trusted oracle/baseline when the workplan requires equivalence.

For optimization/parallelization:

- profile/measure representative current behavior;
- preserve scientific/API/deterministic semantics;
- bound CPU/RAM/GPU/VRAM/I/O/storage and nested concurrency;
- include serialization/data movement/cache load/recovery when material;
- compare optimized and reference results before claiming speedups;
- keep explicit fallback until removal/default promotion is separately accepted.

Do not reduce fidelity, validation, or coverage merely to meet a runtime target unless that policy is explicitly in the accepted design.

## 5. Persistence, concurrency, and security are correctness domains

For material persisted state, define/test identity, invalidation, atomic publication, corruption/partial-write handling, retention, restart/recovery, migration, and disk footprint.

For concurrent work, test failure propagation, bounded retries, cancellation/preemption, backpressure, deterministic aggregation, idempotency, and cleanup independently from throughput tuning.

For trust boundaries, use least privilege; reject unsafe archive/path/deserialization/subprocess/plugin/network behavior rather than treating external scientific artifacts as inherently trusted.

## 6. Validation ladder

Read `references/testing-and-qualification.md` and run checks from cheap/local to broad:

```text
structural sanity
-> focused behavior/regression
-> oracle/property/invariance
-> consumer/integration
-> broad regression/distribution
-> production/target-environment qualification
```

A blocked or unavailable GPU/HPC/external-service test is not a pass. Do not claim backend qualification because a fallback backend succeeded.

For release/distribution changes read `references/release-and-distribution.md`: build from a controlled source state, inspect produced artifacts, install into an isolated environment, and exercise installed behavior outside the source checkout.

## 7. Normative closeout only after accepted implementation

Read `references/documentation-and-evidence.md`.

At the final applicable gate:

- update current specifications to match accepted implemented behavior;
- update architecture manuals **only if the accepted architecture actually changed**, and describe current architecture rather than workplan gate status/history;
- update history/changelog/release notes and authoritative versions according to project policy;
- update schema/cache/model/protocol versions independently when required;
- regenerate changed **permanent** Markdown documents into PDF/provenance manifests;
- do not render temporary workplans to PDF unless project policy explicitly requires it;
- update indexes/navigation/generated current-state graphs as needed;
- bind final evidence to source revision plus workplan ID/revision/SHA-256;
- mark the workplan `COMPLETE` only after all mandatory closeout evidence passes.

Prefer already-installed usable `pandoc` and `typst`; do not repeatedly download temporary copies. If they are unavailable and installation is not authorized, report PDF regeneration as blocked.

## 8. Workplan/evidence hygiene

The workplan should remain a compact coordination object. Store detailed test logs, benchmarks, audits, run manifests, and release evidence in project-sanctioned locations and link them.

Use task-local gate IDs (`G0`, `G1`, ...) unless a stage is genuinely part of the product/domain architecture. Do not create permanent architecture-stage concepts merely to track temporary engineering work.

## Completion report

Report:

- exact workplan ID/revision/digest consumed (if any);
- gates completed/failed/blocked/deferred;
- changed code/test/spec/architecture/history/version surfaces;
- focused and broad validation actually run;
- benchmark/resource/storage/recovery evidence where applicable;
- release/installed-artifact checks where applicable;
- remaining limitations or design-revision blockers;
- repository branch/worktree state and any pre-existing unrelated changes preserved.
