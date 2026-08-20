# Protocol Versioning and Compatibility

## Versioning

`PROTOCOL_VERSION` identifies the protocol contract.

- major: incompatible role/lifecycle or governing-doctrine change;
- minor: backward-compatible capability or doctrine addition;
- patch: clarification or defect correction.

Protocol 4 is a major revision because it replaces the four-role qualification lifecycle with two roles and makes simplicity/minimum mechanism a governing principle.

## Candidate identity

For a normal Git repository, the candidate commit plus absence of unintended product-defining working-tree changes is usually sufficient source identity.

Use additional hashes/manifests only at real boundaries not already represented by Git, such as mutable external datasets, model weights, generated release binaries, or other artifacts whose exact bytes materially affect interpretation.

Do not duplicate Git identity through universal content digests.

## Evidence invalidation

Rerun a check when a changed dimension could plausibly alter its result or interpretation. Do not rerun solely because documentation, report wording, evidence paths, timestamps, or unrelated administrative metadata changed.

## Compatibility

Preserve software compatibility when the product contract requires it. Compatibility mechanisms themselves create complexity, so do not retain obsolete compatibility layers indefinitely without a supported-version or migration requirement.

Prefer deleting derived caches and rebuilding them when that is cheaper and safer than maintaining migration code. Preserve/migrate authoritative user data when required.

## Earlier protocol versions

Completed Protocol 2/3 history remains valid historical work. Do not rewrite old records merely to resemble Protocol 4.

Active work may adopt Protocol 4 directly. Existing qualification/verification artifacts are not required for new Protocol 4 acceptance unless a project independently requires them.
