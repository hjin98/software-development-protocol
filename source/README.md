# Software Development Protocol 5.14

This directory is the canonical Protocol 5.14 source.

## Governing hierarchy and authority boundary

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Protocol 5.14 clarifies the operational meaning of that existing hierarchy.

- **Tier 1A — product/problem truth:** the stakeholder's research, computational, scientific, operational, correctness, reliability, compatibility, resource, performance, security, and governed external-contract demands.
- **Tier 1B — Frozen high-level architecture:** material architecture/ownership/algorithm/data-representation/resource/compatibility decisions Software Design deliberately fixes for the current implementation cycle.
- **Tier 2 — solution machinery:** everything beneath that boundary. Functions, helpers, wrappers, adapters, retries, caches, state machines, synchronization paths, intermediate representations, implementation-created invariants, and previous patches remain replaceable unless explicitly promoted into Frozen architecture by Design.
- **Tier 3 — development economy:** optimize reasoning/context/tool/compute/I/O/wall-time only after the required product is achieved through the minimum justified Tier-2 system.

Implementation machinery does not become Tier 1 through existence, dependency, tests, documentation, prior review, previous workplan wording, or previous repair. Correctness of a current mechanism and necessity of that mechanism are separate questions.

## Active simplicity

A first clean local defect remains a local owning-layer repair. But when repeated patches, patch-on-patch repair, duplicated/synchronized state, competing authorities, accumulating wrappers/fallbacks/special cases, repeated reconciliation machinery, or an evident materially simpler realization show that the Tier-2 solution has ossified, simplification/re-derivation is mandatory before another additive durable repair.

Hold Tier-1 product truth and Frozen high-level architecture fixed, then prefer removing, narrowing, altering, consolidating, or refactoring the cause of solution-created problems. Add machinery only when a genuinely required capability remains absent or one canonical mechanism replaces broader existing complexity.

Affected-surface expansion expands inspection, implementation impact, and acceptance coverage; it does not by itself expand the product requirement or freeze the current realization.

## Two-role lifecycle

```text
software-design -> software-implementation
```

- `software-design` diagnoses the real problem, classifies product/problem invariants versus cycle-scoped Frozen architecture versus delegated solution space, chooses the globally justified high-level design, defines active simplification triggers, translates task-specific intent losslessly, designs acceptance, and independently reviews substantial/high-risk implementations.
- `software-implementation` realizes that contract adaptively, may simplify/replace delegated machinery while preserving Tier 1, closes coherent material stages semantically and functionally, performs active Tier-2 restoration when structural complexity triggers fire, and completes final accepted-contract reconciliation plus affected-surface regression/integration.

Testing and independent review are activities/modes, not extra lifecycle roles. Optional specialists remain supporting capabilities, not approval gates.

## Deterministic progressive disclosure and tools

Protocol 5.14 preserves Protocol 5.13 deterministic per-question tool routing and optional-tool status:

```text
literal/path/text -> ordinary repository search/read
symbol owner/definition/reference/caller -> Serena
AST/syntax/structural pattern -> Semgrep
broad Python input/state invariant -> Hypothesis
interprocedural flow/taint/source-to-sink -> CodeQL
```

A specialized trigger directly routes to its tool-specific method. When availability is unknown, use a cheap non-mutating capability probe when practical; when the capability is available/current/supported and directly models the claim, presumptively use it, otherwise take a concrete permitted fallback. Tool presence never creates a fixed multi-tool pipeline.

All analyzer output remains bounded evidence, not product truth or task authority. Tools do not replace focused tests, stage-local/final affected regression, real-boundary integration, repository/project-required checks, or production qualification where required.

## Workplans and complete acceptance

A substantial accepted workplan is a compressed task-specific implementation contract, not a frozen proof script. It preserves product/problem invariants, Frozen high-level architecture, delegated solution space, task-specific acceptance boundaries, affected surfaces, and genuine redesign/simplification triggers.

The plan remains a minimum known contract rather than a ceiling only for newly discovered affected behavior and logically necessary consequences of already-binding product/Frozen semantics. Discovery does not mint new product requirements or grant incidental machinery invariant status.

Executable changes still require focused checks, stage-local affected regression for every material behavior-changing stage, final affected-surface re-derivation/regression, real-boundary integration, and repository/project-required checks. Semantic conformance never substitutes for executable testing; green tests never prove an omitted obligation was implemented. Material real-owner acceptance remains proxy-proof while bounded fakes below/outside the owner remain valid. Full production qualification remains separate from routine functional acceptance.

## Canonical detailed owners

Lifecycle entrypoints retain high-salience invariants and deterministic triggers. Detailed semantics live in canonical references:

- lifecycle/workplans/authority/stages/handoff/rework -> `shared/references/workflow-and-workplans.md`;
- recurrence/active simplification/review readiness/revision economy -> `shared/references/convergence-and-cycle-economy.md`;
- regression/integration/evidence reuse/proxy-proof acceptance/qualification -> `shared/references/testing-and-validation.md`;
- Tier-1/Tier-2 boundary, architecture/ownership/redesign/complexity -> `shared/references/architecture-and-design.md`;
- repository inspection/context economy -> `shared/references/repository-intake.md`;
- optional tool selection/composition -> `shared/references/tool-assisted-engineering.md`;
- Serena method -> `shared/references/tool-serena.md`;
- Semgrep method -> `shared/references/tool-semgrep.md`;
- Hypothesis method -> `shared/references/tool-hypothesis.md`;
- CodeQL method -> `shared/references/tool-codeql.md`;
- protocol/workplan inheritance -> `shared/references/protocol-versioning-and-compatibility.md`;
- other domain concerns -> their existing references.

## Build and repository acceptance

`source/` is canonical. `dist/skills/<skill-name>/` contains generated ready-to-install directory bundles; top-level ZIPs are generated from the same bundle tree for backward-compatible transport. `agents/openai.yaml` remains separately validated adapter metadata.

Run:

```bash
python -m pip install -r source/requirements-validation.txt
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

All commands must succeed before a protocol revision is complete.
