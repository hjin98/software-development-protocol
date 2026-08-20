---
name: software-implementation
description: Implement, refactor, test, benchmark, and validate software under Protocol 5. Meet functionality, correctness, resource, scaling, hardware, and performance requirements first; then minimize unnecessary total complexity through reuse, consolidation, refactoring, and deletion.
---

# Software Implementation

Implement the requested behavior as the best globally justified engineering solution for the material requirements and target environment.

## Governing doctrine

> **Engineering fitness first; simplicity within the engineering-sufficient solution space.**

Required functionality, correctness, scientific/domain fidelity, reliability, resource feasibility, target-scale behavior, hardware requirements, and materially important performance must be met. Do not weaken those properties merely to reduce line count, component count, or architectural sophistication.

Necessary complexity is valid when it buys a material capability or prevents a material failure. Once the primary requirements are protected, aggressively avoid unnecessary mechanisms, duplicated authority, special cases, abstractions, and maintenance surface.

## Before editing

Understand the owning code path, material contracts, governing workplan if any, production workload, relevant scaling variables, repository instructions, and target resource/hardware constraints.

Inspect progressively. For a local change, understand the local owner. For substantial or repeatedly modified subsystems, also look for existing equivalent functionality, duplicated authorities, stale compatibility paths, or structural debt that would make another local patch the wrong solution.

If the existing design is failing through accumulated wrappers, fallbacks, state translations, retries, duplicated paths, poor scaling, or repeated resource failures, do not automatically add another layer. Consider algorithmic improvement, data-layout change, consolidation, simplification, or redesign first.

## Implement for engineering fitness

Choose implementation techniques according to the actual workload and hardware.

Prefer improving, in material order:

1. unnecessary work and repeated I/O/serialization;
2. asymptotic algorithm/search space;
3. data representation, layout, reuse, and data movement;
4. batching and allocation behavior;
5. vectorized/compiled library kernels;
6. locality and temporary-copy reduction;
7. appropriate CPU concurrency;
8. accelerator execution when justified;
9. custom native kernels only when remaining benefit is material.

Do not preserve a simpler but materially inferior algorithm merely because it is easier to read. Conversely, do not add sophisticated optimization whose measured benefit does not justify its engineering and maintenance cost.

Treat CPU, RAM, VRAM, disk footprint, I/O bandwidth, serialization, host-device transfer, restart/recovery time, and wall time as first-class resources when relevant. Optimize the user-visible stage rather than moving cost outside the measured kernel.

## Implement cleanly

Within the engineering-sufficient design, prefer:

- direct and understandable control flow;
- one authoritative state where feasible;
- cohesive functions/modules with clear ownership;
- established project patterns;
- semantic reuse of existing mechanisms;
- refactoring that reduces duplicated responsibility and special cases;
- deletion of obsolete paths;
- standard-library or existing project mechanisms over new dependencies where sufficient.

Create an abstraction only when it removes real semantic duplication, isolates a genuine responsibility, enforces a material boundary, enables required hardware/performance behavior, or clearly improves the total design.

Do not build speculative extension points or compatibility machinery without a current requirement.

## Reuse, consolidation, and cleanup

Before adding a new helper/module/state mechanism, check whether the owning area already has an implementation that can be cleanly reused or extended.

Consolidate code when implementations represent the same responsibility, invariant, lifecycle, and reason to change. Do not deduplicate merely because source text looks similar.

Retain intentional duplication when it has a distinct material role, such as:

- independent trusted reference/oracle versus optimized production backend;
- hardware-specific implementation required for effective target performance;
- supported compatibility or migration path;
- materially different lifecycle or failure semantics.

After replacing a mechanism, delete the superseded path when compatibility, migration, validation, or recovery no longer materially requires it. Temporary complexity should have a retirement condition when practical.

## Fixes and redesign

For a clear local defect, make the smallest clean owning-layer fix that restores the material contract without degrading engineering fitness.

Escalate to refactor/redesign when repeated fixes target the same mechanism, another fix would add structural debt, ownership is wrong, state or functionality is duplicated, control flow is becoming exceptional, resource behavior is unacceptable, or the existing algorithm cannot meet material scale/reliability/performance requirements cleanly.

A successful fix should not leave the system materially less capable, less efficient, or harder to understand and maintain without explicit justification.

## Testing and validation

Testing is part of implementation. Use three levels as needed:

1. **Focused** — unit, regression, property, numerical, or boundary checks for the mechanism.
2. **Integrated** — exercise the real consumer/path/state transition.
3. **Real use** — representative or production/target-environment execution when needed to establish the material claim.

Not every task needs every level. Stop when the material question is answered with adequate confidence.

Prefer the real product interface over a parallel test implementation. Do not substantially reconstruct or duplicate production logic merely for testing.

Run production scale when scale itself is material or smaller execution cannot establish the required algorithmic/resource/performance behavior.

For performance or accelerator changes, compare against an accepted reference under representative conditions and verify correctness/equivalence. Do not claim target-hardware behavior from unavailable hardware.

## Resource safety and performance evidence

Do not exhaust the host. Honor explicit CPU/RAM/VRAM/storage/I/O/wall-time constraints and use reasonable containment when runaway behavior is plausible.

Use a smaller representative workload when it answers the same material question. Do not build a resource-discovery, calibration, admission, supervisor, checkpoint, or scavenging framework solely because a test is expensive.

When performance materially matters, measure enough to establish the claim: comparable baseline/candidate, representative input, wall time or throughput, relevant peak resources, scaling trend, and end-to-end costs such as I/O/recovery when applicable.

Optimize until further complexity is no longer materially justified; do not pursue theoretical optimum for its own sake.

## External environments

When workstation, HPC, GPU, production data, package-install, or other external execution is materially required, run the actual product there or provide the shortest reproducible command/conditions needed to do so.

Create a dedicated runner only when automation independently reduces real repeated work or error. A different machine does not by itself require a qualification lifecycle.

Never fabricate unavailable execution results.

## Documentation and cleanup

Update public/specification/architecture documentation only when its owned contract actually changed.

Before completion, ask whether the accepted change materially altered a public capability, scientific interpretation, durable architecture, API/configuration contract, workflow, or existing explanation. If not, do not invent a documentation stage. If yes, update the affected durable documentation proportionally. Make a trivial local documentation correction directly; use the optional `software-documentation` specialist when the work requires substantive reconciliation, restructuring, theory/method explanation, user-oriented synthesis, or publication maintenance.

Documentation must describe the accepted present system rather than accumulate implementation chronology. Do not append layers of corrective prose merely to minimize documentation diffs when a conceptual rewrite is warranted. At the same time, documentation maintenance must not become a third lifecycle gate or cause unrelated stale documents to block a correct local product change.

Delete obsolete helpers, experimental paths, stale compatibility layers, generated scratch, and superseded task-local machinery when safe. Git history is usually sufficient history; do not preserve dead machinery merely because it once existed.

## Completion

Report what materially changed; functionality/correctness/scientific behavior established; tests, benchmarks, and real-use checks actually run; resource/performance limitations or external checks still needed; justified complexity added; complexity removed or consolidated; affected durable documentation reconciled when material; and any unresolved design problem. Keep the report proportional to the work.
