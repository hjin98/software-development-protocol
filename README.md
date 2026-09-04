# Software Development Protocol

Software Development Protocol 5 is an engineering-fitness-first workflow for AI-assisted software engineering.

## Governing doctrine

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Protocol 5.13 preserves the complete two-role lifecycle and all material Protocol 5.4-5.12 safeguards while strengthening deterministic tool entry, adding CodeQL as an optional interprocedural/data-flow capability, and restoring progressive-disclosure context economy:

```text
software-design -> software-implementation
```

The durable stakeholder product is the objective; workplans, tests, gates, metrics, reviews, and reports are constraints or evidence. Requirements are interpreted according to their protected engineering purpose, not gamed for an easier green result.

`software-design` diagnoses and chooses the product design, preserves task-specific intent in a lossless implementation contract, designs acceptance, and independently reviews when warranted. `software-implementation` realizes that contract adaptively, closes coherent material stages semantically and functionally, and completes final accepted-contract reconciliation plus affected-surface regression/integration.

## Deterministic progressive disclosure

Protocol 5.13 preserves Protocol 5.9 deterministic reference routing and makes optional tool routing operational **per material engineering question** rather than depending on an agent first deciding that an unfamiliar tool would help. The relation under the current claim determines the route:

```text
literal/path/text -> ordinary repository search/read
symbol owner/definition/reference/caller -> Serena
AST/syntax/structural pattern -> Semgrep
broad Python input/state invariant -> Hypothesis
interprocedural flow/taint/source-to-sink -> CodeQL
```

A specialized trigger directly routes to its tool-specific method. When availability is unknown, the agent uses a cheap non-mutating capability probe when practical; when the capability is available/current/supported and directly models the claim, it is presumptively used, otherwise the agent takes a concrete permitted fallback. Familiarity with built-in search/read/shell/test primitives is not itself a fallback reason. Tool availability alone never creates a fixed multi-tool pipeline.

The former monolithic tool manual is split into one compact common selection/composition owner plus Serena, Semgrep, Hypothesis, and CodeQL method references. Detailed Protocol 5.12 convergence/cycle-economy mechanics are likewise conditionally owned outside the common workflow reference, while compact recurrence/review triggers remain directly visible. This reduces loaded context and duplication without weakening accepted doctrine.

## CodeQL evidence model

CodeQL is optional and specialized for supported interprocedural/data-flow relations. Protocol 5.13 distinguishes:

1. local/external CodeQL execution;
2. separately executed GitHub-managed CodeQL analysis;
3. the GitHub code-scanning result/alert surface, which may contain results from managed CodeQL, uploaded SARIF, or another analyzer.

Uploading SARIF from a local run does not create a second independent execution merely because the result appears in GitHub. Database/source/build/query identity, invalidation after relevant changes, negative-evidence bounds, query governance, privileged build/extraction behavior, resource limits, and upload trust boundaries are all explicit. Generic protocol validity does not require GitHub or CodeQL unless project/task authority independently requires a named check.

## Acceptance and convergence remain intact

Executable changes still require focused checks, stage-local affected regression for every material behavior-changing stage, final affected-surface re-derivation/regression, integration through real product/consumer boundaries, and repository/project-required checks. Semantic conformance never substitutes for executable testing; green tests never prove an omitted obligation was implemented. Production qualification remains separate from functional acceptance.

A first clean local defect remains local. Material sibling recurrence changes the unit of work to a bounded semantic family; genuine same-family recurrence after adequate family closure triggers bounded Software Design reconsideration before another ordinary sibling patch. Review readiness, acceptance liveness, blocker-family saturation, finite-surface census when justified, closure horizons, revision economy, and evidence reuse remain preserved through the conditionally loaded convergence reference.

Independent review remains Software Design mode, not a third lifecycle role. Optional specialists and optional analyzers are supporting capabilities, not approval gates.

## Build and repository acceptance

`source/` is canonical. `dist/skills/<skill-name>/` contains first-class ready-to-install directory bundles and top-level ZIPs remain backward-compatible generated transport artifacts. See `PORTABILITY.md` for installation, reference-routing qualification, and live tool-routing qualification.

Before a protocol revision is complete:

```bash
python -m pip install -r source/requirements-validation.txt
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```
