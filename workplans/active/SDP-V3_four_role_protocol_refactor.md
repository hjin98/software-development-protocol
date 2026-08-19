---
kind: implementation-workplan
workplan_id: SDP-V3
plan_revision: 1
status: IN_PROGRESS
protocol_version: 2.0.1
analysis_base_ref: main
analysis_base_commit: 3a6bb9bfdb66d8822ddeca3b66a199bd3abe5a7e
assumption_paths:
  - source/roles/
  - source/shared/references/
  - source/shared/templates/
  - source/build_skills.py
  - dist/
architecture_refs:
  - README.md
  - source/README.md
spec_refs:
  - source/shared/references/workplans-and-agent-handoff.md
  - source/shared/references/testing-and-qualification.md
expected_change_paths:
  - source/
  - dist/
  - .github/workflows/
  - workplans/
default_gate_approval: AUTO
---

# SDP-V3 — Four-role Protocol Refactor

## Objective

Refactor Software Development Protocol v2.0.1 from a two-role design/review + implementation/qualification model into four explicit authority roles—design, implementation, qualification, and verification—so reasoning/source construction can be separated from expensive target-environment execution without weakening acceptance evidence.

## Current diagnosis

The v2 protocol successfully prevents implementation agents from repeating broad design work, but its implementation role still owns source construction, testing, benchmarking, qualification, and normative closeout. In workflows where target-environment execution is expensive, this couples high-cost execution with work that can be prepared elsewhere and obscures the distinction among implementation completion, executed qualification, and independent acceptance.

## Frozen design decisions

- Protocol major version becomes `3.0.0`.
- Generated roles become:
  - `software-design`
  - `software-implementation`
  - `software-qualification`
  - `software-verification`
- Roles are authority categories, not specific agent/product names.
- Formal lifecycle:
  `Implementation Workplan -> Qualification Handoff -> Qualification Report -> Verification Report`.
- Qualification and verification keep product source read-only by default.
- Gate state separates implementation, qualification, and acceptance.
- Capability classes are `SOURCE`, `LOCAL_LIGHT`, `TARGET_RUNTIME`, `PRODUCTION_DATA`, `TARGET_HARDWARE`, `EXTERNAL_ACTION`.
- `qualification_barrier` controls whether later implementation can be prepared before pending expensive qualification.
- Candidate spec/architecture/version/release closeout may be staged before qualification so the exact merge candidate is exercised; branch-local candidate docs do not become accepted authority before verification/merge.
- Completed v2 artifacts remain readable historical evidence; active substantial v2 work migrates according to explicit `READ | MIGRATE | REJECT` rules.
- Expensive baseline/evidence reuse is permitted only under explicit identity/comparability compatibility.
- Generated skill packages remain derived from canonical `source/`; committed `dist/` must pass deterministic rebuild drift checks.

## Invariants

- No role may infer PASS for a mandatory check that did not execute.
- Qualification evidence is source-bound.
- Product-source mutations after qualification invalidate evidence for the new source unless affected checks are rerun.
- Qualification does not become a second open-ended implementation/design pass.
- Verification does not repair substantial product source while reviewing.
- Frozen design contradictions route to design rather than being silently improvised.
- Trivial low-risk work retains a compressed path; the four-artifact lifecycle is not mandatory ceremony for every edit.
- Existing cross-cutting scientific, numerical, persistence, storage, concurrency, security, Git, documentation, and release doctrine remains authoritative unless explicitly revised for role ownership.

## Gate summary

| Gate | Status | Purpose |
|---|---|---|
| G0 | PASS | Review/freeze four-role architecture against v2 protocol |
| G1 | PASS | Canonical role/lifecycle/artifact refactor |
| G2 | PASS | Builder, deterministic distribution, and CI drift enforcement |
| G3 | PASS | Protocol-source/generated-package static verification |
| G4 | PENDING | Synthetic lifecycle edge-case qualification |
| G5 | PENDING | Representative real-workflow v3 dogfood |
| G6 | PENDING | Independent final protocol verification/freeze decision |

## G0 — Design freeze

**Acceptance:**

- role responsibilities are non-overlapping enough to route work;
- v2 compatibility and major-version rationale are explicit;
- handoff/evidence identities and source mutability are resolved;
- gate batching cannot bypass mandatory qualification;
- no fifth generic testing/debugging/security role is required.

**Evidence:** design/review discussion preceding this workplan.

## G1 — Canonical protocol refactor

**Work:**

- add four role SKILL.md files;
- revise workplan/handoff lifecycle and authority matrix;
- add protocol-versioning/compatibility reference;
- revise testing/evidence/release/spec/performance doctrine for split roles;
- add Implementation Workplan, Qualification Handoff, Qualification Report, and Verification Report templates;
- add v3 freeze/dogfood checklist and update traceability.

**Acceptance:**

- no stale current two-role ownership remains outside explicit v2 lineage;
- role skills reference only shared resources they actually package;
- templates do not hard-code a semantic protocol version.

**Evidence:**

- canonical source commit: `7ce6a9da429d0062b919f9ae1c88f042218ac5af`;
- current `source/roles/` contains exactly the four v3 role directories;
- current v2 role names remain only in explicit compatibility/traceability lineage;
- builder role/resource/frontmatter/template validation passes on the canonical working copy.

## G2 — Builder and generated distribution

**Work:**

- expand builder to four roles;
- add role/frontmatter/resource/template validation;
- add deterministic `--check`;
- rebuild all four ZIPs and BUILD_INDEX;
- remove legacy v2 role ZIP from v3 distribution;
- add CI build-drift check.

**Acceptance:**

- two consecutive builds have identical ZIP SHA-256;
- `python source/build_skills.py --output dist --check` passes;
- BUILD_INDEX lists exactly four v3 roles.

**Evidence:**

- two consecutive local canonical builds produced identical ZIP SHA-256 values;
- local canonical `python source/build_skills.py --output dist --check` => PASS for protocol `3.0.0`;
- branch one-shot Actions build regenerated `dist/` from canonical source and removed itself;
- remote `dist/` contains exactly `software-design.zip`, `software-implementation.zip`, `software-qualification.zip`, `software-verification.zip`, plus `BUILD_INDEX.json`;
- legacy `software-design-review.zip` is absent;
- permanent `.github/workflows/protocol-check.yml` runs the canonical `--check` on PRs and `main`.

## G3 — Static verification

**Acceptance:**

- canonical/generated source manifests match;
- role package contents are minimal/relevant;
- no missing role-referenced resource;
- legacy two-role wording appears only in compatibility/history;
- v3 templates contain required identity/source fields.

**Evidence:**

- builder validates the role registry against `source/roles/`, SKILL frontmatter names, referenced packaged resources, and template protocol-version placeholders before generating packages;
- generated BUILD_INDEX reports protocol `3.0.0` and exactly the four v3 skills;
- remote canonical evidence/documentation reference includes Workplan, Qualification Handoff, Qualification Report, and Verification Report as distinct artifact classes;
- one-shot maintenance patch and temporary rebuild workflow are absent from the resulting branch;
- no G4/G5 lifecycle result is inferred from these static/build checks.

## G4 — Synthetic lifecycle qualification

Exercise happy path, stale handoff SHA, FAIL return-to-implementation, BLOCKED target capability, both qualification-barrier modes, source mutation after qualification, mismatched evidence identity, design contradiction, and trivial compressed path.

## G5 — Representative dogfood

Use one real nontrivial workflow with expensive target execution—preferably the current mdstats MVSEL2 hardening flow—to prove Chat-first implementation preparation, narrow workstation/Codex qualification, and independent verification.

## G6 — Final verification/freeze

Do not declare v3 frozen until G4/G5 evidence is complete. Verification should return `MERGE_READY` only when canonical source, generated packages, role boundaries, compatibility rules, and dogfood evidence agree.

## Design-revision triggers

Stop for design revision if:

- qualification cannot remain source-bound/read-only without losing required functionality;
- candidate-before-qualification closeout creates an authority contradiction that cannot be expressed as branch-local candidate state;
- capability/barrier semantics permit mandatory checks to be bypassed;
- v2 compatibility cannot preserve completed historical evidence cleanly;
- four roles still have material overlapping final authority.

## Closeout

After G6:

- update workplan status to COMPLETE and archive if useful;
- ensure README/source README and dist describe only v3 current protocol;
- retain v2 lineage in compatibility/traceability rather than current role docs;
- record final source SHA and generated ZIP digests.
