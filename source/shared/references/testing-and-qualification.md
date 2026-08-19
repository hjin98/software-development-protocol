# Testing, Qualification, and Verification

## Terminology and role boundary

Protocol v3 distinguishes:

- **test/check** — executable or inspectable mechanism producing evidence;
- **qualification** — source-bound execution of required checks in a declared environment;
- **verification** — independent review that exact candidate content plus evidence satisfies the frozen workplan/current contracts and deserves acceptance.

Implementation authors tests/harnesses and may run cheap available checks. `software-qualification` owns declared target-environment execution/evidence. `software-verification` decides final acceptance.

## Evidence ladder

Run proportional checks from cheap/local to broad:

1. **Structural sanity** — syntax/import/compile, formatter/linter/type, schema/config, generated-file/document parity.
2. **Focused behavior** — unit/regression/boundary/malformed-input/deterministic-error tests.
3. **Contract/oracle/property** — trusted oracle, randomized/property, metamorphic/invariance, tolerance-qualified numerical equivalence.
4. **Consumer/integration** — final observable behavior through affected consumers, including persistence/state sequences.
5. **Broad regression/distribution** — subsystem/full suite, controlled build, artifact inspection, isolated install, installed behavior.
6. **Production/environment qualification** — real data, realistic scale, target accelerators/HPC/services/user workflows.

Do not compare only digests/state when two wrong implementations could agree.

## Evidence states

Each required check is exactly one of:

- `PASS`
- `FAIL`
- `BLOCKED`
- `NOT RUN`
- `DEFERRED`

A blocked/not-run check is not a pass.

For `DEFERRED`, record:

```yaml
mandatory_for_current_acceptance: true|false
deferred_to: <workplan/release/milestone>
reason: <why>
```

A deferred check mandatory for current acceptance blocks final acceptance.

Implementation may prepare later independent gates while qualification is pending only when `qualification_barrier: no`. Verification never converts missing mandatory evidence into PASS.

## Qualification candidate identity

Read `protocol-versioning-and-compatibility.md`.

A Qualification Handoff binds:

```text
candidate_commit
candidate_content_identity
candidate_identity_policy
workplan identity/digest
```

Before executing:

- verify checkout provenance and candidate content identity;
- verify no staged/tracked modifications on candidate surfaces;
- reject undeclared untracked files capable of affecting import/build/runtime;
- verify submodule/LFS state when applicable;
- control/record cwd and import/source origin where material;
- verify required inputs/environment/hardware.

After execution, recompute candidate identity and verify only declared ephemeral/write paths changed.

`HEAD == candidate_commit` alone is not sufficient source identity.

## Qualification output classes

- `EPHEMERAL_QUALIFICATION_OUTPUT` — logs, reports, build scratch, temporary packages, profiles, benchmark outputs and similar non-product evidence. May be written only in declared paths.
- `TRACKED_CANDIDATE_OUTPUT` — tracked generated product/release artifacts included in candidate identity. Qualification must not create/change them.

If target execution is needed to generate a tracked product artifact, produce it only as proposed ephemeral output, return to implementation, commit a new candidate and rerun affected qualification.

## Regression design

- Test the failure mechanism, not only the reported example.
- Keep tests deterministic/small by default; mark slow/external tests distinctly.
- Avoid incidental implementation-detail assertions unless contractual.
- For caches/schedulers/concurrency, test state transitions, invalidation, retries/backoff, deterministic ordering, interrupted/partial state and restart/resume.
- For parsers, include malformed, ambiguous, empty/minimal, boundary and representative real fixtures.
- For compatibility, retain historical supported forms.

## Numerical/scientific verification

- Define exact equality versus justified absolute/relative tolerance per quantity.
- Compare meaningful final observables as well as intermediate kernels when both matter.
- Test invariants such as conservation, symmetry, periodicity, positive-definiteness, normalization and monotonicity.
- Record precision/dtype/backend when material.

## Performance qualification

Correctness precedes performance.

- Warm JIT/GPU/cache paths where relevant.
- Use repeated measurements and robust summaries; include dispersion when decisions are close.
- Record input size/distribution, environment, versions, threads/workers, backend, precision and memory metric.
- Compare runtime, peak/transient memory and I/O/disk footprint when tradeoffs matter.
- Benchmark representative and adversarial workloads; include cold/warm/restart paths when production-relevant.
- Keep conservative crossover/default policy and explicit fallback.

Authenticated baseline evidence may be reused only when the governing source/input/method/environment comparability dimensions remain compatible.

## Evidence dependencies and reuse

Expensive check reuse must be dependency-bound.

Declare as applicable:

```yaml
evidence_dependencies:
  source_paths: []
  candidate_identity_components: []
  config_identity: []
  inputs: []
  environment_dimensions: []
  upstream_checks: []
```

After candidate/config/input/environment change:

- invalidate checks whose dependencies intersect the change;
- preserve unrelated evidence only when dependency compatibility is explicit;
- if dependency is ambiguous, rerun by default;
- record reuse rationale in the Qualification Report;
- let verification audit nontrivial reuse.

Do not reuse evidence because branch/file/session names happen to match.

## Retry semantics

Each check declares one retry mode:

- `NONE`
- `IDENTICAL_RETRY`
- `CLEAN_RETRY`
- `RESUME_RETRY`

Record every attempt, cleanup/resume state, command/config identity and result.

A retry that changes candidate content or undeclared scientific/config/resource/backend/dataset policy is not a retry under the same handoff. Issue a new handoff or request design revision.

Deleting caches/checkpoints before retry is allowed only when the handoff's `CLEAN_RETRY` policy explicitly authorizes that state cleanup. Resuming is allowed only under declared `RESUME_RETRY` state semantics.

## Persistence and recovery qualification

When material persisted state changes, test proportional risks:

- stale identity/incompatible schema;
- truncated/partial/corrupt artifact;
- interrupted publication;
- restart from latest valid state and equivalence with uninterrupted execution;
- cache hit/miss/invalidation reason;
- storage admission/low-space where feasible;
- concurrent writer/cache collision;
- cleanup preserving authoritative/external inputs.

A clean-start test is not evidence for resumability.

## Security/trust-boundary qualification

When material trust boundaries change, test archive path/symlink escape, unsafe-deserialization rejection, subprocess argv handling, secret redaction, output-root enforcement, malformed-resource admission, stale/tampered persistence and renderer/plugin restrictions as applicable.

Do not claim absolute security; state exercised boundaries/failure modes.

## Configuration and orchestration qualification

When configuration/concurrency changes, test canonical precedence/default/override resolution, stable resolved-config identity, semantic cache invalidation, serial-vs-concurrent equivalence/order, failure propagation, bounded retry/backoff, cancellation/preemption/cleanup, backpressure/resource ownership and READ/MIGRATE/REJECT compatibility.

## Release/distribution qualification

For distributable candidates, build from controlled candidate content, inspect artifact contents, install into an isolated environment and exercise installed behavior outside the checkout. Candidate specification/architecture/history/version/package/tracked generated product artifacts should already belong to the candidate identity or be returned to implementation before acceptance.

## Verification acceptance review

After qualification, `software-verification` independently checks:

- every mandatory acceptance clause maps to executed evidence at the required capability;
- candidate content identity and dirty-tree/source-origin evidence are coherent;
- evidence reuse dependencies justify any retained old result;
- retries stayed within declared policy;
- blocked/not-run/blocking-deferred checks are represented honestly;
- performance claims are comparable and include material setup/I/O/recovery costs;
- release/install/documentation evidence applies to the exact candidate content identity.

A Qualification Report is evidence, not self-validating authority.
