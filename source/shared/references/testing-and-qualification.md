# Testing, Qualification, and Verification

## Purpose

Testing produces evidence. Qualification executes the checks that materially matter in the required environment. Verification decides whether the candidate plus evidence satisfies the workplan.

The protocol prioritizes confidence in software correctness over completeness of qualification paperwork.

## Evidence ladder

Use checks proportionally:

1. structural sanity: syntax/import/compile/schema where useful;
2. focused behavior: unit/regression/boundary/error tests;
3. oracle/property/numerical invariants;
4. consumer/integration/persistence sequences;
5. broad regression and distribution checks;
6. production data, scale, target hardware, services, and user workflows.

Not every task requires every level.

## Check states

A required check is one of:

```text
PENDING
PREPARED
PASS
FAIL
BLOCKED
```

A mandatory check that did not execute cannot be called PASS.

Future-release checks that are not required for current acceptance should be listed separately rather than encoded as deferred acceptance states.

## Materiality and failure routing

### Product/material failure

A check demonstrates incorrect behavior, candidate-caused regression, scientific/numerical mismatch, broken persistence/recovery, security failure, install/package failure, unacceptable resources, or missed performance threshold.

Return to implementation, or to design when the accepted target itself must change.

### Environment blocker

A required dataset, service, compiler, credential, accelerator, machine, or other execution prerequisite is unavailable. Mark `BLOCKED`.

### Harness/record problem

A command has the wrong cwd, quoting, scratch path, log destination, environment activation syntax, or unambiguous intended config path; or an evidence report has a non-material metadata error.

Qualification may correct these locally and continue when candidate behavior, material inputs/configuration/environment, and acceptance semantics stay unchanged. Record the actual conditions used.

## Candidate execution boundary

For Git projects, identify the candidate by commit and ensure execution is not unintentionally shadowed by modified/untracked product source. Control cwd/import origin when it materially affects what code is tested.

Qualification may create logs, build outputs, wheels, reports, profiles, benchmark data, cloned scratch databases, and temporary files. It must not silently modify product-defining source/config/test/spec files and still claim to have qualified the original candidate.

Additional hashes are used only for material external/generated content boundaries.

## Broad regression policy

A zero-failure full suite is a hard gate only when:

- the repository maintains it as a green gate; or
- the workplan/release policy explicitly makes global green status mandatory.

Otherwise run broad tests when useful and attribute failures:

- candidate-caused or plausibly candidate-caused failure -> blocking;
- clearly pre-existing unrelated failure -> repository-health finding, not automatic candidate failure;
- uncertain failure affecting the changed surface -> investigate or rerun until attribution is adequate.

Do not create elaborate historical test trees solely to compensate for an already-red repository.

## Scientific and numerical qualification

When material:

- define exact equality or justified tolerances;
- compare meaningful final observables as well as kernels where needed;
- test invariants such as conservation, symmetry, periodicity, normalization, positivity, or monotonicity;
- record precision/backend only when it affects interpretation;
- use representative real data when small fixtures cannot establish validity.

Do not weaken fidelity merely to make qualification cheaper.

## Persistence and recovery

When persisted state changes materially, test proportional risks:

- stale/incompatible state;
- truncated/corrupt state;
- interrupted publication;
- restart from latest valid state;
- equivalence with uninterrupted execution;
- migration/read/reject behavior;
- storage/resource behavior when it is part of the design.

A clean-start test is not evidence for resumability.

## Performance qualification

Correctness precedes performance.

For a comparative claim, use a trustworthy comparable baseline and material conditions: representative workload, backend, thread/resource policy, precision, and setup/I/O/recovery costs where relevant.

Use repeated measurements when noise could change the decision. Record memory/I/O when the workplan makes them important.

If no trustworthy baseline exists, report absolute performance and do not claim a relative speedup. Do not manufacture an elaborate counterfactual solely to preserve a percentage or speedup claim.

## Distribution qualification

When shipping a package/artifact:

- build from the intended candidate;
- inspect artifact contents where relevant;
- install in an isolated target;
- exercise installed behavior outside the source checkout;
- verify user-visible version only when version identity is part of the deliverable;
- test entry points/resources that users rely on.

## Security/trust qualification

When trust boundaries changed materially, test the applicable boundary: path/archive escape, unsafe deserialization, subprocess handling, credentials/secrets, dependency/plugin behavior, tampered persistence, untrusted rendering, or other project-specific risks.

Do not invent generic security gates unrelated to the change.

## Reruns and evidence reuse

Rerun a check when a changed candidate/input/config/environment dimension could plausibly affect its result or interpretation. Do not rerun because an advisory report/hash/path field changed.

Expensive workflows may keep a dependency map when it saves substantial rerun cost, but the map is optional and must not become a second acceptance system.

## Verification

Verification asks:

1. did implementation conform to material frozen design;
2. did every acceptance-critical requirement receive adequate executed evidence;
3. are failures attributable correctly;
4. are scientific/performance/recovery/security claims supported;
5. did qualification exercise the intended candidate under material conditions;
6. is any unresolved material risk blocking acceptance.

Final decision:

```text
MERGE_READY
NOT_READY
DESIGN_REVISION_REQUIRED
```

A report is evidence, not authority. Administrative metadata completeness is not a substitute for software evidence and is not a reason to discard valid evidence by itself.
