# Software Development Protocol

**Software Development Protocol** is a role-separated Agent Skills framework for disciplined, evidence-driven software engineering with AI agents and target execution environments.

Protocol v3 separates four kinds of authority:

- **`software-design`** — diagnoses problems, selects algorithms/architecture, freezes invariants/acceptance criteria, and owns Implementation Workplans.
- **`software-implementation`** — consumes frozen design, implements code/tests/harnesses, stages the exact candidate, computes candidate identity, and produces a Qualification Handoff.
- **`software-qualification`** — executes source-bound tests/benchmarks/production/hardware/release checks against the exact candidate while keeping product source and tracked candidate outputs read-only.
- **`software-verification`** — independently reviews candidate content plus qualification evidence and returns `MERGE_READY`, `NOT_READY`, or `DESIGN_REVISION_REQUIRED`.

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

Protocol v3 deliberately distinguishes **Git commit provenance**, **qualified candidate content identity**, and later **evidence/coordination commits**. Qualification binds both `candidate_commit` and `candidate_content_identity`; repository-resident reports may be committed afterward without invalidating qualification only when they preserve the declared candidate content identity. Dirty tracked state, undeclared execution-affecting untracked files, or tracked generated product mutations are not valid source-bound qualification states.

These are authority roles, not product names. Chat, Codex, CI, a workstation/HPC session, a human, or another agent may occupy a role. Role boundaries remain useful even when one system performs multiple roles sequentially.

`source/` is the canonical protocol library. `dist/` contains generated self-contained Agent Skill ZIPs. Generated packages must never be hand-edited; change canonical source and rebuild/check distributions with `source/build_skills.py`.

Protocol compatibility, candidate/evidence identity, retry/invalidation rules, and the v2-to-v3 transition are defined in `source/shared/references/protocol-versioning-and-compatibility.md`.
