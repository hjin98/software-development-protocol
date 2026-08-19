# Protocol v3 Freeze and Dogfood Checklist

This is a protocol-maintenance checklist, not a generated role runtime contract.

Protocol v3 should not be declared frozen merely because the four SKILL.md files read consistently. Before freeze, verify both generated-package integrity and lifecycle behavior.

## Static/build checks

- `PROTOCOL_VERSION` is the intended major version.
- canonical role directories exactly match builder `ROLE_SPECS`;
- each role frontmatter `name` equals its package name;
- every `references/`, `scripts/`, and `templates/` path named by a role is packaged;
- canonical templates do not hard-code a semantic protocol version;
- deterministic ZIP rebuild matches committed `dist/`;
- `BUILD_INDEX.json` lists exactly the four v3 roles;
- no legacy v2 role ZIP remains in the v3 generated distribution;
- CI runs the canonical builder `--check`.

## Synthetic lifecycle cases

Exercise:

1. happy path: design -> implementation -> qualification PASS -> verification `MERGE_READY`;
2. stale workplan assumption -> `STALE_WORKPLAN`;
3. stale Qualification Handoff source SHA -> qualification refuses execution;
4. mandatory qualification FAIL -> `RETURN_TO_IMPLEMENTATION`;
5. unavailable target hardware/data -> `BLOCKED`, never PASS;
6. `qualification_barrier: yes` -> dependent implementation waits;
7. `qualification_barrier: no` -> independent implementation may be prepared before expensive qualification;
8. source changes after qualification -> old report remains historical but does not qualify new source;
9. mismatched/tampered workplan/handoff/report identity -> verification rejects evidence;
10. implementation evidence reveals frozen-design contradiction -> `DESIGN_REVISION_REQUIRED`;
11. trivial low-risk edit -> compressed path works without unnecessary four-artifact ceremony.

## Representative real-workflow dogfood

Before v3 is frozen, use one nontrivial real workflow where:

- substantial design reasoning already exists;
- source construction can be performed separately from expensive target execution;
- production/runtime evidence is meaningful;
- independent final review can detect unsupported PASS claims.

Record the workplan/handoff/report/verification identities and any protocol corrections discovered.

A successful dogfood run proves the role boundaries are operationally useful; it is not a claim that every future project requires all four roles for every change.
