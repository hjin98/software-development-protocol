# Software Development Protocol 5.3

This directory is the canonical Protocol 5.3 source.

## Governing doctrine

> **Choose the globally best justified software solution that satisfies the material engineering requirements; among engineering-sufficient solutions, prefer the one with the lowest justified total product/system complexity.**

Material requirements define the feasible solution space: functionality/capability, correctness and scientific/domain fidelity, reliability/recovery/safety/security/compatibility, CPU/RAM/VRAM/storage/I/O/wall-time constraints, target scale, hardware effectiveness, and materially important end-to-end performance.

### Product simplicity, not process minimalism

Simplicity is a design objective for the engineered product/system. Minimize unnecessary components, states, interfaces, dependencies, synchronization, duplicated authorities, compatibility paths, runtime/operational stages, special cases, and maintenance surface once the material engineering envelope is satisfied. Necessary specialization is valid when it provides material engineering value.

Do not generalize this objective into a requirement to minimize engineering-process length. The development process is governed by sufficiency, confidence, risk reduction, and efficient use of human and compute resources. Use the analysis, staging, regression testing, integration testing, review, benchmarking, and validation needed to establish the required result. Eliminate redundant, ceremonial, duplicative, or low-information work, but do not omit materially useful work merely because a shorter workflow exists.

## Lifecycle roles

Protocol 5.3 preserves the two-role lifecycle:

- `software-design` — diagnosis, engineering-envelope definition, globally justified architecture/algorithm/resource decisions, product-complexity review, validation design, and independent review when useful;
- `software-implementation` — implementation/refactoring, mandatory affected-surface regression and integration testing for executable changes, benchmarking/validation of material claims, cleanup, and delivery.

Testing and production qualification remain engineering activities, not additional lifecycle roles.

## Functional acceptance

Executable changes require affected-surface regression testing and integration testing through the assembled affected product path. The affected surface includes directly changed/new code and existing consumers, callers, shared utilities, configuration/persistence/state/orchestration paths, interfaces, and transitive behavioral dependencies that could plausibly change because of the revision.

Use bounded fixtures and representative workloads where they preserve required coverage. Test-cost minimization must never become coverage minimization.

Intermediate regression checks are appropriate between material behavior-changing stages when they reduce defect propagation, debugging ambiguity, rework, or downstream risk. A final assembled regression and integration pass is required after material implementation/cleanup changes.

## Production qualification

Full production qualification is distinct from functional testing. It characterizes an already functionally accepted candidate with real, long, data-heavy, target-machine/target-hardware execution for production-scale performance, resource use, scaling, recovery, and similar environment-specific properties.

Do not run full production qualification by default during implementation. Run it only when explicitly requested, required by project/release policy, or necessary to establish a material scale/resource/performance/hardware claim. Bounded benchmarks, accelerator smoke/equivalence checks, and representative resource sanity checks remain normal implementation validation when relevant.

## Optional specialists

`software-documentation` and `repository-hygiene` remain optional supporting capabilities, not lifecycle roles or approval gates.

## Process proportionality

Use a workflow sufficient for the material risks and acceptance requirements. Workplans, gates, reviews, and repeated checks are justified when they reduce ambiguity, risk, rediscovery, debugging cost, or wasted downstream work. Avoid them when they add no material engineering value. The objective is an effective engineering process, not the fewest process steps.

## Build

`source/` is canonical. `dist/` contains generated ready-to-install skill packages and is committed for convenient distribution. Whenever canonical source changes:

```bash
python source/build_skills.py --output dist
python source/check_dist.py
```

Both commands must succeed before the protocol revision is complete.
