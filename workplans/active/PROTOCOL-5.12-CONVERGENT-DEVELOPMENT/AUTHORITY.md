---
kind: workplan-authority
workplan_id: PROTOCOL-5.12-CONVERGENT-DEVELOPMENT
parent_workplan: ../PROTOCOL-5.12-CONVERGENT-DEVELOPMENT.md
protocol_version: 5.11.0
target_protocol_version: 5.12.0
status: active
reviewed_date: 2026-09-03
reviewed_candidate: dea9b7a58c1c1cba52617d94fc31745635ed18e1
review_verdict: no-pass
---

# Protocol 5.12 Convergent Development — Current Authority

## Authority composition and current state

The current Design -> Implementation authority is the supplied set:

1. `workplans/active/PROTOCOL-5.12-CONVERGENT-DEVELOPMENT.md`; and
2. this `AUTHORITY.md`.

The parent workplan remains the substantive Protocol 5.12 implementation contract. This authority carries accepted Design refinements and the current independent implementation-review result. Where this authority is more specific, it controls.

The Protocol 5.12 **product/design target remains frozen and sound**. Candidate `dea9b7a58c1c1cba52617d94fc31745635ed18e1` is **NO-PASS** because the semantic-regression acceptance family is substantially improved but still not genuinely closed. This remains **incomplete family closure / implementation nonconformance under the existing design**, not a workplan/design deficiency and not a Mode R architecture reopen.

Do not create a numbered review-revision series for this rework. Git history provides provenance. Reconcile the canonical current authority in place so each new Design -> Implementation handoff remains snapshot-complete.

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

Conversely, broad subsystem labels are not valid families when members lack a shared closure mechanism or semantic authority. Actors may not fragment one recurring family into source-local names to avoid family closure or Design reconsideration, and may not overaggregate unrelated defects to force broader work.

When family closure is active, its basis must make the boundary reviewable by stating, as applicable, the governing invariant/product claim; semantic owner/authority; included transition/lifecycle/failure classes; materially distinct exclusions; discovered member sites/equivalence classes and their disposition; and completeness basis plus material limitations. No universal persistent matrix is required.

### B. Incomplete family closure versus genuine post-family recurrence

A prior family-closure cycle counts as a **genuine family closure** for later escalation only when, on the then-current candidate:

1. the family was materially defined rather than merely named;
2. an adequate bounded closure basis was established;
3. discovered members/equivalence classes were dispositioned;
4. the canonical enforcement/ownership realization, including justified specialization, was implemented;
5. required focused, family-level affected regression, real-owner/integration, and structural/absence evidence actually executed as applicable; and
6. the family was explicitly claimed closed on that evidence.

A label, partial search, vacuous scan, missing real-owner evidence, artificially narrow family, or counterfactual evidence that never exercises the discriminating condition is incomplete family closure.

Incomplete/narrow/vacuous family closure routes as **implementation nonconformance** to complete/correct the family under the accepted design unless separate redesign evidence exists.

A material same-family blocker that survives or reappears despite genuine family closure, or a census that establishes duplicated/contradictory ownership, uncontrolled entry points, proliferating exceptional paths, or another structural redesign trigger, requires bounded Software Design reconsideration before another ordinary same-family patch cycle.

Mode R is a mandatory **Design reconsideration boundary**, not a predetermined architecture rewrite. Design may change the affected frozen target decision, or preserve frozen product/design semantics and require stronger implementation consolidation/refactor/canonicalization under the same authority.

No recurrence count, review count, cycle budget, or convergence target can force acceptance.

### C. Independent-review family saturation and stopping

When review finds a blocker in an identifiable material family, the reviewer must, to the degree proportionate and practical, continue cheap/high-information read-only inspection far enough to characterize obvious sibling variants/equivalence classes instead of intentionally returning one cheap sibling per review cycle.

Group same-family evidence into one family-level closure problem. Reviewer saturation is not a second implementation census and not whole-repository exhaustiveness. Expansion may stop when the plausible low-cost sibling space is sufficiently characterized, further work would become implementation-like or expensive/unavailable, additional enumeration would mainly duplicate Implementation's required family census, or no evidence-driven ownership/contract/affected chain justifies broader search.

A closure review may PASS when accepted-contract conformance is closed, affected-surface evidence is adequate, material family-closure premises have been challenged, material engineering risk surfaces have been inspected to evidence-directed sufficiency, and no unresolved blocker or evidence-driven reason to expand remains. Review is not proof that no conceivable defect exists.

### D. Review readiness is not a refusal mechanism

Normal final independent closure review should receive a review-ready exact candidate. Earlier Design consultation or a bounded high-risk checkpoint may occur when it materially reduces rework.

A user-requested review must not be refused merely because the candidate is not review-ready. Missing mandatory regression/integration/structural/liveness evidence is implementation nonconformance under unchanged authority unless it exposes a genuine design deficiency.

Missing evidence does not manufacture a design revision. Final claimed implementation closure still requires all protocol-required acceptance on a candidate whose relevant dimensions have not subsequently changed.

### E. Revision economy and snapshot-complete authority

Do not create a numbered authority revision solely because an existing obligation was missed, another sibling site violates an already-explicit invariant, a required check was absent/failed, another implementation patch is required, generated derivatives need regeneration, or review supplies more concrete evidence without changing binding task semantics.

If review discovers a genuinely new still-binding task-specific requirement, consequence, acceptance boundary, redesign trigger, or other semantic constraint not recoverable from supplied current authority, reconcile it into canonical current authority before the next Design -> Implementation handoff.

Concrete new sites, examples, call stacks, failing inputs, or sibling manifestations are evidence rather than new normative semantics when current supplied invariant/owner authority already governs them strongly enough for a new implementer to recover the required end state.

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

- **O1 workflow/workplans:** canonical convergence mechanics include anti-fragmentation/anti-overaggregation, genuine versus incomplete family closure, Design reconsideration outcomes, reviewer saturation/stopping, non-refusal review readiness, and revision economy with snapshot completeness.
- **O2 architecture/design:** genuine post-family recurrence requires Design reconsideration; same-design structural refactor/consolidation is a valid outcome when frozen target semantics remain sound.
- **O3 testing/validation:** acceptance liveness protects real-owner and seam/failpoint/callback claims; structural evidence complements rather than replaces runtime acceptance.
- **O4 Software Implementation:** recurring families are closed systematically, discovered members/equivalence classes are dispositioned, and genuine post-family recurrence routes to Design instead of another ordinary patch.
- **O5 Software Design:** blockers are grouped by semantic family, implicated families are proportionately saturated, incomplete family closure is distinguished from genuine post-family recurrence, and review stops by evidence-directed sufficiency rather than exhaustive-defect proof.
- **O6 repository intake:** progressive intake remains default; bounded census is used only when recurrence or the product claim makes completeness material.
- **O7 tool-assisted engineering:** Serena/Semgrep/Hypothesis and equivalent tools remain optional instruments; their absence does not relax the claim and their presence does not make a three-tool pipeline or whole-repository scan mandatory.
- **O8 workplan template:** convergence guidance remains conditional and nonbureaucratic.
- **O9 version/release:** Protocol 5.12 remains a backward-compatible minor refinement; older workplans retain declared-version meaning unless explicitly reconciled/upgraded.
- **O10 regression:** the 33 convergence/preservation semantics below are protected by durable semantic tests rather than brittle prose-presence checks where policy direction matters.
- **O11 distributions:** canonical source builds into valid shipped bundles with source-to-`dist` parity.
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

# Current implementation closure review — NO-PASS

## Reviewed candidate and accepted evidence

Exact reviewed branch candidate:

`dea9b7a58c1c1cba52617d94fc31745635ed18e1`

Relative to the prior reviewed authority candidate `8571f374adc62817149e1f90781cf291929a2ca4`, the persistent implementation delta is confined to `tests/test_protocol_512_counterfactual_closure.py`. Temporary diagnostic workflow/log scaffolding is absent from the final tree, and no canonical Protocol 5.12 source or committed `dist/` content changed.

The exact candidate has genuine green repository evidence. GitHub Actions run `33784769131` completed successfully on this SHA with the complete regression suite, canonical skill-package build, independent package validation, committed-distribution parity, and `git diff --check`. That evidence is accepted for the claims it actually establishes. It does not override a semantic defect in the acceptance harness itself.

## Blocking family: residual contradiction branches remain unproved

### Protected claim

For polarity/relationship-sensitive Protocol 5.12 policy, retained-positive counterfactuals must actually exercise the discriminating branch: a representative forbidden semantic is added while otherwise-valid positive prerequisites remain, and the validator used for the claim must reject that contradictory policy.

The rework successfully closes most of the previously identified family. The remaining blocker is smaller but genuine and remains within the same semantic-regression acceptance family.

### Finding 1 — mandatory three-tool contradiction is not asserted through the validator

`test_tool_optional_policy_rejects_a_mandatory_pipeline` constructs an otherwise-valid tool-optionality policy and inserts:

`Serena, Semgrep, and Hypothesis must always be used as a mandatory three-tool sequence.`

However, the test never asserts `tooling_optional_holds(contradictory) == False`. It only verifies that the contradictory text exists and that the real source does not contain one exact forbidden sentence.

This is a material false-pass path, not merely missing ceremony. The current `tooling_optional_holds` forbidden regex looks for `must|required to|always` *before* `Serena|Semgrep`, while the constructed contradiction names Serena/Semgrep/Hypothesis first and places `must always` afterward. The retained-positive contradictory fixture therefore still satisfies `tooling_optional_holds`.

This leaves **O10-18 / O7 tool optionality** under-discriminating despite the test name claiming rejection.

### Finding 2 — O10-23 retained-positive proof does not exercise file fragmentation or overaggregation

The new `family_identity` validator contains representative forbidden branches for textual grouping, separate-file independence, broad-label acceptance, file fragmentation, and unrelated overaggregation. But the retained-positive counterfactual test exercises only `Family membership is textual similarity.`

The prior all-negative fixture remains vacuous for proving those additional branches because it removes the positive prerequisites. The current suite therefore still lacks the explicitly required retained-positive proof that:

- separate files do not make same-semantic defects independent / file-based fragmentation is rejected; and
- unrelated subsystem-wide overaggregation/broad-label grouping is rejected.

The helper implementation appears capable of rejecting representative forms, so this is primarily missing durable counterfactual evidence rather than a source-policy defect.

### Finding 3 — O10-8 temporary-map conditionality/non-persistence remains presence-oriented

`bounded_census` now correctly protects conditional bounded census and rejects universal whole-repository census. It also requires the positive phrase that temporary closure maps are not universal persistent traceability artifacts.

But the retained-positive counterfactual for this helper exercises only the whole-repository-census inversion. No retained-positive case proves the distinct O10-8 rule that temporary closure maps remain conditional/nonpersistent rather than becoming mandatory permanent process artifacts. A representative contradiction such as `Temporary closure maps must be retained permanently` can coexist with the positive prerequisites without being rejected by the current validator.

This is a second unexercised directional branch in the same bounded-census/map acceptance family.

### Saturation and routing

The review rechecked the original helper family, the new retained-positive helper family, the explicitly named O10-13/14/15/19/21/22 directional closures, O10-18 tool optionality, O10-23 family identity, O10-8 bounded-census/map semantics, final tree delta, and exact-candidate CI. The new broad-review, closure-horizon, unrelated-issue, mandatory regression/integration, evidence-economy, fixed-count, review-saturation, review-nonrefusal, escalation, liveness, structural-complementarity, revision-economy, current-authority, and concrete-evidence counterfactuals are materially discriminating enough for this task. Further reviewer enumeration would mainly duplicate the remaining implementation repair.

No independent source-architecture, packaging, distribution, lifecycle-role, protocol-version, or product-semantics blocker was found. This remains **incomplete family closure under the frozen design**. It is not genuine post-family recurrence for Mode R because the claimed family closure still contains known unexercised/false-pass branches.

## Required final family-completion patch

Implementation must complete this same acceptance family in one bounded patch before the next comprehensive Design review.

1. **Repair tool-optionality counterfactual end to end.** Make `tooling_optional_holds` reject the representative retained-positive mandatory-pipeline fixture regardless of whether the modal (`must`/`mandatory`/equivalent representative form) appears before or after the Serena/Semgrep/Hypothesis names. In `test_tool_optional_policy_rejects_a_mandatory_pipeline`, first prove the positive fixture passes, then explicitly assert that the contradictory fixture fails the same validator. Keep this representative and bounded; do not build a general natural-language parser.
2. **Exercise O10-23's remaining branches.** Add retained-positive counterfactuals that independently add representative separate-file/file-fragmentation and broad-label/unrelated-overaggregation contradictions and assert `family_identity` rejects them. Reuse the existing positive fixture and helper; do not add another policy framework.
3. **Exercise O10-8 map conditionality/non-persistence.** Add a retained-positive bounded-census/map fixture plus a representative contradiction that makes temporary closure maps mandatory/permanent, and assert the same validator rejects it. Harden `bounded_census` only as needed to reject that governed representative forbidden realization while retaining the correct source policy.
4. **Preserve the already-closed family members.** Do not weaken or remove the new retained-positive cases for escalation, review saturation/bounds, non-refusal, broad independent review, closure horizon, unrelated issue routing, liveness, structural complementarity, regression/integration mandatory status, evidence/context/stage economy, fixed-count acceptance, revision economy, current-authority reconciliation, or concrete evidence.
5. **Keep source semantics stable.** Current canonical Protocol 5.12 policy is accepted. Do not rewrite `source/` merely to satisfy matcher wording unless the corrected tests independently expose a real source contradiction. If source remains unchanged, do not manufacture `dist/` churn.
6. **Keep this one test-family repair.** No new lifecycle role, ledger, matrix, universal scan, mandatory analyzer sequence, or persistent diagnostic scaffold.

## Required acceptance for the next candidate

After task-owned changes are stable, execute on the exact candidate:

```bash
python -m unittest tests.test_protocol_512_convergence -v
python -m unittest tests.test_protocol_512_counterfactual_closure -v
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

If canonical shipped source changes, regenerate committed `dist/` before parity checking. If only tests change, do not manufacture distribution churn; still run fresh build/validation/parity checks to prove shipped artifacts remain valid.

Before the next Design review, reconcile the exact candidate against O1-O12 plus this authority and verify that no temporary rework scaffolding remains.

## Current verdict and next handoff

**NO-PASS.**

The blocking family is still implementation acceptance nonconformance. Close the three residual contradiction branches above in one bounded test-family patch, run the exact-candidate acceptance chain, and then request one comprehensive independent closure review.
