---
kind: implementation-workplan
workplan_id: REPLACE_ME
protocol_version: 5.9.0
---

# <Task> Workplan

## Objective and protected concerns

<Concise stakeholder-relevant product outcome, durable-success criterion when material, evidence-grounded diagnosis/root cause, and the invariants/failure modes the implementation must preserve.>

## Engineering envelope and product design

<Material functionality/correctness/scientific/resource/scaling/hardware/performance/security/compatibility requirements, plus the globally justified ownership/algorithm/data/interface design and justified product complexity.>

## Implementation obligations

Record task-specific obligations, not generic protocol prose. An ordinary material obligation should preserve:

- **Concern / rationale:** why this obligation exists.
- **Required end state:** behavior, ownership, architecture, or observable result that must hold.
- **Required consequences / constraints:** concrete consequences already determined by design, including preservation or forbidden behavior.
- **Acceptance evidence:** focused/regression/integration, numerical/resource/compatibility threshold, structural/absence check, or other proof.

Attach only when material:

- **Suggested realization:** useful but replaceable by an equivalent realization preserving frozen semantics.
- **Acceptance boundary:** acceptance claim, required real semantic owner/path, allowed test doubles below/outside it, forbidden substitutions, and observable evidence when proxy acceptance is a material risk.
- **Stage/dependency:** when ordering materially reduces risk or rework.
- **Anti-shortcut / integrity constraint:** a known way local compliance or evidence manipulation could appear to pass while defeating the whole-product outcome.

Known material consequences must not disappear merely to shorten the plan. The accepted obligations are the minimum known contract, not a ceiling: implementation incorporates newly discovered necessary local or affected-surface consequences that preserve frozen design and reopens design only when a frozen material decision must change.

## Implementation authority

### Frozen

<Material requirements, invariants, non-goals, architecture/ownership/algorithm/resource/compatibility decisions, acceptance boundaries, and other accepted target decisions implementation must preserve.>

### Delegated

<Implementation-local mechanics intentionally left open where alternatives do not change frozen semantics.>

### Reopen only on evidence

<Material assumptions/decisions that may change only after a genuine redesign trigger. Reopen only the affected surface and preserve still-valid accepted work/evidence.>

## Affected surface and task-specific acceptance

<Initially expected changed/new behavior plus callers/consumers/shared utilities/configuration/persistence/state/orchestration/interfaces/packaging/documentation/transitive behavior that could plausibly change. This is provisional and must be re-derived from the final assembled implementation.>

Generic functional-acceptance requirements are inherited from the protocol version declared by `protocol_version`; later releases do not silently reinterpret this workplan. Record only task-specific mappings, thresholds, real-owner/test-double boundaries, repository-required checks, and structural/absence claims not already clear in the obligations.

Production qualification: <required / deferred / unnecessary, with reason when materially relevant>.

## Implementation sequence and redesign risks

<List only coherent behavior/risk stages where ordering materially reduces ambiguity or rework. A local coherent behavior change is normally one material stage; do not split tightly coupled helper/caller/test edits merely by file/function. Each executable material stage still closes semantic/conformance plus focused and affected-regression functional acceptance before dependent work proceeds.>

<Material risks or evidence that should cause bounded design reconsideration.>

## Handoff closure

Before accepting a substantial workplan, reconcile:

```text
explicit requirements + protected concerns + accepted design/invariants
+ preservation/non-goals + known cross-module consequences
-> implementation obligations -> acceptance evidence
```

Confirm that no material requirement, protected concern, frozen design decision, known consequence, or required acceptance claim was lost in compression. This is reasoning closure, not a mandatory persistent traceability artifact.
