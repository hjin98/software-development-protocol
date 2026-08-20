# Architecture and Design

Architecture should make the software easier to reason about, change, and validate. It is not a place to maximize abstraction.

## Minimum Mechanism Principle

For designs that satisfy the same material requirements, prefer the one with fewer components, states, interfaces, dependencies, synchronization points, and special cases.

Complexity is a liability unless it buys a material capability. Count not only lines of code but also conceptual surface: ownership rules, configuration, persistence, fallbacks, concurrency, compatibility paths, and workflow machinery.

Necessary complexity remains valid when it protects correctness, scientific fidelity, performance, security, recovery, compatibility, or another material requirement.

## Architecture review

For a nontrivial feature, algorithm, persistence model, concurrency design, or structural refactor, define only what materially matters:

1. problem/root cause and objective;
2. scope and non-goals;
3. important invariants/conventions;
4. authoritative state and ownership;
5. algorithm/data flow and material complexity/scaling;
6. interfaces and dependency direction;
7. failure/recovery/security/resource behavior where relevant;
8. acceptance-critical behavior;
9. materially plausible simpler alternatives.

Reject a design when it violates a hard invariant, cannot meet material scale/reliability requirements, creates unclear ownership, duplicates authoritative state without need, or adds complexity without a material benefit.

## Simplicity review

Before accepting new machinery, ask:

- Can an existing component own this responsibility?
- Can state be derived instead of persisted?
- Can two paths be collapsed into one?
- Can a special case be removed by fixing the underlying abstraction?
- Can a standard or existing library mechanism replace custom infrastructure?
- Can obsolete code be deleted as part of the change?
- Is a new helper/module/class actually clearer than direct code?

Do not turn these questions into a numerical complexity score. Engineering judgment is the point.

## Redesign boundary

A local bug with a local cause should receive a local clean fix.

Redesign when repeated fixes accumulate around the same mechanism, ownership is wrong, duplicated state or logic causes failures, compatibility/fallback layers proliferate, testing requires parallel reconstruction of production behavior, or the current algorithm cannot meet material requirements cleanly.

Do not stabilize bad architecture by surrounding it with more architecture.

## Architecture documentation

Permanent architecture documentation describes accepted current structure: ownership, interfaces, data/control flow, important invariants, durable persistence/concurrency/security/resource boundaries, and accepted algorithms.

Do not put gate logs, temporary benchmark plans, task status, chronological implementation history, or speculative future machinery into the architecture manual.

Proposed transitions belong in a concise workplan until accepted. Update the normative architecture only after the implementation actually changes it.
