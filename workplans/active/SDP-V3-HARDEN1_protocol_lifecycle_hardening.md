---
kind: implementation-workplan
workplan_id: SDP-V3-HARDEN1
plan_revision: 1
status: IN_PROGRESS
protocol_version: 3.0.0
analysis_base_ref: agent/protocol-v3-role-split
analysis_base_commit: 7ce6a9da429d0062b919f9ae1c88f042218ac5af
assumption_paths:
  - source/roles/
  - source/shared/references/
  - source/shared/templates/
  - source/build_skills.py
  - dist/
  - workplans/active/SDP-V3_four_role_protocol_refactor.md
architecture_refs:
  - README.md
  - source/README.md
spec_refs:
  - source/shared/references/workplans-and-agent-handoff.md
  - source/shared/references/testing-and-qualification.md
  - source/shared/references/protocol-versioning-and-compatibility.md
expected_change_paths:
  - source/
  - dist/
  - .github/workflows/
  - workplans/
default_gate_approval: AUTO
---

# SDP-V3-HARDEN1 — Protocol lifecycle and evidence hardening

## Objective

Harden Protocol v3 before freeze so qualification evidence remains valid and auditable across evidence-only commits, dirty working trees, generated outputs, retries, evidence reuse, lifecycle transitions, and the v2-to-v3 bootstrap.

## Current diagnosis

The four-role split is accepted, but the first v3 review found that `source_commit` alone cannot distinguish immutable qualified candidate content from later repository-resident evidence/coordination commits. Qualification also needs stronger working-tree immutability, generated-output classes, dependency-bound evidence reuse, retry semantics, lifecycle derivation, and bootstrap handling.

## Frozen design decisions

- Keep the four v3 authority roles unchanged.
- Distinguish `candidate_commit`, `candidate_content_identity`, and later evidence/coordination commits.
- Qualification binds both commit provenance and candidate content identity.
- Candidate content identity excludes only explicitly declared coordination/evidence paths; product source/tests/specs/package/generated product artifacts remain in identity.
- Qualification must start and end with a clean declared candidate surface and may write only declared evidence/build/temp outputs.
- `TRACKED_CANDIDATE_OUTPUT` cannot be created/changed during qualification; if target runtime is needed to generate it, return the artifact to implementation, commit a new candidate, and requalify affected checks.
- Evidence reuse is allowed only under declared dependency/comparability identity; ambiguity invalidates reuse.
- Retry semantics are explicit: `NONE`, `IDENTICAL_RETRY`, `CLEAN_RETRY`, `RESUME_RETRY`; policy-changing retries require a new handoff or design revision.
- Workplan-level lifecycle states are derived from gate states where possible.
- `DEFERRED` records whether it blocks current acceptance and where it moves.
- Verification records independence metadata.
- The original v2-governed `SDP-V3` plan remains historical lineage for G0-G3; this v3 workplan governs hardening and freeze validation.

## Invariants and acceptance semantics

- No evidence-only/coordination commit may silently invalidate an otherwise identical qualified candidate content identity.
- Any product-relevant content change changes candidate identity and invalidates affected evidence.
- `HEAD == candidate_commit` is insufficient without dirty-tree/import-origin checks.
- Qualification never mutates tracked candidate product outputs.
- Undeclared untracked files that can affect execution are disallowed.
- Evidence reuse defaults to rerun when dependencies are uncertain.
- A mandatory blocking deferred check can never yield `MERGE_READY`.
- Only verification owns final acceptance.

## Gate summary

| Gate | Implementation | Qualification | Acceptance | Barrier | Purpose |
|---|---|---|---|---|---|
| H0 | PREPARED | NOT_REQUIRED | PENDING | no | Freeze identity/immutability model |
| H1 | IN_PROGRESS | NOT_REQUIRED | PENDING | no | Update canonical lifecycle/role doctrine |
| H2 | PENDING | NOT_REQUIRED | PENDING | no | Harden handoff/report templates |
| H3 | PENDING | NOT_REQUIRED | PENDING | no | Harden builder/protocol regression checks |
| H4 | PENDING | NOT_RUN | PENDING | yes | Rebuild/check generated v3 skills |
| H5 | PENDING | NOT_RUN | PENDING | yes | Synthetic lifecycle cases |
| H6 | PENDING | NOT_RUN | PENDING | yes | MVSEL2 real-workflow dogfood |
| H7 | PENDING | NOT_RUN | PENDING | yes | Independent freeze verification |

## H0 — Identity and immutability freeze

Acceptance:
- candidate commit/content/evidence identities are unambiguous;
- evidence-only commits can be represented without claiming a new product candidate;
- dirty tracked/untracked execution surfaces are rejected;
- tracked candidate generated outputs cannot be mutated in qualification.

## H1 — Canonical doctrine and role hardening

Work:
- update protocol versioning/compatibility, workplan/handoff, testing/qualification, documentation/evidence, release and role skills;
- define evidence dependency/retry/deferred/independence semantics;
- define source preflight/postflight requirements.

## H2 — Artifact schema hardening

Work:
- update Implementation Workplan, Qualification Handoff, Qualification Report, Verification Report templates;
- require candidate content identity, evidence exclusions, dirty-tree checks, dependencies, retries, per-check execution provenance, deferred blocking semantics, and verification independence metadata.

## H3 — Builder/protocol regression checks

Work:
- extend canonical builder validation for critical v3 fields and authority invariants;
- retain deterministic source/dist parity checks.

## H4 — Generated distributions

Acceptance:
- canonical builder succeeds;
- `--check` succeeds against committed `dist/`;
- four generated ZIPs contain hardened v3 doctrine/templates and no stale v2 runtime role.

## H5 — Synthetic lifecycle qualification

Exercise at minimum:
- evidence-only commit after qualification;
- dirty tracked tree at expected HEAD;
- undeclared untracked execution source;
- tracked generated product artifact mutation;
- allowed ephemeral qualification output;
- explicit evidence dependency reuse;
- ambiguous dependency invalidation;
- identical/clean/resume retry boundaries;
- forbidden policy-changing retry;
- blocking/non-blocking deferred checks;
- invalid derived lifecycle state;
- fresh/shared verification independence metadata.

## H6 — Real MVSEL2 dogfood

Use the current mdstats MVSEL2 hardening workflow to exercise Chat-first implementation, narrow workstation/Codex qualification, and independent verification using the hardened v3 artifacts.

## H7 — Final freeze verification

Return `MERGE_READY` only when H0-H6 evidence plus canonical/generated parity support the hardened v3 contract.

## Design-revision triggers

Stop if hardening would require:
- adding/removing one of the four authority roles;
- allowing qualification to mutate product source as normal behavior;
- weakening source-bound evidence or mandatory PASS semantics;
- making evidence reuse implicit rather than dependency-bound;
- making workplan/evidence commits indistinguishable from qualified product content.

## Closeout

- Preserve the original `SDP-V3` v2 workplan as bootstrap lineage rather than rewriting it to v3.
- Record v3 hardening/freeze under this workplan or a direct successor.
- Regenerate/check all four distribution ZIPs.
- Do not mark COMPLETE until real dogfood and independent freeze verification pass.
