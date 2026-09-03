# Workflow and Workplans

Protocol 5 keeps the software-development lifecycle small in role count while allowing whatever proportionate engineering work is needed to reach and establish the correct product.

## Shared engineering objective

Every protocol actor is a steward of the stakeholder's durable software outcome. Workplans, tests, gates, metrics, reviews, and reports define constraints or provide evidence; they are not terminal objectives. Stage or final closure is earned by the product/conformance/evidence state and must never create pressure to manufacture a pass.

Long-horizon stewardship is bounded by explicit stakeholder requirements, governed contracts, the accepted engineering envelope, plausibly affected surfaces, and material maintenance/operation consequences. It does not authorize unrelated enhancements or speculative refactoring. Development economy chooses among engineering-valid product/evidence paths; it cannot justify weaker durability, hidden debt, weaker evidence, deferred known correctness work, or premature closure.

## Roles

```text
software-design -> software-implementation
```

`software-design` owns diagnosis/design, engineering-envelope definition, architecture/algorithm/resource decisions, product-complexity review, **lossless translation of accepted design into the implementation contract**, validation design, and independent review when materially useful. `software-implementation` owns code changes/refactoring, repository reconciliation, adaptive realization under accepted authority, **semantic/conformance closure**, mandatory stage-local and final affected-surface regression plus integration testing, benchmarking/validation, ordinary cleanup, and completion evidence.

Testing is not a separate authority. Independent review is a mode of Software Design, not a third lifecycle role. Production qualification is not a separate lifecycle role.

## Product simplicity versus development economy

Material engineering requirements define the feasible product space. Among engineering-sufficient solutions, prefer the product with the lowest justified total product/system complexity. Only after the required product and acceptance confidence are preserved should the development process optimize human/model/context/tool/compute/I/O/wall-time cost.

Avoid redundant, ceremonial, duplicative, rediscovery-heavy, or low-information work. Do not omit materially useful design, implementation conformance, testing, review, or validation merely because a shorter or cheaper workflow exists.

## Typical workflows

Small/local executable work may look like:

```text
inspect -> implement -> conformance + affected regression -> integration -> done
```

Substantial work normally behaves like:

```text
design and diagnose
  -> translate accepted design into lossless implementation obligations
  -> handoff closure
  -> material implementation stage
       -> semantic/conformance closure
       -> focused + affected regression
  -> next material stage as needed
  -> final accepted-contract reconciliation
  -> re-derive final affected surface
  -> final affected regression + integration
  -> independent review when warranted
       -> contract conformance challenge
       -> independent engineering challenge
       -> lossless rework finding/routing when needed
```

Production qualification is appended only when explicitly requested, required by project/release policy, or necessary to establish a material production-scale/resource/performance/hardware claim.

These are patterns, not fixed gate counts. The ordering of cheap focused tests versus conformance inspection within a stage is flexible; both dimensions must close before dependent work proceeds. Add/remove process activities according to engineering value, but do not omit required conformance or stage-local/final functional acceptance merely to reduce process cost.

## Workplans as lossless implementation contracts

Use a workplan when it materially reduces rediscovery, ambiguity, sequencing risk, cross-module drift, or downstream rework.

A useful substantial-work plan contains the objective/diagnosis and protected concerns, material engineering envelope, globally justified product design/ownership/complexity decisions, implementation obligations, implementation authority, initially expected affected surface, task-specific focused/regression/integration/structural acceptance, repository-required checks, final reconciliation, production-qualification disposition when material, implementation sequence where ordering matters, and material risks/redesign triggers.

For substantial work, preserve the stakeholder-relevant outcome and any material durable-success criterion strongly enough that downstream actors cannot optimize individual obligations while degrading the whole product. Where a known local shortcut could satisfy wording or evidence while defeating that outcome, record a concise anti-shortcut/integrity constraint; do not create a mandatory matrix or traceability ledger.

For each material obligation, preserve as applicable:

- protected concern/rationale;
- required end state;
- required constraints/preservation/forbidden behavior;
- useful expected owning/affected surface;
- required implementation consequences already determined by design;
- clearly labeled suggested realization when adaptable;
- acceptance evidence, including structural/absence evidence where behavior tests cannot prove the claim;
- stage/dependency where material.

The format is flexible; IDs/tables/matrices and persistent traceability artifacts are not required. Do not repeat generic protocol prose merely for completeness, but do not omit a known material consequence merely to compress the plan. Do not make administrative provenance, evidence filenames, report schemas, or optional telemetry acceptance requirements unless the project independently needs them.

When a material acceptance claim depends on a real production owner/consumer boundary, preserve the claim, required real owner/path, allowed test doubles, forbidden substitutions, and observable evidence to the degree needed to prevent proxy acceptance. This is task-specific contract content, not a mandatory matrix for ordinary unit tests. An explicitly frozen real-owner boundary is an acceptance decision and cannot be silently weakened as implementation-local reconciliation.

Before accepting a substantial plan, Design performs handoff closure:

```text
requirements + protected concerns + accepted design + preservation/non-goals + known consequences
    -> implementation obligations
    -> acceptance evidence
```

No material requirement or known design consequence may disappear in that translation.

### Snapshot-complete handoff

Before Design -> Implementation handoff, the accepted current handoff artifact set must be **snapshot-complete** for still-binding task-specific semantics. Reconcile accepted amendments and review corrections into supplied current authority; do not leave a requirement only in Git history, prior chat/session context, PR/issue/review discussion, superseded revisions, or an external document that is not actually supplied.

Current composition remains valid: a workplan may inherit generic rules from its declared `protocol_version` and may reference current protocol/specification/architecture/package documents when those authorities are explicit and included in the **supplied artifact set**. Snapshot completeness is not a single-file rule and does not require copying generic protocol doctrine into each workplan.

Apply the **snapshot-loss counterfactual** before closing a substantial handoff: conceptually remove `.git`, prior conversation/review history, superseded revisions not supplied, and external links/resources not supplied. If the remaining supplied current artifacts do not recover every material task-specific requirement, decision, acceptance boundary, and redesign trigger, the handoff is not closed.

Historical identifiers and links may remain provenance/navigation, but they are **not sufficient normative storage** for omitted task semantics. If Implementation discovers that a still-binding requirement depends on unavailable historical or unsupplied material, route that as a **workplan/design deficiency** rather than guessing or reconstructing a private contract from history. This does not weaken the minimum-known-contract rule for newly discovered implementation consequences.

Do not create a mandatory handoff manifest, revision ledger, provenance database, evidence capsule, or semantic workplan linter solely to enforce this rule.

## Accepted-workplan authority

An accepted workplan distinguishes **Frozen**, **Delegated**, and **Reopen only on evidence** decisions. Precedence is:

```text
explicit user/task requirements + safety/project instructions
    -> material product requirements and governed contracts
    -> accepted workplan target decisions
    -> repository evidence about actual state
    -> implementation-local discretion
```

This is not blind-plan obedience. Current code/tests provide evidence of actual state; they do not automatically override an accepted target simply because the target intentionally changes current behavior. Existing contracts remain authoritative except where the accepted plan explicitly changes them.

Implementation may locally realize or reconcile the plan while preserving frozen semantics. A suggested realization is not automatically frozen; a required implementation consequence is not optional advice.

The accepted plan is the **minimum known contract, not a ceiling**. Necessary local consequences and newly discovered affected behavior/tests/docs/configuration/persistence/consumers that preserve frozen design are incorporated and validated by implementation. Reopen design only when evidence shows that a frozen material decision cannot satisfy the engineering envelope, conflicts irreconcilably with actual ownership/contracts, is invalidated by representative measurement, or reaches a stated redesign trigger.

When reopening is necessary, identify the invalidated decision, stop dependent work, preserve unrelated accepted stages/evidence, **reopen only the affected** design surface, update/reconcile the plan, invalidate evidence only where the changed decision can plausibly affect it, and resume from the earliest materially affected stage.

Workplans inherit generic protocol obligations from their declared `protocol_version`; later protocol releases do not silently reinterpret older active/completed plans. Explicit adoption of a newer protocol version requires reconciliation of changed obligations.

## Convergent repair, review readiness, and revision economy

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

Ordinary implementation attempts and review cycles do not require a new numbered authority revision. Existing-obligation misses, unexecuted/failed tests, additional violating sites, implementation patches, generated-derivative regeneration, or clearer non-normative evidence do not by themselves mint task semantics. Projects may retain immutable revision snapshots for independent audit/concurrency needs, but ordinary version control of canonical current authority is sufficient unless project policy requires more.

For substantial work, a provisional **closure horizon** may identify material owners, contracts, state/persistence boundaries, consumers, and invariant families plausibly affected by the accepted change. It focuses implementation and helps classify unrelated findings, but it is not a scope ceiling: expand it whenever evidence establishes a plausible ownership, dependency, contract, or behavioral-impact chain.

### Development-cycle economy

After engineering fitness and product simplicity are preserved, minimize total cycle cost with high-information ordering: reproduce/diagnose before broad editing; search variants before patching an established recurring pattern; consolidate coherent edits before broad reruns; run cheap discriminating checks before family-level affected regression and cross-owner integration; reuse evidence whose claims cannot plausibly change; review deltas rather than replaying settled archaeology; and avoid requesting another comprehensive closure review until identified blocker families are closed where dependencies permit. One comprehensive review of a stable review-ready candidate is normally more valuable than repeated micro-review after each line-level repair.

## Compact working state for long gated work

For long gated sessions, carry forward enough **compact task-local state** to avoid rediscovering accepted decisions and evidence. Keep conceptually the accepted frozen decisions, open/closed obligations, accepted stages, current affected-surface deltas, still-valid evidence, invalidated evidence, and unresolved material risks/redesign triggers. Reason from the delta since the last accepted stage rather than re-deriving unchanged state.

This working state is **not a required persistent artifact**. Do not create a ledger, database, manifest, JSON schema, or parallel evidence system solely for protocol compliance. Persist task state only when the project independently needs recovery, auditability, handoff durability, or another material capability. Final acceptance still re-derives the complete affected surface independently from the assembled candidate.

## Gates and dual stage closure

Gates are value-based. Architecture/release/project gates remain optional unless project policy requires them. A material behavior-changing implementation stage is not accepted until both dimensions close:

1. **semantic/conformance closure** confirms assigned obligations are implemented or legitimately reconciled, protected concerns/frozen decisions remain satisfied, newly discovered consequences are accounted for, no unintended authority/obsolete path/material complexity regression was introduced, and material acceptance evidence has not replaced or bypassed the semantic owner whose behavior constitutes the claim; and
2. **functional closure** completes focused checks and the relevant **stage-local affected regression** for executable behavior, or carries an explicitly non-executable validation dependency to the nearest executable stage.

Define a material stage by a coherent behavior/risk boundary, not by individual files or helper edits. Several tightly coupled edits may close under one stage. Use the cheapest high-signal ordering within the stage so obvious local failures do not waste broader test cost. Semantic review never substitutes for executable regression; **green tests never prove an omitted obligation was implemented**.

Reuse still-valid intermediate evidence until a changed dimension can plausibly invalidate its claim. Do not rerun a check solely because a new agent/session began or unrelated material changed. Final assembled affected-surface regression and integration remain fresh acceptance boundaries after all material executable edits.

Use additional gates when validating a boundary before proceeding materially reduces risk or wasted downstream work, such as architecture/algorithm decisions, irreversible migration, expensive execution prerequisites, scientific semantics, or security boundaries. Do not create G0/G1/G2 merely because a template can represent them; do not remove a useful gate merely to make the process shorter or cheaper.

## Final implementation and functional acceptance

Before handoff, Implementation reconciles every material obligation against the assembled candidate, inspects for unintended/obsolete/ownership/complexity/documentation drift, and uses structural/absence evidence for removal or uniqueness claims when runtime tests cannot prove them.

For executable changes, final functional acceptance then requires re-deriving the affected surface from the assembled candidate, complete affected-surface regression, repository/project-required checks, and integration testing. When impact cannot be bounded confidently, run the broader/full available suite.

Thus final acceptance independently asks: **did we implement the accepted contract completely?** and **does the assembled affected product work?** A production run, benchmark, or qualification result cannot substitute for missing regression coverage.

## External execution

A different machine, GPU, HPC allocation, production dataset, or external service does not automatically create a handoff or qualification role. Record reproducible commands and material conditions when external execution is required. Create dedicated runners when they materially reduce repeated work/error or are product functionality.

## Documentation and hygiene

Update affected durable documentation when accepted product behavior/architecture/contracts changed. Use `software-documentation` when substantive reconciliation or publication work is useful. Use `repository-hygiene` after substantial work only when a dedicated cleanup pass materially improves repository safety/clarity.

Neither specialist is a mandatory lifecycle gate.

## Independent review and rework

Independent review remains independent and retains authority to inspect any surface needed for a sound conclusion. It should first challenge accepted-contract conformance, then challenge unplanned engineering risks and design premises, including functionality/correctness, scientific fidelity, scaling/resources/hardware/performance, product complexity/ownership, failure handling, affected surfaces, stage-local/final regression, integration, broader checks, unavailable checks, and qualification boundaries.

Material blocking findings should identify the violated requirement/invariant or new concern, evidence, affected surface, why it matters, required corrected end state/constraint, acceptance evidence, and routing when material.

Route rework as:

- **implementation nonconformance** -> same accepted design/workplan, implementation repair;
- **workplan/design deficiency** -> reconcile the affected governing design/workplan before reimplementation;
- **new independent issue** -> local implementation consequence or evidence-backed bounded redesign.

Equivalent preferences without material engineering benefit are not acceptance blockers. No separate verification report is required unless project/release/compliance policy independently requires one.
