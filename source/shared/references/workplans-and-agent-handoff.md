# Implementation Workplans and Agent Handoff

## Purpose

An **Implementation Workplan** is the temporary execution contract for moving a repository from an analyzed current state to an accepted target state. It is the formal handoff between design/review work and implementation/testing work.

A workplan is not a specification, architecture manual, history document, audit, benchmark, or release record.

Use a workplan when any of the following materially applies:

- algorithmic or scientific-semantic change;
- cross-module implementation;
- public API/data/configuration contract change;
- persistence/schema/cache/checkpoint change;
- concurrency/orchestration change;
- security/trust-boundary change;
- substantial performance/resource/I/O/storage optimization;
- migration/release qualification work;
- a task for which prior design/diagnostic work can prevent expensive implementation-agent rediscovery.

For trivial isolated fixes, use the compressed path `inspect -> edit -> focused test -> review` without creating a workplan.

## Repository location and artifact class

Prefer a repository-root coordination tree such as:

```text
workplans/
  README.md
  TEMPLATE.md
  active/
  archive/
```

unless the repository already has an equivalent convention.

Workplans are **Markdown-authoritative coordination artifacts** and are normally exempt from mandatory PDF rendering. They should not be packaged as user-facing runtime documentation unless the project explicitly chooses otherwise.

## Workplan lifecycle

Use these statuses:

- `DRAFT` - design/diagnosis is still being developed;
- `READY_FOR_IMPLEMENTATION` - design is accepted and the executor may begin;
- `IN_PROGRESS` - at least one implementation gate is active;
- `BLOCKED` - execution cannot continue under the current contract;
- `COMPLETE` - all mandatory gates and closeout checks passed;
- `SUPERSEDED` - replaced by a newer workplan/revision;
- `CANCELLED` - intentionally abandoned without completion.

Only the design/review role promotes a workplan to `READY_FOR_IMPLEMENTATION` or changes frozen design semantics. The implementation role may update execution/gate status and evidence references without redefining the design contract.

## Versioned handoff contract

A workplan should record at minimum:

```yaml
kind: implementation-workplan
workplan_id: <stable task ID>
plan_revision: <integer>
status: READY_FOR_IMPLEMENTATION
protocol_version: <shared protocol version>
analysis_base_ref: <branch/tag/ref>
analysis_base_commit: <commit SHA>
```

Also record where useful:

```yaml
assumption_paths:
  - <files/directories whose state materially supports the design>
architecture_refs:
  - <current architecture documents>
spec_refs:
  - <current normative contracts>
expected_change_paths:
  - <likely implementation/test/doc surfaces>
```

Do not store a self-referential SHA-256 inside the workplan. The executor/review evidence should record the exact `workplan_sha256` it consumed together with `workplan_id` and `plan_revision`.

## Required workplan sections

A substantial workplan should contain:

1. **Objective** - one concise outcome statement.
2. **Current diagnosis** - evidence-grounded explanation of the problem.
3. **Current authority references** - architecture/spec/source/test/evidence locations.
4. **Frozen design decisions** - choices already resolved and not delegated to the executor.
5. **Invariants and acceptance semantics** - scientific/numerical/API/persistence/security/resource properties that must hold.
6. **Expected change surface** - likely modules/tests/specs/docs/benchmarks; this is a guide, not permission to ignore necessary adjacent files.
7. **Non-goals** - explicitly excluded work.
8. **Execution/resource constraints** - environment, compatibility, CPU/GPU/RAM/VRAM/I/O/storage, dependency, or release constraints that materially affect implementation.
9. **Gate table and gate definitions** - ordered implementation/testing stages.
10. **Design-revision triggers** - conditions under which the executor must stop rather than redesign silently.
11. **Closeout requirements** - current specification/architecture/history/version/evidence/PDF/release reconciliation after implementation is accepted.

Keep the workplan concise. Link to authoritative files and evidence instead of copying large code, logs, manuals, or benchmark output.

## Role authority matrix

| Decision/domain | Design/review role | Implementation role |
|---|---|---|
| Root-cause diagnosis | Owns/finalizes | May refine with implementation evidence |
| Algorithm/architecture choice | Owns | Must follow or escalate |
| Scientific/numerical semantics | Owns target/invariants | Must preserve |
| Public API/data/persistence target contract | Owns | Implements; local details only |
| Resource/performance strategy and acceptance threshold | Owns | Implements/measures; may propose change |
| Security/trust model | Owns target | Implements/validates |
| Gate structure/mandatory acceptance | Owns | Executes and records evidence |
| Local helper placement/internal naming | Advisory | Owns within scope |
| Small refactor required by chosen design | Reviews | Owns within scope |
| Test implementation/instrumentation | Specifies acceptance intent | Owns implementation |
| Benchmark execution | Specifies comparability/criteria | Owns execution |
| Normative-doc closeout | Reviews for architectural/contract correctness | Updates after accepted implementation |
| Redesign after contradiction | Owns revision | Must block/escalate |

The implementation role may strengthen tests, improve diagnostics, or choose a better local implementation technique when this does not change frozen semantics, public contracts, persistence/trust architecture, acceptance thresholds, or declared non-goals.

## Design revision required

The implementation role must stop the affected gate and report `DESIGN_REVISION_REQUIRED` when implementation evidence shows that continuing would require changing any frozen item such as:

- scientific/numerical meaning;
- chosen algorithm or architectural ownership;
- public contract/default semantics;
- persistence/schema/recovery model;
- security/trust model;
- resource-policy semantics or acceptance thresholds;
- mandatory gate acceptance criteria;
- non-goals/scope boundary in a material way.

Use a compact blocker record:

```text
Gate: <ID>
Status: BLOCKED
Reason: DESIGN_REVISION_REQUIRED
Finding: <earliest violated assumption/invariant>
Evidence: <focused reproducer/test/file/measurement>
Decision needed: <specific design choice>
```

Do not spend implementation-agent context on broad redesign after this boundary is crossed.

## Stale-workplan detection

Before implementation, perform bounded revalidation rather than a new repository-wide design pass.

1. Read repository/agent instructions.
2. Verify the workplan is `READY_FOR_IMPLEMENTATION` (or explicitly resumed `IN_PROGRESS`).
3. Record its `workplan_id`, `plan_revision`, and SHA-256.
4. Verify the analyzed base commit exists and determine its relationship to current `HEAD`.
5. If `HEAD == analysis_base_commit`, proceed.
6. If the base is an ancestor of `HEAD`, inspect changes since the base that intersect `assumption_paths`, referenced architecture/specs, target interfaces, and other design-critical surfaces.
7. If those changes do not invalidate assumptions, record bounded revalidation and proceed.
8. If the base is unrelated/unavailable or a material assumption changed, mark `BLOCKED: STALE_WORKPLAN` and return concise evidence for design review.

A later unrelated commit is not sufficient reason to discard a valid plan. Conversely, matching branch names or file existence are not proof that assumptions remain valid.

## Gate construction

Use task-local gate IDs unless a stage is genuinely part of the product/domain architecture. Prefer `G0`, `G1`, `G2`, etc. or concise scoped names. Avoid permanently proliferating architecture-stage names for temporary engineering steps.

A strong sequence often includes:

### G0 - Baseline/oracle/preflight

- freeze current accepted behavior;
- qualify required dependencies/backends/environment early;
- identify a trustworthy oracle;
- record representative correctness/performance/resource/I/O/recovery baseline when relevant;
- add focused fixtures for boundary/adversarial cases.

### G1 - Minimal coherent capability

- implement the smallest exact/compatible form;
- compare directly with the oracle;
- preserve fallback where required.

### G2 - Integration/state reuse

- add persistence/cache/reuse/consumer integration after the core result is correct;
- validate identity/invalidation/atomic publication/recovery;
- measure build/load/recovery cost if persistence exists to save work.

### G3 - Hard/resource/concurrency cases

- large inputs, deformation, concurrency, cancellation, disk pressure, restart, migration, or other difficult regimes;
- adversarial and bounded-resource tests.

### G4 - Automatic/default/production closeout

- enable automatic/default behavior only from evidence;
- run broad regression/release qualification as applicable;
- reconcile current specs/architecture/history/version/evidence/PDFs with the accepted implementation.

Adapt the number and names of gates. Do not force this exact sequence onto small work.

## Gate template

```text
Gate: <ID and short name>
Goal: <one coherent capability>
Prerequisites: <prior gates/contracts/environment>
Change surface: <modules/APIs/docs/tests>
Work:
  - ...
Acceptance:
  - exact check or tolerance/oracle
  - edge/adversarial cases
  - compatibility requirement
  - resource/performance/storage/recovery criterion if applicable
Evidence:
  - tests/benchmarks/builds/audits/manifests
Security/trust boundary:
  - focused checks when applicable
Fallback/rollback: <safe behavior>
Excluded/deferred: <explicitly not in this gate>
```

Do not paste large logs into the workplan. Store them in the repository's audit/benchmark/evidence location and link them.

## Design/review workflow (intended for Chat)

Use two modes:

### DESIGN

```text
repository reconnaissance
-> diagnosis/root cause
-> architecture/algorithm alternatives
-> chosen design and invariants
-> workplan DRAFT
-> review/convergence
-> READY_FOR_IMPLEMENTATION
```

The deliverable is the accepted workplan, not broad implementation.

### REVIEW

After implementation, consume the exact workplan revision plus diff/evidence and check:

- conformance to frozen design/invariants;
- accidental scope widening;
- scientific/numerical/API/persistence semantics;
- hidden scaling/I/O/storage/recovery regressions;
- security/trust-boundary behavior;
- whether acceptance evidence actually supports each PASS;
- specification/architecture/history/version/documentation ownership;
- unresolved blockers or deferred work.

Return narrow corrective actions to the implementation role when possible. Redesign only when evidence requires it.

## Implementation workflow (intended for Codex/executor agents)

When an approved workplan exists:

```text
bounded preflight/revalidation
-> implement one gate
-> focused tests/evidence
-> fix gate-local failures
-> next gate
-> broad qualification
-> normative closeout
```

Do not repeat repository-wide investigation, algorithm comparison, or architecture planning already frozen in the workplan unless stale-plan/design-contradiction evidence requires escalation.

## Closeout and archival lifecycle

After all mandatory gates pass:

- update current specifications to describe accepted implemented behavior;
- update architecture manuals only where the accepted current architecture actually changed;
- update history/changelog/release notes and authoritative versions according to project policy;
- regenerate permanent Markdown-derived PDFs/provenance manifests;
- record final evidence, including the workplan identity/digest consumed;
- mark the workplan `COMPLETE`.

For materially important changes, archive the completed workplan according to repository policy. For mundane tasks, deletion after closeout is acceptable because Git/history already preserves the transition. Do not turn every temporary workplan into permanent product documentation.
