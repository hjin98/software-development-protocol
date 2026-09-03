---
kind: workplan-authority
workplan_id: PROTOCOL-5.12-CONVERGENT-DEVELOPMENT
parent_workplan: ../PROTOCOL-5.12-CONVERGENT-DEVELOPMENT.md
protocol_version: 5.11.0
target_protocol_version: 5.12.0
status: active
reviewed_date: 2026-09-03
reviewed_candidate: 2bca076e21aa030405e9148b026342efa5522f4e
review_verdict: no-pass
---

# Protocol 5.12 Convergent Development — Current Authority

## Authority composition and current state

The current Design -> Implementation authority is the supplied set:

1. `workplans/active/PROTOCOL-5.12-CONVERGENT-DEVELOPMENT.md`; and
2. this `AUTHORITY.md`.

The parent workplan remains the substantive Protocol 5.12 implementation contract. This authority carries the accepted Design refinements and the current independent implementation-review result. Where this authority is more specific, it controls.

The Protocol 5.12 **product/design target remains frozen and sound**. Candidate `2bca076e21aa030405e9148b026342efa5522f4e` is **NO-PASS** because the semantic-regression acceptance family is materially improved but not yet genuinely closed. This is **incomplete family closure / implementation nonconformance under the existing design**, not a new product-design deficiency and not a Mode R architecture reopen.

Do not create a numbered review-revision series for this rework. Git history provides provenance. Current authority is reconciled in place so the next handoff remains snapshot-complete.

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

A label such as `Mode F complete`, a partial caller search, a vacuous scan, missing real-owner evidence, an artificially narrow family, or counterfactual evidence that never exercises the discriminating condition is not a genuine family closure.

If review finds the prior family closure incomplete, narrow, or vacuous, route it as **implementation nonconformance** and complete/correct family closure under the accepted design unless separate redesign evidence exists.

If a material same-family blocker survives or reappears despite a genuine family closure, or the family census itself establishes duplicated/contradictory ownership, uncontrolled entry points, proliferating exceptional paths, or another structural redesign trigger, Software Design must perform bounded ownership/architecture reconsideration before another ordinary same-family patch cycle.

Mode R is a mandatory **Design reconsideration boundary**, not a predetermined architecture rewrite. Design may either change a frozen material target decision and reconcile current authority, or preserve frozen product/design semantics and require stronger implementation consolidation/refactor/canonicalization under the same authority.

No recurrence count, review count, cycle budget, or convergence target can force acceptance.

### C. Independent-review family saturation and stopping

When review finds a genuine blocker in an identifiable material family, the reviewer must, to the degree proportionate and practical, continue cheap/high-information read-only inspection far enough to characterize obvious sibling variants/equivalence classes rather than intentionally returning one cheap sibling per review cycle.

Review must identify the governing invariant/owner/failure family, characterize the directly implicated sibling space enough to distinguish isolated from systemic behavior, group concrete same-family findings into one family-level closure problem, and state whether reviewer sibling discovery appears saturated or whether systematic family closure remains Implementation's responsibility.

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

# Current implementation closure review — NO-PASS

## Reviewed candidate and accepted evidence

Exact reviewed branch candidate:

`2bca076e21aa030405e9148b026342efa5522f4e`

From the previous NO-PASS authority to this candidate, the persistent task delta is confined to `tests/test_protocol_512_convergence.py`; temporary rework workflow/log scaffolding was removed before the final candidate.

The exact candidate has genuine green repository evidence: the native protocol build check completed successfully with the complete regression suite, canonical skill-package build, independent package validation, committed-distribution parity, and whitespace check. This evidence is accepted for the claims it actually establishes. It does **not** cure semantic under-discrimination in the acceptance harness itself.

## Blocking family: semantic counterfactuals do not yet prove contradiction resistance

### Protected claim

For a polarity/relationship-sensitive Protocol 5.12 policy, regression evidence must distinguish the required relation from its prohibited opposite. A counterfactual test must not pass merely because its negative fixture already fails an unrelated positive precondition. Representative contradictory policy that retains the otherwise-valid positive semantics must be rejected by the same validator.

### Primary owner and family boundary

Primary owner:

- `tests/test_protocol_512_convergence.py`

Family members are the Protocol 5.12 semantic validators and O10 checks whose claim depends on policy direction, relationship, boundedness, conditionality, or mandatory-versus-optional status. Exact identity facts such as `PROTOCOL_VERSION == 5.12.0` are not forced into this family merely because they live in the same file.

### Finding 1 — current negative fixtures are largely vacuous with respect to the forbidden branch

The three counterfactual test groups call each validator with a fully inverted short policy and assert `False`. For most validators, those policies omit one or more **required positive** regexes. The assertion therefore remains green even if the validator's forbidden-polarity detection is deleted or broken.

Representative examples:

- the first-local negative omits the required `does not require ...` relation;
- the recurrence negative omits the required `family closure is required ... recurs after claimed closure` relation;
- the genuine-post-family negative omits the required `route to ... Software Design reconsideration` relation;
- the Mode-R negative omits the required `normative design change is not predetermined` / same-design realization relation;
- the revision-economy negative omits the required `do not require ... numbered authority revision` relation;
- the current-authority negative omits the required canonical-reconciliation relation.

These tests show that a wholly different policy does not satisfy the complete positive matcher. They do **not** prove that an otherwise passing policy plus a contradictory clause is rejected.

### Finding 2 — representative contradictory policies can still satisfy current validators

The family weakness is not theoretical. Current helper structure permits representative positive-plus-contradiction false positives.

Examples include:

- `family_identity_holds` checks only the required positive patterns. A section can contain all four required anti-fragmentation/anti-overaggregation sentences and also state that family membership *is* textual similarity; the validator still returns true.
- `saturation_bounds_hold` rejects only a narrow `must|required to -> exhaustive|whole-repository|every conceivable` grammar. A passing bounded-stopping policy can also state that reviewer expansion **always** continues across the whole repository exhaustively without tripping that matcher.
- `nonrefusal_holds` can accept its required non-refusal sentence while a later representative contradiction refers to the same review indirectly (for example, `that review is always refused`) outside its narrow forbidden grammar.

Protocol regression tests do not need to parse unrestricted English, but they must prove the representative forbidden realizations they claim to guard rather than relying on missing positive prerequisites.

### Finding 3 — several explicitly implicated O10 classes remain presence-oriented rather than discriminating

The rework substantially hardened escalation, family identity, review saturation, liveness, tooling, and authority/revision helpers, but several polarity-sensitive/preservation classes remain primarily `assertIn(...)` checks without an equivalent relation-aware existing test demonstrated in the current suite.

The next family patch must cover, at minimum, the materially directional parts of:

- **O10-13:** broad independent review and authority to surface a material new independent issue;
- **O10-14:** closure horizon remains focus rather than a scope ceiling;
- **O10-15:** unrelated pre-existing issues are not automatically current blockers absent material interaction;
- **O10-19:** stage-local plus final affected-surface regression/integration remain mandatory rather than optional;
- **O10-21:** evidence reuse/context economy/coherent-stage guidance is preserved without becoming permission to skip invalidated/final evidence;
- **O10-22:** no recurrence/review/cycle count can force acceptance.

O10-20 production qualification separation and other low-ambiguity preservation facts may retain simpler assertions when the checked clause itself establishes the required direction and existing tests genuinely protect the opposite. Do not create counterfactual machinery merely for a numeric coverage target.

### Reviewer saturation and routing

This review inspected the complete helper/counterfactual pattern and the remaining O10 presence-oriented classes rather than stopping at one example. The blocker is still one semantic-regression acceptance family; further reviewer enumeration would mainly duplicate Implementation's correction work.

The prior rework is **not treated as a genuine family closure for Mode R purposes**. The acceptance mechanism was materially improved, but its negative evidence is partly vacuous and known members of the originally implicated semantic-test family remain under-discriminating. Under the frozen convergence rule, this is incomplete family closure / implementation nonconformance to be completed under the same design.

No source-architecture, packaging, distribution, lifecycle-role, or protocol-version blocker was found. The persistent rework diff is test-only, and exact-candidate CI establishes current package validity/parity. No Protocol 5.12 policy rewrite is justified by this review.

## Required one-fix family-completion patch

Implementation must complete the same semantic-regression family in one coherent patch before the next comprehensive Design review.

1. **Make counterfactual tests non-vacuous.** For every polarity-sensitive validator exercised by the counterfactual groups, construct a minimal synthetic **positive** policy and first assert that the validator accepts it. Then derive a representative contradictory/inverted form that retains the positive prerequisites and assert that the same validator rejects it.
2. **Exercise the discriminating branch.** Prefer `positive fixture -> add/change one forbidden semantic -> must fail` over unrelated all-negative prose. The negative case should fail because of the forbidden relation being introduced, not because required positive content disappeared.
3. **Harden validators only as far as the governed claim requires.** Add representative forbidden-clause handling for helpers such as family identity, bounded reviewer saturation, and review non-refusal so the tested contradictions are actually rejected. Do not build a general natural-language parser or large generic policy framework.
4. **Close the remaining directional O10 members.** Add small relation-aware validators/counterfactuals, or point to and rely on genuinely discriminating existing tests, for O10-13, O10-14, O10-15, O10-19, O10-21, and O10-22. Preserve simple exact/presence assertions for identity or low-ambiguity facts when they genuinely establish the claim.
5. **Keep coverage recoverable from the test organization.** The test names or nearby organization must make all 33 O10 semantics recoverable without a new ledger/matrix. Existing strong tests count and should not be duplicated for counting.
6. **Do not weaken earlier Protocol 5.4-5.11 regression.** In particular, preserve the Protocol 5.11 clause/polarity precedents and all existing stage/final regression, integration, snapshot-completeness, tool-optionality, and acceptance-integrity safeguards.
7. **Keep correct source semantics stable.** Do not rewrite canonical Protocol 5.12 policy merely to satisfy matcher wording. Change source only if the corrected semantic tests independently expose a real ambiguity/contradiction, then regenerate affected distributions.
8. **Keep this one family repair.** Do not add a new lifecycle role, persistent semantic ledger, universal matrix, whole-repository scan mandate, or mandatory analyzer pipeline.

## Required acceptance for the next candidate

After task-owned changes are stable, execute on the exact candidate:

```bash
python -m unittest tests.test_protocol_512_convergence -v
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

If canonical shipped source changes, regenerate committed `dist/` before parity checking. If only tests change, do not manufacture distribution churn; still run the fresh build/validation/parity checks to prove shipped artifacts remain valid.

Before the next Design review, reconcile the exact candidate against O1-O12 plus this current authority and verify that no temporary rework scaffolding remains.

## Current verdict and next handoff

**NO-PASS.**

The blocking family is still implementation acceptance nonconformance. Complete the semantic counterfactual family so representative positive-plus-contradiction policies are rejected and the remaining directional O10 members are genuinely protected, then request one comprehensive independent closure review.