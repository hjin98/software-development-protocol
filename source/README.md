# Software Development Protocol 5.9

This directory is the canonical Protocol 5.9 source.

## Governing hierarchy and product truth

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Build the stakeholder's intended durable product rather than optimizing for the appearance of satisfying a workplan, test, gate, metric, review, or report. Interpret requirements according to their protected engineering purpose. Do not trade material correctness, scientific fidelity, reliability, ownership, maintainability, operability, resource feasibility, target-scale behavior, hardware effectiveness, or required performance for lower complexity or development cost.

Protocol 5.9 preserves all material Protocol 5.4-5.8 guarantees unchanged. It strengthens only routing and distribution: high-salience entrypoint triggers now link directly to exact canonical references, role-critical routes are mandatory under their named conditions, and domain references remain progressively disclosed.

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
- protocol/workplan inheritance -> `shared/references/protocol-versioning-and-compatibility.md`;
- other domain-specific concerns -> their existing specialist references.

Each packaged `SKILL.md` now maps material triggers directly to linked references. Role-critical routes are mandatory before the corresponding decision or closure; domain references remain conditional. Context minimization never permits omission of plausible affected behavior or material evidence.

## Lossless workplans, proportionate stages, complete acceptance

A substantial accepted workplan is a compressed task-specific implementation contract. It preserves protected concerns, required end states/constraints, known required implementation consequences, implementation authority, affected surfaces, and acceptance claims without copying generic protocol manuals. It distinguishes `Frozen / Delegated / Reopen only on evidence` and remains a minimum known contract rather than a ceiling on necessary consequences discovered during implementation.

A local coherent behavior change is normally one material stage. Split stages only when an intermediate behavior/risk/dependency boundary materially reduces downstream risk or rework. This changes ceremony, not required coverage.

Executable changes still require focused checks, stage-local affected regression for every material behavior-changing stage, final affected-surface re-derivation/regression, real-boundary integration, and repository/project-required checks. Semantic conformance never substitutes for executable testing; green tests never prove an omitted obligation was implemented. Material real-owner acceptance remains proxy-proof, while bounded fakes below/outside the owner remain valid. Full production qualification remains separate from routine functional acceptance.

## Build and repository acceptance

`source/` is canonical. `dist/skills/<skill-name>/` contains generated ready-to-install directory bundles; top-level ZIPs are generated from the same bundles for backward-compatible transport. `agents/openai.yaml` is a separately validated OpenAI adapter, not part of generic Agent Skill validity. See `../PORTABILITY.md` for harness installation and live routing qualification.

Run:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

All commands must succeed before a protocol revision is complete.
