# Software Development Protocol

Software Development Protocol 5 is an engineering-fitness-first workflow for AI-assisted software engineering.

## Governing doctrine

> **Choose the globally best justified software solution that satisfies the material engineering requirements; among engineering-sufficient solutions, prefer the one with the lowest justified total product/system complexity.**

Material requirements can include functionality and capability, correctness and scientific/domain fidelity, reliability, recovery, safety, security, required compatibility, CPU/RAM/VRAM/storage/I/O/wall-time constraints, target-scale behavior, effective hardware use, and materially important end-to-end performance.

Simplicity applies primarily to the **engineering target: the software/system being produced**. Minimize unnecessary product mechanisms, duplicated authorities, states, abstractions, interfaces, dependencies, synchronization points, compatibility paths, runtime/operational stages, special cases, and maintenance surface after the required engineering envelope is satisfied. Necessary specialization remains valid when it buys a material capability or prevents a material failure.

Do **not** turn product simplicity into a requirement to minimize the number of engineering steps. The development process is governed by sufficiency, confidence, risk reduction, and efficient use of engineering time and compute resources. Use the design, implementation staging, regression testing, integration testing, review, benchmarking, and validation needed to establish the required result. Remove redundant, ceremonial, duplicative, or low-information work, but do not omit materially useful work merely to make the workflow shorter.

Protocol 5.3 keeps the same two-role lifecycle:

```text
software-design -> software-implementation
```

- `software-design` diagnoses root causes, defines the material engineering envelope, chooses the globally justified product design, controls product complexity, defines validation obligations, and performs independent review when useful.
- `software-implementation` implements/refactors the product, performs mandatory stage-local and final affected-surface regression plus integration testing for executable changes, benchmarks and validates material claims, cleans up superseded product machinery, and delivers the result.

Optional specialists remain supporting capabilities, not approval gates:

- `software-documentation` — reconcile and improve durable documentation;
- `repository-hygiene` — conservative post-stage repository cleanup.

## Functional acceptance versus production qualification

For executable product changes, functional acceptance requires:

1. focused checks for new/modified mechanisms as appropriate;
2. affected regression after each material behavior-changing implementation stage before dependent work proceeds;
3. re-deriving the affected behavioral surface from the final assembled implementation;
4. final regression coverage across that complete surface, including affected existing and new code;
5. integration testing through the assembled affected product path and real consumer/interface boundaries;
6. repository/project-required checks, using the broader/full available suite when impact cannot be bounded confidently.

Use bounded fixtures/workloads where they preserve required behavioral coverage. Optimize test cost without narrowing required coverage. A tiny atomic change can share its stage and final pass; a genuinely non-executable intermediate may carry validation to the nearest executable stage when that dependency is explicit.

Full production qualification is distinct. It uses real, long, data-heavy, target-machine/target-hardware runs to characterize an already functionally accepted candidate for production-scale wall time, throughput, RAM/VRAM/storage/I/O, accelerator utilization, recovery cost, and similar environment-specific properties. It is not a substitute for regression/integration testing and is not run by default during implementation unless explicitly requested, required by project/release policy, or necessary to establish a material scale/resource/performance claim.

There is no separate qualification or verification lifecycle. These are engineering activities within the two-role lifecycle.

## Process proportionality

Use a workflow sufficient for the material engineering risks and acceptance requirements. Small work may be short; substantial work may need staged implementation, repeated regression checks, integration tests, and review. Required stage-local regression is part of functional acceptance, not optional process ceremony.

Workplans and gates are instrumental, not ceremonial. Use them when they reduce ambiguity, rediscovery, sequencing risk, or wasted downstream work. Do not add them merely because a template can represent them, and do not remove useful ones merely to reduce process length.

`source/` is canonical. `dist/` contains generated ready-to-install skill packages and is committed for distribution. Whenever canonical source changes, build once from canonical source, validate the generated packages as shipped artifacts, run protocol regression tests, and verify semantic parity with committed `dist/` before completion.
