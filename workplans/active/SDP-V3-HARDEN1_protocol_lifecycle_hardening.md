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
  - source/check_protocol_lifecycle_cases.py
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

## Frozen hardening decisions

- Keep the four v3 authority roles unchanged.
- Distinguish `candidate_commit`, `candidate_content_identity`, and later evidence/coordination commits.
- Candidate content identity excludes only explicitly declared coordination/evidence paths; product source/tests/specs/package/generated product artifacts remain in identity.
- Qualification starts/ends with a clean candidate surface and may write only declared ephemeral outputs.
- `TRACKED_CANDIDATE_OUTPUT` cannot be changed during qualification.
- Evidence reuse requires declared dependency/comparability identity; ambiguity invalidates reuse.
- Retry modes are `NONE`, `IDENTICAL_RETRY`, `CLEAN_RETRY`, `RESUME_RETRY`; policy-changing retries require a new handoff/design decision.
- Workplan-level lifecycle states are derived from gate states where possible.
- `DEFERRED` explicitly records whether it blocks current acceptance and where it moves.
- Verification records independence metadata.
- Original v2-governed `SDP-V3` is preserved as bootstrap lineage and marked `SUPERSEDED`; this v3 workplan governs hardening/freeze validation.

## Gate summary

| Gate | Implementation | Qualification | Acceptance | Barrier | Purpose |
|---|---|---|---|---|---|
| H0 | PREPARED | NOT_REQUIRED | PENDING | no | Freeze identity/immutability model |
| H1 | PREPARED | NOT_REQUIRED | PENDING | no | Update canonical lifecycle/role doctrine |
| H2 | PREPARED | NOT_REQUIRED | PENDING | no | Harden handoff/report templates |
| H3 | PREPARED | NOT_REQUIRED | PENDING | no | Add protocol semantic/lifecycle regression checks |
| H4 | PREPARED | PASS | PENDING | yes | Rebuild/check generated v3 skills |
| H5 | PREPARED | PASS | PENDING | yes | Synthetic lifecycle cases |
| H6 | PENDING | NOT_RUN | PENDING | yes | MVSEL2 real-workflow dogfood |
| H7 | PENDING | NOT_RUN | PENDING | yes | Independent freeze verification |

## H0-H2 — Canonical identity/lifecycle/artifact hardening

Prepared evidence:
- canonical protocol separates candidate commit provenance, candidate content identity, and later evidence/coordination commits;
- qualification dirty tracked/untracked/source-origin preflight and postflight are mandatory;
- tracked candidate generated outputs are immutable during qualification;
- workplan/handoff/report templates carry candidate identity, output classes, evidence dependencies, retry policy, per-check execution provenance, deferred semantics and verifier independence;
- implementation/qualification/verification roles consume the same rules.

## H3 — Protocol regression checks

Prepared evidence:
- `source/check_protocol_semantics.py` asserts four-role registry and critical v3 authority/identity/immutability/template fields;
- `source/check_protocol_lifecycle_cases.py` models qualification preflight versus later evidence-only verification, output classes, dependency reuse, retry boundaries and derived lifecycle/deferred semantics;
- permanent CI runs both checkers before canonical/generated parity validation.

## H4 — Generated distributions

Qualification evidence:
- one-shot branch workflow executed semantic checks, rebuilt all four generated ZIPs, executed `source/build_skills.py --output dist --check`, then self-removed;
- remote `dist/` contains only `BUILD_INDEX.json` plus hardened `software-design.zip`, `software-implementation.zip`, `software-qualification.zip`, and `software-verification.zip`;
- successful self-removal/publication means the workflow reached the post-check commit step.

## H5 — Synthetic lifecycle qualification

Qualification evidence:
- one-shot validation workflow executed `source/check_protocol_semantics.py`, `source/check_protocol_lifecycle_cases.py`, and canonical/generated `--check` against the hardened branch, then self-removed on success;
- synthetic cases include dirty tracked state, undeclared untracked execution-affecting state, candidate content mismatch, evidence-only post-qualification commits, tracked versus ephemeral outputs, explicit/ambiguous evidence dependency reuse, identical/clean/resume retry rules, policy-changing retry rejection, and blocking/non-blocking deferred lifecycle semantics.

Residual limitation:
- these are protocol-rule regression tests, not proof that an arbitrary future agent will obey the prose. H6 real-workflow dogfood and H7 independent verification remain mandatory freeze barriers.

## H6 — Real MVSEL2 dogfood

Use the current mdstats MVSEL2 hardening workflow to exercise Chat-first implementation, narrow workstation/Codex qualification, evidence-only commit handling, dependency-aware reruns and independent verification using the hardened v3 artifacts.

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

- Preserve original v2 bootstrap lineage.
- Regenerate/check all four distribution ZIPs after canonical packaged source changes.
- Do not mark COMPLETE until real dogfood and independent freeze verification pass.
