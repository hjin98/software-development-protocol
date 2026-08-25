---
kind: implementation-workplan
workplan_id: PROTOCOL-5.6-PROXY-PROOF-ACCEPTANCE
protocol_version: 5.5.0
target_protocol_version: 5.6.0
status: completed
completed_date: 2026-08-25
---

# Protocol 5.6 Proxy-Proof Acceptance Workplan

## Objective

Strengthen Protocol 5.5 so integration/acceptance evidence cannot satisfy a material requirement by mocking, bypassing, reimplementing, or precomputing the production semantic owner whose behavior is actually under acceptance, while preserving Protocol 5's governing doctrine, two-role lifecycle, adaptive implementation, bounded test cost, mandatory regression/integration acceptance, independent review authority, and development-economy guarantees.

## Diagnosis and protected concerns

Protocol 5.5 already separates semantic/conformance closure from functional testing, requires real product/consumer integration, and states that green tests cannot prove omitted obligations. The remaining defect is narrower: the protocol does not explicitly define the production **semantic owner under acceptance**, the boundary below/outside which test doubles may safely begin, or the counterfactual condition that evidence must fail when that owner is materially broken.

That omission permits false-positive acceptance patterns such as:

- monkeypatching an authorization/validation owner to return the desired result while claiming that authorization/validation is accepted;
- directly calling a downstream invalidation/helper function while claiming that the production restart/reconciliation/orchestration caller detects and invokes it correctly;
- replacing real persistence with a custom in-memory store while claiming persistence/restart semantics;
- reimplementing migration/compatibility/identity logic in a fixture while claiming the production compatibility path;
- asserting a helper-produced plan while claiming that the assembled real consumer used the plan correctly.

The protected concern is not "avoid mocks". Test doubles remain essential for bounded execution. The protected concern is **acceptance substitution**: evidence must exercise the production authority/decision/state-transition that constitutes the claim, while expensive external computation may be replaced below or outside that boundary.

## Engineering envelope

The revision must preserve or strengthen all existing Protocol 5.5 guarantees:

- governing hierarchy remains exactly `product engineering fitness > minimum justified product/system complexity > development economy`;
- lifecycle remains exactly `software-design -> software-implementation`; no review/testing role is added;
- Design retains diagnosis/design, lossless workplan translation, validation design, and independent review;
- Implementation retains adaptive realization, repository reconciliation, semantic/conformance closure, stage-local/final affected regression, integration, validation, cleanup, and delivery;
- accepted workplans remain minimum known contracts rather than ceilings and preserve `Frozen / Delegated / Reopen only on evidence`;
- evidence-backed local reconciliation and bounded redesign remain valid; an acceptance boundary explicitly frozen by a workplan may not be weakened as local reconciliation;
- functional acceptance still requires focused checks, stage-local affected regression, final affected-surface re-derivation/regression, integration, and repository/project checks;
- bounded/synthetic tests remain preferred when they exercise the same real contract;
- full production qualification remains separate and is not introduced as a prerequisite for ordinary acceptance;
- no mandatory persistent ledger, per-function checklist, mutation-testing regime, universal AST scanner, anti-mocking framework, or model-specific policy is introduced;
- `source/` remains canonical and `dist/` remains generated distribution output.

The revision must be precise enough that a smaller implementer cannot reinterpret a required real-owner acceptance boundary as a suggested fixture structure, while remaining concise enough that the role entrypoints and root `AGENTS.md` function as routing/golden-path documents rather than duplicated manuals.

## Product design

### A. Define the semantic owner and proxy-proof acceptance

`source/shared/references/testing-and-validation.md` owns the normative generic testing rule.

Define:

- **Semantic owner under acceptance** — the production component, state machine, consumer, validator, persistence mechanism, compatibility/migration path, authorization layer, orchestrator, or decision-maker whose real behavior materially constitutes the acceptance claim.
- **Allowed test-double boundary** — a dependency below or outside the semantic owner that may be replaced to bound cost, hardware, external services, data volume, or nondeterminism while leaving the owner's real decision/control/state-transition path intact.
- **Proxy-proof acceptance** — evidence is valid for a material owner claim only when a material defect in the required semantic owner would cause the evidence to fail.

Normative consequence: an integration/acceptance test does not establish a production-owner claim if it mocks, stubs, monkeypatches, precomputes, substantially reimplements, or bypasses the owner whose behavior is under acceptance.

Explicitly include these invalid substitutions when they replace the claimed owner/path:

- patching the owner to return the expected answer;
- directly invoking a downstream helper when the production caller/orchestrator/reconciler decision is part of the claim;
- seeding post-decision/post-transition state and skipping the required transition;
- replacing durable/project persistence when persistence/restart/recovery is part of the claim;
- reimplementing production compatibility, migration, identity, scheduling, authorization, or orchestration logic inside the harness;
- treating helper-only output as assembled-consumer acceptance.

This is not a global ban on test doubles. External/expensive computation may be faked below/outside the real accepted boundary.

### B. Lossless acceptance-boundary handoff from Design

Extend the existing implementation-obligation model rather than creating a parallel traceability artifact.

When a material acceptance claim depends on a real orchestration, persistence/restart/recovery, authorization, compatibility/migration, scientific/configuration identity, policy/selection, state transition, or assembled consumer boundary, Design must preserve enough information to recover, as applicable:

- **Acceptance claim** — the material behavior/result being established;
- **Required real owner/path** — production owner(s)/boundary that must actually execute;
- **Allowed test doubles** — expensive/external dependencies permitted to be replaced;
- **Forbidden substitutions** — owner/boundary that must not be mocked, bypassed, reimplemented, or precomputed;
- **Observable acceptance evidence** — state/output/transition/consumer result proving the claim.

These fields are semantic requirements only when material; no table or identifier format is mandatory. Ordinary unit tests do not require ceremonial owner matrices.

### C. Implementation must audit the acceptance path, not merely the test result

Before relying on material integration/acceptance evidence, Software Implementation must determine:

1. which production owner/path the claim depends on;
2. what components on that path are replaced or bypassed;
3. whether every replacement lies below/outside the required real boundary; and
4. whether the evidence could remain green if the required semantic owner were materially broken.

If the answer to item 4 is yes, that evidence cannot close the acceptance obligation.

Calling a downstream helper directly does not establish that its production caller, authorization layer, restart reconciler, persistence owner, state machine, or orchestrator detects the condition and invokes it correctly.

When a workplan explicitly freezes a real-owner/test-double boundary, weakening that boundary is not an implementation-local reconciliation. If the real boundary cannot be exercised without changing a frozen material design or acceptance decision, report an unavailable/blocking check or reopen the affected design on evidence rather than silently accepting a proxy.

### D. Preserve bounded test cost

The protocol must continue to encourage bounded deterministic fixtures and permit, where below/outside the claimed owner:

- fake ML/scientific training or prediction subprocesses;
- fake GPU/accelerator execution;
- synthetic/reduced scientific data;
- stubbed external network/services;
- reduced epochs/iterations/workload size;
- deterministic external responses;
- fake expensive computation invoked by a real repository-owned decision/state machine.

The generic rule is boundary fidelity, not production-scale execution.

### E. Executable anti-bypass checks are targeted, not universal

When a task-specific workplan names forbidden semantic-owner substitutions and a robust inexpensive structural/negative check can prevent recurrence, Implementation should add that guardrail to the task's regression/acceptance surface.

Do not require universal AST scanning, mutation testing, a global monkeypatch ban, one acceptance test per function, or a new framework. Structural anti-bypass checks are required only where the task contract/risk makes them material.

### F. Compact root `AGENTS.md` as authority router

Add a short root `AGENTS.md`. It must route rather than duplicate the protocol.

Required routing semantics:

- `source/` is canonical; do not hand-edit generated `dist/` output;
- explicit user/task requirements and the workplan actually governing the task take precedence according to existing protocol authority;
- do not infer that every file in `workplans/active/` governs every task merely from directory membership;
- Design/review tasks route to `source/roles/software-design/SKILL.md`;
- implementation tasks route to `source/roles/software-implementation/SKILL.md`;
- testing/regression/integration/test-double/qualification questions route to `source/shared/references/testing-and-validation.md`;
- lifecycle/workplan authority routes to `workflow-and-workplans.md`;
- protocol-version inheritance routes to `protocol-versioning-and-compatibility.md`;
- one concise reminder states that a required production semantic owner may not be replaced/bypassed when its behavior is the acceptance claim;
- repository completion routes to the existing documented test/build/package/parity/whitespace workflow.

`AGENTS.md` must remain substantially shorter than role/reference documents and must not become a second implementation skill or duplicate detailed mock/test-double rules.

### G. Version and documentation synchronization

Release as Protocol `5.6.0`, a backward-compatible protocol capability/acceptance strengthening. Update concise root/source README and versioning text to identify the new proxy-proof acceptance capability without rewriting existing doctrine.

Protocol inheritance remains version-bound: older completed/active workplans do not silently acquire 5.6 semantics unless their declared protocol version is explicitly reconciled/updated under existing compatibility rules.

### H. Independent review explicitly challenges proxy acceptance

Software Design independent review must treat a materially mocked/bypassed semantic owner as implementation nonconformance when the accepted workplan already required that owner/path to execute for real. If the workplan failed to specify a materially necessary real boundary, route that as a workplan/design deficiency instead.

Review should use the same counterfactual: could the evidence remain green while the claimed production owner is broken? If yes, the claim is not established.

## Implementation authority

### Frozen

- Protocol 5 governing doctrine/hierarchy is unchanged.
- The lifecycle remains exactly two roles; no new review/testing/compliance role is introduced.
- Protocol 5.3/5.4/5.5 regression/integration, bounded redesign, workplan authority, evidence/context economy, lossless handoff, dual closure, independent review, version binding, and production-qualification separation remain at least as strong.
- Test doubles remain valid engineering tools below/outside the material real-owner boundary.
- A material owner claim cannot be accepted through evidence that replaces or bypasses that owner and could remain green while the owner is broken.
- Explicit real-owner/test-double boundaries in accepted workplans are acceptance decisions, not suggestions implementation may silently weaken.
- No mandatory persistent compliance artifact or universal anti-mock machinery is introduced.
- Root `AGENTS.md` is a compact router, not a duplicated protocol manual.

### Delegated

- Exact terminology/prose ordering provided the semantic-owner, allowed-double, forbidden-substitution, and counterfactual rules remain unambiguous.
- Whether task-specific workplans use prose, bullets, or tables for acceptance-boundary information.
- Exact structural anti-bypass test technique where a task-specific guardrail is material.
- Minor README wording and exact `AGENTS.md` formatting provided routing/authority semantics remain concise and correct.

### Reopen only on evidence

Reopen only the affected design surface if implementation shows that:

- the semantic-owner concept conflicts with an existing valid testing/architecture contract;
- the proxy-proof counterfactual necessarily requires production-scale qualification rather than bounded integration for a material class of normal software;
- correct owner boundaries cannot be expressed without a persistent compliance bureaucracy;
- compact `AGENTS.md` routing cannot coexist with the current package/source authority model;
- preserving older protocol-version inheritance is incompatible with the strengthening;
- proposed wording weakens any existing doctrine, adaptive-realization, regression/integration, evidence-economy, or qualification guarantee.

## Initially expected affected behavioral surface

Required source/repository changes:

- new root `AGENTS.md`;
- `source/PROTOCOL_VERSION`;
- `source/roles/software-design/SKILL.md`;
- `source/roles/software-implementation/SKILL.md`;
- `source/shared/references/testing-and-validation.md`;
- `source/shared/references/workflow-and-workplans.md` for concise lifecycle/closure synchronization only;
- `source/shared/references/protocol-versioning-and-compatibility.md`;
- `source/shared/templates/implementation_workplan_template.md`;
- root `README.md` and `source/README.md` concise version/capability summaries;
- protocol semantic/regression tests;
- generated `dist/` packages and `BUILD_INDEX.json`.

Conditional only on concrete consistency evidence:

- `source/shared/references/architecture-and-design.md` if owner/boundary terminology cannot be expressed through existing ownership semantics;
- build tooling only if current package generation/validation cannot carry the changed canonical source unchanged.

Do not broaden into specialists, performance/scientific references, git policy, security policy, or repository hygiene without concrete affected-contract evidence.

## Task-specific acceptance

Generic Protocol 5.5 functional acceptance remains inherited during implementation of this 5.6 revision.

The assembled Protocol 5.6 source/packages must establish all of the following:

1. The existing lexicographic doctrine and two-role lifecycle remain explicit and unchanged in meaning.
2. Existing 5.3/5.4/5.5 guarantees listed under Frozen remain protected by regression assertions.
3. Testing guidance defines semantic owner under acceptance, allowed test-double boundary, and proxy-proof acceptance.
4. A materially mocked/bypassed owner cannot satisfy its own integration/acceptance claim.
5. Test doubles below/outside the real owner remain explicitly permitted for bounded execution.
6. Direct downstream-helper invocation is explicitly insufficient when caller/orchestrator/restart/authorization detection is part of the claim.
7. Fake persistence is explicitly insufficient when durable persistence/restart/recovery is the claim.
8. Harness reimplementation/helper-only proof is explicitly insufficient for the corresponding real compatibility/orchestration/consumer claim.
9. Design/workplan handoff preserves required real owner/path, allowed doubles, forbidden substitutions, and observable evidence where materially necessary, without imposing mandatory matrices on ordinary unit tests.
10. Implementation performs the acceptance-path/counterfactual audit before relying on material acceptance evidence.
11. A frozen real-owner boundary cannot be weakened as local reconciliation.
12. Unavailable real-boundary acceptance is not silently downgraded to a proxy pass.
13. Independent review challenges proxy acceptance and routes failures correctly as implementation nonconformance versus plan/design deficiency.
14. Targeted structural anti-bypass checks are supported where material, without universal anti-mock bureaucracy.
15. Root `AGENTS.md` remains compact and accurately routes to canonical role/reference/workflow authority; it does not treat all active-directory workplans as automatically governing.
16. `source/` remains canonical; generated `dist/` remains source-derived and exactly synchronized.
17. Protocol versioning identifies 5.6.0 as a backward-compatible acceptance-strengthening release without silently changing older workplan inheritance.
18. Existing package build/validation/parity/whitespace workflow remains the repository completion path.

Add semantic/structural protocol regression tests that protect these contracts without brittle exact-line-count or large exact-prose assertions.

Perform an assembled scenario review covering at minimum:

- **S1 invalid owner mock:** preflight/authorization owner mocked to desired success while authorization is the claim -> must be classified insufficient;
- **S2 valid below-owner fake:** real authorization/state machine/persistence executes while expensive training/GPU/external computation is faked below it -> valid bounded integration;
- **S3 invalid helper bypass:** invalidation helper called directly while restart/reconciliation detection is the claim -> insufficient;
- **S4 invalid fake persistence:** custom/in-memory store used while durable restart semantics are the claim -> insufficient;
- **S5 invalid helper-only consumer proof:** helper plan/result asserted while assembled consumer use is the claim -> insufficient;
- **S6 unavailable real boundary:** real required boundary cannot execute -> unavailable/blocking or evidence-backed redesign, never proxy-pass.

Production qualification: **unnecessary**. This protocol/instruction revision requires no long-running target-hardware workload.

## Implementation sequence

### G0 - Preserve established Protocol 5 doctrine and 5.5 guarantees

Before changing semantics, add/identify regression assertions protecting doctrine hierarchy, two-role lifecycle, adaptive workplan authority/bounded redesign, lossless implementation-fidelity handoff, dual stage closure, stage-local/final regression/integration, evidence/context economy, version-bound inheritance, production-qualification separation, and no persistent compliance bureaucracy.

**Semantic closure:** no prior guarantee is weakened or reinterpreted.

**Functional closure:** focused protocol-contract tests and all affected existing tests pass.

### G1 - Proxy-proof testing and acceptance contract

Implement A, C, D, and E primarily through `testing-and-validation.md` plus concise implementation-role enforcement. Add scenario-oriented protocol regression assertions for owner mock, below-owner fake, helper bypass, fake persistence, helper-only consumer proof, and unavailable-boundary behavior.

**Semantic closure:** the real-owner boundary and counterfactual rule are unambiguous; bounded test doubles remain valid.

**Functional closure:** focused testing/implementation semantic tests plus affected protocol tests pass.

### G2 - Lossless acceptance-boundary design handoff and review

Implement B and H in Software Design and the workplan template, with only necessary workflow synchronization.

**Semantic closure:** a smaller implementer can determine which path must remain real and which expensive dependencies may be faked without reconstructing the design; independent review can distinguish implementation proxying from a missing design boundary.

**Functional closure:** design/template/workflow semantic tests plus affected protocol tests pass.

### G3 - Compact agent routing and version/documentation synchronization

Implement F and G. Add root `AGENTS.md`, update version to 5.6.0, versioning history/inheritance wording, and concise README summaries. Keep `AGENTS.md` routing-focused and substantially shorter than role/reference documents.

**Semantic closure:** no authority duplication or active-directory ambiguity is introduced; canonical paths and completion workflow are accurate.

**Functional closure:** version/routing/README/tooling semantic tests plus affected protocol tests pass.

### G4 - Final assembled conformance and regression review

Reconcile every workplan requirement against the assembled candidate. Independently inspect for doctrine drift, accidental global mock bans, production-qualification creep, weakened adaptive implementation, authority duplication, `AGENTS.md` bloat, and scenario gaps. Repair any implementation nonconformance before proceeding.

Re-derive the complete affected surface and run the complete protocol regression suite on the same assembled candidate.

**Gate closure:** all task-specific acceptance and S1-S6 scenarios are represented correctly; complete protocol tests pass.

### G5 - Package and repository closure

Build canonical packages from final `source/`, independently validate packages, regenerate committed `dist/`, verify exact source-to-dist parity, run whitespace checks, and inspect final diff for unintended scope/stale contradictory 5.5-only wording.

Required repository commands remain:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

Only after G0-G5 pass may this workplan be marked completed and archived.

## Design handoff closure

Reconciled:

`explicit request to prevent mocking/bypass acceptance failures`
`+ diagnosed acceptance-substitution failure`
`+ preserved Protocol 5 doctrine and 5.5 guarantees`
`+ semantic-owner/test-double/counterfactual design`
`+ compact AGENTS.md routing requirement`
`+ no-global-mock-ban/no-production-qualification/no-bureaucracy non-goals`
`-> concrete implementation obligations A-H`
`-> task-specific acceptance 1-18 and scenarios S1-S6`
`-> gated regression/package closure G0-G5`.

No material known consequence from the reviewed design has been omitted. The workplan intentionally delegates prose/layout and local anti-bypass mechanism choices while freezing the acceptance semantics and doctrine-preservation boundary.

## Risks / redesign triggers

1. **Overreach into anti-mocking policy:** wording accidentally bans legitimate bounded test doubles rather than only owner substitution.
2. **Proxy loophole remains:** wording forbids monkeypatching but still permits direct helper calls, seeded post-state, fake persistence, or harness reimplementation to stand in for the real owner.
3. **Acceptance inflation:** owner-fidelity requirements accidentally force production-scale qualification rather than bounded real-control-path testing.
4. **Workplan bureaucracy:** every unit test is forced to carry an owner matrix despite no material boundary risk.
5. **Local-reconciliation loophole:** implementation treats an explicit real-owner acceptance boundary as adaptable mechanics and weakens it.
6. **AGENTS authority drift:** root instructions become a second protocol manual or incorrectly declare all `workplans/active/` entries governing.
7. **Doctrine regression:** engineering hierarchy, adaptive realization, regression/integration breadth, evidence economy, version inheritance, or qualification separation weakens.
8. **Distribution drift:** generated packages or version/build index diverge from canonical source.

If a trigger fires, reopen only the affected design surface and preserve unrelated accepted work/evidence.

## Frozen implementation principle

> **Acceptance must execute the production semantic owner whose behavior constitutes the claim; test doubles may replace expensive or external dependencies only below or outside that boundary. Evidence that could remain green while the required owner is materially broken cannot close the claim. Preserve all existing Protocol 5 doctrine and acceptance guarantees while enforcing this boundary without unnecessary process or production-scale cost.**


## Completion record

Protocol 5.6 was implemented and independently reviewed under this workplan without reopening the governing Protocol 5 doctrine or two-role lifecycle.

### G0-G3 implementation evidence

The gated implementation workflow applied the canonical source/test transformation and succeeded through regression, package build, package validation, source-to-dist parity, and whitespace checks before creating implementation commit `ee99ad861f62b5cac472d006abbcd3a62823ee2e`. A content-identical reviewed checkpoint used tree `dee32889ecbbed2873c4f37b8044b72f3b5cf95b` at commit `30f64fc3d1a4b972f04e2c349d7d337737a4c58a`.

Implementation workflow evidence: GitHub Actions run `32887845204`, job `97932397376`, conclusion `success`.

### G4 independent assembled review

The final source/diff was reviewed against the accepted contract rather than the implementer's summary. The review found no material doctrine regression, no lifecycle expansion, no global anti-mock policy, no production-qualification inflation, no local-reconciliation loophole for frozen real-owner boundaries, and no authority duplication. Root `AGENTS.md` remains a short authority router rather than a second protocol manual.

Scenario closure:

- S1 owner mock: rejected as insufficient owner acceptance.
- S2 below-owner fake: explicitly permitted for bounded integration while the real owner/control path executes.
- S3 direct helper bypass: rejected when caller/restart/reconciliation/authorization detection is the claim.
- S4 fake persistence: rejected when durable persistence/restart/recovery is the claim.
- S5 helper-only consumer proof: rejected when assembled consumer behavior is the claim.
- S6 unavailable real boundary: unavailable/blocking or evidence-backed design reopen; never silently proxy-passed.

### G5 final repository acceptance

Final closure workflow run `32888128588` executes the repository-required commands on the assembled candidate before this completion commit is created:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

This workplan is archived only if every command succeeds. Production qualification remains unnecessary for this protocol/instruction revision.
