---
name: software-implementation
description: Implement, refactor, test, benchmark, and validate software under Protocol 5. Meet material functionality, correctness, scientific, resource, scaling, hardware, security, and performance requirements; minimize unjustified product/system complexity; and require stage-local plus final affected-surface regression and integration testing for executable changes.
---

# Software Implementation

Implement the requested behavior as the globally best justified solution for the material requirements and target environment.

## Governing doctrine

> **Engineering fitness first; minimize unjustified product/system complexity within the engineering-sufficient solution space; then avoid unnecessary development cost without weakening the product or its acceptance.**

Apply the hierarchy lexicographically:

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Required functionality/capability, correctness, scientific/domain fidelity, reliability, resource feasibility, target-scale behavior, hardware requirements, compatibility/security where relevant, and materially important performance must be met. Necessary complexity is valid when it buys a material capability or prevents a material failure.

Simplicity applies primarily to the product being engineered: code, runtime mechanisms, state, interfaces, dependencies, compatibility machinery, operational stages, and maintenance surface. Do not weaken the engineering process merely to reduce the number of steps.

Development economy applies after engineering fitness and product simplicity. Avoid redundant reasoning, rediscovery, low-information inspection, unnecessary validation reruns, repeated boilerplate, and other process waste when the required product and confidence remain unchanged. Never trade a material requirement or required acceptance evidence for lower development cost.

## Before editing

Understand the owning code path, material contracts, governing workplan if any, production workload, relevant scaling variables, repository instructions, target resources/hardware, and the plausibly affected behavioral surface.

The affected surface is broader than the diff when behavior propagates. Include directly changed/new code plus existing callers/consumers, shared utilities, public interfaces, configuration, persistence, caches/checkpoints, state transitions, orchestration/concurrency paths, packaging/entry points, and transitive behavioral dependencies that could plausibly change.

Inspect progressively. Expand scope when evidence shows broader ownership or impact; do not inventory unrelated areas merely for ceremony. When impact cannot be bounded confidently, assume the broader plausible surface until evidence narrows it.

## Governing workplan authority

When an **accepted workplan** exists, treat its material target decisions as the implementation contract. Do not reopen a frozen architecture, ownership, algorithm, invariant, non-goal, or acceptance decision merely because another plausible design exists.

The accepted workplan remains subordinate to higher-priority explicit user/task requirements, safety/platform constraints, applicable project instructions, and governed contracts outside the authorized change scope. Existing specifications/contracts remain authoritative except where the workplan explicitly defines their intended change.

Repository evidence describes actual state. When current code/tests differ from the accepted target, that difference is not by itself permission to abandon the workplan. Reconcile repository reality with the target and escalate only when the mismatch invalidates a frozen material assumption.

Use three deviation levels:

1. **Implementation realization** — local mechanics such as factoring, naming, fixture construction, or exact placement where the workplan intentionally leaves discretion. Proceed without reopening design when frozen semantics are preserved.
2. **Local reconciliation** — adapt superficial plan/repository mismatch while preserving the frozen target. Record a material reason when interpretation depends on it; do not create a design cycle for ordinary realization details.
3. **Material redesign** — a frozen architecture/ownership/algorithm/product-semantics/resource/persistence/compatibility decision must change. Stop dependent implementation and reopen design.

A material redesign requires evidence: an unreconcilable repository-authority conflict, inability to meet a material requirement, representative measurement that invalidates a material premise, an explicit redesign trigger, or repeated local fixes exposing a structural defect.

When redesign is required, identify the invalidated decision, preserve unrelated accepted work/evidence, reopen only the affected design surface, reconcile the workplan, invalidate evidence only where the changed decision can plausibly affect its claim, and resume from the **earliest materially affected** stage. Do not restart unrelated accepted work.

## Implement for engineering fitness

Choose implementation techniques according to the actual workload and hardware. Prefer, in material order, eliminating redundant work/I/O, improving algorithmic scaling, improving representation/layout/reuse/data movement, batching/allocation behavior, compiled/vectorized kernels, locality/copy reduction, appropriate CPU concurrency, accelerator execution when justified, and custom native kernels only when remaining benefit is material.

Do not preserve a simpler but materially inferior algorithm merely because it is easier to read. Conversely, do not add sophisticated optimization whose material benefit does not justify its product complexity and maintenance cost.

Treat CPU, RAM, VRAM, storage, I/O, serialization, host-device transfer, restart/recovery time, and wall time as first-class resources where relevant.

## Implement cleanly

Within the engineering-sufficient design, prefer direct control flow, one authoritative state, cohesive ownership, established project patterns, semantic reuse, consolidation, deletion of obsolete paths, and standard/existing mechanisms when sufficient.

Create abstractions only when they remove real semantic duplication, isolate genuine responsibilities, enforce material boundaries, enable required hardware/performance behavior, or reduce total product complexity.

Retain intentional duplication when it has a distinct material role such as an independent reference/oracle, hardware-specific backend, supported compatibility/migration path, or materially different lifecycle/failure semantics.

## Fixes and redesign

For a clear local defect, make the clean owning-layer fix that restores the material contract without degrading engineering fitness. The implementation may be small; the validation coverage still follows the affected behavioral surface.

Escalate to refactor/redesign when repeated fixes target the same mechanism, another patch would add structural debt, ownership is wrong, state/functionality is duplicated, exceptional paths proliferate, resource behavior is unacceptable, or the current algorithm cannot meet material scale/reliability/performance requirements cleanly. If an accepted workplan governs the change, use the bounded material-redesign rule above rather than silently replacing frozen design.

## Mandatory functional testing

Testing is part of implementation. For every executable product change, functional acceptance requires **affected-surface regression testing** and **integration testing**. Focused checks establish individual mechanisms; regression and integration establish the assembled product.

### Focused checks

Add or run unit/property/numerical/boundary/error tests appropriate to each new or modified mechanism. A bug fix should preserve a reproducing case as regression coverage when practical.

Do not require one test per file/function. Existing tests count when they genuinely protect the changed contract; add coverage where they do not.

### Affected-surface regression

Run regression tests sufficient to establish that:

- new/modified behavior works;
- supported behavior across every plausibly affected existing path remains functional;
- changed shared contracts do not silently break consumers;
- relevant failure/error/recovery behavior still works.

Repository/project-required checks remain mandatory. A shared or central change may require a broad or repository-wide suite. If impact analysis cannot confidently bound the regression surface, run the broader/full available suite rather than assuming unexamined consumers are unaffected.

A required regression check that did not execute is not a pass. Newly introduced failures and failures that plausibly intersect the affected surface block functional acceptance. Demonstrably pre-existing unrelated failures may be attributed and reported rather than repaired, but not silently ignored.

### Integration testing

Exercise the assembled affected product path across the relevant real module/interface boundaries using bounded representative fixtures when possible. Prefer the public/real consumer path over a parallel test implementation. Do not mock away the boundary whose integration is being established.

For libraries, use the nearest real consumer/public interface. For CLI/package/build changes, exercise the user-facing entry point or built/installed artifact as applicable.

### Stage-local regression is required

After **each material implementation stage that changes executable behavior**, run the focused checks and affected regression subset relevant to that stage before dependent implementation proceeds. Fix newly introduced hard failures and affected regressions at the stage that introduced them rather than stacking later work on an unaccepted stage.

A tiny atomic change may use its final pass as its stage pass. A stage that genuinely cannot be exercised independently may be combined with the nearest executable integration stage, but record that dependency rather than silently deferring all regression to the end.

Intermediate regression is required for material behavior-changing stages because it limits defect propagation and preserves fault localization; it is not optional merely because a final suite will run later.

### Final assembled acceptance

Before completion:

1. re-derive the affected behavioral surface from the **final assembled implementation**, because implementation/refactoring may have broadened impact beyond the initial plan;
2. account for every identified affected path with executed regression coverage, a repository-required broader suite, or an explicit unavailable/blocking check;
3. rerun the complete affected-surface regression on the final candidate after all material executable refactoring/cleanup/package changes;
4. run the required integration/end-to-end path(s) on that same assembled candidate.

Optimize test **cost**, not required **coverage**. Use small deterministic fixtures, bounded datasets, reduced epochs/iterations, synthetic inputs, and representative workloads when they exercise the same behavioral contracts.

## Production qualification is separate

Full production qualification assumes functional regression and integration acceptance already passed. It uses real, long, data-heavy, target-machine/target-hardware workloads to characterize production-scale wall time/throughput, RAM/VRAM/storage/I/O, scaling, accelerator utilization, recovery cost, and similar environment-specific properties.

Do not run full production qualification by default during implementation or between implementation stages. Run it only when explicitly requested, project/release policy requires it, or the material scale/resource/performance/hardware claim cannot be established otherwise.

Bounded performance benchmarks, accelerator smoke tests, CPU/GPU/reference equivalence checks, and representative resource sanity checks remain normal implementation validation when affected code requires them. Do not claim unavailable target-hardware results.

A successful production run never substitutes for missing focused/regression/integration coverage, and bounded functional tests do not prove production-scale performance/resource qualification.

## Resource safety and performance evidence

Honor explicit CPU/RAM/VRAM/storage/I/O/wall-time constraints. Use bounded representative workloads when they establish the same claim. Do not build unnecessary calibration/supervision infrastructure solely because a test is expensive.

When performance materially matters, measure enough to establish the claim under comparable conditions: baseline/candidate, representative inputs, wall time/throughput, relevant peak resources, scaling trend, and end-to-end costs such as I/O/recovery where applicable.

## External environments

When workstation, HPC, GPU, production data, package installation, or another external environment is materially required, run the actual product there when available or provide reproducible commands/conditions. A different machine does not itself create a qualification lifecycle. Never fabricate unavailable execution results.

## Documentation and cleanup

Update durable public/specification/architecture/user documentation when its owned contract actually changed. Documentation work should be sufficient to keep the accepted system accurate and understandable; it need not become a separate approval lifecycle.

Delete obsolete helpers, experimental paths, stale compatibility layers, generated scratch, and superseded product machinery when safe. Do not treat useful tests or validation infrastructure as product complexity to be removed merely because they lengthen the engineering process.

## Supporting references

Read the packaged references when their surface is material:

- `references/workflow-and-workplans.md` — lifecycle, gates, stage acceptance, and workplans;
- `references/testing-and-validation.md` — regression/integration contract and qualification boundary;
- `references/protocol-versioning-and-compatibility.md` — protocol/candidate/evidence compatibility;
- `references/architecture-and-design.md` — redesign, ownership, and product-complexity decisions;
- `references/debugging-and-state-recovery.md` — failures, fixes, durable state, and recovery;
- `references/specification-and-implementation.md` — API/schema/persistence/scientific contracts;
- `references/configuration-and-policy.md` — configuration resolution and semantic identity;
- `references/concurrency-and-orchestration.md` — workers, retries, cancellation, publication, and deterministic aggregation;
- `references/security-and-trust-boundaries.md` — untrusted inputs, credentials, subprocess/network/archive/model boundaries;
- `references/performance-and-parallelism.md` — scaling, CPU/GPU, resource budgets, and benchmarking;
- `references/storage-and-io.md` — storage, cache/checkpoint, I/O, crash consistency, and recovery;
- `references/scientific-software.md` — numerical/scientific invariants and reference equivalence;
- `references/repository-intake.md` — progressive repository inspection and change surface;
- `references/git-and-version-control.md` — Git safety, concurrent work, and authorization boundaries;
- `references/release-and-distribution.md` — built/installed artifact validation;
- `references/documentation-and-evidence.md` — durable documentation ownership and evidence.

## Completion

Report what materially changed and the evidence needed to interpret acceptance. For executable changes include the final affected surface, focused tests, stage-local regression results for each material behavior-changing stage, final affected-surface regression results, integration path(s), repository-required broader checks, and unavailable/blocking functional checks.

Report benchmarks/target-hardware checks and production qualification only when materially relevant, requested, required, performed, or intentionally deferred. Also report significant product complexity added/removed/consolidated, affected durable documentation reconciled, and unresolved material risks.

Do not call an executable change functionally complete while required stage-local/final regression, repository-required checks, or integration checks are failing or unexecuted.
