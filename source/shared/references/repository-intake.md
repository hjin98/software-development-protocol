# Repository Intake

Build enough context to make the requested change safely. Do not inventory the entire repository when the target path and its dependencies are already clear.

## Start focused

1. read applicable repository instructions;
2. locate the requested entry point/module/feature;
3. follow its callers, dependencies, persisted state, tests, and owning documentation only as far as needed;
4. inspect relevant build/CI/configuration when the change touches them;
5. preserve unrelated user changes.

Use progressive inspection rather than exhaustive reconnaissance.

## Change surface

For substantial work, identify the material surfaces that actually apply: public API, data contracts, callers, tests, persistence, performance, security/trust, documentation, packaging/release.

Do not create a mandatory matrix when most rows are irrelevant.

## Prefer existing patterns

Inspect adjacent implementation before introducing a new abstraction. Reuse an existing component when it can own the responsibility cleanly.

Do not split modules, introduce frameworks, or reorganize unrelated areas merely because the repository could be cleaner in general. Refactor when it materially improves the requested change or removes an identified failure surface.

## Generated artifacts

Determine source versus generated output before editing. Edit the source of truth and regenerate only required derivatives.

Generated scratch/build artifacts should not be committed unless repository policy makes them authoritative.

## Repository safety

Do not delete, revert, overwrite, or broadly reformat unrelated work. Do not change dependency versions merely for local convenience. Do not commit secrets, machine-specific paths, large transient data, caches, or benchmark noise.
