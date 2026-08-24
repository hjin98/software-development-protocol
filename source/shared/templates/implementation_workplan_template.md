---
kind: implementation-workplan
workplan_id: REPLACE_ME
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
---

# <Task> Workplan

## Objective

<One concise product outcome.>

## Diagnosis

<Evidence-grounded root cause/current limitation.>

## Engineering envelope

<Material functionality/correctness/scientific/resource/scaling/hardware/performance/security/compatibility requirements that define an acceptable product.>

## Product design

<Globally justified engineering-sufficient design: ownership, algorithms/data representation, interfaces, target-scale behavior, and justified product complexity. Simplicity applies to the engineered product, not to minimizing the development-process step count.>

## Implementation authority

### Frozen

<Material requirements, invariants, non-goals, architecture/ownership/algorithm/resource/compatibility decisions, and other accepted target decisions implementation must preserve.>

### Delegated

<Implementation-local mechanics intentionally left open where alternative realizations do not change frozen semantics.>

### Reopen only on evidence

<Explicit redesign triggers or assumptions whose invalidation requires material design reconsideration. Reopen only the affected design surface and preserve still-valid accepted work/evidence.>

## Initially expected affected behavioral surface

<New/modified code plus existing callers/consumers/shared utilities/configuration/persistence/state/orchestration/interfaces/packaging/transitive behavior that could plausibly change. This is provisional and must be re-derived from the final assembled implementation.>

## Task-specific acceptance

Generic functional-acceptance requirements are inherited from the protocol version declared in `protocol_version`; later protocol releases do not silently change this workplan's meaning.

<Record only task-specific obligations or useful concrete mappings, such as focused/new tests, stage-specific affected regression subsets, real integration boundaries, numerical/security/resource/compatibility thresholds, repository-required checks, and material benchmark/backend requirements. Do not repeat generic protocol prose merely for completeness.>

Production qualification: <required / deferred / unnecessary, with reason when materially relevant>.

## Implementation sequence

<List ordering that materially reduces risk, ambiguity, or rework. Identify coherent material behavior-changing stages and the affected regression subset that closes each stage. An atomic stage may share its final pass; a genuinely non-executable intermediate may validate at the nearest executable stage when that dependency is explicit.>

## Risks / redesign triggers

<Only material risks or evidence that should cause design reconsideration.>
