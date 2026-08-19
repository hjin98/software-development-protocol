---
kind: qualification-handoff
handoff_id: REPLACE_ME
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
workplan_id: REPLACE_ME
plan_revision: REPLACE_ME
workplan_sha256: REPLACE_ME
candidate_ref: REPLACE_ME
candidate_commit: REPLACE_ME
candidate_content_identity: REPLACE_ME
candidate_identity_policy: REPLACE_ME
status: PREPARED_FOR_QUALIFICATION
product_source_mutation: FORBIDDEN
allowed_write_paths: []
---

# Qualification Handoff

## Objective

Execute only the source-bound qualification defined below. Do not repeat architecture/design reconnaissance already frozen by the workplan.

## Prepared candidate

- Candidate ref/commit: ...
- Candidate content identity: ...
- Candidate identity policy/include-exclude manifest: ...
- Workplan: ...
- Implemented/prepared gates: ...
- Candidate closeout state: ...

## Candidate preflight requirements

Before executing any check, verify as applicable:

- `HEAD == candidate_commit`;
- recomputed candidate content identity equals `candidate_content_identity`;
- no staged/tracked modifications on candidate surfaces;
- no undeclared untracked files can affect import/build/runtime;
- submodule/LFS identities match declared state;
- import/source origins and working directory are controlled where material.

If any condition fails, stop as stale/dirty candidate rather than executing against an ambiguous source state.

## Required capabilities

- ...

## Execution environment prerequisites

- ...

## Output classes

- `EPHEMERAL_QUALIFICATION_OUTPUT`: declared logs/reports/build scratch/temp packages/profiles/benchmarks; may be written only under allowed paths.
- `TRACKED_CANDIDATE_OUTPUT`: product/release files included in candidate identity; qualification must not create or modify them.

If target execution is needed to produce a tracked candidate artifact, place the proposed artifact in a declared ephemeral/evidence path and return it to implementation for adoption into a new candidate.

## Qualification checks

### Q1 — <name>

- Gate(s): ...
- Mandatory: yes
- Mandatory for current acceptance: yes
- Capability: `TARGET_RUNTIME`
- Working directory: ...
- Command: `...`
- Inputs/fixtures and identities: ...
- Expected result: ...
- Evidence/output paths: ...
- Output class: `EPHEMERAL_QUALIFICATION_OUTPUT`
- Allowed side effects: ...
- Evidence dependencies:
  - source paths/candidate components: ...
  - configuration identity: ...
  - input identities: ...
  - environment dimensions: ...
  - upstream checks: ...
- Retry policy:
  - mode: `NONE | IDENTICAL_RETRY | CLEAN_RETRY | RESUME_RETRY`
  - max attempts: ...
  - allowed cleanup/resume state: ...
- Notes: ...

## Postflight requirements

After execution:

- recompute/verify candidate content identity unchanged;
- verify no tracked candidate output/source changed;
- verify only declared output paths/classes changed;
- record dirty/untracked state and import/source origin where material.

## Failure routing

- Product-source/test-contract defect -> `RETURN_TO_IMPLEMENTATION`
- Frozen design/acceptance contradiction -> `DESIGN_REVISION_REQUIRED`
- Missing environment/data/hardware -> `BLOCKED`
- Candidate identity/dirty-tree mismatch -> stop as stale/ambiguous candidate
- External/irreversible action not authorized -> stop for approval

## Forbidden work

Unless a check explicitly authorizes an ephemeral output:

- do not mutate product source or tracked candidate outputs;
- do not redesign architecture/algorithms/policy;
- do not change scientific/configuration/resource/backend/dataset policy as a retry;
- do not perform repository-wide reconnaissance;
- do not refactor unrelated code;
- do not rewrite the governing workplan.
