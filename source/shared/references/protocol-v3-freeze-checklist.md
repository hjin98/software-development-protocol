# Protocol v3 Freeze and Dogfood Checklist

This is a protocol-maintenance checklist, not a generated role runtime contract.

Protocol v3 should not be declared frozen merely because the four SKILL.md files read consistently. Before freeze, verify generated-package integrity, identity/immutability behavior, lifecycle semantics, and one real expensive-execution workflow.

## Static/build checks

- `PROTOCOL_VERSION` is the intended major version.
- Canonical role directories exactly match builder `ROLE_SPECS`.
- Each role frontmatter `name` equals package name.
- Every referenced role resource is packaged.
- Canonical templates do not hard-code a semantic protocol version.
- `python source/check_protocol_semantics.py` passes.
- Deterministic ZIP rebuild matches committed `dist/`.
- `BUILD_INDEX.json` lists exactly four v3 roles.
- No legacy v2 role ZIP remains in v3 distribution.
- CI runs semantic and canonical/generated parity checks.

## Candidate identity and immutability cases

Exercise:

1. candidate commit/content identity happy path;
2. evidence-only coordination commit after qualification preserves candidate content identity;
3. product-source/spec/package/tracked generated change alters candidate identity;
4. expected HEAD with dirty tracked candidate file is rejected;
5. expected HEAD with undeclared untracked import/build/runtime-shadowing file is rejected;
6. controlled declared untracked/ephemeral output cannot affect candidate execution;
7. qualification changes only allowed `EPHEMERAL_QUALIFICATION_OUTPUT` paths;
8. attempted `TRACKED_CANDIDATE_OUTPUT` mutation is rejected/returned to implementation;
9. postflight candidate identity mismatch invalidates the report;
10. import/source-origin mismatch is detected where material.

## Evidence dependency and retry cases

Exercise:

1. explicit dependency set permits safe reuse after unrelated candidate delta;
2. intersecting dependency forces rerun;
3. ambiguous/undeclared dependency defaults to invalidation;
4. `IDENTICAL_RETRY` keeps candidate/config/state policy identical;
5. `CLEAN_RETRY` removes only declared ephemeral state;
6. `RESUME_RETRY` resumes only declared checkpoint/authoritative state;
7. policy-changing/backend/dataset/resource/scientific retry is rejected as same-handoff retry.

## Lifecycle cases

Exercise:

1. happy path: design -> implementation -> qualification PASS -> verification `MERGE_READY`;
2. stale workplan assumption -> `STALE_WORKPLAN`;
3. stale candidate commit/content identity -> qualification refuses execution;
4. mandatory qualification FAIL -> `RETURN_TO_IMPLEMENTATION`;
5. unavailable target hardware/data -> `BLOCKED`, never PASS;
6. `qualification_barrier: yes` -> dependent implementation waits;
7. `qualification_barrier: no` -> independent implementation may be prepared;
8. blocking deferred mandatory check prevents `READY_FOR_VERIFICATION` and `MERGE_READY`;
9. non-current-acceptance deferred check records explicit target milestone;
10. source/content change after qualification invalidates affected evidence only under explicit dependencies;
11. mismatched/tampered workplan/handoff/report identity -> verification rejects evidence;
12. implementation evidence reveals frozen-design contradiction -> `DESIGN_REVISION_REQUIRED`;
13. invalid workplan/gate status combination is detected during verification;
14. trivial low-risk edit -> compressed path retains executed checks and explicit acceptance without four-artifact ceremony;
15. verification report records fresh/shared/unknown independence honestly.

## Bootstrap migration case

Preserve the original v2-governed `SDP-V3` workplan as bootstrap lineage for initial v3 construction, then use a v3-governed continuation/hardening workplan for v3 qualification/freeze. This must exercise the documented v2 `MIGRATE` semantics rather than rewriting completed v2 history.

## Representative real-workflow dogfood

Before v3 is frozen, use one nontrivial workflow where:

- substantial design reasoning already exists;
- source construction is separate from expensive target execution;
- production/runtime evidence is meaningful;
- evidence-only commits occur without changing product candidate identity;
- independent final review can detect unsupported PASS/reuse claims.

Prefer the current mdstats MVSEL2 hardening workflow. Record workplan/handoff/report/verification identities and any protocol corrections discovered.

A successful dogfood run proves the role boundaries and identity model are operationally useful; it does not require all four formal artifacts for every future trivial edit.
