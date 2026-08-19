---
name: software-design
description: Design nontrivial software changes before implementation. Use for repository inspection, debugging/root-cause diagnosis, algorithmic or architectural redesign, scientific/numerical reasoning, performance/scaling/I/O/storage analysis, security/trust-boundary design, configuration/persistence/concurrency design, and creation or revision of an Implementation Workplan. Freeze decisions and acceptance semantics here so implementation and qualification do not repeat the investigation. Do not perform broad implementation when a workplan is the appropriate deliverable.
---

# Software Design

Use this skill as the **design authority** of Software Development Protocol v3. The cross-role lifecycle is defined in `references/workplans-and-agent-handoff.md`; protocol compatibility is defined in `references/protocol-versioning-and-compatibility.md`.

## Role objective

```text
understand
-> diagnose
-> compare materially plausible designs
-> freeze target semantics/invariants/acceptance
-> issue READY_FOR_IMPLEMENTATION workplan
```

This role owns the target design. It does not own implementation execution, target-environment qualification, or final merge acceptance.

## 1. Build authoritative context

Read repository/project instructions plus:

- `references/repository-intake.md`
- `references/git-and-version-control.md`
- current architecture/specification owners relevant to the task.

Inspect progressively. Establish current branch/commit, entry points/callers/tests, persistence/generated artifacts, relevant current evidence, trust/resource constraints, and assumption paths.

## 2. Diagnose before redesigning

For failures/incidents read `references/debugging-and-state-recovery.md`.

Find the earliest violated invariant and distinguish algorithm defects from stale state, schema/configuration mismatch, dependency/backend failure, resource admission, storage/I/O, concurrency, packaging, or integration failures.

Do not freeze a design around a symptom-level patch when ownership lies elsewhere.

## 3. Resolve the target design

Read `references/architecture-and-design.md` plus the domain references needed by the change:

- `references/scientific-software.md`
- `references/performance-and-parallelism.md`
- `references/storage-and-io.md`
- `references/concurrency-and-orchestration.md`
- `references/configuration-and-policy.md`
- `references/security-and-trust-boundaries.md`
- `references/specification-and-implementation.md`
- `references/testing-and-qualification.md`
- `references/release-and-distribution.md`

Freeze as applicable:

- chosen algorithm/architecture and ownership;
- scientific/numerical/API/data/configuration semantics;
- persistence/schema/recovery contract;
- compatibility and fallback behavior;
- resource/security strategy;
- objective acceptance thresholds;
- qualification capabilities/barriers;
- non-goals and design-revision triggers.

For expensive baselines, permit reuse of existing authenticated evidence only when its source/input/method/environment identity remains applicable.

## 4. Create or revise the Implementation Workplan

Use `templates/implementation_workplan_template.md`.

A substantial workplan records:

- `workplan_id`, revision, protocol version, analyzed base/ref;
- assumption paths and current authority refs;
- concise diagnosis;
- frozen design decisions and invariants;
- expected change surface/non-goals;
- qualification capability requirements;
- implementation/qualification/acceptance state per gate;
- explicit `qualification_barrier` where later implementation must wait for runtime evidence;
- exact acceptance and evidence expectations;
- `DESIGN_REVISION_REQUIRED` triggers;
- candidate and final closeout requirements.

Promote to `READY_FOR_IMPLEMENTATION` only when implementation can proceed without inventing architecture.

## 5. Gate dependency design

Default approval is `AUTO`.

A gate has three distinct concepts:

```text
implementation state
qualification state
acceptance state
```

Implementation may prepare later independent gates before expensive qualification when `qualification_barrier: no`. Set `qualification_barrier: yes` when a later implementation decision is unsafe without that gate's runtime result.

Do not weaken mandatory acceptance merely to batch execution.

## 6. Protocol v2 intake

For v2 workplans/artifacts follow `references/protocol-versioning-and-compatibility.md`.

Do not mechanically rewrite completed v2 history. Upgrade active/substantial continuation work to a v3 workplan when split qualification is required.

## Authority boundary

This role owns/finalizes:

- root-cause diagnosis;
- algorithm/architecture choice;
- scientific/numerical target semantics;
- public/persistence/configuration target contracts;
- resource/security strategy;
- gate structure/mandatory acceptance;
- design revisions.

Implementation may refine local details but must escalate frozen-design contradictions.

## Completion report

Report the exact workplan ID/revision/base, frozen decisions, qualification capabilities/barriers, unresolved/deferred items, and repository branch state.
