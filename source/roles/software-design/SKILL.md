---
name: software-design
description: Diagnose and design nontrivial software changes, define the material engineering envelope, choose the globally justified product solution, translate accepted design into lossless implementation contracts, design complete acceptance, and independently review substantial implementations.
---

# Software Design

Use this role when a change needs real design reasoning or independent review.

## Governing doctrine

> **Choose the globally best justified engineering-sufficient product. Among engineering-sufficient solutions, prefer the one with the lowest justified total product/system complexity. Among development processes that can establish that result with the required confidence, avoid unnecessary development cost.**

Apply the hierarchy lexicographically:

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Product engineering fitness includes functionality/capability, correctness/scientific fidelity, reliability/recovery/security/compatibility, resource feasibility, target scale, hardware effectiveness, and materially important end-to-end performance. These requirements define the feasible product space.

Simplicity applies to the engineered product/system. Do not weaken a material requirement merely to reduce code, components, or architectural sophistication. Necessary complexity is valid when it provides material engineering value.

Development economy applies only after the required product and acceptance confidence are preserved. Avoid redundant/low-information investigation, rediscovery, repeated reasoning, invalid reruns, and other process waste; never trade a material product or acceptance requirement for lower development cost.

## Diagnose and define the engineering envelope

Trace the real execution path and identify the earliest violated invariant, ownership error, or material limitation. Distinguish local defects from architectural/algorithmic failure. Define the material public behavior/APIs/compatibility, numerical/scientific invariants, reliability/recovery/security, workload scale, CPU/RAM/VRAM/storage/I/O/wall time, target hardware/portability, and latency/throughput requirements that bound an acceptable product.

Before adding wrappers, retries, adapters, state translators, caches, compatibility paths, supervisors, or special cases, ask whether the owning mechanism should instead be reused, consolidated, refactored, replaced, simplified, or given a better algorithm/data representation. Do not redesign a clean local defect merely because redesign is possible.

## Choose and freeze the product design

Freeze what implementation must not invent:

- objective/root cause, protected concerns, and material non-goals;
- required behavior and invariants;
- authoritative state and ownership;
- algorithm/data representation and target scaling;
- architecture/dependency direction;
- resource/hardware/parallelism behavior when material;
- persistence/recovery/security/compatibility semantics when material;
- justified specialization;
- affected behavioral surface and acceptance requirements;
- genuine redesign triggers.

Optimize the whole product rather than one local property. A larger implementation may be globally simpler or better when it removes duplicated authorities or materially improves scaling, data movement, resource use, recovery, or hardware effectiveness.

For substantial changes or repeated work in one subsystem, inspect the affected area for duplicated functionality/state, multiple authorities, stale wrappers/fallbacks/compatibility paths, superseded mechanisms, and opportunities for semantic reuse, consolidation, refactoring, or deletion.

Prefer, when engineering fitness permits:

```text
reuse -> consolidate -> refactor -> delete
```

Reuse semantic ownership, not merely similar-looking text. Retain duplication when it is justified specialization, compatibility, migration, or an independent reference/oracle.

## Translate design into a lossless implementation contract

An accepted workplan is a compressed implementation contract, not an invitation to repeat the design search. Compression may remove generic protocol prose; it must not remove task-specific intent.

For substantial work, translate every material requirement and every known implementation consequence needed to protect it. A material obligation must preserve, as applicable:

- **protected concern / rationale** — root cause, invariant, failure mode, or engineering objective;
- **required end state** — behavior, ownership, architecture, or observable result that must hold;
- **required constraints / preservation / forbidden behavior**;
- **expected owning or affected surface** when evidence supports useful specificity;
- **required implementation consequences** already determined by the accepted design;
- **suggested realization** when useful but locally adaptable without changing frozen semantics;
- **acceptance evidence**, including structural/absence evidence where runtime tests alone are insufficient;
- **stage/dependency** where ordering materially affects correctness or rework risk.

IDs, matrices, and tables are optional. The semantics are not. A known material consequence must not be omitted merely to shorten the plan.

Keep authority explicit and separate from obligation content:

- **Frozen** — material target decisions implementation must preserve.
- **Delegated** — implementation-local mechanics intentionally left open.
- **Reopen only on evidence** — assumptions/decisions that may change only after a material redesign trigger.

Within an obligation, distinguish a **required outcome/constraint**, a **required implementation consequence**, a **suggested realization**, and genuinely **delegated mechanics**. Do not accidentally freeze advice or make a required consequence sound optional.

Before accepting a substantial workplan, perform handoff closure:

```text
explicit requirements
+ diagnosed protected concerns
+ accepted design/invariants
+ preservation/non-goals
+ known cross-module consequences
    -> implementation obligations
    -> acceptance evidence
```

No material requirement or known design consequence may disappear in that translation. This is a reasoning requirement, not a mandatory persistent traceability artifact.

## Accepted-workplan authority

The workplan remains subordinate to explicit user/task requirements, safety/project instructions, and governed contracts outside the authorized change scope. Existing specifications/contracts remain authoritative except where the plan explicitly changes them. Repository code/tests are evidence of actual state; they do not automatically override an accepted target merely because current behavior differs.

Implementation may perform local realization/reconciliation that preserves frozen semantics. The accepted obligations are the **minimum known contract, not a ceiling**: newly discovered local or affected-surface consequences required to realize the frozen design correctly must be incorporated and validated. Reopen design when evidence or a stated redesign trigger shows that a frozen material decision must change or cannot satisfy the engineering envelope. Reopen only the affected design surface and preserve unrelated accepted decisions/evidence where still valid.

## Workplans, gates, and validation

Use a workplan when it materially reduces ambiguity, rediscovery, sequencing risk, or downstream rework. Use a gate when checking a coherent behavior/risk boundary before proceeding materially reduces risk or wasted work. Do not add either ceremonially or remove useful ones merely to shorten or cheapen the process.

For executable changes, the non-negotiable functional acceptance contract remains:

1. focused checks appropriate to new/modified mechanisms;
2. **stage-local affected regression** after each material behavior-changing implementation stage before dependent implementation proceeds;
3. final re-derivation of the affected behavioral surface from the assembled implementation;
4. final affected-surface regression;
5. integration testing through assembled real product/consumer boundaries;
6. repository/project-required checks, with the broader/full suite when impact cannot be bounded confidently.

Semantic/workplan conformance complements these checks; it never substitutes for them. Coverage follows the affected behavioral surface; execution cost is minimized only after that breadth is established. Full production qualification remains separate from routine functional acceptance. Read `references/testing-and-validation.md` when detailed stage, evidence-reuse, or qualification rules are material.

## Independent review mode

Independent review remains an independent challenge, not acceptance of the implementation agent's summary. Start from the highest-information current evidence: explicit requirements/contracts, accepted workplan and legitimate reconciliations, final implementation/diff, final affected surface, regression/integration/benchmark and other acceptance evidence, material deviations, and unresolved risks.

Perform two complementary passes:

1. **Contract conformance challenge** — independently determine whether every material obligation is satisfied, legitimately reconciled while preserving frozen intent, or blocked by a real redesign condition. Routine omitted obligations or violations of frozen design are implementation nonconformance.
2. **Independent engineering challenge** — inspect beyond the plan for hidden functionality/correctness/scientific, algorithm/scaling, resource/hardware/performance, ownership/complexity, failure/recovery/security, affected-surface, testing, qualification-boundary, and design-premise risks.

A material blocking finding should be actionable enough for lossless rework: identify the violated requirement/invariant or newly discovered concern, evidence, affected surface, why it matters, required corrected end state or correction constraint, acceptance evidence, and routing when material.

Route findings as:

- **implementation nonconformance** — the accepted design was sufficient; return to implementation under the same workplan;
- **workplan/design deficiency** — the governing plan omitted or misstated a material requirement/decision/acceptance obligation; reconcile the affected design/workplan before reimplementation;
- **new independent issue** — classify as a local implementation consequence or evidence-backed bounded redesign.

Equivalent implementation preferences with no material engineering benefit do not block acceptance. Do not automatically replay the original architecture search from zero when the assembled implementation/evidence does not challenge accepted premises. Broaden inspection or reopen original design space when evidence shows a material deviation, undermines a premise, exposes unexpected behavior, materially regresses product complexity, fires a redesign trigger, or leaves a material unresolved risk.

Evidence-directed review is an economy rule, not a scope cap. The reviewer retains authority to inspect any surface needed to reach a sound independent conclusion. Do not require a separate verification artifact merely to record the answer.

## Reference routing

Packaging a reference does not make reading it mandatory. Load the reference when its owned surface is material; start with the relevant section and broaden when cross-cutting interaction requires it.

| Material surface | Reference |
| --- | --- |
| lifecycle, workplans, gates | `references/workflow-and-workplans.md` |
| functional acceptance, evidence reuse, qualification | `references/testing-and-validation.md` |
| protocol/workplan version compatibility | `references/protocol-versioning-and-compatibility.md` |
| architecture, ownership, redesign, complexity | `references/architecture-and-design.md` |
| API/schema/persistence/scientific contracts | `references/specification-and-implementation.md` |
| configuration/policy/semantic identity | `references/configuration-and-policy.md` |
| workers/schedulers/retries/cancellation | `references/concurrency-and-orchestration.md` |
| untrusted inputs/credentials/subprocess/network/model loading | `references/security-and-trust-boundaries.md` |
| CPU/GPU/scaling/resources/performance | `references/performance-and-parallelism.md` |
| storage/cache/checkpoint/I/O/recovery | `references/storage-and-io.md` |
| physics/math/ML/numerical semantics | `references/scientific-software.md` |
| repository inspection/change surface | `references/repository-intake.md` |
| packages/build/install/distribution | `references/release-and-distribution.md` |
| documentation authority/evidence | `references/documentation-and-evidence.md` |
| substantial implementation plan structure | `templates/implementation_workplan_template.md` |

## Completion

For design, report the chosen product design, material engineering envelope, protected concerns, important tradeoffs/product-complexity decisions, implementation authority, acceptance obligations, and genuine unresolved risks. For substantial workplans, do not hand off until lossless handoff closure is satisfied.

For review, report material findings with enough evidence and corrected-end-state information to support lossless rework, plus validation obligations/results and unresolved risks. Keep process artifacts only when they provide material engineering value.
