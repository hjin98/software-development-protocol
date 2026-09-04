# Agent portability and routing qualification

Protocol 5.9 established the portable skill-routing/distribution contract. Protocol 5.13 preserved that contract while making optional-tool routing deterministic per material relation. Protocol 5.15 preserves both contracts and adds deterministic language-profile routing for material Python/C++ executable work.

The runtime installation unit remains the self-contained directory under `dist/skills/<skill-name>/`; the top-level ZIP with the same skill name contains identical files under one enclosing skill directory.

## Installation contract

Install each skill as a direct child of a harness skill root so the entrypoint is exactly `<skills-root>/<skill-name>/SKILL.md`. Do not install `source/roles/...` or `source/specialists/...` directly: canonical source references become self-contained only in generated bundles.

Use a harness-supported shared `.agents/skills` root when available or the harness-native root when required. Harness-specific paths are integration guidance, not protocol doctrine; verify them against the harness version being qualified.

ZIPs are transport artifacts: extract the enclosing `<skill-name>/` directory before placing it under a runtime skill root. A symlinked/shared installation is a separate harness capability and must be qualified on that harness; the **direct-directory installation contract** is the portability baseline.

## Why deterministic routing exists

Skill activation proves only that a harness/model obtained `SKILL.md`. Protocol 5 therefore makes material progressive-disclosure triggers explicit.

Protocol 5.15 has two independent routing dimensions:

1. **Language/runtime routing:** material executable Python/C++ design, implementation, or review routes through `references/language-profiles.md` and then directly to `references/python-engineering.md`, `references/cpp-engineering.md`, or both for a mixed boundary.
2. **Engineering-relation/tool routing:** semantic, structural, property/generative, interprocedural, runtime-state, memory/UB, race, and performance questions route to the capability that directly models the relation.

Static validation proves that referenced files are packaged, directly linked, and structurally reachable. It cannot prove that a real harness/model follows the route or invokes an external capability, so live qualification remains a separate evidence class.

## Optional external development capabilities

Serena, Semgrep, Hypothesis, CodeQL, compiler-native analyzers, sanitizers, debuggers, profilers, fuzzers, and similar tools are **optional environment capabilities**. They are **not part of generic Agent Skill validity**, the **direct-directory installation contract**, or reference-routing package validity unless project/task authority explicitly requires one.

Generic bundles do not embed executable paths, credentials, analyzer databases, compiler/toolchain installations, hosted-service configuration, or project-specific query/rule settings. Language/backend/build/runtime support varies independently of skill packaging.

A claim that a particular harness actually exposes Serena, executes a Semgrep configuration, runs a Hypothesis profile, invokes CodeQL, follows a C++ sanitizer/debugger/profiler route, or follows a language-specific conditional route requires evidence for that **named harness/tool configuration**. Static package validation or reference-routing success does not establish those external-tool claims. Managed/cloud tooling that receives source, findings, SARIF, or credentials remains subject to project/user authorization and protocol security/trust rules.

## Bounded reference-routing qualification

Use `qualification/reference-routing/protocol-routing-sentinel/` as a tiny independent Agent Skill. The required answer token exists only in its bundled reference; `SKILL.md` deliberately does not contain the token.

For each harness/model/install mode being claimed:

1. install the sentinel as a direct child of the harness skill root;
2. start a fresh session;
3. ask: `Use protocol-routing-sentinel and return the routing sentinel.`;
4. verify that the answer equals the token in `references/sentinel.md`;
5. when a trajectory is exposed, verify an actual read of `references/sentinel.md` after skill activation;
6. classify failures separately as discovery, activation, resource-access/path-canonicalization, route-selection, or model-compliance failures.

A simulated parser/local loader cannot establish a real-harness claim. If read traces are unavailable, a correct token is behavioral evidence with lower confidence; report that limitation.

## Language-profile routing qualification

When claiming Protocol 5.15 live language routing for a harness/model, use a representative material executable prompt whose language/runtime surface is unambiguous.

Expected trace when observable:

```text
lifecycle SKILL.md
-> references/language-profiles.md
-> matching Python or C++ profile
-> shared domain references/tools only as triggered by the engineering question
```

For a mixed Python/C++ extension/binding prompt, both language profiles must be read and boundary reasoning must remain subordinate to shared product/scientific/security/performance doctrine. A purely generic documentation/architecture prompt should not be forced to load language profiles when language semantics are immaterial.

Static tests may establish the protocol-level route and package completeness; they do not establish universal model compliance.

## Bounded live tool-routing qualification

Reference reachability and tool selection are different claims. Use `qualification/tool-routing/SCENARIOS.md` when claiming real harness/model behavior.

For each **actually available** harness/model/tool combination being claimed:

1. install/build the current lifecycle skill bundle and start a fresh session;
2. ensure the specialized capability is genuinely exposed and record enough harness/model/tool identity to interpret the run;
3. use one representative question whose relation unambiguously triggers the target class;
4. when the harness exposes a trajectory, verify the direct tool-specific reference read before substantive reliance on lower-information defaults;
5. verify either the specialized capability invocation or a concrete permitted fallback such as unsupported backend/language, unavailable tool surface, stale/unreliable state that cannot economically be refreshed, model mismatch, disproportionate setup for a trivially bounded claim, or already-available equally reliable cheaper evidence;
6. do not count silent built-in search/read/shell/test preference as a valid fallback after a specialized trigger;
7. record only the combination actually exercised; **do not infer another harness/model/tool** from static tests or from a different combination.

The **minimum live regression**, when a trace-bearing Serena-enabled harness is available, remains the Serena initiating regression: a nontrivial symbol definition/semantic-owner plus callers/references question. Equivalent bounded scenarios exist for Semgrep structural variants, Hypothesis broad Python invariants, CodeQL cross-function flow, and Protocol 5.15 C++ compiler/sanitizer/debugger/performance capability classes.

Live qualification is useful evidence, not a generic CI dependency. If no suitable live harness/tool environment is available, Protocol 5.15 may claim deterministic **protocol-level routing semantics** from static/counterfactual/package tests, but it **must not claim empirical universal model compliance** or an unexecuted harness/tool pass.

## Compatibility matrix

Record actual qualification results in release/PR closeout when relevant. Do not infer a pass from static validation.

| Harness | Direct-directory/reference routing | Language-profile routing | Tool routing | Notes |
| --- | --- | --- | --- | --- |
| Codex/OpenAI | unqualified | unqualified | unqualified | Qualify the actual installed model/tool configuration. |
| Claude Code | unqualified | unqualified | unqualified | Run the Serena initiating regression when a trace-bearing Serena-enabled environment is available. |
| Pi | unqualified | unqualified | unqualified | Qualify only installed/exposed tools actually exercised. |
| Gemini CLI / Antigravity | unqualified | unqualified | unqualified | Qualify only installed/exposed tools actually exercised. |
| GitHub Copilot | unqualified | unqualified | unqualified | Qualify only installed/exposed tools actually exercised. |
| DeepSeek Harness | unqualified | unqualified | unqualified | Qualify only installed/exposed tools actually exercised. |

Ordinary repository CI intentionally does not call external agents. Live qualification may enter CI only if credentials, harness/model/tool versions, cost, and stochastic behavior become stable enough to make it a reliable release signal.
