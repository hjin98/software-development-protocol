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
  - source/check_protocol_semantics.py
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
- The original v2-governed `SDP-V3` plan is preserved as bootstrap lineage for G0-G3 and marked `SUPERSEDED`; this v3 workplan governs hardening and freeze validation.

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
| H1 | PREPARED | NOT_REQUIRED | PENDING | no | Update canonical lifecycle/role doctrine |
| H2 | PREPARED | NOT_REQUIRED | PENDING | no | Harden handoff/report templates |
| H3 | PREPARED | NOT_REQUIRED | PENDING | no | Add protocol semantic regression checks |
| H4 | PREPARED | PASS | PENDING | yes | Rebuild/check generated v3 skills |
| H5 | PENDING | NOT_RUN | PENDING | yes | Synthetic lifecycle cases |
| H6 | PENDING | NOT_RUN | PENDING | yes | MVSEL2 real-workflow dogfood |
| H7 | PENDING | NOT_RUN | PENDING | yes | Independent freeze verification |

## H0 — Identity and immutability freeze

Prepared evidence:
- canonical protocol separates candidate commit provenance, candidate content identity, and later evidence/coordination commits;
- dirty tracked/untracked/source-origin preflight and postflight are mandatory;
- tracked candidate generated outputs are immutable during qualification.

## H1 — Canonical doctrine and role hardening

Prepared evidence:
- `protocol-versioning-and-compatibility.md` defines identity, generated output classes, dependency invalidation, retry identity, and v2 bootstrap migration;
- `workplans-and-agent-handoff.md` defines derived lifecycle, deferred semantics, evidence reuse, pre/postflight, role authority and independence metadata;
- implementation, qualification, verification role skills consume those hardened contracts;
- testing/qualification doctrine matches the same semantics.

## H2 — Artifact schema hardening

Prepared evidence:
- Implementation Workplan template requires candidate identity policy and dependency/comparability rules;
- Qualification Handoff requires candidate identity, dirty-tree preflight, output classes, dependencies, retry policy and postflight;
- Qualification Report records per-check command/cwd/timestamps/exit/attempts, pre/postflight, retry history and evidence reuse;
- Verification Report records candidate/evidence identity, reuse audit, blocking deferred state and independence metadata.

## H3 — Builder/protocol regression checks

Prepared evidence:
- `source/check_protocol_semantics.py` asserts four-role registry and critical v3 identity/immutability/authority/template fields;
- permanent CI runs the semantic checker before canonical/generated parity validation;
- existing builder continues deterministic role/resource/frontmatter/template validation.

## H4 — Generated distributions

Qualification evidence:
- one-shot branch workflow executed the semantic checker, rebuilt all four generated ZIPs, executed `source/build_skills.py --output dist --check`, then self-removed;
- remote `dist/` now contains only `BUILD_INDEX.json` plus hardened `software-design.zip`, `software-implementation.zip`, `software-qualification.zip`, and `software-verification.zip`;
- successful self-removal/commit is evidence that semantic and canonical/generated parity commands completed before publication.

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
- Regenerate/check all four distribution ZIPs after every canonical role/reference/template change.
- Do not mark COMPLETE until synthetic lifecycle cases, real dogfood and independent freeze verification pass.
