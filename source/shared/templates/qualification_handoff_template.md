---
kind: qualification-handoff
handoff_id: REPLACE_ME
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
workplan_id: REPLACE_ME
plan_revision: REPLACE_ME
workplan_sha256: REPLACE_ME
source_ref: REPLACE_ME
source_commit: REPLACE_ME
status: PREPARED_FOR_QUALIFICATION
product_source_mutation: FORBIDDEN
allowed_write_paths: []
---

# Qualification Handoff

## Objective

Execute only the source-bound qualification defined below. Do not repeat architecture/design reconnaissance already frozen by the workplan.

## Prepared implementation

- Source commit: ...
- Workplan: ...
- Implemented/prepared gates: ...
- Candidate closeout state: ...

## Required capabilities

- ...

## Execution environment prerequisites

- ...

## Qualification checks

### Q1 — <name>

- Gate(s): ...
- Mandatory: yes
- Capability: `TARGET_RUNTIME`
- Working directory: ...
- Command: `...`
- Inputs/fixtures: ...
- Expected result: ...
- Evidence/output paths: ...
- Allowed retry policy: ...
- Notes: ...

## Failure routing

- Product-source/test-contract defect -> `RETURN_TO_IMPLEMENTATION`
- Frozen design/acceptance contradiction -> `DESIGN_REVISION_REQUIRED`
- Missing environment/data/hardware -> `BLOCKED`
- External/irreversible action not authorized -> stop for approval

## Forbidden work

Unless a check explicitly authorizes otherwise:

- do not mutate product source;
- do not redesign architecture/algorithms/policy;
- do not perform repository-wide reconnaissance;
- do not refactor unrelated code;
- do not rewrite the governing workplan.
