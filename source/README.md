# Software Development Protocol 5

This directory is the canonical Protocol 5 source.

## Governing doctrine

> **Seek the best globally justified engineering solution.**

Material engineering requirements define the feasible solution space. These can include:

- required functionality and capability;
- correctness and scientific/domain fidelity;
- reliability, recovery, safety, security, and required compatibility;
- CPU, RAM, VRAM, storage, I/O, wall-time, scheduler, and other resource constraints;
- appropriate asymptotic scaling for the target workload;
- effective use of the target hardware;
- materially important end-to-end performance.

These requirements are not a rigid numeric ranking; they form the engineering envelope that an acceptable solution must satisfy. Use the best materially justified algorithmic scaling and implementation for the target workload and hardware. Do not pursue theoretical optimality when further complexity has no material benefit.

## Simplicity and clean architecture

Among engineering-sufficient solutions, prefer the one with the lowest justified **total system complexity**: fewer unnecessary mechanisms, duplicated authorities, states, abstractions, interfaces, dependencies, synchronization points, compatibility paths, workflow stages, and special cases.

Do not sacrifice capability, correctness, scientific fidelity, scalability, resource feasibility, hardware effectiveness, robustness, or materially required performance merely to make code or architecture look simpler.

Necessary specialization is valid. Separate CPU/GPU kernels, a trusted slow oracle plus an optimized implementation, migration code, or other duplication may remain when it provides a distinct material capability. Reuse and consolidation should follow shared semantic responsibility, invariant, ownership, and reason to change—not textual similarity alone.

## Complexity regression and consolidation

Simplicity is also a corrective feedback mechanism. For substantial work, repeated modifications in one subsystem, or independent review, inspect the affected area for accumulated complexity:

- duplicated functionality or state;
- multiple authorities for one concept;
- wrappers, adapters, fallbacks, compatibility layers, or special cases that have outlived their purpose;
- parallel implementations that can safely share one semantic owner;
- superseded machinery that can be deleted;
- opportunities to reuse, consolidate, or refactor without degrading engineering fitness.

Scope this review proportionally. A small local fix does not require a repository-wide cleanup. Refactor before extension when the current structure prevents a clean, correct, efficient change or when another patch would materially increase structural debt.

## Roles

Protocol 5 keeps two roles:

- `software-design` — root-cause diagnosis, engineering-envelope definition, architecture/algorithm/resource decisions, complexity-regression review, and independent review when useful;
- `software-implementation` — implementation, refactoring, testing, benchmarking, target-environment validation, cleanup, and delivery under the chosen design.

Testing, performance measurement, package checks, target-hardware runs, production-data runs, and recovery checks are implementation/validation activities. They do not require a separate qualification role or handoff unless the project itself genuinely needs such an artifact.

## Proportional workflow

Use the shortest workflow that answers the engineering question.

```text
small/local:         inspect -> implement -> relevant test -> done
substantial:         design -> implement/refactor -> affected tests -> review
external/production: design if needed -> implement -> run real program -> inspect result
```

A workplan is optional and should exist only when it prevents material design or sequencing from being rediscovered. Gates are optional and should exist only when crossing a boundary has a real engineering reason.

## Build

`source/` is canonical. `dist/` contains generated, ready-to-install role-skill packages and is committed for convenient distribution. Whenever canonical source changes, rebuild it before committing:

```bash
python source/build_skills.py --output dist
```
