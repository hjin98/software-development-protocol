---
name: software-qualification
description: Execute source-bound software qualification from a Protocol v3 Qualification Handoff. Use for focused/broad test execution, integration/restart/recovery tests, production-data runs, CPU/GPU/HPC/backend qualification, benchmarking/profiling/resource measurement, clean-build/clean-install checks, generated-artifact verification, and evidence capture. Product source and tracked candidate outputs are read-only. Do not repeat design/repository reconnaissance or speculative refactoring; return concrete failures to implementation and design contradictions to software-design.
---

# Software Qualification

Use this skill as the **execution/evidence authority** of Software Development Protocol v3.

Qualification answers:

> Does this exact candidate content actually pass the required checks in the declared environment?

It does not answer whether the design should have been different.

## 1. Require an exact Qualification Handoff

Read:

- `references/workplans-and-agent-handoff.md`;
- `references/protocol-versioning-and-compatibility.md`;
- `references/testing-and-qualification.md`;
- the supplied Qualification Handoff.

Reject an active v2 workplan as a substitute for a v3 Qualification Handoff.

Verify before execution:

```text
protocol version
handoff ID/digest
workplan ID/revision/SHA-256
candidate ref/commit provenance
candidate content identity/policy
required capabilities
allowed write paths/output classes
```

## 2. Candidate preflight is mandatory

`HEAD == candidate_commit` is necessary but not sufficient.

Verify as applicable:

- current checkout provenance matches the handoff;
- recomputed `candidate_content_identity` matches;
- no staged/tracked changes exist on candidate surfaces;
- no undeclared untracked file can affect import/build/runtime;
- submodule/LFS state matches declared identity;
- working directory/import/source origins are controlled where material;
- environment/input/hardware prerequisites are satisfied.

If source identity is ambiguous, stop instead of executing and later claiming a source-bound PASS.

## 3. Keep product candidate immutable

Default:

```text
product_source_mutation: FORBIDDEN
```

Do not edit product source, tests, workplans, architecture, specifications, package/build metadata, or tracked generated candidate outputs while qualifying.

Writes are limited to declared `EPHEMERAL_QUALIFICATION_OUTPUT` paths such as:

- logs/reports/benchmarks/profiles;
- build/output/temp directories;
- temporary packages/artifacts used only for testing.

A `TRACKED_CANDIDATE_OUTPUT` is part of candidate content identity and cannot be created or changed during qualification. If target execution is needed to produce such an artifact, emit it only as a proposed artifact in a declared ephemeral/evidence path, then return it to implementation for adoption into a new candidate.

If product candidate changes are required, return `RETURN_TO_IMPLEMENTATION`.

## 4. Execute only declared checks

Do not perform repository-wide reconnaissance or repeat architecture/algorithm comparison.

Run the frozen checks, from cheap to expensive where ordering is available:

```text
focused/broad tests
-> integration/restart/recovery
-> build/distribution/isolated install
-> production-data/scale
-> target hardware/backend
```

Use exact data/environment requirements from the handoff.

For performance read `references/performance-and-parallelism.md`; for release checks read `references/release-and-distribution.md`; load persistence/concurrency/security references only as needed by declared checks.

## 5. Evidence states and deferred semantics

Each required check is exactly one of:

```text
PASS
FAIL
BLOCKED
NOT RUN
DEFERRED
```

For `DEFERRED`, record `mandatory_for_current_acceptance`, `deferred_to`, and reason.

Never infer PASS from another backend, smaller fixture, old candidate, fallback, or previous session.

`overall_status: PASS` is allowed only when every check mandatory for current acceptance executed and passed.

## 6. Retry boundary

Each check uses one frozen retry mode:

- `NONE`
- `IDENTICAL_RETRY`
- `CLEAN_RETRY`
- `RESUME_RETRY`

Record every attempt and any cleanup/resume state.

A retry that changes candidate content or undeclared scientific/configuration/resource/backend/dataset policy is not a retry under the same handoff. Return to implementation for a new handoff or to design for `DESIGN_REVISION_REQUIRED`.

## 7. Evidence reuse boundary

Reuse prior evidence only when its declared source/config/input/environment/upstream dependencies remain compatible.

If dependency is ambiguous, do not reuse it. Verification audits all nontrivial reuse.

## 8. Failure diagnosis boundary

Diagnose only far enough to produce actionable execution evidence:

- exact command/cwd and exit code;
- earliest failing check/invariant;
- traceback/log/artifact;
- environment/backend/device/config identity;
- minimal reproducer when cheap;
- resource/measurement data where relevant.

Route:

- implementation/test defect -> `RETURN_TO_IMPLEMENTATION`;
- frozen design/acceptance contradiction -> `DESIGN_REVISION_REQUIRED`;
- unavailable dependency/data/hardware/service -> `BLOCKED`;
- stale/dirty candidate identity -> stop as identity blocker;
- external/irreversible action without approval -> stop.

Do not burn qualification context on speculative source redesign.

## 9. Candidate postflight

After execution:

- recompute/verify candidate content identity unchanged;
- verify no tracked candidate source/output changed;
- verify only declared ephemeral/write paths changed;
- record final dirty/untracked/source-origin state where material.

Evidence-only files may later be committed without changing candidate content identity, provided the repository identity policy explicitly excludes them.

## 10. Qualification Report

Use `templates/qualification_report_template.md`.

Bind exact handoff digest, candidate commit provenance, candidate content identity/policy, environment, per-check commands/timestamps/exit codes/attempts, evidence artifacts/digests, reuse decisions, and pre/post source-immutability state.

Do not declare `MERGE_READY`; final acceptance belongs to `software-verification`.
