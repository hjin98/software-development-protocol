# Workflow and Workplans

Protocol 5 keeps the software-development lifecycle small in role count while allowing whatever proportionate engineering work is needed to reach and establish the correct product.

## Shared engineering objective

Every protocol actor is a steward of the stakeholder's durable software outcome. Workplans, tests, gates, metrics, reviews, and reports define constraints or provide evidence; they are not terminal objectives. Stage/final closure is earned by product/conformance/evidence state and must never create pressure to manufacture a pass.

Long-horizon stewardship is bounded by explicit stakeholder requirements, governed contracts, the accepted engineering envelope, plausibly affected surfaces, and material maintenance/operation consequences. It does not authorize unrelated enhancements or speculative refactoring. Development economy chooses among engineering-valid paths; it cannot justify weaker durability, hidden debt, weaker evidence, deferred known correctness work, or premature closure.

## Roles

```text
software-design -> software-implementation
```

`software-design` owns diagnosis/design, engineering-envelope definition, architecture/algorithm/resource decisions, product-complexity review, **lossless translation of accepted design into the implementation contract**, validation design, and independent review. `software-implementation` owns code/refactoring, repository reconciliation, adaptive realization under accepted authority, **semantic/conformance closure**, mandatory stage-local and final affected-surface regression plus integration, benchmarking/validation, ordinary cleanup, and completion evidence.

Testing is not a separate authority. Independent review is a mode of Software Design, not a third lifecycle role. Production qualification is not a separate lifecycle role.

## Product simplicity versus development economy

Material engineering requirements define the feasible product space. Among engineering-sufficient solutions, prefer the lowest justified total product/system complexity. Only after product and required acceptance confidence are preserved should development optimize human/model/context/tool/compute/I/O/wall-time cost.

Avoid redundant, ceremonial, rediscovery-heavy, or low-information work. Do not omit materially useful design, conformance, testing, review, or validation merely because a shorter workflow exists.

## Typical workflows

Small/local executable work may look like:

```text
inspect -> implement -> conformance + affected regression -> integration -> done
```

Substantial work normally behaves like:

```text
design/diagnose
  -> lossless implementation obligations + handoff closure
  -> coherent material implementation stage
       -> semantic/conformance closure
       -> focused + affected regression
  -> next material stage only when a real behavior/risk boundary exists
  -> final accepted-contract reconciliation
  -> re-derive final affected surface
  -> final affected regression + integration
  -> independent review when warranted
```

Production qualification is appended only when explicitly requested, required by project/release policy, or necessary for a material production-scale/resource/performance/hardware claim. These are patterns, not fixed gate counts.

## Workplans as lossless implementation contracts

Use a workplan when it materially reduces rediscovery, ambiguity, sequencing risk, cross-module drift, or downstream rework. A substantial plan preserves objective/diagnosis, protected concerns, engineering envelope, product design/ownership/complexity decisions, implementation obligations/authority, initially expected affected surface, task-specific acceptance, repository-required checks, final reconciliation, qualification disposition when material, sequence where ordering matters, and redesign triggers.

For each material obligation preserve, as applicable: concern/rationale; required end state; required constraints/preservation/forbidden behavior; expected owning/affected surface; required implementation consequences already determined by design; clearly labeled suggested realization when adaptable; acceptance evidence including structural/absence evidence where runtime behavior cannot prove the claim; and stage/dependency where material.

The format is flexible. IDs/tables/matrices and persistent traceability artifacts are not required. Do not copy generic protocol prose merely for completeness, but do not omit a known material consequence merely to compress the plan. A known local shortcut that could satisfy wording/evidence while defeating stakeholder outcome should receive a concise anti-shortcut/integrity constraint.

When material acceptance depends on a real production owner/consumer boundary, preserve the claim, required real owner/path, allowed doubles, forbidden substitutions, and observable evidence enough to prevent proxy acceptance. An explicitly frozen real-owner boundary cannot be silently weakened as implementation-local reconciliation.

Before accepting substantial work, Design closes:

```text
requirements + protected concerns + accepted design + preservation/non-goals + known consequences
    -> implementation obligations -> acceptance evidence
```

No material requirement or known design consequence may disappear.

### Snapshot-complete handoff

The accepted current handoff artifact set must be **snapshot-complete** for still-binding task-specific semantics. Reconcile accepted amendments/review corrections into supplied current authority; do not leave a requirement only in Git history, prior chat/session context, PR/issue/review discussion, superseded revisions, or an external document not actually supplied.

Current composition remains valid: a workplan may inherit generic rules from its declared `protocol_version` and reference current supplied protocol/specification/architecture/package authorities. Snapshot completeness is not a single-file rule and does not require copying generic protocol doctrine into each workplan.

Apply the **snapshot-loss counterfactual** before handoff: conceptually remove `.git`, prior conversation/review history, superseded revisions not supplied, and external links/resources not supplied. If the remaining supplied current artifacts do not recover every material task-specific requirement, decision, acceptance boundary, and redesign trigger, handoff is not closed.

Historical identifiers/links may remain provenance/navigation but are not sufficient normative storage. If Implementation finds a still-binding requirement dependent on unavailable historical/unsupplied material, route it as a **workplan/design deficiency** rather than guessing. Do not create a mandatory handoff manifest, revision ledger, provenance database, evidence capsule, or semantic workplan linter solely for this rule.

## Accepted-workplan authority

An accepted workplan distinguishes **Frozen**, **Delegated**, and **Reopen only on evidence**. Precedence is:

```text
explicit user/task requirements + safety/project instructions
    -> material product requirements and governed contracts
    -> accepted workplan target decisions
    -> repository evidence about actual state
    -> implementation-local discretion
```

This is not blind-plan obedience. Current code/tests provide evidence of actual state; they do not automatically override an accepted target merely because the target intentionally changes current behavior. Existing contracts remain authoritative except where the accepted plan explicitly changes them.

Implementation may locally realize/reconcile the plan while preserving frozen semantics. A **suggested realization is not automatically frozen**; a required implementation consequence is not optional advice.

The accepted plan is the **minimum known contract, not a ceiling**. Necessary local consequences and **newly discovered affected behavior**/tests/docs/configuration/persistence/consumers that preserve frozen design are incorporated and validated. Reopen design only when evidence shows a frozen material decision cannot satisfy the engineering envelope, conflicts irreconcilably with ownership/contracts, is invalidated by representative measurement, or reaches a stated trigger.

When reopening is necessary, identify the invalidated decision, stop dependent work, preserve unrelated accepted stages/evidence, **reopen only the affected** design surface, update/reconcile authority, invalidate evidence only where the changed decision can alter its claim, and resume from the earliest materially affected stage.

Workplans inherit generic obligations from their declared protocol version; later releases do not silently reinterpret older active/completed plans. Explicit adoption of a newer backward-compatible version requires reconciliation of changed obligations.

## Convergence trigger and conditional owner

The first clean local defect remains local and receives an owning-layer repair plus proportionate consideration of obvious variants. Material sibling recurrence, a canonical mechanism with bypasses, family-level review blockers, or claimed family closure whose adequacy becomes material triggers [Convergence and development-cycle economy](convergence-and-cycle-economy.md).

That reference owns detailed semantic-family definition, bounded family closure, post-family Design reconsideration, review readiness, blocker-family saturation/stopping rules, closure horizons, revision economy, and cycle-economy method. No recurrence/review count can force acceptance. Keep compact triggers here so conditional extraction never hides the escalation boundary.

## Compact working state for long gated work

For long gated sessions, carry enough compact task-local state to avoid rediscovering accepted decisions/evidence: frozen decisions, open/closed obligations, accepted stages, affected-surface deltas, still-valid/invalidated evidence, and unresolved risks/redesign triggers. Reason from the delta since the last accepted stage rather than re-deriving unchanged state.

This is **not a required persistent artifact**. Do not create a ledger/database/manifest/parallel evidence system solely for protocol compliance. Persist task state only when the project independently needs recovery, auditability, handoff durability, or another capability. Final acceptance still re-derives the complete affected surface from the assembled candidate.

## Gates and dual stage closure

Gates are value-based. Architecture/release/project gates remain optional unless project policy requires them. A material behavior-changing implementation stage is not accepted until both dimensions close:

1. **semantic/conformance closure** — assigned obligations are implemented or legitimately reconciled, protected concerns/frozen decisions remain satisfied, newly discovered consequences are accounted for, no unintended authority/obsolete path/material complexity regression was introduced, and material acceptance evidence has not bypassed the semantic owner whose behavior constitutes the claim;
2. **functional closure** — focused checks and the relevant **stage-local affected regression** execute for changed behavior, or an explicitly non-executable validation dependency is carried to the nearest executable stage.

Define a material stage by a coherent behavior/risk boundary, not individual files/helpers. **Several tightly coupled edits may close under one stage.** Use the cheapest high-signal order within the stage. Semantic review never substitutes for executable regression; **green tests never prove an omitted obligation was implemented**.

Reuse still-valid intermediate evidence until a changed dimension can plausibly invalidate its claim. Do not rerun a check solely because a new agent/session began or unrelated material changed. Final assembled affected-surface regression/integration remain fresh acceptance boundaries after material executable edits.

Use additional gates when validating a boundary before proceeding materially reduces risk/rework, such as architecture/algorithm decisions, irreversible migration, expensive execution prerequisites, scientific semantics, or security boundaries. Do not create numbered micro-gates merely because a template can represent them.

## Final implementation and functional acceptance

Before handoff, Implementation reconciles every material obligation against the assembled candidate, inspects unintended/obsolete/ownership/complexity/documentation drift, and uses structural/absence evidence for removal/uniqueness claims when runtime tests cannot prove them.

For executable changes, final acceptance then requires re-deriving the affected surface from the assembled candidate, complete affected-surface regression, repository/project-required checks, and integration testing. When impact cannot be bounded confidently, run the broader/full available suite.

Thus final acceptance independently asks: **did we implement the accepted contract completely?** and **does the assembled affected product work?** Production runs/benchmarks/qualification cannot substitute for missing regression coverage.

## External execution

A different machine, GPU, HPC allocation, production dataset, or external service does not automatically create a handoff/qualification role. Record reproducible commands and material conditions when external execution is required. Create dedicated runners when they materially reduce repeated work/error or are product functionality.

## Documentation and hygiene

Update affected durable documentation when accepted behavior/architecture/contracts changed. Use `software-documentation` when substantive reconciliation/publication work is useful. Use `repository-hygiene` after substantial work only when a dedicated cleanup pass materially improves repository safety/clarity. Neither specialist is a mandatory lifecycle gate.

## Independent review and rework

Independent review remains independent and may inspect any surface needed for a sound conclusion. It first challenges accepted-contract/outcome conformance, then unplanned engineering risks/design premises including functionality/correctness, scientific fidelity, scaling/resources/hardware/performance, complexity/ownership, failure handling, affected surfaces, stage/final regression, integration, broader checks, unavailable checks, and qualification boundaries.

Material blockers identify the violated requirement/invariant or new concern, evidence, affected surface, why it matters, corrected end state/constraint, acceptance evidence, and routing when material.

Route rework as:

- **implementation nonconformance** -> same accepted design/workplan, implementation repair;
- **workplan/design deficiency** -> reconcile affected governing design/workplan before reimplementation;
- **new independent issue** -> local necessary consequence or evidence-backed bounded redesign.

Equivalent preferences without material engineering benefit are not blockers. Missing required implementation closure/evidence does not authorize a reviewer to refuse an explicitly requested review; detailed recurrence/readiness/saturation semantics live in the convergence reference. No separate verification report is required unless project/release/compliance policy independently requires one.
