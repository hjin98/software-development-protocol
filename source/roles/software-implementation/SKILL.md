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

Development economy applies only after engineering fitness and product simplicity. Avoid redundant reasoning, rediscovery, low-information inspection, invalid reruns, repeated boilerplate, and unnecessary tool/compute work when the required product and confidence remain unchanged.

## Before editing

Understand the owning code path, material contracts, governing workplan if any, production workload/scaling variables, repository instructions, target resources/hardware, and plausibly affected behavioral surface.

Inspect progressively. Expand scope through evidence of ownership, dependency, contract, or behavioral impact rather than adjacency. Reuse established facts until later evidence invalidates them. For detailed information-gain/context rules, read `references/repository-intake.md`.

The affected surface is broader than the diff when behavior propagates: include directly changed/new code plus callers/consumers, shared utilities, public interfaces, configuration, persistence/caches/checkpoints, state transitions, orchestration/concurrency paths, packaging/entry points, and plausible transitive behavioral dependencies.

## Governing workplan authority

When an **accepted workplan** exists, treat its material target decisions as the implementation contract. Do not reopen frozen architecture, ownership, algorithm, invariant, non-goal, or acceptance decisions merely because another plausible design exists.

The plan remains subordinate to higher-priority explicit user/task requirements, safety/platform constraints, applicable project instructions, and governed contracts outside the authorized change scope. Existing contracts remain authoritative except where the workplan explicitly defines their intended change.

Repository evidence describes actual state. Reconcile plan/repository mismatch rather than automatically abandoning the target or blindly forcing an invalid assumption.

Use three deviation levels:

1. **Implementation realization** — local mechanics that preserve frozen semantics; proceed.
2. **Local reconciliation** — adapt superficial plan/repository mismatch while preserving the frozen target; proceed and record a material reason when interpretation depends on it.
3. **Material redesign** — a frozen architecture/ownership/algorithm/product-semantics/resource/persistence/compatibility decision must change; stop dependent implementation and reopen design.

Material redesign requires evidence: an unreconcilable ownership/contract conflict, inability to meet a material requirement, representative measurement invalidating a premise, an explicit redesign trigger, or repeated local fixes exposing a structural defect.

When redesign is required, identify the invalidated decision, preserve unrelated accepted work/evidence, reopen only the affected design surface, reconcile the workplan, invalidate only evidence whose claim can plausibly change, and resume from the **earliest materially affected** stage.

## Implement for engineering fitness and clean ownership

Prefer, in material order, eliminating redundant work/I/O, improving algorithmic scaling, improving representation/layout/reuse/data movement, batching/allocation behavior, compiled/vectorized kernels, locality/copy reduction, appropriate CPU concurrency, accelerator execution when justified, and custom native kernels only when remaining benefit is material.

Within the engineering-sufficient design, prefer direct control flow, one authoritative state, cohesive ownership, established project patterns, semantic reuse, consolidation, deletion of obsolete paths, and standard/existing mechanisms when sufficient.

Do not preserve a materially inferior algorithm merely because it is simpler. Do not add sophisticated optimization/abstraction whose material benefit does not justify product complexity and maintenance cost. Retain intentional duplication when it has a distinct role such as an independent oracle, hardware-specific backend, supported migration path, or materially different lifecycle/failure semantics.

For a clear local defect, fix the owning layer. Escalate to refactor/redesign when repeated fixes target the same mechanism, ownership is wrong, duplicated state/functionality causes failures, exceptional paths proliferate, resources are unacceptable, or the current algorithm cannot meet material requirements cleanly.

## Functional acceptance hard rules

Testing is part of implementation. For executable changes:

1. run focused checks appropriate to changed mechanisms;
2. after **each material behavior-changing implementation stage**, run the relevant **stage-local affected regression** before dependent implementation proceeds;
3. before completion, perform **Final assembled acceptance**: re-derive the affected behavioral surface from the final candidate, rerun complete affected-surface regression after all material executable edits, and run required integration/end-to-end paths through real product/consumer boundaries;
4. run repository/project-required checks, using the broader/full suite when impact cannot be bounded confidently;
5. treat an unexecuted required check as not passed; newly introduced/affected failures block acceptance.

Define stages by coherent behavior/risk boundaries rather than individual file/helper edits. Within a stage, run cheapest high-signal focused checks before the required affected regression. Reuse still-valid intermediate evidence until a changed dimension can plausibly invalidate its claim. None of this weakens final assembled acceptance.

Optimize test **cost**, not required **coverage**. Read `references/testing-and-validation.md` for detailed evidence-reuse, stage, integration, failure-attribution, and qualification rules.

## Production qualification is separate

Full production qualification assumes functional regression/integration acceptance already passed. It uses real, long, data-heavy, target-environment workloads to characterize production-scale performance/resources/scaling/recovery/hardware behavior.

Do not run it by default during implementation or between ordinary stages. Run it only when explicitly requested, required by project/release policy, or necessary to establish a material production-scale/resource/performance/hardware claim. Bounded benchmarks, accelerator smoke tests, reference equivalence, and representative resource sanity checks remain normal implementation validation when relevant.

A production run never substitutes for missing focused/regression/integration coverage. Never fabricate unavailable target-hardware results.

## Resource/performance evidence

Honor explicit CPU/RAM/VRAM/storage/I/O/wall-time constraints. When performance materially matters, measure enough to establish the claim under comparable conditions. Reuse compatible expensive baseline evidence rather than rerunning it merely because a session/date changed.

## Documentation and cleanup

Update durable public/specification/architecture/user documentation when its owned contract changed. Delete obsolete task-owned helpers/experimental paths/superseded product machinery when safe; do not remove useful tests/validation infrastructure merely because it lengthens engineering work.

## Reference routing

Packaging a reference does not make reading it mandatory. Load the reference when its owned surface is material; start with the relevant section and broaden when interaction requires it.

| Material surface | Reference |
| --- | --- |
| lifecycle, workplans, gates | `references/workflow-and-workplans.md` |
| functional acceptance, evidence reuse, qualification | `references/testing-and-validation.md` |
| protocol/workplan compatibility | `references/protocol-versioning-and-compatibility.md` |
| architecture/ownership/redesign/complexity | `references/architecture-and-design.md` |
| nontrivial failure/state recovery | `references/debugging-and-state-recovery.md` |
| API/schema/persistence/scientific contracts | `references/specification-and-implementation.md` |
| configuration/policy/semantic identity | `references/configuration-and-policy.md` |
| workers/schedulers/retries/cancellation | `references/concurrency-and-orchestration.md` |
| untrusted inputs/credentials/subprocess/network/model loading | `references/security-and-trust-boundaries.md` |
| CPU/GPU/scaling/resources/performance | `references/performance-and-parallelism.md` |
| storage/cache/checkpoint/I/O/recovery | `references/storage-and-io.md` |
| physics/math/ML/numerical semantics | `references/scientific-software.md` |
| repository inspection/change surface | `references/repository-intake.md` |
| branches/worktrees/commits/remotes | `references/git-and-version-control.md` |
| packages/build/install/distribution | `references/release-and-distribution.md` |
| documentation authority/evidence | `references/documentation-and-evidence.md` |

## Completion

Report material changes and enough evidence to interpret acceptance. For executable changes include final affected surface, focused checks, stage-local regression results for material stages, final affected-surface regression, integration paths, repository-required broader checks, and unavailable/blocking checks.

Report benchmarks/target-hardware/production qualification only when materially relevant, requested, required, performed, or intentionally deferred. Also report material product-complexity changes, documentation reconciliation, and unresolved risks.

Do not call an executable change functionally complete while required stage-local/final regression, repository-required checks, or integration checks are failing or unexecuted.
