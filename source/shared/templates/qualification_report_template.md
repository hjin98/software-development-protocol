---
kind: qualification-report
report_id: REPLACE_ME
protocol_version: REPLACE_WITH_SKILL_PROTOCOL_VERSION
qualification_handoff_id: REPLACE_ME
qualification_handoff_sha256: REPLACE_ME
workplan_id: REPLACE_ME
plan_revision: REPLACE_ME
workplan_sha256: REPLACE_ME
candidate_commit: REPLACE_ME
candidate_content_identity: REPLACE_ME
candidate_identity_policy: REPLACE_ME
overall_status: NOT_RUN
---

# Qualification Report

## Environment

- OS/runtime:
- Dependencies:
- CPU/GPU/HPC/backend:
- Precision/device:
- Relevant configuration/environment identity:
- Working directory:
- Import/source origins where material:

## Candidate preflight

- `HEAD == candidate_commit`: ...
- Candidate content identity recomputed/matched: ...
- Candidate tracked/staged state clean: ...
- Undeclared untracked execution-affecting files absent: ...
- Submodule/LFS identity checked if applicable: ...
- Notes/exceptions: ...

## Check results

| Check | Gate(s) | Capability | Mandatory now | Status | Exit | Attempts | Command/evidence |
|---|---|---|---|---|---|---|---|
| Q1 | ... | TARGET_RUNTIME | yes | NOT_RUN | - | 0 | ... |

Allowed check states:

```text
PASS
FAIL
BLOCKED
NOT RUN
DEFERRED
```

For `DEFERRED`, record whether it is mandatory for current acceptance and the explicit target milestone/workplan.

`overall_status: PASS` is permitted only when every check mandatory for current acceptance executed and passed.

## Per-check execution provenance

For every executed check record:

- check ID;
- exact command and cwd;
- start/end timestamp;
- exit code;
- attempt number and retry mode;
- input/fixture identities;
- source/config/environment/backend/device identity;
- stdout/stderr/log locations and digests when retained;
- measurements/artifacts and digests;
- result state and rationale.

## Retry history

- Mode used: `NONE | IDENTICAL_RETRY | CLEAN_RETRY | RESUME_RETRY`
- Attempts:
- Cleanup/resume state used:
- Confirm no undeclared policy/candidate change occurred: ...

Any retry that changed candidate product content or undeclared scientific/configuration/resource/backend/dataset policy invalidates execution under this handoff.

## Evidence reuse

For reused prior evidence record:

- prior report/evidence identity;
- declared dependency set;
- changed candidate/config/input/environment dimensions;
- why dependencies remain compatible;
- verification-required note when reuse is nontrivial.

Ambiguous dependency is not reusable evidence.

## Failures/blockers

- Earliest violated requirement:
- Reproducer/log/evidence:
- Routing: `RETURN_TO_IMPLEMENTATION | DESIGN_REVISION_REQUIRED | BLOCKED`

## Evidence artifacts

- ...

## Candidate postflight / source immutability

- Candidate content identity unchanged: ...
- Tracked candidate source/output unchanged: ...
- Only declared ephemeral/write paths changed: ...
- Undeclared untracked execution-affecting files absent: ...
- Post-run import/source origin state if material: ...

If candidate product content changed, this report cannot qualify the new candidate; issue a new candidate/handoff/report after implementation adopts the change.
