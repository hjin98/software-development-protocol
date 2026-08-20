# Software Development Protocol 4

`source/` is the canonical Protocol 4 library.

Protocol 4 has two roles:

- `software-design` — diagnose, design, simplify, and independently review substantial changes;
- `software-implementation` — implement, refactor, test, and validate the real product behavior.

The core doctrine is:

> **Materiality decides what must be accomplished. Simplicity decides how it should be accomplished.**

## Minimum Mechanism Principle

Satisfy each material requirement with the least necessary mechanism. Every additional component, abstraction, state, interface, fallback, compatibility layer, dependency, workflow stage, and special case creates failure and maintenance surface.

When a simple and a complex solution satisfy the same requirement, choose the simple solution. Complexity requires justification; simplicity does not.

Necessary complexity is allowed. Simplicity does not justify omitting correctness, scientific rigor, safety, recovery, security, compatibility, or performance requirements. Add mechanism only when it protects a material capability or risk that a simpler design cannot satisfy.

## Default lifecycle

For ordinary work:

```text
inspect -> implement -> relevant test -> done
```

For substantial work:

```text
diagnose/design -> implement/refactor -> affected tests or real-use validation -> independent review
```

Testing, benchmarking, target-environment execution, and production-scale validation are engineering activities inside implementation. They do not require a separate qualification lifecycle.

Use a workplan only when substantial design, sequencing, expensive execution, public or persisted contracts, scientific semantics, or other material constraints would otherwise be rediscovered.

`dist/` is generated output. Build role packages with:

```bash
python source/build_skills.py --output dist
```
