#!/usr/bin/env python3
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def rd(p): return (R/p).read_text(encoding='utf-8')
def wr(p,s): (R/p).write_text(s,encoding='utf-8')
def rep(p,a,b):
 s=rd(p)
 if b in s: return
 if a not in s: raise SystemExit(f'{p}: missing replacement anchor')
 wr(p,s.replace(a,b,1))
def ins(p,anchor,block,sentinel):
 s=rd(p)
 if sentinel in s:return
 if anchor not in s:raise SystemExit(f'{p}: missing insertion anchor {anchor}')
 wr(p,s.replace(anchor,block.rstrip()+'\n\n'+anchor,1))

rep('source/PROTOCOL_VERSION','5.11.0\n','5.12.0\n')

W='''## Convergent repair, review readiness, and revision economy

Normal evidence-directed development remains the default. A first clean local defect receives an owning-layer fix plus proportionate consideration of obvious variants; it does not require a census, matrix, or redesign. When evidence shows that instance-level repair did not close a recurring material invariant or failure mechanism, the unit of work broadens to the bounded **defect family** before another equivalent repair cycle.

### Semantic defect families

A material defect family is the smallest useful semantic set whose members share enough of the following that one owner-level or mechanism-level closure can reasonably govern them:

```text
protected invariant / required product claim
+ semantic owner or authority class
+ state / transition / lifecycle class
+ materially equivalent failure mechanism or forbidden realization
```

Family membership is not textual similarity. Separate files, helpers, callers, commands, exception branches, or tests do not make defects independent when they violate the same product claim for the same semantic reason. Conversely, broad labels such as `storage bugs`, `scheduler bugs`, `security issues`, or `performance problems` are not valid families when the members lack a shared authority or closure mechanism. Do not fragment a recurring family to keep applying local patches, and do not overaggregate unrelated work to force a larger redesign.

### Family closure after recurrence

Family closure is required when materially equivalent sibling behavior recurs after claimed closure; another local repair is needed in the same owner/failure mechanism and evidence shows a pattern; a supposedly canonical safety/correctness mechanism has production bypasses; proxy/vacuous acceptance weakness plausibly affects a family of claims; wrappers/fallbacks/special cases accumulate around the same owner; or correctness itself requires all members of a finite critical site set to satisfy one invariant.

A bounded closure basis records the governing invariant/product claim and semantic owner; included transition/lifecycle/failure classes plus materially distinct exclusions; discovered production sites or equivalence classes and their disposition; the completeness basis and limitations of source, semantic, structural, configuration, generated-source, or runtime discovery; the canonical enforcement/ownership realization including justified specialization; and focused, family-level affected regression, real-owner/integration, and structural/absence evidence appropriate to the claim.

Use the cheapest sufficiently reliable discovery combination. A temporary closure map may be used when finite/exhaustive coverage materially establishes correctness, but it is not a generic persistent artifact. Whole-repository inventory remains unnecessary unless the actual product claim is repository-wide.

A prior cycle is a **genuine family closure** for later escalation only when the family was materially defined, an adequate bounded closure basis was established, discovered members/equivalence classes were dispositioned, the canonical realization was implemented, required executable and structural acceptance actually ran, and the family was explicitly claimed closed on that evidence. A label, partial search, vacuous scan, missing real-owner acceptance, or artificially narrow family is incomplete family closure and remains implementation nonconformance under the current accepted design unless independent redesign evidence already exists.

If the same material family survives or reappears after a genuine family closure, or the census itself demonstrates duplicated/contradictory ownership, uncontrolled entry points, proliferating exceptional paths, or another structural redesign trigger, stop another ordinary sibling-patch cycle and route to **bounded Software Design reconsideration**. Reconsideration is mandatory, but a normative design change is not predetermined: Design may keep frozen product/architecture semantics and require stronger implementation consolidation/refactoring/canonicalization, or reopen only the affected frozen decision when evidence shows that decision itself must change.

### Review readiness and exact-candidate closure

Normal final independent closure review should challenge a candidate Implementation has actually completed. Before claiming final review-ready state, Implementation completes, as applicable: exact candidate identity; accepted-contract reconciliation; all triggered family closure; material stage-local focused and affected regression; final affected-surface re-derivation; final complete affected-surface regression and real-boundary integration after invalidating executable edits; repository/project-required checks; structural/absence claims; acceptance-liveness evidence where a patched seam/failpoint/callback is material; known-failure triage; and final tree/diff inspection for stale paths, fallbacks, ownership drift, and unnecessary complexity.

Missing required closure/evidence makes the candidate not review-ready and is implementation nonconformance under unchanged authority, not an automatic design revision or a pass. Review readiness is a final-closure quality boundary, not a refusal mechanism: an explicitly requested review still proceeds to the highest useful depth available, and a bounded Design checkpoint may occur earlier when resolving a high-risk structural question before expensive final testing materially reduces rework.

### Independent review saturation and sufficiency

When a blocker implicates a material family, the reviewer should continue cheap, high-information read-only inspection of the directly implicated family far enough to characterize obvious sibling variants/equivalence classes before routing it back. Group same-family evidence into one family-level closure problem rather than intentionally returning one cheap sibling per review cycle. Review characterizes and batches the family; Implementation owns the systematic family closure.

Reviewer expansion stops when the materially plausible low-cost sibling space is sufficiently characterized, further discovery would become implementation-like reconstruction or expensive/unavailable execution, evidence already establishes that systematic family closure is required and more enumeration would mainly duplicate it, or no evidence-driven ownership/contract/affected-surface chain justifies broader inspection. State material limits rather than implying exhaustiveness. A sound PASS requires adequate contract closure, affected-surface evidence, challenge of material family-closure premises, and no unresolved material blocker or evidence-driven reason to expand; it is not proof that no conceivable repository defect exists.

### Finding routing, closure horizon, and authority revisions

Route findings by engineering meaning, not cycle count: an already-binding requirement/invariant/acceptance miss is implementation nonconformance under the same authority; a genuinely missing or incorrect still-binding task semantic requires reconciliation of current workplan/design before the next handoff; a newly affected material issue that preserves frozen design is incorporated as a necessary implementation consequence and grouped into an existing family when semantics match; an unrelated pre-existing issue with no material dependency on the active claim is routed separately.

Concrete new sites, call stacks, examples, failing inputs, or sibling manifestations are evidence rather than new normative semantics when current supplied invariant/owner authority already governs them strongly enough for a new implementer to recover the required end state. If new evidence reveals a still-binding task-specific consequence, acceptance boundary, or redesign trigger not recoverable from supplied current authority, reconcile that semantic into canonical current authority before the next Design -> Implementation handoff so snapshot completeness is preserved.

Ordinary implementation attempts and review cycles do **not** require a new numbered authority revision. Existing-obligation misses, unexecuted/failed tests, additional violating sites, implementation patches, generated-derivative regeneration, or clearer non-normative evidence do not by themselves mint task semantics. Projects may retain immutable revision snapshots for independent audit/concurrency needs, but ordinary version control of canonical current authority is sufficient unless project policy requires more.

For substantial work, a provisional **closure horizon** may identify material owners, contracts, state/persistence boundaries, consumers, and invariant families plausibly affected by the accepted change. It focuses implementation and helps classify unrelated findings, but it is not a scope ceiling: expand it whenever evidence establishes a plausible ownership, dependency, contract, or behavioral-impact chain.

### Development-cycle economy

After engineering fitness and product simplicity are preserved, minimize total cycle cost with high-information ordering: reproduce/diagnose before broad editing; search variants before patching an established recurring pattern; consolidate coherent edits before broad reruns; run cheap discriminating checks before family-level affected regression and cross-owner integration; reuse evidence whose claims cannot plausibly change; review deltas rather than replaying settled archaeology; and avoid requesting another comprehensive closure review until identified blocker families are closed where dependencies permit. One comprehensive review of a stable review-ready candidate is normally more valuable than repeated micro-review after each line-level repair.
'''
ins('source/shared/references/workflow-and-workplans.md','## Compact working state for long gated work',W,'## Convergent repair, review readiness, and revision economy')

A='''## Convergence boundary for repeated defect families

A first clean local defect remains a local owning-layer repair. When materially equivalent defects recur around the same invariant/authority/mechanism, establish the bounded semantic family and close it at the canonical owner, consolidating duplicate enforcement or deleting bypasses when that reduces the failure surface.

After an adequate family closure has implemented the canonical realization and passed required family-level real-owner, affected-regression, integration, and structural evidence, a same-family material recurrence triggers bounded Software Design reconsideration before another ordinary sibling patch. An incomplete or artificially narrow family closure is instead implementation nonconformance that must be completed unless separate redesign evidence already exists.

Design reconsideration does not automatically mean architecture churn or a new normative workplan revision. If frozen product/architecture/ownership semantics remain sound, Design may require a stronger implementation refactor, consolidation, API narrowing, or canonicalization under the same authority. Reopen current design authority only when a frozen material decision itself must change. Preserve justified specialization where distinct hardware, scientific, compatibility, lifecycle, or failure semantics make one abstraction worse.
'''
ins('source/shared/references/architecture-and-design.md','## Architecture documentation',A,'## Convergence boundary for repeated defect families')

T='''## Acceptance liveness and family-closure evidence

Proxy-proof acceptance also requires the intended acceptance mechanism to be live. When a material regression depends on a patched seam, failpoint, callback, hook, or similar trigger, establish that the trigger actually fired when practical; a green test that never exercised the intended boundary does not close the claim. When a production transition or decision is the claim, execute its real semantic owner and keep doubles below/outside that boundary.

When cheap and meaningful, demonstrate that a bug reproducer or equivalent counterfactual can distinguish known-broken behavior from corrected behavior. This is not a universal requirement to check out historical commits, run mutation testing, or create one test per source site. For family closure, prefer owner-level properties plus representative material transition/equivalence classes when that provides stronger semantic coverage.

Structural/negative scans complement runtime acceptance. If a structural rule establishes an acceptance-critical absence or bypass claim, validate the rule against representative known-positive and known-negative constructs and state its actual scan scope/limitations; zero findings outside a justified scan contract are not proof of absence.

For normal final independent review, functional review readiness includes exact candidate identity, required stage-local closure, final affected-surface re-derivation, final complete affected-surface regression, real-boundary integration, repository/project-required checks, and task-required structural/absence/liveness evidence on a candidate whose relevant dimensions have not changed afterward. A required check that is missing or did not execute remains incomplete acceptance/implementation nonconformance rather than a pass or an automatic design revision. An explicitly requested review still proceeds and reports the missing evidence; review readiness is not a mechanism for refusing review.
'''
ins('source/shared/references/testing-and-validation.md','## Optimize test cost, not coverage',T,'## Acceptance liveness and family-closure evidence')

I='''## Bounded census when completeness is itself a claim

Progressive evidence-directed inspection remains the default. Switch to a bounded census only when recurrence has established a material defect family or when the product claim itself is finite and exhaustive, such as every authority-bearing transition, compatibility reader, persistence mutation, or other critical site in a defined semantic owner family satisfying one invariant.

Bound the census by invariant, semantic owner/authority, transition/lifecycle class, and plausible affected chain rather than the whole repository. State the completeness basis and material blind spots of symbol/reference tools, static rules, dynamic registration/configuration, generated code, external consumers, or runtime-only behavior. Cross-check where those limitations can hide family members.

If the family cannot be bounded with sufficient confidence, do not present a partial search as exhaustive. Escalate ownership/design when uncontrolled entry points are themselves the problem, or use broader executable/property/integration evidence appropriate to the claim. Temporary closure maps are allowed when they materially reduce omission risk; they are not universal persistent traceability artifacts.
'''
ins('source/shared/references/repository-intake.md','## Prefer existing patterns',I,'## Bounded census when completeness is itself a claim')

G='''## Convergence-oriented composition

When a recurring material family requires systematic closure, optional tools can reduce rediscovery without becoming a mandatory pipeline:

- **Serena:** identify semantic owner, callers/references, repeated helper implementations, and affected symbol chains for a bounded family census; cross-check ordinary search/configuration/runtime evidence where language-server or dynamic behavior can hide members.
- **Semgrep:** turn a diagnosed unsafe/nonconforming construct into a focused structural variant scan; preserve known-positive/known-negative rule validation and honest scan-scope/false-negative accounting before relying on zero findings.
- **Hypothesis:** generalize a concrete input/state/transition failure into a bounded property or state machine so sibling states are challenged before another review; keep the real production owner in the test path when that owner is the acceptance claim.

Use another available semantic/static/property tool when it establishes the same claim more economically. Tool absence does not relax family closure, and tool presence does not make whole-repository exhaustiveness or a three-tool sequence mandatory.
'''
ins('source/shared/references/tool-assisted-engineering.md','## Completion discipline',G,'## Convergence-oriented composition')

P='''## Conditional convergence guidance

For substantial work where repeated-family risk, scope diffusion, or finite critical-site completeness is materially plausible, record only task-specific convergence information that reduces ambiguity or rework. This may include a provisional **closure horizon** of material owners/contracts/state boundaries/consumers/invariant families (it is not a scope ceiling); the semantic owner/invariant/failure-family key whose recurrence would require family-level closure; a bounded census/closure basis or temporary closure map when completeness itself is acceptance-critical; the condition under which recurrence after adequate family closure requires bounded Software Design reconsideration; and task-specific real-owner or acceptance-liveness constraints.

Keep this guidance conditional. A first clean local defect does not require a family matrix, and ordinary workplans do not require IDs, ledgers, persistent closure maps, whole-repository scans, or extra review artifacts merely for protocol compliance.
'''
ins('source/shared/templates/implementation_workplan_template.md','## Handoff closure',P,'## Conditional convergence guidance')

M='''## Close recurring defect families before another review

Keep the first clean local defect lightweight: fix the owning layer and consider plausible variants proportionately. If materially equivalent sibling behavior recurs after claimed closure, do not implement only the latest reported source site. Define the bounded semantic family by invariant/product claim, semantic owner or authority class, transition/lifecycle class, and materially equivalent failure mechanism; avoid both file-by-file fragmentation and broad subsystem labels that aggregate unrelated work.

For a recurring family, establish the closure basis described in `references/workflow-and-workplans.md`: identify/disposition member sites or equivalence classes, state completeness basis and limitations, choose the canonical owner/enforcement mechanism, eliminate unjustified bypasses/fallbacks/duplicate authority, and execute required family-level focused, affected-regression, real-owner/integration, and structural/absence evidence before claiming closure.

If review shows a previous family-closure claim was incomplete, artificially narrow, or supported by vacuous acceptance, complete/correct that family closure under the existing accepted design unless separate redesign evidence exists. If the same family materially fails after an adequate family closure, stop ordinary patching and route bounded Software Design reconsideration. Design may preserve the frozen target and require structural consolidation/refactoring under the same authority; a normative design revision is needed only when a frozen material decision must change.

Where dependencies permit, close all blocker families identified by one comprehensive review before requesting the next comprehensive closure review. Continue focused checks during coherent editing, stage-local affected regression at material behavior boundaries, evidence reuse where valid, and final exact-candidate acceptance after material executable edits stabilize.
'''
ins('source/roles/software-implementation/SKILL.md','## Close coherent stages, not individual edits',M,'## Close recurring defect families before another review')

D='''## Convergence-aware independent review

Final review should normally challenge a review-ready exact candidate, but do not refuse an explicitly requested review merely because Implementation omitted required closure or evidence. Inspect to the highest useful depth; missing mandatory regression/integration/structural/liveness evidence is implementation nonconformance unless it also exposes a genuine design deficiency.

Group blockers by semantic invariant/owner/failure family. When a blocker implicates a family and cheap, high-information sibling inspection remains, proportionately saturate the directly implicated family in the same review instead of intentionally stopping after the first sufficient NO-PASS example. Report one family-level closure problem plus concrete evidence. Stop expanding when further discovery becomes implementation-like, expensive/unavailable, mainly duplicates the systematic family census Implementation must perform, or lacks an evidence-driven affected chain. Independent rigor is evidence-directed sufficiency, not proof of zero conceivable defects.

Distinguish an incomplete family-closure claim from a genuine post-family recurrence. Incomplete/narrow/vacuous family closure routes back as implementation nonconformance to complete the family under accepted design unless separate redesign evidence exists. A same-family material blocker after an adequate family closure triggers bounded Design reconsideration before another ordinary patch cycle. Reconsideration may keep frozen target semantics and require implementation consolidation/refactoring, or reopen only the affected design decision if that frozen decision must change; it does not automatically mint a normative revision.

Additional concrete sites/examples already governed by supplied invariant authority are implementation/review evidence, not new task semantics. If review discovers a genuinely new still-binding task-specific consequence, acceptance boundary, or redesign trigger not recoverable from current supplied authority, reconcile it into canonical current authority before the next handoff for snapshot completeness. Ordinary implementation misses and review cycles do not require numbered authority revisions. Keep unrelated pre-existing issues separate unless they materially interact with the active product claim.
'''
ins('source/roles/software-design/SKILL.md','## Completion',D,'## Convergence-aware independent review')

V='''Protocol 5.12 is a backward-compatible **development-convergence and cycle-economy control refinement**. It preserves the Protocol 5 hierarchy, two-role lifecycle, Protocol 5.9 routing/distribution architecture, Protocol 5.10 snapshot-complete handoffs, Protocol 5.11 optional tool-assisted methodology, and all Protocol 5.4-5.11 engineering safeguards while making repeated evidence change the engineering method: normal local repair escalates to bounded semantic-family closure after material recurrence, and genuine same-family recurrence after adequate family closure requires bounded Design reconsideration before another ordinary patch cycle. The release also adds review readiness, acceptance liveness, proportionate blocker-family saturation, conditional finite-surface census, revision economy, and evidence/test-cycle reuse. These controls do not force acceptance, add a lifecycle role, make matrices or exhaustive scans universal, weaken independent review or affected regression/integration, or silently reinterpret older workplans.'''
ins('source/shared/references/protocol-versioning-and-compatibility.md','The two-role lifecycle remains unchanged:',V,'Protocol 5.12 is a backward-compatible')
rep('source/shared/references/protocol-versioning-and-compatibility.md','Active older workplans do not automatically adopt Protocol 5.11 or any other later release.','Active older workplans do not automatically adopt Protocol 5.12 or any other later release.')

rep('source/README.md','# Software Development Protocol 5.11','# Software Development Protocol 5.12')
rep('source/README.md','This directory is the canonical Protocol 5.11 source.','This directory is the canonical Protocol 5.12 source.')
old='Protocol 5.11 preserves all material Protocol 5.4-5.10 guarantees unchanged. It adds optional capability-aware tool-assisted engineering guidance for Serena semantic repository work, Semgrep structural/variant analysis, and Hypothesis property/stateful testing. These tools remain evidence and development instruments rather than generic dependencies, lifecycle gates, normative authority, or substitutes for affected regression and real-boundary integration. Protocol 5.10 snapshot-complete handoffs and Protocol 5.9 deterministic routing/distribution remain unchanged.'
new='Protocol 5.12 preserves all material Protocol 5.4-5.11 guarantees unchanged. It adds explicit development-convergence control: a first clean local defect remains local; material sibling recurrence triggers bounded semantic-family closure; and genuine same-family recurrence after adequate family closure requires bounded Software Design reconsideration before another ordinary patch cycle. Review readiness, acceptance liveness, proportionate blocker-family saturation, conditional finite-surface census, revision-number economy with snapshot-complete current-authority reconciliation, and evidence/test-cycle reuse reduce repeated discovery without reducing reviewer independence or functional acceptance. Protocol 5.11 optional capability-aware tool-assisted engineering guidance for Serena, Semgrep, and Hypothesis remains available as evidence/development methodology rather than a dependency or lifecycle gate.'
rep('source/README.md',old,new)
S='''## Convergent development

Protocol 5.12 keeps ordinary local work proportionate while making recurrence actionable. A recurring defect family is defined semantically by invariant/product claim, owner/authority, lifecycle/transition class, and failure mechanism—not by file names or broad subsystem labels. Family closure uses a bounded completeness basis and canonical owner repair; incomplete family closure is corrected rather than used to manufacture redesign. Recurrence after adequate family closure triggers Design reconsideration, which may either require same-design structural consolidation or reopen the affected frozen decision when evidence requires it.

Final independent review remains broad and evidence-directed. Implementation owns review readiness and systematic family closure; Review batches cheap/high-information sibling findings, has a bounded stopping rule, and does not turn missing implementation evidence into a new design revision. Ordinary implementation attempts do not require numbered authority snapshots, while genuinely new binding task semantics are still reconciled into current supplied authority before handoff.
'''
ins('source/README.md','## Build and repository acceptance',S,'## Convergent development')

rep('README.md','Protocol 5.11 preserves the complete two-role lifecycle and every material Protocol 5.4-5.10 engineering safeguard while adding optional capability-aware tool-assisted engineering methodology:','Protocol 5.12 preserves the complete two-role lifecycle and every material Protocol 5.4-5.11 engineering safeguard while adding explicit development-convergence and cycle-economy controls:')
rep('README.md','Protocol 5.11 preserves Protocol 5.10 snapshot-complete handoffs and Protocol 5.9 **canonical detailed ownership + deterministic progressive-disclosure routing** unchanged.','Protocol 5.12 preserves Protocol 5.11 optional tool-assisted methodology, Protocol 5.10 snapshot-complete handoffs, and Protocol 5.9 **canonical detailed ownership + deterministic progressive-disclosure routing** unchanged.')
RBL='''## Convergent development

The 5.12 convergence control keeps a first clean local defect local, but material sibling recurrence changes the unit of work to a bounded semantic defect family. Implementation establishes a family closure basis, repairs the canonical owner/mechanism, and proves family-level real-owner plus affected-regression/integration behavior. Genuine same-family recurrence after adequate family closure triggers bounded Design reconsideration before another ordinary sibling patch; reconsideration may preserve frozen design and require consolidation/refactoring rather than automatically creating a new normative revision.

Review readiness, acceptance liveness, proportionate blocker-family saturation, conditional finite-surface census, closure horizons, and revision-number economy reduce repeated rediscovery without making exhaustive scans, matrices, new roles, or fixed review counts universal. Independent review remains able to find material new issues, and genuinely new binding task semantics still enter canonical current authority before the next handoff.
'''
ins('README.md','## Build and repository acceptance',RBL,'## Convergent development')

rep('tests/test_protocol_contracts.py','def test_protocol_511_identity_and_two_role_lifecycle(self) -> None:','def test_protocol_512_identity_and_two_role_lifecycle(self) -> None:')
rep('tests/test_protocol_contracts.py','self.assertEqual("5.11.0", read("source/PROTOCOL_VERSION").strip())','self.assertEqual("5.12.0", read("source/PROTOCOL_VERSION").strip())')
rep('tests/test_protocol_contracts.py','self.assertIn("software development protocol 5.11", source_readme)','self.assertIn("software development protocol 5.12", source_readme)')
rep('tests/test_protocol_contracts.py','self.assertIn("protocol 5.11", root_readme)','self.assertIn("protocol 5.12", root_readme)')
rep('tests/test_protocol_contracts.py','self.assertIn("protocol 5.11 is a backward-compatible", versioning)','self.assertIn("protocol 5.12 is a backward-compatible", versioning)\n        self.assertIn("protocol 5.11 is a backward-compatible", versioning)')
rep('tests/test_protocol_contracts.py','self.assertIn("protocol 5.4-5.10 guarantees unchanged", source_readme)','self.assertIn("protocol 5.4-5.11 guarantees unchanged", source_readme)')

TEST='''from __future__ import annotations
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def r(p):return (ROOT/p).read_text(encoding="utf-8").lower()
class Protocol512ConvergenceTests(unittest.TestCase):
 def setUp(self):
  self.w=r("source/shared/references/workflow-and-workplans.md");self.t=r("source/shared/references/testing-and-validation.md");self.a=r("source/shared/references/architecture-and-design.md");self.i=r("source/shared/references/repository-intake.md");self.g=r("source/shared/references/tool-assisted-engineering.md");self.d=r("source/roles/software-design/SKILL.md");self.m=r("source/roles/software-implementation/SKILL.md");self.p=r("source/shared/templates/implementation_workplan_template.md")
 def test_identity_and_preservation(self):
  self.assertEqual("5.12.0",r("source/PROTOCOL_VERSION").strip());h="product engineering fitness > minimum justified product/system complexity > development economy";self.assertIn(h,self.d);self.assertIn(h,self.m);self.assertIn("software-design -> software-implementation",r("source/README.md"))
 def test_escalation_and_family_boundary(self):
  for x in ("a first clean local defect","family closure after recurrence","genuine family closure","bounded software design reconsideration","do not fragment","do not overaggregate"):self.assertIn(x,self.w)
  for x in ("protected invariant / required product claim","semantic owner or authority class","state / transition / lifecycle class","materially equivalent failure mechanism"):self.assertIn(x,self.w)
 def test_incomplete_family_is_not_automatic_redesign(self):
  self.assertIn("incomplete family closure",self.w);self.assertIn("remains implementation nonconformance",self.w);self.assertIn("normative design change is not predetermined",self.w);self.assertIn("does not automatically mean architecture churn",self.a);self.assertIn("complete/correct that family closure",self.m)
 def test_post_family_recurrence_reconsiders_design(self):
  self.assertIn("after a genuine family closure",self.w);self.assertIn("same family materially fails after an adequate family closure",self.m);self.assertIn("triggers bounded design reconsideration",self.d);self.assertIn("same authority",self.a)
 def test_census_is_bounded_and_conditional(self):
  self.assertIn("progressive evidence-directed inspection remains the default",self.i);self.assertIn("switch to a bounded census only when",self.i);self.assertIn("whole-repository inventory remains unnecessary",self.w);self.assertIn("not universal persistent traceability artifacts",self.i)
 def test_acceptance_liveness(self):
  for x in ("patched seam, failpoint, callback","trigger actually fired","real semantic owner","not a universal requirement to check out historical commits","known-positive and known-negative","structural/negative scans complement runtime acceptance"):self.assertIn(x,self.t)
 def test_review_readiness_and_non_refusal(self):
  for x in ("exact candidate identity","final complete affected-surface regression","real-boundary integration","not review-ready","not an automatic design revision","explicitly requested review still proceeds"):self.assertIn(x,self.w)
  self.assertIn("do not refuse an explicitly requested review",self.d);self.assertIn("review readiness is not a mechanism for refusing review",self.t)
 def test_review_saturation_and_stopping(self):
  for x in ("review characterizes and batches the family","implementation owns the systematic family closure","reviewer expansion stops","not proof that no conceivable repository defect exists"):self.assertIn(x,self.w)
  self.assertIn("proportionately saturate the directly implicated family",self.d);self.assertIn("evidence-directed sufficiency",self.d)
 def test_revision_economy_and_snapshot_completeness(self):
  for x in ("do not require a new numbered authority revision","reconcile that semantic into canonical current authority","snapshot completeness is preserved","concrete new sites"):self.assertIn(x,self.w)
  self.assertIn("ordinary implementation misses and review cycles do not require numbered authority revisions",self.d)
 def test_closure_horizon_and_template_are_not_ceiling_or_bureaucracy(self):
  self.assertIn("closure horizon",self.w);self.assertIn("it is not a scope ceiling",self.w);self.assertIn("conditional convergence guidance",self.p);self.assertIn("does not require a family matrix",self.p);self.assertIn("do not require ids, ledgers, persistent closure maps",self.p)
 def test_tools_remain_optional(self):
  self.assertIn("convergence-oriented composition",self.g);self.assertIn("optional tools",self.g);self.assertIn("tool absence does not relax family closure",self.g);self.assertIn("three-tool sequence mandatory",self.g);self.assertIn("tool availability alone is not a reason",self.g)
 def test_regression_integration_qualification_preserved(self):
  self.assertIn("stage-local affected regression",self.t);self.assertIn("stage-local affected regression",self.m);self.assertIn("final complete affected-surface regression",self.t);self.assertIn("integration/end-to-end",self.t);self.assertIn("production qualification is separate",self.m);self.assertIn("distinct from functional testing",self.t)
if __name__=="__main__":unittest.main()
'''
p=R/'tests/test_protocol_512_convergence.py'
if not p.exists() or p.read_text(encoding='utf-8')!=TEST:p.write_text(TEST,encoding='utf-8')
print('applied Protocol 5.12')
