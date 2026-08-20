---
name: software-implementation
description: Implement, refactor, test, and validate software under Protocol 4. Use the simplest sufficient mechanism, fix root causes in the owning layer, prefer deletion and redesign over accumulating patches, and test through the real product path.
---

# Software Implementation

Implement the requested behavior with the least necessary mechanism.

## Governing rule

> **Materiality decides what must be accomplished. Simplicity decides how it should be accomplished.**

Do not write a thousand lines, ten helpers, or a new subsystem for a problem that can be solved cleanly with substantially less machinery.

## Before editing

Understand the owning code path, material contracts, repository instructions, and any governing workplan. Inspect progressively rather than performing repository-wide reconnaissance without need.

If the existing design is already failing through accumulated wrappers, fallbacks, state translations, retries, or duplicated paths, do not automatically add another layer. Consider simplification or redesign first.

## Implement cleanly

Prefer:

- direct control flow;
- one authoritative state;
- small cohesive functions/modules;
- established project patterns;
- deletion of obsolete paths;
- refactoring that reduces duplication and special cases;
- standard-library or existing project mechanisms over new dependencies where sufficient.

Create an abstraction only when it removes real duplication, isolates a genuine responsibility, enforces a material boundary, or clearly improves the design.

Do not build speculative extension points or compatibility machinery without a current requirement.

## Fixes and redesign

For a clear local defect, make the smallest clean owning-layer fix and add the narrowest useful regression evidence.

Escalate to refactor/redesign when repeated fixes target the same mechanism, another fix would add structural debt, ownership is wrong, state is duplicated, control flow is becoming exceptional, or the existing algorithm cannot meet material scale/reliability requirements cleanly.

A successful bug fix should not leave the system materially harder to understand or maintain.

## Testing and validation

Testing is part of implementation. Use three levels as needed:

1. **Focused** — unit, regression, property, numerical, or boundary checks for the mechanism.
2. **Integrated** — exercise the real consumer/path/state transition.
3. **Real use** — representative or production/target-environment execution when needed to establish the material claim.

Not every task needs every level. Stop when the material question is answered with adequate confidence.

Prefer the real product interface over a parallel test implementation. Do not substantially reconstruct or duplicate production logic merely for testing.

Run production scale only when scale itself is material or smaller execution cannot establish the requirement.

## Resource safety

Do not exhaust the host. Honor explicit CPU/RAM/VRAM/storage/wall-time constraints and use reasonable containment when runaway behavior is plausible.

Use a smaller representative workload when it answers the same material question. Do not build a resource-discovery, calibration, admission, supervisor, checkpoint, or scavenging framework solely because a test is expensive.

If the product itself requires such machinery, implement and test it as product functionality.

## External environments

When workstation, HPC, GPU, production data, package-install, or other external execution is materially required, run the actual product there or provide the shortest reproducible command/conditions needed to do so.

Create a dedicated runner only when automation independently reduces real repeated work or error. A different machine does not by itself require a qualification lifecycle.

Never fabricate unavailable execution results.

## Documentation and cleanup

Update public/specification/architecture documentation only when its owned contract actually changed.

Delete obsolete helpers, experimental paths, stale compatibility layers, generated scratch, and superseded task-local machinery when safe. Git history is usually sufficient history; do not preserve dead machinery merely because it once existed.

## Completion

Report what materially changed, tests/real-use checks actually run, limitations or external checks still needed, and any unresolved design problem. Keep the report proportional to the work.
