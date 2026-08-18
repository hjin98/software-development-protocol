# Testing, Verification, and Qualification

## Evidence ladder

Choose checks proportional to the change, then run from local to broad so failures are cheap to diagnose.

### Level 1 - Structural sanity

- syntax/import/compile checks;
- formatter/linter/type checks used by the repository;
- schema/config validation;
- generated-file consistency checks;
- documentation parity checks: current specification vs accepted implemented signatures/defaults where automatable, current architecture parity where architecture changed, and Markdown/PDF content-provenance manifest verification.

### Level 2 - Focused behavior

- unit tests for changed functions/classes;
- regression test reproducing each bug;
- boundary and malformed-input cases;
- deterministic error/warning behavior.

### Level 3 - Contract/oracle/property verification

Use when correctness is broader than example fixtures:

- compare optimized/new backend against a trusted reference/oracle;
- randomized/property tests over valid input spaces;
- metamorphic/invariance tests (permutation, basis, coordinate, serialization round-trip, etc.);
- tolerance-qualified numerical equivalence with justified tolerances;
- fixed seeds plus reproduction payloads for randomized failures.

Do not compare only digests/state if two wrong implementations could agree.

### Level 4 - Consumer/integration verification

Test final observable behavior through affected consumers, not only low-level kernels. Include multi-step state/caching/persistence sequences when applicable.

### Level 5 - Broad regression and distribution

Run subsystem/full tests when the change surface warrants it. For distributable changes, read `release-and-distribution.md`: build from a controlled/clean source state, inspect produced artifact contents, install into an isolated environment, and exercise the installed artifact outside the checkout. Complete documentation/version closeout: reconcile specification with code, update architecture only for actual accepted architectural changes, update history/version metadata, regenerate changed permanent Markdown PDFs/provenance manifests, run content-provenance checks, and verify representative rendered pages. Bind release evidence to the governing workplan identity when applicable.

### Level 6 - Production-like/environment-specific qualification

Use real data, realistic sizes, target accelerators/HPC runtime, external services, or user workflows only after internal gates pass. Record exact environment and artifact versions.

## Blocking semantics

Classify each required check as:

- **PASS** - executed and met acceptance criteria;
- **FAIL** - executed and violated criteria;
- **BLOCKED** - required but environment/dependency/data prevents execution;
- **NOT RUN** - intentionally omitted with rationale;
- **DEFERRED** - explicitly outside the current gate/release.

A blocked or not-run check is not a pass. Do not advance a mandatory workplan gate unless its acceptance criteria pass or the design/review role explicitly revises the workplan.

## Regression design

- Test the failure mechanism, not merely the reported example when a broader invariant caused the bug.
- Keep tests deterministic and small by default; mark slow/external tests distinctly.
- Avoid asserting incidental implementation details unless they are intentional contracts.
- For caches/schedulers/concurrency, test state transitions, identity/invalidation, retries/backoff, deterministic output ordering, interrupted/partial state, and restart/resume behavior.
- For parsers, include malformed, ambiguous, empty/minimal, boundary, and representative real-format fixtures.
- For compatibility, test legacy forms as long as they are supported.

## Numerical/scientific verification

- Define exact equality vs absolute/relative tolerance per quantity.
- Compare scientifically meaningful final observables as well as intermediate kernels when both matter.
- Test invariants (conservation, symmetry, periodicity, positive-definiteness, normalization, monotonicity) where they are stronger than fixtures.
- Record precision/dtype/backend in evidence when it affects results.

## Performance qualification

A performance test is not a correctness test. Require correctness first, then benchmark.

- Warm up JIT/GPU/cache paths when relevant.
- Use repeated measurements and robust summaries such as median; include dispersion when decisions are close.
- Record input size/distribution, environment, versions, threads/workers, backend, precision, and memory metric.
- Compare runtime, peak/transient memory, and I/O/on-disk footprint if optimization may trade among them.
- Benchmark representative and adversarial workloads; do not tune only to one convenient fixture. Include cold-load/warm-cache and restart/recovery paths when they materially affect production cost.
- Set automatic crossover/default policy conservatively and keep explicit override/fallback.


## Persistence and recovery verification

When a change creates or reuses material persisted state, add failure/recovery coverage proportional to risk:

- stale identity or incompatible schema/version;
- truncated/partial/corrupt artifact;
- interrupted checkpoint/cache publication;
- restart from the latest valid state and equivalence with uninterrupted execution;
- cache hit/miss/invalidation reason;
- storage admission/low-space failure where feasible;
- concurrent writer/cache-creation collision;
- cleanup that preserves authoritative/external inputs.

Do not treat a clean-start test as evidence that a resumable workflow is correct.

## Production/user acceptance

After all internal gates pass, invite or run a production-like test on real data when it can expose integration, deployment, scale, or domain issues unavailable locally. Treat findings as new evidence: reproduce, fix, add regression coverage, and re-run affected gates.

## Security/trust-boundary verification

When a change crosses a material trust boundary, read `references/security-and-trust-boundaries.md` and add focused tests proportional to the capability exposed. Examples include archive path/symlink escape, unsafe-deserialization rejection, subprocess argv handling, secret redaction, output-root enforcement, malformed-resource admission, stale/tampered persistence, and renderer/plugin restrictions. Do not claim absolute security; report what boundary and failure modes were actually exercised.


## Configuration and orchestration verification

When configuration or concurrent orchestration changes, add evidence proportional to risk:

- canonical precedence/default/override resolution and redaction;
- stable resolved-configuration serialization/digest;
- semantic cache invalidation when configuration changes;
- serial-vs-concurrent equivalence and deterministic ordering;
- worker failure propagation, bounded retry/backoff, cancellation/preemption, and cleanup;
- queue/backpressure/resource-ownership behavior;
- reader/artifact schema READ/MIGRATE/REJECT compatibility where durable state evolves.

Read `configuration-and-policy.md` and `concurrency-and-orchestration.md` for the owning contracts.
