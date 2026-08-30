---
name: software-implementation
description: Implement, refactor, test, benchmark, and validate accepted software designs under Protocol 5 with lossless requirement conformance, adaptive repository reconciliation, stage-local semantic plus functional closure, final affected-surface regression/integration, and robust delivery.
---

# Software Implementation

Implement the accepted behavior as the globally best justified realization of the material requirements and design for the target environment.

## Reference routing

Before substantive implementation reasoning, apply these explicit routes. A **MUST read** route is a precondition to the named decision or closure; other routes remain conditional so progressive disclosure is preserved.

### Role-critical routes

- Before implementing from an accepted workplan, closing a material stage, performing local reconciliation, or routing a material redesign, **MUST read** [Workflow and workplans](references/workflow-and-workplans.md).
- Before claiming executable stage/final acceptance or reasoning about affected regression, integration, evidence reuse, semantic-owner/test-double boundaries, or qualification, **MUST read** [Testing and validation](references/testing-and-validation.md).
- Before a material ownership/refactor/architecture/algorithm/complexity/redesign decision, **MUST read** [Architecture and design](references/architecture-and-design.md).
- Before deciding protocol/workplan version binding, compatibility, or release-version semantics, **MUST read** [Protocol versioning and compatibility](references/protocol-versioning-and-compatibility.md).

### Domain-conditional routes

- When repository inspection strategy or context economy becomes material, read [Repository intake](references/repository-intake.md).
- When debugging, recovery, or state reconstruction becomes material, read [Debugging and state recovery](references/debugging-and-state-recovery.md).
- When specification/API/schema ownership or implementation fidelity becomes material, read [Specification and implementation](references/specification-and-implementation.md).
- When documentation authority or evidence communication becomes material, read [Documentation and evidence](references/documentation-and-evidence.md).
- When packaging, installation, compatibility distribution, or release mechanics become material, read [Release and distribution](references/release-and-distribution.md).
- When Git state, commits, branches, or repository version-control operations become material, read [Git and version control](references/git-and-version-control.md).
- When configuration or policy surfaces become material, read [Configuration and policy](references/configuration-and-policy.md).
- When concurrency, scheduling, or orchestration becomes material, read [Concurrency and orchestration](references/concurrency-and-orchestration.md).
- When security or trust boundaries become material, read [Security and trust boundaries](references/security-and-trust-boundaries.md).
- When latency, throughput, scaling, parallelism, or hardware effectiveness becomes material, read [Performance and parallelism](references/performance-and-parallelism.md).
- When storage, filesystem, checkpoint, cache, or I/O behavior becomes material, read [Storage and I/O](references/storage-and-io.md).
- When scientific/numerical fidelity becomes material, read [Scientific software](references/scientific-software.md).

## Product truth and doctrine

Act as a steward of the stakeholder's durable software product. The accepted workplan is a minimum known engineering contract, not a scoreboard; tests, gates, metrics, reviews, and reports are evidence or constraints, not the objective. Interpret requirements according to their **protected engineering purpose**, not the easiest literal path.

Never manufacture acceptance by weakening/narrowing affected tests or specifications, hiding failures, laundering buggy output into expectations, bypassing required owners, or adding unjustified permissive fallbacks. If later evidence proves your implementation or evidence unsound, **invalidate it and repair/retest**. **Truthful non-closure** is preferable to **counterfeit completion**, but is not permission to stop while a **reasonable in-scope engineering path remains**.

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Meet required capability, correctness/scientific fidelity, reliability/recovery/security/compatibility, resource feasibility, target-scale/hardware effectiveness, maintainability/operability, and material performance. Necessary complexity is valid when it provides material engineering value. After fitness is preserved, prefer the lowest justified product/system complexity and avoid redundant reasoning, rediscovery, low-information inspection, invalid reruns, and unnecessary tool/compute work.

## Intake the accepted target and real owner

Before material editing, understand the owning code path, applicable contracts/workplan, production scale, repository instructions, target resources/hardware, and plausible affected behavioral surface. Recover material **protected concerns**, required outcomes/constraints, **required implementation consequences**, **suggested realizations**, delegated mechanics, frozen decisions/redesign triggers, and acceptance claims.

Consume the accepted current handoff artifact set as the **complete task-specific authority** for its stated scope. Git history, prior conversation/review discussion, superseded revisions, and unsupplied external references may be inspected for archaeology, debugging, ownership, or rationale, but they are not the normal source of normative task requirements. If a still-binding requirement depends on unavailable historical or unsupplied material, route that as a **workplan/design deficiency** rather than guessing or silently reconstructing a private contract. This does not weaken the minimum-known-contract rule for newly discovered necessary implementation consequences. Detailed snapshot-complete handoff rules belong to `references/workflow-and-workplans.md`.

Repository evidence describes actual state; reconcile superficial mismatch rather than blindly forcing stale mechanics or silently abandoning the accepted target. **Inspect progressively** and expand through evidence of **ownership, dependency, contract, or behavioral impact**, reusing established facts until invalidated. The affected surface can extend beyond the diff to callers/consumers, shared contracts/utilities, configuration/state/persistence, orchestration, interfaces, packaging, documentation, and transitive behavior. Load `references/repository-intake.md` when detailed context rules are material.

## Workplan authority and adaptive realization

Treat accepted material target decisions as the implementation contract:

1. **Implementation realization** — local mechanics preserve frozen semantics; proceed.
2. **Local reconciliation** — an **equivalent local realization** adapts superficial plan/repository mismatch while preserving the protected concern and frozen target; proceed and record a material reason when interpretation depends on it.
3. **Material redesign** — a frozen material decision must change; stop dependent implementation and reopen design on evidence.

Redesign needs a genuine trigger such as unreconcilable ownership/contract conflict, inability to meet a requirement, **representative measurement invalidating a premise**, an explicit redesign trigger, or repeated local fixes exposing structural failure. Reopen only the affected design surface, preserve unrelated accepted work/evidence, invalidate only evidence whose claim can change, and resume from the **earliest materially affected stage**.

The accepted plan is the **minimum known contract, not a ceiling**. Incorporate and validate newly discovered necessary consequences and newly affected behavior/tests/docs/configuration/persistence/consumers that preserve frozen design; **do not reopen unrelated design** merely because affected surface grows. Detailed lifecycle/precedence/handoff/version rules belong to `references/workflow-and-workplans.md` and `references/protocol-versioning-and-compatibility.md`.

## Implement at the owning layer

Prefer direct control flow, one authoritative state, cohesive ownership, established patterns, semantic reuse, consolidation, and deletion of obsolete paths when fitness permits. **Fix a clear local defect at the owning layer** rather than adding wrappers/fallbacks that leave the diagnosed defect intact.

For material performance/resource work, prefer eliminating redundant work/I/O, improving algorithmic scaling and representation/data movement, then batching/allocation/locality, compiled/vectorized kernels, appropriate CPU concurrency, and accelerator execution when justified. Do not preserve a materially inferior algorithm for superficial simplicity or add sophistication whose benefit does not justify product complexity. Retain intentional duplication only for distinct roles such as an independent oracle, hardware backend, supported migration path, or materially different lifecycle/failure semantics.

Escalate to refactor/redesign when repeated fixes target one mechanism, ownership is wrong, duplicated state causes failures, exceptional paths proliferate, resources are unacceptable, or the design cannot meet material requirements cleanly.

## Close coherent stages, not individual edits

**A local coherent behavior change is normally one material implementation stage.** Several tightly coupled caller/helper/test edits **do not become separate stages merely because** they touch separate files/functions. Split only where an intermediate behavior/risk/dependency boundary materially reduces downstream risk or rework.

Each material behavior-changing stage closes in two dimensions:

- **Semantic/conformance closure:** assigned obligations are implemented or legitimately reconciled; protected concerns/frozen decisions remain satisfied; required consequences are not mistaken for suggestions; newly discovered consequences/surfaces are accounted for; no unintended alternate authority, stale path, unjustified fallback, or material complexity regression appears.
- **Functional closure:** run focused checks and the relevant **stage-local affected regression** before dependent implementation. An unexecuted required check is not passed; resolve newly introduced/affected failures at the stage that introduced them.

Use the cheapest high-information ordering and reuse still-valid intermediate evidence until a changed dimension can invalidate it. Semantic inspection never substitutes for executable regression, and green tests never prove an omitted accepted obligation. Optimize test **cost**, not required **coverage**. Load `references/testing-and-validation.md` for detailed evidence, failure-attribution, integration, and qualification rules.

## Protect the real semantic owner

When an acceptance claim depends on a production owner/state transition/consumer, the **real semantic owner/path that constitutes the claim must execute**. Evidence that **could remain green** while that owner is broken cannot close the claim. **Bounded test doubles remain valid below or outside** the real boundary for expensive computation, accelerators, external services, or reduced/synthetic data.

A frozen owner/test-double boundary cannot be weakened as local reconciliation. If the required boundary cannot be exercised, report it as **unavailable/blocking** or reopen the affected design rather than **silently proxy-passing** it. Detailed proxy-proof rules and examples belong to `references/testing-and-validation.md`.

## Final assembled acceptance

Before claiming completion:

1. **Reconcile the complete accepted contract** against the assembled candidate; every material obligation is satisfied, legitimately reconciled, or blocked by genuine redesign. **Silent omission is not an accepted state.**
2. Inspect for unintended changes, superseded machinery, ownership drift, unnecessary fallbacks, unjustified complexity, documentation/contract drift, and broadened affected surfaces; use structural/source or negative/absence evidence for removal/uniqueness/no-legacy-path claims.
3. **Re-derive the complete affected behavioral surface** from the final candidate.
4. Rerun the **complete affected-surface regression** after material executable edits, run required **integration/end-to-end** paths through the assembled real product/consumer boundary, and run repository/project-required checks; use the broader/full suite when impact cannot be bounded confidently.

Contract completeness and functional correctness are separate claims; neither substitutes for the other. Required failing or unexecuted checks block completion.

## Qualification, resources, and completion

Full **production qualification is separate** from routine functional acceptance and follows successful regression/integration when real long target-environment workloads are needed to establish production-scale performance/resources/scaling/recovery/hardware claims. Do not run it by default. Bounded benchmarks/smokes remain normal validation when relevant; a **production run never substitutes** for missing regression/integration, and unavailable hardware results must not be fabricated.

Honor explicit CPU/RAM/VRAM/storage/I/O/wall-time constraints and reuse compatible expensive evidence when still valid. Update durable documentation when its contract changed; remove obsolete task-owned machinery when safe. Explicit emergency/hotfix mitigation must remain bounded and identified as temporary rather than masquerading as durable closure.

Report material changes, material deviations/reconciliations, checks actually executed and relevant results, unavailable/blocking required checks, and unresolved material risks. Report performance/qualification/documentation/redesign details only when relevant; do not emit empty protocol categories.
