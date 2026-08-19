---
kind: implementation-workplan
workplan_id: SDP-V3-SIMPLIFY1
plan_revision: 1
status: READY_FOR_IMPLEMENTATION
protocol_version: 3.0.0
analysis_base_ref: agent/protocol-v3-role-split
analysis_base_commit: 4eda8b9efe2ad5e3fdc5290079b7699800769832
assumption_paths:
  - source/roles/
  - source/shared/references/
  - source/shared/templates/
  - source/check_protocol_semantics.py
  - source/check_protocol_lifecycle_cases.py
  - source/build_skills.py
  - dist/
  - workplans/active/SDP-V3-HARDEN1_protocol_lifecycle_hardening.md
architecture_refs:
  - README.md
  - source/README.md
spec_refs:
  - source/shared/references/workplans-and-agent-handoff.md
  - source/shared/references/testing-and-qualification.md
  - source/shared/references/protocol-versioning-and-compatibility.md
expected_change_paths:
  - README.md
  - source/
  - dist/
  - workplans/
default_gate_approval: AUTO
---

# SDP-V3-SIMPLIFY1 — Materiality-first Protocol v3 simplification

## Objective

Keep Protocol v3's useful four-role separation while removing protocol machinery that can block or repeat software qualification without changing the validity of the software result.

## Current diagnosis

The four-role v3 architecture is useful: design, implementation, target-environment qualification, and final verification have distinct responsibilities. The MVSEL2 dogfood exposed a different failure: the hardening layer promoted candidate-content fingerprints, artifact SHA chains, dependency manifests, retry taxonomies, output-class bookkeeping, lifecycle metadata, and universal document provenance into blocking protocol semantics. Multiple qualification cycles then failed on coordination/harness details without demonstrating product defects.

The protocol therefore needs a materiality rule: protocol controls may block acceptance only when violating them could materially change the code executed, material inputs/configuration/environment, observable correctness, scientific or numerical interpretation, security/recovery behavior, performance/resource claim, installability/shipped artifact, or whether a candidate introduced a regression.

## Frozen design decisions

1. Keep the four authority roles: `software-design`, `software-implementation`, `software-qualification`, and `software-verification`.
2. Roles are authority boundaries; separate lifecycle artifacts are created only when they materially help a handoff. A separate Qualification Handoff is normally required only for a real execution boundary such as workstation/HPC/production/external execution.
3. Every substantial workplan has one authoritative **Acceptance-critical requirements** section. Qualification and verification may find real defects but may not manufacture new administrative acceptance requirements downstream.
4. Acceptance-critical criteria must be expressed in product/domain or material-execution language. Administrative provenance completeness is advisory.
5. Default candidate identity for a Git repository is the candidate Git commit plus absence of unintended product-defining working-tree changes. A separate `candidate_content_identity` is optional and used only at a real content boundary where Git does not sufficiently identify the thing being accepted.
6. Hashes/fingerprints remain useful at real content boundaries such as external datasets, model weights, built artifacts, mutable production inputs, or canonical-source/generated-artifact parity. They are not universal lifecycle paperwork.
7. Workplan/handoff/report digests, repeated protocol/version fields, evidence-file digests, timestamps, report filenames, and similar metadata are advisory unless the current task makes them materially necessary to interpret an acceptance claim.
8. Qualification Handoffs, when used, freeze intent and material conditions, not shell-script spelling. Equivalent cwd/path/activation/logging/scratch choices are operationally flexible.
9. Qualification may repair harmless harness or record defects locally and continue when candidate behavior, material inputs/configuration/environment, and acceptance semantics remain unchanged. Record the actual executed command/conditions.
10. Workplan revision increments only for material changes to target design, semantics, acceptance criteria, important scope, or material qualification conditions. Administrative/harness corrections do not require a new workplan revision.
11. Evidence reuse and rerun use one rule: rerun a check when something changed that could plausibly alter that check's result or interpretation. Structured dependency manifests are optional optimization for unusually expensive programs, not default protocol requirements.
12. Formal retry-mode taxonomy is removed from the core protocol. A rerun remains the same qualification while the candidate and material test conditions remain unchanged; important attempt changes are recorded.
13. Simplify ordinary gate state to `PENDING | PREPARED | PASS | FAIL | BLOCKED`. Final verification returns `MERGE_READY | NOT_READY | DESIGN_REVISION_REQUIRED`. Future-release obligations are listed separately rather than represented as blocking/nonblocking `DEFERRED` state machinery.
14. Capability labels are optional execution descriptors, not state-machine inputs.
15. A broad full-suite zero-failure gate is mandatory only when the repository actually maintains it as such or project/release policy explicitly requires it. Otherwise broad failures are triaged for attribution; candidate-caused failures block, clearly pre-existing unrelated failures are repository-health findings.
16. If no trustworthy performance baseline exists, report absolute performance and do not claim relative speedup; do not manufacture elaborate historical/counterfactual baselines solely to preserve a comparative claim.
17. Scientific/numerical, persistence/recovery, security, distribution, and performance checks remain strict when material. Simplification must reduce paperwork, not real validation.
18. Documentation closeout is proportional: specification-code parity and actual architecture/API/migration changes remain acceptance-critical; changelog/version/release notes follow repository lifecycle; PDFs/provenance manifests are required only when the project ships or explicitly requires them.
19. Verification reviews material design conformance and evidence sufficiency, not administrative hash completeness. Fresh-context independence is recommended for high-risk work but is not itself a rerun trigger unless project policy requires it.
20. Anti-bureaucracy invariant: **no administrative or evidence-format defect may by itself require product requalification**. If correcting an artifact does not change candidate code, material test inputs/environment, acceptance semantics, or interpretation of an observed result, valid execution evidence remains valid.
21. Future blocking protocol rules must identify the concrete software failure they prevent, show why an existing simpler rule is insufficient, and justify why advisory treatment is inadequate.
22. Keep protocol version `3.0.0`: v3 is still pre-freeze and the four-role architecture remains intact; this is correction through dogfooding, not a new major lifecycle.

## Acceptance-critical requirements

A1. The four role authorities remain distinct and no role may infer PASS for a mandatory check that did not execute.

A2. Qualification cannot silently change product code, scientific/configuration/dataset/backend semantics, or acceptance thresholds merely to obtain PASS.

A3. A real product/material failure routes to implementation or design; an unavailable required environment/input routes to `BLOCKED`; a harmless harness/record defect can be corrected locally without product requalification.

A4. The default Git candidate identity is sufficient for normal repository work, while real external/generated content boundaries can still use hashes when materially useful.

A5. Administrative metadata defects cannot by themselves invalidate otherwise applicable execution evidence or force a new candidate/workplan/handoff.

A6. Evidence rerun decisions are materiality-based: changes that could affect a check rerun it; unrelated administrative changes do not.

A7. Broad regression policy distinguishes candidate-caused regressions from pre-existing unrelated repository failures unless an explicit globally-green release policy applies.

A8. Scientific/numerical, persistence/recovery, security, package/install, production-data, and performance acceptance checks remain available and strict when the workplan makes them material.

A9. Canonical protocol source and generated skill packages remain deterministic and source-derived; generated-package drift remains a material artifact-boundary check.

A10. The simplified protocol dogfoods on the MVSEL2 workflow without restarting qualification solely for metadata, report-format, cwd/path, or other harmless harness errors.

## Non-goals

- Remove the four-role architecture.
- Weaken actual correctness, scientific, recovery, security, distribution, performance, or production-data acceptance.
- Allow qualification to redesign product semantics.
- Eliminate all hashes; hashes remain appropriate at real content boundaries.
- Force every repository into one test policy or release process.
- Preserve backward compatibility with every unfinished intermediate v3 hardening artifact; v3 is not frozen.

## Gate summary

| Gate | Status | Purpose |
|---|---|---|
| S0 | PREPARED | Freeze materiality-first design and acceptance list |
| S1 | PENDING | Simplify lifecycle/workplan/handoff doctrine |
| S2 | PENDING | Simplify candidate identity, evidence reuse, rerun, and versioning doctrine |
| S3 | PENDING | Rewrite testing/qualification semantics and broad-regression policy |
| S4 | PENDING | Simplify all four role skills |
| S5 | PENDING | Replace default templates with compact proportional forms |
| S6 | PENDING | Rewrite semantic/lifecycle regression checks around safety properties |
| S7 | PENDING | Make documentation/version/provenance policy proportional |
| S8 | PENDING | Rebuild generated distributions and run canonical protocol checks |
| S9 | PENDING | MVSEL2 dogfood and final v3 freeze verification |

## Gate definitions

### S1 — Lifecycle doctrine

Rewrite `workplans-and-agent-handoff.md` so the four roles remain authoritative but artifacts are proportional, gate state is simple, the workplan acceptance list is primary, handoffs freeze material intent rather than exact shell syntax, and administrative corrections cannot cause requalification.

Acceptance: A1, A3, A5 are explicit and internally consistent.

### S2 — Identity/evidence/rerun doctrine

Rewrite `protocol-versioning-and-compatibility.md` around Git commit identity by default, optional hashes at real content boundaries, material-change evidence reuse, and material workplan revisions. Remove mandatory SHA chains, universal identity policies, dependency manifests, retry taxonomy, and output-class state machinery.

Acceptance: A4, A5, A6 and v2 compatibility remain clear.

### S3 — Testing and qualification doctrine

Rewrite `testing-and-qualification.md` to preserve the proportional evidence ladder and strict material checks while adding harness-repair authority, material failure routing, broad-regression attribution, and absolute-vs-relative performance behavior.

Acceptance: A1-A8 are enforceable without metadata ceremony.

### S4 — Role skills

Shorten the four role `SKILL.md` files to consume the simplified doctrine. Design owns material target/acceptance; implementation constructs product/tests and prepares real execution handoffs; qualification executes and may repair harmless harness issues; verification reviews material conformance/evidence.

Acceptance: no role requires universal candidate-content identities, handoff/report hashes, dependency manifests, retry labels, or administrative reruns.

### S5 — Templates

Make the default workplan, optional qualification run card, evidence summary, and verification report compact. Required fields are only those needed to identify the task/candidate and understand material checks/results. Optional sections cover high-assurance or expensive workflows.

Acceptance: a normal cross-environment qualification can be understood without a chain of digests or policy IDs.

### S6 — Protocol regression checks

Rewrite `check_protocol_semantics.py` and `check_protocol_lifecycle_cases.py` to test safety behavior rather than mandatory metadata strings. At minimum exercise:

- mandatory not-run cannot PASS;
- candidate/product semantic change invalidates affected evidence;
- material dataset/config change invalidates affected evidence;
- administrative report typo does not invalidate PASS;
- handoff cwd/path correction is permitted when material intent is unchanged;
- qualification cannot silently change product semantics;
- candidate-caused regression blocks;
- pre-existing unrelated broad failure does not automatically fail a candidate absent globally-green policy;
- generated-source/distribution drift remains detectable.

### S7 — Documentation/version proportionality

Revise `documentation-and-evidence.md` and related release/spec references where necessary so current spec/code parity remains strong while PDF provenance, release/version synchronization, and structured manifests become project/release-driven rather than universal acceptance gates.

### S8 — Build/parity qualification

Run canonical semantic/lifecycle checks, rebuild all four generated skills from `source/`, and verify deterministic `dist/` parity. Generated ZIPs/BUILD_INDEX are a real content boundary, so deterministic parity remains acceptance-critical.

### S9 — Dogfood/freeze

Re-run the current MVSEL2 workflow under the simplified doctrine. Qualification may correct harmless cwd/path/log/report mistakes in place, but real product/material failures still block. Final verification assesses A1-A10 and returns `MERGE_READY | NOT_READY | DESIGN_REVISION_REQUIRED`.

S9 is the only gate expected to require the external/workstation MVSEL2 environment. All deterministic protocol-repository work should be completed before that boundary.

## Design-revision triggers

Return to design only if implementation would require:

- collapsing or changing the four authority roles materially;
- allowing qualification to modify product semantics as normal behavior;
- allowing mandatory unexecuted checks to count as PASS;
- weakening an actual scientific/correctness/security/recovery/performance acceptance requirement;
- abandoning source-derived deterministic generated distributions;
- introducing a new blocking administrative rule that cannot satisfy the materiality test.

Operational/template/editorial corrections are not design revisions.

## Completion

S0-S8 should be completed in the protocol repository without external qualification. S9 performs the real-workflow dogfood and final verification. Do not stop implementation for metadata mismatch, formatting, path spelling, or other non-material coordination defects; fix them in place and continue.
