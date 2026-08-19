# Prompt-Compendium Traceability

This maintenance reference maps source examples 3-8 into the protocol and records deliberate revisions made for software-engineering robustness.

| Source example | Preserved requirement | Revision/generalization |
|---|---|---|
| 3 - architecture/gated implementation | evaluate architecture; staged implementation; test each gate; do not advance on failure; final real-scenario test | separate durable current architecture from temporary Implementation Workplans; add baseline/oracle gates, objective acceptance, blocked/not-run semantics, versioned handoffs, split qualification, independent verification, and production qualification |
| 4 - code constraints | multi-format input, inference plus explicit override, libraries to reduce complexity, factorization, robust inputs/edge cases, tests | generalize format inference to unambiguous evidence; normalize to canonical model; preserve compatibility; justify dependencies; structured errors and ownership boundaries |
| 5 - specification and implementation | define API/data contract; theory/motive; edge cases; implement against spec; focused tests; spec/code review | make spec-first conditional on public/persisted/cross-module contracts; add versioning, migration, one normative owner, candidate closeout, qualification identity, and generated-artifact closeout |
| 6 - optimization | remove repeated I/O, improve algorithms, replace slow dense Python hot loops, vectorize/use optimized libraries, progress/diagnostics, speed+memory evaluation | require profiling/baseline, correctness oracle, distinguish irregular algorithms, structured progress, repeated benchmarks, no fidelity reduction; elevate disk I/O, storage footprint, cache lifecycle, recovery cost, and authenticated baseline reuse |
| 7 - parallelization | parallelize independent work; auto-detect CPU/GPU; memory safeguards; ~90% CPU and 80% RAM | treat fractions as configurable upper budgets; detect affinity/cgroups/scheduler limits; control nested BLAS/native threads; GPU only when measured viable; VRAM headroom/backoff/fallback |
| 8 - documentation | cite algorithm sources; LaTeX math; concise readable docs; Markdown plus PDF | distinguish current architecture/specification, temporary workplans/handoffs, qualification/verification evidence, and history; make Markdown authoritative; require regenerated/verified PDF for permanent engineering docs while exempting temporary coordination artifacts |

## Added standard engineering requirements

The protocol additionally requires:

- preserve unrelated user/repository changes;
- compatibility/deprecation/schema migration discipline;
- generated-artifact source ownership;
- targeted-to-broad validation ladder;
- property/metamorphic tests where example tests are insufficient;
- build/install smoke tests for distributable changes;
- deterministic/reproducible evidence and explicit unverified environments;
- dependency and observability discipline;
- progressive context loading for large codebases;
- explicit residual-risk reporting;
- root-cause debugging through execution/data-lineage tracing rather than symptom-only patches;
- cache/checkpoint identity, invalidation, crash consistency, bounded retention, and restart/recovery qualification;
- disk I/O/storage admission and footprint management as resource domains alongside CPU/RAM/GPU/VRAM;
- explicit security/trust-boundary review for archives, unsafe deserialization, subprocesses, paths, networks, credentials, dependencies/plugins, model/checkpoint loading, and document rendering;
- mandatory specification-code parity plus separation of current architecture from temporary transition state;
- version/history synchronization for completed release-bearing changes and workplan closeout;
- Markdown-authoritative permanent documentation with content-addressed PDF provenance;
- source-bound target-environment qualification and independent acceptance verification.

## Collaboration-derived protocol evolution

Later revisions intentionally extend beyond source examples where repeated project failures exposed missing lifecycle concerns. These additions are protocol synthesis from development experience rather than claims that Examples 3-8 explicitly contained them:

- disk I/O/storage lifecycle, cache/checkpoint identity, write amplification, restart/recovery cost, and parallel-filesystem behavior;
- security/trust boundaries for serialization, archives, subprocesses, credentials, plugins, dependencies, network inputs, and document rendering;
- strict specification-code parity, current-architecture/workplan separation, version/history governance, and Markdown-authoritative PDF generation;
- content-addressed Markdown/PDF provenance rather than timestamp freshness;
- canonical resolved configuration and configuration-to-state identity;
- concurrency/orchestration correctness: failure propagation, bounded retry, cancellation/preemption, idempotency, backpressure, deterministic aggregation, and resource ownership;
- explicit persisted-schema READ/MIGRATE/REJECT compatibility;
- clean-build/distribution inspection/isolated-install qualification;
- longitudinal performance-regression tracking and structured run/evidence manifests;
- capability-aware qualification and explicit qualification barriers so expensive target execution can be batched without weakening mandatory acceptance;
- source-bound evidence invalidation and dependency-aware reuse of expensive baselines/checks;
- role-specific Agent Skills built from one canonical protocol source.

## Role-model lineage

Protocol v2 used two generated roles:

```text
software-design-review
software-implementation
```

with the Implementation Workplan as the principal handoff. That model successfully prevented repeated design rediscovery but still coupled source construction, target-environment qualification, and final acceptance too tightly.

Protocol v3 splits authority into:

```text
software-design
  -> Implementation Workplan
software-implementation
  -> Qualification Handoff
software-qualification
  -> Qualification Report
software-verification
  -> Verification Report
```

The v3 change is a major protocol revision because it changes role ownership, lifecycle state, and handoff compatibility. Completed v2 artifacts remain readable historical evidence; active substantial v2 work migrates according to `protocol-versioning-and-compatibility.md`.

These extensions should continue to evolve empirically: add a protocol domain when repeated real failures reveal a missing invariant or lifecycle concern, not merely to accumulate generic software-engineering advice.
