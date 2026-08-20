# Protocol Versioning and Compatibility

## Versioning

`PROTOCOL_VERSION` identifies the protocol contract.

- major: incompatible role/lifecycle or governing-doctrine change;
- minor: backward-compatible capability or doctrine addition;
- patch: clarification or defect correction.

Protocol 5 is a major revision because it changes the governing doctrine from simplicity-first selection to global engineering fitness: functionality, correctness/scientific fidelity, resource feasibility, scaling, hardware effectiveness, robustness, and materially required performance define the acceptable solution space; simplicity, reuse, clean architecture, refactoring, and deletion then minimize unnecessary total complexity within that space. Protocol 5 also makes complexity-regression/consolidation review an explicit corrective mechanism.

Protocol 5.1 is a backward-compatible capability addition. It preserves the two-role lifecycle and governing doctrine while adding the optional `software-documentation` specialist plus documentation-evolution guidance. The specialist keeps evolving AI-developed software understandable and usable, but it is not a third lifecycle role, approval gate, or parallel acceptance authority.

The two-role lifecycle introduced by Protocol 4 remains unchanged.

## Candidate identity

For a normal Git repository, the candidate commit plus absence of unintended product-defining working-tree changes is usually sufficient source identity.

Use additional hashes/manifests only at real boundaries not already represented by Git, such as mutable external datasets, model weights, generated release binaries, or other artifacts whose exact bytes materially affect interpretation.

Do not duplicate Git identity through universal content digests.

## Evidence invalidation

Rerun a check when a changed dimension could plausibly alter its result or interpretation. Do not rerun solely because documentation, report wording, evidence paths, timestamps, or unrelated administrative metadata changed.

Documentation checks follow the same rule: a local product or documentation change should not be blocked by unrelated stale generated artifacts. Scope mechanical document validation to affected source chains and directly affected navigation unless a repository-wide audit or release policy independently requires broader review.

## Compatibility

Preserve software compatibility when the product contract requires it. Compatibility mechanisms themselves create complexity, so do not retain obsolete compatibility layers indefinitely without a supported-version or migration requirement.

Prefer deleting derived caches and rebuilding them when that is cheaper and safer than maintaining migration code. Preserve/migrate authoritative user data when required.

## Earlier protocol versions

Completed Protocol 2/3/4/5.0 history remains valid historical work. Do not rewrite old records merely to resemble Protocol 5.1.

Active work may adopt Protocol 5.1 directly. Existing Protocol 4/5.0 workplans and review records remain interpretable under their original version. Earlier qualification/verification artifacts are not required for new Protocol 5.1 acceptance unless a project independently requires them.
