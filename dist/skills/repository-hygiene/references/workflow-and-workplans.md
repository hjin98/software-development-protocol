# Workflow and Workplans

Protocol 5 keeps the lifecycle small while allowing proportionate engineering work needed to establish the correct product.

## Shared engineering objective

Every protocol actor is a steward of the stakeholder's durable software outcome. Workplans, tests, gates, metrics, reviews, reports, and implementation mechanisms are constraints, evidence, or solutions; they are **not terminal objectives**. Stage/final closure is earned by product/conformance/evidence state and **must never create pressure to manufacture a pass**.

Long-horizon stewardship is bounded by explicit stakeholder requirements, governed contracts, the accepted engineering envelope, plausibly affected surfaces, and material maintenance/operation consequences. It does not authorize unrelated enhancements or speculative refactoring.

## Roles

```text
software-design -> software-implementation
```

`software-design` owns diagnosis/design, Tier-1 engineering-envelope definition, high-level architecture/algorithm/resource decisions, product-complexity review, lossless translation of accepted design into the implementation contract, validation design, and independent review. `software-implementation` owns code/refactoring, repository reconciliation, adaptive realization beneath Frozen authority, semantic/conformance closure, stage-local/final affected-surface regression plus integration, benchmarking/validation, ordinary cleanup, and completion evidence.

Testing is not a separate authority. Independent review is a mode of Software Design, not a third lifecycle role. Production qualification is not a separate lifecycle role.

## Product simplicity versus development economy

Material Tier-1 engineering requirements define the feasible product space. Among engineering-sufficient realizations, prefer the lowest justified total product/system complexity. This simplicity rule applies both prospectively when choosing a solution and retrospectively when accumulated structural complexity shows the current realization should be reduced or re-derived.

Only after product fitness and simplicity are preserved should development optimize human/model/context/tool/compute/I/O/wall-time cost.

## Typical workflows

Small/local executable work may look like:

```text
inspect -> implement -> conformance + affected regression -> integration -> done
```

Substantial work normally behaves like:

```text
design/diagnose
  -> classify problem/product invariants
  -> freeze only high-level architecture
  -> delegate lower-level solution space
  -> coherent material implementation stage
       -> semantic/conformance closure
       -> focused + affected regression
  -> active simplification if structural complexity triggers fire
  -> final accepted-contract reconciliation
  -> re-derive final affected surface
  -> final affected regression + integration
  -> independent review when warranted
```

These are patterns, not fixed gate counts. Production qualification is appended only when independently required.

## Workplans as bounded implementation contracts

Use a workplan when it materially reduces rediscovery, ambiguity, sequencing risk, cross-module drift, or downstream rework.

A substantial workplan separates three authority classes:

1. **Problem/product invariants** — the stakeholder/domain outcomes and governed contracts that define what must ultimately be true.
2. **Frozen high-level architecture** — material solution decisions Design deliberately fixes for the current cycle.
3. **Delegated solution space** — implementation realization that remains replaceable, reducible, consolidatable, or deletable while the first two classes remain satisfied.

Task-specific obligations preserve required outcomes/constraints, important preservation/non-goals, acceptance evidence, useful affected/owning surfaces, and sequencing where material. They are not a frozen proof script. A suggested realization is not automatically Frozen. A detailed mechanism does not become binding merely because a prior plan named it.

A known downstream consequence is binding only because it is logically necessary to an already-binding product invariant or Frozen architecture decision. Implementation may satisfy that parent authority through an equivalent simpler realization unless the realization itself was explicitly frozen at architecture level.

The accepted plan is the **minimum known contract, not a ceiling** in this bounded sense: newly discovered affected behavior and logically necessary consequences of existing product/Frozen architecture must be incorporated and validated. Discovery does not mint new product capability, does not grant an incidental mechanism invariant status, and does not authorize unrelated improvement.

For material obligations, preserve as applicable: concern/rationale, required end state, required constraints/preservation/forbidden behavior, useful expected owning/affected surface, task-specific acceptance evidence, and stage/dependency where material. **Attach only when material**: a suggested realization, an **acceptance boundary** when proxy acceptance is a material risk, or an **anti-shortcut / integrity constraint** when local wording/evidence could defeat the stakeholder outcome.

When material acceptance depends on a **real production owner/consumer boundary**, preserve the claim, required real owner/path, allowed doubles, forbidden substitutions, and observable evidence enough to prevent proxy acceptance.

## Affected surface is not requirement surface

The affected surface can expand during implementation: additional callers, consumers, shared utilities, configuration, persistence, state, orchestration, interfaces, packaging, documentation, and transitive behavior may require implementation or validation.

**Affected-surface expansion is not requirement expansion.** It expands inspection, implementation impact, and acceptance coverage where existing Tier-1/Frozen semantics propagate. It does not by itself create a new product capability, freeze the current mechanism, or turn a solution-created intermediate problem into a product invariant.

## Snapshot-complete handoff

The accepted current handoff artifact set must be **snapshot-complete** for still-binding task-specific product/problem invariants, Frozen architecture, non-goals, acceptance boundaries, and redesign/simplification triggers. Reconcile accepted amendments/review corrections into supplied current authority; do not leave a requirement only in Git history, prior chat/session context, PR/issue/review discussion, superseded revisions, or an external document not actually supplied.

Current composition remains valid: a workplan may inherit generic rules from its declared `protocol_version` and reference current supplied protocol/specification/architecture/package authorities. Snapshot completeness is not a single-file rule and does not require copying generic doctrine into each workplan.

Apply the **snapshot-loss counterfactual** before handoff: conceptually remove `.git`, prior conversation/review history, superseded revisions not supplied, and external links/resources not supplied. If the remaining supplied current artifacts do not recover every still-binding task-specific product/Frozen decision and material acceptance boundary, handoff is not closed. Obsolete implementation-realization history is not normative storage.

Do not create a mandatory handoff manifest, revision ledger, provenance database, evidence capsule, or semantic workplan linter solely for this rule.

## Accepted-workplan authority

Precedence is:

```text
explicit user/task requirements + safety/project instructions
    -> material product requirements and governed contracts
    -> explicitly Frozen high-level workplan decisions
    -> repository evidence about actual state
    -> delegated implementation-local discretion
```

Repository code/tests provide evidence of actual state; they do not automatically override an accepted target or become product authority through existence.

Implementation may locally realize/reconcile the plan while preserving product/Frozen semantics. An **equivalent local realization** may remove, consolidate, or replace previously expected Tier-2 machinery. If a materially simpler realization would change Frozen high-level architecture, route to bounded Design reconsideration instead of silently changing it.

Reopen Design only when evidence shows a Frozen decision cannot satisfy the engineering envelope, conflicts irreconcilably with actual ownership/contracts, is invalidated by representative measurement, or reaches a stated redesign trigger. Reopen only the affected design surface, preserve unrelated accepted stages/evidence, and resume from the earliest materially affected dependency.

Workplans inherit generic obligations from their declared protocol version; later releases do not silently reinterpret older active/completed plans. Explicit adoption of a newer backward-compatible version requires reconciliation of changed obligations.

## Convergence trigger and active simplicity

The **first clean local defect remains local** and receives an owning-layer repair plus proportionate consideration of obvious variants.

**Material sibling recurrence** changes the unit of reasoning from isolated instances to the shared owner/mechanism. Recurrence alone does not require preserving that mechanism. When recurrence or other structural evidence shows patch-on-patch repair, duplicated/synchronized state, competing authorities, accumulating wrappers/fallbacks/special cases, or a materially simpler realization, active Tier-2 simplification/re-derivation is required before another additive durable repair.

Detailed bounded recurrence/family/review-economy semantics live in `convergence-and-cycle-economy.md`. Use finite family census when the product correctness claim itself requires bounded completeness or when sibling discovery is needed to simplify/canonicalize safely. Post-simplification recurrence or evidence that Frozen architecture is wrong routes to bounded Design reconsideration. **No recurrence/review count can force acceptance**; escalation changes engineering method, not the pass threshold.

## Compact working state for long gated work

For long gated sessions, carry enough compact task-local state to avoid rediscovering accepted decisions/evidence: product/Frozen decisions, open/closed obligations, accepted stages, affected-surface deltas, still-valid/invalidated evidence, and unresolved risks/redesign/simplification triggers.

This is **not a required persistent artifact**. Do not create a ledger/database/manifest/parallel evidence system solely for protocol compliance.

## Gates and dual stage closure

Gates are value-based. A material behavior-changing implementation stage is not accepted until both dimensions close:

1. **semantic/conformance closure** — assigned obligations are implemented or legitimately reconciled, product/Frozen decisions remain satisfied, newly discovered affected behavior is accounted for, and no unintended authority/obsolete path/material complexity regression was introduced; and
2. **functional closure** — focused checks and the relevant **stage-local affected regression** execute for changed behavior, or an explicitly non-executable validation dependency is carried to the nearest executable stage.

Define a material stage by a coherent behavior/risk boundary, not individual files/helpers. **Several tightly coupled edits may close under one stage.** Use the cheapest high-signal order. Semantic review never substitutes for executable regression; **green tests never prove an omitted obligation was implemented**.

Reuse still-valid intermediate evidence until a changed dimension can plausibly invalidate its claim. Final assembled affected-surface regression/integration remain fresh acceptance boundaries after material executable edits.

## Final implementation and functional acceptance

Before handoff, Implementation reconciles every material product/Frozen obligation against the assembled candidate, inspects unintended/obsolete/ownership/complexity/documentation drift, and uses structural/absence evidence for removal/uniqueness claims when runtime tests cannot prove them.

For executable changes, final acceptance requires re-deriving the affected surface from the assembled candidate, complete affected-surface regression, repository/project-required checks, and integration testing. When impact cannot be bounded confidently, run the broader/full available suite.

Thus final acceptance independently asks: **did we implement the accepted product/Frozen contract completely?** and **does the assembled affected product work?** Production runs/benchmarks/qualification cannot substitute for missing regression coverage.

## External execution, documentation, and hygiene

A different machine, GPU, HPC allocation, production dataset, or external service does not automatically create a new role. Record reproducible commands/material conditions when external execution is required.

Update affected durable documentation when accepted behavior/architecture/contracts changed. Optional specialists remain supporting capabilities, not lifecycle gates.

## Independent review and rework

Independent review remains independent and may inspect any surface needed for a sound conclusion. It first challenges product/Frozen contract conformance, then unplanned engineering risks/design premises including functionality/correctness, scientific fidelity, scaling/resources/hardware/performance, complexity/ownership, failure handling, affected surfaces, regression/integration, unavailable checks, and qualification boundaries.

When a finding asks to preserve or add implementation machinery, identify the Tier-1/Frozen authority it protects. If the problem exists only because of delegated solution machinery, challenge that machinery under Tier 2 before demanding another patch.

Route rework as:

- **implementation nonconformance** -> same accepted product/Frozen design, implementation repair/refactor;
- **workplan/design deficiency** -> reconcile affected governing design/workplan before reimplementation;
- **new independent issue** -> local necessary consequence, separate issue, or evidence-backed bounded redesign according to its authority.

Equivalent preferences without material engineering benefit are not blockers. No separate verification report is required unless project/release/compliance policy independently requires one.
