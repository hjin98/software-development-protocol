# Agent portability and routing qualification

Protocol 5.9 established the portable skill-routing/distribution contract. Protocol 5.13 preserves that contract while adding deterministic per-question optional-tool routing and a distinct live tool-routing qualification procedure. The runtime installation unit remains the self-contained directory under `dist/skills/<skill-name>/`; the top-level ZIP with the same skill name contains identical files under one enclosing skill directory.

## Installation contract

Install each skill as a direct child of a harness skill root so the entrypoint is exactly `<skills-root>/<skill-name>/SKILL.md`. Do not install `source/roles/...` or `source/specialists/...` directly: canonical source references live under `source/shared/` and become self-contained only in generated bundles.

Use a harness-supported shared `.agents/skills` root when available, or the harness-native skill root when required. Current commonly supported locations include project `.agents/skills` for Pi, Gemini/Antigravity, GitHub Copilot, and DeepSeek Harness; Claude Code also supports `.claude/skills`, Copilot supports `.github/skills`, Pi supports `.pi/skills`, and DeepSeek Harness supports `.dsh/skills`. Harness-specific paths are integration guidance, not protocol doctrine; verify them against the harness version being qualified.

ZIPs are transport artifacts: extract the enclosing `<skill-name>/` directory before placing it under a runtime skill root. A symlinked/shared installation is a separate harness capability and must be qualified on that harness; the **direct-directory installation contract** is the portability baseline.

## Why deterministic routing exists

Skill activation proves only that the harness/model obtained `SKILL.md`. Protocol 5.9 therefore made role-critical routing explicit: a material task trigger names the exact linked reference and states when reading it is mandatory. Protocol 5.13 applies the same principle to specialized engineering questions: lifecycle entrypoints classify the relation under each material question and directly name the relevant Serena, Semgrep, Hypothesis, or CodeQL method.

Static validation proves that references are packaged, directly linked, and structurally reachable. It cannot prove that a real harness/model actually performs the follow-up read or invokes an external capability, so live qualification remains a separate evidence class.

## Optional external development capabilities

Protocol 5.13 describes Serena, Semgrep, Hypothesis, and CodeQL as **optional environment capabilities**. They are **not part of generic Agent Skill validity**, the **direct-directory installation contract**, or reference-routing package validity. A skill remains valid and usable when one or more are unavailable; the agent establishes the same engineering claim using available repository/search/analyzer/test mechanisms unless project/task authority explicitly requires a named tool.

Generic bundles do not embed Serena MCP declarations, executable/environment paths, credentials, Semgrep service configuration, Hypothesis installation state, CodeQL binaries/query packs/databases, or GitHub authentication/configuration. Serena backend capabilities, Semgrep editions/engines, project-specific Hypothesis settings, CodeQL language/build/query support, and GitHub code-scanning configuration vary independently of skill packaging.

A claim that a particular harness actually exposes Serena, executes a Semgrep configuration, runs a Hypothesis profile, invokes CodeQL, or follows a tool-specific conditional route requires evidence for that **named harness/tool configuration**. Static package validation or the reference-routing sentinel does not establish those external-tool claims. Managed/cloud tooling that receives source, findings, SARIF, or credentials remains subject to project/user authorization and protocol security/trust rules.

## Bounded reference-routing qualification

Use `qualification/reference-routing/protocol-routing-sentinel/` as a tiny independent Agent Skill. The required answer token exists only in its bundled reference; `SKILL.md` deliberately does not contain the token.

For each harness/model/install mode being claimed:

1. copy the sentinel skill directory as a direct child of that harness's skill root;
2. start a fresh session so skill discovery is not inherited from earlier context;
3. ask: `Use protocol-routing-sentinel and return the routing sentinel.`;
4. verify that the final answer equals the token in `references/sentinel.md`;
5. when the harness exposes a tool/file trajectory, verify an actual read of `references/sentinel.md` after skill activation;
6. classify failures separately as discovery, activation, resource-access/path-canonicalization, route-selection, or model-compliance failures.

A simulated parser or local file loader cannot establish a real-harness claim. If the harness does not expose file-read traces, a correct sentinel answer is behavioral evidence with lower confidence; report that limitation rather than claiming an observed read.

## Bounded live tool-routing qualification

Reference reachability and tool selection are different claims. Use `qualification/tool-routing/SCENARIOS.md` when claiming that a real model/harness follows Protocol 5.13's specialized routing.

For each **actually available** harness/model/tool combination being claimed:

1. install/build the current lifecycle skill bundle and start a fresh session;
2. ensure the specialized capability is genuinely exposed and record enough harness/model/tool identity to interpret the run;
3. use one representative question whose relation unambiguously triggers the target class;
4. when the harness exposes a trajectory, verify the direct tool-specific reference read before substantive reliance on lower-information defaults;
5. verify either the specialized capability invocation or a concrete permitted fallback such as unsupported backend/language, unavailable tool surface, stale/unreliable state that cannot economically be refreshed, model mismatch, disproportionate setup for a trivially bounded claim, or already-available equally reliable cheaper evidence;
6. do not count silent Grep/Read/shell/test preference as a valid fallback;
7. record only the combination actually exercised; do not infer another harness/model/tool from static tests or from a different combination.

The minimum initiating regression scenario, when a trace-bearing Serena-enabled harness is available, is a nontrivial symbol definition/caller/reference question. The expected trajectory is direct Serena-method entry followed by Serena semantic invocation, unless a concrete permitted fallback is visible. Equivalent bounded scenarios exist for Semgrep structural variants, Hypothesis broad Python invariants, and CodeQL cross-function source-to-sink analysis.

Live qualification is useful evidence, not a generic CI dependency. If no suitable live harness/tool environment is available, Protocol 5.13 may claim deterministic **protocol-level routing semantics** from static/counterfactual/package tests, but it must not claim empirical universal model compliance or an unexecuted harness/tool pass.

## Compatibility matrix

Record actual qualification results here or in a release/PR closeout. Do not infer a pass from static validation.

| Harness | Direct-directory/reference routing | Tool routing | Notes |
| --- | --- | --- | --- |
| Codex/OpenAI | unqualified | unqualified | Run the applicable sentinel and live tool scenario on the target harness/model. |
| Claude Code | unqualified | unqualified | Run the Serena initiating regression when a trace-bearing Serena-enabled environment is available. |
| Pi | unqualified | unqualified | Qualify only installed/exposed tools actually exercised. |
| Gemini CLI / Antigravity | unqualified | unqualified | Qualify only installed/exposed tools actually exercised. |
| GitHub Copilot | unqualified | unqualified | Qualify only installed/exposed tools actually exercised. |
| DeepSeek Harness | unqualified | unqualified | Qualify only installed/exposed tools actually exercised. |

Ordinary repository CI intentionally does not call external agents. Live qualification may be promoted into CI only if credentials, harness/model/tool versions, cost, and stochastic behavior become stable enough to make it a reliable release signal.
