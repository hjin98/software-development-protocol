# Software Development Protocol

Software Development Protocol 4 is a simplicity-first, materiality-driven workflow for AI-assisted software engineering.

The governing rule is:

> **Materiality decides what must be accomplished. Simplicity decides how it should be accomplished.**

When two approaches satisfy the same material requirements, choose the one with fewer components, abstractions, states, interfaces, dependencies, workflow stages, and special cases. Complexity is justified only by a material capability or risk that the simpler design cannot satisfy.

Protocol 4 uses two role skills:

```text
software-design -> software-implementation
```

- `software-design` diagnoses root causes, chooses the simplest sufficient architecture, freezes material requirements when needed, and performs independent final review for substantial or high-risk work.
- `software-implementation` implements, refactors, tests, and validates the real product path, including target-environment or production-scale execution when that is materially necessary.

There is no separate qualification or verification lifecycle. Testing and target-environment validation are engineering activities, not parallel products. Independent review remains available through `software-design` when it adds material value.

Default workflows are intentionally short:

```text
small change:       inspect -> implement -> relevant test -> done
substantial change: design -> implement -> affected tests/real-use check -> review
```

Use workplans, gates, special harnesses, generated evidence, and automation only when they solve a real problem. Do not build a second system merely to certify the first.

`source/` is canonical. `dist/` contains the generated, ready-to-install role skill packages and is committed for convenient distribution. Whenever canonical source changes, rebuild `dist/` before committing.
