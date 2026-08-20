# Testing and Validation

Testing exists to answer material engineering questions, not to create a parallel product.

## Three levels

Use only the levels needed:

1. **Focused** — unit, regression, property, numerical, boundary, or error checks for the mechanism.
2. **Integrated** — exercise the real consumer, interface, persistence path, or state transition.
3. **Real use** — representative real data, target hardware/environment, installed package, or production-scale execution when needed to establish the material claim.

Stop when the relevant question has been answered with adequate confidence. Do not run a fixed matrix merely because one exists.

## Prefer direct testing

Test through the actual implementation path whenever practical.

A test harness must not substantially reimplement the algorithm, state reconstruction, orchestration, or compatibility logic it is intended to test. That creates a second implementation with its own failure modes.

If the product is difficult to test, expose a smaller stable seam or refactor ownership rather than constructing a pseudo-production qualification system.

Synthetic fixtures are useful when they isolate a mechanism. They should not replace the real path when the material claim depends on real integration, data, hardware, scale, or scientific behavior.

## Scale and performance

Use the smallest workload that exercises the relevant algorithmic regime. Run full production scale when scale itself is the requirement, smaller execution cannot establish the claim, or a real campaign is the most direct useful test.

For performance claims, use a comparable baseline and representative material conditions. Do not build elaborate historical/counterfactual infrastructure solely to preserve a speedup percentage.

## Resource safety

Do not exhaust the machine. Honor explicit CPU/RAM/VRAM/storage/wall-time constraints and add simple containment when runaway behavior is plausible.

Resource safety does not imply a generic calibration/admission/supervisor framework. Measure or estimate only what is needed to run safely.

If a test itself requires extensive checkpointing, recovery, resource discovery, state reconstruction, cleanup orchestration, or other infrastructure, ask whether the product should expose a simpler test seam or whether running the actual product is more useful.

## Real failures

A real production/workstation/HPC failure is high-value evidence. Diagnose it through the product path, fix the owner, and rerun the affected path when useful.

Do not keep adding layers to a failing test harness. Simplify or remove it.

## Broad suites

Run broad tests when useful or when repository policy requires them. Attribute unrelated pre-existing failures rather than building historical machinery around them.

A required check that did not execute is not a pass. Do not fabricate unavailable environment results.

## Evidence

The command output, CI result, benchmark, or real-run log is normally enough evidence. Record additional metadata only when needed to interpret the material claim.
