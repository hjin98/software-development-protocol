# Specification-Driven Implementation

## Contract-first cases

Create or update a specification when changing any of:

- public function/class/protocol behavior;
- CLI commands/flags or configuration keys;
- input/output file formats and format inference;
- data model, schema, serialization, checkpoints, caches, journals, indexes, or persisted metadata;
- units, shapes, indexing, ordering, precision, tolerances, or numerical conventions;
- backend interfaces, plugin points, callback/progress contracts, or resource policies;
- cross-module ownership or lifecycle rules.

## Specification contents

Define only what downstream users/implementers need to rely on:

1. purpose and motive;
2. scope/non-goals;
3. theory/context where necessary to interpret behavior;
4. public data structures and function signatures;
5. input types, units, shapes, ranges, required/optional fields, and normalization;
6. output types, units, ordering/determinism, and provenance;
7. errors/warnings/fallback semantics;
8. edge cases and unsupported regimes;
9. compatibility, versioning, deprecation, and migration behavior;
10. persistence/storage contract when material: artifact class (authoritative/output/checkpoint/cache/temp), identity/invalidation, atomicity, retention/eviction, recovery/migration, and footprint expectations;
11. examples and acceptance criteria;
12. owning source modules and related specs when the repository uses ownership maps.

Keep implementation details out of the public contract unless consumers must depend on them. The specification describes **accepted current implemented behavior only**. Proposed/future behavior belongs in an Implementation Workplan or explicitly non-normative proposal until implementation is accepted; do not mix `PLANNED`/`PROPOSED` clauses into the current normative contract by default.

## Persisted schema compatibility and migration

For durable artifacts that must survive software evolution, define compatibility explicitly rather than relying on package-version comparison alone. A useful matrix is:

```text
reader implementation/schema version x artifact schema version
    -> READ | MIGRATE | REJECT
```

Specify:

- the authoritative artifact/schema version field;
- which historical versions remain readable;
- whether migration is in-memory, copy-on-write, write-new/read-old, or destructive;
- whether rollback to older software remains possible after migration;
- whether new software writes only the newest format while reading older supported formats;
- how interrupted migration is detected/recovered;
- whether derived caches/indexes should migrate at all or simply be invalidated and rebuilt.

Prefer non-destructive/copy-on-write migration for authoritative user data. Never mutate authoritative input merely because a newer reader can rewrite it. Keep representative historical fixtures and test read/migrate/reject behavior across supported boundaries.

## Input and format handling

When supporting multiple formats:

- Prefer robust, documented format identification from unambiguous extensions, filenames, magic/signatures, or parser metadata.
- Do not guess when evidence is ambiguous.
- Provide an explicit user override when inference can fail or multiple interpretations are plausible.
- Normalize formats into one internal data model before downstream analysis where feasible.
- Preserve source provenance and units needed for audit/reproducibility.
- Validate semantic constraints after parsing; a syntactically valid file can still be scientifically/operationally inadmissible.

## API evolution

- Preserve existing positional/keyword behavior by default.
- Prefer keyword-only additions for optional policy controls when this avoids ambiguity.
- Use explicit enums/literals/protocols for stable policy values rather than ad hoc strings spread through consumers.
- Deprecate before removal when compatibility expectations require it; keep aliases thin and centrally resolved.
- Version persisted schemas and define migrations/read compatibility where long-lived artifacts exist. Bind reusable caches/checkpoints to the inputs/configuration/algorithm identity that affects their semantics; file existence alone is not validity.
- Do not change defaults to an optimized/automatic backend until equivalence and representative behavior are established.

## Implementation structure

- Factor by responsibility, not arbitrary function length.
- Separate parsing/I/O, canonical data structures, numerical kernels, orchestration, policy selection, caching/state, and presentation/diagnostics when they have different invariants or test needs.
- Reuse stable project utilities before adding parallel abstractions.
- Add a dependency only when it materially reduces complexity/risk or provides a proven optimized kernel; consider install size, portability, license, maintenance, and optionality.
- Keep hot numerical code in vectorized/compiled operations where appropriate, but retain clear bounded Python orchestration for irregular logic.
- Keep diagnostics observational. Library code should prefer structured progress/callback/logging ports over unconditional printing unless the repository explicitly defines CLI-only behavior.

## Error handling and robustness

- Validate user-controlled sizes, ranges, paths, options, and incompatible argument combinations at boundaries.
- Raise specific, actionable errors; include the violated condition and safe remediation when possible.
- Reject singular/ill-conditioned/unsupported states explicitly when silent fallback would corrupt semantics.
- Use fallback only when it is correctness-preserving and reportable.
- Avoid broad exception swallowing. Catch only errors the layer can interpret or augment.
- Keep deterministic cleanup for temporary files/processes/resources. Publish important persisted artifacts transactionally where feasible so interrupted writes cannot masquerade as valid completion.

## Implementation/spec alignment review

Before closing the gate:

1. Compare actual signatures/defaults/types/units/shapes against the specification.
2. Compare edge/error/fallback/persistence/resource behavior.
3. If implementation materially diverged from the accepted workplan target, obtain a design/workplan revision before treating the divergence as accepted; then write the specification to the final accepted implemented contract.
4. Search affected callers/tests/examples for old assumptions.
5. Update migration/deprecation and independent schema/protocol/cache version notes if needed.
6. Update the architecture manual only when the accepted implementation actually changes current architecture; do not add task-local gate status to it.
7. Record the completed change/version in history/changelog according to repository policy, and bind final evidence to the workplan ID/revision/digest when a workplan governed the change.
8. Regenerate the authoritative Markdown specification into PDF and verify parity/layout.
9. Add a test for each newly material contract that would be easy to regress.

Specification-code parity is a mandatory acceptance check, not optional documentation cleanup.
