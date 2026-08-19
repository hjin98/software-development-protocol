---
name: software-qualification
description: Execute source-bound software qualification from a Protocol v3 Qualification Handoff. Use for focused/broad test execution, integration/restart/recovery tests, production-data runs, CPU/GPU/HPC/backend qualification, benchmarking/profiling/resource measurement, clean-build/clean-install checks, generated-artifact verification, and evidence capture. Product source is read-only by default. Do not repeat design/repository reconnaissance or speculative refactoring; return concrete failures to implementation and design contradictions to software-design.
---

# Software Qualification

Use this skill as the **execution/evidence authority** of Software Development Protocol v3.

Qualification answers:

> Does this exact candidate actually pass the required checks in the declared environment?

It does not answer:

> Should the design have been different?

## 1. Require an exact Qualification Handoff

Read:

- `references/workplans-and-agent-handoff.md`
- `references/protocol-versioning-and-compatibility.md`
- `references/testing-and-qualification.md`
- the supplied Qualification Handoff.

Reject an active v2 workplan as a substitute for a v3 Qualification Handoff.

Verify before execution:

```text
protocol version
handoff ID/digest
workplan ID/revision/SHA-256
source ref/commit
required capabilities
allowed write paths/side effects
```

If current source does not equal `source_commit`, stop as stale handoff.

## 2. Keep product source immutable

Default:

```text
product_source_mutation: FORBIDDEN
```

Do not edit product source, tests, workplans, architecture, specifications, or policy while qualifying.

Writes are limited to:

- declared evidence/log/benchmark/report paths;
- build/output/temp paths authorized by the handoff;
- generated artifacts explicitly required by a qualification check.

If a product-source change is required, return `RETURN_TO_IMPLEMENTATION`. A report produced after changing source cannot qualify the new source without a new handoff.

## 3. Execute only the declared checks

Do not perform repository-wide reconnaissance or repeat architecture/algorithm comparison.

Run the frozen commands/checks, from cheap to expensive where ordering is available:

```text
focused/broad tests
-> integration/restart/recovery
-> build/distribution/isolated install
-> production-data/scale
-> target hardware/backend
```

Use exact data/environment requirements from the handoff.

For performance qualification read `references/performance-and-parallelism.md`; for release checks read `references/release-and-distribution.md`; for persistence/concurrency/security checks load the owning references as needed.

## 4. Evidence states

Each required check is exactly one of:

```text
PASS
FAIL
BLOCKED
NOT RUN
DEFERRED
```

Never infer PASS from another backend, smaller fixture, old source revision, or successful fallback.

`overall_status: PASS` is allowed only when every mandatory check executed and passed.

## 5. Failure diagnosis boundary

Diagnose only far enough to produce actionable execution evidence:

- exact command and exit code;
- earliest failing test/assertion/invariant;
- traceback/log/artifact;
- environment/backend/device;
- minimal reproducer when cheap;
- resource/measurement data when relevant.

Route:

- implementation/test defect -> `RETURN_TO_IMPLEMENTATION`;
- frozen target/acceptance contradiction -> `DESIGN_REVISION_REQUIRED`;
- unavailable dependency/data/hardware/service -> `BLOCKED`;
- external/irreversible action without approval -> stop.

Do not burn qualification context on speculative source redesign.

## 6. Qualification Report

Use `templates/qualification_report_template.md`.

Bind the exact handoff digest and source commit. Record environment identity, commands, results, artifacts/digests, measurements, and source-immutability status.

When a rerun is necessary, rerun only the affected mandatory checks when dependency is explicit; otherwise rerun conservatively.

## Completion report

Return the Qualification Report/evidence paths and a concise overall status. Do not declare `MERGE_READY`; final acceptance belongs to `software-verification`.
