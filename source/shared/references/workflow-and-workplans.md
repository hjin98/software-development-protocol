# Workflow and Workplans

Protocol 5 keeps the software-development lifecycle small in role count while allowing whatever proportionate engineering work is needed to reach and establish the correct product.

## Roles

```text
software-design -> software-implementation
```

`software-design` owns diagnosis/design, engineering-envelope definition, architecture/algorithm/resource decisions, product-complexity review, validation design, and independent review when materially useful. `software-implementation` owns code changes, refactoring, mandatory affected-surface regression and integration testing for executable changes, benchmarking/validation, ordinary cleanup, and completion evidence.

Testing is not a separate authority. Production qualification is not a separate lifecycle role.

## Product simplicity versus process proportionality

The protocol's simplicity doctrine targets the engineered product/system. Among solutions that satisfy the material engineering requirements, prefer the product with the lowest justified total system complexity.

The engineering process has a different objective: use a sufficient, efficient workflow that reaches and establishes the right product with appropriate confidence. Avoid redundant, ceremonial, duplicative, or low-information work; do not omit materially useful design, testing, review, or validation merely because a shorter workflow exists.

## Typical workflows

Small/local executable work may look like:

```text
inspect -> implement -> affected regression -> integration -> done
```

Substantial work may look like:

```text
design -> staged implementation + useful intermediate regression -> final affected regression -> integration -> independent review
```

Production qualification is appended only when explicitly requested, required by project/release policy, or necessary to establish a material production-scale/resource/performance/hardware claim.

These are patterns, not fixed gate counts. Add or remove process steps according to engineering value, not minimum length.

## Workplans

Use a workplan when it materially reduces rediscovery, ambiguity, sequencing risk, cross-module drift, or downstream rework.

A useful substantial-work plan contains:

- objective and diagnosis;
- material engineering envelope;
- globally justified product design, ownership, and important complexity decisions;
- affected behavioral/regression surface;
- focused/new tests required for changed mechanisms;
- integration path(s) required for end-to-end functional acceptance;
- stage-local regression checks where they materially improve fault localization or risk control;
- production qualification requirement, deferral, or explicit non-requirement;
- implementation sequence where ordering matters;
- material risks/redesign triggers.

Do not make administrative provenance, evidence filenames, report schemas, or optional telemetry acceptance requirements unless the project independently needs them.

## Gates

Gates are optional but value-based. Use one when validating a boundary before proceeding materially reduces risk or wasted downstream work, such as architecture/algorithm decisions, irreversible migration, expensive execution prerequisites, scientific semantics, security boundaries, or fault-localization boundaries in substantial staged work.

Do not create G0/G1/G2 merely because a template can represent them. Do not remove a useful gate merely to make the process shorter.

## Functional acceptance

For executable changes, final acceptance requires affected-surface regression and integration testing. A production run, benchmark, or qualification result cannot substitute for missing regression coverage.

The affected surface extends beyond the diff when behavior can propagate through callers/consumers, shared utilities, interfaces, configuration/persistence/state/orchestration, packaging, or other transitive dependencies.

## External execution

A different machine, GPU, HPC allocation, production dataset, or external service does not automatically create a handoff or qualification role. Record reproducible commands and material conditions when external execution is required. Create dedicated runners when they materially reduce repeated work/error or are product functionality.

## Documentation and hygiene

Update affected durable documentation when accepted product behavior/architecture/contracts changed. Use `software-documentation` when substantive reconciliation or publication work is useful. Use `repository-hygiene` after substantial work only when a dedicated cleanup pass materially improves repository safety/clarity.

Neither specialist is a mandatory lifecycle gate.

## Review

Independent review is appropriate when change scope/risk warrants it. Review material functionality/correctness, scientific fidelity, scaling/resources/hardware/performance, product complexity and ownership, reuse/consolidation/deletion opportunities, affected regression coverage, integration results, unavailable checks, production-qualification boundaries, and unresolved material risks.

No separate verification report is required unless project/release/compliance policy independently requires one.
