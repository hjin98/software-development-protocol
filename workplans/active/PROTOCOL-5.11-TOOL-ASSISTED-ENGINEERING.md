---
kind: implementation-workplan
workplan_id: PROTOCOL-5.11-TOOL-ASSISTED-ENGINEERING
protocol_version: 5.10.0
target_protocol_version: 5.11.0
status: frozen
created_date: 2026-09-02
frozen_date: 2026-09-02
base_commit: 36ea966dc87d4feeee80abac2e24f79efe8f5999
---

# Protocol 5.11 Tool-Assisted Engineering Workplan

## Objective and protected concerns

Integrate the now-available **Serena**, **Semgrep**, and **Hypothesis** capabilities into the Software Development Protocol skills so agents can inspect repositories more precisely, reason from higher-information evidence, detect structural/static defects more reliably, and design stronger invariant-driven tests without changing the protocol's engineering doctrine, lifecycle, authority model, or acceptance philosophy.

This is a **methodological capability upgrade only**. The desired result is:

```text
same Protocol 5.10 engineering doctrine and lifecycle
+ capability-aware use of higher-information development tools
-> better repository understanding, defect detection, and test generation
-> less low-information context loading and fewer avoidable blind spots
-> unchanged product-truth, ownership, conformance, regression,
   integration, proxy-proof, and handoff semantics
```

Protected concerns:

1. **No doctrine or philosophy rework.** Protocol 5.11 must preserve the governing hierarchy exactly as `product engineering fitness > minimum justified product/system complexity > development economy`, the two-role lifecycle `software-design -> software-implementation`, and all Protocol 5.4-5.10 hardening unchanged in normative meaning.
2. **Tools augment engineering judgment; they do not become authority.** Serena symbol results/memories, Semgrep findings, and Hypothesis-generated examples are evidence or development aids. Repository source, governed contracts, accepted workplans, real product behavior, and required acceptance boundaries retain their existing authority.
3. **Optional capability, not a new hard dependency.** Skill behavior must improve when these tools are available and configured, while remaining valid and usable on harnesses or repositories where one or more are unavailable, unsupported, inappropriate, or intentionally disabled.
4. **No false completeness from semantic/static analysis.** Serena and Semgrep can narrow and strengthen inspection, but neither may be treated as proof that the complete affected surface has been found when dynamic dispatch, reflection, configuration, generated code, external consumers, runtime state, or unsupported language semantics can escape their model.
5. **No replacement of executable acceptance.** Semgrep/static evidence and Serena structural inspection never replace required focused tests, stage-local affected regression, final affected-surface regression, real-boundary integration, or repository/project-required checks.
6. **No replacement of example/regression testing by property generation.** Hypothesis supplements normal testing by exploring invariant-defined input spaces and operation sequences; it does not eliminate explicit regression cases, semantic-owner integration, or task-specific acceptance obligations.
7. **No hidden normative state in Serena memories or tool caches.** Tool-local memory, indexes, caches, databases, and generated analysis state may improve context economy, but still-binding requirements, frozen decisions, acceptance boundaries, and redesign triggers must remain recoverable from the supplied current authority under Protocol 5.10 snapshot-completeness rules.
8. **Reproducible acceptance over volatile convenience.** Exploratory external rule packs, ephemeral caches, random seeds, AI autofix suggestions, and similar conveniences may assist development but cannot be the sole basis for a durable acceptance claim unless the project independently pins and governs them sufficiently for that claim.
9. **No tool-maximalist process.** The protocol must not require running Serena, Semgrep, and Hypothesis ceremonially on every task. Tool choice follows information gain, affected risk, language/support fit, and execution cost under existing development-economy doctrine.
10. **No silent source disclosure or unsafe tool configuration.** Local analysis is the portability baseline. Cloud upload, external indexing, managed scanning, or other source-disclosing integrations require explicit project/user authorization and applicable security policy.

## Scope freeze — Protocol 5.4-5.10 is preservation territory

Protocol 5.11 authorizes one backward-compatible addition: **capability-aware tool-assisted engineering guidance** for Serena, Semgrep, and Hypothesis.

All existing Protocol 5.4-5.10 semantics remain preservation territory. In particular, implementation must preserve unchanged in normative meaning:

- the governing hierarchy and stakeholder durable-product objective;
- the two-role lifecycle and optional-specialist/non-gate status;
- progressive evidence-directed repository inspection, established-fact reuse, and context economy;
- minimum justified product/system complexity and the prohibition on process/tool bureaucracy without engineering value;
- accepted-workplan authority, minimum-known-contract semantics, local reconciliation, and bounded redesign;
- lossless Design -> Implementation translation, protected-concern preservation, required-consequence versus suggested-realization/delegation distinctions, and final accepted-contract reconciliation;
- coherent material stages, dual semantic/conformance plus functional closure, and stage-local affected regression;
- final affected-surface re-derivation/regression, real-boundary integration, repository/project-required checks, and production-qualification separation;
- evidence reuse/invalidation semantics;
- proxy-proof semantic-owner/test-double boundaries;
- anti-acceptance-gaming, truthful non-closure, and self-correction rules;
- Protocol 5.8 canonical ownership/progressive disclosure/effective compression;
- Protocol 5.9 deterministic reference routing, portable self-contained skill bundles, adapter separation, and live-harness qualification boundaries;
- Protocol 5.10 snapshot-complete handoff and current-authority rules.

Permitted normative additions are limited to describing **when and how these optional tools improve an already-required engineering activity**, plus the tool-specific safeguards needed to keep their evidence honest.

Prohibited under this workplan:

- redefining any product/design/testing/lifecycle principle because a tool enables a different workflow;
- adding a new lifecycle role, approval gate, mandatory analysis stage, mandatory persistent task ledger, or mandatory tool-output report;
- making Serena/Semgrep/Hypothesis prerequisites for generic skill validity or package installation;
- requiring harness-specific MCP configuration in generic skill metadata;
- weakening existing direct source inspection, affected-surface reasoning, regression, integration, or independent review because tool output appears comprehensive;
- treating a Serena memory, Semgrep finding set, Hypothesis example database, or external ruleset as normative task authority;
- folding unrelated protocol cleanup, wording modernization, compression, expansion, or doctrinal repair into this release.

A genuine defect discovered in preserved doctrine requires a separate bounded Software Design task and must not be silently repaired under Protocol 5.11.

## Engineering envelope and product design

### 1. One canonical tool-assisted engineering reference

Add one shared canonical reference, expected path:

```text
source/shared/references/tool-assisted-engineering.md
```

This reference owns tool-specific methodology for Serena, Semgrep, and Hypothesis. The lifecycle entrypoints remain compact and gain only a domain-conditional route to this reference when semantic repository navigation, static/structural analysis, or property-based/stateful testing would materially improve the current task.

This is the minimum-complexity design because:

- duplicating tool instructions in both lifecycle `SKILL.md` files would increase drift and entrypoint context;
- modifying every existing domain reference would spread tool-specific mechanics across generic doctrine owners;
- creating separate Serena/Semgrep/Hypothesis skills or lifecycle roles would incorrectly turn optional development instruments into process architecture;
- a single shared reference preserves Protocol 5.8 canonical ownership and Protocol 5.9 deterministic routing.

The new reference must itself route tool use back to the existing canonical engineering owners: repository inspection remains governed by `repository-intake.md`, testing/acceptance by `testing-and-validation.md`, security/trust questions by the existing security reference, and lifecycle authority by the existing workflow reference.

### 2. Capability-aware selection rule

The generic rule is:

```text
material engineering question
-> identify the cheapest sufficiently reliable evidence source
-> use Serena / Semgrep / Hypothesis when their model matches the question
-> cross-check or fall back where their model is incomplete
-> interpret output under existing protocol authority and acceptance rules
```

Agents should use the tools because they provide higher information density or broader defect discovery for a material question, not because they are installed.

Tool unavailability is not an acceptance failure unless an accepted workplan or project policy explicitly makes a particular tool execution a required check. When an optional tool is unavailable, use ordinary repository search/read/test mechanisms that establish the same required engineering claim.

### 3. Serena — semantic repository intelligence and bounded symbolic editing

Serena is integrated primarily as a **semantic repository-intake and code-navigation accelerator**.

Required method:

- Prefer symbol overviews and targeted symbol lookup when learning a code file or locating an implementation owner.
- Use reference/caller queries to follow dependency and affected-surface chains where the language backend can model them.
- Retrieve only the bodies/signatures needed for the current question rather than loading entire large files when bounded semantic retrieval is sufficient.
- In Software Implementation, symbol-level edits may be used when they match the required edit boundary and the agent has first inspected the actual symbol body/context being replaced or extended.
- After symbolic edits, inspect the resulting repository diff and execute normal semantic/conformance plus functional acceptance; successful Serena editing is not correctness evidence by itself.

Mandatory limitations:

- Do not infer that Serena found every consumer/reference when dynamic dispatch, reflection, generated code, configuration strings, external entry points, unsupported files/languages, language-server limitations, or runtime registration may hide dependencies.
- Cross-check with textual search, configuration/docs, generated-source inspection, runtime tests, or other evidence when those surfaces are plausible.
- Treat Serena indexes and project memories as caches/derived context. Stale or conflicting memory must yield to current source and current accepted authority.
- Serena memory may summarize durable repository conventions when project policy permits and doing so materially reduces rediscovery, but it must not become the sole storage for task requirements, workplan decisions, acceptance evidence, or current normative semantics.
- Do not require committing `.serena` or any Serena-generated state. Whether project configuration or memory is versioned is a repository/tooling policy decision; transient or local state must not be silently added to source control.

### 4. Semgrep — targeted structural/static analysis and negative evidence

Semgrep is integrated as an **AST-aware static-analysis and structural-query instrument**.

High-value uses include:

- locating syntax/AST patterns more precisely than raw text search;
- identifying repeated unsafe or nonconforming constructs during implementation/review;
- checking security-sensitive patterns when a suitable rule exists;
- constructing narrow repository-local rules for a diagnosed bug pattern, forbidden legacy path, API misuse, or structural absence claim;
- supporting independent review with a second evidence channel beyond the implementation agent's manual inspection.

Required method and limitations:

- Prefer focused queries/rules tied to the current concern over indiscriminate broad scanning when the latter would produce low-signal noise.
- Triage findings in repository context; a finding is evidence requiring interpretation, not automatically a defect, requirement, or blocker.
- Absence of Semgrep findings proves only what the selected rules/languages/dataflow model actually cover. It does not prove absence outside that modeled surface.
- For acceptance-critical custom rules, keep the rule or exact reproducible configuration under current task/project authority when durability matters; do not make a volatile network-fetched ruleset the sole evidence for a stable acceptance claim.
- Broad community/automatic configurations may be used for exploratory discovery, but new findings must be classified against the accepted affected surface and project policy rather than mechanically turning every advisory into scope.
- Autofix or AI-assisted remediation is never self-validating. Any applied fix is ordinary implementation output and requires source/diff review plus the same conformance and functional acceptance as a manually written change.
- Semgrep never replaces real-owner execution, regression, integration, runtime security testing, or project-required analyzers when those claims are material.

### 5. Hypothesis — invariant-driven property and stateful testing

Hypothesis is integrated as a **property-based test generation and shrinking instrument for Python projects**.

Use it when the contract naturally defines a broad input/state space, including:

- round-trip invariants such as encode/decode or serialize/deserialize;
- parser/normalizer/domain boundary behavior;
- algebraic/data-structure invariants;
- numerical/domain edge cases with meaningful bounded strategies;
- equivalence between an optimized implementation and an independent trusted/reference implementation;
- combinations that are impractical to enumerate manually;
- sequences of operations or state transitions where rule-based stateful testing materially improves coverage.

Required method and limitations:

- Derive properties from governed behavior/invariants, not merely from the current implementation's outputs. A property that reimplements the same bug is not an independent oracle.
- Keep generated domains representative of the actual contract. Do not use excessive filtering/assumptions or over-narrow strategies to make a property pass.
- Bound examples, object sizes, sequence lengths, and expensive scientific work so routine regression remains resource-safe while still exercising the required property.
- Preserve explicit regression protection for known material counterexamples when appropriate; do not rely solely on the local Hypothesis example database, which is cache-like development state rather than correctness authority.
- Use failure replay/seeds as debugging aids, not as a permanent substitute for an understandable durable property or explicit regression case.
- Hypothesis-generated tests participate in the same stage-local and final affected regression rules as other tests. Passing property tests do not prove omitted workplan obligations or untested integration boundaries.
- For stateful testing, the real production state machine/semantic owner under acceptance must execute when that owner is the claim. A model may serve as an oracle but may not replace the production owner and then establish proxy acceptance.
- Longer exploratory/fuzz-style runs may be useful, but they are not automatically required production qualification and must not make routine acceptance unbounded.

### 6. Tool state, persistence, and current authority

Tool-local state is classified as follows:

- **Serena indexes/memories:** derived repository context/cache unless a project independently promotes a specific configuration file to governed source.
- **Semgrep caches/external rule downloads/findings:** derived analysis state unless a project explicitly versions a local rule/config as part of its engineering policy.
- **Hypothesis example database:** generated test cache; useful for replay but not sufficient normative regression storage by itself.

The protocol must tell agents not to create a parallel persistent authority layer from these artifacts. If tool state is useful across sessions, it may be retained according to repository policy, but every still-binding task requirement and acceptance boundary remains in current supplied authority and every durable product/test contract remains represented in governed source/tests/docs as appropriate.

### 7. Portability and harness neutrality

Protocol 5.11 must remain generically installable as an Agent Skill bundle.

Therefore:

- do not add Serena MCP server declarations, shell paths, Python environment paths, API tokens, Semgrep credentials, or Hypothesis installation commands to generic skill metadata;
- do not assume a specific MCP tool recipient/name beyond describing recognizable Serena capabilities;
- do not add these tools to package-validation prerequisites;
- if a harness exposes Serena, use the harness's configured integration; otherwise follow the same method with available repository tools;
- Semgrep/Hypothesis invocation syntax may be illustrated where useful in the canonical reference, but exact project commands remain delegated to repository configuration;
- generic skill validation proves the guidance is packaged/reachable, not that every harness has each external tool installed.

`PORTABILITY.md` should receive only a concise clarification, if needed, that external development tools described by Protocol 5.11 are optional environment capabilities and are not part of generic skill validity or the direct-directory installation contract.

### 8. Versioning

Target version is **5.11.0**.

This is a backward-compatible minor capability/methodology strengthening under existing version semantics. It adds optional tool-assisted engineering methods while preserving Protocol 5.10 doctrine, lifecycle, routing, packaging, authority, handoff, and acceptance semantics.

Existing workplans remain bound to their declared protocol versions. Protocol 5.11 does not silently impose tool-use requirements on work governed by Protocol 5.10 or earlier.

## Implementation obligations

### O1 — Add the canonical tool-assisted engineering reference

- **Concern / rationale:** tool-specific method should be precise and reusable without bloating lifecycle entrypoints or scattering guidance across generic doctrine owners.
- **Required end state:** add `source/shared/references/tool-assisted-engineering.md` containing the capability-aware selection rule and the Serena/Semgrep/Hypothesis methods and safeguards frozen above.
- **Required consequences / constraints:** tool guidance must be optional, evidence-oriented, authority-safe, portability-safe, resource-aware, and explicitly subordinate to existing repository-intake/testing/workflow/security doctrine. It must not invent a new lifecycle stage or persistent evidence system.
- **Acceptance evidence:** focused contract tests assert the three tool sections, optionality/fallback semantics, tool-state authority boundaries, and no-substitution rules.

### O2 — Route Software Design to the new reference when materially relevant

- **Concern / rationale:** Design can benefit from Serena navigation and Semgrep independent/static analysis, and must be able to design Hypothesis-based acceptance where properties are the right instrument.
- **Required end state:** `source/roles/software-design/SKILL.md` adds one domain-conditional direct Markdown route to `references/tool-assisted-engineering.md` for material semantic repository navigation, static/structural analysis, or property/stateful-test design.
- **Required consequences / constraints:** preserve all existing role-critical routes and non-tool Design doctrine unchanged in meaning; do not make the new route role-critical for unrelated tasks.
- **Acceptance evidence:** route/link/package tests plus semantic regression that existing Design hierarchy, workplan, review, proxy-proof, snapshot-complete, and effective-compression invariants remain present.

### O3 — Route Software Implementation to the new reference when materially relevant

- **Concern / rationale:** Implementation is the primary consumer of symbol-aware editing, static checks, and property-based tests.
- **Required end state:** `source/roles/software-implementation/SKILL.md` adds the corresponding domain-conditional direct Markdown route.
- **Required consequences / constraints:** existing implementation authority, owning-layer fix, stage closure, final acceptance, testing, and resource rules remain unchanged; tool output must not shortcut them.
- **Acceptance evidence:** route/link/package tests plus unchanged implementation contract regressions.

### O4 — Package the new reference in both lifecycle role bundles only

- **Concern / rationale:** Protocol 5.9 requires directly routed references to be self-contained in generated skill bundles.
- **Required end state:** update `source/build_skills.py` so `tool-assisted-engineering.md` is included in `software-design` and `software-implementation` packages.
- **Required consequences / constraints:** do not add it to specialists unless their entrypoints actually route to it; do not make external tools package dependencies; preserve generic Agent Skill/OpenAI-adapter separation.
- **Acceptance evidence:** generated directory/ZIP packages contain the new reference for both lifecycle roles, validation succeeds, and no packaged-unlinked-reference failure appears.

### O5 — Protect Serena against hidden-authority and false-completeness misuse

- **Concern / rationale:** Serena's strongest features—semantic references and persistent memories—can improve context efficiency but can also tempt agents to over-trust LSP completeness or use memory as hidden task state.
- **Required end state:** canonical guidance explicitly requires fallback/cross-checking for plausible non-LSP surfaces and classifies memories/indexes as derived context, not normative task authority.
- **Required consequences / constraints:** no mandatory memory writing, onboarding artifact, `.serena` commit policy, or Serena-specific repository configuration is introduced by the protocol.
- **Acceptance evidence:** focused text-contract tests and independent source review confirm the required caveats are present and Protocol 5.10 snapshot-complete semantics are not weakened.

### O6 — Protect Semgrep against scanner-as-authority and volatile-gate misuse

- **Concern / rationale:** Semgrep can provide high-signal structural evidence, but broad rulesets, false positives/negatives, unsupported semantics, and autofix can create counterfeit confidence if treated as product truth.
- **Required end state:** canonical guidance distinguishes exploratory scanning from acceptance-critical reproducible rules, requires contextual triage, bounds negative claims to actual rule coverage, and treats autofix as ordinary untrusted implementation output until validated.
- **Required consequences / constraints:** no mandatory `--config=auto`, cloud account, managed scanning, ruleset subscription, CI gate, or autofix behavior is introduced.
- **Acceptance evidence:** focused contract tests protect these boundaries; existing runtime/proxy-proof acceptance doctrine remains unchanged.

### O7 — Integrate Hypothesis without weakening regression or oracle quality

- **Concern / rationale:** property-based testing can materially improve edge-case coverage but can also encode implementation bugs, become resource-unbounded, or rely on ephemeral example databases.
- **Required end state:** canonical guidance defines high-value property/stateful-test cases, independent-property/oracle expectations, resource bounds, durable counterexample handling, and real-owner stateful acceptance boundaries.
- **Required consequences / constraints:** Hypothesis remains a technique within existing focused/affected/integration testing, not a new mandatory suite category or replacement for explicit bug regressions.
- **Acceptance evidence:** focused contract tests assert property-oracle integrity, bounded execution, example-database non-authority, and non-substitution of integration/regression.

### O8 — Add Protocol 5.11 release/portability wording with preservation freeze

- **Concern / rationale:** release identity must accurately describe a methodology/capability strengthening without implying a doctrinal or lifecycle change.
- **Required end state:** update `source/PROTOCOL_VERSION`, `source/shared/references/protocol-versioning-and-compatibility.md`, `source/README.md`, root `README.md`, and generated package metadata to 5.11.0; add only the minimum portability clarification needed in `PORTABILITY.md`.
- **Required consequences / constraints:** version/connective wording only outside the new tool reference and role routes. Protocol 5.4-5.10 doctrine remains preservation territory.
- **Acceptance evidence:** version tests assert 5.11.0, backward-compatible tool-assisted methodology wording, unchanged two-role lifecycle, unchanged exact hierarchy string, and preserved prior-version descriptions.

### O9 — Add narrow Protocol 5.11 semantic regressions

- **Concern / rationale:** the release needs executable protection against both missing tool integration and accidental tool-driven doctrine drift.
- **Required end state:** add a focused test module, suggested `tests/test_protocol_511_tool_assistance.py`, plus minimal updates to existing version/contract tests.
- **Required consequences / constraints:** tests should protect semantic invariants rather than overfit prose formatting. At minimum verify:
  - both lifecycle role entrypoints directly link the new reference;
  - both generated lifecycle role packages contain it;
  - the reference covers Serena, Semgrep, and Hypothesis;
  - optional capability/fallback behavior is explicit;
  - Serena memory/index state is non-authoritative;
  - Semgrep findings/absence/autofix cannot substitute for governed acceptance;
  - Hypothesis database/generated cases do not replace durable regression/integration and properties require independent contract grounding;
  - existing hierarchy/lifecycle/proxy-proof/snapshot-complete/stage/final-acceptance regressions remain green.
- **Acceptance evidence:** focused new module passes, then the complete repository unittest suite passes without weakening existing assertions or fixtures.

### O10 — Regenerate and validate distributions from canonical source

- **Concern / rationale:** `source/` is authoritative and `dist/` is generated; Protocol 5.9 requires package parity.
- **Required end state:** regenerate committed `dist/skills/*`, ZIP bundles, `BUILD_INDEX.json`, protocol manifests, and other generated versioned outputs from canonical source.
- **Required consequences / constraints:** do not hand-edit `dist/`; generated runtime forms must remain semantically identical to source and to one another.
- **Acceptance evidence:** repository-required build/package validation and committed-dist parity checks all pass.

## Implementation authority

### Frozen

- Target protocol version is `5.11.0`.
- Protocol 5.11 is a backward-compatible **tool-assisted engineering methodology/capability upgrade only**.
- The exact governing hierarchy, lifecycle, role responsibilities, accepted-workplan authority, stage semantics, testing/acceptance semantics, proxy-proof boundaries, stewardship rules, routing/distribution architecture, and snapshot-complete handoff semantics are unchanged.
- Serena, Semgrep, and Hypothesis are optional environment capabilities, not generic skill dependencies or mandatory task gates.
- Tool output is evidence/assistance, not normative authority or product truth.
- Serena memory/index state cannot become sole normative task storage.
- Semgrep cannot substitute for executable acceptance and its negative claims are bounded by selected rule/model coverage.
- Hypothesis cannot substitute for explicit durable regression/integration and properties must be grounded in independent governed invariants/oracles.
- One canonical shared tool-assisted reference plus compact conditional routes is the accepted ownership design.
- No new lifecycle role, specialist, mandatory persistent ledger, harness-specific generic metadata dependency, or separate tool qualification gate is introduced.

### Delegated

- Exact heading names and local wording inside `tool-assisted-engineering.md` provided the frozen semantics remain recoverable.
- Exact placement/order of the new domain-conditional route within each lifecycle entrypoint.
- Whether the new shared reference is added to a small named list constant or directly to each lifecycle role's `references` list in `build_skills.py`.
- Exact focused test organization and helper functions.
- Exact concise release wording in root/source README and portability documentation.
- Tool-specific example commands, if included, provided they are clearly illustrative/non-authoritative and do not create hidden prerequisites.

### Reopen only on evidence

Reopen only the affected design surface if implementation proves one of these assumptions false:

- the package validator cannot support a new directly linked shared reference without a material redesign of Protocol 5.9 packaging;
- a lifecycle entrypoint cannot route to the tool reference without violating Agent Skill portability or existing direct-route validation;
- Serena/Semgrep/Hypothesis capabilities materially differ from the frozen method in a way that would make the prescribed use unsafe or misleading;
- generic skill metadata must declare external tool dependencies for a target portability claim that the repository is required to support;
- a proposed acceptance regression can pass while the tool guidance is absent or materially contradicted, requiring a stronger but still bounded validation mechanism.

Tool unavailability on one harness is not by itself a doctrine-redesign trigger; first preserve generic optionality and adapt only the affected harness/tool integration surface.

## Affected surface and task-specific acceptance

Initially expected source/behavioral surface:

- `source/roles/software-design/SKILL.md`;
- `source/roles/software-implementation/SKILL.md`;
- new `source/shared/references/tool-assisted-engineering.md`;
- `source/build_skills.py` package reference registry;
- `source/shared/references/protocol-versioning-and-compatibility.md`;
- `source/PROTOCOL_VERSION`;
- `source/README.md` and root `README.md`;
- narrowly `PORTABILITY.md`;
- new/focused protocol contract tests and minimal version assertion updates;
- generated `dist/` lifecycle bundles, ZIPs, build index, and protocol manifests.

Preservation-only unless direct evidence requires a minimal connective edit:

- `workflow-and-workplans.md`;
- `testing-and-validation.md`;
- `architecture-and-design.md`;
- `repository-intake.md`;
- security/configuration/domain references;
- specialist `SKILL.md` files;
- implementation workplan template;
- routing sentinel qualification assets;
- package validator semantics beyond recognizing the newly packaged direct reference.

The implementation must re-derive the final affected surface from the assembled diff. Any substantive change outside the tool-method, routing, packaging, test, release/version, or portability surfaces above requires explicit justification; any doctrine change routes back to Design.

Task-specific acceptance requires all of the following on the same assembled candidate:

1. Focused Protocol 5.11 contract tests pass.
2. Entire existing `python -m unittest discover -s tests -v` suite passes without weakened assertions/fixtures.
3. `python source/build_skills.py --output /tmp/protocol-dist` succeeds.
4. `python source/validate_packages.py --dist /tmp/protocol-dist` succeeds.
5. `python source/check_dist.py --expected /tmp/protocol-dist --committed dist` succeeds.
6. `git diff --check` succeeds.
7. Structural review confirms both lifecycle entrypoints directly route to the packaged reference and no specialist/package receives an unlinked copy.
8. Doctrine-preservation review compares the assembled non-tool normative text against base commit `36ea966dc87d4feeee80abac2e24f79efe8f5999`; no unrelated semantic rewrite is allowed.
9. The exact hierarchy string remains directly present in both lifecycle entrypoints.
10. Existing tests protecting Protocol 5.4-5.10 stewardship, effective compression, portability/routing, proxy-proof acceptance, workplan authority, stage-local/final acceptance, and snapshot completeness remain green.

A live harness smoke using the user's configured Serena/Semgrep/Hypothesis environment may be useful as post-implementation confidence, but it is **not a generic Protocol 5.11 release gate** and must not be represented as cross-harness qualification. If a release or README makes a specific harness/tool-execution claim, qualify that claim on the named harness separately.

Production qualification: **unnecessary**. This release changes skill methodology/routing/package content, not a production workload, hardware path, performance envelope, or runtime service.

## Implementation sequence and redesign risks

### Stage 1 — Canonical method, lifecycle routing, package reachability, and focused tests

Implement O1-O7 and the focused portion of O9 together as one coherent behavior/risk stage:

- add the canonical reference;
- add conditional routes to both lifecycle entrypoints;
- package the reference for those roles;
- add focused tests for tool semantics, optionality, authority boundaries, and package reachability.

Before Stage 2, close semantic/conformance and functional acceptance for this stage with focused new tests plus the existing routing/effective-compression/tooling regressions that can be affected by new reference packaging.

### Stage 2 — Release identity, portability wording, full regression, and generated distribution

Implement O8, remaining version-test updates, and O10. Then perform final accepted-contract reconciliation, re-derive the affected surface, run the full repository acceptance workflow, and conduct the independent doctrine-preservation diff review.

Material redesign risks:

- **Entrypoint bloat:** if tool detail begins migrating into `SKILL.md`, move it back to the canonical reference rather than expanding role-local prose.
- **Tool authority drift:** if implementation wording implies that Serena/Semgrep/Hypothesis outputs are authoritative, blocking, or complete by default, correct the wording under the frozen design; do not reinterpret existing doctrine.
- **Portability regression:** if package or frontmatter changes make skills depend on tool-specific environment configuration, revert to optional runtime capability detection and keep generic packaging self-contained.
- **Testing ceremony:** if implementation adds mandatory tool runs to every task or protocol CI solely because the tools exist, remove them unless an independent engineering/project requirement justifies that gate.
- **Persistent-state drift:** if Serena memories or Hypothesis databases become necessary to reconstruct current requirements/tests, move the durable semantics into current governed artifacts and treat tool state only as cache.
- **False negative confidence:** if guidance presents Serena references or Semgrep zero-findings as complete affected-surface proof, add the required model-boundary caveat and complementary-evidence rule.

## Handoff closure

The accepted implementation handoff is:

```text
user requirement:
  integrate Serena + Semgrep + Hypothesis into the skills
  as a methodological capability upgrade only
  while preserving all prior doctrine/improvements

+ current Protocol 5.10 preserved authority
+ one canonical optional tool-method reference
+ direct conditional routing from both lifecycle roles
+ package reachability under Protocol 5.9
+ explicit tool evidence/authority/portability safeguards
+ Protocol 5.11 backward-compatible version identity

-> O1-O10 implementation obligations
-> focused semantic/package regressions
-> full existing protocol regression
-> generated distribution parity
-> independent doctrine-preservation review
```

No material task-specific requirement is intentionally delegated to Git history, this conversation, or external tool documentation. External Serena/Semgrep/Hypothesis documentation may be used during implementation as non-normative capability reference, but the required protocol semantics are fully stated in this workplan.

Apply the Protocol 5.10 snapshot-loss counterfactual: with `.git`, prior chat/review context, and external tool links removed, this workplan plus the current supplied repository still contains the protected concerns, frozen design, implementation obligations, acceptance boundaries, and redesign triggers needed for implementation.
