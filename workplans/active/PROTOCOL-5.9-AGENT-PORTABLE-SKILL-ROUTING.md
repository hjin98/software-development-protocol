---
kind: implementation-workplan
workplan_id: PROTOCOL-5.9-AGENT-PORTABLE-SKILL-ROUTING
protocol_version: 5.8.0
target_protocol_version: 5.9.0
status: active
created_date: 2026-08-29
base_commit: 483532e9c8801d2ec35398b629df8a18c15a4224
---

# Protocol 5.9 Agent-Portable Skill Routing Workplan

## Objective and protected concerns

Make the Software Development Protocol reliably portable across Agent-Skills-style coding agents and harnesses, including Codex/OpenAI, Claude Code, Pi, Gemini CLI/Antigravity, GitHub Copilot, and DeepSeek Harness, without weakening Protocol 5.8 progressive disclosure or regrowing the always-loaded control plane.

The diagnosed defect is not that bundled references are absent. The current packages contain the references, but the lifecycle entrypoints rely on a model to infer that a material concern has entered a reference's ownership domain, map that concern to a filename, and voluntarily read the file. Some harnesses expose only the activated `SKILL.md` plus resource availability and leave subsequent reference reads to the model. A competent model can therefore run a superficially compliant but materially incomplete "Protocol-lite" path that never loads the canonical workflow/testing/architecture doctrine.

Durable success is:

```text
portable Agent Skill discovery/activation
+ deterministic, explicit reference-routing triggers
+ self-contained direct-root skill bundles
+ progressive disclosure without indiscriminate eager loading
+ static route/package conformance
+ separately qualified real-harness routing behavior
= materially equivalent protocol semantics across supported agents
```

Protected concerns:

1. **No hidden-reference failure.** A task that materially depends on canonical detailed doctrine must have an explicit, high-salience route from `SKILL.md` to that exact bundled file.
2. **No model-initiative dependency for role-critical doctrine.** Workplan/handoff/review/stage/acceptance flows must not depend on a model independently deciding that an unlabeled or generically described reference should be opened.
3. **No progressive-disclosure rollback.** Do not solve routing unreliability by copying all detailed references back into every `SKILL.md` or loading every reference for every task.
4. **No vendor-core inversion.** OpenAI-, Claude-, Gemini-, Pi-, Copilot-, or DeepSeek-specific metadata/integration may exist as adapters but must not define generic Agent Skill validity.
5. **No archive-only portability.** A ZIP may remain a transport artifact, but there must be a first-class self-contained directory representation that matches the native runtime shape expected by skill loaders.
6. **No false portability claim.** Static file presence is not evidence that a real harness activates the skill, reads the required reference, and applies the referenced rule.
7. **No flaky external CI gate.** Live agent/model qualification is valuable compatibility evidence but must not become an unbounded, credential-dependent, stochastic blocker for every ordinary repository CI run.
8. **Preserve Protocol 5.8 economy.** Context and tool cost should increase only where deterministic routing protects a material protocol behavior.

## Engineering envelope and product design

### Portable core contract

The canonical external skill substrate remains the open Agent Skills shape:

```text
<skill-root>/<skill-name>/
  SKILL.md
  references/...
  templates/...
  scripts/...       # when applicable
  assets/...        # when applicable
  agents/...        # optional vendor adapters
```

`SKILL.md` frontmatter remains minimal and portable (`name`, `description`, plus only standard-compatible additions when independently justified). The skill directory name and frontmatter name must obey the strict shared standard rather than relying on a lenient harness.

Every shipped skill bundle must be self-contained. Relative routes from `SKILL.md` must resolve inside the bundle without depending on the canonical repository's `source/shared/...` layout.

Keep each skill as a direct child of the exported skill root. Do not rely on recursive discovery beyond `<skills-root>/<skill-name>/SKILL.md`; this is the strict common topology and also makes the bundle easy to copy or symlink into harness-specific roots.

### Deterministic reference-routing contract

Each lifecycle/specialist `SKILL.md` must contain a concise, high-salience routing section near the beginning, before substantive role instructions can be acted on.

The routing section must:

- directly name and Markdown-link every bundled `references/*.md` file that the skill may use;
- state a concrete trigger describing when that reference must or may be read;
- use normative `MUST read ... before ...` language for role-critical triggers where omission can materially change protocol behavior;
- preserve conditional/on-demand loading for domain references whose relevance is genuinely task-dependent;
- refer to the exact relative path rather than an abstract domain label that the model must translate into a filename;
- keep references one level below the skill entrypoint and directly discoverable from `SKILL.md`.

Two routing classes are frozen:

1. **Role-critical deterministic routes.** When the trigger is true, reading the linked reference is a required precondition to the corresponding substantive decision/closure.
2. **Domain-conditional routes.** The reference remains on-demand, but the trigger must still explicitly map the material domain to an exact linked file.

For `software-design`, at minimum:

- workplan creation/amendment, Design -> Implementation handoff, implementation review/Pass-No-Pass, stage/gate reasoning, rework/redesign routing -> **MUST read** `references/workflow-and-workplans.md`;
- acceptance design or review of testing/regression/integration/evidence/proxy-proof/qualification claims -> **MUST read** `references/testing-and-validation.md`;
- nontrivial architecture/ownership/algorithm/complexity/redesign decisions or independent engineering challenge -> **MUST read** `references/architecture-and-design.md`;
- protocol/workplan version binding, compatibility, or release-version decisions -> **MUST read** `references/protocol-versioning-and-compatibility.md`;
- broad repository-intake/context-economy questions -> explicitly route to `references/repository-intake.md` when that surface is material.

For `software-implementation`, at minimum:

- implementation governed by an accepted workplan, material stage closure, local reconciliation, or redesign routing -> **MUST read** `references/workflow-and-workplans.md`;
- executable stage/final acceptance, regression/integration, evidence reuse, semantic-owner/test-double, or qualification reasoning -> **MUST read** `references/testing-and-validation.md` before claiming the relevant closure;
- material ownership/refactor/architecture/redesign questions -> explicitly route to `references/architecture-and-design.md`;
- version binding/compatibility questions -> explicitly route to `references/protocol-versioning-and-compatibility.md`;
- repository-intake/context-economy questions -> explicitly route to `references/repository-intake.md` when material.

Specialist skills receive the same explicit-route treatment for every packaged reference, but must not be forced to load unrelated references merely because they are bundled.

Anti-shortcut: a route is not considered deterministic merely because a filename appears somewhere in `SKILL.md`. The trigger and required timing must be sufficiently explicit that a model does not need to reconstruct protocol ownership semantics before deciding whether to read it.

### Distribution architecture

`source/` remains canonical and generated outputs remain non-authoritative.

Extend the build so a fresh distribution contains a first-class unpacked tree:

```text
dist/
  BUILD_INDEX.json
  skills/
    software-design/...
    software-implementation/...
    software-documentation/...
    repository-hygiene/...
  software-design.zip
  software-implementation.zip
  software-documentation.zip
  repository-hygiene.zip
```

The unpacked `dist/skills/<skill-name>/` tree is the semantic runtime-install representation. Existing top-level ZIP names remain for backward compatibility and are derived from the same generated bundle tree; do not create separate package-generation logic for directory versus ZIP output.

`agents/openai.yaml` may continue to ship as an OpenAI adapter. Generic Agent Skill conformance must not be defined in terms of this file. Repository support for OpenAI may separately require and validate the adapter as an OpenAI-specific contract.

### Validation and qualification architecture

Static repository CI owns deterministic, reproducible claims:

- strict Agent Skills-compatible frontmatter/name/layout validation;
- direct-root self-contained bundle structure;
- every packaged reference directly linked from its owning `SKILL.md`;
- all linked reference/template routes resolve inside the package;
- required role-critical routing paths remain present and explicit;
- generic core validation is separated from vendor-adapter validation;
- unpacked bundle contents and ZIP contents are semantically identical;
- committed generated distribution matches a fresh canonical build recursively;
- existing protocol semantic/failure-mode tests remain green.

Live harness qualification owns external compatibility claims. Provide a bounded, reproducible qualification procedure/fixture that can establish separately:

```text
skill discovered
-> skill activated/read
-> required reference route selected
-> exact reference actually read when tool trace is observable
-> rule that exists only in that reference correctly affects the result
```

Qualification must distinguish skill activation failure from reference-routing failure. Use a synthetic sentinel rule located only in the reference so `SKILL.md`-only execution cannot accidentally pass. When a harness exposes file/tool trajectories, actual reference access is the preferred evidence. When it does not, final behavioral evidence may be reported with lower confidence rather than falsely claiming an observed read.

The initial compatibility matrix should cover, when accessible: Codex/OpenAI, Claude Code, Pi, Gemini CLI/Antigravity, GitHub Copilot, and DeepSeek Harness. Direct-directory installation is the baseline. Symlink/shared-directory installation may be qualified and documented per harness where supported, but unsupported symlink semantics must not invalidate the generic skill format.

Live qualification is not part of ordinary deterministic CI unless a future environment provides stable credentials, fixed harness/model versions, bounded cost, and sufficiently deterministic execution to justify promotion.

### Versioning

Target Protocol version is **5.9.0**. The change preserves Protocol 5 doctrine and the two-role lifecycle but strengthens the backward-compatible control plane and portability contract; under current versioning rules this is a minor release, not a patch-only wording correction.

## Implementation obligations

### O1 - Make reference routing explicit and deterministic

- **Concern / rationale:** current progressive disclosure can fail silently when an agent activates `SKILL.md` but does not voluntarily inspect canonical references.
- **Required end state:** every packaged reference is directly linked from its owning `SKILL.md` with an explicit trigger; role-critical routes use mandatory timing language.
- **Required consequences / constraints:** place the routing section early; preserve concise entrypoints; do not duplicate detailed reference contents; do not make all references unconditional.
- **Acceptance evidence:** structural tests enumerate packaged references and confirm direct resolvable links; targeted contract tests assert the frozen role-critical routes; source review confirms trigger/timing semantics are not generic filename mentions.

### O2 - Preserve progressive disclosure while lowering routing freedom where failure is costly

- **Concern / rationale:** reliability must improve without recreating Protocol 5.7 context bloat.
- **Required end state:** workflow/testing/architecture/version references are mandatory only under the frozen material triggers; specialist/domain references remain conditional.
- **Required consequences / constraints:** do not require every core reference for trivial/local tasks; do not move canonical detailed doctrine back into lifecycle entrypoints merely to avoid file reads.
- **Acceptance evidence:** entrypoint size/duplication tests continue to protect effective compression; review demonstrates no material Protocol 5.8 doctrine loss and no indiscriminate eager-loading rule.

### O3 - Separate generic Agent Skill validity from vendor adapters

- **Concern / rationale:** `agents/openai.yaml` is currently treated as a required package member by the generic validator, making the package contract OpenAI-shaped.
- **Required end state:** generic portability validation covers the Agent Skill core independently; OpenAI adapter validation is explicitly scoped as an adapter/repository support check.
- **Required consequences / constraints:** OpenAI support must not regress; optional extra adapter files must remain harmless to non-OpenAI harnesses.
- **Acceptance evidence:** tests can validate generic package structure without using OpenAI metadata as a generic invariant, while separate tests still detect a broken/missing OpenAI adapter when validating the repository's supported OpenAI integration.

### O4 - Add a first-class unpacked runtime distribution

- **Concern / rationale:** current committed distribution is ZIP-only, while coding harnesses consume directories and relative bundled resources.
- **Required end state:** fresh/committed distribution exposes `dist/skills/<skill-name>/...` self-contained direct-root bundles and backward-compatible ZIPs derived from the same tree.
- **Required consequences / constraints:** `source/` remains canonical; generated directory and archive contents cannot drift; existing top-level ZIP consumers remain supported.
- **Acceptance evidence:** build tests compare unpacked and ZIP member trees byte-for-byte/semantically; recursive dist parity detects missing/extra/modified generated files; installation smoke checks resolve all routed files inside an unpacked skill directory.

### O5 - Bring package validation up to the portable common standard

- **Concern / rationale:** the current hand-written validator both over-constrains frontmatter to exactly `name`/`description` and under-enforces parts of the stricter shared naming/schema rules.
- **Required end state:** accepted standard-compatible frontmatter/layout is validated without relying on lenient harness behavior.
- **Required consequences / constraints:** preserve strict name-directory consistency and safe paths; allow independently justified standard-compatible optional fields; avoid silently accepting malformed names because one harness is permissive.
- **Suggested realization:** use a real YAML parser and either encode the Agent Skills constraints locally or add a pinned official validator cross-check if its dependency/availability is robust enough. The implementation mechanism is delegated.
- **Acceptance evidence:** positive/negative fixtures cover valid optional metadata, invalid naming/layout/frontmatter, unsafe routes, and missing resources.

### O6 - Add route-level static acceptance rather than presence-only acceptance

- **Concern / rationale:** current tests can stay green while an agent never reads a reference.
- **Required end state:** CI distinguishes "reference packaged" from "reference deterministically routed from entrypoint".
- **Required consequences / constraints:** do not create brittle prose snapshots for every sentence; test semantic routing invariants and path closure.
- **Acceptance evidence:** a fixture with an unlinked packaged reference fails; a broken link fails; omission of a frozen role-critical route fails; unrelated wording changes remain possible.

### O7 - Add bounded real-harness portability qualification

- **Concern / rationale:** static validation cannot prove activation/read/application behavior.
- **Required end state:** repository documentation or tooling defines a repeatable portability scenario and compatibility matrix for the supported harnesses.
- **Required consequences / constraints:** sentinel rule must live only in a reference; record harness/version/model/install mode and whether actual read trajectory was observable; do not require expensive software-development tasks to qualify routing.
- **Acceptance boundary:** the real harness skill activation/resource-loading path is the semantic owner. A local parser or simulated loader cannot close a claim that Gemini/Pi/Claude/Copilot/DeepSeek/Codex actually routes the reference.
- **Acceptance evidence:** bounded real runs per claimed harness when available; unavailable harnesses remain explicitly unqualified rather than proxy-passed.

### O8 - Document installation and compatibility without making vendor paths protocol doctrine

- **Concern / rationale:** users need reliable installation, but harness-specific roots evolve.
- **Required end state:** README/distribution docs explain the generic exported bundle and give current harness-specific copy/symlink/install examples, including the strict direct-child topology.
- **Required consequences / constraints:** vendor paths are documentation/adapters, not canonical protocol semantics; prefer a shared `.agents/skills` root where a harness officially supports it, with harness-specific roots where required.
- **Acceptance evidence:** documentation is consistent with the generated tree and currently supported harness behavior; no instruction points users at canonical `source/roles/...` as if those directories were self-contained runtime bundles.

### O9 - Release Protocol 5.9 coherently

- **Concern / rationale:** version text, manifests, generated packages, README, and compatibility claims must describe one assembled protocol release.
- **Required end state:** bump to `5.9.0` only when the implementation and deterministic acceptance are complete; update version history with the portable deterministic-routing refinement; regenerate all distributions.
- **Acceptance evidence:** repository-required tests/build/validation/parity/whitespace checks pass on the final candidate; generated manifests/indexes report 5.9.0; final source inspection finds no stale 5.8-only portability description that contradicts the new contract.

## Implementation authority

### Frozen

- Preserve the Protocol 5 two-role lifecycle and all material Protocol 5.8 engineering/effective-compression guarantees.
- Agent Skills-style `SKILL.md` + relative bundled resources remains the portable core format.
- Every packaged reference is directly linked from its owning `SKILL.md` with an explicit trigger.
- Role-critical routes use deterministic mandatory-read semantics under the frozen triggers; domain references remain on-demand.
- Do not restore all detailed doctrine to `SKILL.md` and do not force all references to load on every invocation.
- Exported skill bundles are self-contained direct children of the skill root.
- A first-class unpacked distribution is generated; existing top-level ZIP artifacts remain backward compatible and derive from the same bundle tree.
- Generic package validity is not defined by `agents/openai.yaml`; OpenAI metadata remains a separately validated supported adapter.
- Static CI and live real-harness portability qualification are separate evidence classes.
- Real-harness claims cannot be closed by a simulated loader/parser.
- Target release is Protocol 5.9.0.

### Delegated

- Exact wording/format of routing tables, provided the frozen trigger/path/timing semantics remain explicit and high-salience.
- Exact YAML/schema validation library and whether an official external validator is a pinned supplemental check.
- Internal builder refactor needed to generate one bundle tree and derive both unpacked and ZIP outputs.
- Exact fixture/tooling format for the bounded portability qualification and compatibility report.
- Exact documentation layout and harness-specific installation command syntax, subject to current official behavior.

### Reopen only on evidence

Reopen the affected design surface only if implementation or representative harness qualification shows that:

- a supported harness cannot access directly linked one-level relative references from an activated skill;
- an agent requires a materially different bundle format that cannot coexist as an optional adapter;
- deterministic mandatory routing causes material context/tool-cost regression on ordinary tasks that cannot be solved by better trigger granularity;
- committing the unpacked generated tree creates unacceptable repository/distribution cost or platform incompatibility, in which case preserve the first-class directory export capability and redesign only its committed-storage policy;
- a stable live qualification environment becomes deterministic/cheap enough that promotion into CI is materially better than separate release qualification.

Do not reopen Protocol 5 doctrine, the two-role lifecycle, or unrelated engineering semantics because one harness has a packaging/discovery quirk.

## Affected surface and task-specific acceptance

Initially expected affected surfaces:

- `source/roles/*/SKILL.md`;
- `source/specialists/*/SKILL.md`;
- `source/build_skills.py`;
- `source/validate_packages.py`;
- `source/check_dist.py`;
- `source/shared/references/protocol-versioning-and-compatibility.md`;
- root/source README and installation/compatibility documentation;
- protocol tooling/contract/effective-compression tests and new portability fixtures/tests;
- `.github/workflows/protocol-check.yml` only as needed for deterministic static checks;
- generated `dist/` tree, ZIPs, manifests, and build index.

Implementation must re-derive the affected surface from the assembled candidate. In particular, changes to builder output shape may affect `BUILD_INDEX.json`, tests that assume `dist/` contains files only, ZIP parity logic, release/documentation paths, and any tooling that enumerates generated artifacts.

Task-specific final acceptance requires:

1. all four shipped skills pass strict generic core validation;
2. every packaged reference has a direct, resolvable `SKILL.md` route with an explicit trigger;
3. all frozen role-critical routes remain mandatory under their specified task conditions;
4. a negative fixture proves that merely packaging an unlinked reference is insufficient;
5. unpacked bundles and ZIPs are generated from one semantic source tree and remain equivalent;
6. generic validation and OpenAI-adapter validation are independently testable;
7. Protocol 5.8 effective-compression/failure-mode regression tests remain green;
8. the standard repository acceptance workflow passes on the final candidate;
9. the live compatibility procedure is documented and at least the harnesses actually available to the implementer are run and reported without proxy-passing unavailable harnesses.

Production qualification: **unnecessary**. This is a control-plane/package compatibility change; bounded real-harness routing qualification is the relevant external evidence.

## Implementation sequence and redesign risks

### P1 - Portable package substrate and validators

Refactor package generation around one self-contained bundle tree; add unpacked `dist/skills` output; preserve existing ZIPs; separate generic Agent Skill validation from OpenAI-adapter validation; upgrade recursive dist parity and standard-compatible frontmatter/path validation.

Close P1 with builder/validator/parity focused tests plus the affected existing tooling suite before routing semantics depend on the new package structure.

### P2 - Deterministic entrypoint routing

Add high-salience explicit reference routing to lifecycle and specialist entrypoints, direct links for every bundled reference, and frozen mandatory routes for role-critical workflow/testing/architecture/version triggers. Add route-level negative/positive acceptance while preserving effective-compression constraints.

Close P2 with semantic review of all route triggers, route/package tests, existing protocol contract/failure-mode/effective-compression regression, and rebuilt package validation.

### P3 - Compatibility qualification, documentation, and 5.9 release closure

Add the bounded sentinel routing qualification procedure/fixture and compatibility matrix; update installation guidance; update versioning/release text; run available real harness qualifications; bump/regenerate Protocol 5.9.0 only after deterministic acceptance is green; then run the complete repository acceptance workflow and final affected-surface re-derivation.

Material redesign risks are limited to the explicit reopen conditions above. Harness-specific failures should first be classified as discovery, activation, resource access/path-canonicalization, route selection, or model-compliance failures before changing the generic skill architecture.

## Handoff closure

The plan preserves the full chain:

```text
observed cross-agent behavior gap
+ evidence that several harnesses load SKILL.md/resources progressively
+ Protocol 5.8 hidden-reference risk
+ need for cross-agent file/discovery portability
-> deterministic direct reference routes
-> self-contained direct-root runtime bundles
-> generic-core/vendor-adapter separation
-> static routing/package acceptance
-> real-harness activation/read/application qualification
```

No material requirement is delegated back to implementation as an architectural decision: the portable core, routing classes, mandatory role-critical triggers, distribution semantics, adapter boundary, static-versus-live evidence boundary, and target version are frozen. Implementation retains discretion only over local mechanics and wording that preserve those outcomes.