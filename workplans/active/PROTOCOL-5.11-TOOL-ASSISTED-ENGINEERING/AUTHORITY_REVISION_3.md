---
kind: implementation-workplan-amendment
workplan_id: PROTOCOL-5.11-TOOL-ASSISTED-ENGINEERING
parent_workplan: ../PROTOCOL-5.11-TOOL-ASSISTED-ENGINEERING.md
protocol_version: 5.10.0
target_protocol_version: 5.11.0
status: frozen
revision: 3
supersedes_revision: 2
reviewed_date: 2026-09-02
base_implementation_commit: 8bccd564de91ac28bfc8ac94c1bd243600587966
---

# Protocol 5.11 Rework Authority — Revision 3

This amendment is the current rework authority for the two blocking implementation nonconformances found during independent Software Design review of revision 2 at implementation candidate `8bccd564de91ac28bfc8ac94c1bd243600587966`.

The parent workplan remains frozen and authoritative for all Protocol 5.11 design, O1-O11 obligations, preservation constraints, and acceptance requirements except where this amendment strengthens the implementation consequences and evidence required to close the two findings below. This is implementation repair, not a redesign or doctrine change.

## Preserved frozen design

The following remain unchanged:

- Protocol 5.11 is a backward-compatible methodological/capability upgrade only.
- `source/shared/references/tool-assisted-engineering.md` is the single canonical owner of Serena/Semgrep/Hypothesis operational methodology.
- Lifecycle entrypoints retain only compact domain-conditional routes to that owner.
- Serena, Semgrep, and Hypothesis remain optional evidence/development capabilities rather than authorities, generic dependencies, lifecycle stages, or universal gates.
- Protocol 5.4-5.10 doctrine, lifecycle, workplan authority, testing/acceptance, proxy-proof boundaries, routing/distribution architecture, and snapshot-complete handoff semantics remain preservation territory.
- Target protocol identity remains `5.11.0`; no new version bump is introduced by this repair.

## R12 — Restore single-owner documentation boundaries

### Concern

The implementation added a substantive `## Tool-assisted engineering` section to `source/README.md` that repeats operational Serena, Semgrep, and Hypothesis method/safeguard content. This conflicts with the frozen one-canonical-reference design and O9's constraint that release documents outside the canonical tool reference and lifecycle routes receive only version/connective wording.

### Required end state

`source/README.md` must remain a concise current-release overview. It may:

- identify Protocol 5.11 as the optional tool-assisted methodology release;
- state the high-level non-authority/non-dependency/non-substitution boundary;
- identify or link `shared/references/tool-assisted-engineering.md` as the canonical detailed owner.

It must not independently restate operational Serena, Semgrep, or Hypothesis methods, backend/edition caveats, scan-accounting rules, property-test mechanics, or tool-state safeguards already owned by the canonical reference.

### Required implementation consequence

Remove the duplicated operational `## Tool-assisted engineering` subsection from `source/README.md` while preserving the concise release identity already present in the introduction and canonical-owner list. Do not move that duplicated detail into another README or generic reference.

### Acceptance evidence

- Source review shows detailed tool methodology has one current owner: `source/shared/references/tool-assisted-engineering.md`.
- `source/README.md` still describes Protocol 5.11 accurately and names the canonical tool-method owner without operational duplication.
- Existing README/version contract tests remain green.

## R13 — Make Protocol 5.11 regressions polarity-safe

### Concern

The focused regression for optional tool composition currently asserts only that the neutral substring `mandatory three-tool pipeline` exists. That check can remain green if the policy is inverted to require a mandatory pipeline. Similar neutral-token checks must not be the only protection for material negative safeguards.

### Required end state

Focused Protocol 5.11 tests must fail when a material protected policy is semantically inverted while remaining tolerant of reasonable local wording changes. At minimum, tests must protect the polarity of:

1. tool composition being optional/non-mandatory rather than required;
2. Hypothesis filtering/settings/health-check manipulation being forbidden when done merely to manufacture green acceptance;
3. external/cloud disclosure of source/findings/credentials requiring explicit project/user authorization.

Where another acceptance-critical negative safeguard in the focused module is currently protected only by a neutral keyword, strengthen it when a small semantic assertion can prevent an inverted-policy false pass without turning the test into paragraph-format lint.

### Required implementation consequence

Refactor `tests/test_protocol_511_tool_assistance.py` with small semantic helpers/assertions that inspect the relevant clause or paragraph and establish required polarity. Prefer bounded phrase/paragraph semantics or targeted regular expressions over exact full-paragraph matching.

Do not weaken source policy text to satisfy the tests. Do not require one exact connective such as `not`, `never`, or `without becoming` when several equivalent negative constructions correctly preserve the invariant.

### Acceptance evidence

- The composition test cannot pass on text that positively mandates the three-tool pipeline.
- The Hypothesis anti-gaming test establishes both the affected mechanism (filtering/settings/health checks or equivalent) and a prohibition tied to manufacturing a green property.
- The external-service test establishes a positive authorization requirement, not merely the presence of words such as `authorization` or `cloud`.
- Existing Serena mutation/memory, Semgrep rule/scope, Hypothesis durability/isolation, packaging, routing, authority, and portability checks remain intact or stronger.

## Rework affected surface

Expected direct edits:

- this revision-3 amendment;
- `source/README.md`;
- `tests/test_protocol_511_tool_assistance.py`.

Generated `dist/` does not require a content change unless implementation evidence shows a packaged canonical source changed. Nevertheless, final source-to-generated parity must be rechecked on the assembled candidate.

No lifecycle role, canonical tool reference, build registry, protocol-version history, portability policy, specialist skill, package validator, or preserved Protocol 5.4-5.10 doctrine should change unless a newly discovered necessary consequence proves otherwise.

## Rework acceptance

On the assembled repair candidate:

1. Review R12 and R13 semantically against this amendment and the parent frozen plan.
2. Run the focused Protocol 5.11 test module.
3. Run the complete repository unittest suite.
4. Build canonical skill packages to a temporary distribution.
5. Validate generated packages independently.
6. Verify committed `dist/` parity with the generated candidate.
7. Run `git diff --check`.
8. Review the final diff from `8bccd564de91ac28bfc8ac94c1bd243600587966` and confirm it is limited to the workplan amendment, README ownership repair, semantic-test strengthening, and any strictly implied generated output.
9. Confirm no temporary CI/debug machinery remains and no Protocol 5.4-5.10 normative owner was modified.

Production qualification and live Serena/Semgrep/Hypothesis qualification remain unnecessary for this bounded repair.

## Handoff closure

With prior chat/review state removed, this amendment plus the parent workplan and current repository fully state the two blocking findings, corrected end states, implementation consequences, preserved design, affected surface, and acceptance evidence. No rework requirement depends on the independent-review conversation alone.
