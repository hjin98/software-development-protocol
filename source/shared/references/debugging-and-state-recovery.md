# Debugging and Stateful Recovery

## Diagnose before patching

For nontrivial failures:

1. reproduce a bounded trustworthy failure when practical;
2. trace the actual execution path and authoritative state;
3. identify the earliest violated invariant;
4. classify the owning cause rather than the final symptom;
5. fix the owning layer;
6. add focused regression evidence for the defect;
7. run the affected-surface regression and integration checks required by `testing-and-validation.md`.

A reduced reproducer is a diagnostic aid, not a reason to narrow final regression coverage.

## Complexity as a diagnostic signal

Repeated failures in the same area can indicate product/design debt rather than independent bugs. Reconsider the design when fixes increasingly require wrappers, adapters, retries, compatibility shims, duplicate state, translation layers, broad exception handling, or test-only reconstruction of production behavior.

Prefer consolidation, deletion, refactoring, or replacement when it removes the root failure surface. Do not redesign a simple local bug if a clean owning-layer fix restores the contract.

## Stateful systems

Persist only state that materially needs persistence. Prefer derivable state over synchronized duplicates when recomputation is reasonable.

When durable state matters:

- define owner and validity boundary;
- distinguish complete, partial, stale, corrupt, and incompatible forms where material;
- publish completion only after authoritative outputs are valid;
- make retry/restart semantics bounded and unambiguous;
- reject or migrate incompatible state rather than silently treating it as current.

## Real-world failures

When production input exposes a bug, preserve/reduce a fixture when useful, identify the general invariant, fix the owner, run focused tests, run affected regression/integration, and rerun the original real path when materially needed to establish that production-specific dimension.

Do not build a second implementation solely to diagnose the first. Instrument the product or expose a clean test seam instead.

## Recovery testing

Test the actual state transitions that matter: interruption/restart, stale-state rejection, corrupt-state handling, migration, or equivalence with uninterrupted execution. Bounded fixtures are preferred when they preserve the transition semantics.

Recovery-specific checks augment, rather than replace, protocol-wide affected regression and integration requirements.

## Completion

Record root cause, owning-layer fix/redesign, focused reproducer coverage, affected regression/integration evidence, state compatibility impact, and whether any original production-specific failure path was retested or explicitly deferred.
