# Protocol Origin and Evolution Traceability

The protocol grew from repeated software-engineering needs: deliberate architecture for nontrivial changes, robust APIs/specifications, performance optimization with measurement, resource-aware parallelism, useful documentation, and staged testing.

Protocol v2 separated design/review from implementation. Protocol v3 further separates four authorities:

```text
software-design
software-implementation
software-qualification
software-verification
```

The four-role split addresses a real workflow problem: expensive target execution should not be mixed with source construction, and final acceptance should not be self-certified by implementation.

Early v3 hardening added universal candidate-content identities, evidence dependency manifests, retry taxonomies, output classes, artifact digest chains, and broad documentation provenance requirements. MVSEL2 dogfooding showed that these controls could themselves dominate qualification without improving confidence in the software result.

The pre-freeze v3 simplification therefore adopts a materiality-first rule: blocking protocol machinery must prevent a concrete software/evidence failure that could change acceptance. Git commit identity is the default for Git projects; additional hashes are retained at real external/generated content boundaries. Administrative metadata is advisory unless a project/release/compliance context makes it material.

Protocol evolution should remain empirical. Add a new blocking rule only when repeated or plausibly consequential failures expose a missing invariant, and prefer the simplest rule that protects the software result.
