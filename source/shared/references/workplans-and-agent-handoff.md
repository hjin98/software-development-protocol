# Workplans, Qualification, and Agent Roles

## Purpose

Protocol v3 separates four authority roles:

```text
software-design -> software-implementation -> software-qualification -> software-verification
```

The roles prevent silent redesign, invented PASS claims, and self-acceptance of substantial work. They are authority boundaries, not a requirement for four different people, agents, or documents.

## Materiality rule

A protocol condition may block acceptance only when violating it could materially change the code executed, material inputs/configuration/environment, observable correctness, scientific or numerical interpretation, security or recovery behavior, performance/resource claims, installability/shipped artifacts, or whether the candidate introduced a regression.

Everything else is advisory recordkeeping. Administrative or evidence-format defects may be corrected without product requalification when they do not change those material dimensions or the interpretation of an observed result.

Resource-bounded execution follows the same rule: hard safety containment may be mandatory, but optional telemetry, advisory resource estimates, evidence formatting, and secondary diagnostics do not become blocking merely because the harness can collect them.

## Proportional lifecycle

Use the lightest workflow that preserves the material authority boundaries.

### Small/local work

```text
inspect -> implement -> relevant checks -> review
```

### Substantial work

```text
design/workplan -> implementation -> required checks -> verification
```

### Cross-environment work

When qualification must move to a workstation, HPC system, production dataset, external service, or other distinct execution environment:

```text
design/workplan -> implementation -> qualification run card -> target execution/evidence -> verification
```

A separate Qualification Handoff is therefore conditional, not universal. For nontrivial external execution, prefer a standalone autonomous qualifier rather than an interactive agent-driven gate loop.

## Implementation Workplan

Use a workplan when design reasoning, cross-module change, public/persisted/scientific semantics, performance/resource targets, security/recovery behavior, or expensive execution would otherwise be rediscovered.

A substantial workplan records:

- objective and diagnosis;
- frozen product/domain design decisions;
- expected change surface and non-goals;
- material execution constraints;
- one authoritative **Acceptance-critical requirements** section;
- ordered gates where staging is useful;
- conditions that truly require `DESIGN_REVISION_REQUIRED`.

Acceptance-critical requirements should be written in product/domain language, not protocol-artifact language.

Good: `restart after a corrupt checkpoint produces the uninterrupted result`.

Bad: `the report contains the checkpoint-policy SHA`.

The workplan revision changes only when target design, acceptance semantics, important scope, or material qualification conditions change. Correcting a command, path, report field, log destination, safe benchmark size, or other non-semantic execution detail does not require a new revision.

## Gate state

Use the simple state set:

```text
PENDING
PREPARED
PASS
FAIL
BLOCKED
```

`PREPARED` means implementation is ready but a required execution check remains. Final acceptance belongs to verification and is one of:

```text
MERGE_READY
NOT_READY
DESIGN_REVISION_REQUIRED
```

Future-release obligations belong in a separate section rather than being encoded as blocking/nonblocking deferred-state machinery.

## Qualification run card

A run card is useful only when execution crosses a real boundary. It identifies:

- candidate Git commit or other materially sufficient source identity;
- governing workplan/task;
- checks to perform and their acceptance criteria;
- material dataset/config/backend/hardware conditions;
- product-defining things qualification must not change;
- required external inputs or permissions;
- for expensive checks, the safe adaptive execution strategy and whether full production scale is truly required.

It freezes intent and material conditions, not shell spelling or universal machine numbers. Equivalent environment activation, cwd, absolute paths, quoting, scratch directories, log destinations, and safe adaptive workload sizing are operational choices unless the workplan says they are material.

## Qualification correction authority

Qualification distinguishes three classes.

### Product/material failure

Examples: wrong result, numerical mismatch, candidate-caused regression, invalid recovery, package failure, excessive product memory under a properly designed representative measurement, or missed performance threshold.

Route to `RETURN_TO_IMPLEMENTATION`, or `DESIGN_REVISION_REQUIRED` if frozen target semantics must change.

### Environment/input blocker

A required GPU, dataset, service, compiler, credential, or target environment is unavailable, or the minimum materially sufficient check cannot run safely after allowed adaptation. Record `BLOCKED`.

### Harness/record defect

Examples: wrong cwd, bad quoting, intended config path expressed incorrectly, unwritable evidence directory, oversized qualification workload, report typo, stale administrative version label, missing optional telemetry, or missing advisory digest.

Correct, degrade, resize, record, or skip locally as appropriate and continue when candidate behavior and material test conditions remain unchanged. A hard containment event caused by the harness does not by itself fail the product.

No administrative, secondary diagnostic, or evidence-format defect may by itself require product requalification.

## Candidate source boundary

In a normal Git repository, the candidate Git commit plus absence of unintended product-defining working-tree changes is the default source identity.

Use additional hashes only at real content boundaries where Git does not sufficiently identify what is being accepted, such as external datasets, model weights, source archives, generated binaries, mutable production snapshots, or canonical-source/generated-artifact parity.

Qualification should not modify product source or other candidate-defining files while claiming to test that candidate. Evidence, build, log, benchmark, profile, and bounded scratch outputs are allowed unless a project says otherwise.

## Evidence and reruns

Record enough evidence to understand what was tested and what happened. Do not require provenance fields that cannot change interpretation of the result.

Rerun a check when something changed that could plausibly alter that check's result or interpretation. Unrelated administrative edits do not invalidate execution evidence.

For unusually expensive programs, a dependency map may help selective reuse, but it is optional optimization rather than default protocol ceremony.

A repeated attempt remains part of the same qualification while candidate behavior and material test conditions remain unchanged. Record material changes between attempts. No formal retry taxonomy is required.

## Role authority

| Domain | Design | Implementation | Qualification | Verification |
|---|---|---|---|---|
| Root cause / target architecture | owns | follows or escalates | execution-local diagnosis | reviews |
| Scientific/API/persistence/security semantics | owns target | implements | exercises | verifies |
| Acceptance-critical requirements | owns | consumes | executes | decides sufficiency |
| Local helpers/tests/harnesses | intent | owns | may repair/adapt non-material harness defects | reviews if consequential |
| Product source | no broad implementation | owns | read-only during candidate qualification | review-only |
| Final acceptance | no | no | no | owns |

## Design revision boundary

Use `DESIGN_REVISION_REQUIRED` only when proceeding requires materially changing frozen product/domain design, acceptance semantics, performance thresholds, public/persisted/scientific/security/recovery behavior, or a material scope boundary.

Do not use design revision for operational commands, metadata, evidence layout, report formatting, or safe adaptive execution mechanics that preserve the claim.

## Broad-suite policy

A full-suite zero-failure requirement is mandatory only when the repository actually maintains that suite as a green gate or project/release policy explicitly requires it. Otherwise run broad tests when useful, attribute failures, and block the candidate only for failures plausibly introduced by it or for explicitly mandatory globally-green policy.

Do not construct elaborate historical/counterfactual baselines solely to turn a repository with known unrelated failures into an artificial zero-failure oracle.

## Protocol growth rule

A proposed new blocking rule must state:

1. the concrete software failure it prevents;
2. why an existing simpler rule does not cover it;
3. why advisory treatment is insufficient;
4. why its burden is proportional to the risk.

If the main benefit is provenance completeness, observability completeness, or diagnostic convenience, the rule is advisory by default.
