# Software Development Protocol 4

This directory is the canonical Protocol 4 source.

## Governing doctrine

**Materiality decides what must be accomplished. Simplicity decides how it should be accomplished.**

Satisfy each material requirement with the least necessary mechanism. Every additional component, abstraction, state, interface, fallback, compatibility layer, dependency, workflow stage, and special case adds failure and maintenance surface. When a simple and a complex solution satisfy the same requirements, choose the simple solution.

Necessary complexity is allowed. Simplicity must never be used to omit correctness, scientific rigor, safety, recovery, security, compatibility, or performance requirements that are genuinely material.

When a mechanism repeatedly fails, first consider removing, consolidating, refactoring, or redesigning it. Do not stabilize a failing design by surrounding it with increasingly elaborate wrappers, adapters, supervisors, retries, state translators, recovery layers, or validation systems.

## Roles

Protocol 4 keeps two roles:

- `software-design` — root-cause diagnosis, simplest-sufficient design, material acceptance requirements, and independent review when useful;
- `software-implementation` — implementation, refactoring, testing, real-use validation, and delivery under the chosen design.

Testing, performance measurement, package checks, target-hardware runs, production-data runs, and recovery checks are implementation/validation activities. They do not require a separate qualification role or handoff unless the project itself genuinely needs such an artifact.

## Proportional workflow

Use the shortest workflow that answers the engineering question.

```text
small/local:         inspect -> implement -> relevant test -> done
substantial:         design -> implement -> affected tests -> review
external/production: design if needed -> implement -> run real program -> inspect result
```

A workplan is optional and should exist only when it prevents material design or sequencing from being rediscovered. Gates are optional and should exist only when crossing a boundary has a real engineering reason.

## Build

`source/` is canonical. `dist/` contains generated, ready-to-install role skill packages and is committed for convenient distribution. Whenever canonical source changes, rebuild it before committing:

```bash
python source/build_skills.py --output dist
```
