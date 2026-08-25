---
kind: implementation-workplan
workplan_id: PROTOCOL-5.5-IMPLEMENTATION-FIDELITY
protocol_version: 5.4.0
target_protocol_version: 5.5.0
status: completed
completed_date: 2026-08-25
---

# Protocol 5.5 Implementation-Fidelity Workplan

## Objective

Strengthen the existing Protocol 5 design -> implement -> review cycle so accepted design intent reaches implementation and rework without lossy compression, routine omissions, silent plan drift, or avoidable reviewer rediscovery, while preserving the Protocol 5 doctrine, two-role lifecycle, implementation adaptability, independent review authority, mandatory regression/integration acceptance, and Protocol 5.4 development-economy guarantees.

## Diagnosis

Protocol 5.4 correctly establishes accepted-workplan authority, frozen/delegated/evidence-reopened decisions, bounded redesign, coherent stage-local regression, final affected-surface acceptance, and evidence/context economy. The remaining failure surface is the translation and closure interface between those mechanisms:

1. A substantial workplan can be architecturally correct yet omit concrete implementation consequences, leaving implementation to reconstruct design intent.
2. Frozen/delegated/reopen authority states who may decide, but does not by itself prove that every material requirement became an actionable implementation obligation.
3. Adaptive implementation can drift when it receives a requested action without the protected concern/root failure mode that the action is meant to preserve.
4. Required implementation consequences and merely suggested realizations are not explicitly distinguished, so implementers may either treat advice as frozen or treat a required consequence as optional.
5. Stage-local regression proves exercised behavior but does not prove that all obligations assigned to the stage were implemented; an omitted obligation can coexist with green tests.
6. Final affected-surface derivation answers what behavior may have changed, but does not independently reconcile what the accepted contract required against what the final candidate actually implements.
7. The accepted workplan must remain a minimum known contract rather than a ceiling: newly discovered local consequences necessary to preserve frozen semantics must be incorporated without arbitrary redesign.
8. Reviewer findings can recreate the same lossy handoff if they are returned as vague criticism instead of evidence-backed correction requirements with proper routing.
9. Independent review must remain free to discover unplanned issues without turning equivalent implementation preferences into endless blocking redesign.

The revision is therefore a workflow-integration and communication-fidelity refinement, not a fundamental protocol redesign.

## Engineering envelope

The revision must preserve or strengthen all existing Protocol 5.4 guarantees:

- lexicographic doctrine: product engineering fitness > minimum justified product/system complexity > development economy;
- two lifecycle roles only: `software-design -> software-implementation`;
- design owns diagnosis, engineering envelope, product/architecture decisions, accepted-workplan authority, validation design, and independent review;
- implementation owns realization/refactoring, repository reconciliation, testing/validation, cleanup, and delivery under accepted design authority;
- evidence-triggered bounded redesign rather than blind plan obedience or independent architecture rediscovery;
- mandatory focused checks, stage-local affected regression after each material executable stage, final affected-surface re-derivation, final affected regression, integration, and repository/project-required checks;
- production qualification remains separate from functional acceptance;
- progressive repository inspection, compact task-local state, evidence reuse/invalidation, and no unnecessary process work;
- no model-specific behavior, no new lifecycle role, and no persistent compliance bureaucracy.

The revision must improve first-pass and rework fidelity by making task-specific implementation intent explicit enough that a capable smaller implementer need not guess material semantics, while retaining discretion over genuinely delegated local mechanics.

## Product design

### A. Lossless implementation contract

For substantial work, Software Design must translate accepted reasoning into an implementation contract that preserves every material requirement and every known implementation consequence needed to protect it. Compression may remove generic protocol prose; it must not remove task-specific intent.

A material obligation must carry enough information, as applicable, to recover:

- **protected concern / rationale**: the root cause, invariant, failure mode, or engineering objective that local realization must preserve;
- **required end state**: the behavior, ownership, architecture, or observable result that must hold;
- **required constraints / preservation / forbidden behavior**: what must remain unchanged or must no longer exist;
- **expected owning or affected surface**: components, interfaces, callers, persistence, configuration, tests, documentation, packaging, or transitive consumers where evidence justifies that specificity;
- **required implementation consequences** already determined by the accepted design;
- **suggested realization** when useful but adaptable without changing frozen semantics;
- **acceptance evidence** proving the obligation, including structural/absence evidence where runtime tests alone are insufficient;
- **stage/dependency** where ordering materially affects correctness or rework risk.

IDs, tables, and matrices are optional presentation mechanics. The semantics above are mandatory when material.

### B. Authority must remain explicit

Keep the existing `Frozen / Delegated / Reopen only on evidence` authority split. Clarify the difference between:

- **Required outcome/constraint** — must hold.
- **Required implementation consequence** — must occur because the accepted design logically requires it.
- **Suggested realization** — evidence-based recommendation that may be replaced by an equivalent local realization preserving the same protected concern and frozen semantics.
- **Delegated mechanics** — intentionally left open.

A known material consequence must not be omitted merely to keep the workplan shorter.

### C. Design handoff closure

Before accepting a substantial workplan, Software Design must reconcile:

`explicit requirements + diagnosed protected concerns + accepted design/invariants + preservation/non-goals + known cross-module consequences -> implementation obligations -> acceptance evidence`.

No material requirement or known design consequence may disappear between design reasoning and the accepted implementation contract. This is a reasoning/closure requirement, not a mandatory persistent traceability artifact.

### D. Implementation intake and adaptive realization

Before material editing under an accepted workplan, Software Implementation must identify the material obligations and their protected concerns, reconcile them against actual repository ownership, and classify mismatches using the existing implementation-realization / local-reconciliation / material-redesign boundary.

Implementation must not blindly execute stale mechanics. It should adapt local realization when repository evidence supports a better equivalent method, but it may not invent a different product, silently violate a protected concern, or change a frozen material decision.

### E. Workplan is a floor, not a ceiling

Accepted obligations are the minimum known contract. During implementation:

- a newly discovered necessary local consequence that preserves frozen design is incorporated and validated as implementation realization/local reconciliation;
- a newly discovered affected behavior/test/documentation consequence is added to the task-local affected surface and acceptance coverage;
- a newly discovered need to change frozen architecture, ownership, algorithm, product semantics, material resource/persistence/compatibility policy, or another frozen decision requires evidence-backed bounded redesign.

### F. Dual stage closure

A material implementation stage closes only when both dimensions are satisfied:

1. **semantic/conformance closure** — all obligations assigned to the stage are implemented or legitimately reconciled; frozen concerns remain protected; no unintended alternate authority, stale superseded path, or unjustified complexity was introduced; newly discovered affected consequences are accounted for;
2. **functional closure** — the existing Protocol focused checks and stage-local affected regression pass.

Use the cheapest high-information ordering for the stage. Do not add ceremonial review before every helper/file edit. If either dimension fails, repair within the stage before dependent implementation proceeds.

### G. Final implementation closure

Before handoff to independent review, Software Implementation must first reconcile the complete accepted contract against the final assembled candidate. Every material obligation must be satisfied, legitimately reconciled while preserving frozen intent, or blocked by a genuine redesign condition; silent omission is not an acceptable state.

Then inspect the assembled implementation for unintended changes, retained superseded machinery, ownership drift, unnecessary fallbacks/compatibility paths, unjustified complexity, and newly broadened affected surfaces. After that conformance closure, retain the existing final affected-surface re-derivation, complete affected regression, integration, and repository-required checks.

This establishes two independent questions: `did we build everything required?` and `does the resulting software work across the affected surface?` Neither substitutes for the other.

### H. Independent review and rework routing

Independent review is two-pass but remains one Design-role review activity:

1. **Contract conformance challenge** — independently compare requirements/workplan/legitimate reconciliations with the final candidate and evidence. Routine omitted obligations or violations of frozen design are implementation nonconformance, not new architecture work.
2. **Independent engineering challenge** — inspect beyond the plan for hidden correctness/scientific/resource/scaling/security/recovery/ownership/complexity/testing risks and premise failures.

Material reviewer findings must be actionable enough for lossless rework: identify the violated requirement/invariant or newly discovered concern, evidence, affected surface, why it matters, required corrected end state or correction constraint, acceptance evidence, and routing classification when material.

Route findings as:

- **implementation nonconformance**: accepted design was sufficient; return to implementation under the same workplan;
- **workplan/design deficiency**: accepted plan omitted or misstated a material requirement/decision/acceptance obligation; reconcile the affected design/workplan first, then reimplement;
- **new independent issue**: classify as local implementation consequence or evidence-backed bounded redesign.

Equivalent preferences with no material engineering benefit do not block acceptance. Review retains authority to broaden whenever material evidence warrants it.

### I. Absence is an acceptance claim when material

Task-specific acceptance may require behavioral/integration tests plus structural/source inspection or negative/absence assertions. Examples include proving that no legacy authority, hardcoded fixture, stale fallback, duplicate writer, obsolete documentation semantic, or superseded product path remains. Green runtime tests alone do not establish such obligations.

## Implementation authority

### Frozen

- Protocol 5 doctrine and lexicographic hierarchy are unchanged.
- The lifecycle remains exactly two roles; no `software-review` role/skill is introduced.
- The workplan/implementation-fidelity changes above are workflow integration, not a redesign of product engineering doctrine.
- `Frozen / Delegated / Reopen only on evidence` remains the authority model.
- Design must preserve task-specific intent through a lossless implementation contract and pre-handoff closure.
- Implementation must perform obligation intake, adaptive-but-faithful realization, dual semantic+functional stage closure, and final contract reconciliation before handoff.
- The workplan is a minimum known contract, not a cap on necessary consequences discovered during implementation.
- Independent review remains genuinely independent and returns material findings in a lossless, correctly routed form.
- Existing Protocol 5.4 functional acceptance, evidence/context economy, bounded redesign, version binding, and production-qualification separation remain at least as strong.
- The protocol must not require a new persistent ledger, database, manifest, per-file checklist, mandatory reflection essay, or model-specific policy.

### Delegated

- Exact prose and section titles, provided the role golden paths remain direct and unambiguous.
- Whether material obligations are expressed as prose, bullets, or tables.
- Optional local requirement identifiers where they improve clarity.
- Exact ordering of conformance inspection versus cheapest focused tests within a stage, provided both semantic and functional closure are achieved before stage acceptance.
- Minor source/reference factoring where it reduces duplication without hiding hard role obligations.

### Reopen only on evidence

Reopen only the affected design surface if implementation shows that:

- the obligation information model necessarily creates a persistent compliance bureaucracy to function;
- the distinction between required consequence and suggested realization cannot be expressed without undermining adaptive implementation;
- dual stage closure conflicts materially with the existing stage-local regression/evidence-economy model;
- rework routing requires a new lifecycle authority rather than clearer semantics inside the existing roles;
- the current package/reference architecture cannot expose the required behavior without a material build-system change;
- a proposed wording weakens an existing Protocol 5.4 engineering or acceptance guarantee.

## Initially expected affected behavioral surface

### Required source changes

- `source/PROTOCOL_VERSION`
- `source/roles/software-design/SKILL.md`
- `source/roles/software-implementation/SKILL.md`
- `source/shared/templates/implementation_workplan_template.md`
- `source/shared/references/workflow-and-workplans.md`
- `source/shared/references/testing-and-validation.md`
- `source/shared/references/protocol-versioning-and-compatibility.md`
- `source/README.md`
- root `README.md`
- protocol regression tests
- regenerated `dist/` packages and `BUILD_INDEX.json`

### Conditional only on evidence

- `source/shared/references/architecture-and-design.md` if the existing accepted-design boundary cannot express the clarified contract semantics cleanly.
- build tooling only if package validation/version propagation cannot support the source revision unchanged.

Do not broaden into repository intake, optional specialists, or domain references without a concrete ownership/consistency need.

## Task-specific acceptance

Generic functional acceptance is inherited from Protocol 5.4.0.

Protocol 5.5-specific semantic acceptance must establish that:

1. Software Design explicitly owns lossless design-to-implementation translation and pre-handoff completeness.
2. Substantial workplans preserve protected concern, required end state/constraints, known required implementation consequences, adaptable suggestions/delegation, affected surface, and acceptance evidence where material.
3. Required consequences and suggested realizations are distinguishable.
4. Software Implementation explicitly reconciles accepted obligations before material editing.
5. The accepted plan is a minimum known contract rather than a ceiling on newly discovered necessary consequences.
6. A material stage requires both semantic/conformance closure and the existing focused + affected-regression functional closure.
7. Final implementation closure reconciles every material obligation against the assembled candidate before final affected-surface regression/integration.
8. Absence/structural claims can require source/negative evidence rather than runtime tests alone.
9. Independent review performs contract-conformance challenge plus independent engineering challenge without losing scope authority.
10. Material review findings are actionable and route implementation nonconformance separately from workplan/design deficiency and genuinely new issues.
11. Equivalent preference disagreements without material engineering benefit do not become acceptance blockers.
12. Protocol 5.3/5.4 doctrine, two-role lifecycle, regression/integration, bounded redesign, production-qualification separation, version binding, and development-economy guarantees remain intact.

Add semantic/structural regression tests for these contracts. Avoid brittle exact-prose, exact-line-count, bullet-count, or fixed-size assertions.

Perform an assembled scenario review of the packaged role/workplan instructions covering at minimum:

- an obligation is omitted while existing tests still pass;
- actual repository layout requires an equivalent local realization differing from suggested mechanics;
- implementation discovers a necessary additional consequence that preserves frozen design;
- independent review discovers a genuine workplan/design omission.

The four scenarios must route to the intended closure/rework behavior without requiring a new lifecycle role or persistent artifact.

Production qualification: **unnecessary**. No long-running target-machine product workload is required for this protocol/instruction revision; do not claim quantitative reduction in review rounds without later representative workflow evidence.

## Implementation sequence

### G0 - Preserve Protocol 5.4 guarantees

Before behavior changes, add or identify regression assertions protecting the doctrine hierarchy, two-role lifecycle, accepted-workplan authority/bounded redesign, stage-local and final regression/integration, production-qualification separation, version binding, context/evidence economy, and no mandatory persistent task ledger.

**Stage semantic closure:** no existing guarantee is reinterpreted or weakened.

**Stage functional closure:** focused protocol-contract tests and affected existing tests pass.

### G1 - Lossless design handoff

Refactor Software Design and the implementation workplan template so substantial design produces a concrete, lossless implementation contract with protected concern, required end state/constraints, required consequences, clearly labeled suggested/delegated realization, expected affected surface, acceptance evidence, and handoff-completeness reconciliation.

Keep generic protocol doctrine inherited rather than copied into every plan. Keep `Frozen / Delegated / Reopen only on evidence` as a separate authority dimension.

**Stage semantic closure:** every design-side acceptance item 1-3 above is directly represented without creating mandatory traceability bureaucracy.

**Stage functional closure:** focused template/design semantic tests plus affected protocol tests pass.

### G2 - Closed-loop implementation

Refactor Software Implementation around accepted-contract intake, protected-concern understanding, repository reconciliation, adaptive realization, discovered-consequence handling, dual semantic+functional stage closure, and repair-before-dependent-work.

**Stage semantic closure:** implementation can adapt mechanics without changing frozen intent; omitted assigned obligations cannot be accepted merely because tests are green; newly discovered necessary consequences do not automatically trigger redesign.

**Stage functional closure:** implementation/workflow/testing semantic tests plus affected protocol tests pass.

### G3 - Final implementation closure

Add explicit final accepted-contract reconciliation and assembled implementation self-review before the existing final affected-surface derivation/regression/integration boundary. Include structural/absence evidence where task-specific claims require it.

**Stage semantic closure:** final acceptance separately establishes contract completeness and functional correctness; neither can silently stand in for the other.

**Stage functional closure:** final-closure semantic tests plus affected protocol tests pass.

### G4 - Review and rework integration

Refactor Software Design independent-review mode and shared workflow so review first challenges contract conformance, then independently challenges unplanned engineering risk. Define actionable finding content and route implementation nonconformance, workplan/design deficiency, and new independent issues without adding a lifecycle role.

**Stage semantic closure:** a vague reviewer finding is insufficient for material rework; a plan deficiency updates/reconciles the governing authority before reimplementation; preference-only alternatives do not block acceptance.

**Stage functional closure:** review/rework semantic tests plus affected protocol tests pass.

### G5 - Workflow/version/documentation reconciliation

Reconcile `workflow-and-workplans.md`, `testing-and-validation.md`, versioning documentation, concise root/source README descriptions, and `PROTOCOL_VERSION` to 5.5.0. Update `architecture-and-design.md` only if direct consistency requires it.

**Stage semantic closure:** terminology and authority are consistent, role entrypoints remain the clearest golden path, and no generic doctrine is duplicated unnecessarily.

**Stage functional closure:** version/README/reference-route/package-source tests plus affected protocol tests pass.

### G6 - Protocol regression and scenario closure

Run the complete protocol test suite and inspect the assembled source instructions against the four task scenarios. Fix semantic ambiguity rather than satisfying strings mechanically. Re-derive the complete affected source/package surface.

**Stage semantic closure:** all Protocol 5.5 task-specific acceptance items are satisfied and no required 5.4 guardrail has been lost.

**Stage functional closure:** complete protocol regression suite passes.

### G7 - Final package acceptance

Build canonical packages once from the final source, independently validate them, update committed `dist/`, verify exact semantic source-to-dist parity, run whitespace checks, and inspect the final diff for unintended scope or stale 5.4 wording that contradicts 5.5 semantics.

Required final commands remain:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

**Final acceptance:** all required checks pass on the same assembled candidate; final requirement-to-candidate reconciliation is complete; no unresolved material design/implementation issue remains.

## Risks / redesign triggers

1. **Lossy implementation contract:** a material protected concern, requirement, known consequence, or acceptance claim can still disappear between design reasoning and workplan.
2. **Over-prescription:** suggested local realization is accidentally frozen, reducing legitimate implementation adaptability.
3. **Under-prescription:** a required implementation consequence is phrased as optional advice.
4. **Checklist ceiling:** implementers treat enumerated obligations as permission to ignore newly discovered necessary consequences or affected surfaces.
5. **Test substitution:** green focused/regression tests are treated as proof that all accepted obligations were implemented.
6. **Review substitution:** semantic conformance review is treated as a substitute for executable regression/integration.
7. **Micro-review bureaucracy:** dual closure degenerates into mandatory review after every helper/file edit instead of coherent material stages.
8. **Vague rework handoff:** reviewer findings lack evidence/corrected end state/acceptance or are sent directly to implementation when the governing workplan itself is deficient.
9. **Authority inflation:** independent review becomes a source of preference-driven redesign without material engineering benefit.
10. **Entrypoint dilution:** critical golden-path role behavior is buried in shared references and therefore easy for an agent to miss.
11. **Protocol regression:** any 5.4 guarantee is weakened, historical workplan meaning changes silently, or a new lifecycle/persistent compliance mechanism is introduced.
12. **Package drift:** generated skill packages or version/build index no longer match canonical source.

If a trigger fires, reopen only the affected design surface and preserve unrelated accepted work/evidence.

## Completion criteria

Protocol 5.5.0 is complete only when the task-specific acceptance items and G0-G7 closures above are satisfied, the final affected surface is re-derived, all canonical regression/build/package/parity/whitespace checks pass, generated `dist/` matches canonical source, and no known material obligation or reviewer concern remains unresolved.

## Frozen implementation principle

> **Preserve the concern, state the required end result and known consequences, distinguish requirements from recommendations, implement adaptively without changing frozen intent, close semantic conformance and executable behavior before handoff, and return review findings with the same fidelity required of the original design contract.**


## Completion record

Protocol 5.5 implementation-fidelity work was completed before Protocol 5.6 integration. The finalized Protocol 5.5 package state is represented by commit `e705d2192d522b83265c1994c22423f6c4b9c7e1`, which is retained in the ancestry of the Protocol 5.6 mainline. Protocol 5.7 reconciles the stale directory/status metadata only; it does not reinterpret or rerun the completed 5.5 contract.
