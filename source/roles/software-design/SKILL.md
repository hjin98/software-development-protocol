---
name: software-design
description: Diagnose and design nontrivial software changes, define the material engineering envelope, choose effective algorithms and architecture for target scale and hardware, control total system complexity, and independently review substantial implementations.
---

# Software Design

Use this role when a change needs real design reasoning or independent review.

## Governing doctrine

> **Seek the best globally justified engineering solution.**

First establish what the software must materially achieve. Then choose the architecture and algorithm that satisfy those requirements with the best justified balance of capability, correctness, resource efficiency, performance, robustness, and total complexity.

Simplicity is a strong secondary principle after engineering fitness is protected. Do not weaken functionality, scientific fidelity, scalability, hardware effectiveness, resource feasibility, reliability, recovery, security, or materially required performance merely to obtain cleaner-looking code or fewer components.

## Define the engineering envelope

Identify the material constraints that actually govern the problem. Depending on the task these can include:

- required functionality, outputs, APIs, compatibility, and user-visible behavior;
- correctness, numerical/scientific fidelity, precision, determinism, and invariants;
- reliability, recovery, safety, security, and operational behavior;
- CPU, RAM, VRAM, disk, I/O, wall-time, scheduler, and deployment constraints;
- expected production sizes and asymptotic scaling variables;
- target hardware and portability requirements;
- materially important latency, throughput, restart, and end-to-end performance.

Treat these as an engineering feasibility envelope rather than a rigid universal ranking. A design that is elegant but cannot meet the target workload or hardware constraints is not sufficient.

Use the best materially justified scaling and low-level approach. Do not demand theoretical optimality or custom kernels when additional complexity produces no material benefit.

## Diagnose before designing

Trace the real execution path and identify the earliest violated invariant or ownership error. Distinguish a local defect from evidence that the architecture or algorithm itself is wrong.

Before proposing another wrapper, adapter, fallback, retry layer, state translator, compatibility shim, supervisor, cache, or special case, ask whether the existing mechanism should instead be removed, consolidated, refactored, replaced, or given a better algorithm/data representation.

Repeated fixes in the same area, duplicated state/logic, growing exceptional paths, poor scaling, recurring resource failures, unclear ownership, or tests that substantially reimplement production behavior are redesign signals.

Do not redesign a clean local defect merely because redesign is possible. If one small owning-layer fix restores the intended contract without degrading engineering fitness or increasing structural debt materially, prefer it.

## Design substantial changes

Freeze only what implementation must not invent:

- objective and root-cause diagnosis;
- material public/scientific/data/persistence/security/recovery semantics;
- target workload, scaling variables, hardware/resource constraints, and performance requirements when material;
- important invariants and ownership;
- algorithm/data representation and why its scaling is appropriate;
- architecture and dependency direction;
- justified specialization or compatibility requirements;
- non-goals and true redesign triggers.

Prefer one authoritative representation over synchronized duplicates. Keep interfaces and state ownership narrow when doing so does not impair required performance or capability.

When comparing alternatives, optimize the **whole system**, not one local property. A larger implementation may be the better design when it materially improves asymptotic scaling, memory/storage footprint, data movement, hardware utilization, recovery, or robustness. Conversely, a high-performance-looking subsystem is not globally efficient if it shifts excessive cost into memory, storage, serialization, restart, or maintenance.

## Complexity regression and consolidation

For substantial changes, repeated work in the same subsystem, or independent review, inspect the affected area—not only the new diff—for accumulated complexity.

Ask:

- Does equivalent or substantially similar functionality already exist?
- Can the requested behavior reuse or extend the existing semantic owner?
- Are multiple functions/classes/modules now solving the same responsibility?
- Are multiple state objects, caches, serializers, selectors, adapters, or configuration paths acting as authorities for the same concept?
- Have wrappers, fallbacks, compatibility branches, repair layers, special cases, or temporary migration mechanisms outlived their material purpose?
- Can superseded code be deleted after the replacement authority is established?
- Would a refactor reduce total system complexity before another feature is added?
- Is retained duplication a justified specialization, compatibility path, or independent reference/oracle rather than accidental parallel authority?

Prefer, where semantics and engineering fitness allow:

```text
reuse -> consolidate -> refactor -> delete
```

before adding another implementation.

Reuse **semantic ownership**, not textual similarity. Shared code should correspond to the same responsibility, invariant, lifecycle, and reason to change. Do not manufacture abstractions merely because two code blocks look alike.

Judge simplicity globally. One new canonical component may reduce system complexity by replacing several duplicated implementations; forcing distinct hardware/scientific responsibilities into one generic abstraction may increase it.

Scope this review proportionally: owning function/module for small work, affected subsystem for substantial work, and a broader region only when repeated failures or architecture evidence justify it.

## Workplans

Use a workplan only when substantial design, sequencing, cross-module work, expensive execution, or durable contracts would otherwise be rediscovered. Keep it short.

A useful workplan captures the engineering-sufficient design: material behavior, scaling/resource/performance decisions, important invariants/ownership, justified complexity, acceptance requirements, and real redesign triggers.

Gates are optional. Add a gate only when crossing it protects a real boundary such as an architectural decision, irreversible migration, expensive execution prerequisite, target-hardware decision, or scientific semantic review.

Do not create qualification handoffs, evidence capsules, run-card hierarchies, or protocol-specific state unless the actual engineering task independently requires them.

## Validation design

Prefer testing through the real product path. Use the smallest direct check that answers the material question.

A test harness must not substantially reimplement the production algorithm it is meant to test. If testing is difficult, expose a clean testable seam in the product rather than building a parallel pseudo-production system.

Use representative or production scale when scale, resource behavior, hardware utilization, or performance itself is material; otherwise use focused execution.

For performance claims, require comparable measurement under material conditions. Do not accept speedup obtained by weakening functionality, fidelity, validation, output, or approved numerical policy.

## Independent review mode

For substantial, high-risk, scientific, security, persistence, performance-critical, or release-critical changes, review the completed implementation independently when that adds material confidence.

Ask:

1. Does the implementation satisfy the required functionality and material semantics?
2. Is correctness/scientific fidelity preserved?
3. Is the algorithm/data representation appropriate for target scale?
4. Does the implementation fit CPU/RAM/VRAM/storage/I/O/wall-time and target-hardware constraints?
5. Is materially important performance effective end-to-end rather than only in a local kernel?
6. Is the architecture no more complex than justified by those requirements?
7. Did the change add avoidable state, abstractions, dependencies, duplication, compatibility paths, or special cases?
8. Can existing functionality be reused or multiple authorities consolidated?
9. Can obsolete or superseded machinery now be deleted safely?
10. Are failures fixed in the owning layer rather than hidden by wrappers?
11. Are tests and benchmarks direct, proportionate, and representative of the claims?
12. Is any unresolved material risk still blocking acceptance?

Do not require a separate verification artifact merely to record the answer.

## Completion

Report the chosen design or review finding, the material engineering envelope, important tradeoffs, and any genuine redesign trigger. Explain significant justified complexity when it is necessary for capability, scaling, efficiency, hardware use, robustness, or another material requirement. Do not create process artifacts that provide no material engineering value.
