# Testing and Validation

Testing exists to establish product behavior and engineering claims with appropriate confidence. It is not a parallel product or approval bureaucracy, and it does not by itself establish that every accepted implementation obligation was performed.

## Functional acceptance for executable changes

Every executable product change requires:

1. **Focused checks** appropriate to new/modified mechanisms: unit, property, numerical, boundary, error, or bug-reproducer tests.
2. **Affected-surface regression** covering all new/modified behavior and every existing behavior that could plausibly change because of the revision.
3. **Integration testing** through the assembled affected product path and relevant real consumer/interface/state-transition boundaries.

The affected surface is not limited to changed files. Include callers/consumers, shared utilities, public interfaces, configuration, persistence, caches/checkpoints, orchestration/concurrency paths, packaging/entry points, documentation/contracts, and transitive behavioral dependencies where the change can plausibly propagate.

Do not require one test per function/file. Existing tests count when they genuinely protect the relevant contract; add coverage where they do not.

Repository/project-required checks remain mandatory. If impact analysis cannot confidently bound the affected surface, run the broader/full available regression suite rather than treating unexamined consumers as unaffected.

A required check that did not execute is not a pass. Newly introduced failures and failures plausibly intersecting the affected surface block functional acceptance. Demonstrably pre-existing unrelated failures may be attributed and reported rather than repaired.

## Conformance and testing are complementary

For work governed by an accepted implementation contract, functional evidence and semantic/workplan conformance answer different questions:

- conformance establishes that the required obligations, protected concerns, and frozen decisions were actually realized or legitimately reconciled;
- testing establishes that the resulting behavior works across the required affected surface.

Green tests do not prove an omitted obligation was implemented. Source/conformance inspection does not replace executable regression/integration.

For removal, uniqueness, ownership, or no-legacy-path claims, use structural/source inspection or negative/absence assertions when runtime tests cannot establish the claim directly.

## Optimize test cost, not coverage

Coverage breadth follows the affected behavioral surface. Then minimize execution cost while preserving that coverage.

Prefer small deterministic fixtures, bounded datasets, reduced iterations/epochs, synthetic inputs, and representative workloads when they exercise the same contracts. A broad regression suite can be inexpensive if each path is tested with bounded data.

Do not interpret “small,” “focused,” or “representative” as permission to omit affected modules, consumers, interfaces, or integration boundaries.

## Coherent stage granularity and dual closure

A material implementation stage is a coherent behavior-changing unit. It may include several tightly coupled helper/caller/fixture edits whose behavior is only meaningful as one assembled stage. Do not create a separate stage-local regression gate for every file/function edit unless it independently changes executable behavior or forms a useful risk boundary.

Before dependent implementation proceeds, the stage must achieve both:

1. **semantic/conformance closure** of the obligations assigned to that stage; and
2. **functional closure** — focused checks plus the required affected regression subset for executable behavior.

Use the cheapest high-information order within the stage. Cheap focused checks prevent spending broader test cost on obvious local defects, but do not substitute for the affected regression. Obvious conformance defects may likewise be repaired before test cost is spent.

## Stage-local affected regression

After **each material implementation stage that changes executable behavior**, run focused checks and the required **stage-local affected regression** subset relevant to that stage before dependent implementation proceeds. Resolve newly introduced hard failures and affected regressions at the stage that introduced them.

A tiny atomic change may use the final pass as its stage pass. A genuinely non-executable intermediate stage may combine validation with the nearest executable integration stage when that dependency is explicit. Do not defer all regression to final completion merely because a later suite will eventually exercise the code.

This requirement preserves fault localization and prevents defect accumulation; it is not optional based only on whether an agent predicts that intermediate testing will be useful.

## Evidence reuse and invalidation

Reuse still-valid intermediate evidence instead of rerunning it merely because time passed, a new agent session began, or unrelated files changed.

Rerun a check when a changed dimension can plausibly alter the result or interpretation. Examples:

- documentation-only wording does not invalidate an unrelated numerical regression result;
- executable refactoring invalidates regression evidence for behavior that could be affected;
- serialization changes invalidate relevant persistence/compatibility evidence but not an unrelated mathematical oracle;
- GPU execution-policy changes invalidate affected GPU equivalence/performance evidence without automatically invalidating an unchanged CPU reference result.

Evidence reuse is an intermediate development-economy optimization. It never removes final assembled acceptance requirements and never turns an unexecuted required check into a pass.

## Final assembled acceptance

Before functional completion:

1. implementation first completes final accepted-contract reconciliation and accounts for material structural/absence claims;
2. re-derive the affected behavioral surface from the final assembled implementation;
3. account for every identified affected path with executed regression coverage, a required broader suite, or an explicit unavailable/blocking check;
4. rerun the complete affected-surface regression after all material executable edits that could invalidate earlier evidence;
5. run integration/end-to-end tests through the assembled affected product path on the same candidate.

Implementation can broaden impact beyond the initial plan, so initial impact analysis is not sufficient final evidence.

## Prefer direct testing

Test through the actual implementation/product path whenever practical. A harness must not substantially reimplement the algorithm, state reconstruction, orchestration, or compatibility logic it is intended to test.

Synthetic fixtures are useful for bounded execution; they do not replace real integration boundaries when those boundaries are part of the functional claim.

## Production qualification

Full production qualification is distinct from functional testing. It assumes regression and integration acceptance already passed and uses real, long, data-heavy, target-machine/target-hardware workloads to characterize production-scale wall time/throughput, RAM/VRAM/storage/I/O, scaling, accelerator utilization, recovery cost, and related environment-specific behavior.

Do not run full production qualification by default during implementation or between ordinary stages. Run it only when explicitly requested, required by project/release policy, or necessary to establish a material production-scale/resource/performance/hardware claim.

Bounded benchmarks, accelerator smoke tests, reference-equivalence checks, and representative resource checks remain normal implementation validation when relevant.

A successful production run never substitutes for missing focused/regression/integration coverage. Bounded functional testing does not prove production-scale performance/resource qualification.

## Resource safety

Honor explicit CPU/RAM/VRAM/storage/I/O/wall-time constraints. Do not exhaust the machine to prove basic functionality. Use bounded failure simulations rather than actual resource exhaustion when they establish the same behavior.

## Domain-specific tests

Security, persistence/recovery, concurrency, configuration, scientific/numerical, performance, packaging, and other specialized test guidance augments this protocol-wide regression/integration contract; it does not replace it.

## Evidence

Command output, CI results, benchmark output, source inspection, or run logs are normally sufficient evidence. Record only metadata needed to interpret the material claim. Do not create qualification/evidence machinery merely for ceremony.
