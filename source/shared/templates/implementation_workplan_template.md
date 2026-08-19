---
kind: implementation-workplan
workplan_id: REPLACE_ME
plan_revision: 1
status: DRAFT
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
analysis_base_ref: REPLACE_ME
analysis_base_commit: REPLACE_ME
assumption_paths: []
architecture_refs: []
spec_refs: []
expected_change_paths: []
default_gate_approval: AUTO
candidate_identity_policy: REPLACE_ME
---

# <Task> Implementation Workplan

## Objective

<One concise outcome statement.>

## Current diagnosis

<Evidence-grounded root cause/current limitation.>

## Current authority references

- Architecture: ...
- Specifications: ...
- Source/tests/evidence: ...

## Frozen design decisions

- ...

## Invariants and acceptance semantics

- ...

## Candidate identity policy

Define the repository policy/helper or explicit include/exclude classes used to compute `candidate_content_identity`.

- Included product/test/spec/package/generated surfaces: ...
- Excluded coordination/evidence-only surfaces: ...
- Dirty/untracked/import-origin controls required for qualification: ...

Do not exclude any path capable of changing build/runtime/scientific/release behavior merely to avoid requalification.

## Expected change surface

- Source: ...
- Tests: ...
- Candidate specs/docs/release: ...
- Benchmarks/audits: ...

## Non-goals

- ...

## Execution and resource constraints

- ...

## Qualification capabilities

Use only capabilities actually required:

- `SOURCE`
- `LOCAL_LIGHT`
- `TARGET_RUNTIME`
- `PRODUCTION_DATA`
- `TARGET_HARDWARE`
- `EXTERNAL_ACTION`

## Evidence dependency/comparability policy

For expensive evidence that may be reused after a correction, freeze consequential dependency dimensions or require each check to declare them. Ambiguous dependency defaults to rerun.

- Source/candidate components: ...
- Configuration identity: ...
- Input identities: ...
- Environment/backend/device dimensions: ...
- Upstream check dependencies: ...

## Gate summary

| Gate | Approval | Implementation | Qualification | Acceptance | Barrier | Purpose |
|---|---|---|---|---|---|---|
| G0 | AUTO | PENDING | NOT_RUN | PENDING | no | ... |

## G0 — <name>

**Approval:** AUTO  
**Qualification barrier:** no

**Goal:** ...

**Prerequisites:** ...

**Work:**
- ...

**Acceptance:**
- ...

**Qualification:**
- Capability: `LOCAL_LIGHT`
- Mandatory for current acceptance: yes
- Required check/evidence: ...
- Evidence dependencies: ...
- Retry mode: `NONE | IDENTICAL_RETRY | CLEAN_RETRY | RESUME_RETRY`
- Allowed ephemeral output paths/classes: ...

**Evidence:**
- ...

**Fallback/rollback:** ...

**Excluded/deferred:** ...

If a check is deferred, record:

```yaml
mandatory_for_current_acceptance: true|false
deferred_to: <workplan/release/milestone>
reason: <why>
```

## Design-revision triggers

Stop and report `DESIGN_REVISION_REQUIRED` if implementation would require changing:

- ...

## Final candidate closeout

Before qualification of a release-significant final candidate:

- [ ] Candidate current specifications match candidate code.
- [ ] Candidate architecture updated only for actual target architectural changes.
- [ ] Candidate history/changelog/version/release metadata staged according to repository policy.
- [ ] Required tracked generated product artifacts staged before qualification.
- [ ] Candidate content identity computed and recorded.
- [ ] Qualification Handoff declares only ephemeral qualification output writes.

## Final acceptance closeout

- [ ] All checks mandatory for current acceptance PASS.
- [ ] Any reused evidence has explicit dependency/comparability justification.
- [ ] Verification report is `MERGE_READY`.
- [ ] Final evidence records workplan ID/revision/SHA-256, candidate commit/content identity/policy, and protocol version.
- [ ] Workplan marked/archived only after acceptance.
