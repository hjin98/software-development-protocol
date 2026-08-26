# Software Development Protocol 5.8

This directory is the canonical Protocol 5.8 source.

## Governing hierarchy and product truth

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Build the stakeholder's intended durable product rather than optimizing for the appearance of satisfying a workplan, test, gate, metric, review, or report. Interpret requirements according to their protected engineering purpose. Do not trade material correctness, scientific fidelity, reliability, ownership, maintainability, operability, resource feasibility, target-scale behavior, hardware effectiveness, or required performance for lower complexity or development cost.

Protocol 5.8 preserves all material Protocol 5.4-5.7 guarantees while reducing control-plane duplication. High-salience invariants remain directly visible in lifecycle skills; detailed generic rules have one canonical reference owner where practical and are loaded when their material surface becomes relevant.

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

Load a reference when a material question enters its ownership domain; start with the relevant section and broaden only when cross-cutting evidence requires it. Context minimization never permits omission of plausible affected behavior or material evidence.

## Lossless workplans, proportionate stages, complete acceptance

A substantial accepted workplan is a compressed task-specific implementation contract. It preserves protected concerns, required end states/constraints, known required implementation consequences, implementation authority, affected surfaces, and acceptance claims without copying generic protocol manuals. It distinguishes `Frozen / Delegated / Reopen only on evidence` and remains a minimum known contract rather than a ceiling on necessary consequences discovered during implementation.

A local coherent behavior change is normally one material stage. Split stages only when an intermediate behavior/risk/dependency boundary materially reduces downstream risk or rework. This changes ceremony, not required coverage.

Executable changes still require focused checks, stage-local affected regression for every material behavior-changing stage, final affected-surface re-derivation/regression, real-boundary integration, and repository/project-required checks. Semantic conformance never substitutes for executable testing; green tests never prove an omitted obligation was implemented. Material real-owner acceptance remains proxy-proof, while bounded fakes below/outside the owner remain valid. Full production qualification remains separate from routine functional acceptance.

## Build and repository acceptance

`source/` is canonical. `dist/` contains generated ready-to-install skill packages and is committed for distribution.

Run:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

All commands must succeed before a protocol revision is complete.
