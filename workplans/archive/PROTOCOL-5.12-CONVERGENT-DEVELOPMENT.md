---
kind: implementation-workplan
workplan_id: PROTOCOL-5.12-CONVERGENT-DEVELOPMENT
protocol_version: 5.11.0
target_protocol_version: 5.12.0
status: completed
completed_date: 2026-09-03
created_date: 2026-09-03
base_commit: 9cc44fc05732416bf8ca4744cf7ee68b54581ee4
review_source: mdstats-storage-io-reset-nonconvergence-postmortem
---

# Protocol 5.12 Convergent Development Workplan

## Objective and protected concerns

Strengthen Protocol 5 so substantial software work **converges deliberately** rather than accumulating repeated implementation/review cycles that repair one manifestation of an invariant at a time. Preserve the existing engineering doctrine, lifecycle, product-truth hierarchy, lossless handoff semantics, proxy-proof acceptance, affected-surface regression, independent review, and truthful non-closure while adding explicit mechanics that:

- detect non-convergent repair patterns early;
- force family-level closure rather than another instance-level patch when evidence shows recurrence;
- distinguish incomplete implementation handoff from a new design revision;
- make exhaustive/finite-surface reasoning available when correctness genuinely depends on complete coverage;
- operationalize the existing repeated-fix -> refactor/redesign doctrine;
- reduce redundant review, context loading, broad test reruns, authority churn, and rediscovery;
- preserve independent review's ability to discover material new defects without turning the accepted contract into an indefinitely expanding search process.

The intended refinement is:

```text
same Protocol 5.11 engineering doctrine and two-role lifecycle
+ explicit recurrence/family-closure escalation
+ review-readiness and exact-candidate discipline
+ proportionate finite-surface closure where exhaustiveness is itself a claim
+ blocker-family routing and revision-economy rules
+ delta/evidence/test reuse across repair cycles
-> fewer development cycles and less repeated work
-> earlier structural/root-cause repair
-> no reduction in engineering quality, robustness, or reviewer independence
```

### Evidence-grounded diagnosis

The motivating failure mode is not “implementation agents do no work.” In the observed storage/I/O case, implementation changed large production surfaces repeatedly and fixed many genuine defects. The failure was **poor convergence**: broad semantic invariants such as descriptor-pinned destructive authority, truthful mutation accounting, close/finalization semantics, and real-owner acceptance were repaired at particular call sites, while sibling manifestations survived elsewhere and were rediscovered by later independent reviews. Review revisions also mixed genuine contract changes with pure implementation nonconformance, authority-pointer/reseal bookkeeping, and evidence incompleteness, making iteration count appear even larger and creating more handoff material without necessarily increasing product information.

The protocol already contains most of the right principles:

- fix defects at the owning layer;
- treat the workplan as a minimum known contract rather than a ceiling;
- inspect beyond the workplan during independent review;
- use stage-local semantic plus functional closure;
- prefer consolidation when repeated fixes target one mechanism;
- reopen design when repeated fixes expose structural failure;
- optimize development economy only after engineering fitness is preserved.

The missing piece is a sufficiently explicit **control mechanism that converts repeated evidence into a different mode of work**. Without that mode switch, both Implementation and Design can truthfully follow existing prose while still producing the loop:

```text
find instance -> patch instance -> review -> find sibling instance
-> amend/reopen -> patch sibling -> review -> find another sibling -> ...
```

Protocol 5.12 must make the preferred loop:

```text
first defect -> owning-layer fix + proportionate variant consideration
recurrence after claimed closure -> family census + family-level repair + acceptance
same family after family closure -> bounded redesign/consolidation before more patching
```

### Protected concerns

1. **Preserve the governing product doctrine exactly.** Continue to optimize lexicographically as `product engineering fitness > minimum justified product/system complexity > development economy`. Cycle reduction never authorizes weaker correctness, scientific fidelity, security, durability, compatibility, performance, resource feasibility, or maintainability.
2. **Preserve the two-role lifecycle.** Keep `software-design -> software-implementation`; do not create a convergence role, verification role, test role, or process-manager role.
3. **Preserve truthful non-closure.** No cycle budget, recurrence count, review limit, or convergence target may force a pass. A candidate with a genuine blocker remains blocked.
4. **Preserve independent review.** Design may still inspect beyond the accepted plan and surface material new engineering risks. Convergence rules organize and route findings; they do not blind or scope-cap independent challenge.
5. **Preserve minimum-known-contract semantics.** Implementation must still incorporate newly discovered necessary consequences that preserve the accepted design. Protocol 5.12 may not turn the workplan into a ceiling or permit known affected consequences to be ignored merely to freeze scope.
6. **Preserve bounded redesign.** Reopen only the affected design surface and preserve unrelated accepted stages/evidence. Convergence escalation makes an existing redesign trigger operational; it does not normalize wholesale redesign.
7. **Preserve snapshot-complete handoffs.** Still-binding task semantics may not hide in chat, review history, tool state, or superseded artifacts. Convergence aids must not create a parallel hidden authority system.
8. **Preserve proxy-proof acceptance.** Real semantic-owner claims still require the real owner/path to execute. Family-level tests may use bounded doubles below/outside the owner but may not substitute for it.
9. **Preserve affected-surface regression and integration.** Structural census/negative scans strengthen completeness claims but never replace executable regression or assembled real-boundary integration.
10. **Preserve production-qualification separation.** Cycle minimization must not pull long production/GPU/HPC qualification into routine repair loops.
11. **No universal traceability bureaucracy.** Ordinary local work must remain lightweight. Persistent matrices, defect ledgers, manifests, reports, or provenance databases are not generic requirements. Temporary closure maps are allowed only when finite/exhaustive coverage materially establishes correctness or non-convergence has already demonstrated their value.
12. **No universal exhaustive repository scan.** Progressive evidence-directed intake remains the default. Exhaustive or census-style inspection is activated only for the bounded owner/failure family where completeness itself is material.
13. **Tools remain optional instruments.** Serena, Semgrep, Hypothesis, CodeQL, or other analyzers may accelerate convergence but do not become mandatory generic dependencies or authorities.
14. **Do not replace product simplicity with process complexity.** The refinement should add a small number of high-leverage decision rules, not a new lifecycle bureaucracy.
15. **Do not invalidate completed historical work retroactively.** Protocol 5.12 is backward-compatible. Existing workplans remain bound to their declared protocol versions unless explicitly upgraded.
16. **Do not count implementation attempts as design evolution.** A failed implementation may be repaired under the same accepted authority. New normative task semantics, not mere passage of another review cycle, determine whether the workplan/design authority changed.
17. **Preserve reviewer materiality.** Equivalent implementation preferences, speculative hardening, and unrelated pre-existing defects do not become blockers merely because review is broad.
18. **Reduce total engineering cost, not merely number of messages.** Optimize context, tool calls, test reruns, wall time, review passes, and human/model attention while retaining the evidence needed for a robust product.

## Scope freeze — Protocol 5.4-5.11 is preservation territory

Protocol 5.12 is a backward-compatible **development-convergence and cycle-economy control refinement**. It operationalizes already-existing Protocol 5 principles and adds no new product philosophy.

Preserve unchanged in normative meaning:

- the governing hierarchy and durable stakeholder-product objective;
- the two-role lifecycle and optional-specialist/non-gate model;
- accepted-workplan precedence, Frozen/Delegated/Reopen-only-on-evidence semantics, and local reconciliation;
- minimum-known-contract semantics;
- lossless Design -> Implementation translation and Protocol 5.10 snapshot completeness;
- coherent material stages and dual semantic/conformance plus functional closure;
- stage-local affected regression, final affected-surface re-derivation/regression, and assembled integration;
- proxy-proof semantic-owner/test-double boundaries;
- evidence reuse/invalidation;
- progressive repository intake and context economy;
- minimum justified product/system complexity and consolidation preference;
- anti-acceptance-gaming, self-correction, and truthful non-closure;
- production-qualification separation;
- Protocol 5.9 deterministic routing/distribution architecture;
- Protocol 5.11 optional capability-aware Serena/Semgrep/Hypothesis guidance.

Permitted additions are limited to mechanics that improve **convergence, completeness of repeated-family repair, review routing, review readiness, revision economy, evidence economy, and escalation to structural redesign** while preserving those semantics.

Prohibited under this workplan:

- a fixed maximum number of reviews after which work must pass;
- a rule that forbids independent review from reporting a genuinely material new issue;
- treating “scope stabilization” as permission to ignore newly affected behavior;
- mandatory persistent traceability matrices for normal tasks;
- mandatory use of Serena, Semgrep, Hypothesis, or any specific analyzer;
- a third lifecycle role or standing convergence committee/gate;
- universal full-suite execution after every edit;
- universal exhaustive repository scans;
- weakening stage-local regression, final regression/integration, or proxy-proof acceptance to save cycles;
- silently reclassifying a design deficiency as implementation nonconformance to avoid a revision;
- silently reclassifying implementation nonconformance as a new design revision merely to create a new plan artifact;
- using review-count reduction as a quality metric independent of product truth.

## Engineering envelope and product design

### 1. Convergence becomes an explicit process property

A substantial implementation is not convergent merely because each individual repair is reasonable. The process is convergent when repeated evidence causes the **unit of reasoning and repair to broaden appropriately** before another equivalent failure can be expected.

Protocol 5.12 defines three modes without creating new lifecycle stages or roles:

#### Mode N — normal evidence-directed development

Default for ordinary work and the first clean local defect.

Implementation:

- diagnoses the owning mechanism;
- fixes at the owning layer;
- performs normal semantic/conformance plus focused/affected regression closure;
- considers plausible sibling variants proportionately when the defect clearly represents a pattern rather than a one-off input.

No census, matrix, or special convergence artifact is required for a genuinely local defect.

#### Mode F — family closure

Activate when evidence shows that instance-level repair has not closed the material invariant/failure family. The next implementation cycle must close the **family**, not merely the newly reported site.

A family is defined by materially shared semantics, not textual similarity alone. Typical family dimensions are:

```text
protected invariant
+ semantic owner / authority boundary
+ state or transition class
+ failure mechanism / forbidden realization
```

Examples include all persistent mutation transitions owned by one executor family, all final destructive syscalls governed by one authorization invariant, all serialization readers governed by one compatibility rule, or all scheduler transitions governed by one cancellation/terminality state machine.

Mode F does not mean “scan the whole repository.” It means systematically establish and close the bounded family that recurrence proved was not safely handled by progressive instance-level inspection.

#### Mode R — bounded redesign/consolidation

Activate when the same material family remains nonconformant **after a Mode F family-closure attempt**, or when the Mode F census itself demonstrates duplicated/wrong ownership, parallel state machines, unsafe fallbacks, or another structural cause that makes reliable family closure through local repair unjustified.

Mode R requires Software Design to revisit the affected ownership/architecture/mechanism before further instance patches. Preserve unrelated accepted design and evidence.

This is the hard convergence guarantee:

```text
normal first defect
-> recurrence after claimed closure: family closure, not another instance patch
-> recurrence after family closure: bounded redesign/consolidation, not another family patch loop
```

No recurrence count can force acceptance; the escalation changes the engineering method, not the pass threshold.

### 2. Explicit triggers for family closure

Mode F is mandatory when any of the following materially occurs within the same active task or accepted subsystem repair:

1. Independent review finds a **sibling manifestation of an invariant/failure mechanism that Implementation already claimed to have closed**.
2. A second material local repair is needed in substantially the same semantic owner/failure mechanism and evidence suggests the sites are members of one pattern rather than independent bugs.
3. A required acceptance test is discovered to be vacuous, proxy-passing, patching a dead seam, or otherwise incapable of failing while the owner under acceptance is broken, and the weakness plausibly affects a family of claims rather than one isolated test.
4. A supposedly canonical safety/correctness primitive is bypassed by another production path with equivalent authority.
5. Review repeatedly finds the same class of stale fallback, duplicate authority, post-hoc inference, missing transition recording, cleanup/finalization loss, or other mechanism-level defect.
6. A local fix requires another wrapper/fallback/special case around the same owner instead of eliminating the diagnosed cause.
7. A finite set of authority-bearing, persistence-bearing, compatibility-bearing, mutation-bearing, or similarly critical sites must all satisfy one invariant and partial coverage would defeat the accepted product claim.

Mode F may also be selected proactively during initial design/implementation when the risk and finite surface make it cheaper than waiting for recurrence.

### 3. Explicit trigger for bounded redesign

Mode R is mandatory when:

- a material blocker in the same family survives or reappears after a documented Mode F closure attempt;
- the family census shows materially duplicated or contradictory ownership/state;
- reliable acceptance requires tests to substantially reconstruct the production owner in parallel;
- repeated fixes proliferate exceptional paths/fallbacks or increase total product complexity;
- the family cannot be bounded with sufficient confidence because the current architecture exposes too many uncontrolled entry points and a canonical owner can reasonably reduce that surface;
- another existing Protocol 5 redesign trigger fires.

Implementation must not respond to a post-Mode-F recurrence with “one more small patch” unless Design establishes that the new defect is genuinely independent of the closed family.

### 4. Family census and closure basis

When Mode F activates, Implementation must establish a **bounded closure basis** before claiming the family closed.

The closure basis answers:

1. What invariant/failure family is being closed?
2. What production semantic owner(s) actually carry that behavior?
3. What set or equivalence classes of call sites/transitions/consumers can exercise the family?
4. By what evidence is that set sufficiently complete for the claim?
5. What canonical realization should all applicable sites use?
6. What executable and structural evidence proves both positive behavior and absence of bypasses/variants?

Use the cheapest sufficiently reliable combination of:

- direct source inspection;
- symbol/reference/caller analysis;
- AST/static structural search;
- registration/configuration/entry-point inspection;
- persisted-schema or state-transition enumeration;
- generated-source inspection when relevant;
- focused runtime instrumentation or tests;
- other project-specific evidence.

Serena may accelerate semantic owner/reference enumeration; Semgrep may accelerate structural variant/negative scans; Hypothesis may generalize a concrete state/input failure into property/stateful coverage. Their absence does not weaken the closure requirement and does not itself block work.

#### Temporary closure map

Where completeness materially depends on covering a finite set, a temporary in-session or workplan-local closure map is explicitly allowed and may be required by the task plan. It can record, for example:

```text
site / transition class
semantic owner
binding invariant
current realization
canonical realization / disposition
acceptance evidence
```

This is a reasoning/evidence instrument, not a new generic persistent artifact. Persist it only when the project independently needs auditability/handoff durability or when the active workplan requires it because losing the census would materially reintroduce risk. Otherwise the final governed product/tests/source remain the durable authority.

### 5. Fix the family at the canonical owner

After the closure basis is understood, prefer one canonical implementation mechanism that makes sibling correctness the default rather than separately patching every caller.

Implementation must challenge whether the right correction is:

- centralizing the invariant in the semantic owner;
- replacing duplicated local helpers with one canonical primitive;
- eliminating a bypass/fallback;
- making state/transition truth explicit in the owning data structure;
- narrowing an API so invalid callers cannot express the unsafe path;
- consolidating ownership;
- deleting obsolete alternative machinery;
- introducing a small justified abstraction that removes several independent failure surfaces.

A family census does not require forced DRY. Materially distinct lifecycle/hardware/scientific paths may remain specialized when one abstraction would reduce fitness. But duplicated enforcement of the **same authority/invariant** is presumptively suspect after recurrence.

### 6. Acceptance must demonstrate liveness of the intended boundary

For a diagnosed bug or recurring family, acceptance should establish not merely that a helper returns the expected result, but that the intended production owner/path actually executes and would detect the failure.

Protocol 5.12 strengthens existing proxy-proof acceptance with **acceptance liveness**:

- when a regression relies on a patched seam/failpoint/callback, assert that the seam or failpoint actually fired when practical;
- when the claim is about a production transition, execute the real owner that performs the transition;
- when a structural guard claims “no bypass,” validate the search/rule against known-positive and known-negative constructs when the rule is acceptance-critical;
- when practical and cheap, demonstrate a new bug reproducer fails on the known-broken implementation or otherwise prove the counterfactual can distinguish broken from fixed behavior;
- for family closure, cover material equivalence classes/transition classes rather than mechanically writing one test per source site when one owner-level property genuinely covers them.

A test suite that could remain green while the same owner/family is broken is not sufficient family-closure evidence.

### 7. Review-readiness becomes an explicit handoff boundary

Independent review is high-value when it challenges a candidate that Implementation has actually completed. It is wasteful when Design repeatedly becomes the first actor to discover that mandatory implementation closure or evidence was never attempted.

Before Implementation requests/claims final independent review of executable work, the candidate must be **review-ready**. Review readiness requires, as applicable:

- exact candidate source identity (normally commit plus absence of unintended product-defining working-tree changes);
- final accepted-contract reconciliation completed;
- all known implementation obligations either satisfied, legitimately reconciled, or explicitly blocked by genuine redesign/unavailable acceptance;
- any triggered Mode F family closure completed with a sufficient closure basis;
- stage-local focused and affected-regression checks completed for material stages;
- final affected-surface re-derivation completed;
- final complete affected-surface regression and real-boundary integration executed on the assembled candidate after material executable edits that could invalidate them;
- repository/project-required checks executed;
- required structural/absence checks executed;
- material test/failpoint/patch liveness established where acceptance depends on it;
- known failures triaged rather than silently omitted;
- the final diff/current tree inspected for unintended/stale/fallback/complexity drift;
- unavailable required checks reported as unavailable rather than passed.

No mandatory standalone “review packet” file is created. Existing command output, CI, concise implementation completion reporting, source/tests, and the accepted workplan are sufficient unless project policy requires more.

If these prerequisites are materially absent, Software Design may inspect enough to identify the problem, but the normal routing is **implementation handoff incomplete / not review-ready**, not “invent a new design revision.” Missing execution evidence for an unchanged accepted obligation is implementation nonconformance, not automatically new task semantics.

This does not prevent Design from finding a genuine design deficiency while checking an unready candidate.

### 8. Independent review routes findings by semantic novelty, not cycle count

Independent review remains a challenge. Protocol 5.12 requires findings to be grouped and routed by their engineering meaning:

#### Existing-contract implementation nonconformance

The implementation failed to satisfy an already-binding requirement/invariant/acceptance boundary.

- Repair under the same accepted design/workplan authority.
- Do not create a new design/workplan revision solely because another implementation attempt is needed.
- If findings are sibling variants of one family, group them and trigger Mode F rather than issuing separate micro-repair plans.

#### Workplan/design deficiency

A still-binding material requirement, invariant consequence, acceptance boundary, or redesign trigger was absent/incorrect in current supplied authority.

- Amend/reconcile the affected current workplan/design.
- Preserve snapshot completeness.
- A normative revision is justified because the implementation contract actually changed.

#### New affected-surface material issue

Review discovers a material issue not previously known but plausibly caused by, exposed by, or materially interacting with the current change.

- Incorporate it as a necessary implementation consequence if it preserves frozen design.
- Reopen bounded design only when a frozen decision must change.
- Group it into an existing family when its mechanism/invariant matches rather than treating each site as a new design revision.

#### Unrelated pre-existing issue

A genuine problem is discovered but lies outside the current affected surface and does not undermine the current candidate's required product claim.

- Record/route it separately when worthwhile.
- It does not block current closure merely because independent review noticed it.
- Safety/security/data-loss issues may still intersect scope if the current change would expose or depend on them; classification must follow actual engineering impact rather than age alone.

### 9. Review should challenge the closure basis, not replay the whole investigation without cause

For long tasks, independent review starts from the highest-information current evidence, including the accepted authority, final candidate/diff, affected-surface derivation, family closure basis when present, and executed acceptance.

The reviewer remains free to broaden where evidence undermines a premise, but should avoid low-information archaeology or rediscovering unchanged facts merely because a new review cycle began.

After Mode F, review should specifically challenge:

- whether the family definition is materially correct;
- whether semantic ownership is correctly identified;
- whether the census/completeness basis could miss a material class;
- whether canonicalization actually removes bypasses;
- whether acceptance can fail when the owner is broken;
- whether structural negative evidence is scoped honestly;
- whether the final exact candidate passed the affected functional surface.

If those hold, review need not rescan settled, unrelated areas merely to search for another iteration. Genuine independent new findings remain valid.

### 10. Revision economy and authority identity

Protocol 5.12 explicitly separates **normative authority evolution** from **implementation attempts/review cycles**.

A workplan/design authority revision is warranted when still-binding task semantics change materially: requirements, frozen decisions, required consequences, acceptance boundaries, redesign triggers, or supplied current authority are corrected/extended.

A new authority revision is **not** warranted merely because:

- Implementation missed an existing obligation;
- a required test was not run;
- a regression failed;
- a review found another source site that violates an already-explicit invariant;
- an implementation attempt needs another patch;
- a docs/build derivative needs regeneration;
- a reviewer wants a clearer explanation that does not add/change binding semantics.

Projects may maintain revision snapshots for audit/concurrency needs, but Protocol 5 does not require one numbered authority artifact per implementation review. Git history already versions ordinary current workplan edits. Prefer one canonical current authority plus narrowly justified historical snapshots when they provide independent value.

Implementation attempts may be named in commits/branches/review notes when useful, but those labels are provenance, not normative protocol revisions.

This rule reduces both artifact churn and the cognitive illusion that every failed implementation is a new design.

### 11. Closure horizon prevents uncontrolled scope diffusion without making the plan a ceiling

For substantial work, Design should identify the expected **closure horizon**: the material owners, contracts, state/persistence boundaries, consumers, and invariant families plausibly affected by the accepted change. This remains provisional; final affected-surface derivation can expand it.

The closure horizon serves two purposes:

- it focuses Implementation and Review on surfaces with a plausible causal/contract chain;
- it provides a basis for classifying genuinely unrelated pre-existing findings separately.

It does **not** authorize ignoring evidence outside the initial horizon. When new evidence establishes a plausible affected chain, expand the horizon. When no such chain exists, do not indefinitely absorb unrelated repository defects into the active workplan.

### 12. Development-cycle economy becomes an explicit optimization concern

After engineering fitness and product simplicity are preserved, actors should minimize total development-cycle cost by choosing high-information ordering.

Preferred mechanics:

1. **Diagnose and reproduce before broad editing.** For a concrete bug, create or identify the cheapest discriminating reproducer/property when practical.
2. **Search variants before patching repeated patterns.** Once a pattern is established, a targeted semantic/structural sweep is cheaper than waiting for the next independent review to find siblings.
3. **Consolidate related fixes before broad reruns.** Do not run a full affected suite after each line edit when several edits form one coherent stage; use focused checks until the stage candidate is coherent, then stage-local affected regression.
4. **Use staged evidence cost.** Cheap compile/import/static/focused tests first, family-level affected regression next, cross-owner integration after local stability, and final complete affected-surface/broader regression once the assembled executable candidate is stable.
5. **Reuse unaffected evidence.** Do not rerun checks whose claims cannot plausibly change because of the latest edit; do rerun final affected functional acceptance after material executable changes.
6. **Review deltas, not sessions.** Carry forward settled facts, accepted stages, family closure bases, and still-valid evidence until a changed dimension invalidates them.
7. **Batch independent read-only discovery.** Combine/parallelize independent searches or checks where the harness/resources allow and doing so reduces turns without obscuring failures.
8. **Do not use broad low-information scans ceremonially.** Target known uncertainty/family first; broaden only when findings justify it or impact cannot otherwise be bounded.
9. **Do not micro-gate tightly coupled edits.** Preserve coherent stage granularity.
10. **Avoid exact-candidate churn.** Complete material executable edits before the final functional pass. Documentation-only/generated derivative changes do not automatically invalidate unrelated executable evidence; use normal evidence-invalidation rules.
11. **Perform one comprehensive closure review per review-ready exact candidate.** If blockers remain, Implementation should close all identified blocker families before requesting the next closure review rather than asking for micro-review after each patch, unless a specific high-risk intermediate boundary materially reduces rework.

These are economy rules subordinate to product truth. They reduce unnecessary cycles; they do not justify combining unrelated risky work or deferring known failures.

### 13. Workplan guidance for recurrence and finite coverage

Substantial workplans should record **task-specific convergence triggers** when repeated-family risk is material, especially for security/authorization, persistence/recovery, state machines, migrations/compatibility, resource managers, concurrency/orchestration, and destructive operations.

Do not add boilerplate triggers to every small plan. Where relevant, record:

- the semantic owner/invariant whose repeated failure would trigger Mode F;
- whether a finite/census-style closure basis is likely available;
- the condition that would require bounded redesign instead of another repair;
- task-specific real-owner acceptance/liveness constraints.

The implementation-workplan template should gain concise conditional guidance for this without making a matrix mandatory.

### 14. Tool-assisted convergence patterns

Protocol 5.11 tools remain optional. Protocol 5.12 adds convergence-specific use cases:

- **Serena:** identify semantic owner(s), callers/references, repeated helper implementations, and affected symbol chains for a Mode F census; use ordinary search/config inspection to cover dynamic limitations.
- **Semgrep:** turn a diagnosed unsafe/nonconforming construct into a focused variant scan; validate acceptance-critical rules against positive/negative fixtures; use zero-findings only within an explicit scan scope.
- **Hypothesis:** generalize a concrete input/state/transition bug into a bounded invariant/property/state machine so sibling states are discovered before review; preserve real-owner execution when that owner is the claim.

When another static/semantic/property tool provides the same engineering value, it may be used instead. Tool output remains evidence, not authority.

## Implementation obligations

### O1 — Make convergence escalation canonical in workflow/workplans

**Concern / rationale:** The current workflow permits repeated local repair and independent rediscovery without a hard mode switch even though repeated fixes are already recognized as a redesign signal.

**Required end state:** `source/shared/references/workflow-and-workplans.md` becomes the canonical owner of Mode N / Mode F / Mode R semantics, recurrence triggers, family closure, review readiness, finding routing, closure horizon, and revision economy.

**Required consequences / constraints:**

- Preserve the current two-role lifecycle and existing workplan authority semantics.
- State the first-recurrence family-closure rule and post-family-closure bounded-redesign rule clearly enough that agents cannot truthfully choose endless sibling patches.
- Define family closure as bounded and evidence-driven, not whole-repository exhaustiveness.
- Define review readiness without requiring a new persistent report artifact.
- State that implementation nonconformance does not by itself mint a new normative workplan revision.
- Preserve snapshot completeness when current task semantics actually change.
- Explain closure horizon as scope focusing/classification, not a ceiling.
- Preserve evidence reuse and coherent stage granularity.

**Acceptance evidence:** Protocol contract tests plus direct inspection must show all of these semantics are present in the canonical workflow reference and do not contradict minimum-known-contract, independent-review, or snapshot-completeness rules.

### O2 — Make repeated-family structural failure an actionable architecture rule

**Concern / rationale:** Architecture guidance currently says repeated fixes *should* trigger refactor/redesign, but the storage case demonstrated that this can remain advisory across many cycles.

**Required end state:** `source/shared/references/architecture-and-design.md` explicitly requires bounded architecture/ownership reconsideration when the same material family recurs after Mode F closure or when the census demonstrates duplicated/wrong authority.

**Required consequences / constraints:**

- Do not redesign a first clean local defect.
- Preserve evidence-backed bounded redesign and unrelated accepted work/evidence.
- Prefer consolidation/canonical ownership when recurrence shows duplicated invariant enforcement.
- Permit justified specialization where one abstraction would reduce engineering fitness.

**Acceptance evidence:** Text/contract tests distinguish first-local-defect repair, family closure, and post-family-closure redesign escalation.

### O3 — Add acceptance-liveness and review-readiness semantics to testing/validation

**Concern / rationale:** A test can be green while patching a dead seam, bypassing the owner, manually constructing result state, or never firing the intended failpoint; independent review then becomes the first real acceptance gate.

**Required end state:** `source/shared/references/testing-and-validation.md` adds acceptance-liveness guidance and the functional evidence portion of review readiness.

**Required consequences / constraints:**

- Preserve proxy-proof boundaries.
- Assert patched seam/failpoint/callback invocation when that invocation materially establishes the claim and it is practical.
- Prefer pre-fix bug-reproducer/counterfactual failure evidence when cheap and meaningful; do not make historical checkout testing universally mandatory.
- For family closure, test material equivalence/transition classes through the real owner instead of one helper per source site where owner-level coverage is stronger.
- Keep structural scans complementary to runtime testing.
- Preserve stage-local and final affected regression/integration requirements.
- Explicitly state that missing mandatory evidence means not-ready/incomplete acceptance, not pass.

**Acceptance evidence:** Contract tests include dead-seam/failpoint liveness wording and retain all existing proxy-proof/final-regression guarantees.

### O4 — Strengthen Software Implementation with family-first repair behavior

**Concern / rationale:** Implementation currently performs excellent owning-layer local fixes but can still stop after satisfying the explicitly named manifestation.

**Required end state:** `source/roles/software-implementation/SKILL.md` directs Implementation to recognize recurrence, establish the family closure basis, consolidate at the owner where justified, execute review-readiness acceptance, and request redesign after post-family recurrence.

**Required consequences / constraints:**

- Keep normal first-local-defect handling lightweight.
- On Mode F trigger, do not implement only the latest reported instance.
- Search plausible variants/callers/transitions before claiming closure.
- Use tools opportunistically, not mandatorily.
- Complete all blocker families from one review before requesting the next comprehensive closure review where dependencies permit.
- Preserve the rule that the workplan is a minimum known contract, not a ceiling.
- Preserve truthful non-closure and no forced pass.

**Acceptance evidence:** Skill contract tests and packaged-skill inspection show the new decision loop while retaining existing stage/final acceptance and ownership rules.

### O5 — Strengthen Software Design independent review with convergence routing

**Concern / rationale:** Review can correctly find defects yet accidentally transform each implementation miss into another design revision and restart broad investigation every cycle.

**Required end state:** `source/roles/software-design/SKILL.md` requires Design to group findings by invariant/owner family, distinguish implementation attempt failure from normative design change, trigger Mode F/Mode R as appropriate, check review readiness, and reuse settled evidence/deltas without weakening independent challenge.

**Required consequences / constraints:**

- Preserve broad independent engineering challenge.
- Existing-contract misses remain implementation nonconformance unless current authority is genuinely deficient.
- Sibling findings should be reported as one family-level closure problem plus concrete sites/evidence, not unrelated micro-plans.
- A post-Mode-F sibling blocker triggers bounded redesign/consolidation review.
- Unrelated pre-existing defects are separated unless materially coupled to the active product claim.
- Equivalent preferences remain nonblocking.

**Acceptance evidence:** Contract tests verify all routing distinctions and preservation of reviewer independence/materiality.

### O6 — Add finite-surface/census exception to progressive repository intake

**Concern / rationale:** Progressive inspection is correct by default, but when “every authority-bearing transition must satisfy invariant X” is itself the correctness claim, sampling until confidence feels adequate can perpetuate sibling misses.

**Required end state:** `source/shared/references/repository-intake.md` explicitly distinguishes ordinary progressive intake from bounded census-style inspection when finite/exhaustive coverage materially establishes a claim or Mode F has triggered.

**Required consequences / constraints:**

- Never require whole-repository inventory by default.
- Bound the census by semantic owner/failure family/affected chain.
- Require a stated completeness basis appropriate to dynamic/static limitations.
- If the family cannot be bounded confidently, escalate ownership/design or choose broader functional/property evidence rather than pretending a partial search was exhaustive.

**Acceptance evidence:** Tests/inspection confirm both progressive-default and bounded-census exception remain explicit.

### O7 — Extend tool-assisted engineering for convergence

**Concern / rationale:** Protocol 5.11 introduced the right tools but does not yet connect them directly to the repeated-family convergence mechanism.

**Required end state:** `source/shared/references/tool-assisted-engineering.md` adds concise Mode F patterns for semantic caller census, structural variant scans, and invariant/stateful generalization.

**Required consequences / constraints:**

- Preserve optional capability-aware use.
- Preserve Semgrep scan-scope/false-negative caveats and rule validation.
- Preserve Serena dynamic/reference limitations.
- Preserve Hypothesis oracle/real-owner constraints.
- Do not create a required three-tool pipeline.

**Acceptance evidence:** Existing tooling tests plus new protocol-contract assertions establish routing/content and optionality.

### O8 — Refine workplan template without adding generic bureaucracy

**Concern / rationale:** Plans need a place to preserve high-risk recurrence/redesign triggers and closure-horizon information when material, but adding universal matrices would violate Protocol 5.8 economy.

**Required end state:** `source/shared/templates/implementation_workplan_template.md` adds conditional guidance for:

- closure horizon when substantial scope can diffuse;
- recurrence/family-closure trigger when repeated-family risk is material;
- post-family-closure redesign trigger;
- finite closure map/census only when completeness itself is acceptance-critical.

**Required consequences / constraints:**

- Keep all additions conditional and concise.
- Do not require IDs/matrices/ledgers for ordinary work.
- Preserve current handoff closure and snapshot-loss counterfactual.

**Acceptance evidence:** Template tests/inspection show conditional rather than universal requirements.

### O9 — Add Protocol 5.12 versioning and top-level summary

**Concern / rationale:** The refinement changes generic protocol behavior for newly bound workplans and therefore requires a minor-version release.

**Required end state:**

- `source/PROTOCOL_VERSION` becomes `5.12.0`.
- `source/shared/references/protocol-versioning-and-compatibility.md` describes Protocol 5.12 as a backward-compatible development-convergence and cycle-economy control refinement preserving Protocol 5.4-5.11 doctrine.
- `source/README.md` and root `README.md` summarize the release at appropriate detail.

**Required consequences / constraints:**

- Existing workplans remain bound to their declared version.
- Do not silently reinterpret Protocol 5.11-or-earlier active/completed plans.
- Explicit adoption of 5.12 by an older active workplan requires reconciliation of new convergence/review-readiness obligations only where materially applicable; still-valid evidence remains reusable.

**Acceptance evidence:** Version/README/contract tests establish exact identity and compatibility wording.

### O10 — Add protocol regression tests for convergence invariants

**Concern / rationale:** The convergence mechanics themselves must not drift into either quality weakening or process bureaucracy.

**Required end state:** Add/extend repository tests to protect at least:

1. exact Protocol 5.12 version identity;
2. unchanged two-role lifecycle;
3. unchanged engineering hierarchy;
4. first clean local defect remains eligible for local owning-layer repair;
5. recurrence after claimed closure triggers family closure;
6. same-family recurrence after family closure triggers bounded redesign/consolidation;
7. family census is bounded/conditional, not universal repository exhaustiveness;
8. temporary closure maps are conditional and not mandatory persistent artifacts;
9. review readiness includes exact candidate, contract reconciliation, final affected regression/integration, and required evidence;
10. missing evidence is implementation nonconformance/not-review-ready rather than an automatic design revision;
11. implementation nonconformance alone does not require a new authority revision;
12. new task semantics still require current-authority reconciliation/snapshot completeness;
13. independent review remains broad and may find material new issues;
14. closure horizon is not a scope ceiling;
15. unrelated pre-existing issues are not automatically current blockers;
16. acceptance-liveness protects real-owner/patch/failpoint claims;
17. structural/static scans do not replace executable acceptance;
18. Serena/Semgrep/Hypothesis remain optional;
19. stage-local and final affected-surface regression/integration remain mandatory;
20. production qualification remains separate;
21. evidence reuse/context economy/coherent stage granularity remain intact;
22. no fixed review-count rule can force acceptance.

Tests should assert durable semantics rather than brittle exact paragraphs where possible.

### O11 — Regenerate and validate distributions from canonical source

**Concern / rationale:** Protocol users consume built skill bundles, not only canonical source.

**Required end state:** Rebuild supported skill distributions from canonical `source/` using the existing build machinery and validate package structure/metadata/reference reachability.

**Required consequences / constraints:**

- `software-design` and `software-implementation` packaged bundles include every newly referenced shared file required by their routes.
- Version metadata is 5.12.0 where appropriate.
- Generic Agent Skill and OpenAI adapter validation continue to pass.
- Generated packages correspond to canonical source and contain no machine-local caches/paths/credentials.
- Build/package changes do not become a new release architecture.

**Acceptance evidence:** Execute the repository's existing build/validation tooling, including `source/build_skills.py`, `source/validate_packages.py`, and affected packaging/tooling tests. Inspect the built software-design/software-implementation artifacts outside canonical source as existing release policy requires.

### O12 — Preserve historical protocol behavior through regression

**Concern / rationale:** A convergence release is especially prone to accidentally overconstraining old economy/proportionality rules or weakening truth/review rules in the name of fewer cycles.

**Required end state:** Existing Protocol 5.4-5.11 contract tests remain green except for intentionally updated version/summary assertions.

**Required consequences / constraints:**

- Do not weaken or delete earlier regression assertions simply because new wording makes them inconvenient.
- When a test must change because canonical ownership moved, preserve or strengthen the same semantic claim.
- Do not make completed archived workplans normative for current semantics; they remain historical evidence.

**Acceptance evidence:** Full repository test suite plus targeted comparison of affected doctrine owners.

## Implementation authority

### Frozen

The following are frozen for Protocol 5.12 implementation:

- target version `5.12.0` and classification as a backward-compatible minor refinement;
- exact two-role lifecycle;
- governing engineering hierarchy;
- truthful non-closure/no forced pass;
- broad independent review authority with materiality;
- workplan minimum-known-contract semantics;
- snapshot-complete current authority;
- proxy-proof real-owner acceptance;
- stage-local and final affected regression/integration;
- production qualification separation;
- progressive intake as the ordinary default;
- Mode N -> Mode F -> Mode R escalation semantics;
- recurrence after claimed closure of the same material family requires family-level closure rather than another isolated patch;
- same-family recurrence after a genuine family-closure attempt requires bounded redesign/consolidation unless independently shown to be outside that family;
- review readiness as an Implementation responsibility before normal final independent review;
- implementation nonconformance does not by itself require a new normative authority revision;
- finite/census reasoning and temporary closure maps are conditional tools, not universal artifacts;
- closure horizon is a focusing/classification aid, not a workplan ceiling;
- optional status of Serena/Semgrep/Hypothesis and other analysis tools;
- no fixed review/cycle count can force acceptance.

### Delegated

Implementation may choose, while preserving frozen semantics:

- exact wording placement among canonical references and compact skill entrypoints;
- whether “Mode N/F/R” labels survive into final prose or are replaced by clearer equivalent terminology;
- test organization/file names and assertion granularity;
- whether temporary family closure evidence is represented as prose, a table, comments, or ephemeral working notes where persistence is not independently required;
- exact examples used to explain family closure;
- exact packaging commands within the repository's existing supported build path;
- minor editorial compression that preserves all protected concerns and required consequences.

### Reopen only on evidence

Reopen the affected design surface if implementation proves that:

- the N/F/R escalation cannot be expressed without materially changing the two-role lifecycle;
- review readiness cannot be enforced without a new persistent artifact or role and no lower-complexity equivalent exists;
- distinguishing normative authority revisions from implementation attempts conflicts with an existing mandatory repository/project authority mechanism;
- a first-recurrence family-closure trigger causes demonstrable material overreach on common local work that cannot be solved by better family-definition wording;
- post-family recurrence cannot reliably distinguish structural failure from genuinely independent defects;
- distribution/package architecture prevents portable inclusion of the new canonical guidance;
- another frozen Protocol 5.4-5.11 guarantee cannot coexist with these mechanics.

A wording inconvenience, test update, or preference for a different process architecture is not a redesign trigger.

## Affected surface and task-specific acceptance

### Canonical source expected to change

At minimum:

```text
source/PROTOCOL_VERSION
source/README.md
README.md
source/roles/software-design/SKILL.md
source/roles/software-implementation/SKILL.md
source/shared/references/workflow-and-workplans.md
source/shared/references/testing-and-validation.md
source/shared/references/architecture-and-design.md
source/shared/references/repository-intake.md
source/shared/references/tool-assisted-engineering.md
source/shared/references/protocol-versioning-and-compatibility.md
source/shared/templates/implementation_workplan_template.md
```

Potentially affected if current build/routing ownership requires it:

```text
source/build_skills.py
source/validate_packages.py
tests/test_protocol_contracts.py
tests/test_protocol_tooling.py
other existing protocol/version/workplan lifecycle tests
```

Generated distributables derived from `source/` are affected through normal build/regeneration policy.

### Required task-specific acceptance

#### Doctrine preservation

Demonstrate that Protocol 5.12 has not changed:

- engineering hierarchy;
- two-role lifecycle;
- product-truth/anti-gaming semantics;
- minimum-known-contract and snapshot-complete handoff;
- independent-review breadth;
- proxy-proof acceptance;
- stage-local/final affected regression/integration;
- evidence reuse/invalidation;
- qualification separation;
- Protocol 5.11 tool optionality.

#### Convergence behavior

Tests and source inspection must establish the escalation ladder with counterfactual distinctions:

```text
first clean local defect -> local owning-layer repair remains permitted
sibling recurrence after claimed closure -> family closure required
same-family blocker after family closure -> bounded redesign required
```

The test suite should make it difficult for future edits to collapse all three cases into either “always local patch” or “always redesign.”

#### Review routing

Establish that:

- not-review-ready/missing-evidence remains implementation nonconformance under unchanged authority;
- a genuinely deficient current workplan still requires reconciliation;
- implementation misses do not mechanically mint normative revisions;
- materially new affected-surface issues remain discoverable/in-scope;
- unrelated pre-existing issues can be routed separately;
- review independence and materiality remain intact.

#### Economy behavior

Establish that:

- family census/closure maps are conditional;
- progressive inspection remains default;
- full-suite-after-every-edit is not required;
- final affected regression/integration remains fresh after material executable changes;
- evidence reuse and delta-based review remain valid;
- no review-count quota forces acceptance.

#### Distribution

Build and validate all materially affected skill packages and version metadata from canonical source.

Production qualification: **unnecessary**. Protocol 5.12 changes methodology/text/tests/packaging, not a target-machine performance claim. Repository build/test/package validation is sufficient.

## Implementation sequence and convergence gates

### Stage A — Canonical workflow/convergence semantics

Implement O1, O2, and the core review-routing/revision-economy semantics first in canonical shared references.

Before dependent role/template work:

- inspect for contradictions with minimum-known-contract, snapshot-complete handoff, evidence-directed review, and bounded redesign;
- run focused protocol tests covering workflow/architecture semantics;
- ensure first-local-defect proportionality remains intact.

### Stage B — Acceptance/repository/tool mechanics

Implement O3, O6, and O7.

Close:

- acceptance liveness;
- review-readiness evidence;
- bounded census exception;
- tool-assisted family discovery.

Run focused and affected regression for testing/tooling/reference-contract behavior.

### Stage C — Role decision loops and workplan template

Implement O4, O5, and O8.

The role entrypoints should remain compact: route detailed convergence mechanics to canonical references while retaining the high-salience mode-switch/decision rules needed to prevent an agent from missing them.

Run skill/package reference-reachability and protocol contract tests.

### Stage D — Version/release integration

Implement O9, O10, O11, and O12.

- update 5.12 identity/README/versioning;
- complete regression protection;
- rebuild/validate distributions;
- run complete repository tests.

### Final assembled closure

Before declaring Protocol 5.12 implemented:

1. Reconcile every obligation O1-O12 against the exact candidate.
2. Re-derive the final affected source/test/distribution surface.
3. Inspect for doctrine drift, duplicate convergence authority, newly mandatory bureaucracy, accidental tool hard dependencies, hidden authority, or weakened acceptance.
4. Run all focused Protocol 5.12 tests.
5. Run the complete repository test suite.
6. Rebuild supported distributions from canonical source.
7. Validate built packages/adapters/reference reachability and version identity.
8. Run source/generated parity or repository-required diff checks.
9. Inspect the exact final candidate for unintended changes.
10. Rerun affected final checks after any material executable/build/test-framework changes that could invalidate them.

No live production qualification is required.

## Design-review challenges for the next pass

Before freezing this workplan for implementation, the next Software Design review should specifically challenge:

1. Whether first-recurrence -> family closure is early enough to prevent churn without over-triggering on genuinely independent local bugs.
2. Whether post-family recurrence -> bounded redesign is sufficiently hard to prevent another endless family-patch loop while still allowing evidence that a new defect is independent.
3. Whether “family” and “closure basis” are precise enough for agents to act consistently across state machines, persistence, security, scientific, concurrency, and performance domains.
4. Whether review-readiness can reduce wasted review cycles without becoming a new approval/report bureaucracy.
5. Whether revision economy preserves Protocol 5.10 snapshot completeness when a reviewer discovers a new still-binding consequence.
6. Whether closure horizon cleanly separates affected-surface expansion from unrelated repository bug absorption.
7. Whether acceptance-liveness wording remains proportionate and does not create universal historical mutation testing or one-test-per-site requirements.
8. Whether the workplan/template additions remain effectively compressed and canonically owned rather than spreading convergence prose across every skill/reference.
9. Whether the final test plan can prove both convergence strengthening and preservation of older quality guarantees.

## Handoff closure

This draft preserves the motivating requirements and their known consequences:

```text
observed repeated implementation/review churn
+ genuine evidence of substantial implementation progress
+ recurring sibling manifestations of the same invariant families
+ repeated acceptance/evidence gaps
+ authority-revision inflation
+ existing Protocol 5 repeated-fix/redesign and development-economy doctrine
-> explicit convergence escalation
-> bounded family census and canonical owner repair
-> acceptance-liveness and review-readiness
-> family-based review routing and revision economy
-> bounded redesign after failed family closure
-> delta/evidence/test reuse
-> preserved independent review and engineering quality
```

No protected concern is intentionally delegated to implementation discovery. The current plan remains `status: active` pending an independent closure review before it is frozen for implementation.

Apply the Protocol 5.10 snapshot-loss counterfactual at freeze time: the final supplied current workplan plus current Protocol 5.11 source authorities must recover every still-binding Protocol 5.12 target decision, preservation rule, acceptance boundary, and redesign trigger without relying on this conversation or the mdstats review history. The mdstats history is motivating evidence, not normative authority for Protocol 5.12.
