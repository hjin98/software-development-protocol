# Protocol Versioning and Compatibility

## Versioning

`PROTOCOL_VERSION` identifies the protocol contract.

- major: incompatible role/lifecycle or governing-doctrine change;
- minor: backward-compatible capability or doctrine addition/strengthening;
- patch: clarification or defect correction.

Protocol 5 established the governing product doctrine: material engineering requirements define the feasible solution space, and among engineering-sufficient solutions the protocol prefers the globally justified software/system design with the lowest unnecessary total complexity.

Protocol 5.1 added the optional `software-documentation` specialist without changing the two-role lifecycle.

Protocol 5.2 added the optional `repository-hygiene` specialist without changing the two-role lifecycle.

Protocol 5.3 clarified that product simplicity is not process minimalism, strengthened mandatory stage-local plus final affected-surface regression/integration, optimized test cost only after required coverage is established, and separated functional acceptance from full production qualification.

Protocol 5.4 is a backward-compatible development-economy and reasoning-authority refinement. It preserves the Protocol 5 product doctrine, two-role lifecycle, and Protocol 5.3 functional-acceptance guarantees while making these points explicit:

1. **The hierarchy is lexicographic:** product engineering fitness first, minimum justified product/system complexity second, development economy third.
2. **Accepted workplans are implementation contracts:** frozen material design should not be independently re-proved during implementation unless evidence invalidates it.
3. **Redesign is evidence-triggered and bounded:** reopen only invalidated design/dependency surfaces and preserve still-valid work/evidence.
4. **Workplan inheritance is version-bound:** generic protocol obligations inherited by a workplan are those defined by the workplan's declared `protocol_version`, not whatever protocol is newest later.
5. **Development context and evidence are reusable:** avoid rediscovery, low-information inspection, and invalid reruns while preserving complete affected-surface acceptance.

The two-role lifecycle introduced by Protocol 4 remains unchanged.

## Workplan protocol binding

Every workplan that inherits protocol-wide behavior binds that inheritance to its declared `protocol_version`.

A workplan governed by version `X` continues to mean the Protocol `X` contract even after a newer protocol is released. Do not reinterpret an active or completed older plan using newer generic rules merely because the installed/latest skill changed.

An active workplan may explicitly adopt a newer backward-compatible protocol version when doing so is appropriate. Reconcile the plan against the new contract and update its `protocol_version`; do not silently upgrade it. Previously executed evidence remains reusable when no changed protocol obligation or affected product dimension can plausibly alter the evidence claim.

A workplan that targets a future protocol revision may record that target separately while remaining governed by the currently accepted protocol until the target revision is accepted.

## Candidate identity

For a normal Git repository, the candidate commit plus absence of unintended product-defining working-tree changes is usually sufficient source identity. Use additional hashes/manifests only at real boundaries not represented by Git, such as mutable external datasets, model weights, generated release binaries, or other artifacts whose exact bytes materially affect interpretation.

## Evidence invalidation

Rerun a check when a changed dimension could plausibly alter its result or interpretation.

For executable changes, stage-local evidence must correspond to the stage it accepts. Final affected-surface regression and integration checks must reflect the assembled candidate after all material executable edits that could invalidate earlier evidence. Re-derive the final affected surface rather than assuming the initial workplan remained complete.

Do not rerun expensive scientific/production qualification merely because documentation wording, evidence paths, timestamps, unrelated administrative metadata, or hygiene-only movement/removal changed. Rerun qualification only when a dimension relevant to the qualification claim changed.

## Compatibility

Preserve software compatibility when the product contract requires it. Compatibility mechanisms create product complexity, so do not retain obsolete layers indefinitely without a supported-version or migration requirement.

Prefer invalidation/rebuild for derived caches when safer/cheaper than migration. Preserve/migrate authoritative user data when required.

## Earlier protocol versions

Completed work under earlier protocol versions remains valid historical work under the version that governed it. Do not rewrite old records merely to resemble a newer protocol.

Active older workplans do not automatically adopt Protocol 5.4. They may continue under their declared version or explicitly adopt 5.4 after reconciling its authority/economy semantics. A protocol-version change alone does not require repeating still-valid evidence unless a newly adopted requirement or affected dimension invalidates the claim.
