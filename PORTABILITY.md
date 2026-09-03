# Agent portability and routing qualification

Protocol 5.9 preserves Protocol 5.8 engineering doctrine and changes only skill routing, packaging, validation, and compatibility mechanics. The runtime installation unit is the self-contained directory under `dist/skills/<skill-name>/`; the top-level ZIP with the same skill name contains identical files under one enclosing skill directory.

## Installation contract

Install each skill as a direct child of a harness skill root so the entrypoint is exactly `<skills-root>/<skill-name>/SKILL.md`. Do not install `source/roles/...` or `source/specialists/...` directly: canonical source references live under `source/shared/` and become self-contained only in the generated bundles.

Use a harness-supported shared `.agents/skills` root when available, or the harness-native skill root when required. Current commonly supported locations include project `.agents/skills` for Pi, Gemini/Antigravity, GitHub Copilot, and DeepSeek Harness; Claude Code also supports `.claude/skills`, Copilot supports `.github/skills`, Pi supports `.pi/skills`, and DeepSeek Harness supports `.dsh/skills`. Harness-specific paths are integration guidance, not protocol doctrine; verify them against the harness version being qualified.

ZIPs are transport artifacts: extract the enclosing `<skill-name>/` directory before placing it under a runtime skill root. A symlinked/shared installation is a separate harness capability and must be qualified on that harness; direct-directory installation is the portability baseline.

## Why deterministic routing exists

Skill activation proves only that the harness/model obtained `SKILL.md`. Protocol 5.9 therefore makes role-critical routing explicit in each entrypoint: a material task trigger names the exact linked reference and states when reading it is mandatory. Domain references remain conditional so Protocol 5.8 progressive disclosure and context economy are preserved.

Static validation proves that references are packaged, directly linked, and structurally reachable. It cannot prove that a real harness/model actually performs the follow-up read, so live qualification is a separate evidence class.

## Optional external development capabilities

Protocol 5.11 describes Serena, Semgrep, and Hypothesis as **optional environment capabilities**. They are not part of generic Agent Skill validity, the direct-directory installation contract, or Protocol 5.9 routing qualification. A skill remains valid and usable when one or more are unavailable; the agent uses available repository/search/test mechanisms to establish the required engineering claim unless a project-specific contract explicitly requires a named tool.

Generic bundles do not embed Serena MCP declarations, executable/environment paths, credentials, Semgrep service configuration, or Hypothesis installation state. Serena backend capabilities, Semgrep editions/engines, and project-specific Hypothesis settings can vary independently of skill packaging.

A claim that a particular harness actually exposes Serena, executes a Semgrep configuration, or runs a Hypothesis profile requires evidence for that named harness/tool configuration. Static package validation or the routing sentinel does not establish those external-tool claims. Managed/cloud tooling that receives source, findings, or credentials remains subject to project/user authorization and the protocol security/trust rules.

## Bounded live qualification

Use `qualification/reference-routing/protocol-routing-sentinel/` as a tiny independent Agent Skill. The required answer token exists only in its bundled reference; `SKILL.md` deliberately does not contain the token.

For each harness/model/install mode being claimed:

1. copy the sentinel skill directory as a direct child of that harness's skill root;
2. start a fresh session so skill discovery is not inherited from an earlier context;
3. ask: `Use protocol-routing-sentinel and return the routing sentinel.`;
4. verify that the final answer equals the token in `references/sentinel.md`;
5. when the harness exposes a tool/file trajectory, verify an actual read of `references/sentinel.md` after skill activation;
6. classify failures separately as discovery, activation, resource-access/path-canonicalization, route-selection, or model-compliance failures.

A simulated parser or local file loader cannot establish a real-harness claim. If the harness does not expose file-read traces, a correct sentinel answer is behavioral evidence with lower confidence; report that limitation rather than claiming an observed read.

## Compatibility matrix

Record actual qualification results here or in a release/PR closeout. Do not infer a pass from static validation.

| Harness | Direct-directory routing | Read trace observed | Notes |
| --- | --- | --- | --- |
| Codex/OpenAI | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |
| Claude Code | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |
| Pi | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |
| Gemini CLI / Antigravity | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |
| GitHub Copilot | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |
| DeepSeek Harness | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |

Ordinary repository CI intentionally does not call external agents. Live qualification may be promoted into CI only if credentials, harness/model versions, cost, and stochastic behavior become stable enough to make it a reliable release signal.
