# Workflow and Workplans

Protocol 5 keeps the lifecycle small in role count while allowing whatever proportionate engineering work is needed to reach and establish the correct product.

## Roles

```text
software-design -> software-implementation
```

`software-design` owns diagnosis/design, engineering-envelope definition, architecture/algorithm/resource decisions, product-complexity review, **lossless translation of accepted design into the implementation contract**, validation design, and independent review when materially useful. `software-implementation` owns repository reconciliation, code/refactoring, adaptive realization under accepted authority, **semantic/conformance closure**, mandatory stage-local and final affected-surface regression plus integration testing, benchmarking/validation, cleanup, and delivery.

Testing is not a separate authority. Independent review is a mode of Software Design, not a third lifecycle role. Production qualification is not a lifecycle role.

## Product simplicity versus development economy

Material engineering requirements define the feasible product space. Among engineering-sufficient solutions, prefer the product with the lowest justified total product/system complexity. Only after the required product and acceptance confidence are preserved should the development process optimize human/model/context/tool/compute/I/O/wall-time cost.

Avoid redundant, ceremonial, duplicative, rediscovery-heavy, or low-information work. Do not omit materially useful design, implementation conformance, testing, review, or validation merely because a shorter workflow exists.

## Typical substantial workflow

```text
design and diagnose
  -> translate accepted design into lossless implementation obligations
  -> handoff closure
  -> implementation stage
       -> semantic/conformance closure
       -> focused + affected regression
  -> next stage as needed
  -> final accepted-contract reconciliation
  -> re-derive final affected surface
  -> final affected regression + integration
  -> independent review when warranted
       -> contract conformance challenge
       -> independent engineering challenge
       -> lossless rework finding/routing when needed
```

The ordering of cheap focused tests versus conformance inspection within a stage is flexible; both dimensions must close before dependent work proceeds. These are behavior/risk boundaries, not fixed gate counts.

## Workplans as lossless implementation contracts

Use a workplan when it materially reduces rediscovery, ambiguity, sequencing risk, cross-module drift, or downstream rework.

A substantial workplan must be compressed without losing task-specific intent. It should contain objective/diagnosis, engineering envelope, product design, implementation authority, expected affected surface, task-specific acceptance, sequence where material, and implementation obligations detailed enough to preserve each material protected concern and known consequence.

For material obligations, preserve as applicable the protected concern/rationale, required end state, required constraints/forbidden behavior, useful expected owning/affected surface, required implementation consequences, clearly labeled suggested realization, acceptance evidence, and stage/dependency. The format is flexible; persistent matrices/IDs are not required.

Before acceptance, Design performs handoff closure:

```text
requirements + protected concerns + accepted design + preservation/non-goals + known consequences
    -> implementation obligations
    -> acceptance evidence
```

No material requirement or known design consequence may disappear in that translation.

## Accepted-workplan authority

An accepted workplan distinguishes **Frozen**, **Delegated**, and **Reopen only on evidence** decisions. Precedence remains:

```text
explicit user/task requirements + safety/project instructions
    -> material product requirements and governed contracts
    -> accepted workplan target decisions
    -> repository evidence about actual state
    -> implementation-local discretion
```

Implementation may locally realize or reconcile the plan while preserving frozen semantics. Suggested realization is not automatically frozen; a required implementation consequence is not optional advice.

The plan is the **minimum known contract, not a ceiling**. Necessary local consequences and newly discovered affected surfaces that preserve frozen design are incorporated and validated by implementation. Reopen design only when evidence shows a frozen material decision must change. When reopening is necessary, identify the invalidated decision, stop dependent work, preserve unrelated accepted stages/evidence, reopen only the affected design surface, reconcile the plan, invalidate only affected evidence, and resume from the earliest materially affected stage.

## Compact working state for long gated work

Carry forward enough task-local state to avoid rediscovery: accepted frozen decisions, open/closed obligations, accepted stages, affected-surface deltas, still-valid/invalidated evidence, and unresolved risks/redesign triggers. This is **not a required persistent artifact**. Do not create a ledger, database, manifest, or parallel evidence system solely for protocol compliance.

## Dual stage closure

A material implementation stage is a coherent behavior-changing/risk unit. It closes only when:

1. **semantic/conformance closure** confirms all assigned obligations are implemented or legitimately reconciled, protected concerns/frozen decisions remain satisfied, newly discovered consequences are accounted for, and no unintended authority/obsolete path/material complexity regression was introduced; and
2. **functional closure** completes focused checks and the relevant affected regression for executable behavior.

Several tightly coupled edits may close under one stage. Do not micro-gate every file/helper edit. Use the cheapest high-signal ordering within the stage. Semantic review never substitutes for executable regression; green tests never establish an omitted obligation.

## Final implementation closure

Before handoff, Implementation reconciles every material obligation against the assembled candidate, inspects for unintended/obsolete/ownership/complexity/documentation drift, and uses structural/absence evidence for removal or uniqueness claims when runtime tests cannot prove them. It then re-derives the final affected surface and completes fresh final affected regression, integration, and repository/project-required checks.

Thus final acceptance asks independently: **did we implement the accepted contract completely?** and **does the assembled affected product work?**

## Review and rework

Independent review remains independent and retains authority to inspect any needed surface. It should first challenge accepted-contract conformance, then challenge unplanned engineering risks and design premises.

Material blocking findings should identify the violated requirement/invariant or new concern, evidence, affected surface, why it matters, required corrected end state/constraint, acceptance evidence, and routing when material.

Route rework as:

- **implementation nonconformance** -> same accepted design/workplan, implementation repair;
- **workplan/design deficiency** -> reconcile the affected governing design/workplan before reimplementation;
- **new independent issue** -> local implementation consequence or evidence-backed bounded redesign.

Equivalent preferences without material engineering benefit are not acceptance blockers.

## Functional acceptance and production qualification

Executable changes retain focused checks, stage-local affected regression, final affected-surface re-derivation/regression, integration, repository/project-required checks, and broader/full suites when impact cannot be bounded confidently. Production qualification remains separate and cannot substitute for functional acceptance.

## Documentation and hygiene

Update affected durable documentation when accepted product behavior/architecture/contracts changed. Optional documentation/hygiene specialists remain supporting capabilities, not approval gates.
