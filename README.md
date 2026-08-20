# Software Development Protocol

Software Development Protocol 5 is a globally optimized, engineering-fitness-first workflow for AI-assisted software engineering.

The governing doctrine is:

> **Seek the best globally justified engineering solution.**
>
> First satisfy the material engineering requirements: required functionality and capability, correctness, scientific or domain fidelity, reliability, resource and hardware constraints, target-scale behavior, and materially important performance and scalability. Among designs that satisfy those requirements, prefer the one with the lowest justified total complexity and maintenance surface.

Simplicity is therefore a strong design principle, not a goal that may weaken the product. Necessary complexity is justified when it materially improves capability, asymptotic scaling, resource efficiency, hardware utilization, robustness, recovery, portability, compatibility, security, or another real requirement. Complexity without such benefit is debt.

Protocol 5 also treats simplicity as a corrective feedback mechanism. Substantial design and review should look beyond the immediate diff when appropriate for duplicated functionality, duplicated authority, stale compatibility paths, repeated special cases, and opportunities for semantic reuse, consolidation, refactoring, or deletion. Reuse responsibilities and invariants, not merely text that looks similar.

Protocol 5.1 keeps the same two-role development lifecycle:

```text
software-design -> software-implementation
```

- `software-design` diagnoses root causes, defines the material engineering envelope, chooses an engineering-sufficient architecture, evaluates performance/resource/scaling tradeoffs, and performs independent review when useful.
- `software-implementation` implements, refactors, tests, measures, and validates the real product path, including representative or target-environment execution when materially necessary.

Protocol 5.1 also adds one optional specialist:

- `software-documentation` keeps an evolving AI-developed software system intellectually accessible to humans by reconciling documentation drift, refactoring degraded narratives, explaining theory and algorithms, maintaining usable guides, and publishing reproducible derived documents.

The specialist is not a third lifecycle role or an approval gate. Documentation follows accepted engineering results proportionally and must not obstruct capability-first development or create a parallel acceptance system.

There is no separate qualification or verification lifecycle. Testing, benchmarking, target-hardware execution, recovery checks, and production-scale validation are engineering activities, not parallel products. Independent review remains available through `software-design` when it adds material confidence.

Default workflows remain intentionally short:

```text
small change:       inspect -> implement -> relevant test -> done
substantial change: design -> implement/refactor -> affected tests/real-use check -> review
```

Before completion, ask whether the accepted change materially altered a public capability, scientific interpretation, durable architecture, API/configuration contract, workflow, or existing explanation. If so, reconcile the affected documentation proportionally; use `software-documentation` when that requires substantive synthesis, restructuring, theory explanation, or publication work.

Use workplans, gates, special harnesses, generated evidence, and automation only when they solve a real engineering problem.

`source/` is canonical. `dist/` contains the generated, ready-to-install skill packages and is committed for convenient distribution. Whenever canonical source changes, rebuild `dist/` before committing.
