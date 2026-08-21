# Workflow and Workplans

Protocol 5 deliberately keeps the software-development lifecycle small while requiring engineering decisions to account for the whole material problem.

## Roles

```text
software-design -> software-implementation
```

`software-design` owns substantial diagnosis/design, engineering-envelope definition, architecture/algorithm/resource decisions, complexity-regression review, and independent final review when materially useful. `software-implementation` owns code changes, refactoring, testing, benchmarking, target-environment validation, ordinary task cleanup, and completion evidence.

Testing is not a separate authority. Verification is review, not a separate workflow system.

Protocol 5.2 provides optional specialists rather than additional lifecycle roles:

- `software-documentation` — substantive documentation reconciliation, editorial refactoring, theory/method explanation, user-oriented synthesis, or derived-document publication;
- `repository-hygiene` — conservative repository cleanup after a development stage is formally closed or when explicitly requested: removal of proven disposable residue, archival of completed workplans, repair of clear hierarchy drift, and strictly guarded temporary-branch retirement.

Neither specialist approves code or becomes a required development gate. `repository-hygiene` must not interrupt active work merely to make the tree look tidy, and it must preserve useful/ambiguous material, unique work, protected branches, the default branch, and `main`.

### Permanent repository safety invariant

Across every role, specialist, development stage, cleanup pass, migration, and release operation, **never delete the branch named `main`**. Preserve the configured default branch as well unless an explicitly authorized default-branch migration has first established and verified its replacement; even such a migration does not authorize deleting `main`. Normal authorized commits, merges, and fast-forward updates to `main` are unaffected.

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

Before completion, ask one lightweight documentation-impact question:

> Did this accepted change materially alter a public capability, scientific interpretation, durable architecture, API/configuration contract, workflow, or existing explanation?

If not, no documentation stage is required. If yes, reconcile only the affected durable documentation. A trivial edit can remain part of implementation; use `software-documentation` when the change requires real synthesis, restructuring, theory explanation, or publication work. Do not make unrelated stale documents block a local product change.

After a substantial stage is formally closed, a dedicated hygiene pass is optional. Use `repository-hygiene` only when accumulated temporary diagnostics, completed workplans, generated scratch/test residue, stale temporary branches, or directory-tree drift create a real maintenance/safety burden. Ordinary cleanup remains part of implementation; do not invoke a repository-wide hygiene pass after every local change.

## Workplans

Use a workplan only when it prevents meaningful rediscovery or ambiguity: substantial architectural or algorithmic change, cross-module work, durable API/persistence/scientific semantics, expensive execution, migration, target-hardware work, or other material sequencing.

A useful workplan contains only:

- objective;
- diagnosis;
- material engineering envelope where relevant, including required functionality, invariants, scale, resources, hardware, and performance;
- proposed engineering-sufficient design and important ownership;
- significant justified complexity or specialization;
- acceptance requirements;
- implementation sequence when ordering matters;
- material risks/redesign triggers.

Do not make administrative provenance, evidence filenames, report schemas, or optional telemetry acceptance requirements.

Completed workplans may be moved from a repository's active location to its canonical archive only after their terminal state is genuinely accepted. A paused, blocked, deferred, or partially implemented plan remains active unless project policy says otherwise.

## Gates

Gates are optional. Use one when crossing it protects a real boundary, such as:

- architecture/algorithm approval before a broad rewrite;
- irreversible schema/data migration;
- expensive execution after prerequisites;
- target-hardware decision or deployment;
- scientific semantics requiring review.

Do not create G0/G1/G2/... merely because a template can represent them.

Documentation maintenance or repository hygiene is not by itself a reason to add a gate. Mechanical document checks may fail only on objective integrity problems in the affected document chain; semantic ambiguity should be routed to design/implementation rather than converted into brittle lint rules.

## External execution

A different machine, GPU, HPC allocation, production dataset, or external service does not automatically require a handoff artifact or qualification role.

Record the shortest reproducible command and material conditions. Create a dedicated runner only when automation independently reduces repeated work/error or is product functionality.

## Failure routing

Use one decision:

```text
failure
  -> find owning cause
  -> clean fix fits engineering requirements? yes: fix simply
                                         no: refactor/redesign owning mechanism
```

The redesign may target architecture, algorithmic scaling, data representation, resource use, hardware utilization, or accumulated structural complexity depending on the evidence.

Do not create formal retry/state taxonomies unless the product itself needs them.

## Review

Independent review is appropriate when the change is substantial or risk warrants it. Review material functionality/correctness, scientific fidelity, algorithmic scaling, resource and target-hardware behavior, end-to-end performance where material, architecture, complexity, reuse/consolidation opportunities, tests, cleanup opportunities, and whether any materially affected durable documentation now misrepresents the accepted system.

Scope complexity, documentation, and hygiene review proportionally. A small local change does not require repository-wide refactoring, a repository-wide documentation audit, or a repository-wide cleanup.

No separate verification report is required unless project/release/compliance policy independently requires one.
