---
kind: implementation-workplan
workplan_id: SDP-V3
plan_revision: 1
status: SUPERSEDED
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

## Lifecycle note

This workplan was authored under Protocol v2.0.1 and successfully governed the initial v3 architectural refactor through G0-G3. It is now **SUPERSEDED for freeze/hardening execution** by `SDP-V3-HARDEN1`, which is itself governed by Protocol v3.0.0.

Preserve this artifact as bootstrap lineage. Do not reinterpret its pending G4-G6 as v3 qualification authority; those concerns move to the successor workplan.

## Objective

Refactor Software Development Protocol v2.0.1 from a two-role design/review + implementation/qualification model into four explicit authority roles—design, implementation, qualification, and verification—so reasoning/source construction can be separated from expensive target-environment execution without weakening acceptance evidence.

## Current diagnosis

The v2 protocol successfully prevents implementation agents from repeating broad design work, but its implementation role still owns source construction, testing, benchmarking, qualification, and normative closeout. In workflows where target-environment execution is expensive, this couples high-cost execution with work that can be prepared elsewhere and obscures the distinction among implementation completion, executed qualification, and independent acceptance.

## Frozen design decisions

- Protocol major version becomes `3.0.0`.
- Generated roles become `software-design`, `software-implementation`, `software-qualification`, and `software-verification`.
- Roles are authority categories, not specific agent/product names.
- Formal lifecycle: `Implementation Workplan -> Qualification Handoff -> Qualification Report -> Verification Report`.
- Qualification and verification keep product source read-only by default.
- Gate state separates implementation, qualification, and acceptance.
- Capability classes are `SOURCE`, `LOCAL_LIGHT`, `TARGET_RUNTIME`, `PRODUCTION_DATA`, `TARGET_HARDWARE`, `EXTERNAL_ACTION`.
- `qualification_barrier` controls whether later implementation can be prepared before pending expensive qualification.
- Candidate spec/architecture/version/release closeout may be staged before qualification so the exact merge candidate is exercised; branch-local candidate docs do not become accepted authority before verification/merge.
- Completed v2 artifacts remain readable historical evidence; active substantial v2 work migrates according to explicit `READ | MIGRATE | REJECT` rules.
- Expensive baseline/evidence reuse is permitted only under explicit identity/comparability compatibility.
- Generated skill packages remain derived from canonical `source/`; committed `dist/` must pass deterministic rebuild drift checks.

## Completed gates

| Gate | Status | Purpose |
|---|---|---|
| G0 | PASS | Review/freeze four-role architecture against v2 protocol |
| G1 | PASS | Canonical role/lifecycle/artifact refactor |
| G2 | PASS | Builder, deterministic distribution, and CI drift enforcement |
| G3 | PASS | Protocol-source/generated-package static verification |
| G4 | SUPERSEDED | Synthetic lifecycle qualification moved to `SDP-V3-HARDEN1` |
| G5 | SUPERSEDED | Representative real-workflow dogfood moved to `SDP-V3-HARDEN1` |
| G6 | SUPERSEDED | Independent freeze verification moved to `SDP-V3-HARDEN1` |

## G0-G3 evidence summary

- Canonical four-role source established in commit `7ce6a9da429d0062b919f9ae1c88f042218ac5af`.
- Builder expanded to four roles with role/frontmatter/resource/template validation and deterministic `--check`.
- Remote `dist/` rebuilt with exactly four v3 role ZIPs plus `BUILD_INDEX.json`.
- Permanent CI parity check added.

## Successor

Continue only under:

`workplans/active/SDP-V3-HARDEN1_protocol_lifecycle_hardening.md`
