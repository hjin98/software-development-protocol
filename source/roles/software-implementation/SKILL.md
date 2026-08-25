---
name: software-implementation
description: Implement accepted software designs with lossless requirement conformance, adaptive repository reconciliation, stage-local semantic plus functional closure, final regression/integration acceptance, and robust delivery under Protocol 5.
---

# Software Implementation

Implement the requested behavior as the globally best justified realization of the material requirements and accepted design for the target environment.

## Governing doctrine

> **Engineering fitness first; minimize unjustified product/system complexity within the engineering-sufficient solution space; then avoid unnecessary development cost without weakening the product or its acceptance.**

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Required functionality/capability, correctness, scientific/domain fidelity, reliability, resource feasibility, target-scale behavior, hardware requirements, compatibility/security where relevant, and materially important performance must be met. Necessary complexity is valid when it buys material engineering value.

## Intake the accepted contract before editing

Understand the owning code path, material contracts, governing workplan if any, production workload/scaling variables, repository instructions, target resources/hardware, and plausibly affected behavioral surface.

When an accepted workplan exists, identify its material implementation obligations and the **protected concern** behind each one. Distinguish:

- required outcome/constraint;
- required implementation consequence;
- suggested realization;
- delegated mechanics;
- frozen decisions and evidence-triggered redesign boundaries;
- acceptance evidence.

Reconcile those obligations against actual repository ownership before material editing. Repository evidence describes actual state; it does not automatically override an accepted target or justify blindly forcing a stale mechanical suggestion.

The affected surface is broader than the diff when behavior propagates: include directly changed/new code plus callers/consumers, shared utilities, public interfaces, configuration, persistence/caches/checkpoints, state transitions, orchestration/concurrency paths, packaging/entry points, documentation/contracts, and plausible transitive behavioral dependencies.

Inspect progressively and reuse established facts until later evidence invalidates them. Read `references/repository-intake.md` when detailed information-gain/context rules are material.

## Governing workplan authority and adaptive realization

Treat accepted material target decisions as the implementation contract. Do not reopen frozen architecture, ownership, algorithm, invariant, non-goal, product semantics, material resource/persistence/compatibility policy, or acceptance decisions merely because another plausible design exists.

The plan remains subordinate to higher-priority explicit user/task requirements, safety/platform constraints, applicable project instructions, and governed contracts outside its authorized change scope.

Use three deviation levels:

1. **Implementation realization** — local mechanics that preserve frozen semantics; proceed.
2. **Local reconciliation** — adapt a superficial plan/repository mismatch or use an equivalent local realization while preserving the protected concern and frozen target; proceed and record the material reason when interpretation depends on it.
3. **Material redesign** — a frozen material decision must change; stop dependent implementation and reopen only the affected design surface on evidence.

Material redesign requires evidence: an unreconcilable ownership/contract conflict, inability to meet a material requirement, representative measurement invalidating a premise, an explicit redesign trigger, or repeated local fixes exposing a structural defect.

The accepted plan is the **minimum known contract, not a ceiling**. If implementation discovers:

- a necessary local consequence that preserves frozen design, incorporate and validate it;
- a newly affected behavior/test/documentation/configuration/persistence/consumer surface, add it to task-local acceptance and affected-surface reasoning;
- a need to change a frozen material decision, reopen design on evidence rather than silently inventing a new target.

Preserve unrelated accepted work/evidence when redesign is bounded; resume from the earliest materially affected stage.

## Implement for engineering fitness and clean ownership

Within the accepted design, prefer direct control flow, one authoritative state, cohesive ownership, established project patterns, semantic reuse, consolidation, and deletion of obsolete paths. Do not preserve a materially inferior algorithm merely because it is simpler, and do not add sophisticated optimization/abstraction whose benefit does not justify product complexity.

For a clear local defect, fix the owning layer. Escalate to refactor/redesign when repeated fixes target the same mechanism, ownership is wrong, duplicated state/functionality causes failures, exceptional paths proliferate, resources are unacceptable, or the accepted/current algorithm cannot meet material requirements cleanly.

## Close each material implementation stage in two dimensions

A coherent material behavior-changing stage is not accepted until **both** dimensions close:

### Semantic / conformance closure

Before dependent work proceeds, establish that:

- every accepted obligation assigned to the stage is implemented or legitimately reconciled;
- its protected concerns and frozen decisions remain satisfied;
- required consequences were not mistaken for optional advice;
- suggested realizations were not unnecessarily frozen when an equivalent realization is used;
- newly discovered necessary consequences and affected surfaces are accounted for;
- no unintended alternate authority, stale superseded product path, unjustified fallback/compatibility path, or material product-complexity regression was introduced.

### Functional closure

For executable changes:

1. run focused checks appropriate to the changed mechanisms;
2. run the relevant **stage-local affected regression** before dependent implementation proceeds;
3. treat an unexecuted required check as not passed and resolve newly introduced/affected failures at the stage that introduced them.

Use the cheapest high-information ordering for the stage: a cheap focused test may precede conformance inspection, or obvious source nonconformance may be repaired first. Do not create a review gate for every helper/file edit. Semantic review never substitutes for executable regression, and green tests never prove that an omitted accepted obligation was implemented.

Read `references/testing-and-validation.md` for detailed evidence reuse, stage, integration, failure-attribution, and qualification rules.

## Final implementation closure before handoff

Before claiming implementation complete or handing it to independent review:

1. **Reconcile the complete accepted contract against the assembled candidate.** Every material obligation must be satisfied, legitimately reconciled while preserving frozen intent, or blocked by a genuine redesign condition. Silent omission is not an accepted state.
2. Inspect the assembled implementation/diff for unintended changes, retained superseded machinery, ownership drift, unnecessary fallback/compatibility paths, unjustified complexity, documentation/contract drift, and newly broadened affected surfaces.
3. For claims about removal or uniqueness, use structural/source or negative/absence evidence when runtime tests cannot prove the claim (for example no legacy authority, hardcoded fixture, stale fallback, duplicate writer, or obsolete documented semantic remains).
4. Re-derive the complete affected behavioral surface from the final candidate.
5. Rerun complete affected-surface regression after all material executable edits that could invalidate earlier evidence.
6. Run required integration/end-to-end paths through real product/consumer boundaries.
7. Run repository/project-required checks, using the broader/full suite when impact cannot be bounded confidently.

This final boundary establishes both **contract completeness** and **functional correctness**. Neither substitutes for the other.

## Production qualification is separate

Full production qualification assumes functional regression/integration acceptance already passed. It uses real, long, data-heavy, target-environment workloads to characterize production-scale performance/resources/scaling/recovery/hardware behavior.

Do not run it by default during implementation or between ordinary stages. Run it only when explicitly requested, required by project/release policy, or necessary to establish a material production-scale/resource/performance/hardware claim. Bounded benchmarks, accelerator smoke tests, reference equivalence, and representative resource sanity checks remain normal implementation validation when relevant.

A production run never substitutes for missing focused/regression/integration coverage. Never fabricate unavailable target-hardware results.

## Documentation and cleanup

Update durable public/specification/architecture/user documentation when its owned contract changed. Delete obsolete task-owned helpers/experimental paths/superseded product machinery when safe; do not remove useful tests/validation infrastructure merely because it lengthens engineering work.

## Reference routing

Packaging a reference does not make reading it mandatory. Load the reference when its owned surface is material; start with the relevant section and broaden when interaction requires it.

| Material surface | Reference |
| --- | --- |
| lifecycle, workplans, gates | `references/workflow-and-workplans.md` |
| functional acceptance, evidence reuse, qualification | `references/testing-and-validation.md` |
| protocol/workplan compatibility | `references/protocol-versioning-and-compatibility.md` |
| architecture/ownership/redesign/complexity | `references/architecture-and-design.md` |
| nontrivial failure/state recovery | `references/debugging-and-state-recovery.md` |
| API/schema/persistence/scientific contracts | `references/specification-and-implementation.md` |
| configuration/policy/semantic identity | `references/configuration-and-policy.md` |
| workers/schedulers/retries/cancellation | `references/concurrency-and-orchestration.md` |
| untrusted inputs/credentials/subprocess/network/model loading | `references/security-and-trust-boundaries.md` |
| CPU/GPU/scaling/resources/performance | `references/performance-and-parallelism.md` |
| storage/cache/checkpoint/I/O/recovery | `references/storage-and-io.md` |
| physics/math/ML/numerical semantics | `references/scientific-software.md` |
| repository inspection/change surface | `references/repository-intake.md` |
| branches/worktrees/commits/remotes | `references/git-and-version-control.md` |
| packages/build/install/distribution | `references/release-and-distribution.md` |
| documentation authority/evidence | `references/documentation-and-evidence.md` |

## Completion

Report material changes and enough evidence to interpret both contract completeness and functional acceptance. For executable changes include final affected surface, focused checks, stage-local regression results for material stages, final affected-surface regression, integration paths, repository-required broader checks, structural/absence checks when material, and unavailable/blocking checks.

Do not call an executable change functionally complete while required semantic/conformance closure, stage-local/final regression, repository-required checks, or integration checks are failing or unexecuted.
