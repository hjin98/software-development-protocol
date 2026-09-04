# Software Development Protocol 5.13

This directory is the canonical Protocol 5.13 source.

## Governing hierarchy and product truth

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Build the stakeholder's intended durable product rather than optimizing for the appearance of satisfying a workplan, test, gate, metric, review, or report. Interpret requirements according to their protected engineering purpose. Do not trade material correctness, scientific fidelity, reliability, ownership, maintainability, operability, resource feasibility, target-scale behavior, hardware effectiveness, or required performance for lower complexity or development cost.

Protocol 5.13 preserves all material Protocol 5.4-5.12 guarantees. It strengthens deterministic progressive disclosure for optional engineering tools, adds CodeQL as a bounded interprocedural/data-flow capability, and performs a lossless control-plane compression pass. The two-role lifecycle, product-truth doctrine, implementation fidelity, proxy-proof acceptance, snapshot-complete handoff, stage-local/final affected regression, convergence/family-closure rules, review readiness, acceptance liveness, and revision economy remain unchanged in engineering meaning.

## Two-role lifecycle

```text
software-design -> software-implementation
```

- `software-design` diagnoses the real problem, defines the engineering envelope, chooses/freezes the globally justified product design, translates task-specific intent losslessly, designs proportionate acceptance, and independently reviews substantial/high-risk implementations.
- `software-implementation` realizes the accepted design against repository reality, incorporates newly discovered necessary consequences, closes coherent material stages semantically and functionally, completes final accepted-contract reconciliation plus affected-surface regression/integration, and delivers the candidate.

Testing and independent review are activities/modes, not extra lifecycle roles. **Optional specialists** remain supporting capabilities, **not approval gates**.

## Canonical detailed owners and progressive disclosure

Lifecycle entrypoints contain high-salience invariants and deterministic triggers. Detailed generic semantics live in canonical references:

- lifecycle/workplans/authority/stages/handoff/rework -> `shared/references/workflow-and-workplans.md`;
- recurrence/family closure/review readiness/saturation/revision economy -> `shared/references/convergence-and-cycle-economy.md`;
- regression/integration/evidence reuse/proxy-proof acceptance/qualification -> `shared/references/testing-and-validation.md`;
- architecture/ownership/redesign/complexity -> `shared/references/architecture-and-design.md`;
- repository inspection/context economy -> `shared/references/repository-intake.md`;
- common optional tool selection/composition/authority -> `shared/references/tool-assisted-engineering.md`;
- Serena method -> `shared/references/tool-serena.md`;
- Semgrep method -> `shared/references/tool-semgrep.md`;
- Hypothesis method -> `shared/references/tool-hypothesis.md`;
- CodeQL local/external and GitHub-managed/code-scanning method -> `shared/references/tool-codeql.md`;
- protocol/workplan inheritance -> `shared/references/protocol-versioning-and-compatibility.md`;
- other domain concerns -> their existing references.

Role-critical routes are mandatory before the corresponding decision or closure. Specialized tool routing is **conditional but deterministic per material question**: classify the relation first, read the directly linked method when a specialized class fires, then use the available/reliable capability or take a concrete permitted fallback. Tool presence never creates a mandatory multi-tool pipeline.

## Tool-assisted engineering in Protocol 5.13

Serena remains the semantic-navigation/reference/bounded-editing instrument; Semgrep remains the AST/structural/variant instrument; Hypothesis remains the Python property/stateful-testing instrument. CodeQL adds optional interprocedural data-flow/taint/source-to-sink analysis.

CodeQL evidence preserves provenance: a local/external CLI run, a separately executed GitHub-managed CodeQL run, and the GitHub code-scanning result/alert surface are not interchangeable concepts. Uploading SARIF from a local run to GitHub does not create an independent second execution. Generic protocol validity does not require GitHub or CodeQL; project-required hosted/local checks remain required when authority explicitly names them.

All analyzer output remains bounded evidence, not product truth or task authority. Specialized tools do not replace focused tests, stage-local/final affected regression, real-boundary integration, repository/project-required checks, or production qualification where required. Hosted/cloud analysis that receives source/findings/credentials remains subject to trust authorization.

## Lossless control-plane compression

Protocol 5.13 restores progressive disclosure after Protocol 5.11-5.12 growth without deleting safeguards. Tool-specific mechanics are split from the common tool router so a Serena question does not require loading Semgrep/Hypothesis/CodeQL manuals. Detailed convergence/cycle-economy mechanics move out of the common workflow owner while compact recurrence/review triggers remain visible in lifecycle/workflow surfaces.

The optimization target is loaded context and duplicated doctrine, not ZIP size or an arbitrary per-file byte quota. Compression is valid only when historical failure-mode defenses remain discoverable at the point they are needed.

## Lossless workplans and complete acceptance

A substantial accepted workplan is a compressed task-specific implementation contract. It preserves protected concerns, required end states/constraints, known required implementation consequences, implementation authority, affected surfaces, and acceptance claims without copying generic protocol manuals. It distinguishes `Frozen / Delegated / Reopen only on evidence` and remains a minimum known contract rather than a ceiling on necessary consequences discovered during implementation.

Before final Design -> Implementation handoff, accepted amendments/review corrections are consolidated into supplied current authority. Historical commits, prior chat/review state, superseded revisions, and unsupplied external links may remain provenance but cannot be the only storage location for a still-binding task requirement.

Executable changes still require focused checks, stage-local affected regression for every material behavior-changing stage, final affected-surface re-derivation/regression, real-boundary integration, and repository/project-required checks. Semantic conformance never substitutes for executable testing; green tests never prove an omitted obligation was implemented. Material real-owner acceptance remains proxy-proof while bounded fakes below/outside the owner remain valid. Full production qualification remains separate from routine functional acceptance.

## Build and repository acceptance

`source/` is canonical. `dist/skills/<skill-name>/` contains generated ready-to-install directory bundles; top-level ZIPs are generated from the same bundle tree for backward-compatible transport. `agents/openai.yaml` is separately validated adapter metadata, not generic Agent Skill validity. See `../PORTABILITY.md` for installation, reference-routing qualification, and bounded live tool-routing qualification.

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
