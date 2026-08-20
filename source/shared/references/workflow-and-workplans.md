# Workflow and Workplans

Protocol 4 deliberately keeps the software-development lifecycle small.

## Roles

```text
software-design -> software-implementation
```

`software-design` owns substantial diagnosis/design and independent final review when materially useful. `software-implementation` owns code changes, refactoring, testing, target-environment validation, and completion evidence.

Testing is not a separate authority. Verification is review, not a separate workflow system.

## Default workflows

Small/local work:

```text
inspect -> implement -> relevant test -> done
```

Substantial work:

```text
design -> implement/refactor -> affected tests/real-use validation -> independent review
```

Use the shorter path unless the additional step protects a material risk.

## Workplans

Use a workplan only when it prevents meaningful rediscovery or ambiguity: substantial architectural change, cross-module work, durable API/persistence/scientific semantics, expensive execution, migration, or other material sequencing.

A useful workplan contains only:

- objective;
- diagnosis;
- proposed simplest sufficient design and important invariants;
- acceptance requirements;
- implementation sequence when ordering matters;
- material risks/redesign triggers.

Do not make administrative provenance, evidence filenames, report schemas, or optional telemetry acceptance requirements.

## Gates

Gates are optional. Use one when crossing it protects a real boundary, such as:

- architecture approval before a broad rewrite;
- irreversible schema/data migration;
- expensive execution after prerequisites;
- scientific semantics requiring review.

Do not create G0/G1/G2/... merely because a template can represent them.

## External execution

A different machine, GPU, HPC allocation, production dataset, or external service does not automatically require a handoff artifact or qualification role.

Record the shortest reproducible command and material conditions. Create a dedicated runner only when automation independently reduces repeated work/error or is product functionality.

## Failure routing

Use one decision:

```text
failure
  -> find owning cause
  -> clean fix fits existing design? yes: fix simply
                                  no: refactor/redesign owning mechanism
```

Do not create formal retry/state taxonomies unless the product itself needs them.

## Review

Independent review is appropriate when the change is substantial or risk warrants it. Review material correctness, architecture, complexity, tests, and cleanup opportunities.

No separate verification report is required unless project/release/compliance policy independently requires one.
