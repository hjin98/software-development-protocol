# Architecture and Design

Architecture exists to help the software satisfy its global engineering goals: capability, correctness, scientific/domain fidelity, scalability, resource feasibility, robustness, target-hardware effectiveness, maintainability, and materially important performance.

Architecture is judged over the material operational and maintenance horizon of the accepted scope. A locally convenient design is not simpler in the engineering sense when it knowingly creates avoidable ownership ambiguity, operational fragility, maintenance debt, or supported-evolution cost that materially degrades the durable product. Conversely, stewardship does not justify speculative generalization or unrelated future-proofing.

## Engineering fitness first

Define the material engineering envelope before choosing architecture: required behavior, correctness/scientific invariants, reliability/recovery/security/compatibility, target workload and scaling variables, CPU/RAM/VRAM/storage/I/O/wall-time limits, hardware/portability requirements, and materially important latency/throughput.

Reject designs that cannot satisfy this envelope cleanly enough for the actual product. Do not prefer a locally simple architecture that is globally unusable because of poor scaling, excessive resource use, weak hardware utilization, or missing capability.

## Minimum justified product complexity

Among designs that satisfy the material engineering requirements, prefer the one with the lowest justified **total product/system complexity**: fewer unnecessary components, states, interfaces, dependencies, synchronization points, duplicated authorities, compatibility paths, runtime/operational stages, special cases, and maintenance burdens.

Development economy is subordinate to engineering fitness and product simplicity. Process activities should be eliminated when they add no material information, confidence, or risk reduction, but never when their removal weakens the product or required acceptance.

Necessary specialization remains valid when it protects correctness, scientific fidelity, performance, hardware effectiveness, recovery, compatibility, portability, security, or another material requirement. A trusted reference implementation plus an optimized backend, or separate CPU/GPU kernels, may be globally better than forcing distinct responsibilities through one abstraction.

## Architecture review

For nontrivial work, define what materially matters: root cause/objective, scope/non-goals, acceptance-critical behavior, invariants/conventions, authoritative state/ownership, algorithm/data flow/scaling, representation/data movement, resource/hardware/parallelism behavior, interfaces/dependencies, failure/recovery/security behavior, important alternatives/tradeoffs, justified specialization/complexity, affected behavioral surface, and genuine redesign triggers.

Reject a design when it violates a hard invariant, cannot meet material scale/resource/reliability/performance requirements, creates unclear ownership, duplicates authoritative state without need, or adds product complexity without material engineering benefit.

## Accepted design and implementation authority

Once a substantial design is accepted into a governing workplan, implementation should not repeat the entire architecture search. The workplan should identify frozen material decisions, delegated implementation mechanics, and assumptions/redesign triggers that may reopen design.

Repository evidence may reveal that a frozen assumption is false. Treat that as a design-invalidation question rather than silently changing the target or blindly forcing the plan onto incompatible reality.

A local realization or **local reconciliation** that preserves frozen architecture, ownership, algorithms, and semantics remains implementation work. A **material redesign** changes one of those frozen decisions and requires reopening design.

When redesign is required, **reopen only the affected** design surface. Preserve unrelated accepted design, implementation stages, and evidence whose claims remain valid. Resume implementation from the earliest materially affected dependency rather than restarting the whole workplan.

## Complexity regression and consolidation review

Substantial changes and repeated work in one subsystem should include affected-area structural review. Ask whether existing components can own the responsibility, equivalent functionality/state already exists, multiple authorities can be consolidated, derivable state can replace synchronized duplicates, stale wrappers/fallbacks/compatibility paths can be retired, or superseded machinery can be deleted.

Prefer semantic reuse and consolidation rather than textual DRY. A new canonical component may reduce global complexity by replacing several authorities; forcing materially distinct hardware/scientific responsibilities into one generic abstraction may increase it.

## Redesign boundary

A local bug with a local cause should receive a clean local owning-layer fix. Redesign when repeated fixes accumulate around the same mechanism, ownership is wrong, duplicated state/logic causes failures, compatibility/fallback layers proliferate, testing requires parallel reconstruction of production behavior, resource failures repeat, or the current algorithm cannot meet material requirements cleanly.

For accepted workplans, require evidence before reopening frozen design: an irreconcilable ownership/contract mismatch, material engineering infeasibility, representative measurement that invalidates a premise, or an explicit redesign trigger. Do not reopen settled design merely because another plausible architecture exists.

## Convergence boundary for repeated defect families

A first clean local defect remains a local owning-layer repair. When materially equivalent defects recur around the same invariant/authority/mechanism, establish the bounded semantic family and close it at the canonical owner, consolidating duplicate enforcement or deleting bypasses when that reduces the failure surface.

After an adequate family closure has implemented the canonical realization and passed required family-level real-owner, affected-regression, integration, and structural evidence, a same-family material recurrence triggers bounded Software Design reconsideration before another ordinary sibling patch. An incomplete or artificially narrow family closure is instead implementation nonconformance that must be completed unless separate redesign evidence already exists.

Design reconsideration does not automatically mean architecture churn or a new normative workplan revision. If frozen product/architecture/ownership semantics remain sound, Design may require a stronger implementation refactor, consolidation, API narrowing, or canonicalization under the same authority. Reopen current design authority only when a frozen material decision itself must change. Preserve justified specialization where distinct hardware, scientific, compatibility, lifecycle, or failure semantics make one abstraction worse.

## Architecture documentation

Permanent architecture documentation describes accepted current product structure, ownership, interfaces, data/control flow, important invariants, persistence/concurrency/security/resource boundaries, target-hardware assumptions where material, and accepted algorithms. Do not turn it into a log of development-process gates or temporary benchmark attempts.
