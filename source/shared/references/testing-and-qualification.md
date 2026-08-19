# Testing, Qualification, and Verification

## Terminology and role boundary

Protocol v3 distinguishes the mechanism from the authority decision:

- **test/check** — an executable or inspectable mechanism that produces evidence;
- **qualification** — source-bound execution of required checks in a declared environment, with PASS/FAIL/BLOCKED/NOT RUN/DEFERRED evidence;
- **verification** — independent review that the exact candidate plus qualification evidence satisfies the frozen workplan/current contracts and deserves acceptance.

Implementation normally authors tests/harnesses and may run cheap available checks. `software-qualification` owns target-environment execution/evidence. `software-verification` decides final acceptance. Do not let the same word `verification` ambiguously mean both a unit test and the final acceptance role.


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

Run subsystem/full tests when the change surface warrants it. For distributable changes, read `release-and-distribution.md`: build from a controlled/clean source state, inspect produced artifact contents, install into an isolated environment, and exercise the installed artifact outside the checkout.

For release-significant candidates, qualification should exercise the **staged candidate closeout** rather than inventing it: specification/code parity, architecture only where the target architecture changed, history/version metadata, required generated Markdown/PDF/provenance artifacts, and package contents should already be present in the exact candidate or explicitly declared as generated outputs in the Qualification Handoff. Bind release evidence to the governing workplan and source identity.

### Level 6 - Production-like/environment-specific qualification

Use real data, realistic sizes, target accelerators/HPC runtime, external services, or user workflows only after internal gates pass. Record exact environment and artifact versions.

## Blocking semantics

Classify each required check as:

- **PASS** - executed and met acceptance criteria;
- **FAIL** - executed and violated criteria;
- **BLOCKED** - required but environment/dependency/data prevents execution;
- **NOT RUN** - intentionally omitted with rationale;
- **DEFERRED** - explicitly outside the current gate/release.

A blocked or not-run check is not a pass. It cannot satisfy final gate acceptance.

Implementation may still prepare later independent gates while qualification is pending when the workplan declares `qualification_barrier: no`. A gate with `qualification_barrier: yes` blocks dependent implementation until mandatory qualification passes. Verification never converts missing mandatory evidence into PASS.

## Qualification handoff and source identity

Target-environment qualification should consume a v3 Qualification Handoff rather than a broad workplan instruction. The handoff binds the exact source commit, workplan identity/digest, required capability, command/cwd, inputs, expected result, evidence path, retry policy, and allowed side effects.

Before executing a check:

- verify the candidate source equals the handoff `source_commit`;
- verify required inputs/environment/hardware are available;
- keep product source read-only unless the handoff explicitly declares a generated-output action;
- record exact environment/backend/device/precision when material.

If product source changes, old evidence remains evidence for the old source. Issue a new handoff/report for the new source and rerun checks affected by the delta.

## Expensive qualification batching and evidence reuse

When target-environment execution is expensive:

- batch independent mandatory checks into the smallest number of sessions consistent with fault isolation;
- prepare deterministic commands, fixtures, expected outputs, evidence paths, and failure-capture instructions before handoff;
- reuse authenticated baselines/evidence when the governing comparability identity (source/input/method/environment as applicable) remains compatible;
- after a source correction, rerun the affected dependency set rather than blindly repeating unrelated expensive production checks;
- never reuse evidence merely because a filename, branch name, or agent session is the same.

Cost optimization never authorizes reduced scientific fidelity, smaller substitutes for required production scale, or backend inference unless the workplan explicitly defines those checks as sufficient.

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


## Verification acceptance review

After qualification, `software-verification` should independently check that:

- each mandatory acceptance clause maps to executed evidence at the required capability;
- evidence is bound to the candidate source and governing workplan/handoff;
- new/optimized behavior is compared against an independent oracle/observable where required;
- blocked/not-run/deferred checks are represented honestly;
- performance claims use comparable methodology and do not hide setup/I/O/recovery costs that matter;
- release/install/documentation evidence applies to the exact merge candidate.

A Qualification Report is evidence, not self-validating authority.
