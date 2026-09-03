---
kind: implementation-workplan-amendment
workplan_id: PROTOCOL-5.11-TOOL-ASSISTED-ENGINEERING
parent_workplan: ../PROTOCOL-5.11-TOOL-ASSISTED-ENGINEERING.md
protocol_version: 5.10.0
target_protocol_version: 5.11.0
status: frozen
revision: 5
supersedes_revision: 4
reviewed_date: 2026-09-03
base_implementation_commit: 153857351dadde4487ebe6e635daf6f1644ac4c4
---

# Protocol 5.11 Rework Authority — Revision 5

This amendment reopens Protocol 5.11 implementation after a full Software Design review of candidate `153857351dadde4487ebe6e635daf6f1644ac4c4` against the parent workplan and Revisions 3-4. It supersedes Revision 4 as the current rework authority and consolidates all blocking findings found in that comprehensive review so implementation is not repaired one counterexample at a time.

This remains a bounded implementation/test-hardening repair under the existing frozen Protocol 5.11 design. It does not redesign the methodology, change the target version, reopen README ownership, or authorize changes to preserved Protocol 5.4-5.10 doctrine.

## Preserved accepted state

The following implementation state is accepted and must remain unchanged unless a newly discovered necessary consequence proves otherwise:

- `source/shared/references/tool-assisted-engineering.md` is the single canonical detailed owner and its current Serena, Semgrep, Hypothesis, tool-state, trust-boundary, and completion methodology is semantically accepted.
- Both lifecycle entrypoints have compact domain-conditional direct routes to the canonical reference; the route is not role-critical for unrelated tasks.
- `source/build_skills.py` packages the new reference for `software-design` and `software-implementation` only; specialists do not receive an unlinked copy.
- Revision 3 R12 remains closed: `source/README.md` keeps concise release/connective wording and names the canonical detailed owner without duplicating operational tool method.
- Protocol identity/release wording remains `5.11.0`; `source/PROTOCOL_VERSION`, protocol-versioning history, root/source README wording, and `PORTABILITY.md` correctly describe a backward-compatible optional capability/methodology refinement.
- Serena, Semgrep, and Hypothesis remain optional evidence/development capabilities, not generic dependencies, lifecycle roles/stages, authorities, or substitutes for affected regression/integration.
- Generated distribution content and package parity at the reviewed implementation candidate are accepted; this rework is expected not to change canonical source or `dist/` content.
- Existing Protocol 5.4-5.10 hierarchy, lifecycle, workplan authority, proxy-proof, stage/final acceptance, routing/distribution, and snapshot-complete semantics remain preservation territory.

The remaining blockers are in the focused Protocol 5.11 acceptance implementation. Green repository CI at the reviewed candidate is valid functional evidence for the code it executes, but it cannot close acceptance predicates that can remain green under direct semantic inversions or omit explicit parent-workplan acceptance requirements.

## R15 — Implement bounded clause-level polarity rather than sentence-plus-synonym whitelists

### Concern

Revision 4 requires the protected policy to be coupled at the smallest practical clause/sentence boundary. The current helper still defines sentence boundaries only with terminal `.?!` punctuation. A semicolon therefore leaves contradictory policy clauses inside one unit. The subsequent Hypothesis and settings checks compensate with finite lists of positive/negative words, which has repeatedly produced new direct false passes when an ordinary unlisted construction is used.

Representative current false passes include:

```text
The tools can reinforce one another without becoming a mandatory three-tool pipeline; a mandatory three-tool pipeline is required.
```

```text
Do not use excessive filtering, health-check suppression, disabled useful phases, removed deadlines, or reduced exploration solely to make a property green; health-check suppression is acceptable solely to make a property green.
```

```text
Change settings when project/test semantics justify it and required coverage remains intact; required coverage is no longer necessary.
```

```text
Change settings when project/test semantics justify it and required coverage remains intact; required coverage may be sacrificed.
```

These are direct, ordinary contradictions of the protected policy, not exotic natural-language attacks.

### Required end state

Focused acceptance must use a bounded policy-clause model sufficient for the canonical policy text and representative direct inversions:

1. **Clause extraction:** split policy units at terminal sentence punctuation and at semicolons at minimum. Commas must not be treated as generic clause separators because the canonical anti-gaming sentence contains a mechanism list. Additional strong separators may be supported if useful, but no general NLP parser is required.
2. **Composition:** inspect every extracted clause containing `mandatory three-tool pipeline`. At least one such clause must exist, and every such clause must express that the pipeline is not required/mandatory. A negative clause cannot mask a later positive clause about the same protected subject.
3. **Hypothesis anti-gaming:** every extracted clause that couples any protected anti-gaming mechanism with the green-manufacturing purpose must itself be a governed prohibition. Do not accept a valid prohibition merely because another clause with the same protected purpose uses an unrecognized positive-permission synonym.
4. **Hypothesis settings:** the governing `change settings` clause must positively condition the change on legitimate project/test semantics and preserve required coverage. Any additional extracted policy clause in the same relevant paragraph that refers to settings or required coverage must not reopen or weaken either condition. A bounded implementation may reject such an additional clause unless it independently preserves the same condition; it does not need to recognize every possible English synonym for weakening.

### Required implementation consequence

Refactor the semantic helpers in `tests/test_protocol_511_tool_assistance.py` around bounded clause extraction. Remove or retire synonym-chasing logic such as the current positive-permission and coverage-relaxation word lists where clause structure makes them unnecessary. Do **not** close this finding by merely adding `acceptable`, `no longer necessary`, `sacrificed`, or the next discovered synonym.

Keep reasonable wording flexibility and targeted structural predicates. Do not exact-match the entire canonical paragraph, introduce a general semantic linter, or add mutation-testing infrastructure.

Add direct helper-level cases for all four examples above. The existing Revision 3/4 counterexamples must remain rejected.

## R16 — Cover the complete Hypothesis anti-gaming subject defined by the parent workplan

### Concern

The canonical source and parent O7 explicitly protect representative generated domains against gaming through excessive filtering/`assume`, over-narrow strategies, exclusions, health-check suppression, disabled useful phases, removed deadlines, and reduced exploration. The current helper's `required_scope` covers only:

```text
filtering
health-check suppression
disabled useful phases
removed deadlines
reduced exploration
```

It omits `assume`, over-narrow strategies, and exclusions. Therefore the focused predicate can remain green while one of those omitted mechanisms is explicitly permitted solely to manufacture a green property.

Representative current false passes include a valid prohibition for the five currently listed mechanisms followed by any of:

```text
Over-narrow strategies are allowed solely to make a property green.
Assume may be used solely to make a property green.
Exclusions are permitted solely to make a property green.
```

### Required end state

The anti-gaming semantic test must protect the complete parent-workplan subject:

- excessive filtering;
- `assume`;
- over-narrow strategies;
- exclusions;
- health-check suppression;
- disabled useful phases;
- removed deadlines;
- reduced exploration.

The canonical complete prohibition must pass. Any extracted policy clause that permits any one of these mechanisms for the green-manufacturing purpose must fail, even when another clause correctly prohibits the rest.

### Required implementation consequence

Make the full protected mechanism set explicit in the focused helper or equivalent bounded logic. Add direct mutation-style cases covering `assume`, over-narrow strategies, and exclusions. Preserve reasonable wording flexibility; do not require an exact whole-paragraph string match.

## R17 — Close explicit O6/O7 focused-acceptance coverage gaps

### Concern

The parent workplan requires focused tests to protect several safeguards that are present correctly in canonical source but are not currently asserted with sufficient specificity. Source correctness alone does not satisfy an explicit durable-regression acceptance requirement.

### Semgrep required coverage

O6/O10 require focused protection for the zero-finding scan contract and external-rule identity. The current focused module protects CE compatibility, `.gitignore`, `.semgrepignore`, `nosemgrep`, general scan-contract wording, known-positive/known-negative rule validation, and autofix. It does not directly protect all of these required dimensions:

- actual target paths/languages scanned;
- rule/analysis limitations that can create false negatives;
- acceptance-critical rule identity not depending solely on a volatile network-fetched ruleset;
- proportionate pin/version/governance of that identity when exact identity materially affects the claim.

Add concise semantic assertions for those source guarantees. Do not introduce Semgrep execution, a permanent ruleset, or a cloud dependency merely to test prose.

### Hypothesis required coverage

O7/O10 require focused protection for bounded execution and durable/non-authoritative cache semantics. The current focused module mentions the example database and checks several durability phrases, but it does not directly establish all of these required safeguards:

- resource-bounded property/stateful execution (`max_examples`, object sizes, stateful step counts, deadlines/expensive operations, and scientific workloads) while preserving representative coverage;
- the local example database is cache/replay state and **not durable regression authority by itself**;
- a material minimized counterexample is preserved with an explicit ordinary regression, `@example`, or another understandable governed input when that adds stable protection.

Add concise semantic assertions for those guarantees. Existing seed/replay, state-isolation, oracle-integrity, settings anti-gaming, and non-substitution checks must remain intact or stronger.

## Rework affected surface

Expected direct delta from reviewed implementation commit `153857351dadde4487ebe6e635daf6f1644ac4c4`:

- this Revision 5 amendment;
- `tests/test_protocol_511_tool_assistance.py`.

No canonical methodology, lifecycle entrypoint, build registry, README, portability, versioning, specialist, package-validator, generated `dist/`, or preserved doctrine content should change. If implementation discovers a genuine source-policy defect rather than a test defect, stop and route that evidence back to Software Design instead of rewriting accepted source to satisfy the harness.

This is one coherent test-hardening stage. Do not create a sequence of micro-stages for individual counterexamples.

## Acceptance evidence

The assembled repair candidate must satisfy all of the following:

1. The current accepted canonical `tool-assisted-engineering.md` passes the focused Protocol 5.11 module without source changes.
2. All Revision 3, Revision 4, and Revision 5 direct polarity counterexamples are rejected by the relevant helper.
3. Composition rejects a negative semicolon clause followed by a positive mandatory-pipeline clause.
4. Hypothesis anti-gaming rejects direct positive green-manufacturing policy for each omitted mechanism: `assume`, over-narrow strategies, and exclusions, as well as the previously covered mechanisms.
5. Hypothesis anti-gaming rejects an unlisted ordinary permission construction such as `health-check suppression is acceptable solely to make a property green` without adding that word to a synonym whitelist.
6. Hypothesis settings rejects both `required coverage is no longer necessary` and `required coverage may be sacrificed` after an otherwise valid retention clause without solving the issue by enumerating those exact phrases.
7. Focused Semgrep assertions explicitly protect target paths/languages, rule/analysis limitations, volatile external-rule identity, and proportionate identity governance in addition to the already-covered ignore/suppression/rule-validation/autofix safeguards.
8. Focused Hypothesis assertions explicitly protect bounded execution, example-database non-authority, durable counterexample preservation, seed/replay limits, state isolation, oracle integrity, and non-substitution.
9. Existing Protocol 5.11 routing, packaging, README ownership, Serena safeguards, tool optionality, cloud authorization, tool-content non-authority, portability, and composition-opportunity checks remain intact or stronger.
10. The complete repository unittest suite passes without weakening/removing existing assertions or fixtures.
11. Canonical package build succeeds.
12. Independent package validation succeeds.
13. Committed `dist/` parity succeeds; because canonical source is not expected to change, no generated content delta is expected.
14. `git diff --check` succeeds.
15. Final diff from `153857351dadde4487ebe6e635daf6f1644ac4c4` is limited to this Revision 5 amendment and the focused test module unless a newly discovered necessary consequence is separately justified.

Production qualification and live Serena/Semgrep/Hypothesis qualification remain unnecessary for this bounded rework.

## Handoff closure

With prior conversation/review state removed, this Revision 5 amendment plus the parent workplan, Revisions 3-4, and the supplied current repository recover all still-binding Protocol 5.11 semantics and all currently known blocking rework requirements. Implementation must repair the complete R15-R17 set together and then run final assembled acceptance; passing one representative counterexample does not close the rework while another listed obligation remains open.
