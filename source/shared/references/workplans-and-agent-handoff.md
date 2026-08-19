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

These roles are authority boundaries, not product or vendor names. Chat, Codex, CI, a workstation/HPC session, a human, or another agent may occupy a role. The same system may perform multiple roles sequentially when appropriate, but downstream artifacts must still bind exact source and upstream identities.

The split exists to prevent repeated expensive reasoning, separate source construction from target-environment execution, and make PASS claims independently auditable.

## Artifact classes

### Implementation Workplan

A temporary design-to-implementation contract for moving an analyzed repository state to a target state.

It freezes:

- diagnosis and target design;
- scientific/numerical/API/persistence/security/resource invariants;
- expected change surface and non-goals;
- gate structure and acceptance semantics;
- qualification capabilities and barriers;
- design-revision triggers;
- candidate/final closeout expectations.

It is not current product authority.

### Qualification Handoff

A source-bound implementation-to-qualification execution contract.

It freezes:

- exact source ref/commit;
- exact workplan ID/revision/SHA-256;
- required capability/environment;
- exact commands/checks/inputs;
- expected results/evidence paths;
- allowed writes/side effects/retries;
- failure routing.

It must not ask the qualification role to rediscover the implementation plan.

### Qualification Report

Evidence that the exact handoff/source was actually exercised in the declared environment.

It records:

- handoff digest;
- workplan identity;
- source commit;
- environment/backend/device/configuration;
- commands/checks and result states;
- logs/benchmarks/artifact digests;
- source-immutability status;
- failure routing.

### Verification Report

Independent acceptance evidence binding:

- candidate source;
- governing workplan identity;
- qualification evidence;
- gate acceptance;
- blocking/non-blocking findings;
- final `MERGE_READY | NOT_READY | DESIGN_REVISION_REQUIRED` decision.

## Repository placement

Prefer:

```text
workplans/
  active/
  archive/
qualification/
  handoffs/
  reports/
verification/
  reports/
```

or the repository's established audit/evidence layout.

Workplans are temporary coordination artifacts and normally Markdown-only. Qualification/verification artifacts may be Markdown or machine-readable manifests according to project needs. Do not package temporary coordination artifacts into runtime/user distributions unless explicitly required.

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

`software-implementation` may update implementation state/evidence and promote to `PREPARED_FOR_QUALIFICATION` when the candidate and handoff are ready.

`software-qualification` records qualification evidence; it does not redefine the workplan.

`software-verification` makes the final acceptance decision and may mark/archive a workplan `COMPLETE` after mandatory acceptance passes.

## Gate state model

Do not overload one status with three different meanings.

Each substantial gate has:

### Implementation state

```text
PENDING
IN_PROGRESS
PREPARED
BLOCKED
```

`PREPARED` means implementation plus locally available construction checks are complete enough for the remaining declared qualification.

### Qualification state

```text
NOT_REQUIRED
NOT_RUN
PASS
FAIL
BLOCKED
DEFERRED
```

### Acceptance state

```text
PENDING
PASS
FAIL
BLOCKED
```

A gate can be implementation `PREPARED` while qualification remains `NOT_RUN`; this is not a PASS.

Only verification converts complete implementation + mandatory qualification evidence into final acceptance.

## Qualification capability classes

Use capability labels rather than hard-coding agent/product names:

- `SOURCE` — repository/source inspection and mutation;
- `LOCAL_LIGHT` — cheap structural/unit/property checks available to the implementation environment;
- `TARGET_RUNTIME` — the real project runtime/dependency environment;
- `PRODUCTION_DATA` — representative or full real datasets/workloads;
- `TARGET_HARDWARE` — GPU/HPC/native/accelerator/special hardware;
- `EXTERNAL_ACTION` — deployment/publish/merge/external irreversible action or service.

A gate/check may require more than one capability.

## Qualification barriers

Each gate should declare whether pending qualification blocks later implementation.

- `qualification_barrier: no` — implementation may prepare later independent gates while this gate awaits expensive qualification.
- `qualification_barrier: yes` — later implementation cannot safely proceed until this gate's mandatory qualification passes.

Examples of legitimate barriers:

- runtime evidence determines which implementation branch/algorithm is valid;
- a migration must prove source compatibility before later destructive work;
- hardware parity is required before making that backend the basis of subsequent code.

Do not set barriers merely to force conversational ceremony. Do not remove a barrier merely to batch expensive execution.

## Default approval policy

Sequential implementation gates default to `AUTO`.

Human confirmation is required only for `MANUAL_APPROVAL_REQUIRED` gates involving genuinely consequential user choices, irreversible/external actions, or intentionally reserved policy decisions.

Auto-advance applies only within the role's authority and gate dependencies:

- implementation may auto-advance across implementation-preparable gates when barriers allow;
- qualification may execute the handoff checks without per-check confirmation unless an external action requires it;
- verification does not auto-accept missing mandatory evidence.

## Versioned workplan contract

A v3 workplan should record at minimum:

```yaml
kind: implementation-workplan
workplan_id: <stable ID>
plan_revision: <integer>
status: READY_FOR_IMPLEMENTATION
protocol_version: <version from skill PROTOCOL_VERSION>
analysis_base_ref: <ref>
analysis_base_commit: <SHA>
```

Also record as useful:

```yaml
assumption_paths: []
architecture_refs: []
spec_refs: []
expected_change_paths: []
default_gate_approval: AUTO
```

Do not store a self-referential SHA-256 inside the workplan. Downstream evidence records the exact digest consumed.

## Required workplan content

For substantial work:

1. Objective.
2. Current diagnosis.
3. Current authority references.
4. Frozen design decisions.
5. Invariants and acceptance semantics.
6. Expected change surface.
7. Non-goals.
8. Execution/resource/security constraints.
9. Qualification capabilities/barriers.
10. Gate definitions.
11. Design-revision triggers.
12. Candidate/final closeout requirements.

Use `templates/implementation_workplan_template.md`.

## Four-role authority matrix

| Decision/domain | Design | Implementation | Qualification | Verification |
|---|---|---|---|---|
| Root-cause diagnosis | owns/finalizes | may refine from source evidence | only failure-local diagnosis | audits consistency |
| Algorithm/architecture choice | owns | follows/escalates | must not redesign | verifies conformance |
| Scientific/numerical semantics | owns target/invariants | implements/preserves | executes checks | accepts/rejects evidence |
| Public/API/data/config target | owns | implements | exercises declared behavior | verifies parity |
| Persistence/schema/recovery target | owns | implements | executes corruption/restart/migration checks | verifies contract/evidence |
| Resource/performance strategy/threshold | owns | implements/instruments | measures | verifies comparability/claim |
| Security/trust model | owns | implements | exercises declared boundary | verifies coverage/assumptions |
| Gate structure/mandatory acceptance | owns | consumes | consumes | decides final acceptance |
| Local helper/internal naming | advisory | owns within scope | none | reviews only if consequential |
| Test/harness construction | specifies intent | owns | executes source-bound checks | verifies sufficiency |
| Benchmark execution | specifies criteria | prepares harness | owns execution | verifies methodology/claim |
| Product source mutation | no broad implementation | owns | forbidden by default | forbidden during review |
| Candidate spec/docs/version/release edits | defines target ownership | stages exact candidate | may generate declared outputs | verifies parity |
| Workplan completion/archive | design may revise | may update progress | no design change | owns final accepted lifecycle |
| Redesign after contradiction | owns revision | escalates | escalates | escalates |

## Stale-workplan detection

Before substantial implementation:

1. read repository/agent instructions;
2. verify workplan state;
3. record workplan ID/revision/SHA-256;
4. verify analyzed base exists and relationship to current HEAD;
5. inspect only base-to-HEAD changes intersecting assumption paths/current authority/target interfaces;
6. proceed if assumptions remain valid;
7. otherwise `BLOCKED: STALE_WORKPLAN`.

Do not repeat repository-wide design just because HEAD advanced.

## Design revision required

Implementation/qualification/verification must route to `software-design` when continuing would require changing frozen:

- scientific/numerical meaning;
- algorithm or architectural ownership;
- public/default semantics;
- persistence/schema/recovery model;
- security/trust model;
- resource-policy semantics or mandatory thresholds;
- mandatory acceptance criteria;
- material scope/non-goals.

Use a compact record:

```text
Gate/check: <ID>
Status: BLOCKED
Reason: DESIGN_REVISION_REQUIRED
Finding: <earliest violated assumption/invariant>
Evidence: <focused source/test/measurement>
Decision needed: <specific frozen choice>
```

## Qualification Handoff contract

Use `templates/qualification_handoff_template.md`.

Required identity:

```yaml
kind: qualification-handoff
handoff_id: <ID>
protocol_version: <v3>
workplan_id: <ID>
plan_revision: <N>
workplan_sha256: <digest>
source_ref: <ref>
source_commit: <SHA>
status: PREPARED_FOR_QUALIFICATION
product_source_mutation: FORBIDDEN
```

Each check declares:

- check ID and owning gate(s);
- mandatory or optional;
- capability;
- exact command/cwd;
- prerequisites and inputs;
- expected result;
- evidence/output paths;
- retry policy;
- allowed side effects/writes.

A broad instruction such as "run the workplan" is not a valid qualification handoff.

## Qualification source immutability

Product source is read-only by default during qualification.

Qualification may write only declared:

- logs/reports/benchmarks/audits;
- build/temp/output paths;
- generated artifacts explicitly required by a check.

If fixing the candidate requires source/test/workplan/spec changes:

```text
RETURN_TO_IMPLEMENTATION
```

Any changed source requires a new source-bound handoff before that source can be qualified.

## Qualification evidence and retries

Use `templates/qualification_report_template.md`.

A mandatory check is one of:

```text
PASS
FAIL
BLOCKED
NOT RUN
DEFERRED
```

No inferred PASS.

When source changes after a failure, old evidence remains historical evidence for the old source. Rerun all checks affected by the source delta; do not rerun unrelated expensive checks merely because an agent session changed.

Existing authenticated baselines may be reused when their source/input/method/environment identity is still compatible with the workplan's comparability contract.

## Candidate closeout

For release-significant changes, implementation should stage the exact candidate that qualification is meant to exercise, including current spec/architecture/version/release/package/generated-artifact surfaces as applicable.

Those branch-local candidate documents do not become accepted current authority until verification returns `MERGE_READY` and the candidate is accepted/merged.

This avoids a post-qualification documentation/version mutation that would make the qualified source differ from the merge candidate.

If target-environment tooling is required to build generated artifacts, the handoff must declare the exact build/verification command and allowed output paths.

## Verification contract

Use `templates/verification_report_template.md`.

Verification binds:

- workplan identity/digest;
- exact candidate source;
- qualification handoff/report digests;
- relevant architecture/spec/release surfaces.

It checks design conformance, evidence sufficiency, claim comparability, compatibility, scope growth, candidate documentation/release parity, and remaining risk.

Final decision:

```text
MERGE_READY
NOT_READY
DESIGN_REVISION_REQUIRED
```

`MERGE_READY` requires no unresolved mandatory acceptance failure/blocker/not-run check.

Verification must not repair substantial product source while reviewing. Corrections return to implementation, then affected qualification reruns against the new source.

## Trivial compressed path

A formal four-artifact lifecycle is unnecessary for isolated low-risk edits.

A compressed path may be:

```text
inspect
-> implement
-> focused local checks
-> independent review
```

Use a workplan/qualification handoff when persistence/public contracts/scientific semantics/concurrency/security/release-significant behavior/target hardware/production scale or expensive prior reasoning materially applies.

Do not manufacture protocol ceremony when it adds no risk control.

## Legacy v2 compatibility

Read `protocol-versioning-and-compatibility.md`.

Completed v2 workplans/evidence remain readable historical inputs. Do not rewrite completed history.

Active substantial v2 work generally migrates to a v3 design/continuation workplan before split qualification. `software-qualification` does not treat a raw v2 workplan as its execution contract.

## Freeze/dogfood requirement for major protocol revisions

Before declaring a major protocol version frozen:

1. rebuild every generated skill;
2. run the builder's drift check;
3. exercise happy-path handoff/qualification/verification;
4. exercise stale source SHA;
5. exercise qualification FAIL and return-to-implementation;
6. exercise BLOCKED target capability;
7. exercise `qualification_barrier: yes`;
8. exercise source change after qualification and evidence invalidation;
9. exercise tampered/mismatched evidence identity;
10. exercise design contradiction routing;
11. dogfood the lifecycle on at least one representative nontrivial real workflow.

Major-version freeze should prove role boundaries, not just prose consistency.
