# Repository Intake

Build enough context to make the requested change safely and to bound its affected behavioral surface with appropriate confidence. Do not inventory the entire repository when ownership, dependencies, and impact are already clear.

## Start focused and expand on evidence

1. read applicable repository instructions;
2. locate the requested entry point/module/feature;
3. follow callers, dependencies, persisted state, tests, and owning documentation until the material ownership and affected surface are understood;
4. inspect relevant build/CI/configuration/security/release surfaces when the change touches them;
5. preserve unrelated user changes.

Use progressive inspection rather than exhaustive reconnaissance. Process efficiency means avoiding unrelated inspection, not stopping before plausible transitive impact has been understood.

## Information gain and context economy

Choose the lowest-cost next inspection, search, test, benchmark, or other read-only action that most strongly resolves a material uncertainty or establishes required acceptance evidence.

- Prefer targeted symbol/search/range inspection before loading an entire large file when the bounded view is sufficient.
- Reuse repository facts already established in the current task until later evidence invalidates them; do not reread unchanged material without a new material question.
- Prefer an inspection or test that distinguishes among remaining materially plausible explanations over broad speculative reconnaissance.
- Expand scope through a plausible ownership, dependency, contract, or behavioral-impact chain rather than adjacency alone.
- When command/test/build output is large, preserve the full output when materially useful but bring the smallest sufficient summary/failing region into active reasoning context. Do not hide warnings/failures that may affect acceptance.
- Combine closely related read-only queries when that reduces turns without broadening the investigated surface or obscuring evidence.
- Avoid repeatedly reloading a governing workplan or reference solely to restate already-established decisions; consult it again when a new question depends on exact wording or later evidence may have invalidated an assumption.

Context minimization is never permission to omit required affected behavior, material failure evidence, or a transitive dependency that can plausibly change the result.

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
