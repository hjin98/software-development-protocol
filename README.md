# Software Development Protocol

**Software Development Protocol** is a role-separated Agent Skills framework for disciplined, evidence-driven software engineering with AI agents and target execution environments.

Protocol v3 separates four kinds of authority:

- **`software-design`** — understands the repository/problem, diagnoses root causes, selects algorithms/architecture, freezes invariants and acceptance criteria, and produces/revises Implementation Workplans.
- **`software-implementation`** — consumes a frozen workplan, performs bounded stale-plan revalidation, implements the change, authors tests/benchmark harnesses, performs available light checks, stages candidate closeout, and produces a Qualification Handoff.
- **`software-qualification`** — consumes an exact source-bound Qualification Handoff and executes the required tests, benchmarks, production-data, hardware, recovery, packaging, and environment checks. Product source is read-only by default; the role returns evidence rather than redesigning.
- **`software-verification`** — independently reviews the final candidate, governing workplan, and qualification evidence; checks semantic/contract/resource/security/release conformance; and returns `MERGE_READY`, `NOT_READY`, or `DESIGN_REVISION_REQUIRED`.

The normal substantial-change flow is:

```text
software-design
  -> Implementation Workplan
software-implementation
  -> Qualification Handoff
software-qualification
  -> Qualification Report / evidence
software-verification
  -> MERGE_READY or corrective routing
```

These are authority roles, not product names. Chat, Codex, CI, a workstation/HPC session, a human, or another agent may occupy a role. Role boundaries remain useful even when one system performs multiple roles sequentially.

`source/` is the canonical protocol library. `dist/` contains generated self-contained Agent Skill ZIPs. Generated packages must never be hand-edited; change canonical source and rebuild/check distributions with `source/build_skills.py`.

Protocol compatibility and the v2-to-v3 transition are defined in `source/shared/references/protocol-versioning-and-compatibility.md`.
