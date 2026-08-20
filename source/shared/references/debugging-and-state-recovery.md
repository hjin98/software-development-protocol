# Debugging and Stateful Recovery

## Diagnose before patching

For nontrivial failures:

1. reproduce the smallest trustworthy failure when practical;
2. trace the actual execution path and authoritative state;
3. identify the earliest violated invariant;
4. classify the owning cause rather than the final symptom;
5. fix the owning layer;
6. add the narrowest regression evidence that protects the mechanism.

Do not repeatedly patch downstream symptoms.

## Complexity as a diagnostic signal

Repeated failures in the same area can indicate design debt rather than independent bugs.

Stop adding machinery and reconsider the design when fixes increasingly require wrappers, adapters, retries, compatibility shims, duplicate state, translation layers, broad exception handling, or test-only reconstruction of production behavior.

Prefer consolidation, deletion, refactoring, or replacement when it removes the root failure surface.

Do not redesign a simple local bug if a small clean fix restores the intended contract.

## Stateful systems

Persist only state that materially needs persistence. Prefer derivable state over synchronized duplicates when recomputation is reasonable.

When durable state matters:

- define its owner and validity boundary;
- distinguish complete, partial, stale, corrupt, and incompatible forms when those states can occur materially;
- publish completion only after authoritative outputs are valid;
- make retries/restart semantics bounded and unambiguous;
- reject or migrate incompatible state rather than silently treating it as current.

Do not create a state machine merely to manage incidental files when a simpler atomic output or checkpoint is sufficient.

## Real-world failures

When a production input exposes a bug, preserve or reduce a fixture when useful, identify the general invariant, fix the owner, run focused tests, and rerun the affected real path when materially needed.

Avoid parallel diagnostic programs that duplicate the product. Instrument the product or expose a small testable seam instead.

## Recovery testing

Test the actual state transition that matters: interruption/restart, stale-state rejection, corrupt-state handling, migration, or equivalence with uninterrupted execution.

A recovery test need not replay the entire production workflow when the relevant transition can be exercised directly.

## Anti-patterns

- catching broad exceptions and continuing with stale/partial output;
- deleting caches until a failure disappears without finding the invalidation bug;
- retrying resource/I/O failures indefinitely;
- using file existence as proof of completion;
- adding another translation/fallback layer instead of fixing ownership;
- building a second implementation solely to diagnose the first.

## Completion

Record root cause, owning-layer fix or redesign, relevant regression evidence, state compatibility impact when any, and whether the original material failure path was retested.
