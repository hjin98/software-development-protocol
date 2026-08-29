# Protocol Versioning and Compatibility

## Versioning

`PROTOCOL_VERSION` identifies the protocol contract.

- major: incompatible role/lifecycle or governing-doctrine change;
- minor: backward-compatible capability, doctrine, or control-plane strengthening;
- patch: clarification or defect correction.

Protocol 5 established the governing product doctrine: material engineering requirements define the feasible product space, and among engineering-sufficient solutions the protocol prefers the globally justified software/system design with the lowest unnecessary total complexity.

Protocol 5.1 added the optional `software-documentation` specialist. Protocol 5.2 added the optional `repository-hygiene` specialist. Protocol 5.3 strengthened stage-local/final functional acceptance and separated production qualification. Protocol 5.4 added development-economy, accepted-workplan authority, bounded redesign, version-bound workplan inheritance, evidence/context reuse, coherent stage granularity, and evidence-directed review.

Protocol 5.5 is a backward-compatible **implementation-fidelity and workflow-integration refinement**. It preserves the Protocol 5 doctrine, two-role lifecycle, and Protocol 5.3/5.4 acceptance/economy guarantees while adding lossless Design -> Implementation translation, protected-concern preservation, required-consequence versus suggestion/delegation distinctions, minimum-known-contract semantics, dual semantic/functional stage closure, final accepted-contract reconciliation, and lossless review/rework routing.

Protocol 5.6 is a backward-compatible **proxy-proof acceptance and test-double-boundary strengthening**. It preserves all earlier Protocol 5 guarantees while adding explicit semantic-owner-under-acceptance, allowed test-double boundary, proxy-proof counterfactual, real-owner handoff, and independent-review challenge rules. Material acceptance may use bounded fakes below/outside the required real owner; it may not replace or bypass that owner and then claim the owner is accepted.

Protocol 5.7 is a backward-compatible **engineering-stewardship and outcome-alignment strengthening**. It preserves the exact Protocol 5 hierarchy, two-role lifecycle, and all earlier guarantees while making the stakeholder's intended durable product the shared optimization target. Workplans, tests, gates, metrics, and reports remain subordinate constraints/evidence; non-adversarial interpretation, acceptance-integrity, self-correction, and truthful non-closure take precedence over counterfeit completion. Stewardship remains bounded to accepted scope.

Protocol 5.8 is a backward-compatible **effective-compression and canonical-ownership refinement**. It intentionally preserves the material engineering semantics and historical failure-mode defenses of Protocols 5.4-5.7 while reducing always-loaded duplication. Lifecycle entrypoints retain high-salience invariants and role decision loops; detailed generic doctrine has one canonical owner where practical and is loaded when its material surface becomes relevant. Task workplans inherit generic protocol rules and preserve task-specific intent without copying protocol manuals. Stage proportionality reduces micro-gating ceremony without weakening affected-surface regression, semantic-owner acceptance, final assembled acceptance, or product-truth safeguards.

Protocol 5.9 is a backward-compatible **agent-portable deterministic-routing refinement**. It preserves the Protocol 5 hierarchy, two-role lifecycle, and all Protocol 5.4-5.8 hardening semantics unchanged while making progressive disclosure more reliable across Agent-Skills-style harnesses: role-critical task triggers route explicitly to exact linked references, domain references remain conditional, exported skill directories are first-class runtime bundles, and generic Agent Skill conformance is separated from vendor-adapter validation. The release changes reference reachability and distribution mechanics, not engineering doctrine.

The two-role lifecycle remains unchanged:

```text
software-design -> software-implementation
```

## Workplan protocol binding

Every workplan that inherits protocol-wide behavior binds that inheritance to its declared `protocol_version`.

A workplan governed by version `X` continues to mean the Protocol `X` contract after newer releases. Do not reinterpret an active or completed older plan using newer generic rules merely because the installed/latest skill changed.

An active workplan may explicitly adopt a newer backward-compatible protocol version after reconciling changed obligations and updating `protocol_version`; do not silently upgrade it. Previously executed evidence remains reusable when no changed protocol obligation or affected product dimension can plausibly alter its claim.

## Candidate identity

For a normal Git repository, the candidate commit plus absence of unintended product-defining working-tree changes is usually sufficient source identity. Use additional hashes/manifests only at real boundaries not represented by Git.

## Evidence invalidation

Rerun a check when a changed dimension could plausibly alter its result or interpretation. Stage-local evidence must correspond to the stage it accepts; final affected-surface regression and integration must reflect the assembled candidate after all material executable edits that could invalidate earlier evidence.

Semantic/conformance closure and functional evidence are separate claims. A protocol-version adoption may require newly introduced conformance reasoning without automatically invalidating still-valid unrelated executable evidence. Do not rerun expensive scientific/production qualification merely because documentation wording, evidence paths, timestamps, unrelated administrative metadata, or hygiene-only movement/removal changed.

## Compatibility

Preserve software compatibility when the product contract requires it. Compatibility mechanisms create product complexity, so do not retain obsolete layers indefinitely without a supported-version or migration requirement.

## Earlier protocol versions

Completed work under earlier protocol versions remains valid historical work under the version that governed it. Active older workplans do not automatically adopt Protocol 5.9 or any other later release. They may continue under their declared version or explicitly adopt a newer backward-compatible version after reconciling changed obligations. A protocol-version change alone does not require repeating still-valid evidence unless a newly adopted requirement or affected dimension invalidates the claim.
