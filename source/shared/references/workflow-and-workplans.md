# Workflow and Workplans

Protocol 5 keeps the software-development lifecycle small in role count while allowing whatever proportionate engineering work is needed to reach and establish the correct product.

## Roles

```text
software-design -> software-implementation
```

`software-design` owns diagnosis/design, engineering-envelope definition, architecture/algorithm/resource decisions, product-complexity review, validation design, and independent review when materially useful. `software-implementation` owns code changes, refactoring, mandatory stage-local and final affected-surface regression plus integration testing for executable changes, benchmarking/validation, ordinary cleanup, and completion evidence.

Testing is not a separate authority. Production qualification is not a separate lifecycle role.

## Product simplicity versus development economy

Material engineering requirements define the feasible product space. Among engineering-sufficient solutions, prefer the product with the lowest justified total product/system complexity. Only after the required product and acceptance confidence are preserved should the development process optimize human/model/context/tool/compute/I/O/wall-time cost.

Avoid redundant, ceremonial, duplicative, rediscovery-heavy, or low-information work. Do not omit materially useful design, testing, review, or validation merely because a shorter or cheaper workflow exists.

## Typical workflows

Small/local executable work may look like:

```text
inspect -> implement -> affected regression -> integration -> done
```

Substantial work normally behaves like:

```text
design
  -> material implementation stage -> focused + affected regression
  -> next material implementation stage -> focused + affected regression
  -> re-derive final affected surface
  -> final affected regression + integration
  -> independent review when warranted
```

Production qualification is appended only when explicitly requested, required by project/release policy, or necessary to establish a material production-scale/resource/performance/hardware claim.

These are patterns, not fixed gate counts. Add or remove process activities according to engineering value, but do not omit required stage-local/final functional acceptance merely to reduce process length or cost.

## Workplans

Use a workplan when it materially reduces rediscovery, ambiguity, sequencing risk, cross-module drift, or downstream rework.

A useful substantial-work plan contains:

- objective and diagnosis;
- material engineering envelope;
- globally justified product design, ownership, and important complexity decisions;
- initially expected affected behavioral/regression surface;
- focused/new tests required for changed mechanisms;
- affected regression subset required after each material behavior-changing stage;
- integration path(s) required for end-to-end functional acceptance;
- repository/project-required broader checks;
- final affected-surface reconciliation and assembled regression/integration pass;
- production qualification requirement, deferral, or explicit non-requirement;
- implementation sequence where ordering matters;
- material risks/redesign triggers.

Do not make administrative provenance, evidence filenames, report schemas, or optional telemetry acceptance requirements unless the project independently needs them.

## Accepted-workplan authority

An **accepted workplan** is a compressed implementation contract. It should make clear which material decisions are frozen, which implementation mechanics are delegated, and which assumptions or redesign triggers may reopen design.

Precedence is:

```text
explicit user/task requirements + safety/project instructions
    -> material product requirements and governed contracts
    -> accepted workplan target decisions
    -> repository evidence about actual state
    -> implementation-local discretion
```

This is not blind-plan obedience. Current code/tests provide evidence of actual state; they do not automatically override an accepted target simply because the target intentionally changes current behavior. Existing contracts remain authoritative except where the accepted plan explicitly changes them.

Implementation may locally realize or reconcile the plan while preserving frozen semantics. Reopen design only when evidence shows that a frozen material decision cannot satisfy the engineering envelope, conflicts irreconcilably with actual ownership/contracts, is invalidated by representative measurement, or reaches a stated redesign trigger.

When reopening is necessary, identify the invalidated decision, stop dependent work, preserve unrelated accepted stages/evidence, **reopen only the affected** design surface, update/reconcile the plan, invalidate evidence only where the changed decision can plausibly affect it, and resume from the earliest materially affected stage.

## Gates

Gates are value-based. Architecture/release/project gates remain optional unless project policy requires them, but a material behavior-changing implementation stage is not accepted until its relevant focused/regression checks pass or its explicitly non-executable validation dependency is carried to the nearest executable stage.

Use additional gates when validating a boundary before proceeding materially reduces risk or wasted downstream work, such as architecture/algorithm decisions, irreversible migration, expensive execution prerequisites, scientific semantics, or security boundaries.

Do not create G0/G1/G2 merely because a template can represent them. Do not remove a useful gate merely to make the process shorter or cheaper.

## Functional acceptance

For executable changes, final acceptance requires re-deriving the affected surface from the assembled candidate, complete affected-surface regression, repository/project-required checks, and integration testing. When impact cannot be bounded confidently, run the broader/full available suite.

A production run, benchmark, or qualification result cannot substitute for missing regression coverage.

## External execution

A different machine, GPU, HPC allocation, production dataset, or external service does not automatically create a handoff or qualification role. Record reproducible commands and material conditions when external execution is required. Create dedicated runners when they materially reduce repeated work/error or are product functionality.

## Documentation and hygiene

Update affected durable documentation when accepted product behavior/architecture/contracts changed. Use `software-documentation` when substantive reconciliation or publication work is useful. Use `repository-hygiene` after substantial work only when a dedicated cleanup pass materially improves repository safety/clarity.

Neither specialist is a mandatory lifecycle gate.

## Review

Independent review is appropriate when change scope/risk warrants it. Review material functionality/correctness, scientific fidelity, scaling/resources/hardware/performance, product complexity and ownership, reuse/consolidation/deletion opportunities, stage-local regression evidence, final affected-surface reconciliation and regression, integration results, repository-required/broader checks, unavailable checks, production-qualification boundaries, and unresolved material risks.

No separate verification report is required unless project/release/compliance policy independently requires one.
