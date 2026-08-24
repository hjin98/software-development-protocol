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

## Initially expected affected behavioral surface

<New/modified code plus existing callers/consumers/shared utilities/configuration/persistence/state/orchestration/interfaces/packaging/transitive behavior that could plausibly change. This is provisional and must be re-derived from the final assembled implementation.>

## Acceptance

- focused checks for new/modified mechanisms as applicable;
- relevant affected regression after each material behavior-changing implementation stage before dependent work proceeds;
- final reconciliation/re-derivation of the affected behavioral surface from the assembled implementation;
- final regression coverage across that complete surface;
- integration testing through the assembled affected product path and real relevant boundaries;
- repository/project-required checks; use the broader/full available suite if impact cannot be bounded confidently;
- material performance/resource/backend checks where required;
- production qualification: <required / deferred / unnecessary, with reason when materially relevant>.

## Implementation sequence

<List ordering that materially reduces risk, ambiguity, or rework. Identify the regression subset that closes each material behavior-changing stage. An atomic stage may share its final pass; a genuinely non-executable intermediate may validate at the nearest executable stage when that dependency is explicit.>

## Risks / redesign triggers

<Only material risks or evidence that should cause design reconsideration.>
