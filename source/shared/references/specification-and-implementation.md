# Specification and Implementation

Create or update a specification only when changing a contract that consumers, persisted data, or scientific interpretation relies on: public API/CLI/configuration, formats/schemas, units/shapes/order/precision, persistence semantics, compatibility/migration, backend policy, or durable error/fallback behavior.

Do not create specifications for purely internal implementation details.

## Keep contracts minimal

Specify the stable information consumers actually need. Avoid exposing implementation details that unnecessarily constrain future simplification.

## Implementation structure

Factor by genuine responsibility, not by arbitrary size targets. A single clear function is better than a network of helpers when responsibilities do not actually differ.

Separate layers when they own materially different invariants or lifecycle concerns. Do not split merely to increase abstraction.

Prefer canonical internal representations and one authoritative state. Avoid synchronized copies and parallel code paths unless necessary.

## Compatibility

Preserve compatibility when it is a real supported contract. Do not add speculative compatibility layers for hypothetical users or indefinitely retain obsolete paths after the supported migration window.

Derived caches can often be invalidated/rebuilt instead of migrated. Authoritative user data may require explicit migration.

## Error handling

Validate meaningful boundaries and raise actionable failures. Do not hide invariant violations behind broad fallbacks. Keep cleanup deterministic where it materially protects resources or state.

## Alignment

Before accepting a contract-changing implementation, compare actual behavior with the specification, update affected consumers/tests/examples, and update architecture only when architecture actually changed.
