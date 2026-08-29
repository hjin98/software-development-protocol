---
kind: implementation-workplan
workplan_id: PROTOCOL-5.8-EFFECTIVE-COMPRESSION
protocol_version: 5.7.0
target_protocol_version: 5.8.0
status: completed
completed_date: 2026-08-29
created_date: 2026-08-26
base_commit: cf80643d80dd9ff667c26a8be84310874b19b15d
---

# Protocol 5.8 Effective Compression Workplan

## Objective and durable success criterion

Refactor Protocol 5.7's control plane so agents receive a smaller, higher-salience, progressively disclosed instruction set while preserving every material engineering doctrine and historical failure-mode defense established through Protocols 5.4-5.7.

Protocol 5.8 is a semantic-consolidation release, not a relaxation of engineering requirements and not a new lifecycle. Its target state is:

```text
Protocol 5.7 engineering semantics and failure-mode protection
+ materially lower always-loaded instruction duplication
+ clearer role-local decision loops
+ canonical detailed ownership of generic rules
+ task-specific workplans that preserve design intent without copying protocol prose
= equal-or-better engineering reliability with lower avoidable reasoning/context/process cost
```

The governing hierarchy remains exactly:

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Efficiency gains are acceptable only inside the solution/process space that preserves the stakeholder's durable product outcome and the confidence required to establish it.

## Diagnosis and protected concerns

Protocol 5.7 is semantically mature but its always-loaded lifecycle entrypoints and surrounding control-plane surfaces have accumulated overlapping explanations of genuine safeguards introduced in 5.5-5.7. Protocol 5.4 intentionally reduced repeated reasoning, workplan boilerplate, micro-gating, broad reference loading, evidence reruns, and review rediscovery; later fidelity, proxy-proof acceptance, and engineering-stewardship revisions fixed real failure modes but partially regrew the control plane.

The defect to correct is therefore not excessive software-engineering rigor. It is excessive duplication and cognitive competition among safeguards that should remain fully normative but need not all be restated in every lifecycle entrypoint, template, README, and test.

Protected concerns:

1. **No semantic regression.** Compression must not remove, weaken, ambiguate, or hide a material 5.4-5.7 doctrine or historical failure-mode defense.
2. **No attention inversion.** Protocol administration must not become more salient than solving the actual software problem.
3. **No hidden-reference failure.** A rule moved out of an entrypoint must retain an unmistakable role-local invariant/trigger when losing salience could change behavior.
4. **No boilerplate migration.** Duplication removed from `SKILL.md` must not simply reappear in `AGENTS.md`, README, workplan templates, tests, or a newly created generic manual.
5. **No weak fast path.** Proportionality may reduce ceremony and repeated execution, never affected-surface coverage, conformance, real-boundary integration, or required evidence.
6. **No micro-gating by ambiguity.** One coherent local behavior change should normally be one implementation stage; split stages only at material behavior/risk/dependency boundaries.
7. **No benchmark bureaucracy.** Protocol-effectiveness measurement is valuable evidence, not a new permanent lifecycle role, mandatory task ledger, telemetry system, or universal release subsystem.
8. **No arbitrary compression target.** Entry-point size is a diagnostic and design objective, not an acceptance substitute; semantic correctness and observed behavior govern release.

## Engineering envelope

Protocol 5.8 must preserve or strengthen all material guarantees currently present in Protocol 5.7, including the following historical lineage.

### Protocol 5.4 development-economy guarantees

- exact lexicographic hierarchy: engineering fitness, then minimum justified product/system complexity, then development economy;
- two-role lifecycle: `software-design -> software-implementation`;
- progressive, evidence-directed repository inspection;
- lowest-cost/high-information next action and established-fact reuse;
- still-valid evidence reuse with claim-based invalidation;
- coherent stage granularity rather than helper/file micro-gates;
- mandatory stage-local affected regression for each material executable stage;
- final affected-surface re-derivation, regression, integration, and repository-required checks;
- bounded redesign that reopens only the invalidated surface and preserves still-valid work/evidence;
- version-bound workplan inheritance;
- independent review without automatic replay of settled design reasoning;
- production qualification separate from ordinary functional acceptance;
- no mandatory persistent process/evidence/token-accounting bureaucracy.

### Protocol 5.5 implementation-fidelity guarantees

- substantial Design -> Implementation handoff is lossless with respect to material task-specific intent;
- protected concern/root failure mode remains recoverable downstream;
- required outcome/constraint, required implementation consequence, suggested realization, and delegated mechanics remain distinguishable;
- accepted workplan remains a minimum known contract, not a ceiling on newly discovered necessary consequences;
- every material implementation stage requires semantic/conformance closure plus functional closure;
- green tests do not prove an omitted accepted obligation was implemented;
- final accepted-contract reconciliation precedes/augments final functional acceptance;
- structural/absence evidence remains available for removal, uniqueness, no-legacy-path, and similar claims;
- independent review uses contract/outcome conformance plus independent engineering challenge;
- reviewer findings remain lossless/actionable and route as implementation nonconformance, workplan/design deficiency, or new independent issue.

### Protocol 5.6 proxy-proof acceptance guarantees

- material acceptance identifies the production semantic owner/consumer boundary when that owner materially constitutes the claim;
- acceptance evidence cannot close a claim by mocking, bypassing, reimplementing, precomputing, or seeding past the semantic owner under acceptance;
- bounded test doubles remain allowed below/outside that real boundary, including expensive ML/scientific computation, accelerators, external services, and reduced/synthetic data;
- direct helper calls cannot substitute for required production caller/orchestrator/reconciler/state-transition behavior;
- inability to exercise a frozen real-owner boundary is an unavailable/blocking check or evidence-backed redesign condition, not a proxy pass;
- targeted anti-bypass structural checks remain available when a task-specific risk justifies them, without introducing a global anti-mocking framework.

### Protocol 5.7 engineering-stewardship guarantees

- every actor optimizes for the stakeholder's intended durable product rather than the appearance of satisfying tests, workplans, gates, metrics, reviews, or reports;
- requirements are interpreted non-adversarially according to their protected engineering purpose;
- acceptance-signal gaming is forbidden, including weakening/deleting affected assertions, narrowing fixtures to avoid a known failure, laundering buggy output into expectations, swallowing failures, adding unjustified permissive fallbacks, or rewriting specifications merely to bless defective implementation;
- truthful non-closure is preferable to counterfeit completion;
- self-correction, evidence invalidation, rollback of unsound work, and bounded reopening are positive engineering behavior;
- implementation/design/review consider the material operational and maintenance horizon without authorizing unrelated gold-plating;
- independent review may identify a materially deficient accepted contract rather than accepting literal conformance that defeats the stakeholder outcome.

### Repository and packaging constraints

- `source/` remains canonical and generated `dist/` packages are regenerated rather than hand-edited;
- root routing surfaces remain concise and authoritative;
- repository tests, package build/validation, committed-dist parity, and `git diff --check` remain required release checks;
- Protocol 5.8 must remain usable across supported agent hosts without model-specific Terra/Sol/Claude/etc. policy.

## Governing product design

### 1. One canonical detailed owner plus salient triggers

For generic doctrine, prefer one canonical normative detailed owner plus concise invariant/decision-rule/trigger language in lifecycle entrypoints. Intentional duplication is reserved for high-salience invariants whose absence from a role entrypoint could materially change behavior.

Canonical detailed ownership should remain aligned with existing architecture unless implementation evidence proves a better owner is necessary:

| Material surface | Canonical detailed owner |
| --- | --- |
| lifecycle, workplans, authority, stages, handoff, review routing | `source/shared/references/workflow-and-workplans.md` |
| regression/integration, evidence reuse, proxy-proof acceptance, qualification | `source/shared/references/testing-and-validation.md` |
| diagnosis, ownership, architecture, algorithms, complexity, redesign | `source/shared/references/architecture-and-design.md` |
| progressive inspection, information gain, context economy | `source/shared/references/repository-intake.md` |
| protocol/workplan version inheritance | `source/shared/references/protocol-versioning-and-compatibility.md` |
| domain-specific concerns | existing specialist references |
| task-specific frozen decisions, consequences, acceptance boundaries | governing accepted workplan |

Do not create a new generic `core-doctrine`, `compression`, `development-economy`, or equivalent reference merely to relocate duplicated prose unless repository evidence demonstrates a genuinely distinct semantic owner.

### 2. Entrypoint-critical invariants

Both lifecycle entrypoints must retain, compactly and directly:

- stakeholder durable-product truth over acceptance appearance;
- exact governing hierarchy;
- non-adversarial interpretation/protected engineering purpose;
- evidence honesty and truthful non-closure;
- scope expansion through material ownership/impact evidence rather than speculative adjacency;
- a clear trigger that generic detailed rules are loaded only when their owned surface becomes material.

Role-specific hard requirements remain directly visible where losing them would materially weaken behavior.

### 3. `software-design` target structure

Compress Design around the actual role loop:

```text
diagnose real path/root cause
-> define material engineering envelope
-> choose globally justified product design
-> freeze material decisions and delegate local mechanics
-> translate task-specific intent losslessly
-> design proportionate acceptance
-> independently review when warranted
```

Keep directly visible:

- fix/understand the owning mechanism before adding wrappers/fallbacks/special cases;
- global product optimization and justified product-complexity discipline;
- `Frozen / Delegated / Reopen only on evidence`;
- lossless handoff invariant: material concern, required end state, already-known implementation consequence/constraint, and acceptance claim must remain recoverable without implementation reconstructing the design search;
- required consequence vs suggestion/delegation distinction;
- non-negotiable functional acceptance skeleton: focused checks, stage-local affected regression, final affected-surface re-derivation/regression, real-boundary integration, repository-required checks;
- proxy-proof trigger when a claim depends on a real semantic owner;
- independent review as contract/outcome challenge plus independent engineering challenge, with evidence-directed breadth and bounded routing.

Move detailed edge cases/examples to canonical references rather than restating them.

A Design entrypoint near the Protocol 5.4 cognitive footprint (roughly 9-11 KB) is a useful design objective, not a release requirement.

### 4. `software-implementation` target structure

Compress Implementation around the role loop:

```text
understand accepted target + real repository owner
-> implement one coherent material change
-> semantic/conformance closure
-> focused + affected regression
-> repeat only for another genuine material stage
-> final accepted-contract reconciliation
-> final affected regression + real-path integration
```

Keep directly visible:

- progressive intake, plausible affected surface, and established-fact reuse;
- accepted-workplan authority;
- required outcome/consequence vs suggestion/delegation;
- implementation realization / local reconciliation / evidence-backed material redesign;
- minimum-known-contract semantics for newly discovered necessary consequences;
- fix the owning layer, prefer cohesive ownership/one authority/semantic reuse, and avoid materially inferior algorithms or unjustified sophistication;
- semantic/conformance plus functional stage closure;
- stage-local affected regression and final assembled acceptance;
- real semantic-owner acceptance trigger;
- product-truth guardrails: no acceptance manipulation, no swallowed failures/counterfeit success, self-correction allowed/required when evidence becomes unsound;
- production qualification separation and resource honesty.

Detailed examples and edge-case mechanics route to canonical references.

An Implementation entrypoint near 10-12 KB is a useful design objective, not a release requirement.

### 5. Progressive-disclosure references

Reference routing must explicitly mean:

> Load a reference when a material question enters its ownership domain; start with the relevant section and broaden only when cross-cutting evidence requires it.

Do not require full-reference loading merely because a reference is packaged. Preserve concise section indexes for long references when that materially enables targeted reading. Do not use context minimization to omit plausible affected behavior or material evidence.

### 6. Compressed task workplans without lossy handoff

Simplify the default substantial workplan around six conceptual surfaces:

1. Objective + protected concerns.
2. Engineering envelope + chosen product design.
3. Implementation obligations.
4. Implementation authority.
5. Affected surface + task-specific acceptance.
6. Sequence + material risks/redesign triggers.

Ordinary material obligations should normally be expressible as:

```text
Concern
-> Required end state
-> Required consequences / constraints
-> Acceptance evidence
```

Attach only when material:

- suggested realization;
- semantic-owner/test-double acceptance boundary;
- stage/dependency;
- anti-shortcut/integrity constraint.

Do not require empty fields or ceremonial matrices. Generic protocol doctrine is inherited from the workplan's declared `protocol_version`; later releases do not silently reinterpret older plans.

Retain a compact handoff-closure requirement ensuring no material explicit requirement, protected concern, frozen design decision, known cross-module consequence, or required acceptance claim disappears during compression.

### 7. Stage proportionality

Make the default interpretation explicit:

> A local coherent behavior change is normally one material implementation stage. Split stages only where validating an intermediate behavior/risk/dependency boundary materially reduces downstream risk or rework.

Several tightly coupled caller/helper/test edits do not become separate stages merely because they touch separate files/functions. This changes process granularity, not required regression breadth.

### 8. Completion-report proportionality

Completion reports must include the evidence needed to interpret product/conformance status without requiring empty protocol categories. Report material changes, relevant deviations/reconciliations, tests/checks actually executed, unavailable/blocking required checks, and unresolved material risks. Report performance/qualification/docs/redesign sections only when materially relevant.

### 9. Protocol contract tests should enforce ownership, not duplication

Refactor tests that currently encourage repeated wording across multiple files.

For each doctrine:

- assert detailed semantics in its canonical owner;
- assert only the indispensable invariant/trigger at the lifecycle entrypoint(s);
- preserve direct tests for genuinely entrypoint-critical hard rules;
- avoid requiring detailed doctrine to appear verbatim in multiple files solely to make tests green.

Add lightweight protection against control-plane regrowth: expose/compare relevant entrypoint and package text-size statistics or equivalent diagnostics, but do not impose arbitrary hard byte/word/token limits. Material always-loaded growth should require an engineering justification rather than silently accumulating.

### 10. Historical failure-mode scenario validation

Add or extend deterministic protocol tests/fixtures so the compressed semantics clearly preserve expected decisions for representative historical failure modes. At minimum cover:

1. green tests plus omitted accepted obligation -> incomplete;
2. downstream helper invocation replacing required production caller/reconciler -> proxy acceptance rejected;
3. expensive ML/scientific dependency faked below a real state/decision owner -> allowed;
4. stale suggested mechanic but equivalent repository-local realization preserving frozen semantics -> local reconciliation allowed;
5. representative evidence invalidates frozen scaling/architecture premise -> bounded redesign;
6. failing check could be made green by weakening fixture/specification -> product/evidence repair required, not signal manipulation;
7. agent discovers its own earlier patch/evidence is unsound -> invalidate/repair/retest rather than defend sunk work;
8. small localized defect with clear ownership -> no unnecessary substantial-work ceremony or multi-stage decomposition;
9. several tightly coupled edits forming one behavior -> one coherent stage unless an independent risk boundary exists;
10. newly discovered affected consumer/consequence preserving frozen design -> incorporate and validate without unrelated design reopening;
11. removal/unique-authority claim with green runtime behavior but stale structural path remaining -> claim remains unclosed without appropriate structural/absence evidence;
12. literal workplan compliance that defeats the stakeholder's durable outcome -> review rejects/diagnoses contract or implementation deficiency rather than accepting the green surface.

Prefer repository-level deterministic contract/scenario tests over creating an agent benchmark framework inside the protocol repository.

### 11. Effectiveness evidence without a new bureaucracy

When a reproducible model/task execution harness is available at reasonable cost, compare Protocol 5.7 with the 5.8 candidate on representative fixed tasks using identical model/configuration/repository snapshots and evaluate, where observable:

- functional completion;
- independent-review defects;
- design/workplan drift;
- proxy/false-green acceptance;
- escaped affected regressions;
- unnecessary changed surface;
- redesign/rework cycles;
- tool/test executions;
- context/input/output tokens;
- end-to-end completion rate.

Correctness and historical failure-mode protection are non-inferiority constraints; process/token economy is optimized only after those constraints hold.

If reproducible live-agent benchmarking is unavailable or would require substantial new infrastructure, do not create a permanent benchmark subsystem merely to close this release. Instead report the limitation and rely on semantic ownership tests, historical scenario regression, deterministic repository acceptance, structural size/duplication analysis, and independent review. In that case describe the release as semantics-preserving effective compression rather than claiming empirically proven model-level success-rate improvement.

## Implementation authority

### Frozen

- Target protocol version is 5.8.0 and the governing workplan version is 5.7.0.
- Protocol 5.8 is a semantic/control-plane consolidation; no material Protocol 5.7 engineering doctrine is intentionally removed or weakened.
- Lifecycle remains exactly `software-design -> software-implementation`; independent review remains Design mode, not a third role.
- The governing hierarchy and stakeholder-product-truth doctrine remain unchanged.
- Mandatory stage-local affected regression, final affected-surface regression/integration, repository-required checks, lossless handoff, semantic/conformance closure, proxy-proof semantic-owner acceptance, bounded redesign, and truthful non-closure remain mandatory where currently material.
- Full production qualification remains separate from routine functional acceptance.
- `source/` remains canonical; `dist/` remains generated.
- No new mandatory persistent ledger/database/evidence manifest, task-classification bureaucracy, token accounting regime, model-specific policy, universal anti-mocking framework, or permanent agent-benchmark subsystem may be introduced solely for this revision.
- Generic doctrine should have one canonical detailed owner wherever practical; lifecycle entrypoints retain the invariant/decision rule/loading trigger needed for salience.
- Process proportionality may reduce ceremony and redundant execution, never engineering coverage or confidence.

### Delegated

Implementation may choose exact wording, section organization, test factoring, section indexes, and locally appropriate consolidation mechanics provided the frozen semantic guarantees remain unambiguous and canonical ownership is cleaner than Protocol 5.7.

Exact entrypoint byte/token reduction is delegated. The approximate 9-11 KB Design and 10-12 KB Implementation ranges are diagnostics/objectives only. Equivalent or better compression outside those ranges is acceptable; materially smaller reduction must be independently justified by semantic necessity and still demonstrate control-plane simplification.

Implementation may choose whether historical failure-mode scenarios are expressed as direct text-contract tests, compact decision fixtures, or another lightweight deterministic form, provided they test semantics/ownership rather than merely duplicating prose.

### Reopen only on evidence

Reopen the affected design surface if:

- a material 5.4-5.7 doctrine cannot be preserved with one canonical owner plus concise role triggers without becoming behaviorally ambiguous;
- consolidation exposes a genuine conflict between historical doctrines rather than mere duplicated wording;
- current packaging/host behavior requires more direct entrypoint detail than assumed to reliably load the canonical reference;
- deterministic scenario tests demonstrate that a proposed compression permits a historical failure mode;
- controlled effectiveness evidence, when available and valid, shows a material correctness/completion regression attributable to compression;
- a proposed anti-duplication test or size diagnostic itself creates brittle wording-lock or new protocol bureaucracy.

Reopen only the affected ownership/routing/compression decision; preserve unrelated accepted semantics and evidence.

## Initially expected affected behavioral surface

Primary expected files/surfaces:

- `source/roles/software-design/SKILL.md`;
- `source/roles/software-implementation/SKILL.md`;
- `source/shared/references/workflow-and-workplans.md`;
- `source/shared/references/testing-and-validation.md`;
- `source/shared/references/architecture-and-design.md` where canonical ownership clarification is needed;
- `source/shared/references/repository-intake.md` where progressive-disclosure wording is needed;
- `source/shared/references/protocol-versioning-and-compatibility.md` for 5.8 inheritance/history;
- `source/shared/templates/implementation_workplan_template.md`;
- root `AGENTS.md`, root/source README/version narrative where necessary to avoid duplication/drift and route authority concisely;
- `source/PROTOCOL_VERSION` at the release/versioning stage;
- protocol contract/stewardship/proxy-proof/tooling tests as affected by ownership-oriented assertions and new historical scenarios;
- build/package validation and generated `dist/` packages.

Implementation must re-derive the final affected surface from the assembled candidate. Documentation/specialist skills not semantically changed should not be rewritten merely for stylistic consistency; inspect/update them only where canonical ownership, version identity, routing, or duplicated normative doctrine actually intersects the revision.

## Task-specific acceptance

Generic functional-acceptance requirements are inherited from Protocol 5.7.0 while this workplan is active.

Release acceptance additionally requires:

1. every material 5.4-5.7 doctrine/failure-mode defense is accounted for in the final canonical owner + entrypoint-trigger architecture;
2. no material doctrine depends solely on historical workplans/archive files for current normative meaning;
3. lifecycle entrypoints are materially consolidated relative to 5.7 and no comparable duplication is merely shifted into root routing/template/test surfaces;
4. role entrypoints remain self-sufficient for high-salience hard rules and unambiguous about when to load detailed references;
5. the substantial-workplan template remains lossless for task-specific intent but does not require generic protocol boilerplate or empty conditional fields;
6. stage proportionality is explicit without weakening stage-local affected regression breadth;
7. proxy-proof acceptance and permitted bounded test doubles remain behaviorally unambiguous;
8. product-truth/non-gaming/self-correction/truthful-nonclosure semantics remain behaviorally unambiguous;
9. deterministic historical failure-mode scenarios and all existing still-applicable protocol regression tests pass;
10. repository acceptance passes on the final candidate:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

11. generated distributions match canonical source;
12. independent final review finds neither lossy overcompression nor material residual control-plane duplication/ceremony that the accepted design intended to remove;
13. if valid controlled agent/task benchmarking is performed, it shows no material engineering-success regression attributable to compression; absence of such benchmarking is explicitly reported and is not by itself a blocker when creating it would violate the no-bureaucracy constraint.

Production qualification: unnecessary. This protocol revision changes instruction/control-plane artifacts rather than production software runtime behavior. Bounded protocol/package tests and any optional controlled agent evaluation are the relevant evidence.

## Gated implementation sequence

### Gate G0 - Semantic baseline and canonical ownership freeze

**Purpose:** make semantic loss detectable before normative compression begins.

Required implementation work:

- enumerate the current material 5.4-5.7 guarantees represented in current normative source, using the historical lineage above as the minimum set;
- map each guarantee to its intended canonical detailed owner and required entrypoint salience/trigger;
- identify overlapping prose across Design, Implementation, workflow, testing, template, AGENTS/README, and tests;
- identify any apparent doctrinal conflicts or host-loading constraints before deletion.

Acceptance:

- every material guarantee has a surviving normative owner;
- every high-salience guarantee has an explicit role-local invariant/trigger where needed;
- no proposed deletion relies on archive history as current authority;
- no genuine unresolved semantic conflict remains hidden by the compression plan.

Do not create a permanent doctrine ledger solely for compliance. A task-local implementation aid may be used and removed/condensed after it has served the migration.

### Gate G1 - Lifecycle entrypoint consolidation

**Purpose:** remove the highest-cost always-loaded duplication while preserving role-local behavior.

Required implementation work:

- refactor `software-design/SKILL.md` to the accepted compact role loop and direct invariants;
- refactor `software-implementation/SKILL.md` to the accepted compact role loop and direct invariants;
- preserve reference routing by material surface and make progressive-disclosure semantics explicit;
- preserve role descriptions/host metadata needed for correct invocation.

Acceptance:

- semantic-conformance inspection against G0 ownership map passes;
- entrypoints retain all frozen hard rules and required loading triggers;
- material duplicated edge-case exposition has been removed rather than paraphrased repeatedly;
- size/duplication diagnostics demonstrate material consolidation or explain any retained detail by a specific salience/host-behavior need;
- focused protocol tests for entrypoint contracts pass before dependent template/reference consolidation proceeds.

### Gate G2 - Canonical reference, template, and routing reconciliation

**Purpose:** ensure detail removed from entrypoints remains exactly and usefully owned without moving bureaucracy elsewhere.

Required implementation work:

- reconcile workflow/testing/architecture/intake/versioning references so each owns its detailed semantics once;
- compress the implementation workplan template to task-specific intent + inherited generic doctrine;
- reconcile `AGENTS.md` and README/source README so they route authority concisely rather than restating manuals;
- update long-reference section indexes only where materially useful for targeted loading;
- remove stale or newly redundant duplicated wording where safe.

Acceptance:

- no semantic orphan exists;
- no substantial boilerplate migration into template/root routing surfaces;
- template handoff remains lossless and conditional fields remain conditional;
- current workplan/version precedence remains unambiguous;
- focused reference/template/versioning tests pass.

### Gate G3 - Ownership-oriented and historical-failure-mode regression

**Purpose:** replace phrase-duplication incentives with semantic regression evidence.

Required implementation work:

- refactor tests so detailed doctrine is asserted primarily at canonical owners and entrypoints are tested for indispensable invariants/triggers;
- retain direct multi-surface assertions only where deliberate duplication is itself part of the contract;
- add deterministic coverage for the minimum historical failure-mode scenarios listed in this workplan;
- add lightweight control-plane size/duplication diagnostics without arbitrary release thresholds.

Acceptance:

- all existing still-valid Protocol 5.7 regressions remain semantically covered;
- historical scenarios demonstrate preserved decisions for omission, proxy acceptance, allowed bounded fakes, reconciliation, redesign, anti-gaming, self-correction, stage proportionality, discovered affected surface, structural absence, and stakeholder-outcome review;
- tests do not force gratuitous verbatim duplication;
- stage-local affected regression for this executable test/tooling change passes.

### Gate G4 - Final assembled protocol acceptance and effectiveness closure

**Purpose:** establish that the assembled Protocol 5.8 candidate is both semantically non-inferior and materially simpler.

Required implementation work:

- re-derive the complete affected protocol/package/test/documentation surface from the final candidate;
- reconcile every workplan obligation and every G0-preserved doctrine against the assembled candidate;
- inspect for semantic orphaning, contradictory authority, hidden weakening, reference-loading ambiguity, boilerplate migration, and residual unjustified duplication;
- run full repository protocol/package/dist acceptance;
- collect final entrypoint/control-plane size/duplication diagnostics against Protocol 5.7;
- perform controlled 5.7-vs-5.8 agent/task comparison only if a valid reproducible harness is available without introducing disproportionate new infrastructure;
- independently review both overcompression and insufficient compression.

Acceptance:

- all repository checks pass;
- distributions are regenerated and source/dist parity passes;
- all material historical doctrines are preserved with clean canonical ownership;
- no historical failure-mode scenario regresses;
- entrypoint/control-plane consolidation is material and not achieved by relocating equivalent duplication;
- no required coverage, real-owner boundary, conformance obligation, or stakeholder-product safeguard is weakened;
- no new permanent bureaucracy was introduced to prove economy;
- independent review accepts both semantic fidelity and control-plane simplification;
- any unavailable optional effectiveness benchmark is reported accurately without counterfeit empirical claims.

Only after G4 closure may the protocol version be finalized as 5.8.0, generated distributions treated as release candidates, and this workplan moved to completed/archive state under the repository's normal release workflow.

## Design handoff closure

The final review reconciled:

```text
explicit request for improved protocol effectiveness/efficiency
+ diagnosis of Protocol 5.7 control-plane overgrowth
+ Protocol 5.4 development-economy protections
+ Protocol 5.5 lossless implementation fidelity
+ Protocol 5.6 proxy-proof acceptance
+ Protocol 5.7 engineering stewardship/product truth
+ no-loss / no-bureaucracy / no-micro-gating constraints
+ repository source/build/version authority
    -> canonical-ownership compression design
    -> implementation obligations and four coherent gates
    -> semantic + functional + structural acceptance evidence
```

No known material requirement or historical failure-mode defense is intentionally omitted from the implementation contract. Exact prose and local test factoring remain delegated; semantic survival, salience, canonical ownership, and acceptance behavior are frozen.

## Material risks and redesign triggers

- **Overcompression:** a high-value rule becomes discoverable only after the agent has already made the wrong decision. Trigger: scenario failure, host-loading evidence, or independent review finding. Correction: restore the minimum role-local invariant/trigger, not the full duplicate exposition by default.
- **Undercompression:** most 5.7 prose survives with superficial wording edits. Trigger: final duplication/size analysis or review shows no material control-plane simplification. Correction: consolidate repeated explanation into canonical owners while preserving direct hard rules.
- **Ownership conflict:** two references need materially different versions of what appears to be one rule. Trigger: semantic analysis shows distinct lifecycle concerns. Correction: retain justified specialization rather than forcing artificial deduplication.
- **Test-induced prose locking:** revised tests still require particular repeated phrases rather than behavior/ownership. Trigger: semantically equivalent wording fails tests without contract impact. Correction: test the canonical semantic owner and necessary trigger instead.
- **Reference-loading ambiguity:** supported host behavior cannot reliably recover routed details. Trigger: packaging/host validation or controlled task evidence. Correction: increase directly loaded detail only for the affected hard rule/host boundary.
- **Benchmark confounding:** live-agent comparison is not reproducible across models/settings/tool state. Trigger: uncontrolled variance or unavailable instrumentation. Correction: do not use it as release proof; report limitation and rely on deterministic semantic evidence.
- **Economy weakening coverage:** stage proportionality or concise completion reporting is interpreted as permission to skip affected behavior. Trigger: regression/scenario/review evidence. Correction: strengthen the direct coverage invariant while keeping process ceremony proportional.
