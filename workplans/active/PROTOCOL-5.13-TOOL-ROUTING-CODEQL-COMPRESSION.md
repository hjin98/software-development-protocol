---
kind: implementation-workplan
workplan_id: PROTOCOL-5.13-TOOL-ROUTING-CODEQL-COMPRESSION
protocol_version: 5.12.0
target_protocol_version: 5.13.0
status: frozen
created_date: 2026-09-03
frozen_date: 2026-09-03
reviewed_date: 2026-09-03
base_commit: b893eb428a81c71ee9f091d3e3b98417a656ac64
---

# Protocol 5.13 Deterministic Tool Routing, CodeQL Integration, and Lossless Compression Workplan

## Objective and protected concerns

Strengthen Protocol 5.12 so each material engineering question that fits a specialized capability reliably enters the relevant tool methodology and does not silently default to familiar lower-information tooling. Add CodeQL as an optional deep static/data-flow capability usable through local/external CLI execution and repository-hosted CI/code-scanning workflows. Perform a lossless progressive-disclosure compression pass so the new routing does not worsen control-plane attention and context cost.

Protocol 5.13 is a backward-compatible control-plane/methodology refinement. It preserves every material Protocol 5.4-5.12 doctrine and historical failure-mode defense: the exact engineering hierarchy, two-role lifecycle, stakeholder product truth, implementation fidelity, proxy-proof acceptance, stage-local/final affected regression, real-boundary integration, snapshot-complete handoff, deterministic reference routing, tool-evidence limits, convergence/family closure, review readiness, acceptance liveness, revision economy, and truthful non-closure.

The diagnosed failure occurs before the current Serena/Semgrep/Hypothesis method. Protocol 5.12 routes to `tool-assisted-engineering.md` only after the agent has already judged that semantic/static/property tooling would materially improve the task. A model strongly biased toward built-in search/read/shell/test primitives can therefore conclude that familiar tools are sufficient, never load the method that defines the specialized decision boundary, and never invoke an available higher-information capability.

Target state:

```text
Protocol 5.12 doctrine and safeguards
+ compact always-visible per-question dispatch
+ direct conditional entry into the relevant tool method
+ cheap capability discovery when availability is unknown
+ presumptive specialized use or a concrete permitted fallback
+ relation-first overlap/composition rules
+ CodeQL local/external + GitHub-managed provenance semantics
+ lossless progressive-disclosure compression
-> higher-information engineering with lower avoidable context/tool cost
-> no ceremonial tool pipeline, false completeness, or weakened acceptance
```

Protected concerns:

1. **No doctrine regression.** Routing/compression may reorganize control-plane ownership but may not weaken Protocol 5.4-5.12 product, acceptance, convergence, review, or portability guarantees.
2. **Entry plus disposition, not tool maximalism.** When a specialized question-class trigger fires, the role must enter the relevant method and then either use the available/reliable capability when it directly models the material claim or fall back for a concrete permitted reason. Familiarity with Grep/Read/shell/tests is not itself a fallback reason.
3. **Per-question routing.** Classification applies to each material engineering question as it arises, not once to the task as a whole. One task may activate several classes at different times.
4. **Relation-first classification.** Route by the relation under the current claim—literal text, semantic symbol relation, structural pattern, generated property/state space, or interprocedural data flow—not by a broad topic label such as “security.”
5. **Capability-aware discovery/fallback.** Tool absence, unsupported language/backend, stale/unreliable analysis state, or disproportionate setup cost for a trivially bounded claim permits alternative evidence; it never relaxes the engineering claim.
6. **No ceremonial pipeline.** Availability alone never requires Serena -> Semgrep -> CodeQL -> Hypothesis or another fixed multi-tool sequence.
7. **No false completeness.** Semantic/static/data-flow/property tools remain bounded models with language, extraction, build, configuration, generated-code, ignore/suppression, dynamic/runtime, query, and external-consumer blind spots.
8. **No replacement of executable acceptance.** Tool evidence supplements but does not replace required focused tests, stage-local/final affected regression, real-owner integration, repository/project-required checks, or production qualification where separately required.
9. **CodeQL provenance is explicit.** Local/external CodeQL execution, GitHub-managed CodeQL execution, and GitHub code-scanning result hosting are related but not identical evidence channels. Result location does not prove independent execution.
10. **No generic GitHub/CodeQL dependency.** Generic skill validity and ordinary task completion do not require GitHub, hosted code scanning, commercial entitlement, network access, or local CodeQL unless task/project authority independently requires them.
11. **No silent source disclosure or unsafe analyzer build.** Uploads, hosted analysis, credentials, build hooks, dependency installation, and analyzer-generated state obey existing trust, resource, and supply-chain policy.
12. **Lossless compression.** Reduce loaded-context duplication and conditional detail without deleting historical safeguards or making entry-critical rules less discoverable when needed.
13. **No arbitrary size chasing or bureaucracy.** Size is evidence. Do not add mandatory routing ledgers, tool reports, scan artifacts, telemetry systems, or lifecycle gates merely for Protocol 5.13.
14. **Honest qualification claims.** Static tests establish protocol semantics; live harness/tool behavior is claimed only where actually qualified.

## Engineering envelope and product design

### 1. Per-question dispatch and direct reference entry

Both lifecycle entrypoints must expose a compact dispatch rule applicable before detailed tool methodology is loaded:

```text
material engineering question
-> classify the relation under the claim
-> if specialized, read the directly linked method before relying solely on defaults
-> if availability is unknown, perform a cheap non-mutating capability probe when practical
-> use the specialized capability when available/reliable and materially appropriate
   OR take a concrete permitted fallback
-> cross-check where the analyzer model can miss material behavior
```

Required classes:

- **Literal/path/text lookup or small deterministic local inspection** -> ordinary repository search/read normally remains sufficient.
- **Symbol ownership, definition, callers/references, implementations, bounded semantic navigation, or symbol-aware editing on a nontrivial code surface** -> Serena class.
- **AST/syntax/structural pattern, API misuse, diagnosed structural variants, forbidden/legacy constructs, structural absence/uniqueness, or bounded syntax/structure census** -> Semgrep class.
- **Python behavior governed by a meaningful broad/combinatorial input space or operation/state-transition space** -> Hypothesis class.
- **Interprocedural data flow, taint propagation, source-to-sink reachability, or another supported relation whose material value depends on CodeQL's program/data-flow model** -> CodeQL class.

A security question is not automatically a CodeQL question. A forbidden-call pattern is normally structural/Semgrep-class; a multi-function untrusted-source-to-dangerous-sink claim is CodeQL-class.

When one claim spans classes, decompose it into distinct relations where practical and use the minimum capability set required. Do not invoke another analyzer merely to duplicate sufficient evidence.

### 2. Conditional MUST-read plus non-silent fallback

Replace the current subjective route (“read tool-assisted engineering when specialized tooling would materially improve the task”) with objective class triggers.

For a triggered class, the relevant tool-specific reference is a **conditional MUST-read** before substantive reliance on lower-information defaults. Unrelated tasks do not load tool references.

After the read:

- if the capability is known available, supported, current, and directly suited to the relation, presumptively use it;
- if availability is unknown, perform a cheap read-only/non-mutating capability probe when the host exposes one without material setup cost;
- skip/fall back only for a concrete reason such as unsupported language/backend, unavailable executable/tool surface, stale/unreliable semantic state that cannot economically be resynchronized, analyzer model mismatch, disproportionate database/rule/test setup for a trivially bounded claim, or already-available evidence that establishes the same claim at least as reliably and more cheaply;
- no persistent routing report is required. Invocation is trajectory evidence; a skipped triggered capability needs only enough local explanation to make the fallback non-silent.

Tool failure/unavailability is not an acceptance blocker unless task/project authority specifically requires that tool or no alternative evidence can establish the claim.

### 3. Progressive-disclosure tool ownership

Protocol 5.11's single `tool-assisted-engineering.md` owner is already about 16 KB before CodeQL. Whole-file readers would pay for unrelated tool mechanics. Protocol 5.13 therefore freezes a **common router + tool-specific canonical sub-owners** architecture:

- `source/shared/references/tool-assisted-engineering.md` — compact cross-tool selection, overlap/composition, common authority/evidence/trust/fallback/non-ceremony rules;
- `source/shared/references/tool-serena.md` — Serena-specific semantic navigation/editing/index/memory method;
- `source/shared/references/tool-semgrep.md` — Semgrep-specific rule/scan/structural/negative-evidence method;
- `source/shared/references/tool-hypothesis.md` — Hypothesis-specific property/stateful-testing method;
- `source/shared/references/tool-codeql.md` — CodeQL local/external analysis plus GitHub-managed/code-scanning method.

Equivalent filenames are delegated if repository conventions justify them, but the semantic ownership split is frozen unless implementation evidence shows it materially harms portable routing.

Both lifecycle entrypoints must directly link each triggered tool-specific reference. Do not require a second-hop read through the common router before reaching the specific method. Route to the common tool reference when overlap/composition/common tool-evidence policy itself is material.

`source/build_skills.py` and package validation must package all tool references for both lifecycle roles and continue excluding them from unrelated specialists absent a separately justified need.

### 4. Serena contract

Preserve Protocol 5.11/5.12 Serena semantics losslessly. When available and supported, Serena is normally first-choice for nontrivial semantic owner/definition/reference/caller/implementation relations, bounded symbol overview/body retrieval, and symbol-level edits whose semantic boundary matches the intended change.

Ordinary search remains appropriate for literal strings, filenames, configuration, dynamic registration, generated/external surfaces, unsupported language constructs, and cross-checking semantic incompleteness.

Preserve backend-capability honesty, dynamic/external cross-checks, stale-index resynchronization, ambiguous write-state inspection after failed mutation, current-source authority over memory/index state, and generated-state hygiene.

### 5. Semgrep contract

Preserve Protocol 5.11/5.12 Semgrep semantics losslessly. Prefer Semgrep for bounded AST/syntax/structural relations: diagnosed bug variants, API misuse, unsafe/nonconforming constructs, forbidden legacy paths, structural ownership/absence/uniqueness, suitable security-sensitive patterns, and independent structural challenge.

Preserve focused-rule preference where broad scanning is noisy, finding triage, engine/language bounds, acceptance-critical custom-rule known-positive/known-negative validation, scan target/ignore/suppression accounting, false-negative limits, rule identity governance when material, cloud/source-upload authorization, and ordinary acceptance of generated fixes.

### 6. Hypothesis contract

Preserve Protocol 5.11/5.12 Hypothesis semantics losslessly. Prefer Hypothesis when governed Python behavior defines a meaningful broad input/state space where generated exploration/shrinking materially strengthens coverage: round trips, parser/normalizer boundaries, algebraic/data-structure properties, numerical/domain edge cases, independent-reference equivalence, large combinations, and operation/state-transition sequences.

Small deterministic cases and genuinely exhaustive finite cases do not require Hypothesis merely because it is installed.

Preserve independent oracle integrity, representative domains without anti-gaming filtering/settings weakening, bounded resource execution, isolated/reset state, real semantic-owner execution where that owner is the claim, durable preservation of material counterexamples, cache/non-authority semantics, and ordinary stage/final regression/integration.

### 7. CodeQL local/external analysis contract

CodeQL is an optional deep static/program-analysis capability, not a routine universal scan.

High-value uses include interprocedural data/taint flow, source-to-sink reachability, security-sensitive flows crossing functions/modules, supported program relationships that lighter analysis cannot establish with adequate confidence, independent review of a data-flow claim through a distinct execution, and project-governed custom queries/suites where durable enforcement justifies them.

Required method:

1. Treat CodeQL CLI/runtime/query packs as environment capabilities, not bundled skill dependencies. Do not freeze a volatile install path, action version, UI path, or commercial product name into generic doctrine.
2. Determine actual language/analyzer support before relying on CodeQL; do not hard-code a permanent language list.
3. Create/reuse a database only while its source candidate, generated code, build/extraction conditions, dependency/configuration state, and extractor-relevant dimensions remain valid for the claim.
4. Rebuild/invalidate when changed source, generated code, build configuration, dependency resolution, or other extractor-relevant state can plausibly alter extraction or the relevant program/data-flow model. A stale database is not current-candidate evidence.
5. Choose build/extraction mode according to actual language/project needs. Any mode is evidence only for code actually extracted.
6. Treat analyzer-driven build/package hooks as privileged execution. Do not execute untrusted build scripts, install dependencies, or grant credentials/network access merely for analyzer convenience without existing authorization/trust requirements.
7. Use focused built-in/project-governed queries or suites proportionate to the claim. Broad suites remain valid when project policy or the claim warrants them; “narrow first” may optimize cost but cannot weaken required coverage.
8. Preserve query/query-suite/pack identity enough to interpret acceptance-critical results. Pin/version/govern exact query identity proportionately when a moving definition could materially change the claim.
9. Treat findings as evidence requiring repository-context triage, not automatic defects/blockers.
10. Bound zero-finding/completeness claims by database/source scope, language support, extraction/build success, generated/excluded code, query identity/model, configuration, and known analyzer limits.
11. Acceptance-critical custom queries require representative known-positive/known-negative validation or another convincing query test before relying on their results.
12. Bound disk/resource cost. Databases, caches, transient packs, SARIF, and results are derived state by default and should not be committed unless project policy deliberately governs them.
13. CodeQL does not replace runtime security tests, real-owner integration, affected regression, or another project-required analyzer when those claims are material.

### 8. GitHub-managed CodeQL and code-scanning provenance

Distinguish execution from result hosting:

1. **Local/external CodeQL execution** — CLI/database/query analysis executed outside GitHub-managed scanning; may produce/upload SARIF.
2. **GitHub-managed CodeQL execution** — CodeQL executed by GitHub default/advanced code-scanning configuration or an equivalent repository CI workflow under project policy.
3. **GitHub code-scanning result/alert surface** — repository-hosted results that may originate from GitHub-managed CodeQL, externally uploaded CodeQL SARIF, or other analyzers.

Consequences:

- a separately executed GitHub-managed/CI CodeQL run can provide independent execution/environment enforcement relative to a local run;
- uploading the same local SARIF to GitHub does **not** create independent execution evidence;
- result location/UI alone does not establish how or where analysis ran;
- when project policy names a GitHub-managed CodeQL/status check, local CLI results or uploaded SARIF cannot silently substitute for that required execution;
- required hosted evidence must correspond to the intended candidate/configuration and not stale alerts or unrelated branch/commit analysis;
- GitHub-managed scanning may remain active even when development agents never invoke local CodeQL, providing repository enforcement/defense in depth;
- generic protocol packages remain valid for non-GitHub repositories and repositories without hosted scanning capability/entitlement;
- enabling/disabling hosted security features, triggering costly remote workflows, or uploading local results remains subject to user/project authority and trust rules.

Current GitHub setup names/entitlement details belong in non-normative setup/portability guidance, not frozen protocol semantics.

### 9. Tool composition through the development cycle

Use the minimum capability combination that establishes material claims:

- **Diagnosis/ownership:** Serena for semantic owner/reference chains; ordinary search for literal/config/dynamic surfaces.
- **Variant/family discovery:** Semgrep for structural variants; Serena for semantic owners/callers; CodeQL only where the family relation is materially interprocedural/data-flow.
- **Implementation:** Serena may support bounded semantic edits; Semgrep may assert forbidden/legacy structure; Hypothesis may challenge invariant/state space; CodeQL may challenge changed security/data-flow consequences.
- **Independent review:** choose an evidence channel matching the challenged claim and materially increasing confidence; independence of execution/provenance must not be inferred from rehosting the same result.
- **Family closure:** use the minimal semantic/static/property/runtime combination that establishes the bounded family/canonical closure; no whole-repository four-tool census is implied.

Tool use remains subordinate to existing product/conformance/acceptance lifecycle. Passing analyzers cannot close omitted workplan obligations or unexecuted required runtime paths.

### 10. Lossless compression architecture

Protocol 5.12 baseline at `b893eb428a81c71ee9f091d3e3b98417a656ac64` is approximately:

- `source/roles/software-design/SKILL.md`: 15,823 bytes;
- `source/roles/software-implementation/SKILL.md`: 16,265 bytes;
- `source/shared/references/tool-assisted-engineering.md`: 16,052 bytes;
- `source/shared/references/workflow-and-workplans.md`: 26,789 bytes.

Protocol 5.8 treated roughly 9-11 KB Design and 10-12 KB Implementation as useful non-binding objectives. Protocols 5.11-5.12 legitimately added safeguards, so 5.13 does not mechanically restore those sizes. The regrowth is nevertheless sufficient to require a real progressive-disclosure pass rather than appending routing text.

#### 10.1 Lifecycle entrypoints

Keep directly in each `SKILL.md` only the role's high-salience decision loop; hard role-local product-truth/authority/acceptance invariants whose absence before reference loading could change behavior; deterministic direct reference/tool triggers; and compact convergence/review triggers whose loss could suppress required escalation.

Move detailed edge cases, examples, failure taxonomies, and mechanics to canonical owners.

The combined lifecycle-entrypoint byte count must be **lower than the 32,088-byte Protocol 5.12 baseline after the new dispatch is added**, unless independent Design review demonstrates that further lossless reduction is not safely available and reopens this specific decision. There is no individual-file byte target.

#### 10.2 Convergence progressive disclosure

`workflow-and-workplans.md` is role-critical and now contains substantial conditional Protocol 5.12 convergence detail. Create a dedicated conditional owner such as `source/shared/references/convergence-and-cycle-economy.md`.

Move detailed semantic-family definition, family-closure basis, recurrence-after-genuine-closure escalation, review-readiness/saturation mechanics, closure horizon, cycle-economy detail, and related examples there where ownership is coherent.

Keep compact directly recoverable invariants in `workflow-and-workplans.md` and lifecycle entrypoints:

```text
first clean local defect -> local owning-layer repair
material recurrence / repeated mechanism -> bounded semantic-family closure
same-family recurrence after genuine family closure -> bounded Design reconsideration
review readiness/saturation -> read convergence reference when triggered
```

Testing-specific acceptance-liveness and semantic-owner/test-double doctrine remain in `testing-and-validation.md`; do not move them merely for size.

#### 10.3 Tool-reference progressive disclosure

Apply the split in Section 3 so a Serena-only task need not load Semgrep/Hypothesis/CodeQL mechanics and vice versa. The common tool reference owns only true cross-tool semantics.

#### 10.4 Tests/templates/connective surfaces

Refactor tests that force detailed wording to be duplicated across owners. Detailed semantics are asserted in canonical owners; lifecycle tests protect indispensable triggers/polarity, not whole paragraphs. Preserve every historical counterfactual, including Protocol 5.12 convergence and Protocol 5.11 anti-gaming/negative-evidence cases.

Do not move duplication into README, `AGENTS.md`, templates, or test fixtures merely to improve role-file sizes. README/PORTABILITY/version history remain concise connective surfaces.

#### 10.5 Loaded-context diagnostics

Compare before/after minimal read sets for at least:

1. ordinary implementation with no specialized tool and no recurrence;
2. one specialized-tool task, including only the common/specific tool policy actually required;
3. recurrence/family-closure work requiring convergence method.

Report raw file bytes plus effective files/sections loaded in each scenario. Total packaged bytes may increase because new capability is added; optimize loaded context, duplication, and decision salience rather than ZIP size.

### 11. Routing/live qualification

Static contract tests protect dispatch/direct-link semantics but cannot establish model/harness compliance.

Add a bounded tool-routing qualification fixture/procedure distinct from Protocol 5.9's reference-read sentinel. For any harness/tool combination claimed behaviorally qualified:

- start from a fresh session/configuration with the tool genuinely available;
- use a representative prompt whose material relation unambiguously triggers that class;
- where traces are exposed, verify the directly linked method was read and either the specialized tool was invoked or a concrete permitted fallback was taken;
- record exact harness/model/tool configuration exercised;
- do not infer passes for other combinations.

Because live Serena under-calling initiated this change, if a trace-bearing harness with Serena is available during release work, run at least one caller/reference or semantic-owner scenario. If no suitable live environment is available, release may claim **stronger protocol-level deterministic routing semantics** but not empirically demonstrated universal tool-use compliance.

No permanent telemetry/benchmark service is required.

## Implementation obligations

### O1 — Deterministic per-question dispatch

**Concern:** Existing route is circular and can suppress specialized-tool entry.

**Required end state:** Both lifecycle entrypoints directly classify ordinary, Serena, Semgrep, Hypothesis, and CodeQL relations and directly link the relevant method.

**Constraints:** classification is per material question; broad topic labels do not determine the tool; overlap decomposes/composes minimally; ordinary literal/local work remains ordinary.

**Acceptance:** positive/negative counterfactual tests for every class plus overlap cases such as structural-security -> Semgrep and interprocedural-taint -> CodeQL.

### O2 — Capability discovery and non-silent disposition

**Concern:** Reading a method alone does not prevent silent fallback to familiar tools.

**Required end state:** A triggered capability not already known unavailable is probed cheaply when practical; an available/reliable directly matching capability is presumptively used or skipped for a concrete permitted fallback.

**Acceptance:** tests reject policies allowing ordinary tools solely because they are preferred/familiar and protect probe/fallback semantics without requiring a persistent routing report.

### O3 — Split tool-specific canonical ownership

**Concern:** One growing tool reference undermines progressive disclosure.

**Required end state:** Compact common tool owner plus Serena, Semgrep, Hypothesis, and CodeQL specific canonical references; direct links from both lifecycle entrypoints; packaging/validation updated.

**Acceptance:** package manifests contain all lifecycle references; specialists remain unaffected; direct-route tests prove no second-hop dependency for first specific-method read.

### O4 — Preserve Serena/Semgrep/Hypothesis semantics

**Concern:** Routing/refactoring must not regress Protocol 5.11/5.12 safeguards.

**Required end state:** Existing capability, integrity, trust, negative-evidence, anti-gaming, mutation-safety, cache/memory non-authority, and executable-acceptance limits remain semantically intact in new canonical owners.

**Acceptance:** Protocol 5.11 focused tests remain green after ownership-aware refactoring; direct semantic inversions remain rejected.

### O5 — Complete CodeQL local/external methodology

**Concern:** CodeQL adds a distinct data-flow/interprocedural model and introduces database/query identity, staleness, build-execution, and resource risks.

**Required end state:** `tool-codeql.md` covers selection boundary, support/availability, database candidate identity/invalidation, build/extraction trust, query identity/governance, custom-query validation, scope/negative-evidence limits, resource/state hygiene, finding triage, and non-substitution.

**Acceptance:** counterfactual tests reject stale-database acceptance, unbounded zero-findings claims, mandatory-universal CodeQL, untested acceptance-critical custom queries, and analyzer-build privilege bypass.

### O6 — Provenance-correct GitHub CodeQL/code scanning

**Concern:** Code-scanning result location can be mistaken for independent analysis execution.

**Required end state:** Protocol distinguishes local/external execution, GitHub-managed/CI CodeQL execution, and GitHub code-scanning result hosting; same-run uploaded SARIF is not independent execution; project-required hosted checks remain non-substitutable.

**Acceptance:** tests reject “uploaded local SARIF equals independent GitHub scan,” “local pass substitutes for required hosted check,” and stale/wrong-candidate hosted evidence.

### O7 — Lossless progressive-disclosure compression

**Concern:** Protocol 5.12 regrew entrypoints/role-critical references; 5.13 must not add another attention layer.

**Required end state:** Combined lifecycle entrypoints are below the 32,088-byte baseline; `workflow-and-workplans.md` sheds conditional convergence detail into a dedicated routed owner; common tool reference becomes compact; all historical safeguards remain recoverable/routed.

**Acceptance:** before/after bytes plus three minimal-read scenarios; retained duplication justified as entry/role critical; historical semantic/counterfactual suites remain green.

### O8 — Robust routing/compression tests and qualification

**Concern:** Phrase-presence tests can pass under inversion, while static tests cannot prove live model compliance.

**Required end state:** Deterministic tests protect trigger -> direct method entry -> capability discovery -> presumptive use/permitted fallback -> cross-check/non-ceremony. Qualification separately records actual harness behavior where available.

**Acceptance:** mutation/counterfactual tests for polarity, overlap, fallback, CodeQL provenance/staleness, and compression ownership; live qualification claims limited to executed combinations.

### O9 — Versioning, portability, packaging, release

**Concern:** Shipped protocol must expose 5.13 accurately without duplicating manuals or freezing volatile setup details.

**Required end state:** Protocol 5.13.0; version history describes deterministic tool entry, provenance-aware CodeQL integration, and lossless progressive disclosure; PORTABILITY describes external tool availability/qualification including CodeQL; build registry packages new references; README remains concise.

**Acceptance:** version/portability/routing tests, canonical build, package validation, committed-dist parity, and `git diff --check`.

## Implementation authority

### Frozen

- Target protocol version is **5.13.0**, governed by Protocol 5.12.0 until release.
- Protocol 5.13 is backward-compatible and preserves all Protocol 5.4-5.12 doctrine/acceptance semantics.
- Tool routing is per material question and relation-first.
- Triggered specialized classes have direct tool-specific reference routes and conditional MUST-read semantics.
- Unknown availability receives a cheap non-mutating probe when practical; available/reliable directly matching capability is presumptively used or skipped only for concrete permitted fallback.
- No universal multi-tool pipeline exists.
- Tool methodology uses a compact common owner plus tool-specific canonical sub-owners.
- Serena remains semantic navigation/reference/bounded editing; Semgrep structural/variant analysis; Hypothesis Python invariant/state-space testing; CodeQL supported interprocedural/data-flow analysis.
- Local/external CodeQL execution, GitHub-managed CodeQL execution, and GitHub code-scanning result hosting are distinct provenance concepts.
- Uploaded local SARIF is not independent execution merely because it appears in GitHub code scanning.
- CodeQL databases/results are candidate/extraction/query-state evidence and must be invalidated when relevant dimensions change.
- Hosted analysis is optional unless project/task authority requires it.
- Detailed Protocol 5.12 convergence mechanics become conditionally disclosed while compact escalation triggers remain visible.
- Combined lifecycle entrypoints must decrease from Protocol 5.12 baseline unless this criterion is reopened on evidence.
- Semantic preservation outranks compression magnitude.

### Delegated

- Exact concise dispatch wording/table layout, provided classes, direct links, overlap rules, and polarity remain recoverable.
- Exact non-mutating availability probe appropriate to each host/tool.
- Exact filenames of tool/convergence references if an equivalent ownership layout preserves frozen direct routing/progressive disclosure.
- Exact CodeQL CLI commands/examples; generic doctrine must not freeze volatile install/build/UI/action details.
- Exact test helper structure/module placement.
- Exact line-level compression edits preserving all frozen semantics.
- Additional live harness/tool combinations qualified beyond the available-Serena condition.

### Reopen only on evidence

Reopen only the affected design surface if evidence shows:

- direct per-tool references materially worsen portable routing compared with a single owner;
- a safe cheap capability probe cannot be expressed without unwanted side effects for a class/host;
- presumptive specialized use creates systematic waste on common trivial cases that fallback cannot bound cleanly;
- CodeQL local/GitHub provenance cannot be represented accurately under actual supported execution models;
- extracting convergence detail makes recurrence/review triggers materially less reliable;
- combined lifecycle entrypoint reduction cannot be achieved without losing entry/role-critical safeguards;
- common supported harnesses cannot express conditional direct routes portably.

Do not reopen broader Protocol 5 doctrine because a host lacks an optional tool.

## Affected surface and task-specific acceptance

Expected direct source surface:

- `source/roles/software-design/SKILL.md`;
- `source/roles/software-implementation/SKILL.md`;
- `source/shared/references/tool-assisted-engineering.md`;
- new Serena/Semgrep/Hypothesis/CodeQL tool-specific references;
- `source/shared/references/workflow-and-workplans.md`;
- new conditional convergence/cycle-economy reference;
- `source/shared/references/testing-and-validation.md` and `repository-intake.md` only where ownership links/triggers must change;
- `source/shared/references/protocol-versioning-and-compatibility.md`;
- `source/shared/templates/implementation_workplan_template.md` where convergence routing/compression requires it;
- `source/build_skills.py` plus package/build-index validation surfaces;
- `PORTABILITY.md`, `source/README.md`, root `README.md` for concise external-capability/release connective wording;
- Protocol 5.11 tool-assistance, Protocol 5.12 convergence/counterfactual, Protocol 5.8 compression, routing/portability, and new 5.13 tests;
- qualification fixture/procedure for live tool-routing behavior where economical;
- `source/PROTOCOL_VERSION` and generated `dist/` release derivatives.

Non-goals:

- installing/configuring CodeQL on every machine;
- enabling hosted code scanning on arbitrary downstream repositories;
- creating CodeQL MCP or lifecycle role;
- making CodeQL/Semgrep/Serena/Hypothesis generic dependencies;
- adding managed/cloud Semgrep requirements;
- changing downstream project-specific tool configuration;
- changing Protocol 5.12 convergence semantics rather than their ownership/loading;
- rewriting unrelated domain references for style;
- claiming empirical behavior for unqualified harness/tool combinations.

Final acceptance requires:

1. Both lifecycle entrypoints implement compact direct dispatch for ordinary, Serena, Semgrep, Hypothesis, and CodeQL relations.
2. Dispatch is per material question; overlap tests establish relation-first selection rather than topic classification.
3. Triggered specialized classes directly route to tool-specific method without second-hop dependency.
4. Unknown availability is probed cheaply when practical; tests reject silent fallback based solely on familiarity/default preference.
5. Supported/available directly matching capability is presumptively used or skipped only for concrete permitted fallback; no routing ledger is introduced.
6. Literal/local deterministic work is not forced through specialized tooling.
7. Serena/Semgrep/Hypothesis Protocol 5.11/5.12 safeguards remain semantically intact.
8. CodeQL local method protects candidate/database/query identity, invalidation, extraction/build trust, query validation/governance, negative-evidence limits, resource/state hygiene, and runtime/non-substitution boundaries.
9. GitHub-managed execution is distinguished from code-scanning result hosting; uploaded local SARIF is not misclassified as independent execution.
10. Project-required hosted checks cannot be silently replaced by local analysis or stale/wrong-candidate hosted results.
11. Tool unavailability routes to alternative evidence without relaxing engineering claim or generic skill validity.
12. No mandatory multi-tool pipeline or universal CodeQL gate is introduced.
13. Combined lifecycle entrypoint bytes are below the 32,088-byte Protocol 5.12 baseline unless Design formally reopens that criterion on evidence.
14. `workflow-and-workplans.md` materially reduces role-critical conditional convergence detail through a dedicated routed owner or equivalent reopened design.
15. Minimal-read diagnostics show before/after read set for ordinary, one-tool, and recurrence/family-closure scenarios; total package size is not the optimization proxy.
16. Existing Protocol 5.4-5.12 tests, including 5.11/5.12 counterfactual families, pass without semantic weakening.
17. New 5.13 tests reject direct inversions for dispatch, overlap, fallback, mandatory-pipeline, stale CodeQL database, unvalidated custom query, overbroad zero-findings, SARIF provenance, and compression ownership.
18. Canonical skill build succeeds.
19. Independent package validation succeeds.
20. Committed `dist/` parity succeeds.
21. Static portability/routing validation remains green.
22. When a suitable trace-bearing Serena harness is available during release work, bounded live semantic-route qualification is executed; otherwise final claim is limited explicitly to protocol-level routing semantics.
23. Other live harness/tool qualification is reported only for combinations actually executed.
24. `git diff --check` succeeds.
25. Final independent Software Design review confirms doctrine preservation, direct routing, CodeQL provenance correctness, loaded-context improvement, and no unjustified control-plane complexity.

Production qualification: unnecessary. Tool-routing live qualification is control-plane behavior evidence, not production workload qualification.

## Implementation sequence and redesign risks

### Stage 1 — Freeze routing behavior with counterfactual tests

Implement failing/positive semantic tests for per-question relation classification, direct tool-specific entry, overlap, availability probing, presumptive use/permitted fallback, ordinary-tool negatives, and non-ceremony before broad prose movement.

Close with semantic/conformance inspection plus affected routing/portability tests.

### Stage 2 — Refactor tool ownership and add CodeQL

Create compact common tool owner and tool-specific references; migrate Serena/Semgrep/Hypothesis losslessly; add complete CodeQL local/GitHub provenance method; update build registry/package validation/direct links.

Close with Protocol 5.11 regression, new CodeQL/provenance tests, affected security/trust/release/portability checks, and source/package reference validation.

### Stage 3 — Perform convergence/lifecycle compression

Extract detailed conditional Protocol 5.12 convergence mechanics into new routed owner, compress lifecycle entrypoints to role-critical loops/invariants/triggers, refactor duplication-enforcing tests, and preserve all counterfactual semantics.

Close with complete historical semantic/counterfactual suites and before/after minimal-read diagnostics. If combined entrypoint size cannot fall below baseline without semantic loss, stop and reopen that decision instead of deleting safeguards.

### Stage 4 — Version, package, qualify, final assemble

Update 5.13 version/connective surfaces; run canonical build, independent package validation, committed-dist parity, complete tests, routing/portability checks, and `git diff --check`. Run bounded live Serena routing qualification when suitable trace-bearing environment is available and scope empirical claims accurately. Perform final independent review on exact assembled candidate.

Material redesign risks:

- turning direct entry into universal mandatory tool execution;
- silent fallback after reference entry, leaving original under-calling intact;
- classifying by broad topic rather than relation and over-routing security to CodeQL;
- creating fixed multi-tool pipeline;
- splitting references in a way that introduces unreliable multi-hop routing;
- treating GitHub alert as independent analysis without execution provenance;
- reusing stale CodeQL databases/query definitions for current-candidate acceptance;
- analyzer-driven builds executing untrusted/project code without trust/resource control;
- solving routing by increasing always-loaded manuals;
- deleting convergence/acceptance safeguards to meet size goals;
- moving duplicated prose into README/templates/tests instead of fixing ownership;
- exact-phrase tests recreating control-plane bloat pressure.

## Conditional convergence guidance

Protocol 5.13 itself has two bounded semantic families.

**Tool-dispatch entry/capability-selection family:**

```text
relation under claim
+ entrypoint-visible direct trigger
+ tool-specific canonical method
+ availability/capability discovery
+ presumptive use or concrete fallback
+ model-limit cross-check
+ non-ceremonial negative case
```

If another integrated-tool bypass is caused by the same circular/silent-default mechanism, close it across both lifecycle roles and the affected tool family rather than patching one name. Same-family failure after genuine closure/qualification triggers bounded Design reconsideration before another wording-only patch.

**Control-plane ownership/compression family:** repeated regrowth caused by copying conditional canonical mechanics back into role-critical/always-loaded surfaces should be closed at ownership/routing level rather than recurring paragraph trimming.

## Handoff closure

The supplied implementation authority is this canonical workplan plus Protocol 5.12 repository at base commit `b893eb428a81c71ee9f091d3e3b98417a656ac64` and its current references/tests.

Apply snapshot-loss counterfactual: remove prior chat, initial Protocol 5.13 draft/review discussion, Protocol 5.11 design history, later Git history, and external Claude/Serena/CodeQL setup instructions. The remaining workplan/base repository recover:

- diagnosed circular/silent tool-entry failure;
- per-question relation-first dispatch/overlap rules;
- direct conditional tool-method entry;
- capability discovery and non-silent use/fallback semantics;
- Serena/Semgrep/Hypothesis preserved roles;
- CodeQL local/database/query/trust/resource method;
- local/GitHub-managed/code-scanning provenance distinctions;
- no generic hosted/tool dependency;
- tool and convergence progressive-disclosure ownership changes;
- directional loaded-context compression criterion;
- implementation authority, affected surfaces, counterfactual acceptance, live-qualification limits, and redesign triggers.

Implementation must preserve Protocol 5.12 doctrine by inheritance rather than copying it into new prose. No material requirement above may remain only in conversation or superseded review history after handoff.