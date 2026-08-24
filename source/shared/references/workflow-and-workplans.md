# Workflow and Workplans

Protocol 5 keeps the software-development lifecycle small in role count while allowing whatever proportionate engineering work is needed to reach and establish the correct product.

## Roles

```text
software-design -> software-implementation
```

`software-design` owns diagnosis/design, engineering-envelope definition, architecture/algorithm/resource decisions, product-complexity review, validation design, and independent review when materially useful. `software-implementation` owns code changes, refactoring, mandatory stage-local and final affected-surface regression plus integration testing for executable changes, benchmarking/validation, ordinary cleanup, and completion evidence.

Testing is not a separate authority. Production qualification is not a separate lifecycle role.

## Product simplicity versus process proportionality

The protocol's simplicity doctrine targets the engineered product/system. Among solutions that satisfy the material engineering requirements, prefer the product with the lowest justified total system complexity.

The engineering process has a different objective: use a sufficient, efficient workflow that reaches and establishes the right product with appropriate confidence. Avoid redundant, ceremonial, duplicative, or low-information work; do not omit materially useful design, testing, review, or validation merely because a shorter workflow exists.

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

These are patterns, not fixed gate counts. Add or remove process activities according to engineering value, but do not omit required stage-local/final functional acceptance merely to reduce process length.

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

## Gates

Gates are value-based. Architecture/release/project gates remain optional unless project policy requires them, but a material behavior-changing implementation stage is not accepted until its relevant focused/regression checks pass or its explicitly non-executable validation dependency is carried to the nearest executable stage.

Use additional gates when validating a boundary before proceeding materially reduces risk or wasted downstream work, such as architecture/algorithm decisions, irreversible migration, expensive execution prerequisites, scientific semantics, or security boundaries.

Do not create G0/G1/G2 merely because a template can represent them. Do not remove a useful gate merely to make the process shorter.

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
