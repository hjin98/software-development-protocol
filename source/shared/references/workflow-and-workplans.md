# Workflow and Workplans

Protocol 5 keeps the software-development lifecycle small in role count while allowing whatever proportionate engineering work is needed to reach and establish the correct product.

## Roles

```text
software-design -> software-implementation
```

`software-design` owns diagnosis/design, engineering-envelope definition, architecture/algorithm/resource decisions, product-complexity review, **lossless translation of accepted design into the implementation contract**, validation design, and independent review when materially useful. `software-implementation` owns code changes/refactoring, repository reconciliation, adaptive realization under accepted authority, **semantic/conformance closure**, mandatory stage-local and final affected-surface regression plus integration testing, benchmarking/validation, ordinary cleanup, and completion evidence.

Testing is not a separate authority. Independent review is a mode of Software Design, not a third lifecycle role. Production qualification is not a separate lifecycle role.

## Product simplicity versus development economy

Material engineering requirements define the feasible product space. Among engineering-sufficient solutions, prefer the product with the lowest justified total product/system complexity. Only after the required product and acceptance confidence are preserved should the development process optimize human/model/context/tool/compute/I/O/wall-time cost.

Avoid redundant, ceremonial, duplicative, rediscovery-heavy, or low-information work. Do not omit materially useful design, implementation conformance, testing, review, or validation merely because a shorter or cheaper workflow exists.

## Typical workflows

Small/local executable work may look like:

```text
inspect -> implement -> conformance + affected regression -> integration -> done
```

Substantial work normally behaves like:

```text
design and diagnose
  -> translate accepted design into lossless implementation obligations
  -> handoff closure
  -> material implementation stage
       -> semantic/conformance closure
       -> focused + affected regression
  -> next material stage as needed
  -> final accepted-contract reconciliation
  -> re-derive final affected surface
  -> final affected regression + integration
  -> independent review when warranted
       -> contract conformance challenge
       -> independent engineering challenge
       -> lossless rework finding/routing when needed
```

Production qualification is appended only when explicitly requested, required by project/release policy, or necessary to establish a material production-scale/resource/performance/hardware claim.

These are patterns, not fixed gate counts. The ordering of cheap focused tests versus conformance inspection within a stage is flexible; both dimensions must close before dependent work proceeds. Add/remove process activities according to engineering value, but do not omit required conformance or stage-local/final functional acceptance merely to reduce process cost.

## Workplans as lossless implementation contracts

Use a workplan when it materially reduces rediscovery, ambiguity, sequencing risk, cross-module drift, or downstream rework.

A useful substantial-work plan contains the objective/diagnosis and protected concerns, material engineering envelope, globally justified product design/ownership/complexity decisions, implementation obligations, implementation authority, initially expected affected surface, task-specific focused/regression/integration/structural acceptance, repository-required checks, final reconciliation, production-qualification disposition when material, implementation sequence where ordering matters, and material risks/redesign triggers.

For each material obligation, preserve as applicable:

- protected concern/rationale;
- required end state;
- required constraints/preservation/forbidden behavior;
- useful expected owning/affected surface;
- required implementation consequences already determined by design;
- clearly labeled suggested realization when adaptable;
- acceptance evidence, including structural/absence evidence where behavior tests cannot prove the claim;
- stage/dependency where material.

The format is flexible; IDs/tables/matrices and persistent traceability artifacts are not required. Do not repeat generic protocol prose merely for completeness, but do not omit a known material consequence merely to compress the plan. Do not make administrative provenance, evidence filenames, report schemas, or optional telemetry acceptance requirements unless the project independently needs them.

Before accepting a substantial plan, Design performs handoff closure:

```text
requirements + protected concerns + accepted design + preservation/non-goals + known consequences
    -> implementation obligations
    -> acceptance evidence
```

No material requirement or known design consequence may disappear in that translation.

## Accepted-workplan authority

An accepted workplan distinguishes **Frozen**, **Delegated**, and **Reopen only on evidence** decisions. Precedence is:

```text
explicit user/task requirements + safety/project instructions
    -> material product requirements and governed contracts
    -> accepted workplan target decisions
    -> repository evidence about actual state
    -> implementation-local discretion
```

This is not blind-plan obedience. Current code/tests provide evidence of actual state; they do not automatically override an accepted target simply because the target intentionally changes current behavior. Existing contracts remain authoritative except where the accepted plan explicitly changes them.

Implementation may locally realize or reconcile the plan while preserving frozen semantics. A suggested realization is not automatically frozen; a required implementation consequence is not optional advice.

The accepted plan is the **minimum known contract, not a ceiling**. Necessary local consequences and newly discovered affected behavior/tests/docs/configuration/persistence/consumers that preserve frozen design are incorporated and validated by implementation. Reopen design only when evidence shows that a frozen material decision cannot satisfy the engineering envelope, conflicts irreconcilably with actual ownership/contracts, is invalidated by representative measurement, or reaches a stated redesign trigger.

When reopening is necessary, identify the invalidated decision, stop dependent work, preserve unrelated accepted stages/evidence, **reopen only the affected** design surface, update/reconcile the plan, invalidate evidence only where the changed decision can plausibly affect it, and resume from the earliest materially affected stage.

Workplans inherit generic protocol obligations from their declared `protocol_version`; later protocol releases do not silently reinterpret older active/completed plans. Explicit adoption of a newer protocol version requires reconciliation of changed obligations.

## Compact working state for long gated work

For long gated sessions, carry forward enough **compact task-local state** to avoid rediscovering accepted decisions and evidence. Keep conceptually the accepted frozen decisions, open/closed obligations, accepted stages, current affected-surface deltas, still-valid evidence, invalidated evidence, and unresolved material risks/redesign triggers. Reason from the delta since the last accepted stage rather than re-deriving unchanged state.

This working state is **not a required persistent artifact**. Do not create a ledger, database, manifest, JSON schema, or parallel evidence system solely for protocol compliance. Persist task state only when the project independently needs recovery, auditability, handoff durability, or another material capability. Final acceptance still re-derives the complete affected surface independently from the assembled candidate.

## Gates and dual stage closure

Gates are value-based. Architecture/release/project gates remain optional unless project policy requires them. A material behavior-changing implementation stage is not accepted until both dimensions close:

1. **semantic/conformance closure** confirms assigned obligations are implemented or legitimately reconciled, protected concerns/frozen decisions remain satisfied, newly discovered consequences are accounted for, and no unintended authority/obsolete path/material complexity regression was introduced; and
2. **functional closure** completes focused checks and the relevant **stage-local affected regression** for executable behavior, or carries an explicitly non-executable validation dependency to the nearest executable stage.

Define a material stage by a coherent behavior/risk boundary, not by individual files or helper edits. Several tightly coupled edits may close under one stage. Use the cheapest high-signal ordering within the stage so obvious local failures do not waste broader test cost. Semantic review never substitutes for executable regression; **green tests never prove an omitted obligation was implemented**.

Reuse still-valid intermediate evidence until a changed dimension can plausibly invalidate its claim. Do not rerun a check solely because a new agent/session began or unrelated material changed. Final assembled affected-surface regression and integration remain fresh acceptance boundaries after all material executable edits.

Use additional gates when validating a boundary before proceeding materially reduces risk or wasted downstream work, such as architecture/algorithm decisions, irreversible migration, expensive execution prerequisites, scientific semantics, or security boundaries. Do not create G0/G1/G2 merely because a template can represent them; do not remove a useful gate merely to make the process shorter or cheaper.

## Final implementation and functional acceptance

Before handoff, Implementation reconciles every material obligation against the assembled candidate, inspects for unintended/obsolete/ownership/complexity/documentation drift, and uses structural/absence evidence for removal or uniqueness claims when runtime tests cannot prove them.

For executable changes, final functional acceptance then requires re-deriving the affected surface from the assembled candidate, complete affected-surface regression, repository/project-required checks, and integration testing. When impact cannot be bounded confidently, run the broader/full available suite.

Thus final acceptance independently asks: **did we implement the accepted contract completely?** and **does the assembled affected product work?** A production run, benchmark, or qualification result cannot substitute for missing regression coverage.

## External execution

A different machine, GPU, HPC allocation, production dataset, or external service does not automatically create a handoff or qualification role. Record reproducible commands and material conditions when external execution is required. Create dedicated runners when they materially reduce repeated work/error or are product functionality.

## Documentation and hygiene

Update affected durable documentation when accepted product behavior/architecture/contracts changed. Use `software-documentation` when substantive reconciliation or publication work is useful. Use `repository-hygiene` after substantial work only when a dedicated cleanup pass materially improves repository safety/clarity.

Neither specialist is a mandatory lifecycle gate.

## Independent review and rework

Independent review remains independent and retains authority to inspect any surface needed for a sound conclusion. It should first challenge accepted-contract conformance, then challenge unplanned engineering risks and design premises, including functionality/correctness, scientific fidelity, scaling/resources/hardware/performance, product complexity/ownership, failure handling, affected surfaces, stage-local/final regression, integration, broader checks, unavailable checks, and qualification boundaries.

Material blocking findings should identify the violated requirement/invariant or new concern, evidence, affected surface, why it matters, required corrected end state/constraint, acceptance evidence, and routing when material.

Route rework as:

- **implementation nonconformance** -> same accepted design/workplan, implementation repair;
- **workplan/design deficiency** -> reconcile the affected governing design/workplan before reimplementation;
- **new independent issue** -> local implementation consequence or evidence-backed bounded redesign.

Equivalent preferences without material engineering benefit are not acceptance blockers. No separate verification report is required unless project/release/compliance policy independently requires one.
