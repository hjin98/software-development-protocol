---
kind: workplan-authority
workplan_id: PROTOCOL-5.12-CONVERGENT-DEVELOPMENT
parent_workplan: ../PROTOCOL-5.12-CONVERGENT-DEVELOPMENT.md
protocol_version: 5.11.0
target_protocol_version: 5.12.0
status: frozen
reviewed_date: 2026-09-03
frozen_date: 2026-09-03
review_base_commit: 34d618fc519224ba6d2005a4589436436a6d652a
---

# Protocol 5.12 Convergent Development — Frozen Authority

## Authority composition

The accepted Design -> Implementation authority for Protocol 5.12 is the supplied current artifact set:

1. `workplans/active/PROTOCOL-5.12-CONVERGENT-DEVELOPMENT.md`; and
2. this `AUTHORITY.md` closure review.

The parent workplan remains the substantive implementation contract. This authority closes its requested final Design review, resolves the remaining convergence-mechanics gaps below, and freezes the combined artifact set for implementation. Where this authority is more specific than the draft parent, this authority controls. The parent's `status: active`, its statement that another closure review is pending, and its `Design-review challenges for the next pass` are superseded by this frozen authority.

This deliberately does **not** create a numbered review-revision series. The closure changes the accepted task contract once before implementation; ordinary later implementation misses must not mechanically mint new authority revisions. Git history provides provenance for this closure.

## Closure verdict

**PASS — freeze for implementation after the corrections in this authority.**

The parent design is sound: it preserves Protocol 5.4-5.11 doctrine while adding an explicit convergence mode switch, family-level closure, review readiness, revision economy, finite-surface reasoning, acceptance liveness, and bounded redesign/consolidation. The final review found five mechanics that required tightening before freeze:

1. a weak or incorrectly scoped Mode F claim could otherwise trigger premature redesign;
2. a defect family could otherwise be defined artificially narrowly or broadly;
3. independent review grouping did not yet require proportionate same-pass blocker-family saturation;
4. revision economy did not yet distinguish numbered revision churn from required reconciliation of genuinely new binding task semantics into current authority; and
5. review-readiness language needed an explicit non-refusal/stopping rule so it reduces wasted closure cycles without becoming a gate that prevents requested review or encourages endless searching.

The corrections below are frozen target semantics for Protocol 5.12 implementation.

## A. Family identity must be semantic and resistant to fragmentation or over-aggregation

The parent workplan's family concept is retained and tightened.

A **material defect/invariant family** is the smallest useful semantic set whose members share enough of the following that one owner-level or mechanism-level closure can reasonably govern them:

```text
protected invariant / required product claim
+ semantic owner or authority class
+ state / transition / lifecycle class
+ materially equivalent failure mechanism or forbidden realization
```

Family membership is **not** established by textual similarity alone. Conversely, separate files, helpers, callers, command names, exception branches, or test modules do not make defects independent when they exercise the same authority/invariant through materially equivalent semantics.

### Anti-fragmentation rule

After recurrence, an actor may not avoid Mode F or Mode R by renaming each sibling manifestation as a separate local bug merely because it occurs at a different source site. If omission of another such site could violate the same product claim for the same semantic reason, it belongs in the family unless evidence establishes a materially distinct owner, lifecycle, invariant, or failure mechanism.

### Anti-overaggregation rule

Do not define families as broad labels such as `storage bugs`, `scheduler bugs`, `security issues`, or `performance problems` when the members do not share a closure mechanism or semantic authority. Over-broad grouping that forces unrelated repairs, tests, or redesign is also nonconformant.

### Family boundary evidence

When Mode F is active, the closure basis must state enough to make the family boundary reviewable:

- governing invariant/product claim;
- semantic owner or authority class;
- material transition/lifecycle/failure classes included;
- known materially distinct exclusions and why they are independent;
- discovered member sites or equivalence classes and their disposition;
- completeness basis and its limitations.

The representation remains flexible. No universal persistent matrix is required.

## B. Distinguish incomplete Mode F from a genuine post-family recurrence

The parent workplan's Mode N -> Mode F -> Mode R ladder remains frozen, with the following qualification.

### A genuine Mode F closure

A prior Mode F cycle counts as a **genuine family-closure attempt** for purposes of triggering Mode R only when, on the then-current candidate:

1. the family was materially defined rather than merely named;
2. an adequate bounded closure basis was actually established;
3. discovered members/equivalence classes were dispositioned rather than silently omitted;
4. the chosen canonical enforcement/ownership realization, including any justified specialization, was implemented;
5. required focused, family-level affected regression, real-owner/integration, and structural/absence evidence actually executed as applicable; and
6. the family was explicitly claimed closed on that evidence.

A label such as `Mode F complete`, a partial caller search, a vacuous structural scan, missing real-owner evidence, or an incorrectly narrow family boundary is **not** enough to create a post-family redesign trigger.

### Incomplete or invalid Mode F

If independent review finds that the previous claimed family closure lacked a materially adequate closure basis or acceptance, route that finding as **incomplete Mode F / implementation nonconformance** and complete or correct the family closure under the existing accepted design unless separate redesign evidence already exists.

This prevents a low-quality family-closure attempt from unnecessarily forcing architecture churn.

### Genuine post-family recurrence

If a material same-family blocker survives or reappears **despite a genuine Mode F closure as defined above**, or the Mode F census itself proves duplicated/contradictory ownership, uncontrolled entry points, proliferating exceptional paths, or another existing structural redesign trigger, Software Design must perform bounded structural/ownership reconsideration before another ordinary family patch cycle.

The actor may not simply apply `one more sibling fix` and repeat Mode F without explaining evidence that the new issue is materially outside the previously closed family.

### Mode R does not automatically mean a normative design change

Mode R is a mandatory **Design reconsideration boundary**, not a pre-decided architecture rewrite.

Design may conclude either:

- a frozen product/architecture/ownership decision truly must change -> reconcile the affected workplan/design authority; or
- the frozen product design remains sound, but implementation must perform a stronger consolidation/refactor/canonicalization under the same authority -> return a bounded implementation correction without inventing a normative design revision.

This distinction preserves the existing Protocol 5 boundary between material redesign and implementation-local refactoring while still preventing endless local patch loops.

## C. Independent review must saturate an implicated blocker family proportionately

The parent workplan's grouping/delta-review rules are strengthened with **blocker-family saturation**.

When independent review identifies a genuine blocker and evidence indicates a material family, the reviewer should not stop immediately at the first sufficient NO-PASS example when additional same-family discovery is cheap and high-information.

Before routing the family back to Implementation, the reviewer must, to the degree proportionate and practical in the current review:

1. identify the governing invariant/owner/failure family;
2. continue bounded read-only inspection of the directly implicated family far enough to find obvious sibling variants/equivalence classes and expose whether the problem is isolated or systemic;
3. group concrete same-family findings into one family-level closure problem rather than serial micro-findings; and
4. state whether the review's sibling search is believed saturated for the inspected family or whether exhaustive family closure remains Implementation's Mode F responsibility.

### Saturation stopping rule

Reviewer saturation is **not** a second implementation census and is not whole-repository exhaustiveness. The reviewer may stop expanding the family search when one of these is true:

- the materially plausible low-cost sibling space reachable from the current evidence has been examined sufficiently to characterize the family;
- additional discovery would require substantial implementation-like reconstruction, expensive execution, unavailable tooling/environment, or broad speculative search with low expected information gain;
- the evidence already establishes that Mode F must perform the systematic census and further reviewer enumeration would mainly duplicate that work; or
- no evidence-driven ownership/contract/affected-surface chain justifies broader inspection.

When stopping short of saturation, say so; do not imply exhaustive closure.

This rule reduces `review -> one site -> patch -> review -> next sibling` churn while preserving a clean responsibility boundary: **Review characterizes and batches the blocker family; Implementation owns family closure.**

### Independent-review sufficiency

Independent review is not required to prove the absence of every conceivable repository defect. A closure review may PASS when:

- accepted-contract conformance is closed;
- affected-surface evidence is adequate;
- triggered family closure bases have been challenged at the material boundaries;
- the independent engineering challenge has inspected material risk surfaces to evidence-directed sufficiency; and
- no unresolved material blocker or evidence-driven reason to expand remains.

Genuine later-discovered defects remain real defects; this stopping rule simply prevents `search forever` from becoming the definition of rigor.

## D. Review readiness is a final-closure quality boundary, not a refusal mechanism

The parent workplan's review-readiness requirements remain frozen with these clarifications.

1. **Review readiness applies to the normal final independent closure review.** Earlier Design consultation, bounded architecture checkpoints, Mode R reconsideration, or high-risk pre-acceptance review may occur before the final full acceptance pass when doing so materially reduces rework.
2. **A user-requested review must not be refused merely because the candidate is not review-ready.** Perform the requested review to the highest useful depth available. Missing required implementation closure/evidence is itself a finding and routes as not-review-ready/implementation nonconformance unless it exposes a genuine design deficiency.
3. **Do not manufacture a design revision for missing evidence.** Lack of required regression/integration/structural evidence under unchanged authority remains an implementation closure failure.
4. **Do not spend expensive final-suite cost before a known high-risk structural question that Design must resolve.** Use the existing value-based gate doctrine: a bounded Design checkpoint may precede expensive final acceptance if it materially reduces likely invalid reruns. Once the candidate claims final implementation closure, all protocol-required final acceptance must still run on a candidate whose relevant dimensions have not changed afterward.

This preserves both review independence and development economy.

## E. Revision economy must preserve snapshot-complete current authority

The parent workplan correctly separates **implementation attempts/review cycles** from **normative authority evolution**. The following distinction is frozen to remove the remaining ambiguity.

### No numbered revision for ordinary implementation nonconformance

Do not create a new numbered authority revision solely because:

- an existing obligation was missed;
- a sibling source site violates an already-explicit invariant;
- a required check was absent or failed;
- another implementation patch is needed; or
- a reviewer provides additional evidence/examples without changing binding task semantics.

### Reconcile genuinely new binding semantics before the next handoff

If review discovers a **genuinely new still-binding task-specific requirement, required consequence, acceptance boundary, redesign trigger, or other semantic constraint that is not recoverable from the supplied current authority**, it must be reconciled into the canonical current authority before a subsequent Design -> Implementation handoff. Snapshot completeness still applies.

This reconciliation need not mint a numbered `AUTHORITY_REVISION_N` artifact. A canonical current-plan/authority edit, recorded by ordinary version control, is sufficient unless project policy independently requires immutable revision snapshots.

### Concrete evidence is not automatically new normative semantics

Newly discovered concrete sites, examples, call stacks, failing inputs, or sibling manifestations do not require workplan semantic expansion when the existing invariant/owner obligation already governs them strongly enough for a new implementer to recover the required end state. They belong in the implementation/review closure evidence and family census.

If, however, the new evidence reveals a previously unstated material consequence or acceptance boundary that a new implementer could not reliably infer from the supplied authority, reconcile that consequence into current authority before handoff.

Thus Protocol 5.12 distinguishes:

```text
implementation evidence / missed instance
    -> same current authority; no numbered revision

new still-binding task semantic needed for lossless handoff
    -> reconcile canonical current authority
    -> numbered historical snapshot only if independently useful/required

frozen target decision must change
    -> bounded Design reopen + current-authority reconciliation
```

## F. Required implementation-obligation amendments

The parent obligations O1-O12 remain binding. Implementation must incorporate the following additions when satisfying them.

### O1 — workflow/workplans

In addition to the parent O1 requirements, canonical workflow guidance must:

- define anti-fragmentation and anti-overaggregation family semantics;
- distinguish incomplete Mode F from genuine post-family recurrence;
- define Mode R as mandatory Design reconsideration that may result either in bounded redesign or same-design structural refactor;
- define review-saturation and review-sufficiency stopping semantics;
- distinguish canonical-authority reconciliation from numbered revision churn; and
- state that requested review is not refused merely because final review-readiness prerequisites are missing.

### O2 — architecture/design

Architecture guidance must make clear that post-genuine-Mode-F recurrence triggers Design reconsideration, but a normative architecture/workplan change is required only if a frozen material target decision must change. A mandatory implementation consolidation/refactor under unchanged frozen semantics is a valid Mode R outcome.

### O4 — Software Implementation

Implementation guidance must:

- prevent family fragmentation by file/helper/caller labels;
- require an adequate closure basis before claiming Mode F closed;
- disposition discovered family members/equivalence classes;
- treat review evidence showing an inadequate previous Mode F as a requirement to complete/correct Mode F rather than automatically assuming redesign; and
- after a genuine post-family recurrence, stop ordinary patching and route to Design reconsideration.

### O5 — Software Design

Independent-review guidance must:

- apply proportionate blocker-family saturation before returning a family-level NO-PASS when cheap/high-information sibling inspection remains;
- distinguish reviewer characterization/saturation from Implementation's systematic family closure;
- explicitly distinguish incomplete Mode F from genuine post-family recurrence;
- preserve a stopping rule based on evidence-directed sufficiency rather than exhaustive defect absence;
- honor user-requested review even when review-readiness is deficient; and
- classify Mode R outcome as either bounded design change or same-design mandatory implementation consolidation/refactor.

### O8 — workplan template

Conditional recurrence guidance should encourage a task-specific family boundary or owner/invariant key when ambiguity would plausibly permit fragmentation. Do not require this for ordinary local plans.

### O10 — protocol regression tests

The parent O10 list is extended. Regression protection must also establish that:

23. family identity cannot be satisfied merely by textual/source-file grouping and cannot be broadened into unrelated subsystem-wide work;
24. an invalid/incomplete Mode F claim does **not** automatically trigger redesign; it remains family-closure nonconformance unless independent redesign evidence exists;
25. a genuine same-family recurrence after adequate Mode F closure does trigger Design reconsideration;
26. Mode R Design reconsideration does not automatically require a normative workplan revision when frozen target semantics remain valid and a structural implementation refactor can close the family;
27. independent review should batch/saturate an implicated blocker family proportionately rather than intentionally stopping at the first cheap sibling example;
28. review saturation remains bounded and does not become universal repository exhaustiveness;
29. review readiness cannot be used to refuse an explicitly requested review;
30. review has an evidence-directed sufficiency/stopping rule and is not defined as proof of zero conceivable defects;
31. ordinary implementation misses do not create numbered authority revisions;
32. genuinely new still-binding task semantics are nevertheless reconciled into canonical current authority before the next handoff when snapshot completeness requires it; and
33. concrete sibling evidence already governed by an explicit invariant need not be promoted into new normative semantics merely to preserve provenance.

Tests should protect the semantic distinctions, not require the exact N/F/R labels or this authority file's prose.

## G. Resolution of the parent workplan's final review challenges

The nine challenges listed in the parent draft are closed as follows.

1. **First recurrence threshold:** accepted. It is early enough because it activates only on material same-family evidence; anti-overaggregation prevents unrelated local defects from escalating together.
2. **Post-family recurrence:** accepted with the genuine-Mode-F qualification above. Invalid family closure is completed; recurrence after adequate closure triggers Design reconsideration.
3. **Family precision:** closed by the semantic family key plus anti-fragmentation/anti-overaggregation rules and reviewable boundary evidence.
4. **Review readiness:** accepted with the final-closure/non-refusal clarification. No new report artifact or lifecycle gate is introduced.
5. **Revision economy versus snapshot completeness:** closed by separating numbered revision churn from canonical current-authority reconciliation.
6. **Closure horizon:** accepted unchanged. It focuses causal/contract scope but expands whenever evidence establishes an affected chain.
7. **Acceptance liveness:** accepted unchanged. It remains materiality/practicality-bounded and does not require universal historical mutation testing or one-test-per-site acceptance.
8. **Effective compression/canonical ownership:** accepted. Workflow/workplans remains the canonical mechanics owner; role entrypoints receive only high-salience decision rules and routes.
9. **Testability/preservation:** accepted after extending O10 with the negative/counterfactual distinctions above.

## Frozen implementation authority

The parent's `Implementation authority` section remains binding, with these additions to **Frozen**:

- semantic family identity must resist both fragmentation and unrelated overaggregation;
- only a materially adequate Mode F closure can create the genuine post-family recurrence trigger;
- incomplete Mode F is implementation nonconformance, not automatic redesign;
- genuine post-family recurrence requires Design reconsideration before another ordinary same-family patch cycle;
- Design reconsideration may preserve frozen target semantics and mandate structural implementation consolidation without a normative authority revision;
- independent review performs proportionate same-family blocker saturation when doing so is cheap and high-information;
- independent review has an evidence-directed sufficiency stopping rule and is not whole-repository proof of defect absence;
- final review-readiness may not be used to refuse a user-requested review;
- implementation-attempt/review churn does not create numbered authority revisions;
- genuinely new binding task semantics must still be reconciled into canonical current authority before handoff when snapshot completeness requires it.

The parent's delegated choices remain delegated unless contradicted above.

## Final handoff closure

The frozen artifact set now closes the full reasoning chain:

```text
repeated sibling-defect churn
+ strong existing Protocol 5 product/review/testing doctrine
+ need to preserve ordinary local-work proportionality
-> explicit recurrence mode switch
-> semantic family identity resistant to gaming
-> bounded family census and canonical owner repair
-> acceptance liveness and final review readiness
-> distinguish incomplete family closure from genuine structural recurrence
-> mandatory Design reconsideration after genuine post-family recurrence
-> proportionate same-pass reviewer family saturation
-> evidence-directed review stopping rule
-> revision-number economy with snapshot-complete current-authority reconciliation
-> delta/evidence/test reuse and coherent test-cost ordering
-> preserved independent review, affected regression/integration, truthful non-closure,
   two-role lifecycle, minimum product complexity, and tool optionality
```

Apply the snapshot-loss counterfactual to the **parent workplan plus this authority file plus current Protocol 5.11 source authorities**. No Protocol 5.12 target decision in this frozen handoff depends on the prior conversation or mdstats history. The mdstats history remains motivating evidence only.

No material design question remains open for implementation. Protocol 5.12 is **frozen and ready for gated implementation** under this authority set.