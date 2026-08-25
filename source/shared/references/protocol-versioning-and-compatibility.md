# Protocol Versioning and Compatibility

## Versioning

`PROTOCOL_VERSION` identifies the protocol contract.

- major: incompatible role/lifecycle or governing-doctrine change;
- minor: backward-compatible capability or doctrine addition/strengthening;
- patch: clarification or defect correction.

Protocol 5 established the governing product doctrine: material engineering requirements define the feasible product space, and among engineering-sufficient solutions the protocol prefers the globally justified software/system design with the lowest unnecessary total complexity.

Protocol 5.1 added the optional `software-documentation` specialist. Protocol 5.2 added the optional `repository-hygiene` specialist. Protocol 5.3 strengthened stage-local/final functional acceptance and separated production qualification. Protocol 5.4 added development-economy, accepted-workplan authority, bounded redesign, version-bound workplan inheritance, evidence/context reuse, and evidence-directed review.

Protocol 5.5 is a backward-compatible **implementation-fidelity and workflow-integration refinement**. It preserves the Protocol 5 doctrine, two-role lifecycle, and Protocol 5.3/5.4 acceptance/economy guarantees while adding:

1. lossless translation from accepted design into material implementation obligations;
2. protected-concern preservation so adaptive local realization does not recreate the diagnosed failure through another mechanism;
3. explicit distinction between required implementation consequences, suggested realizations, and delegated mechanics;
4. accepted workplans as a minimum known contract rather than a ceiling on necessary consequences discovered during implementation;
5. dual semantic/conformance plus functional closure for material implementation stages;
6. final accepted-contract reconciliation before final affected-surface regression/integration;
7. lossless independent-review findings and explicit rework routing for implementation nonconformance, workplan/design deficiency, and new issues.

Protocol 5.6 is a backward-compatible **proxy-proof acceptance and test-double-boundary strengthening**. It preserves the Protocol 5 doctrine and all Protocol 5.3/5.4/5.5 guarantees while adding explicit semantic-owner-under-acceptance, allowed test-double boundary, proxy-proof counterfactual, real-owner handoff, and independent-review challenge rules. Material acceptance evidence may still use bounded fakes below/outside the required real owner; it may not replace or bypass that owner and then claim the owner is accepted.

The two-role lifecycle remains unchanged.

## Workplan protocol binding

Every workplan that inherits protocol-wide behavior binds that inheritance to its declared `protocol_version`.

A workplan governed by version `X` continues to mean the Protocol `X` contract after newer releases. Do not reinterpret an active or completed older plan using newer generic rules merely because the installed/latest skill changed.

An active workplan may explicitly adopt a newer backward-compatible protocol version after reconciling changed obligations and updating `protocol_version`; do not silently upgrade it. Previously executed evidence remains reusable when no changed protocol obligation or affected product dimension can plausibly alter its claim.

## Candidate identity

For a normal Git repository, the candidate commit plus absence of unintended product-defining working-tree changes is usually sufficient source identity. Use additional hashes/manifests only at real boundaries not represented by Git.

## Evidence invalidation

Rerun a check when a changed dimension could plausibly alter its result or interpretation. For executable changes, stage-local evidence must correspond to the stage it accepts. Final affected-surface regression and integration checks must reflect the assembled candidate after all material executable edits that could invalidate earlier evidence.

Semantic/conformance closure and functional evidence are separate claims. A protocol-version adoption may require newly introduced conformance reasoning without automatically invalidating still-valid unrelated executable evidence.

Do not rerun expensive scientific/production qualification merely because documentation wording, evidence paths, timestamps, unrelated administrative metadata, or hygiene-only movement/removal changed.

## Compatibility

Preserve software compatibility when the product contract requires it. Compatibility mechanisms create product complexity, so do not retain obsolete layers indefinitely without a supported-version or migration requirement.

## Earlier protocol versions

Completed work under earlier protocol versions remains valid historical work under the version that governed it. Active older workplans do not automatically adopt Protocol 5.6 or any other later protocol release. They may continue under their declared version or explicitly adopt a newer backward-compatible version after reconciling its changed obligations. A protocol-version change alone does not require repeating still-valid evidence unless a newly adopted requirement or affected dimension invalidates the claim.
