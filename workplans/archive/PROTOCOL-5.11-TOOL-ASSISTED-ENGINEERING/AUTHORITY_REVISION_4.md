---
kind: implementation-workplan-amendment
workplan_id: PROTOCOL-5.11-TOOL-ASSISTED-ENGINEERING
parent_workplan: ../PROTOCOL-5.11-TOOL-ASSISTED-ENGINEERING.md
protocol_version: 5.10.0
target_protocol_version: 5.11.0
status: frozen
revision: 4
supersedes_revision: 3
reviewed_date: 2026-09-03
base_implementation_commit: 23fc4339d9cdad1172b81d5e999a925c57f93858
---

# Protocol 5.11 Rework Authority — Revision 4

This amendment is the current rework authority for the single blocking implementation nonconformance remaining after Revision 3 review. The parent workplan and Revision 3 remain authoritative for all already-accepted Protocol 5.11 design and repaired ownership semantics except where this amendment strengthens the R13 test implementation and evidence below.

This is a bounded implementation repair. It does not redesign Protocol 5.11, change source methodology, alter the target version, or reopen R12.

## Preserved accepted state

- `source/shared/references/tool-assisted-engineering.md` remains the single canonical tool-method owner and its current policy text is semantically accepted.
- Revision 3 R12 is closed: `source/README.md` remains release/connective wording only.
- Serena, Semgrep, and Hypothesis remain optional evidence/development capabilities, not authorities, dependencies, lifecycle stages, or universal gates.
- Protocol 5.4-5.10 doctrine and all parent O1-O11 obligations remain preservation territory.
- Target protocol identity remains `5.11.0`.

## R14 — Make R13 polarity checks structurally coupled

### Concern

The Revision 3 helper `assert_negative_policy` uses a broad proximity regex. Its `not` alternative lacks token boundaries and can match characters inside unrelated words such as `another`. More generally, proximity to any negation is insufficient evidence that the protected subject itself is negated. Therefore the composition regression can still remain green under a positively mandated three-tool pipeline, violating R13's explicit counterfactual.

The Hypothesis anti-gaming check similarly verifies mechanism words, a prohibition token, and a green-acceptance phrase independently at paragraph scope. Those facts can coexist even if one protected mechanism is positively permitted to game acceptance.

### Required end state

Focused Protocol 5.11 acceptance must couple the protected semantic subject to the required policy polarity at the smallest practical clause/sentence boundary:

1. **Composition:** the clause/sentence containing `mandatory three-tool pipeline` must itself express that the pipeline is not required/mandatory. A negation elsewhere, or the letters `not` embedded in another word, must not satisfy the assertion.
2. **Hypothesis anti-gaming:** the clause/sentence that lists filtering/health-check/exploration manipulation must itself prohibit those manipulations for the purpose of manufacturing a green property. Settings changes must remain conditioned on legitimate test/project semantics with required coverage preserved.
3. Direct mutation-style unit cases must demonstrate that the semantic helper rejects representative inverted policies, including at minimum:
   - `one another ... mandatory three-tool pipeline` with no true negation;
   - a positively mandatory-pipeline sentence followed by an unrelated negative sentence;
   - a Hypothesis sentence that prohibits one mechanism but explicitly permits health-check suppression or equivalent gaming.

### Required implementation consequence

Update only `tests/test_protocol_511_tool_assistance.py` unless a newly discovered necessary consequence requires more. Replace the broad paragraph-proximity helper with bounded sentence/clause extraction and explicit accepted negative constructions for the protected subject. Use word/token boundaries for negative operators. Keep reasonable wording flexibility; do not exact-match the whole canonical paragraph.

For Hypothesis, assert the current anti-gaming sentence as a governed prohibition over the relevant mechanism list and green-acceptance purpose, and separately assert the settings sentence preserves the legitimate-change plus coverage-retention condition. Add helper-level counterexamples so future weakening of the semantic matcher is itself detected.

Do not modify `tool-assisted-engineering.md` merely to satisfy tests: its current semantics are correct. Do not introduce general mutation-testing infrastructure or a semantic linter.

### Acceptance evidence

- Focused tests pass on the current accepted source policy.
- Direct helper counterexamples fail the negative-policy predicate when the pipeline is positively mandated, even when `another` or an unrelated later negation is present.
- Direct Hypothesis counterexample demonstrates that partial/inverted permission to game acceptance is rejected.
- Existing Protocol 5.11 routing, packaging, ownership, Serena, Semgrep, Hypothesis durability/isolation, authorization, portability, and non-substitution assertions remain intact or stronger.
- The complete repository unittest suite passes.
- Canonical package build, independent package validation, committed `dist/` parity, and `git diff --check` pass on the assembled candidate.

## Rework affected surface and closure

Expected direct delta from `23fc4339d9cdad1172b81d5e999a925c57f93858`:

- this Revision 4 amendment;
- `tests/test_protocol_511_tool_assistance.py`.

No source methodology or generated distribution content should change. Final review must confirm that the diff is limited to those surfaces and that no temporary workflow/debug machinery is introduced.

The repair is one coherent non-product test-hardening stage. Production qualification and live external-tool qualification remain unnecessary.

With prior conversation and review state removed, this amendment plus the parent workplan, Revision 3, and current repository state fully recover the remaining blocker, corrected end state, required implementation consequence, and acceptance evidence.