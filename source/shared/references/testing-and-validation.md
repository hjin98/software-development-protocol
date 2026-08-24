# Testing and Validation

Testing exists to establish product behavior and engineering claims with appropriate confidence. It is not a parallel product or approval bureaucracy.

## Functional acceptance for executable changes

Every executable product change requires:

1. **Focused checks** appropriate to new/modified mechanisms: unit, property, numerical, boundary, error, or bug-reproducer tests.
2. **Affected-surface regression** covering all new/modified behavior and every existing behavior that could plausibly change because of the revision.
3. **Integration testing** through the assembled affected product path and relevant real consumer/interface/state-transition boundaries.

The affected surface is not limited to changed files. Include callers/consumers, shared utilities, public interfaces, configuration, persistence, caches/checkpoints, orchestration/concurrency paths, packaging/entry points, and transitive behavioral dependencies where the change can plausibly propagate.

Do not require one test per function/file. Existing tests count when they genuinely protect the relevant contract; add coverage where they do not.

A required check that did not execute is not a pass. Newly introduced failures and failures plausibly intersecting the affected surface block functional acceptance. Demonstrably pre-existing unrelated failures may be attributed and reported rather than repaired.

## Optimize test cost, not coverage

Coverage breadth follows the affected behavioral surface. Then minimize execution cost while preserving that coverage.

Prefer small deterministic fixtures, bounded datasets, reduced iterations/epochs, synthetic inputs, and representative workloads when they exercise the same contracts. A broad regression suite can be inexpensive if each path is tested with bounded data.

Do not interpret “small,” “focused,” or “representative” as permission to omit affected modules, consumers, interfaces, or integration boundaries.

## Stage-local testing

After a material implementation stage changes executable behavior, run the focused checks and affected regression subset whose early execution materially reduces defect propagation, debugging ambiguity, rework, or downstream risk.

Do not duplicate identical checks ceremonially for an atomic change. Conversely, do not defer all testing to the end merely to minimize the number of test executions when intermediate checks materially improve fault localization or reduce wasted work.

Before completion, run a final assembled affected-surface regression pass and integration pass after all material executable changes that could invalidate earlier evidence.

## Prefer direct testing

Test through the actual implementation/product path whenever practical. A harness must not substantially reimplement the algorithm, state reconstruction, orchestration, or compatibility logic it is intended to test.

Synthetic fixtures are useful for bounded execution; they do not replace real integration boundaries when those boundaries are part of the functional claim.

## Production qualification

Full production qualification is distinct from functional testing. It assumes regression and integration acceptance already passed and uses real, long, data-heavy, target-machine/target-hardware workloads to characterize production-scale wall time/throughput, RAM/VRAM/storage/I/O, scaling, accelerator utilization, recovery cost, and related environment-specific behavior.

Do not run full production qualification by default during implementation or between ordinary stages. Run it only when explicitly requested, required by project/release policy, or necessary to establish a material production-scale/resource/performance/hardware claim.

Bounded benchmarks, accelerator smoke tests, reference-equivalence checks, and representative resource checks remain normal implementation validation when relevant.

## Resource safety

Honor explicit CPU/RAM/VRAM/storage/I/O/wall-time constraints. Do not exhaust the machine to prove basic functionality. Use bounded failure simulations rather than actual resource exhaustion when they establish the same behavior.

## Domain-specific tests

Security, persistence/recovery, concurrency, configuration, scientific/numerical, performance, packaging, and other specialized test guidance augments this protocol-wide regression/integration contract; it does not replace it.

## Evidence

Command output, CI results, benchmark output, or run logs are normally sufficient evidence. Record only metadata needed to interpret the material claim. Do not create qualification/evidence machinery merely for ceremony.
