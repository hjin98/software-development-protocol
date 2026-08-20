# Architecture and Design

Architecture exists to help the software satisfy its global engineering goals: capability, correctness, scientific/domain fidelity, scalability, resource feasibility, robustness, target-hardware effectiveness, maintainability, and materially important performance. It is not a place to maximize abstraction or minimize code at the expense of those goals.

## Engineering fitness first

Before choosing architecture, define the material engineering envelope:

- required functionality and user-visible behavior;
- correctness and scientific/numerical invariants;
- reliability, recovery, security, safety, and compatibility where required;
- target workload sizes and asymptotic scaling variables;
- CPU, RAM, VRAM, storage, I/O, wall-time, scheduler, and deployment constraints;
- target hardware and portability requirements;
- materially important end-to-end latency or throughput.

Reject designs that cannot satisfy this envelope cleanly enough for the actual product. Do not prefer a locally simple architecture that is globally unusable because of poor scaling, excessive resource use, weak hardware utilization, or missing capability.

Use the best materially justified algorithm and implementation form for the target workload. More sophisticated architecture is justified when it produces a material engineering benefit; theoretical optimality without material benefit is not a requirement.

## Minimum justified complexity

Among designs that satisfy the material engineering requirements, prefer the one with lower **total system complexity**: fewer unnecessary components, states, interfaces, dependencies, synchronization points, duplicated authorities, compatibility paths, workflow stages, and special cases.

Complexity is a liability unless it buys a material capability or protects a material risk. Count conceptual surface, not merely lines of code or number of functions.

Necessary specialization remains valid when it protects correctness, scientific fidelity, performance, hardware effectiveness, recovery, compatibility, portability, or another material requirement. A trusted reference implementation plus an optimized backend, or separate CPU/GPU kernels, may be better global architecture than forcing everything through one generic abstraction.

## Architecture review

For a nontrivial feature, algorithm, persistence model, concurrency design, performance redesign, or structural refactor, define only what materially matters:

1. problem/root cause and objective;
2. scope and non-goals;
3. required capability and acceptance-critical behavior;
4. important invariants/conventions;
5. authoritative state and ownership;
6. algorithm/data flow and material complexity/scaling;
7. data representation, locality, and data movement where relevant;
8. resource/hardware/parallelism behavior where relevant;
9. interfaces and dependency direction;
10. failure/recovery/security behavior where relevant;
11. materially plausible alternatives and important tradeoffs;
12. justified complexity and true redesign triggers.

Reject a design when it violates a hard invariant, cannot meet material scale/resource/reliability/performance requirements, creates unclear ownership, duplicates authoritative state without need, or adds complexity without a material engineering benefit.

## Complexity regression and consolidation review

Substantial changes and repeated work in one subsystem should include a proportionate affected-area structural review.

Ask:

- Can an existing component own this responsibility?
- Is materially equivalent functionality already implemented elsewhere?
- Are multiple implementations authoritative for one concept?
- Can state be derived instead of persisted or synchronized?
- Can two paths be collapsed into one without harming capability or performance?
- Can a special case be removed by fixing the owning abstraction or algorithm?
- Can a standard/existing library mechanism replace custom infrastructure?
- Can superseded code or temporary migration machinery now be deleted?
- Would one reusable semantic owner reduce total complexity?
- Is apparent duplication actually necessary specialization, compatibility, or independent validation?

Prefer semantic reuse and consolidation, not textual DRY. Code should share an abstraction when it shares responsibility, invariant, lifecycle, and reason to change. Two blocks that merely look similar do not automatically belong together.

A new abstraction can reduce global complexity when it replaces several duplicated authorities. Conversely, a locally smaller abstraction can increase global complexity when it obscures distinct responsibilities or damages performance/hardware specialization.

Do not turn these questions into a numerical complexity score. Engineering judgment is the point.

## Redesign boundary

A local bug with a local cause should receive a local clean fix.

Redesign when repeated fixes accumulate around the same mechanism, ownership is wrong, duplicated state or logic causes failures, compatibility/fallback layers proliferate, testing requires parallel reconstruction of production behavior, resource failures repeat, or the current algorithm cannot meet material scale/reliability/performance requirements cleanly.

Do not stabilize bad architecture by surrounding it with more architecture. Do not block an urgent clean local fix merely because unrelated cleanup is possible.

## Architecture documentation

Permanent architecture documentation describes accepted current structure: ownership, interfaces, data/control flow, important invariants, durable persistence/concurrency/security/resource boundaries, target-hardware assumptions when material, and accepted algorithms.

Do not put gate logs, temporary benchmark plans, task status, chronological implementation history, or speculative future machinery into the architecture manual.

Proposed transitions belong in a concise workplan until accepted. Update the normative architecture only after the implementation actually changes it.
