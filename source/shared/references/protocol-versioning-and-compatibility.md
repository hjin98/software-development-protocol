# Protocol Versioning and Compatibility

## Versioning

`PROTOCOL_VERSION` identifies the protocol contract.

- major: incompatible role/lifecycle or governing-doctrine change;
- minor: backward-compatible capability or doctrine addition/strengthening;
- patch: clarification or defect correction.

Protocol 5 established the governing product doctrine: material engineering requirements define the feasible solution space, and among engineering-sufficient solutions the protocol prefers the globally justified software/system design with the lowest unnecessary total complexity.

Protocol 5.1 added the optional `software-documentation` specialist without changing the two-role lifecycle.

Protocol 5.2 added the optional `repository-hygiene` specialist without changing the two-role lifecycle.

Protocol 5.3 is a backward-compatible doctrine clarification and functional-acceptance strengthening. It preserves the Protocol 5 product doctrine and two-role lifecycle while making two points explicit:

1. **Product simplicity is not process minimalism.** Simplicity primarily optimizes the engineered software/system. The engineering process is governed by sufficiency, confidence, risk reduction, and efficient use of engineering resources; materially useful design/testing/review/validation must not be omitted merely to shorten the workflow.
2. **Executable changes require affected-surface regression and integration testing.** Coverage follows the complete plausibly affected behavioral surface, including affected existing code and new code. Test workloads should be bounded when equivalent evidence is available, but coverage must not be narrowed merely to reduce execution cost.

Protocol 5.3 also explicitly separates functional regression/integration acceptance from full production qualification. Production qualification characterizes an already functionally accepted candidate using long, real, data-heavy, target-environment runs and is not a default implementation-stage requirement.

The two-role lifecycle introduced by Protocol 4 remains unchanged.

## Candidate identity

For a normal Git repository, the candidate commit plus absence of unintended product-defining working-tree changes is usually sufficient source identity. Use additional hashes/manifests only at real boundaries not represented by Git, such as mutable external datasets, model weights, generated release binaries, or other artifacts whose exact bytes materially affect interpretation.

## Evidence invalidation

Rerun a check when a changed dimension could plausibly alter its result or interpretation.

For executable changes, final affected-surface regression and integration checks must reflect the assembled candidate after all material executable edits that could invalidate earlier evidence. Intermediate checks remain valuable when they reduce fault-localization cost or downstream risk.

Do not rerun expensive scientific/production qualification merely because documentation wording, evidence paths, timestamps, unrelated administrative metadata, or hygiene-only movement/removal changed. Rerun qualification only when a dimension relevant to the qualification claim changed.

## Compatibility

Preserve software compatibility when the product contract requires it. Compatibility mechanisms create product complexity, so do not retain obsolete layers indefinitely without a supported-version or migration requirement.

Prefer invalidation/rebuild for derived caches when safer/cheaper than migration. Preserve/migrate authoritative user data when required.

## Earlier protocol versions

Completed work under earlier protocol versions remains valid historical work under the version that governed it. Do not rewrite old records merely to resemble Protocol 5.3.

Active work may adopt Protocol 5.3 directly. Earlier qualification/verification artifacts are not automatically required for 5.3 acceptance unless the current affected surface, project policy, or material engineering claim requires them.
