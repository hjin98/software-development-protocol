---
kind: workplan-authority
workplan_id: PROTOCOL-5.12-CONVERGENT-DEVELOPMENT
parent_workplan: ../PROTOCOL-5.12-CONVERGENT-DEVELOPMENT.md
protocol_version: 5.11.0
target_protocol_version: 5.12.0
status: active
reviewed_date: 2026-09-03
reviewed_candidate: 9a47e492534ba990acbc03ec6dab62de3fe8178a
review_verdict: no-pass
---

# Protocol 5.12 Convergent Development — Current Authority

## Authority composition and current state

The current Design -> Implementation authority is the supplied set:

1. `workplans/active/PROTOCOL-5.12-CONVERGENT-DEVELOPMENT.md`; and
2. this `AUTHORITY.md`.

The parent workplan remains the substantive Protocol 5.12 implementation contract. This authority carries the final pre-implementation Design refinements and the current independent implementation-review result. Where this authority is more specific, it controls.

The Protocol 5.12 **product/design target remains frozen and sound**. The current implementation candidate is **NO-PASS** because its new semantic regression layer does not yet establish the required convergence-policy distinctions robustly. This is implementation nonconformance under already-binding O10 acceptance semantics, not a new product-design deficiency and not a Mode R architecture reopen.

Do not create a numbered review-revision series for this rework. Git history provides provenance. The current authority is updated in place because the still-binding task state must remain snapshot-complete for the next handoff.

## Frozen Protocol 5.12 convergence semantics

### A. Semantic defect-family identity

A material defect/invariant family is the smallest useful semantic set whose members share enough of:

```text
protected invariant / required product claim
+ semantic owner or authority class
+ state / transition / lifecycle class
+ materially equivalent failure mechanism or forbidden realization
```

Family membership is not established by textual/source-file similarity alone. Separate files, helpers, callers, commands, exception branches, or tests do not make defects independent when they exercise the same authority/invariant through materially equivalent semantics.

Conversely, broad labels such as `storage bugs`, `scheduler bugs`, `security issues`, or `performance problems` are not valid families when their members lack a shared closure mechanism or semantic authority.

After recurrence, actors may not fragment one family into source-local bug names to avoid family closure or Design reconsideration, and may not overaggregate unrelated defects to force broader work.

When family closure is active, the closure basis must make the boundary reviewable by stating, as applicable:

- governing invariant/product claim;
- semantic owner or authority class;
- included material transition/lifecycle/failure classes;
- known materially distinct exclusions and why they are independent;
- discovered member sites/equivalence classes and their disposition; and
- completeness basis plus material limitations.

No universal persistent matrix is required.

### B. Incomplete family closure versus genuine post-family recurrence

A prior family-closure cycle counts as a **genuine family closure** for later escalation only when, on the then-current candidate:

1. the family was materially defined rather than merely named;
2. an adequate bounded closure basis was established;
3. discovered members/equivalence classes were dispositioned;
4. the canonical enforcement/ownership realization, including justified specialization, was implemented;
5. required focused, family-level affected regression, real-owner/integration, and structural/absence evidence actually executed as applicable; and
6. the family was explicitly claimed closed on that evidence.

A label such as `Mode F complete`, a partial caller search, a vacuous scan, missing real-owner evidence, or an artificially narrow family is not a genuine family closure.

If review finds the prior family closure incomplete, narrow, or vacuous, route it as **implementation nonconformance** and complete/correct family closure under the accepted design unless separate redesign evidence exists.

If a material same-family blocker survives or reappears despite a genuine family closure, or the family census itself establishes duplicated/contradictory ownership, uncontrolled entry points, proliferating exceptional paths, or another structural redesign trigger, Software Design must perform bounded ownership/architecture reconsideration before another ordinary same-family patch cycle.

Mode R is a mandatory **Design reconsideration boundary**, not a predetermined architecture rewrite. Design may either:

- change a frozen material target decision and reconcile current authority; or
- preserve frozen product/design semantics and require stronger implementation consolidation/refactor/canonicalization under the same authority.

No recurrence count, review count, cycle budget, or convergence target can force acceptance.

### C. Independent-review family saturation and stopping

When review finds a genuine blocker in an identifiable material family, the reviewer must, to the degree proportionate and practical, continue cheap/high-information read-only inspection far enough to characterize obvious sibling variants/equivalence classes rather than intentionally returning one cheap sibling per review cycle.

Review must:

1. identify the governing invariant/owner/failure family;
2. characterize the directly implicated sibling space enough to distinguish isolated from systemic behavior;
3. group concrete same-family findings into one family-level closure problem; and
4. state whether reviewer sibling discovery appears saturated or whether systematic family closure remains Implementation's responsibility.

Reviewer saturation is not a second implementation census and not whole-repository exhaustiveness. Expansion may stop when the plausible low-cost sibling space is sufficiently characterized, further work would become implementation-like or expensive/unavailable, additional enumeration would mainly duplicate the required family census, or no evidence-driven ownership/contract/affected chain justifies broader search.

A closure review may PASS when accepted-contract conformance is closed, affected-surface evidence is adequate, material family-closure premises have been challenged, material engineering risk surfaces have been inspected to evidence-directed sufficiency, and no unresolved blocker or evidence-driven reason to expand remains. Review is not proof that no conceivable defect exists.

### D. Review readiness is not a refusal mechanism

Normal final independent closure review should receive a review-ready exact candidate. Earlier Design consultation, high-risk checkpoints, or Mode R reconsideration may occur before final acceptance when they materially reduce rework.

A user-requested review must not be refused merely because the candidate is not review-ready. Missing mandatory regression/integration/structural/liveness evidence is itself an implementation finding under unchanged authority unless it exposes a genuine design deficiency.

Missing evidence does not manufacture a design revision. Expensive final-suite work may be deferred while a known high-risk Design question is unresolved, but final claimed implementation closure still requires all protocol-required acceptance on a candidate whose relevant dimensions have not subsequently changed.

### E. Revision economy and snapshot-complete authority

Do not create a numbered authority revision solely because an existing obligation was missed, another sibling site violates an already-explicit invariant, a required check was absent/failed, another implementation patch is required, generated derivatives need regeneration, or review supplies more concrete evidence without changing binding task semantics.

If review discovers a genuinely new still-binding task-specific requirement, consequence, acceptance boundary, redesign trigger, or other semantic constraint not recoverable from the supplied current authority, reconcile it into canonical current authority before the next Design -> Implementation handoff.

New concrete sites, examples, call stacks, failing inputs, or sibling manifestations are evidence rather than new normative semantics when current supplied invariant/owner authority already governs them strongly enough for a new implementer to recover the required end state.

Thus:

```text
implementation evidence / missed instance
    -> same current authority; no numbered revision

new still-binding task semantic needed for lossless handoff
    -> reconcile canonical current authority

frozen target decision must change
    -> bounded Design reopen + current-authority reconciliation
```

## Binding implementation obligations retained from the frozen Design closure

The parent O1-O12 obligations remain binding. In particular:

- **O1 workflow/workplans:** canonical convergence mechanics must include anti-fragmentation/anti-overaggregation, genuine versus incomplete family closure, Design reconsideration outcomes, reviewer saturation/stopping, non-refusal review readiness, and revision economy with snapshot completeness.
- **O2 architecture/design:** genuine post-family recurrence requires Design reconsideration; same-design structural refactor/consolidation is a valid outcome when frozen target semantics remain sound.
- **O3 testing/validation:** acceptance liveness must protect real-owner and seam/failpoint/callback claims; structural evidence complements rather than replaces runtime acceptance.
- **O4 Software Implementation:** recurring families must be closed systematically, discovered members/equivalence classes dispositioned, and genuine post-family recurrence routed to Design instead of another ordinary patch.
- **O5 Software Design:** blockers must be grouped by semantic family, implicated families proportionately saturated, incomplete family closure distinguished from genuine post-family recurrence, and review stopped by evidence-directed sufficiency rather than exhaustive-defect proof.
- **O6 repository intake:** progressive intake remains default; bounded census is used only when recurrence or the product claim makes completeness material.
- **O7 tool-assisted engineering:** Serena/Semgrep/Hypothesis and equivalent tools remain optional instruments; their absence does not relax the claim and their presence does not make a three-tool pipeline or whole-repository scan mandatory.
- **O8 workplan template:** convergence guidance remains conditional and nonbureaucratic.
- **O9 version/release:** Protocol 5.12 remains a backward-compatible minor refinement; older workplans retain declared-version meaning unless explicitly reconciled/upgraded.
- **O10 regression:** the 33 convergence/preservation semantics below must be protected by durable semantic tests rather than brittle prose-presence checks where policy direction matters.
- **O11 distributions:** canonical source must build into valid shipped bundles with source-to-`dist` parity.
- **O12 preservation:** Protocol 5.4-5.11 behavior remains protected by regression except for intentional version/summary updates.

### O10 semantic regression set

Regression protection must establish:

1. exact Protocol 5.12 version identity;
2. unchanged two-role lifecycle;
3. unchanged engineering hierarchy;
4. a first clean local defect remains eligible for local owning-layer repair;
5. material sibling recurrence after claimed closure triggers family closure;
6. genuine same-family recurrence after adequate family closure triggers bounded Design reconsideration;
7. family census is bounded/conditional rather than universal repository exhaustiveness;
8. temporary closure maps are conditional and not mandatory persistent artifacts;
9. review readiness includes exact candidate identity, contract reconciliation, final affected regression/integration, and required evidence;
10. missing required evidence is implementation nonconformance/not-review-ready rather than an automatic design revision;
11. implementation nonconformance alone does not require a new authority revision;
12. genuinely new binding task semantics still require current-authority reconciliation/snapshot completeness;
13. independent review remains broad and may surface material new engineering issues;
14. closure horizon is not a scope ceiling;
15. unrelated pre-existing issues are not automatically current blockers;
16. acceptance liveness protects real-owner/seam/failpoint/callback claims;
17. structural/static scans complement and do not replace executable acceptance;
18. Serena/Semgrep/Hypothesis remain optional;
19. stage-local and final affected-surface regression/integration remain mandatory;
20. production qualification remains separate;
21. evidence reuse, context economy, and coherent stage granularity remain intact;
22. no fixed review/cycle count can force acceptance;
23. family identity cannot be satisfied by textual/source-file grouping and cannot be broadened into unrelated subsystem-wide work;
24. invalid/incomplete family closure does not automatically trigger redesign absent independent redesign evidence;
25. genuine same-family recurrence after adequate family closure does trigger Design reconsideration;
26. Mode R does not automatically require a normative authority revision when frozen semantics remain valid and a structural implementation refactor can close the family;
27. independent review proportionately batches/saturates an implicated blocker family instead of intentionally stopping at the first cheap sibling example;
28. reviewer saturation remains bounded and does not become universal repository exhaustiveness;
29. review readiness cannot be used to refuse an explicitly requested review;
30. review uses an evidence-directed sufficiency/stopping rule rather than proof of zero conceivable defects;
31. ordinary implementation misses do not create numbered authority revisions;
32. genuinely new still-binding task semantics are reconciled into canonical current authority before the next handoff when snapshot completeness requires it; and
33. concrete sibling evidence already governed by explicit invariant authority need not be promoted into new normative semantics merely for provenance.

Tests should protect these **semantic distinctions**, not the exact `N/F/R` labels, heading names, or this authority file's wording.

# Implementation closure review — NO-PASS

## Reviewed candidate

Exact reviewed branch candidate:

`9a47e492534ba990acbc03ec6dab62de3fe8178a`

The current branch differs from the previously validated implementation candidate only by removal of temporary branch-build/patch scaffolding. That cleanup does not invalidate prior build/package/parity evidence. The implementation review nevertheless finds a genuine acceptance blocker below.

## Blocking family: under-discriminating Protocol 5.12 semantic regression acceptance

### Protected claim

Protocol 5.12's regression suite must prevent the new convergence controls from drifting into their prohibited opposites. For polarity-sensitive policy, a green test must demonstrate the required semantic relation/direction strongly enough that a contradictory or inverted policy does not pass merely because the same keywords remain present.

### Semantic owner / affected surface

Primary owner:

- `tests/test_protocol_512_convergence.py`

Affected evidence/consumers:

- O10 semantics 1-33;
- `tests/test_protocol_contracts.py` where it overlaps preservation/version assertions;
- established counterfactual/polarity-testing patterns in `tests/test_protocol_511_tool_assistance.py` and other protocol regression tests;
- canonical Protocol 5.12 source clauses only if stronger tests expose actual ambiguity or contradiction.

### Failure mechanism

The new Protocol 5.12 suite relies predominantly on whole-document `assertIn(...)` keyword/prose checks. That proves presence, but for many normative rules it does not prove polarity, relationship, exclusivity, or contradiction resistance.

Representative failures of the current acceptance mechanism include:

- checking for `family closure after recurrence` or `triggers bounded design reconsideration` does not prove that recurrence actually **requires** those actions rather than merely discussing them;
- checking for `trigger actually fired` can remain green if surrounding policy says the trigger need not fire;
- checking for `proportionately saturate the directly implicated family` can remain green if a contradictory clause tells review not to do so;
- checking for `three-tool sequence mandatory` is especially non-discriminating: the current source is correct because it says a three-tool sequence is **not mandatory**, but the assertion would also pass if the convergence-specific rule were inverted to make the sequence mandatory;
- checking only for `concrete new sites` does not establish the required rule that already-governed concrete sibling evidence need not become new normative task semantics;
- exact heading/prose substrings such as `family closure after recurrence` also create avoidable false failures under semantically equivalent editorial refactoring, contrary to the requirement to protect durable semantics rather than this authority's wording.

The repository already contains stronger Protocol 5.11 precedent: paragraph/clause-scoped policy validators plus synthetic inverted-policy examples that prove a matcher rejects forbidden polarity. Protocol 5.12 should reuse that methodological pattern where it materially fits instead of regressing to keyword presence as the principal evidence.

### Reviewer saturation of this family

The review did not stop at the first weak assertion. It inspected the 33 required semantic obligations and the new test file as one acceptance family.

The rework must harden, at minimum, the polarity/relationship-sensitive classes covering:

- first-local-defect proportionality versus universal escalation;
- recurrence -> family closure;
- incomplete family closure versus automatic redesign;
- genuine post-family recurrence -> mandatory Design reconsideration;
- Mode R same-design structural refactor versus automatic normative revision;
- semantic family anti-fragmentation and anti-overaggregation;
- broad independent review and material new-issue authority;
- reviewer family saturation versus first-blocker stopping;
- bounded saturation/stopping versus universal exhaustiveness;
- review-readiness non-refusal;
- acceptance-liveness and real-owner/seam/failpoint behavior;
- structural evidence as complement rather than replacement for runtime acceptance;
- convergence-tool optionality, especially the non-mandatory three-tool rule;
- ordinary implementation nonconformance versus numbered revision churn;
- new binding semantics versus required current-authority reconciliation;
- concrete already-governed sibling evidence versus unnecessary normative promotion;
- preservation of evidence reuse/context economy/coherent stage granularity.

This sibling search is considered **saturated enough for review routing**: the weakness is systemic across the new Protocol 5.12 semantic test layer, and further reviewer enumeration would mainly duplicate Implementation's required O10 test hardening. No independent source-architecture or distribution blocker was found that warrants a separate rework family.

## Required one-fix rework patch

Implementation must close this acceptance family in one coherent patch before requesting the next comprehensive Design review.

1. **Harden `tests/test_protocol_512_convergence.py` as semantic/counterfactual acceptance.** Keep exact equality/presence checks where they genuinely establish identity facts, but do not use whole-document keyword presence as the principal proof of polarity-sensitive policy.
2. **Use bounded semantic validators appropriate to the claim.** Paragraph/clause-scoped checks, relation-aware helpers, explicit positive/negative examples, or an equivalent low-complexity method are acceptable. Reuse the proven Protocol 5.11 polarity-testing style where practical; do not create a large generic framework solely for this task.
3. **Add synthetic inverted/contradictory counterfactuals.** The test machinery must demonstrably reject representative forbidden policies for the material classes listed above. In particular, explicitly prove rejection of:
   - universal redesign/escalation for a first clean local defect;
   - recurrence that permits only another local sibling patch instead of family closure;
   - incomplete family closure that automatically forces redesign;
   - genuine post-family recurrence that permits another ordinary patch without Design reconsideration;
   - Mode R that always requires a normative authority revision;
   - source-file-based family fragmentation and unrelated subsystem-wide overaggregation;
   - review intentionally stopping at the first cheap sibling blocker when proportionate saturation is available;
   - universal/exhaustive reviewer saturation;
   - refusal of an explicitly requested review because readiness is incomplete;
   - a mandatory three-tool convergence pipeline;
   - dead seam/failpoint/callback acceptance where the intended trigger need not fire;
   - structural/negative scans substituting for required executable acceptance;
   - ordinary implementation misses requiring numbered authority revisions;
   - new binding semantics being left outside canonical current authority;
   - already-governed concrete sibling evidence being forced into new normative semantics merely for provenance.
4. **Account for all 33 O10 semantics.** Each semantic must be protected by a genuinely discriminating new/existing test appropriate to its risk. Do not duplicate strong existing tests merely for counting, but make the coverage recoverable from the test organization itself without relying on this review conversation.
5. **Preserve established Protocol 5.4-5.11 tests.** Do not weaken prior assertions to accommodate the new suite. The stronger Protocol 5.11 polarity/counterfactual tests are positive precedent, not obstacles.
6. **Do not rewrite correct source merely to satisfy exact test strings.** If hardened tests expose a genuinely ambiguous or contradictory canonical Protocol 5.12 clause, correct that clause at its canonical owner and regenerate affected distributions. Otherwise keep the source semantics stable.
7. **Keep the patch one acceptance-family repair.** Do not add a new lifecycle role, persistent semantic ledger, universal matrix, repository-wide scan requirement, or mandatory analyzer pipeline.

## Required acceptance for the rework candidate

After all task-owned source/test changes are stable, execute on the exact candidate:

```bash
python -m unittest tests.test_protocol_512_convergence -v
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

If canonical shipped source changes, regenerate committed `dist/` from `source/` before parity checking. If only tests change, do not manufacture distribution churn; still run the fresh build/validation/parity checks to prove shipped artifacts remain valid.

Before the next Design review, reconcile the exact candidate against O1-O12 plus this current authority and verify that no temporary rework scaffolding remains.

## Current verdict and next handoff

**NO-PASS.**

The blocker is implementation acceptance nonconformance, not a newly discovered product-design deficiency. Protocol 5.12's frozen convergence design remains the target. Implementation should produce one semantic-regression-hardening patch covering the complete blocker family, run the full acceptance workflow on that exact candidate, and then request one comprehensive independent closure review.
