# Architecture and Design

Architecture exists to help the software satisfy its global engineering goals: capability, correctness, scientific/domain fidelity, scalability, resource feasibility, robustness, target-hardware effectiveness, maintainability, and materially important performance.

## Engineering fitness first

Define the material engineering envelope before choosing architecture: required behavior, correctness/scientific invariants, reliability/recovery/security/compatibility, target workload and scaling variables, CPU/RAM/VRAM/storage/I/O/wall-time limits, hardware/portability requirements, and materially important latency/throughput.

Reject designs that cannot satisfy this envelope cleanly enough for the actual product. Do not prefer a locally simple architecture that is globally unusable because of poor scaling, excessive resource use, weak hardware utilization, or missing capability.

## Minimum justified product complexity

Among designs that satisfy the material engineering requirements, prefer the one with the lowest justified **total product/system complexity**: fewer unnecessary components, states, interfaces, dependencies, synchronization points, duplicated authorities, compatibility paths, runtime/operational stages, special cases, and maintenance burdens.

This complexity objective describes the engineered product/system. It does **not** require the engineering process itself to have the fewest design steps, tests, reviews, gates, or iterations. Process activities are justified by the confidence, risk reduction, fault localization, or engineering efficiency they provide.

Necessary specialization remains valid when it protects correctness, scientific fidelity, performance, hardware effectiveness, recovery, compatibility, portability, security, or another material requirement. A trusted reference implementation plus an optimized backend, or separate CPU/GPU kernels, may be globally better than forcing distinct responsibilities through one abstraction.

## Architecture review

For nontrivial work, define what materially matters: root cause/objective, scope/non-goals, acceptance-critical behavior, invariants/conventions, authoritative state/ownership, algorithm/data flow/scaling, representation/data movement, resource/hardware/parallelism behavior, interfaces/dependencies, failure/recovery/security behavior, important alternatives/tradeoffs, justified specialization/complexity, affected behavioral surface, and genuine redesign triggers.

Reject a design when it violates a hard invariant, cannot meet material scale/resource/reliability/performance requirements, creates unclear ownership, duplicates authoritative state without need, or adds product complexity without material engineering benefit.

## Complexity regression and consolidation review

Substantial changes and repeated work in one subsystem should include affected-area structural review. Ask whether existing components can own the responsibility, equivalent functionality/state already exists, multiple authorities can be consolidated, derivable state can replace synchronized duplicates, stale wrappers/fallbacks/compatibility paths can be retired, or superseded machinery can be deleted.

Prefer semantic reuse and consolidation rather than textual DRY. A new canonical component may reduce global complexity by replacing several authorities; forcing materially distinct hardware/scientific responsibilities into one generic abstraction may increase it.

## Redesign boundary

A local bug with a local cause should receive a clean local owning-layer fix. Redesign when repeated fixes accumulate around the same mechanism, ownership is wrong, duplicated state/logic causes failures, compatibility/fallback layers proliferate, testing requires parallel reconstruction of production behavior, resource failures repeat, or the current algorithm cannot meet material requirements cleanly.

## Architecture documentation

Permanent architecture documentation describes accepted current product structure, ownership, interfaces, data/control flow, important invariants, persistence/concurrency/security/resource boundaries, target-hardware assumptions where material, and accepted algorithms. Do not turn it into a log of development-process gates or temporary benchmark attempts.
