# Workplans, Qualification Handoffs, and Agent Roles

## Purpose

Protocol v3 separates four kinds of software-development authority:

```text
software-design
  -> Implementation Workplan
software-implementation
  -> Qualification Handoff
software-qualification
  -> Qualification Report / evidence
software-verification
  -> Verification Report / acceptance decision
```

These roles are authority boundaries, not product or vendor names. Chat, Codex, CI, a workstation/HPC session, a human, or another agent may occupy a role. The same system may perform multiple roles sequentially when appropriate, but downstream artifacts must still bind exact upstream and candidate identities.

The split exists to prevent repeated expensive reasoning, separate source construction from target-environment execution, and make PASS claims independently auditable.

## Artifact classes

### Implementation Workplan

Temporary design-to-implementation contract. It freezes diagnosis, design, invariants, change surface/non-goals, gate structure, qualification capabilities/barriers, acceptance semantics, evidence dependency/comparability rules, and design-revision triggers. It is not current product authority.

### Qualification Handoff

Source-bound implementation-to-qualification execution contract. It freezes the exact candidate identity, workplan identity, required capabilities/environment, checks/commands/inputs, expected evidence, dependencies, retries, allowed writes/side effects, and failure routing. A broad instruction such as "finish/run the workplan" is invalid.

### Qualification Report

Evidence that the exact handoff/candidate was exercised. It records handoff digest, candidate identity, environment/configuration, per-check execution provenance, results, artifacts/digests, pre/post source-immutability state, retries, and failure routing.

### Verification Report

Independent acceptance record binding candidate identity, workplan, qualification evidence, gate acceptance, findings, evidence reuse decisions, verifier independence metadata, and final `MERGE_READY | NOT_READY | DESIGN_REVISION_REQUIRED`.

## Repository placement

Prefer project-owned coordination/evidence locations, for example:

```text
workplans/active/
workplans/archive/
qualification/handoffs/
qualification/reports/
verification/reports/
```

These are normally excluded from runtime/user distributions. A repository may use another established audit/evidence layout.

## Candidate identity versus evidence commits

Read `protocol-versioning-and-compatibility.md`.

Protocol v3 distinguishes:

```text
candidate_commit
candidate_content_identity
evidence/coordination commit(s)
```

Qualification accepts candidate content, not merely a branch name or whichever commit happens to be HEAD later.

Evidence/coordination commits may follow qualification without invalidating it **only if** they preserve the declared `candidate_content_identity`. Any product-relevant change creates a new candidate identity and triggers dependency-based qualification invalidation.

## Workplan lifecycle

Use:

- `DRAFT`
- `READY_FOR_IMPLEMENTATION`
- `IN_PROGRESS`
- `PREPARED_FOR_QUALIFICATION`
- `QUALIFICATION_IN_PROGRESS`
- `READY_FOR_VERIFICATION`
- `BLOCKED`
- `COMPLETE`
- `SUPERSEDED`
- `CANCELLED`

Only `software-design` promotes a workplan to `READY_FOR_IMPLEMENTATION` or changes frozen design semantics.

`software-implementation` may update implementation progress and issue a Qualification Handoff.

`software-qualification` records qualification evidence; it does not redesign or redefine the workplan.

`software-verification` makes final acceptance and may mark/archive a workplan `COMPLETE` after mandatory acceptance passes.

### Derived lifecycle rule

Where gate state is represented structurally, workplan-level execution status should be derived rather than chosen independently:

- `PREPARED_FOR_QUALIFICATION` only when every gate needed in the next qualification batch is implementation `PREPARED` and no blocking implementation state prevents the batch;
- `READY_FOR_VERIFICATION` only when every check mandatory for current acceptance is `PASS` or the owning gate is `NOT_REQUIRED`;
- `BLOCKED` when a mandatory blocking dependency cannot proceed;
- `COMPLETE` only after verification returns `MERGE_READY` and final evidence/closeout identity is coherent.

Do not allow contradictory combinations such as `READY_FOR_VERIFICATION` with a mandatory `NOT_RUN`, `FAIL`, `BLOCKED`, or blocking `DEFERRED` check.

## Gate state model

### Implementation state

```text
PENDING
IN_PROGRESS
PREPARED
BLOCKED
```

`PREPARED` means source/test/harness construction and available local checks are complete enough for declared remaining qualification. It is not acceptance.

### Qualification state

```text
NOT_REQUIRED
NOT_RUN
PASS
FAIL
BLOCKED
DEFERRED
```

For `DEFERRED`, record explicitly:

```yaml
mandatory_for_current_acceptance: true|false
deferred_to: <workplan/release/milestone>
reason: <why>
```

A deferred mandatory-for-current-acceptance check blocks `MERGE_READY`.

### Acceptance state

```text
PENDING
PASS
FAIL
BLOCKED
```

Only verification converts prepared implementation plus mandatory qualification evidence into final acceptance.

## Qualification capability classes

Use capability labels, not agent/product names:

- `SOURCE`
- `LOCAL_LIGHT`
- `TARGET_RUNTIME`
- `PRODUCTION_DATA`
- `TARGET_HARDWARE`
- `EXTERNAL_ACTION`

A check may require multiple capabilities.

## Qualification barriers

Each gate declares whether pending qualification blocks later implementation:

- `qualification_barrier: no` — later independent implementation may be prepared;
- `qualification_barrier: yes` — dependent implementation must wait for mandatory qualification PASS.

Do not weaken acceptance to batch expensive execution. Do not set barriers merely for conversational ceremony.

## Default approval policy

Sequential implementation gates default to `AUTO`. Human confirmation is required only for `MANUAL_APPROVAL_REQUIRED` gates involving consequential user choice, irreversible/external actions, or intentionally reserved policy decisions.

Auto-advance applies only within role authority and barrier dependencies.

## Versioned workplan contract

A v3 workplan records at minimum:

```yaml
kind: implementation-workplan
workplan_id: <stable ID>
plan_revision: <integer>
status: READY_FOR_IMPLEMENTATION
protocol_version: <skill version>
analysis_base_ref: <ref>
analysis_base_commit: <SHA>
```

Also record as applicable:

```yaml
assumption_paths: []
architecture_refs: []
spec_refs: []
expected_change_paths: []
default_gate_approval: AUTO
candidate_identity_policy: <repo policy or explicit include/exclude manifest rule>
```

Do not store a self-referential SHA-256 in the workplan. Downstream evidence records the exact digest consumed.

## Required workplan content

For substantial work:

1. objective;
2. diagnosis;
3. current authority;
4. frozen design;
5. invariants/acceptance;
6. change surface/non-goals;
7. resource/security constraints;
8. qualification capabilities/barriers;
9. candidate identity policy;
10. evidence dependency/comparability policy where expensive reuse matters;
11. gates;
12. design-revision triggers;
13. candidate/final closeout.

## Four-role authority matrix

| Decision/domain | Design | Implementation | Qualification | Verification |
|---|---|---|---|---|
| Root cause | owns/finalizes | may refine from source evidence | failure-local diagnosis only | audits consistency |
| Algorithm/architecture | owns | follows/escalates | must not redesign | verifies conformance |
| Scientific/numerical semantics | owns target | implements/preserves | executes checks | accepts/rejects evidence |
| Public/API/data/config target | owns | implements | exercises | verifies parity |
| Persistence/schema/recovery | owns | implements | executes restart/corruption/migration checks | verifies contract/evidence |
| Resource/performance threshold | owns | implements/instruments | measures | verifies comparability/claim |
| Security/trust model | owns | implements | exercises declared boundary | verifies coverage/assumptions |
| Gate structure/mandatory acceptance | owns | consumes | consumes | decides final acceptance |
| Local helper/internal naming | advisory | owns in scope | none | reviews only if consequential |
| Test/harness construction | specifies intent | owns | executes declared checks | verifies sufficiency |
| Evidence dependency semantics | owns if acceptance-critical | instantiates proposed dependencies | records execution identity | audits reuse/invalidation |
| Benchmark execution | specifies criteria | prepares harness | owns execution | verifies methodology/claim |
| Product source mutation | no broad implementation | owns | forbidden by default | forbidden during review |
| Candidate spec/docs/version/release edits | defines target ownership | stages candidate | no tracked candidate mutation | verifies parity |
| Workplan completion/archive | may revise | updates progress | no design change | owns accepted lifecycle |
| Redesign after contradiction | owns revision | escalates | escalates | escalates |

## Stale-workplan detection

Before substantial implementation:

1. read repo/agent instructions;
2. verify workplan state;
3. record ID/revision/SHA-256;
4. verify analyzed base relationship to HEAD;
5. inspect only intersecting assumption/current-authority/target-interface changes;
6. proceed when assumptions remain valid;
7. otherwise `BLOCKED: STALE_WORKPLAN`.

Do not repeat repository-wide design merely because HEAD advanced.

## Qualification Handoff contract

Required identity:

```yaml
kind: qualification-handoff
handoff_id: <ID>
protocol_version: <v3>
workplan_id: <ID>
plan_revision: <N>
workplan_sha256: <digest>
candidate_ref: <ref>
candidate_commit: <SHA>
candidate_content_identity: <digest/manifest identity>
candidate_identity_policy: <policy identity>
status: PREPARED_FOR_QUALIFICATION
product_source_mutation: FORBIDDEN
```

Each check declares:

- check ID and owning gate(s);
- mandatory/current-acceptance semantics;
- required capability;
- command/cwd;
- prerequisites/inputs;
- expected result;
- evidence/output paths;
- evidence dependencies/comparability dimensions;
- retry mode and attempt limit;
- allowed side effects/write classes.

## Qualification preflight/postflight

Qualification must verify before running:

- HEAD/candidate provenance matches the handoff where a checkout is used;
- candidate content identity matches;
- candidate tracked/staged state is clean;
- no undeclared untracked/shadowing source can affect execution;
- submodule/LFS/import/source origins are controlled when material;
- required environment/input/hardware identities are available.

After execution, verify candidate content identity is unchanged and only declared output paths/classes differ.

## Qualification source immutability and outputs

Product source is read-only during qualification.

Allowed writes are declared `EPHEMERAL_QUALIFICATION_OUTPUT` such as logs, reports, build scratch, temporary packages, profiles and benchmark data.

Qualification must not create/change `TRACKED_CANDIDATE_OUTPUT`. If target execution is needed to produce such an artifact, emit it as proposed evidence/output, return it to implementation, commit a new candidate, and requalify affected checks.

If fixing candidate source/tests/spec/workplan is required: `RETURN_TO_IMPLEMENTATION`.

## Qualification evidence, dependencies, and retries

A mandatory check is exactly one of `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`, `DEFERRED`. No inferred PASS.

Evidence reuse requires declared compatible dependencies. Ambiguous dependency => invalidate/rerun.

Retry modes:

- `NONE`
- `IDENTICAL_RETRY`
- `CLEAN_RETRY`
- `RESUME_RETRY`

Any retry changing candidate/product content or undeclared scientific/config/resource/backend/dataset policy is not a retry under the same handoff.

## Candidate closeout

For release-significant changes, implementation stages the exact product candidate—source/tests/spec/architecture/version/release/package/tracked generated products as applicable—before qualification.

Branch-local candidate docs do not become accepted current authority until verification returns `MERGE_READY` and the candidate is accepted/merged.

## Verification contract

Verification binds:

- workplan identity/digest;
- candidate commit provenance plus candidate content identity/policy;
- qualification handoff/report digests;
- relevant current/candidate architecture/spec/release surfaces;
- any reused evidence and its dependency rationale;
- independence metadata.

Final decision is exactly:

```text
MERGE_READY
NOT_READY
DESIGN_REVISION_REQUIRED
```

`MERGE_READY` requires no unresolved mandatory acceptance failure, blocker, not-run, or blocking deferred check.

Verification does not repair substantial product source. Corrections return to implementation; affected qualification reruns against the new candidate identity.

## Verification independence metadata

Record at least:

```yaml
independence:
  verifier_context: fresh | shared | unknown
  implementation_actor_same: true|false|unknown
  qualification_actor_same: true|false|unknown
```

Fresh context is preferred for substantial scientific/security/release-significant work; project policy may require it. Low-risk work may use shared context when appropriate, but independence must not be implied falsely.

## Trivial compressed path

Formal four-artifact lifecycle is unnecessary for isolated low-risk edits. A compressed path may be:

```text
inspect -> implement -> focused executed checks -> source/diff review -> acceptance decision
```

The compressed path still obeys evidence honesty: no inferred PASS, relevant checks actually execute, and final review/acceptance is explicit. Use formal artifacts when public/persisted/scientific/concurrency/security/release/target-hardware/production-scale or expensive prior reasoning materially applies.

## Legacy v2 compatibility

Read `protocol-versioning-and-compatibility.md`. Completed v2 evidence remains readable history. Active substantial v2 work generally migrates before split qualification. A raw v2 workplan is not a v3 Qualification Handoff.

## Major-version freeze/dogfood

Before freezing a major version, exercise source/evidence identity, dirty-tree rejection, generated-output classes, retries, dependency-bound reuse, barriers, blocking deferred checks, failure routing, v2 migration, tampered identity, and at least one representative real workflow.
