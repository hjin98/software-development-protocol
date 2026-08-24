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

## Affected behavioral surface

<New/modified code plus existing callers/consumers/shared utilities/configuration/persistence/state/orchestration/interfaces/packaging/transitive behavior that could plausibly change.>

## Acceptance

- focused checks for new/modified mechanisms as applicable;
- regression coverage across the complete affected behavioral surface;
- integration testing through the assembled affected product path and real relevant boundaries;
- material performance/resource/backend checks where required;
- production qualification: <required / deferred / unnecessary, with reason>.

## Implementation sequence

<List ordering that materially reduces risk, ambiguity, or rework. Identify useful intermediate regression points. Gates are value-based, not required or forbidden by process-length preference.>

## Risks / redesign triggers

<Only material risks or evidence that should cause design reconsideration.>
