---
kind: implementation-workplan
workplan_id: PROTOCOL-5.10-SNAPSHOT-COMPLETE-HANDOFFS
protocol_version: 5.9.0
target_protocol_version: 5.10.0
status: frozen
created_date: 2026-08-29
frozen_date: 2026-08-29
base_commit: 15765a63cf347ce913d01e14dc7d1b0699dce9b4
design_baseline_commit: e4e4e4ba6dbab75a42a6751c2d51a538309e4452
---

# Protocol 5.10 Snapshot-Complete Handoff Workplan

## Objective and protected concerns

Strengthen the Software Development Protocol so a Design -> Implementation handoff remains complete when a repository is transferred as a source snapshot, ZIP/tarball, copied working tree, vendored directory, or other package that does **not** preserve Git history, prior chat context, pull-request discussion, issue comments, or superseded workplan revisions.

The diagnosed failure mode is narrow: a current handoff can appear complete only because it says an earlier revision/commit is "incorporated by reference" while some still-binding task-specific requirements exist only in that historical object. Such a handoff works for an agent with Git-history access but can silently lose requirements when the same current source tree is downloaded without `.git` or passed to another agent as an extracted package.

Durable success is:

```text
accepted design evolution
 -> one current task contract for the handed-off scope
 -> all still-binding task-specific semantics present in current handoff artifacts
 -> source-package transfer with history removed
 -> implementer recovers the same protected concerns, frozen decisions,
    obligations, acceptance boundaries, and redesign triggers
```

Protected concerns:

1. **No Git-history dependency for normative task semantics.** Git commits, earlier workplan revisions, PR/issue comments, chat transcripts, review messages, and archived/superseded documents may provide provenance or explanation, but may not be required to reconstruct the current implementation contract.
2. **No source-package information loss.** Removing `.git` and external conversation/review history from an otherwise complete current handoff artifact set must not remove any still-binding task-specific requirement needed by the implementer.
3. **No regression of Protocol 5.8/5.9 effective compression.** Snapshot completeness must not be implemented by copying generic protocol doctrine, stable architecture manuals, specifications, or shared references into every workplan.
4. **Current-snapshot composition remains valid.** A handoff may reference current protocol/specification/architecture/package documents when those documents are explicit current authorities and are physically included in the supplied handoff artifact set.
5. **Revision overlays are design mechanics, not final handoff authority.** Amendments/review overlays may be useful during design, but every still-binding task-specific requirement must be reconciled into the current authoritative handoff before implementation begins.
6. **No new evidence bureaucracy.** Protocol 5.10 does not require revision ledgers, provenance databases, handoff manifests, commit manifests, evidence capsules, duplicate traceability matrices, or a universal semantic workplan linter.
7. **Implementation must not mine history for hidden requirements.** History remains useful for archaeology/debugging/rationale, but normative task obligations must be discoverable from the current accepted handoff.
8. **No prior-doctrine drift.** Protocol 5.10 is a handoff-portability/control-plane strengthening only. It must not change the governing hierarchy, lifecycle, workplan authority, acceptance semantics, proxy-proof boundaries, stewardship rules, stage/regression rules, evidence reuse, bounded redesign, production-qualification separation, or Protocol 5.9 routing/distribution architecture.

## Scope freeze — Protocol 5.4-5.9 is preservation territory

This workplan authorizes **one semantic addition only**: accepted Design -> Implementation handoffs become snapshot-complete for still-binding task-specific semantics.

Existing Protocol 5.4-5.9 doctrine and hardening are not redesign surfaces under this workplan. In particular, preserve unchanged in normative meaning:

- the governing hierarchy exactly as `product engineering fitness > minimum justified product/system complexity > development economy`;
- the two-role lifecycle `software-design -> software-implementation` and optional-specialist/non-gate status;
- accepted-workplan authority, minimum-known-contract semantics, local reconciliation, bounded redesign, and version-bound inheritance;
- coherent material-stage semantics, dual semantic/conformance plus functional closure, stage-local affected regression, final affected-surface re-derivation/regression, real-boundary integration, and repository-required checks;
- evidence reuse/invalidation and the separation of production qualification from functional acceptance;
- lossless Design -> Implementation translation, protected-concern preservation, required consequence versus suggestion/delegation distinctions, final accepted-contract reconciliation, and structural/absence evidence where appropriate;
- proxy-proof semantic-owner/test-double boundaries and the prohibition on accepting a real-owner claim through mocks/bypasses/reimplementations of that owner;
- stakeholder-product truth, non-adversarial interpretation, anti-acceptance-gaming rules, truthful non-closure, and bounded stewardship;
- Protocol 5.8 canonical detailed ownership, progressive disclosure, effective compression, and stage proportionality;
- Protocol 5.9 deterministic reference routing, self-contained direct-root skill bundles, generic Agent Skill versus vendor-adapter separation, package validation, and real-harness qualification boundaries.

Permitted normative changes are limited to:

- adding the snapshot-complete handoff rule and its precise current-vs-historical dependency boundary;
- adding minimal lifecycle-entrypoint wording needed to make that rule high-salience;
- adding the corresponding current-document clarification to the shared documentation reference;
- updating the workplan template with the snapshot-loss handoff check;
- adding Protocol 5.10 version/release wording;
- adding narrow regression tests for these new invariants;
- regenerating existing Protocol 5.9 distributions from canonical source.

Prohibited under this workplan:

- rewriting, compressing, expanding, reorganizing, strengthening, weakening, rebalancing, or "cleaning up" unrelated existing doctrine merely because different wording seems preferable;
- deleting/merging a prior hardening safeguard because snapshot completeness or deterministic routing is expected to make it redundant;
- changing role responsibility, stage semantics, testing/acceptance doctrine, proxy-proof semantics, stewardship doctrine, architecture/design doctrine, or release/qualification semantics;
- repository-wide documentation normalization unrelated to the new handoff invariant;
- using this release as an opportunity for unrelated refactoring of skills, references, build tooling, or package structure.

Any genuine defect discovered in preserved doctrine is outside Protocol 5.10 and requires a separate Software Design task. It must not be folded into this implementation.

## Engineering envelope and product design

### 1. Snapshot-complete handoff contract

For any accepted workplan or equivalent Design -> Implementation task contract, the **current handed-off artifact set for its scope is normative and snapshot-complete**.

Snapshot-complete means an implementer can recover, without Git history or prior conversational/review context, every still-binding task-specific item needed to execute and validate the work:

- stakeholder outcome and protected concerns;
- diagnosis/root cause when it constrains the solution;
- frozen requirements, invariants, non-goals, ownership, architecture, algorithm/resource/compatibility decisions;
- required implementation consequences;
- delegated mechanics and suggested realizations where their distinction matters;
- acceptance criteria and real semantic-owner/test-double boundaries;
- stage/dependency requirements that materially constrain sequencing;
- preservation obligations and forbidden shortcuts;
- redesign/reopen triggers;
- current task-specific qualification disposition.

Historical evolution may be summarized as provenance, but history is not an authority layer the implementer must traverse.

### 2. Handoff artifact-set boundary

A normative dependency is portable only when the required artifact is **actually included in the handed-off artifact set**.

Valid composition includes, for example:

```text
source snapshot
 + current workplan
 + current protocol references included in that snapshot
 + current architecture/specification/package documents included in that snapshot
```

A URL, commit SHA, PR/issue identifier, conversation reference, or statement that another repository/document contains the missing requirement is **not sufficient normative storage** by itself. Such references may remain provenance/navigation. If an external document is truly normative for the handoff, it must itself be explicitly supplied as part of the handoff artifact set or its semantics must be consolidated into a supplied current authority.

This rule preserves legitimate current multi-document composition while closing the same information-loss hole through external or historical indirection.

### 3. Snapshot-loss counterfactual

Before Design closes a substantial handoff, apply this counterfactual:

```text
Remove:
  .git/
  prior chat/session context
  PR/issue/review discussion
  superseded or archived revisions not included in the handoff
  external links/resources not actually supplied with the handoff

Keep:
  the current supplied source/package
  the current handoff document(s)
  current normative protocol/specification/architecture/package files supplied with it

Question:
  Can an implementation agent still recover every material task-specific
  requirement, decision, acceptance boundary, and redesign trigger?
```

If materially **no**, Design -> Implementation handoff closure has not been achieved. Consolidate or supply the missing current authority before implementation begins.

This is a reasoning/contract counterfactual, not a requirement to physically delete `.git`, create a second archive, or add a mandatory audit artifact.

### 4. Revision and amendment semantics

A workplan may evolve through multiple design/review rounds. Temporary overlays or amendment files remain allowed during active design when useful.

Before final Design -> Implementation handoff:

- reconcile every accepted amendment/review correction into the current authoritative task contract for that scope;
- remove/supersede contradictory earlier wording in the current contract rather than requiring precedence calculation across old revisions;
- preserve still-valid earlier obligations directly in the current contract rather than relying on "revision N remains incorporated by reference" when revision N is absent from the supplied artifact set;
- historical commit IDs/revision labels may remain as provenance, but execution must not require dereferencing them;
- when a later revision invalidates an earlier obligation, state the current requirement directly rather than requiring the implementer to diff history.

Anti-shortcut: a current document is not snapshot-complete merely because a Git-capable or web-connected agent could retrieve the omitted requirement.

### 5. Current document/package composition remains allowed

Snapshot completeness must not create unnecessary duplication.

A workplan may inherit generic protocol-wide behavior from its declared `protocol_version`. It may also reference current architecture/specification/API/configuration/package documents when those are current authorities for distinct/shared semantics and are included in the actual handoff artifact set.

A substantial program may intentionally decompose work into current package/stage documents. In that case:

- each handed-off child is complete for its own task-specific scope;
- the canonical parent/index identifies the current documents required for the handoff;
- every required current document is included in the handoff artifact set;
- no child requires a superseded/historical version to recover current obligations;
- historical ancestry may explain provenance but cannot be the only storage location of an obligation.

Protocol 5.10 therefore distinguishes **current supplied composition** from **historical/external normative dependency**. The former is permitted; the latter is not sufficient for accepted handoff closure.

### 6. Software Implementation intake contract

Software Implementation consumes the accepted current handoff artifact set as the complete task-specific authority for the stated scope.

Implementation may inspect Git history for debugging, archaeology, code ownership, or rationale when useful, but must not treat history mining as the normal way to discover normative requirements. If the accepted handoff explicitly depends on unavailable historical/external material for a still-binding requirement, or is materially incomplete after ordinary current-tree intake, route that as a **workplan/design deficiency** and reopen only the affected handoff surface rather than guessing or silently reconstructing a private contract from history.

This does not weaken the existing minimum-known-contract rule. Implementation must still discover and implement necessary local/affected-surface consequences that preserve the frozen design.

### 7. Current normative documentation integrity

Apply the same principle proportionately to current normative documentation: present current semantics must not require replaying historical revisions.

The Protocol 5.10 implementation itself is narrow:

- add the current-snapshot semantic-completeness clarification to `source/shared/references/documentation-and-evidence.md`;
- preserve legitimate current cross-document references and generated-document source graphs;
- keep chronology in history/release notes or Git history as non-current authority;
- **do not** launch a repository-wide documentation rewrite/audit;
- treat `source/specialists/software-documentation/SKILL.md` and unrelated architecture/specification/user/runbook files as **preservation-only** unless direct evidence shows an actual contradiction that prevents the shared rule from being honored.

If such a contradiction is discovered, make only the minimum additive/connective correction required by the accepted rule; do not use it for general editorial refactoring.

### 8. Minimum justified complexity

Do not introduce a mandatory handoff manifest, revision ledger, database, evidence capsule, universal parser/linter, or new approval stage solely for Protocol 5.10.

The primary mechanism is canonical workflow wording, concise lifecycle-entrypoint safeguards, the workplan template, current documentation guidance, and narrow contract tests. A project may independently add stronger tooling when its own scale/audit requirements justify it.

### 9. Versioning

Target Protocol version is **5.10.0**.

This is a backward-compatible minor control-plane strengthening: it adds a durable handoff-portability requirement and implementation-intake constraint while preserving Protocol 5.9 doctrine, lifecycle, routing, acceptance, distribution, and effective-compression semantics.

Existing active/completed workplans remain bound to their declared versions. Protocol 5.10 does not silently reinterpret Protocol 5.8/5.9 workplans. An older active plan may explicitly adopt 5.10 only after reconciling the new snapshot-completeness obligation.

## Implementation obligations

### O1 - Add snapshot completeness to the canonical workflow owner

- **Concern:** current lossless-handoff doctrine does not explicitly forbid normative requirements living only in history/superseded revisions.
- **Required end state:** `source/shared/references/workflow-and-workplans.md` defines snapshot-complete handoff, the supplied artifact-set boundary, revision consolidation, and the snapshot-loss counterfactual.
- **Constraints:** additive/minimal-connective edit only; existing workflow doctrine is preservation territory; preserve effective compression, minimum-known-contract semantics, stage/regression rules, bounded redesign, workplan authority, and version binding unchanged.
- **Acceptance:** focused contract tests assert the new rule and all pre-existing workflow/contract tests remain green without weakened assertions/fixtures.

### O2 - Make Software Design own consolidated final handoff

- **Concern:** Design can currently produce a logically cumulative plan whose missing semantics are recoverable only from old commits.
- **Required end state:** `source/roles/software-design/SKILL.md` contains one concise high-salience rule that accepted handoffs consolidate all still-binding task-specific semantics and survive loss of Git/conversation history.
- **Constraints:** do not rewrite other role doctrine; detailed semantics remain in the routed workflow reference.
- **Acceptance:** new assertion for the invariant plus unchanged existing Design routing/hierarchy/stewardship/fidelity tests.

### O3 - Make Software Implementation consume current handoff authority

- **Concern:** Git-capable implementers can hide a deficient handoff by reconstructing requirements from history.
- **Required end state:** `source/roles/software-implementation/SKILL.md` states that the accepted current handoff is complete task-specific authority; history is optional archaeology/debugging/rationale, not normative requirement discovery; unavailable historical normative dependency is a workplan/design deficiency.
- **Constraints:** preserve local reconciliation, minimum-known-contract semantics, implementation stewardship, stage/acceptance rules, and all other implementation doctrine unchanged.
- **Acceptance:** narrow new assertions plus unchanged existing Implementation contract tests.

### O4 - Strengthen the implementation workplan template

- **Concern:** handoff closure checks semantic compression but not portability when history disappears.
- **Required end state:** `source/shared/templates/implementation_workplan_template.md` adds a concise supplied-artifact/snapshot-loss check under handoff closure.
- **Constraints:** consolidate task-specific revisions; forbid history-only/external-only normative dependencies; allow supplied current protocol/spec/package composition; continue inheriting generic protocol requirements instead of duplicating them; no traceability matrix requirement.
- **Acceptance:** template tests protect both snapshot completeness and existing generic-protocol inheritance/compression guidance.

### O5 - Add one narrow current-document clarification

- **Concern:** current documentation doctrine already prefers coherent present-state documents but does not explicitly state that current semantics cannot require historical reconstruction.
- **Required end state:** `source/shared/references/documentation-and-evidence.md` states that a current normative document is semantically complete for its scope within the supplied current artifact set; chronology/history is non-normative; current supplied cross-document composition remains allowed.
- **Constraints:** additive/minimal-connective change only. `source/specialists/software-documentation/SKILL.md` and unrelated docs are preservation-only unless an actual contradiction is demonstrated.
- **Acceptance:** focused documentation contract assertion; no unrelated documentation rewrite.

### O6 - Add Protocol 5.10 release/version semantics

- **Concern:** release identity must describe one backward-compatible handoff-portability strengthening without implying broader doctrine change.
- **Required end state:** update `source/shared/references/protocol-versioning-and-compatibility.md`, `source/PROTOCOL_VERSION`, source/root README release text, and generated package metadata to 5.10.0.
- **Constraints:** version/history/connective edits only; preserve Protocol 5.9 routing and every Protocol 5.4-5.9 hardening safeguard.
- **Acceptance:** version tests assert 5.10.0, unchanged two-role lifecycle, unchanged governing hierarchy, and explicit 5.10 backward-compatible semantics.

### O7 - Protect snapshot completeness and prior hardening with narrow tests

Extend `tests/test_protocol_contracts.py` or equivalent focused contract tests to establish:

- accepted handoff task semantics are snapshot-complete;
- Git commits/chat/PR/review/history are provenance, not required normative storage;
- accepted amendments are consolidated before handoff;
- normative cross-document dependencies must be included in the supplied artifact set;
- current supplied protocol/spec/package composition remains allowed;
- Implementation does not need history mining to discover the task contract;
- no mandatory new ledger/manifest/linter bureaucracy is introduced;
- all existing Protocol 5.4-5.9 hardening tests remain present and pass without weakening/removing assertions or narrowing fixtures to accommodate 5.10.

Do not create brittle full-prose snapshots or an unsound general semantic linter for arbitrary project workplans.

### O8 - Regenerate existing portable distributions

Rebuild the existing Protocol 5.9 distribution forms from canonical `source/` after source changes.

- preserve `dist/skills/<skill-name>/...` direct-root bundles and backward-compatible ZIP artifacts;
- preserve deterministic routing and generic/vendor-adapter separation;
- do not introduce a new package format or refactor the builder unless a direct incompatibility blocks 5.10 propagation;
- validate artifact structure/metadata and committed-dist parity using the repository's established acceptance workflow.

## Implementation authority

### Frozen

Implementation must preserve:

- the complete Protocol 5.4-5.9 doctrine/hardening identified in the scope freeze;
- the exact governing hierarchy and two-role lifecycle;
- snapshot-complete final Design -> Implementation handoff for still-binding task-specific semantics;
- Git history, prior conversation, PR/issue/review discussion, superseded revisions, and unsupplied external links as non-normative provenance/navigation at handoff time;
- accepted amendment/review corrections consolidated into supplied current authority before handoff;
- current protocol/specification/architecture/package documents as valid composition only when current, explicit, and included in the handoff artifact set;
- child/package workplans complete for their own scope and independent of historical versions for current obligations;
- history available for archaeology/debugging/rationale but not required contract discovery;
- no new handoff bureaucracy or universal semantic linter;
- no repository-wide documentation rewrite/audit;
- older workplans governed by their declared protocol versions unless explicitly upgraded;
- target release 5.10.0.

### Delegated

Implementation may choose only local mechanics that do not alter frozen semantics:

- exact concise wording/placement of the new additive lifecycle safeguards;
- exact narrow test names/assertions;
- whether the template expresses the counterfactual as prose or a short checklist;
- ordinary version-number/connective wording necessary to describe 5.10 accurately;
- existing Protocol 5.9 generation mechanics for regenerated distributions.

**Not delegated:** general editorial consolidation, unrelated wording cleanup, restructuring of existing doctrine, specialist rewriting, architecture/specification normalization, package-builder refactoring, or any change whose purpose is not required by the snapshot-complete handoff feature.

### Reopen only on evidence

Reopen only the affected Protocol 5.10 surface if implementation demonstrates that:

1. snapshot-complete task semantics cannot be achieved without duplicating large generic protocol/specification content into every workplan rather than composing supplied current authorities;
2. an established supported workflow intentionally requires inaccessible history as normative handoff input and cannot become snapshot-portable without a material compatibility break;
3. supplied current composition versus historical/external dependency cannot be represented without conflicting authorities;
4. narrow contract tests cannot protect the new invariant without brittle prose locking or a general semantic linter;
5. the minimal entrypoint additions materially undo Protocol 5.8/5.9 context compression.

Do **not** reopen prior doctrine/hardening because implementation prefers different wording or structure. Any defect in preserved Protocol 5.4-5.9 semantics requires a separate design task.

## Affected surface and task-specific acceptance

Expected source surface is intentionally narrow:

1. `source/shared/references/workflow-and-workplans.md` — canonical new handoff semantics.
2. `source/roles/software-design/SKILL.md` — one concise Design safeguard.
3. `source/roles/software-implementation/SKILL.md` — one concise Implementation intake/history safeguard.
4. `source/shared/templates/implementation_workplan_template.md` — snapshot-loss handoff check.
5. `source/shared/references/documentation-and-evidence.md` — one narrow current-document clarification.
6. `source/shared/references/protocol-versioning-and-compatibility.md` — 5.10 release description.
7. `source/PROTOCOL_VERSION`, `source/README.md`, root `README.md` — release identity/current summary.
8. `tests/test_protocol_contracts.py` and directly affected existing package/version tests.
9. generated `dist/skills/...`, ZIPs, indexes/manifests produced by the existing build.

`source/specialists/software-documentation/SKILL.md`, architecture/specification/runbook documents, other references, builders/validators, and unrelated tests are **preservation-only** unless direct implementation evidence proves a minimum change is required for this feature. If so, change only the smallest necessary surface and record the evidence.

Task-specific acceptance requires:

- the new snapshot-complete handoff rule is present at the canonical workflow owner and high-salience role entrypoints;
- normative dependencies required for a handoff are in the supplied artifact set rather than only in Git/history/chat/PR/external links;
- current supplied compositional references remain allowed;
- the template includes the snapshot-loss closure check;
- documentation guidance distinguishes current semantics from chronology without broadening documentation scope;
- Protocol 5.10 version/release text is coherent;
- all existing Protocol 5.4-5.9 semantic/failure-mode/routing/acceptance hardening tests remain green without weakened assertions or fixtures;
- source review finds no substantive normative change outside the explicitly authorized handoff/version/connective additions;
- generated distributions preserve Protocol 5.9 structure/routing and match canonical source;
- repository-required unit/contract tests, package build/validation, committed-dist parity, and whitespace checks pass on the final candidate.

Production qualification: **unnecessary**. Protocol 5.10 changes protocol/document/control-plane semantics only and introduces no production-scale runtime, GPU, or data-heavy performance claim.

## Implementation sequence

### Stage 1 - Canonical rule and template

Add only the canonical workflow snapshot-completeness rule and template counterfactual. Run focused contract tests plus affected protocol/template regression before dependent entrypoint edits.

### Stage 2 - Lifecycle safeguards and documentation clarification

Add concise Design/Implementation safeguards and the narrow shared documentation clarification. Do not edit the documentation specialist unless a direct contradiction is demonstrated. Run affected lifecycle/routing/compression/documentation regression.

### Stage 3 - Version/release and distribution reconciliation

Update version/history/README text, focused tests, and regenerate existing distributions. Run the complete repository acceptance workflow on the assembled candidate.

## Material risks and anti-shortcuts

- **Overcorrection into duplication:** snapshot completeness does not mean copying generic protocol/specification content into every workplan.
- **Weak wording:** "history should not normally be needed" is insufficient; still-binding task semantics must not depend on it.
- **External-link loophole:** an unsupplied current URL is not a portable normative artifact.
- **False single-file absolutism:** multiple current supplied documents may form one handoff when their ownership is explicit.
- **Implementation-history mining:** history may explain code but cannot excuse an incomplete accepted task contract.
- **Retroactive reinterpretation:** 5.10 does not silently alter older version-bound plans.
- **Doctrine-cleanup creep:** no prior safeguard may be rewritten or removed merely because a different formulation seems cleaner.
- **Test laundering:** existing hardening tests may not be weakened, deleted, or narrowed to make 5.10 pass.

## Handoff closure

Before accepting this frozen plan for implementation, reconcile:

```text
user requirement:
  current handoff remains complete when Git/history/conversation context is lost

+ Protocol 5.4-5.9 doctrine and hardening preserved unchanged
+ existing lossless Design -> Implementation translation
+ Protocol 5.8 effective compression
+ Protocol 5.9 deterministic portable routing/distribution
+ current-document authority/chronology separation

-> snapshot-complete supplied current task contract
-> accepted revision/amendment consolidation before handoff
-> supplied current composition allowed
-> historical/unsupplied external normative dependency forbidden
-> implementation consumes current contract without history mining
-> no unrelated doctrine/document/package redesign
-> existing hardening regression unchanged + new focused contract tests
-> existing portable distributions regenerated and validated
```

This workplan itself is snapshot-complete: an implementer receiving the current repository/source package with `.git` and prior conversation/review history removed can implement Protocol 5.10 from this document plus the current normative source files it explicitly identifies, without retrieving any earlier version of this plan.
