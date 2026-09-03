# Software Development Protocol 5.12

This directory is the canonical Protocol 5.12 source.

## Governing hierarchy and product truth

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Build the stakeholder's intended durable product rather than optimizing for the appearance of satisfying a workplan, test, gate, metric, review, or report. Interpret requirements according to their protected engineering purpose. Do not trade material correctness, scientific fidelity, reliability, ownership, maintainability, operability, resource feasibility, target-scale behavior, hardware effectiveness, or required performance for lower complexity or development cost.

Protocol 5.12 preserves all material Protocol 5.4-5.11 guarantees unchanged. It adds explicit development-convergence control: a first clean local defect remains local; material sibling recurrence triggers bounded semantic-family closure; and genuine same-family recurrence after adequate family closure requires bounded Software Design reconsideration before another ordinary patch cycle. Review readiness, acceptance liveness, proportionate blocker-family saturation, conditional finite-surface census, revision-number economy with snapshot-complete current-authority reconciliation, and evidence/test-cycle reuse reduce repeated discovery without reducing reviewer independence or functional acceptance. Protocol 5.11 optional capability-aware tool-assisted engineering guidance for Serena, Semgrep, and Hypothesis remains available as evidence/development methodology rather than a dependency or lifecycle gate.

## Two-role lifecycle

```text
software-design -> software-implementation
```

- `software-design` diagnoses the real problem, defines the engineering envelope, chooses and freezes the globally justified product design, translates task-specific intent losslessly, designs proportionate acceptance, and independently reviews substantial/high-risk implementations.
- `software-implementation` realizes the accepted design against repository reality, incorporates newly discovered necessary consequences, closes coherent material stages semantically and functionally, completes final accepted-contract reconciliation plus affected-surface regression/integration, and delivers the candidate.

Testing and independent review are activities/modes, not extra lifecycle roles. Optional specialists remain supporting capabilities, not approval gates.

## Canonical detailed owners and progressive disclosure

Lifecycle entrypoints contain the invariant, role-local decision rule, and trigger. Detailed generic semantics are owned by the relevant reference:

- lifecycle/workplans/authority/stages/handoff/review routing -> `shared/references/workflow-and-workplans.md`;
- regression/integration/evidence reuse/proxy-proof acceptance/qualification -> `shared/references/testing-and-validation.md`;
- architecture/ownership/redesign/complexity -> `shared/references/architecture-and-design.md`;
- repository inspection/context economy -> `shared/references/repository-intake.md`;
- optional Serena/Semgrep/Hypothesis methodology -> `shared/references/tool-assisted-engineering.md`;
- protocol/workplan inheritance -> `shared/references/protocol-versioning-and-compatibility.md`;
- other domain-specific concerns -> their existing specialist references.

Each packaged `SKILL.md` maps material triggers directly to linked references. Role-critical routes are mandatory before the corresponding decision or closure; domain references remain conditional. Context minimization never permits omission of plausible affected behavior or material evidence.

## Lossless workplans, snapshot-complete handoff, proportionate stages, complete acceptance

A substantial accepted workplan is a compressed task-specific implementation contract. It preserves protected concerns, required end states/constraints, known required implementation consequences, implementation authority, affected surfaces, and acceptance claims without copying generic protocol manuals. It distinguishes `Frozen / Delegated / Reopen only on evidence` and remains a minimum known contract rather than a ceiling on necessary consequences discovered during implementation.

Before final Design -> Implementation handoff, accepted amendments/review corrections are consolidated into supplied current authority. Historical commits, prior chat/review state, superseded revisions, and unsupplied external links may remain provenance but cannot be the only storage location for a still-binding task requirement. Current supplied protocol/specification/architecture/package composition remains valid.

A local coherent behavior change is normally one material stage. Split stages only when an intermediate behavior/risk/dependency boundary materially reduces downstream risk or rework. This changes ceremony, not required coverage.

Executable changes still require focused checks, stage-local affected regression for every material behavior-changing stage, final affected-surface re-derivation/regression, real-boundary integration, and repository/project-required checks. Semantic conformance never substitutes for executable testing; green tests never prove an omitted obligation was implemented. Material real-owner acceptance remains proxy-proof, while bounded fakes below/outside the owner remain valid. Full production qualification remains separate from routine functional acceptance.

## Convergent development

Protocol 5.12 keeps ordinary local work proportionate while making recurrence actionable. A recurring defect family is defined semantically by invariant/product claim, owner/authority, lifecycle/transition class, and failure mechanism—not by file names or broad subsystem labels. Family closure uses a bounded completeness basis and canonical owner repair; incomplete family closure is corrected rather than used to manufacture redesign. Recurrence after adequate family closure triggers Design reconsideration, which may either require same-design structural consolidation or reopen the affected frozen decision when evidence requires it.

Final independent review remains broad and evidence-directed. Implementation owns review readiness and systematic family closure; Review batches cheap/high-information sibling findings, has a bounded stopping rule, and does not turn missing implementation evidence into a new design revision. Ordinary implementation attempts do not require numbered authority snapshots, while genuinely new binding task semantics are still reconciled into current supplied authority before handoff.

## Build and repository acceptance

`source/` is canonical. `dist/skills/<skill-name>/` contains generated ready-to-install directory bundles; top-level ZIPs are generated from the same bundles for backward-compatible transport. `agents/openai.yaml` is a separately validated OpenAI adapter, not part of generic Agent Skill validity. See `../PORTABILITY.md` for harness installation and live routing qualification.

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
