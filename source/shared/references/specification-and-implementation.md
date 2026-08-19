# Specification-Driven Implementation

## When a specification is needed

Create or update a specification when changing a contract consumers or persisted data rely on, such as:

- public API/CLI/configuration behavior;
- input/output formats or inference rules;
- persisted schema/checkpoint/cache/index semantics;
- units, shapes, ordering, precision, tolerances, numerical conventions;
- backend/plugin/resource policy contracts;
- durable compatibility, migration, fallback, or error behavior.

Do not require a new specification for purely internal implementation details that do not alter a specified contract.

## Specification content

Define the minimum stable information consumers need: purpose/scope, data/API contracts, units/types/shapes, outputs, deterministic/error/fallback behavior, edge cases, compatibility/migration, persistence semantics, examples, and acceptance criteria where useful.

Current normative specifications describe accepted implemented behavior. Proposed target behavior belongs in the active workplan until accepted.

## Persistence compatibility

For durable artifacts, define READ/MIGRATE/REJECT behavior explicitly when version evolution matters. Prefer non-destructive migration for authoritative user data. Derived caches may often be invalidated and rebuilt rather than migrated.

Test representative historical forms at supported boundaries.

## Input handling

Use unambiguous format evidence where possible, provide explicit override when inference can fail, normalize to a canonical internal model, preserve material provenance/units, and validate semantic constraints after parsing.

## API evolution

Preserve compatibility by default. Use clear policy values, deprecate before removal where required, version persisted schemas when needed, bind reusable state to semantic inputs/configuration, and do not enable optimized defaults before equivalence is established.

## Implementation structure

Factor by responsibility. Separate parsing/I/O, canonical data, numerical kernels, orchestration/policy, persistence/state, and diagnostics when their invariants differ. Use optimized libraries/vectorization where appropriate without obscuring correctness.

## Error handling

Validate boundary inputs, raise actionable errors, reject unsupported/singular states when silent fallback would corrupt semantics, keep cleanup deterministic, and publish important persisted artifacts transactionally where feasible.

## Specification-code alignment

Before acceptance of a contract-changing candidate:

1. compare actual signatures/defaults/types/units/shapes with the specification;
2. compare material edge/error/fallback/persistence/resource behavior;
3. obtain design revision if implementation materially diverged from frozen target semantics;
4. update affected callers/tests/examples and compatibility notes;
5. update architecture only if architecture actually changed;
6. update release/history/version material according to repository policy;
7. generate derived documentation formats only when the project requires them;
8. add tests for newly material contracts that are easy to regress.

Specification-code parity is acceptance-critical when the specification governs a real contract. Workplan/evidence digest completeness is not part of specification parity.
