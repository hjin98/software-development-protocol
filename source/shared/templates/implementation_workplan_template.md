---
kind: implementation-workplan
workplan_id: REPLACE_ME
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
---

# <Task> Workplan

## Objective

<One concise product outcome.>

## Diagnosis and protected concerns

<Evidence-grounded root cause/current limitation plus the material invariants, failure modes, or engineering objectives the implementation must preserve.>

## Engineering envelope

<Material functionality/correctness/scientific/resource/scaling/hardware/performance/security/compatibility requirements that define an acceptable product.>

## Product design

<Globally justified engineering-sufficient design: ownership, algorithms/data representation, interfaces, target-scale behavior, and justified product complexity.>

## Implementation obligations

For each material obligation, preserve enough information to implement without reconstructing design intent. Use prose, bullets, or a table; IDs are optional. Include only fields that are material, but do not omit known consequences merely to shorten the plan.

For each obligation record, as applicable:

- **Protected concern / rationale:** root cause, invariant, failure mode, or engineering objective.
- **Required end state:** behavior/ownership/architecture/result that must hold.
- **Required constraints / preservation / forbidden behavior:** what must remain unchanged or must no longer exist.
- **Expected owning/affected surface:** components, consumers, persistence/configuration/tests/docs/packaging/transitive behavior when known usefully.
- **Required implementation consequences:** concrete consequences already determined by the accepted design.
- **Suggested realization:** useful recommendation that may be replaced by an equivalent local realization preserving frozen semantics.
- **Acceptance evidence:** focused/regression/integration, numerical/resource/compatibility threshold, structural/absence check, or other proof.
- **Acceptance boundary, when material:** acceptance claim; required real owner/path; allowed test doubles below/outside that owner; forbidden substitutions; and observable evidence. Do not require this ceremony for ordinary unit tests where no material real-owner boundary is at risk.
- **Stage/dependency:** when ordering materially reduces risk or rework.

The obligations are the minimum known contract, not a ceiling: implementation must incorporate newly discovered necessary local or affected-surface consequences that preserve frozen design, and reopen design only when a frozen material decision must change.

## Implementation authority

### Frozen

<Material requirements, invariants, non-goals, architecture/ownership/algorithm/resource/compatibility decisions, and other accepted target decisions implementation must preserve.>

### Delegated

<Implementation-local mechanics intentionally left open where alternative realizations do not change frozen semantics.>

### Reopen only on evidence

<Explicit redesign triggers or assumptions whose invalidation requires material design reconsideration. Reopen only the affected design surface and preserve still-valid accepted work/evidence.>

## Initially expected affected behavioral surface

<New/modified code plus existing callers/consumers/shared utilities/configuration/persistence/state/orchestration/interfaces/packaging/documentation/transitive behavior that could plausibly change. This is provisional and must be re-derived from the final assembled implementation.>

## Task-specific acceptance

Generic functional-acceptance requirements are inherited from the protocol version declared `protocol_version`; later protocol releases do not silently change this workplan's meaning.

<Record only task-specific acceptance mappings or thresholds not already clear in the implementation obligations, including material real-owner/test-double boundaries, repository-required checks, structural/absence claims, and material benchmark/backend requirements. A material owner claim must not be accepted through a mock/bypass that could remain green while that owner is broken. Green runtime tests alone do not prove removal/uniqueness claims that require source/structural evidence.>

Production qualification: <required / deferred / unnecessary, with reason when materially relevant>.

## Implementation sequence

<List coherent behavior/risk stages where ordering materially reduces ambiguity or rework. A material stage closes only after both semantic/conformance closure of its assigned obligations and the protocol-required focused + affected-regression functional closure. Do not create stages for individual helper/file edits without an independent behavior/risk boundary.>

## Design handoff closure

Before accepting this substantial workplan, reconcile:

`explicit requirements + protected concerns + accepted design/invariants + preservation/non-goals + known cross-module consequences -> implementation obligations -> acceptance evidence`.

<Confirm that no material requirement or known design consequence was lost in translation. This is a reasoning closure, not a required persistent traceability artifact.>

## Risks / redesign triggers

<Only material risks or evidence that should cause design reconsideration.>
