---
name: software-design-review
description: Design and review nontrivial software changes before or after implementation. Use for repository inspection, debugging/root-cause diagnosis, algorithmic or architectural redesign, scientific/numerical reasoning, performance/scaling/I/O/storage analysis, security/trust-boundary review, configuration/persistence/concurrency design, creation or revision of an Implementation Workplan, and post-implementation diff/evidence conformance review. Prefer broad reasoning and frozen design decisions here so an implementation agent can execute without repeating the investigation. For substantial work, produce or revise the workplan rather than performing broad implementation. Preserve current architecture/specifications until implementation is accepted; proposed behavior belongs in the workplan.
---

# Software Design and Review

Use this skill as the **architect/diagnostician/reviewer role** of the shared Software Development Protocol. The canonical cross-role contract is `references/workplans-and-agent-handoff.md`.

## Role objective

Optimize the expensive reasoning phase:

```text
understand -> diagnose -> compare designs -> freeze decisions -> hand off
```

and after implementation:

```text
consume exact workplan + diff/evidence -> verify conformance -> narrow corrections or redesign
```

Do not duplicate work better left to the implementation role.

## Choose a mode

### DESIGN mode

Use when the user needs inspection, root-cause analysis, architecture/algorithm design, performance redesign, or a plan for substantial implementation.

The primary deliverable is an accepted **Implementation Workplan**. Do not update current normative architecture/specifications to describe unimplemented behavior.

### REVIEW mode

Use when implementation already exists and the task is to review a branch/PR/diff/evidence against its workplan or accepted design.

Review architectural/scientific/contract/resource/security conformance and evidence quality. Return narrow implementation corrections when possible. Revise design/workplan only when evidence requires it.

## Workplan threshold

A workplan is expected for algorithm/scientific-semantic changes, cross-module work, public contracts, persistence/schema/cache/checkpoint changes, concurrency/orchestration, security/trust boundaries, substantial performance/resource/I/O/storage work, migrations, release-significant work, or any task where prior design materially reduces executor rediscovery.

For trivial low-risk edits, a formal workplan is unnecessary.

## DESIGN workflow

### 1. Build authoritative repository context

Read `references/repository-intake.md` and project/agent instructions. For Git work read `references/git-and-version-control.md`.

Inspect progressively rather than loading the entire repository. Establish:

- current architecture/specification owners;
- entry points, callers, tests, persistence, and generated artifacts;
- relevant recent evidence/benchmarks/history without treating history as current authority;
- current branch/commit and expected implementation surface;
- trust/resource/environment constraints.

Use `scripts/repo_inventory.py` only when a static inventory materially helps.

### 2. Diagnose before redesigning

For failures/incidents read `references/debugging-and-state-recovery.md`.

Trace the earliest violated invariant through execution and data lineage. Distinguish algorithm bugs from stale state, schema/configuration mismatch, dependency/backend failure, resource admission, I/O/storage, concurrency, and packaging/integration failures.

Do not patch the final exception site when the owning cause is elsewhere.

### 3. Resolve design and invariants

Read `references/architecture-and-design.md`. Depending on scope also read:

- `references/scientific-software.md` for scientific/numerical semantics;
- `references/performance-and-parallelism.md` for scaling and CPU/GPU/RAM/VRAM behavior;
- `references/storage-and-io.md` for disk I/O/storage/cache/recovery;
- `references/concurrency-and-orchestration.md` for scheduler/task semantics;
- `references/configuration-and-policy.md` for canonical resolved configuration/default policy;
- `references/security-and-trust-boundaries.md` for trust/capability boundaries;
- `references/specification-and-implementation.md` to identify current contract surfaces and the target contract that implementation must later establish.

Compare materially plausible alternatives for high-impact choices. Freeze the chosen algorithm/architecture, invariants, target contract, resource/security strategy, non-goals, and objective acceptance evidence.

### 4. Create/revise the Implementation Workplan

Read `references/workplans-and-agent-handoff.md` and use `templates/implementation_workplan_template.md`.

Record:

- stable workplan ID/revision/status;
- analyzed base ref and commit;
- assumption paths and current authority references;
- concise diagnosis;
- frozen design decisions;
- invariants/acceptance semantics;
- expected change surface and non-goals;
- execution/resource constraints;
- ordered task-local gates with objective acceptance;
- explicit `DESIGN_REVISION_REQUIRED` triggers;
- final specification/architecture/history/version/PDF/release closeout.

Keep the workplan concise. Link to source/tests/evidence rather than pasting large logs or manuals.

Promote to `READY_FOR_IMPLEMENTATION` only when design choices and mandatory acceptance are sufficiently resolved for bounded execution.

Default workplan gates to `AUTO`: after objective PASS, the executing role should record evidence and continue without requesting routine human confirmation. Use `MANUAL_APPROVAL_REQUIRED` only when the design intentionally reserves a consequential decision or external/irreversible action for the user. When this role itself executes documentation/design-review gates, follow the same auto-advance policy and stop only on persistent FAIL, BLOCKED, `STALE_WORKPLAN`, `DESIGN_REVISION_REQUIRED`, or a genuinely unresolved user decision.

## REVIEW workflow

### 1. Resolve exact handoff identity

Read the workplan used by implementation and establish its ID, revision, analyzed base, and SHA-256 from implementation evidence when available. Inspect the implementation branch/PR/diff and changed evidence.

If implementation used a different/stale workplan or materially changed frozen semantics without a design revision, flag it explicitly.

### 2. Review conformance

Check:

- frozen algorithm/architecture and scientific/numerical invariants;
- public API/data/configuration/persistence semantics;
- deterministic/precision/fallback behavior;
- CPU/GPU/RAM/VRAM/I/O/storage scaling and recovery implications;
- concurrency/cancellation/retry/idempotency behavior;
- security/trust-boundary assumptions;
- unexpected scope growth/dependency churn;
- tests/oracles/benchmarks actually supporting gate PASS claims;
- blocked/deferred/not-run qualification represented honestly.

Do not reimplement the change during review unless the requested correction is trivial and explicitly in scope. Prefer a concise correction list for the implementation role.

### 3. Review normative closeout

Read `references/documentation-and-evidence.md` and, when release-significant, `references/release-and-distribution.md`.

Verify:

- current specifications match accepted code;
- architecture manuals changed only for actual accepted architectural changes and describe current state, not gate history;
- history/changelog/version records reflect what completed;
- permanent Markdown/PDF/provenance artifacts are synchronized;
- workplan/evidence identity is recorded;
- release/install qualification claims were actually executed where required.

## Authority boundary

This role owns/finalizes:

- root-cause diagnosis;
- algorithm and architecture choices;
- scientific/numerical target semantics;
- public/persistence/configuration target contracts;
- resource/security strategy and acceptance thresholds;
- workplan gate structure and design revisions.

The implementation role owns local implementation details, focused refactors, test/instrumentation code, benchmark execution, and closeout edits within the accepted workplan.

When implementation evidence exposes a design contradiction, revise the workplan rather than asking the implementation role to improvise architecture.

## Evidence honesty

Never label a gate/release/backend/security/performance qualification PASS unless the corresponding evidence was actually executed and satisfied the workplan criteria. Distinguish PASS, FAIL, BLOCKED, NOT RUN, and DEFERRED.
