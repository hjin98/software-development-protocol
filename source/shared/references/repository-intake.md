# Repository Intake

Build enough context to make the requested change safely and to bound its affected behavioral surface with appropriate confidence. Do not inventory the entire repository when ownership, dependencies, and impact are already clear.

## Start focused and expand on evidence

1. read applicable repository instructions;
2. locate the requested entry point/module/feature;
3. follow callers, dependencies, persisted state, tests, and owning documentation until the material ownership and affected surface are understood;
4. inspect relevant build/CI/configuration/security/release surfaces when the change touches them;
5. preserve unrelated user changes.

Use progressive inspection rather than exhaustive reconnaissance. Process efficiency means avoiding unrelated inspection, not stopping before plausible transitive impact has been understood.

## Change surface

For substantial work, identify the material surfaces that actually apply: public API, data contracts, callers/consumers, configuration, tests, persistence, concurrency/orchestration, performance, security/trust, documentation, packaging/release, and transitive shared dependencies.

Do not create a mandatory matrix when most rows are irrelevant. Conversely, do not equate the Git diff with the behavioral surface when shared contracts propagate beyond changed files.

## Prefer existing patterns

Inspect adjacent implementation before introducing a new abstraction. Reuse an existing component when it can own the responsibility cleanly.

Do not split modules, introduce frameworks, or reorganize unrelated areas merely because the repository could be cleaner in general. Refactor when it materially improves the requested change or removes an identified failure surface.

## Generated artifacts

Determine source versus generated output before editing. Edit the source of truth and regenerate required derivatives.

When a generated artifact is shipped or committed by policy, validate both its consumer-facing structure/behavior and its parity with canonical source. Generated scratch/build artifacts should not be committed unless repository policy makes them authoritative.

## Repository safety

Do not delete, revert, overwrite, or broadly reformat unrelated work. Do not change dependency versions merely for local convenience. Do not commit secrets, machine-specific paths, large transient data, caches, or benchmark noise.
