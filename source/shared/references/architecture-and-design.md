# Architecture and Design

## Purpose

Architecture documentation describes the **accepted current structure of the software**. It is not a task tracker, implementation roadmap, gate log, or release history.

For a nontrivial change, architectural reasoning may be prospective during design, but proposed architecture belongs in the active Implementation Workplan until the implementation is accepted. Only then is the normative architecture manual updated to describe the resulting current architecture.

## Architecture review

For a nontrivial feature, algorithm, persistence model, concurrency design, or structural refactor, reason at the level needed to choose a coherent design and hand it off without guesswork.

Define as applicable:

1. **Problem and motive** - user/scientific/operational need and why the current design is insufficient.
2. **Scope and non-goals** - what the proposed revision will and will not solve.
3. **Conventions** - coordinate/sign/unit/indexing/ordering/precision/serialization conventions that affect correctness.
4. **Invariants** - properties that must remain true across implementations and backends.
5. **Data flow and ownership** - authoritative state, transformations, cache/checkpoint ownership, storage class, lifecycle/retention, invalidation, recovery path, and consumer boundaries.
6. **Algorithm** - equations/pseudocode/complexity where useful; identify exact versus approximate steps.
7. **Alternatives** - materially plausible alternatives for high-impact choices; explain rejection based on constraints rather than taste.
8. **Failure/fallback behavior** - unsupported inputs, numerical degeneracy, partial availability, backend failure, and safe fallback.
9. **Observability/provenance** - diagnostics needed to explain choices or reproduce results without coupling computation to presentation.
10. **Configuration/policy** - canonical defaults/overrides/automatic decisions, resolved-run provenance, and persisted-state identity where behavior depends on configuration.
11. **Concurrency/orchestration** - task ownership/state, failure propagation, bounded retry, cancellation/preemption, idempotency, backpressure, and deterministic aggregation where relevant.
12. **Security/trust boundaries** - untrusted/external inputs, execution/deserialization/plugin/rendering/network/file-write capabilities, least-privilege assumptions, and mitigations.
13. **Release/distribution** - installed-artifact behavior, package resources/versioning, and clean-build/clean-install implications when the design changes a distributable surface.
14. **Risks and deferred design questions** - explicit mitigations and boundaries for later revisions.

Reject an approach when it violates a hard invariant, requires unbounded resources, couples layers incorrectly, makes correctness unverifiable, creates unacceptable trust/recovery risk, or offers no measured benefit over a simpler design.

## Design convergence

Revise a proposed design when evaluation exposes a material gap. Stop revising once:

- major invariants are covered;
- ownership and interfaces are coherent;
- expected acceptance evidence is objective and executable;
- risks have mitigations/fallbacks;
- non-goals and deferred decisions are explicit;
- no materially better alternative remains unsupported by evidence.

Do not continue "hardening" through cosmetic revisions that add no new protection.

## Current architecture versus proposed architecture

Keep these states separate:

```text
accepted current architecture -> architecture manual
proposed architectural transition -> implementation workplan
accepted implemented transition -> update architecture manual
chronology of the transition -> history/changelog/release notes
```

Before implementation, a workplan may quote or summarize the proposed target architecture and link to the current architecture manual. Do not rewrite the normative architecture manual to make unimplemented behavior look current.

If implementation discovers that the proposed design cannot satisfy its frozen invariants, mark the workplan gate blocked and request a design revision rather than silently changing architectural semantics.

## Architecture document quality

A permanent architecture manual should contain only durable current-state information such as:

- theory/domain context needed to understand the structure;
- architectural scope and non-goals;
- ownership and dependency direction;
- accepted components and interfaces;
- authoritative data/control flow;
- invariants and compatibility boundaries;
- persistence/recovery/storage model where architectural;
- concurrency/security/resource boundaries where architectural;
- accepted algorithms and the rationale for materially important choices;
- supported extension points and intentionally unsupported regimes;
- references to normative specifications and durable evidence where useful.

Do **not** use architecture manuals for:

- task-local gate tables;
- `PLANNED`/`IN_PROGRESS` implementation status;
- "next gate" or "next optimization" statements;
- chronological version-by-version implementation logs;
- temporary benchmark plans;
- unresolved implementation checklists.

Those belong in Implementation Workplans, benchmarks/audits, and history/release records.

Author permanent architecture manuals in Markdown and keep their generated PDF/provenance artifacts synchronized according to `documentation-and-evidence.md`.
