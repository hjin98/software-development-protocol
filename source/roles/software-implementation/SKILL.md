---
name: software-implementation
description: Implement, refactor, test, benchmark, and validate software under Protocol 5. Meet the material functionality, correctness, scientific, resource, scaling, hardware, and performance requirements; minimize unjustified product/system complexity; and require affected-surface regression plus integration testing for executable changes.
---

# Software Implementation

Implement the requested behavior as the globally best justified software solution for the material requirements and target environment.

## Governing doctrine

> **Engineering fitness first; minimize unjustified product/system complexity within the engineering-sufficient solution space.**

Required functionality, correctness, scientific/domain fidelity, reliability, resource feasibility, target-scale behavior, hardware requirements, compatibility/security where relevant, and materially important performance must be met. Necessary complexity is valid when it buys a material capability or prevents a material failure.

Simplicity applies primarily to the product being engineered: code, runtime mechanisms, state, interfaces, dependencies, compatibility machinery, operational stages, and maintenance surface. Do not weaken the engineering process merely to reduce the number of steps. Use the implementation staging, tests, integration checks, review support, and benchmarks needed to establish the result; avoid redundant or low-information work because it wastes engineering time/resources.

## Before editing

Understand the owning code path, material contracts, governing workplan if any, production workload, relevant scaling variables, repository instructions, target resources/hardware, and the plausibly affected behavioral surface.

The affected surface is broader than the diff when behavior propagates. Include directly changed/new code plus existing callers/consumers, shared utilities, public interfaces, configuration, persistence, caches/checkpoints, state transitions, orchestration/concurrency paths, packaging/entry points, and transitive behavioral dependencies that could plausibly change.

Inspect progressively. Expand scope when evidence shows broader ownership or impact; do not inventory unrelated areas merely for ceremony.

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

Escalate to refactor/redesign when repeated fixes target the same mechanism, another patch would add structural debt, ownership is wrong, state/functionality is duplicated, exceptional paths proliferate, resource behavior is unacceptable, or the current algorithm cannot meet material scale/reliability/performance requirements cleanly.

## Mandatory functional testing

Testing is part of implementation. For every executable product change, functional acceptance requires both **affected-surface regression testing** and **integration testing**.

### Focused checks

Add or run unit/property/numerical/boundary/error tests appropriate to each new or modified mechanism. A bug fix should preserve a reproducing case as regression coverage when practical.

Do not require one test per file/function. Existing tests count when they genuinely protect the changed contract; add coverage where they do not.

### Affected-surface regression

Run the regression tests needed to establish that:

- new/modified behavior works;
- supported behavior across every plausibly affected existing path remains functional;
- changed shared contracts do not silently break consumers;
- relevant failure/error/recovery behavior still works.

A shared or central change may require a broad or repository-wide suite. Unrelated modules need not be tested merely for symmetry.

A required regression check that did not execute is not a pass. Newly introduced failures and failures that plausibly intersect the affected surface block functional acceptance. Demonstrably pre-existing unrelated failures may be attributed and reported rather than repaired, but not silently ignored.

### Integration testing

Exercise the assembled affected product path across the relevant real module/interface boundaries using bounded representative fixtures when possible. Prefer the public/real consumer path over a parallel test implementation. Do not mock away the boundary whose integration is being established.

For libraries, use the nearest real consumer/public interface. For CLI/package/build changes, exercise the user-facing entry point or installed/built artifact as applicable.

### Stage-local and final testing

After a material implementation stage changes executable behavior, run focused checks plus the regression subset whose early execution materially reduces defect propagation, debugging ambiguity, rework, or downstream risk. A tiny atomic change may use its final pass as the stage pass; do not duplicate identical work ceremonially.

Before completion, run a final assembled affected-surface regression pass and integration pass after all material implementation/refactoring/cleanup changes that could affect behavior.

Optimize test **cost**, not required **coverage**. Use small deterministic fixtures, bounded datasets, reduced epochs/iterations, synthetic inputs, and representative workloads when they exercise the same behavioral contracts.

## Production qualification is separate

Full production qualification assumes functional regression and integration acceptance already passed. It uses real, long, data-heavy, target-machine/target-hardware workloads to characterize production-scale wall time/throughput, RAM/VRAM/storage/I/O, scaling, accelerator utilization, recovery cost, and similar environment-specific properties.

Do not run full production qualification by default during implementation or between implementation stages. Run it only when explicitly requested, project/release policy requires it, or the material scale/resource/performance/hardware claim cannot be established otherwise.

Bounded performance benchmarks, accelerator smoke tests, CPU/GPU/reference equivalence checks, and representative resource sanity checks remain normal implementation validation when affected code requires them. Do not claim unavailable target-hardware results.

## Resource safety and performance evidence

Honor explicit CPU/RAM/VRAM/storage/I/O/wall-time constraints. Use bounded representative workloads when they establish the same claim. Do not build unnecessary calibration/supervision infrastructure solely because a test is expensive.

When performance materially matters, measure enough to establish the claim under comparable conditions: baseline/candidate, representative inputs, wall time/throughput, relevant peak resources, scaling trend, and end-to-end costs such as I/O/recovery where applicable.

## External environments

When workstation, HPC, GPU, production data, package installation, or another external environment is materially required, run the actual product there when available or provide reproducible commands/conditions. A different machine does not itself create a qualification lifecycle. Never fabricate unavailable execution results.

## Documentation and cleanup

Update durable public/specification/architecture/user documentation when its owned contract actually changed. Documentation work should be sufficient to keep the accepted system accurate and understandable; it need not become a separate approval lifecycle.

Delete obsolete helpers, experimental paths, stale compatibility layers, generated scratch, and superseded product machinery when safe. Do not treat useful tests or validation infrastructure as product complexity to be removed merely because they lengthen the engineering process.

## Completion

Report:

- what materially changed;
- functionality/correctness/scientific behavior established;
- affected behavioral surface identified;
- focused tests added/run;
- intermediate regression checks actually run where material;
- final affected-surface regression results;
- integration path(s) exercised;
- benchmarks/target-hardware checks actually run;
- any unavailable required functional checks;
- production qualification performed, explicitly deferred, or unnecessary and why;
- product complexity added/removed/consolidated;
- affected durable documentation reconciled;
- unresolved material risks.

Keep the report proportional to the work, but do not call an executable change functionally complete while required regression or integration checks are failing or unexecuted.
