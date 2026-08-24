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

First establish what the software must materially achieve: functionality/capability, correctness/scientific fidelity, reliability/recovery/security/compatibility, resource feasibility, target scale, hardware effectiveness, and materially important end-to-end performance. These requirements define the feasible product space.

Simplicity applies to the engineered product/system. Do not weaken a material requirement merely to reduce code, components, or architectural sophistication. Necessary complexity is valid when it provides material engineering value.

Development economy applies only after the required product and acceptance confidence are preserved. Avoid redundant or low-information investigation, rediscovery, repeated reasoning, unnecessary validation reruns, and other process waste; never trade a material product or acceptance requirement for lower development cost.

Do not confuse product simplicity or development economy with process minimalism. Use enough investigation, design iteration, validation planning, implementation staging, and independent review to reach and establish the right product.

## Define the engineering envelope

Identify the requirements and constraints that govern the product, including as applicable public behavior/APIs/compatibility, numerical/scientific invariants, reliability/recovery/security, workload scale, CPU/RAM/VRAM/storage/I/O/wall time, target hardware/portability, and required latency/throughput.

Treat these as a feasibility envelope rather than a rigid universal ranking. Reject designs that cannot meet it cleanly enough for the actual product.

## Diagnose before designing

Trace the real execution path and identify the earliest violated invariant or ownership error. Distinguish local defects from architectural/algorithmic failure.

Before adding wrappers, retries, adapters, state translators, caches, compatibility paths, supervisors, or special cases, ask whether the owning mechanism should instead be reused, consolidated, refactored, replaced, simplified, or given a better algorithm/data representation.

Do not redesign a clean local defect merely because redesign is possible.

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

## Product complexity regression

For substantial changes or repeated work in one subsystem, inspect the affected area for duplicated functionality/state, multiple authorities, stale wrappers/fallbacks/compatibility paths, superseded mechanisms, and opportunities for semantic reuse, consolidation, refactoring, or deletion.

Prefer, when engineering fitness permits:

```text
reuse -> consolidate -> refactor -> delete
```

Reuse semantic ownership, not merely similar-looking text. Retain duplication when it is justified specialization, compatibility, migration, or an independent reference/oracle.

## Workplans and gates

Use a workplan when it materially reduces ambiguity, rediscovery, sequencing risk, or downstream rework. Use a gate when checking a boundary before proceeding materially reduces risk or wasted work. Do not add either ceremonially, and do not remove useful ones merely to shorten the process.

For substantial executable changes, a workplan should identify:

- the initially expected affected behavioral/regression surface;
- focused/new tests needed for changed mechanisms;
- the affected regression subset required after **each material behavior-changing implementation stage**;
- integration path(s) that must work end-to-end;
- repository/project-required broader checks;
- the final affected-surface reconciliation and assembled regression/integration pass;
- whether production qualification is required, deferred, or unnecessary.

A stage-local regression gate is not optional for a material behavior-changing stage merely because final regression will run later. An atomic stage may share its final pass; a genuinely non-executable intermediate may close with the nearest executable integration stage when the dependency is explicit.

## Validation design

Coverage follows the affected behavioral surface; workload size and execution cost are then minimized subject to preserving that coverage.

For executable changes, require:

1. focused checks appropriate to new/modified mechanisms;
2. stage-local affected regression after each material behavior-changing implementation stage;
3. final regression testing of all plausibly affected existing and new behavior after re-deriving the affected surface from the assembled implementation;
4. integration testing through the assembled affected product path and real interface/consumer boundaries;
5. repository/project-required checks, with the broader/full available suite when impact cannot be bounded confidently.

The affected surface is not limited to files in the diff. Include callers/consumers, shared utilities, configuration/persistence/state/orchestration paths, interfaces, packaging, and transitive behavioral dependencies that could plausibly change.

Prefer real product interfaces over test-only reconstructions. A harness must not substantially reimplement the production algorithm it tests.

Use bounded fixtures/representative workloads where they establish the required functional evidence. Do not narrow coverage merely to make the suite faster.

Full production qualification is separate: real, long, data-heavy, target-environment execution used to characterize an already functionally accepted candidate for production-scale performance/resource/scaling/hardware claims. Do not require it as routine implementation testing unless the claim or project policy genuinely requires it.

## Independent review mode

For substantial or high-risk changes, review:

1. required functionality and material semantics;
2. correctness/scientific fidelity;
3. algorithm/data representation and target scaling;
4. resource/target-hardware behavior;
5. end-to-end performance where material;
6. product/system complexity and ownership;
7. reuse/consolidation/deletion opportunities;
8. failure handling at the owning layer;
9. whether the final affected surface was re-derived from the assembled implementation;
10. whether every material behavior-changing stage passed its relevant regression checks before dependent work proceeded;
11. whether final regression covered the complete affected surface and repository-required/broader checks ran when required;
12. whether integration exercised the assembled affected product path;
13. whether unavailable checks are honestly reported;
14. whether production qualification is correctly separated from functional acceptance;
15. unresolved material risks.

Do not require a separate verification artifact merely to record the answer.

## Supporting references

Read the packaged references when their surface is material:

- `references/workflow-and-workplans.md` — lifecycle, gates, stage acceptance, and workplans;
- `references/testing-and-validation.md` — regression/integration contract and qualification boundary;
- `references/protocol-versioning-and-compatibility.md` — protocol/candidate/evidence compatibility;
- `references/architecture-and-design.md` — ownership, redesign, and product-complexity review;
- `references/specification-and-implementation.md` — API/schema/persistence/scientific contracts;
- `references/configuration-and-policy.md` — configuration resolution and semantic identity;
- `references/concurrency-and-orchestration.md` — concurrency correctness and execution state machines;
- `references/security-and-trust-boundaries.md` — security boundaries and least privilege;
- `references/performance-and-parallelism.md` — scaling, resource budgets, accelerators, and benchmarks;
- `references/storage-and-io.md` — persistence, storage, cache/checkpoint, and recovery design;
- `references/scientific-software.md` — numerical/scientific invariants and equivalence;
- `references/repository-intake.md` — progressive repository inspection and change surfaces;
- `references/release-and-distribution.md` — built/installed artifact acceptance;
- `references/documentation-and-evidence.md` — documentation authority and durable evidence;
- `templates/implementation_workplan_template.md` — substantial implementation workplan structure.

## Completion

Report the chosen design/review finding, material engineering envelope, important tradeoffs, product-complexity decisions, validation obligations/results when reviewing, and genuine unresolved risks. Keep process artifacts only when they provide material engineering value.
