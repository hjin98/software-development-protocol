---
name: software-design
description: Diagnose and design nontrivial software changes, define the material engineering envelope, choose the globally justified product solution for target scale and hardware, minimize unjustified product/system complexity, design complete regression/integration acceptance, and independently review substantial implementations.
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

## Define the engineering envelope

Identify the material product requirements and constraints, including as applicable public behavior/APIs/compatibility, numerical/scientific invariants, reliability/recovery/security, workload scale, CPU/RAM/VRAM/storage/I/O/wall time, target hardware/portability, and required latency/throughput. Reject designs that cannot satisfy this envelope cleanly enough for the actual product.

## Diagnose before designing

Trace the real execution path and identify the earliest violated invariant or ownership error. Distinguish local defects from architectural/algorithmic failure.

Before adding wrappers, retries, adapters, state translators, caches, compatibility paths, supervisors, or special cases, ask whether the owning mechanism should instead be reused, consolidated, refactored, replaced, simplified, or given a better algorithm/data representation. Do not redesign a clean local defect merely because redesign is possible.

## Design the globally justified product

Freeze what implementation must not invent:

- objective/root cause and material non-goals;
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

## Accepted-workplan authority

When design produces or accepts a governing **accepted workplan**, distinguish what is **frozen**, what is **delegated to implementation**, and what may be **reopened only on evidence**. The workplan is a compressed implementation contract, not an invitation to repeat the full design search.

The workplan remains subordinate to explicit user/task requirements, safety/project instructions, and governed contracts outside the authorized change scope. Existing specifications/contracts remain authoritative except where the plan explicitly defines their intended change. Repository code/tests are evidence of actual state; they do not automatically override an accepted target merely because current behavior differs.

Implementation may perform local realization/reconciliation that preserves frozen semantics. Reopen design when evidence or a stated redesign trigger shows that a frozen material decision cannot satisfy the engineering envelope. Reopen only the affected design surface and preserve unrelated accepted decisions/evidence where still valid.

## Product complexity regression

For substantial changes or repeated work in one subsystem, inspect the affected area for duplicated functionality/state, multiple authorities, stale wrappers/fallbacks/compatibility paths, superseded mechanisms, and opportunities for semantic reuse, consolidation, refactoring, or deletion.

Prefer, when engineering fitness permits:

```text
reuse -> consolidate -> refactor -> delete
```

Reuse semantic ownership, not merely similar-looking text. Retain duplication when it is justified specialization, compatibility, migration, or an independent reference/oracle.

## Workplans, gates, and validation

Use a workplan when it materially reduces ambiguity, rediscovery, sequencing risk, or downstream rework. Use a gate when checking a boundary before proceeding materially reduces risk or wasted work. Do not add either ceremonially or remove useful ones merely to shorten/cheapen the process.

For executable changes, the non-negotiable acceptance contract is:

1. focused checks appropriate to new/modified mechanisms;
2. **stage-local affected regression** after each material behavior-changing implementation stage before dependent implementation proceeds;
3. final re-derivation of the affected behavioral surface from the assembled implementation;
4. final affected-surface regression;
5. integration testing through the assembled real product/consumer boundaries;
6. repository/project-required checks, with the broader/full suite when impact cannot be bounded confidently.

Coverage follows the affected behavioral surface; execution cost is minimized only after that breadth is established. Full production qualification remains separate from routine functional acceptance. Read `references/testing-and-validation.md` when detailed stage, evidence-reuse, or qualification rules are material.

## Independent review mode

Independent review remains an independent challenge, not acceptance of the implementation agent's summary. Start from the highest-information current evidence:

- explicit requirements and governed contracts;
- accepted workplan and its frozen/delegated/redesign boundaries;
- material final implementation/diff;
- final affected-surface derivation;
- regression/integration/benchmark evidence;
- material deviations and unresolved risks.

Independently test the highest-risk assumptions and boundaries: required functionality/correctness, scientific fidelity, algorithm/scaling, resources/hardware/performance, ownership/product complexity, failure handling, workplan deviations, stage-local/final regression, integration, unavailable checks, qualification boundaries, and unresolved risks.

Do not automatically replay the original architecture search from zero when the assembled implementation/evidence does not challenge the accepted premises. Broaden inspection or reopen original design space when evidence shows a material deviation, undermines a design premise, exposes unexpected behavior, materially regresses product complexity, fires a redesign trigger, or leaves a material unresolved risk.

Evidence-directed review is an economy rule, not a scope cap. The reviewer retains authority to inspect any surface needed to reach a sound independent conclusion.

Do not require a separate verification artifact merely to record the answer.

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

Report the chosen design/review finding, material engineering envelope, important tradeoffs, product-complexity decisions, validation obligations/results when reviewing, and genuine unresolved risks. Keep process artifacts only when they provide material engineering value.
