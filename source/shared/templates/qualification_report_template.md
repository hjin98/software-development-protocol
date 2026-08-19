---
kind: qualification-report
report_id: REPLACE_ME
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
qualification_handoff_id: REPLACE_ME
qualification_handoff_sha256: REPLACE_ME
workplan_id: REPLACE_ME
plan_revision: REPLACE_ME
workplan_sha256: REPLACE_ME
source_commit: REPLACE_ME
overall_status: NOT_RUN
---

# Qualification Report

## Environment

- OS/runtime:
- Dependencies:
- CPU/GPU/HPC/backend:
- Precision/device:
- Relevant environment/configuration identity:

## Check results

| Check | Gate(s) | Capability | Status | Command/evidence |
|---|---|---|---|---|
| Q1 | ... | TARGET_RUNTIME | NOT_RUN | ... |

Allowed check states:

```text
PASS
FAIL
BLOCKED
NOT RUN
DEFERRED
```

`overall_status: PASS` is permitted only when every mandatory check executed and passed.

## Failures/blockers

- Earliest violated requirement:
- Reproducer/log/evidence:
- Routing: `RETURN_TO_IMPLEMENTATION | DESIGN_REVISION_REQUIRED | BLOCKED`

## Evidence artifacts

- ...

## Source immutability

Record whether product source remained unchanged during qualification. If it changed, this report cannot qualify the new source revision; issue a new handoff/report for that source.
