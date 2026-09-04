---
kind: implementation-workplan
workplan_id: PROTOCOL-5.13-TOOL-ROUTING-CODEQL-COMPRESSION
protocol_version: 5.12.0
target_protocol_version: 5.13.0
status: completed
completed_date: 2026-09-03
created_date: 2026-09-03
frozen_date: 2026-09-03
reviewed_date: 2026-09-03
reopened_date: 2026-09-03
refrozen_date: 2026-09-03
reopened_again_date: 2026-09-03
refrozen_again_date: 2026-09-03
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
3. **GitHub code-scanning result/alert surface** — repository-hosted findings/results that may originate from GitHub-managed CodeQL, externally uploaded CodeQL SARIF, or other analyzers.

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

## Current refrozen acceptance-oracle rework authority — 2026-09-03

**Plan verdict:** PASS and frozen for implementation. **Current implementation verdict:** NO-PASS only on the bounded acceptance-oracle/test family described below. The implemented Protocol 5.13 normative source, routing architecture, tool-specific ownership split, CodeQL methodology/provenance model, convergence extraction, versioning, packaging, and loaded-context reductions remain accepted and frozen unless new evidence independently invalidates them.

This section supersedes the earlier review-cycle appendices; it preserves their still-binding requirements without requiring prior chat, PR discussion, superseded review text, or historical Git archaeology.

### Root cause and bounded rework surface

The remaining defect is not Protocol 5.13 product design. During the ownership/compression refactor, several historical Protocol 5.11 directional tests were weakened to positive phrase checks, and the first Protocol 5.13 repair restored source linkage without fully restoring the historical inversion family or the complete trigger -> route -> capability-discovery -> disposition chain.

This is **incomplete implementation family closure** under O1/O2/O3/O4/O8 and final acceptance, not evidence for another routing/CodeQL/compression redesign.

The normal rework surface is therefore tests/helpers only. Normative source may change only if the strengthened source-linked oracle exposes an actual contradiction in a frozen rule; if so, repair only that affected rule and regenerate packaged derivatives as required. Do not broaden this into another Protocol 5.13 prose rewrite.

### Counterfactual-oracle contract and liveness

For every directional family below, the acceptance mechanism must be bounded, source-linked, nonvacuous, and capable of distinguishing a materially broken policy from the current valid one.

Each protected family needs, directly or through an equivalent shared helper:

1. **Current canonical-source positive:** the predicate accepts the actual current canonical policy unit that owns the rule.
2. **Compact valid fixture:** a minimal semantically valid policy is accepted when useful for readability and boundary testing.
3. **Canonical-source mutation:** at least one representative material negative mutates a **copy of that actual canonical policy unit inside the semantic scope governed by the predicate**, and the same predicate rejects the mutation.
4. **Additional representative inversions:** enough bounded mutations to cover the material failure classes listed below.
5. **Boundary preservation:** where the rule is conditional, a legitimate frozen exception/fallback remains accepted.

A detached toy-string mutation is insufficient if the same predicate never demonstrates that a material mutation of its actual source owner fails. Likewise, appending a contradiction outside a deliberately sliced paragraph/section does not establish liveness.

For the representative inversion basis below, apply a **monotonic contradiction counterfactual**: if the current governed source unit passes, retaining that valid wording while adding a materially conflicting clause **inside the same governed unit** must make the same predicate fail. A predicate is not live merely because it detects replacement/removal of the positive wording. Unrelated compatible additions must remain acceptable; this is bounded polarity protection, not a rule that any extra prose fails.

Use bounded line/row/paragraph/section extraction or an equivalent deterministic matcher. No general natural-language theorem prover, mutation-testing framework, semantic linter, policy DSL, or persistent routing ledger is required.

### Historical Protocol 5.11 directional preservation basis

Lossless preservation means the new split-owner tests must retain at least the material inversion classes previously exercised by the Protocol 5.12-base suite. Equivalent deterministic fixtures and helper structure are delegated; the semantic family may not be narrowed merely because the current positive wording uses fewer inverse terms.

**Mandatory-pipeline family — reject:**

- tools that `form a mandatory three-tool pipeline`;
- a direct declaration `This is a mandatory three-tool pipeline`, even if followed by unrelated anti-duplication prose;
- tools that `form a mandatory three-tool pipeline without extra ceremony`;
- a valid `without becoming a mandatory three-tool pipeline` rule followed by a conflicting `a mandatory three-tool pipeline is required` clause.

**Hypothesis anti-gaming family — reject:**

- a partial prohibition reopened by `but ... is permitted solely to make a property green`;
- `may be used solely to make a property green`, including a variant conditioned on failures being inconvenient;
- negated prohibition forms such as `Do not prohibit ... solely to make a property green`;
- misleading-negation permission such as `Do not worry; use ... solely to make a property green`;
- `should be used solely to make a property green`, whether in a later sentence or semicolon clause;
- an `unless solely to make a property green` escape hatch;
- `is acceptable solely to make a property green`;
- representative mechanism-specific reopenings including `assume may be used`, `over-narrow strategies are allowed`, and `exclusions are permitted` solely to manufacture a green property.

The valid boundary remains: filtering, assumptions, strategy/domain restriction, exclusions, health-check/phase/deadline settings, or exploration bounds may change when governed domain/test semantics genuinely require the change and it is not an attempt to manufacture acceptance.

**Hypothesis settings/coverage family — reject:**

- settings changed when project/test semantics `do not justify` or `fail to justify` the change;
- a valid justification followed by a statement that intact required coverage `is not required`;
- an `unless` escape hatch on preserving required coverage;
- later clauses allowing required coverage to be `discarded`, declaring it `no longer necessary`, or allowing it to be `sacrificed`.

The valid boundary remains: settings may change when project/test semantics justify the change **and required coverage remains intact**.

Implementation may port/adapt the prior bounded clause/paragraph logic against current split owners or implement a clearer equivalent stronger oracle. Existing Protocol 5.12 convergence/counterfactual tests are not part of this rewrite and must remain unchanged unless an independent defect in those tests is demonstrated.

### Protocol 5.13 routing-chain oracle

Close O1/O2/O3/O8 as one distributed semantic chain rather than a global filename census or isolated phrase checks:

```text
relation class
-> correct direct specific method (or ordinary-tools class)
-> no mandatory common-router second hop before the specific method
-> unknown availability -> cheap non-mutating probe when practical
-> available/current/supported/directly matching -> presumptive specialized use
   OR concrete permitted fallback
-> plausible analyzer blind spot -> proportionate cross-check
-> no fixed multi-tool pipeline
```

Canonical ownership is intentionally distributed:

- **lifecycle entrypoints** own relation-class -> correct direct tool-specific method (or ordinary class), conditional `MUST read`, and compact generic capability probe/disposition;
- **tool-specific references** own specialist selection boundaries, capability/model limitations, tool-specific fallbacks, and relevant model-limit cross-checks;
- the **compact common tool owner** owns overlap/composition, common evidence limits, and non-ceremonial multi-tool policy.

The oracle may compose evidence across those owners. It must not force detailed tool mechanics back into lifecycle entrypoints or specific-tool mechanics into the common owner merely to make testing easier.

For both lifecycle roles, protect all five class associations with stable local semantic anchors rather than only checking that filenames occur somewhere:

- literal/path/text or small deterministic local inspection -> ordinary repository search/read, with no forced specialist;
- symbol ownership/definition/callers/references/implementations/bounded semantic navigation -> Serena specific method;
- AST/syntax/structural patterns/variants/forbidden or legacy constructs/structural absence or uniqueness -> Semgrep specific method;
- broad/combinatorial Python input/state invariants -> Hypothesis specific method;
- supported interprocedural flow/taint/source-to-sink relations -> CodeQL specific method.

At minimum, source-linked route mutations must reject a Serena/Semgrep target swap, Hypothesis target substitution, CodeQL flow routed to ordinary or merely structural handling, and ordinary literal/local work forced into a specialist. Each specialized dispatch row must resolve to **exactly one required specific-tool target for that class**; the ordinary row must resolve to no forced specialist. Therefore also reject additive contradictions that retain the correct target while adding another wrong `MUST read`/specialist target on the same governed row. Prefer mutating the linked target or route meaning in a copied actual dispatch row/line so the mutation is inside the same semantic unit the predicate claims to govern.

**Direct-entry negative:** a policy that makes the common tool router a mandatory prerequisite/second hop before reading the triggered specific method must fail. Direct links plus reading the common owner when overlap/composition/common evidence policy itself is material remain valid.

**Capability-discovery negative:** when a specialized class fires, availability is genuinely unknown, and a cheap non-mutating probe is practical on the host, `never probe`, silently assume absence, or default to ordinary tools without checking must fail. The inverse overconstraint must also fail: do not require probing when availability is already known, when the host exposes no safe/practical cheap probe, or when already-permitted disproportionate setup for a trivially bounded claim makes concrete fallback appropriate. Test both directions against copied actual lifecycle policy units so the conditional is preserved rather than collapsed into either "never probe" or "always probe."

**Disposition/fallback negative:** built-in familiarity/default preference is not a permitted reason to skip an available/current/supported capability that directly models the claim. More generally, retaining the positive presumptive-use rule while adding that such a directly matching capability may be skipped **without a concrete permitted reason** must fail; the oracle may not protect only the familiarity wording. Concrete fallbacks such as unsupported language/backend, unavailable tool surface, irrecoverably stale state, model mismatch, disproportionate setup for a trivial bounded claim, or already-available equally reliable cheaper evidence remain valid.

**Model-limit negative:** an explicit policy that treats specialist output as exhaustive despite a plausible dynamic/generated/runtime/configuration/external-consumer blind spot must fail. The inverse overconstraint must also fail: the policy may not require a duplicate analyzer/search pass when no material blind spot exists. Protect both sides of the conditional with source-linked mutations; cross-checking is required when a material model blind spot can hide the claim and remains unnecessary ceremony when it cannot.

**Overlap/non-ceremony negative:** broad topic rules such as `security always means CodeQL`, structural-security routed away from Semgrep solely because it is security, and any fixed mandatory multi-tool pipeline must fail. Include an explicit source-linked structural-security inversion (for example, retaining the valid forbidden-call/structural rule while adding that the same forbidden-call relation must use CodeQL solely because it is security). Multi-relation claims may decompose and use the minimum capability set needed.

**Tool-specific owner liveness:** because selection boundaries, capability/model limitations, and tool-specific fallbacks are canonically owned by `tool-serena.md`, `tool-semgrep.md`, `tool-hypothesis.md`, and `tool-codeql.md`, a whole-file positive phrase census is insufficient. For **each of the four tool-specific owners**, the governing predicate must accept the actual current owner and reject at least one representative material contradiction inserted into a copied actual selection/capability/fallback policy unit. Use a tool-appropriate inversion—for example, forcing Serena onto literal/unsupported surfaces, allowing Semgrep to substitute for an interprocedural claim, forcing Hypothesis onto a small already-exhaustive deterministic case or permitting arbitrary skip of a triggered broad-state case, or forcing CodeQL onto a purely structural/security-by-topic claim. Equivalent stronger inversions are delegated. The composed routing-chain oracle must also fail when any one distributed owner is so inverted while all other owners remain valid.

This per-owner mutation requirement does **not** require duplicating detailed specialist mechanics into lifecycle/common owners and does not require one mutation for every sentence in a tool file. It closes the finite canonical-owner boundary of the routing-chain family.

### Already-accepted CodeQL/provenance/compression counterfactuals

The existing source-linked predicates for the following families were adequate in the last implementation candidate. Preserve them and keep them green; do not churn these owners unless the strengthened oracle exposes a concrete contradiction:

- CodeQL remains optional rather than a generic universal gate;
- changed relevant source/generated/build/dependency/extraction state invalidates stale database evidence, while unchanged relevant candidate/extraction/query state permits reuse;
- acceptance-critical **custom** CodeQL queries require representative validation, without turning that into a universal bespoke-fixture requirement for every built-in/project-governed query;
- zero results are bounded by the established database/query/model contract and cannot become a global absence claim;
- local/external execution, separately executed GitHub-managed/CI analysis, and code-scanning result hosting retain distinct provenance;
- rehosting local SARIF is not independent execution; local analysis cannot replace an explicitly required hosted run; stale/wrong-candidate hosted evidence is invalid for that required check; local analysis may remain sufficient when no hosted check is required;
- CodeQL analyzer-driven build hooks remain privileged/trust/resource controlled;
- compression ownership is checked over canonical normative `source/`, not required generated `dist/` copies; representative re-duplication of tool-specific mechanics into lifecycle/common owners or detailed convergence mechanics back into the role-critical workflow must fail when it defeats progressive disclosure.

### Acceptance-integrity constraints

Do not obtain a pass by:

- adding sentinel phrases to normative source solely for tests;
- weakening/deleting/skipping a known contradiction fixture;
- narrowing a predicate so the contradictory clause lies outside the policy unit it claims to govern;
- using synthetic fixtures while leaving actual canonical source ungoverned;
- replacing correct relation-to-target checking with global filename presence;
- accepting a row merely because the correct target remains present while a second wrong required specialist is added;
- accepting a current valid policy merely because its positive phrase remains present after an in-unit contradictory clause is added;
- treating tool-specific owner presence checks as liveness without a canonical-source contradiction mutation;
- re-expanding lifecycle/common/convergence prose merely to satisfy an exact-phrase test;
- opportunistically weakening Protocol 5.12 directional/counterfactual coverage.

Conversely, representative explicit material inversions are sufficient. The suite need not recognize every possible paraphrase. Stable semantic anchors and readable failure meaning outrank regex cleverness.

### Evidence reuse, exact candidate, and closure

The prior exact implementation candidate `8750f420efc6f0ed8c6f074cef97916077f65dfb` passed the normal PR regression, canonical build, independent package validation, committed-dist parity, and whitespace workflow. That evidence remains reusable only for dimensions not changed by the new test work. The final exact candidate must rerun the complete chain.

Before requesting independent closure review, Implementation must demonstrate:

1. current-owner positives plus in-unit canonical-source mutations for the historical 5.11 family and Protocol 5.13 routing-chain family;
2. the complete finite historical Protocol 5.11 inversion basis and its legitimate boundaries;
3. all five relation-class associations with unique per-row target ownership, direct entry/no mandatory second hop, practical unknown-availability probing **and its legitimate no-probe boundary**, presumptive-use/permitted-fallback polarity including arbitrary-skip rejection, conditional model-limit cross-check **and its no-blind-spot boundary**, structural-security overlap, non-ceremony, and canonical-source contradiction liveness for each Serena/Semgrep/Hypothesis/CodeQL specific owner;
4. the composed routing-chain predicate fails when a representative contradiction is introduced into each distributed owner class while unrelated owners remain valid;
5. the already-accepted CodeQL/provenance/compression counterfactual families remain green;
6. Protocol 5.12 convergence/counterfactual suites remain unchanged and green;
7. run the focused affected family first: `python -m unittest tests.test_protocol_511_tool_assistance tests.test_protocol_513_counterfactual_oracles tests.test_protocol_513_oracle_family_closure -v`;
8. then run complete `python -m unittest discover -s tests -v`;
9. `python source/build_skills.py --output <fresh-temp-dist>`;
10. `python source/validate_packages.py --dist <fresh-temp-dist>`;
11. `python source/check_dist.py --expected <fresh-temp-dist> --committed dist`;
12. `git diff --check`;
13. final tree/diff inspection confirms no temporary diagnostic/trigger artifacts or unintended normative-source changes remain;
14. a fresh independent Software Design review on that exact assembled candidate before closing or archiving this workplan.

If only tests and this workplan change, do not regenerate `dist/` merely to create byte churn; parity must still be checked. If canonical packaged source changes because the oracle exposes a real contradiction, regenerate derivatives before parity validation.

The bounded family is considered genuinely closed only when the current canonical owners pass, the finite inversion/boundary basis above passes, representative **additive in-unit contradictions** fail, each distributed owner class is mutation-live, the focused family command passes before the full chain, and the exact assembled candidate passes final acceptance. A later material failure in this same acceptance-oracle family becomes eligible for genuine post-family Design reconsideration only after that closure has actually been achieved and explicitly claimed. Until then, another miss is incomplete implementation family closure under this unchanged design.
