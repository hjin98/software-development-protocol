---
kind: implementation-workplan
workplan_id: PROTOCOL-5.10-SNAPSHOT-COMPLETE-HANDOFFS
protocol_version: 5.9.0
target_protocol_version: 5.10.0
status: active
created_date: 2026-08-29
base_commit: 15765a63cf347ce913d01e14dc7d1b0699dce9b4
---

# Protocol 5.10 Snapshot-Complete Handoff Workplan

## Objective and protected concerns

Strengthen the Software Development Protocol so a Design -> Implementation handoff remains complete when the repository is transferred as a source snapshot, ZIP/tarball, copied working tree, vendored directory, or other package that does **not** preserve Git history, prior chat context, pull-request discussion, issue comments, or superseded workplan revisions.

The diagnosed failure mode is a handoff that is logically cumulative only because the current document says an earlier revision/commit is "incorporated by reference" while some still-binding task-specific requirements exist only in that historical object. Such a handoff can work for an agent with direct Git-history access yet silently lose requirements when the same current source tree is downloaded without `.git` or given to another agent as an extracted package.

Durable success is:

```text
accepted design evolution
 -> one current task contract for the handed-off scope
 -> all still-binding task-specific semantics consolidated in current snapshot artifacts
 -> source-package transfer with history removed
 -> implementer recovers the same protected concerns, frozen decisions,
    obligations, acceptance boundaries, and redesign triggers
```

Protected concerns:

1. **No Git-history dependency for normative task semantics.** Git commits, earlier workplan revisions, PR/issue comments, chat transcripts, review messages, and archived/superseded documents may provide provenance or explanation, but may not be required to reconstruct the current implementation contract.
2. **No source-package information loss.** Removing `.git` and external conversation/review history from an otherwise complete current source snapshot must not remove any still-binding task-specific requirement needed by the implementer.
3. **No regression of Protocol 5.8/5.9 effective compression.** Do not solve snapshot completeness by copying generic protocol doctrine, stable architecture manuals, specifications, or shared references into every workplan.
4. **Current-snapshot references remain valid.** A handoff may reference a stable current protocol/specification/architecture/package document when that referenced artifact is part of the declared current handoff/source snapshot and owns genuinely shared or separate semantics. The defect is historical/unavailable normative dependency, not all document composition.
5. **Revision overlays are temporary design mechanics, not final handoff authority.** Amendments, review overlays, or rework notes may be useful during design iteration, but before implementation handoff every still-binding requirement for the handed-off scope must be reconciled into the current authoritative document or explicitly bundled current-snapshot document set.
6. **No new evidence bureaucracy.** Do not require revision ledgers, provenance databases, commit manifests, or duplicate traceability matrices solely to prove handoff completeness.
7. **Implementation must not mine history for hidden requirements.** Git history remains useful for code archaeology and diagnosis, but the implementer must not need to discover normative task obligations by replaying design history.
8. **Preserve Protocol 5 doctrine and two-role lifecycle.** This is a backward-compatible control-plane/handoff strengthening only; `product engineering fitness > minimum justified product/system complexity > development economy`, Design -> Implementation authority, proxy-proof acceptance, stage-local regression, and all Protocol 5.9 routing semantics remain unchanged.

## Engineering envelope and product design

### 1. Snapshot-complete handoff contract

For any accepted workplan or equivalent Design -> Implementation task contract, the **current handed-off artifact for its scope is normative and snapshot-complete**.

Snapshot-complete means that an implementer can recover, without Git history or prior conversational context, every still-binding task-specific item needed to execute and validate the work:

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

Historical evolution may be summarized in metadata or prose, but history is not an authority layer the implementer must traverse.

### 2. The snapshot-loss counterfactual

Before Design closes a substantial handoff, apply this counterfactual:

```text
Remove:
  .git/
  prior chat/session context
  PR/issue/review discussion
  superseded or archived workplan revisions not included in the handoff

Keep:
  the current source tree/package
  the current handoff document(s)
  current normative protocol/specification/architecture files explicitly shipped with it

Question:
  Can an implementation agent still recover every material task-specific
  requirement, decision, acceptance boundary, and redesign trigger?
```

If materially **no**, handoff closure has not been achieved. Consolidate the missing semantics before implementation begins.

This counterfactual is a reasoning/contract check, not a requirement to physically delete `.git`, manufacture a second package, or create an audit artifact for every task.

### 3. Revision and amendment semantics

A workplan may evolve through multiple design/review rounds. During active design, temporary overlays or amendment files are permitted when they reduce rework or make review easier. They do not change the final handoff rule.

Before Design -> Implementation handoff:

- reconcile every accepted amendment into the current authoritative task contract for that scope;
- remove or supersede contradictory earlier wording in the current document rather than requiring the implementer to calculate precedence across historical commits;
- preserve still-valid earlier obligations explicitly in the current document rather than using phrases such as "revision N remains incorporated by reference" when revision N exists only in Git history;
- historical commit IDs/revision labels may remain as provenance, but execution must not require dereferencing them;
- if an amendment invalidates an earlier obligation, the current document must state the current requirement directly rather than relying on the reader to diff revisions.

Anti-shortcut: a current document is **not** snapshot-complete merely because it contains links or commit SHAs that would let a Git-capable agent recover omitted requirements.

### 4. Current-snapshot document composition remains allowed

Snapshot completeness must not create unnecessary duplication.

A workplan may inherit generic protocol-wide behavior from its declared `protocol_version`, and it may reference current architecture/specification/API/configuration documents when those are current authorities and are part of the same supplied repository/package or otherwise an explicitly guaranteed handoff dependency.

A substantial program may also be intentionally decomposed into current package/stage documents. In that case:

- each handed-off child document must be complete for its own task-specific scope;
- the canonical parent/index must identify the current documents needed for the handoff;
- no current child may require a superseded/historical version to recover still-binding semantics;
- historical ancestry may explain provenance but cannot be the only storage location of an obligation.

Thus Protocol 5.10 distinguishes **current compositional dependency** from **historical normative dependency**. The former is permitted when explicit and portable; the latter is forbidden for accepted handoffs.

### 5. Implementation intake contract

Software Implementation consumes the current accepted handoff as the complete task-specific authority for the stated scope.

Implementation may inspect Git history for debugging, archaeology, code ownership, or rationale when useful, but must **not** treat history mining as a normal requirement-discovery step. If the accepted handoff explicitly depends on unavailable historical material for a still-binding requirement, or appears materially incomplete after ordinary current-tree intake, route that as a **workplan/design deficiency** and reopen only the affected handoff surface rather than guessing or silently reconstructing a private contract from history.

This does not weaken the existing rule that the workplan is a minimum known contract rather than a ceiling. Implementation must still incorporate newly discovered necessary consequences and affected surfaces that preserve frozen design.

### 6. Current documentation integrity beyond workplans

The same principle applies proportionately to current normative documentation:

- current architecture/specification/user/runbook documents should describe the accepted current state without requiring readers to replay historical revisions to learn what is presently true;
- chronology belongs in history/release notes or Git history, not as a required semantic layer beneath the current document;
- a current document may compose with other current authoritative documents by explicit stable references when that reduces duplication and those documents ship together;
- generated/derived documentation may continue to have a source graph; snapshot completeness concerns normative semantic availability, not a ban on legitimate generated-document pipelines.

This strengthens the existing documentation rule that permanent current documents describe the accepted present system and are rewritten coherently when older explanations are superseded.

### 7. Minimum justified complexity

Do **not** add a mandatory handoff manifest, revision ledger, database, evidence capsule, or universal workplan parser/linter solely for Protocol 5.10.

The primary mechanism is stronger canonical contract wording in the workflow reference, high-salience Design/Implementation entrypoint instructions, and the workplan template. Repository tests should protect those protocol invariants without attempting to semantically prove arbitrary downstream workplans complete.

A project may independently add tooling when its scale/audit/release needs justify it, but Protocol 5.10 itself should remain lightweight.

### 8. Versioning

Target Protocol version is **5.10.0**.

This is a backward-compatible minor control-plane strengthening: it adds a durable handoff-portability requirement and implementation-intake constraint while preserving Protocol 5.9 doctrine, lifecycle, routing, acceptance, and effective-compression semantics.

Existing active/completed workplans remain bound to the protocol version they declare. Protocol 5.10 does not silently reinterpret Protocol 5.8/5.9 workplans. An older active plan may explicitly adopt 5.10 only after reconciling the snapshot-completeness obligation.

## Implementation obligations

### O1 - Make snapshot completeness canonical workflow doctrine

- **Concern / rationale:** current `workflow-and-workplans.md` requires lossless handoff reasoning but does not explicitly forbid storing still-binding obligations only in Git history or superseded revisions.
- **Required end state:** `source/shared/references/workflow-and-workplans.md` defines snapshot-complete handoff, historical versus current-snapshot references, amendment consolidation, and the snapshot-loss counterfactual.
- **Required consequences / constraints:** preserve existing compression/minimum-known-contract/version-binding rules; do not imply that all generic protocol/specification content must be copied into each workplan.
- **Acceptance evidence:** contract tests assert the canonical workflow contains the no-history normative rule, amendment-consolidation rule, snapshot-loss counterfactual, and allowance for current-snapshot composition.

### O2 - Make Software Design responsible for consolidated final handoff

- **Concern / rationale:** Design currently owns lossless translation but can technically close a plan whose cumulative semantics are recoverable only by following old commits.
- **Required end state:** `source/roles/software-design/SKILL.md` states, at high salience in the handoff/translation path, that final accepted handoffs must consolidate still-binding task-specific semantics and survive loss of Git/conversation history.
- **Required consequences / constraints:** do not expand the entrypoint into a duplicate workflow manual; route detail to the canonical workflow reference while retaining the decisive invariant in the entrypoint.
- **Acceptance evidence:** contract tests require explicit snapshot-complete/history-independent handoff language in the Design entrypoint and preserve existing entrypoint compression/routing tests.

### O3 - Make Software Implementation consume the current handoff, not design history

- **Concern / rationale:** an implementation agent with Git access may compensate for a deficient handoff by reconstructing requirements from old revisions, hiding the portability defect.
- **Required end state:** `source/roles/software-implementation/SKILL.md` treats the accepted current handoff as complete task-specific authority; Git-history inspection remains optional archaeology/debugging, not normative requirement discovery.
- **Required consequences / constraints:** if a material requirement is explicitly delegated to unavailable historical material, route as a workplan/design deficiency rather than guessing; preserve minimum-known-contract semantics for newly discovered implementation consequences.
- **Acceptance evidence:** contract tests assert the Implementation entrypoint distinguishes current handoff authority from optional history inspection and preserves local reconciliation/redesign behavior.

### O4 - Strengthen the implementation workplan template

- **Concern / rationale:** the template checks lossless compression but does not test portability when history disappears.
- **Required end state:** `source/shared/templates/implementation_workplan_template.md` includes a concise snapshot-complete handoff instruction/check alongside handoff closure.
- **Required consequences / constraints:** require consolidation of still-binding task-specific revisions before handoff; forbid history-only normative dependencies; allow current bundled normative references and declared current package decomposition; do not require a traceability matrix or repeated generic protocol prose.
- **Acceptance evidence:** template contract tests require snapshot-loss/history-independence language and continue to require generic protocol inheritance rather than duplication.

### O5 - Reconcile current-document documentation guidance

- **Concern / rationale:** the broader documentation discipline already prefers coherent current-state documents but should explicitly reject historical reconstruction as a prerequisite for current semantics.
- **Required end state:** `source/shared/references/documentation-and-evidence.md` states that current normative documents are semantically complete for their scope in the current snapshot, while chronology/Git history is non-normative and current cross-document composition remains allowed.
- **Required consequences / constraints:** do not ban legitimate source graphs, generated documents, cross-references, or release history; do not create a second handoff authority.
- **Affected specialist:** update `source/specialists/software-documentation/SKILL.md` only to the extent needed to keep its current-state reconciliation instructions consistent; avoid duplicating the full workflow rule.
- **Acceptance evidence:** focused documentation contract tests or existing specialist tests establish current-state semantic completeness without requiring duplication.

### O6 - Add Protocol 5.10 version semantics without altering doctrine

- **Concern / rationale:** release/version documentation must identify this as a backward-compatible handoff-portability strengthening rather than a lifecycle or philosophy change.
- **Required end state:** `source/shared/references/protocol-versioning-and-compatibility.md`, `source/PROTOCOL_VERSION`, source/root README version text, and generated package metadata describe Protocol 5.10 consistently.
- **Required consequences / constraints:** explicitly preserve Protocol 5.9 routing and all Protocol 5.4-5.9 hardening; older workplans remain version-bound and are not silently upgraded.
- **Acceptance evidence:** version tests assert `5.10.0`, the unchanged two-role lifecycle, the governing hierarchy, and explicit backward-compatible version history.

### O7 - Protect the rule with narrow contract tests

- **Concern / rationale:** prose-only protocol changes can regress during later compression/refactoring.
- **Required end state:** extend `tests/test_protocol_contracts.py` (or equivalent focused contract tests) with semantic-presence checks covering:
  - current handoff is snapshot-complete for task-specific semantics;
  - historical commits/chat/reviews are provenance, not required normative dependencies;
  - amendments are consolidated before handoff;
  - current-snapshot protocol/spec/package composition remains allowed;
  - Implementation does not need Git-history mining to discover the contract;
  - no mandatory new ledger/manifest bureaucracy is introduced.
- **Required consequences / constraints:** avoid brittle full-prose snapshots and do not attempt an unsound general semantic linter for arbitrary project workplans.
- **Acceptance evidence:** focused tests fail when the decisive invariant is removed but tolerate equivalent wording/refactoring.

### O8 - Regenerate and validate portable skill distributions

- **Concern / rationale:** Protocol 5.10 changes canonical source entrypoints/references/templates and therefore must propagate to generated ready-to-install bundles.
- **Required end state:** rebuild `dist/skills/...` and ZIP artifacts from canonical `source/`, with Protocol 5.10 metadata and identical source semantics.
- **Required consequences / constraints:** preserve Protocol 5.9 direct-root routing and generic/vendor portability architecture; no new distribution format is required.
- **Acceptance evidence:** repository unit/contract tests, build, package validation, committed-dist parity, and `git diff --check` all pass on the final candidate.

## Implementation authority

### Frozen

Implementation must preserve:

- the Protocol 5 governing hierarchy and two-role lifecycle;
- all Protocol 5.9 deterministic reference routing, portability, proxy-proof acceptance, stage-local/final regression, bounded redesign, and effective-compression behavior;
- final Design -> Implementation handoff is snapshot-complete for all still-binding **task-specific** semantics;
- Git history, prior conversation, PR/issue/review discussion, and superseded revisions are non-normative provenance at handoff time;
- accepted amendments/review corrections are consolidated into the current authoritative document for the affected scope before implementation handoff;
- current protocol/specification/architecture/package documents may remain compositional dependencies when they are current, explicit, and supplied with the handoff snapshot;
- a child/package workplan is complete for its own scope and cannot require a historical version to recover current obligations;
- Implementation is not responsible for reconstructing hidden normative requirements from Git history;
- history remains available for code archaeology/debugging/rationale where useful;
- no mandatory ledger, manifest, database, or universal semantic workplan linter is introduced solely for this rule;
- existing older workplans remain governed by their declared protocol versions unless explicitly upgraded;
- target release is Protocol 5.10.0.

### Delegated

Implementation may choose:

- exact concise wording and placement in lifecycle entrypoints, provided the high-salience invariant remains visible;
- whether documentation-specialist wording is changed directly or remains covered by its routed shared reference, provided no contradictory current-state guidance remains;
- exact focused test names and semantic-presence assertions;
- whether the template expresses the counterfactual as prose, a short checklist, or both;
- ordinary editorial consolidation needed to keep workflow/documentation/version references coherent;
- generated distribution mechanics already established by Protocol 5.9.

### Reopen only on evidence

Reopen only the affected Protocol 5.10 surface if implementation demonstrates that:

1. enforcing snapshot-complete task semantics necessarily requires duplicating large generic protocol/specification content into every workplan rather than referencing current bundled authorities;
2. an established supported workflow intentionally treats inaccessible historical revisions as normative handoff dependencies and cannot be made snapshot-portable without a material compatibility break;
3. the distinction between current-snapshot composition and historical normative dependency cannot be expressed without creating multiple conflicting authorities;
4. a narrow contract-test strategy cannot protect the invariant without an unjustified brittle prose lock or general semantic linter;
5. the proposed entrypoint additions materially undo Protocol 5.8/5.9 context compression rather than providing a concise routing/control-plane safeguard.

Do not reopen the Protocol 5 engineering hierarchy, two-role lifecycle, acceptance doctrine, or routing architecture merely because wording must be reconciled.

## Affected surface and task-specific acceptance

Initially expected affected source surface:

1. `source/shared/references/workflow-and-workplans.md` — canonical snapshot-complete handoff semantics.
2. `source/roles/software-design/SKILL.md` — high-salience Design responsibility.
3. `source/roles/software-implementation/SKILL.md` — implementation intake/history boundary.
4. `source/shared/templates/implementation_workplan_template.md` — final handoff counterfactual/check.
5. `source/shared/references/documentation-and-evidence.md` — current-document semantic completeness.
6. `source/specialists/software-documentation/SKILL.md` — only if needed for consistency.
7. `source/shared/references/protocol-versioning-and-compatibility.md` — Protocol 5.10 history/binding.
8. `source/PROTOCOL_VERSION`, `source/README.md`, root `README.md` — release identity/current description.
9. `tests/test_protocol_contracts.py` and any directly affected package/build tests.
10. generated `dist/skills/...`, ZIPs, indexes/manifests derived from canonical source.

Implementation must re-derive the final affected surface; this list is provisional.

Task-specific structural acceptance:

- no current lifecycle instruction says or implies that a Design -> Implementation handoff may omit still-binding task-specific semantics merely because Git history contains them;
- no new wording accidentally requires every workplan to duplicate generic protocol doctrine or current stable specifications;
- the Design and Implementation entrypoints agree on the same current-handoff authority boundary;
- the template contains the source-package/snapshot-loss closure check;
- current documentation guidance distinguishes present-state semantics from chronology;
- version and generated package metadata are coherent at 5.10.0.

Repository-required final checks remain the existing deterministic build/test/validation/parity/whitespace suite.

Production qualification: **unnecessary**. This is a protocol/document/control-plane change; no production-scale runtime, GPU, or data-heavy qualification claim is introduced.

## Implementation sequence and redesign risks

### Stage 1 - Canonical handoff semantics

Update the canonical workflow reference and workplan template first. Close semantic consistency around:

```text
lossless task contract
+ snapshot completeness
+ current-snapshot composition
- historical normative dependency
```

Run focused protocol/template contract tests and affected regression before dependent entrypoint edits proceed.

### Stage 2 - Lifecycle entrypoints and documentation consistency

Propagate the concise invariant to Software Design and Software Implementation, then reconcile documentation guidance/specialist wording without duplicating the canonical reference. Run affected entrypoint/routing/compression/specialist regression.

### Stage 3 - Version 5.10 release reconciliation

Update version history, version files, READMEs, tests, and generated distributions. Run the complete repository acceptance suite on the assembled candidate.

Material risks to challenge during implementation:

- **Overcorrection into duplication:** snapshot completeness must not become "copy every external contract into every workplan."
- **Weak wording:** "history should not normally be needed" is insufficient; still-binding task semantics must not depend on it.
- **False single-file absolutism:** legitimate current package/spec composition should remain possible when all required current artifacts ship together.
- **Implementation-history mining:** implementation may inspect history for engineering context but must not use that capability to excuse an incomplete accepted handoff.
- **Retroactive reinterpretation:** Protocol 5.10 must not silently invalidate or reinterpret older version-bound workplans.

## Handoff closure

Before accepting Protocol 5.10 for implementation, reconcile:

```text
user requirement:
  handoff/document remains authoritative when Git history is lost

+ existing Protocol 5 lossless Design -> Implementation translation
+ Protocol 5.8 effective compression
+ Protocol 5.9 deterministic portable routing
+ current-document authority/chronology separation

-> snapshot-complete current task contract
-> amendment consolidation before handoff
-> current-snapshot references allowed, historical normative references forbidden
-> implementation consumes current contract without history mining
-> focused contract tests + regenerated portable distributions
```

The decisive handoff counterfactual for this workplan itself is satisfied only if an implementer receiving the repository at the current tree with `.git` removed can implement Protocol 5.10 from this document plus the current normative source files it explicitly identifies, without retrieving this plan's creation conversation or any earlier unbundled revision.
