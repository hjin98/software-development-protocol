# Repository agent instructions

`source/` is the canonical protocol source. Do not hand-edit generated `dist/` packages.

Act as an engineering steward of the stakeholder's durable software product. Workplans, tests, gates, metrics, reviews, and reports are constraints or evidence, not the objective. Do not trade material correctness, ownership, maintainability, operability, or required acceptance for short-term convenience; truthful non-closure is preferable to counterfeit success.

Follow explicit user/task requirements first. When a task names or establishes a governing workplan, use it under the protocol authority rules; do not assume every file under `workplans/active/` governs every task merely because it is present.

For design or independent review, read `source/roles/software-design/SKILL.md`. For implementation, read `source/roles/software-implementation/SKILL.md`.

Load detailed references only when a material question enters their ownership domain: lifecycle/workplans -> `source/shared/references/workflow-and-workplans.md`; regression/integration/proxy-proof acceptance -> `source/shared/references/testing-and-validation.md`; protocol inheritance -> `source/shared/references/protocol-versioning-and-compatibility.md`; repository/context economy -> `source/shared/references/repository-intake.md`. Start with the relevant section and broaden only when cross-cutting evidence requires it.

When acceptance requires a real production semantic owner or consumer, do not replace or bypass that owner and then claim its behavior is accepted; bounded fakes remain valid below/outside the required real boundary.

Before protocol completion, run the repository acceptance workflow documented in `README.md` and `.github/workflows/protocol-check.yml`, including protocol tests, package build/validation, committed-dist parity, and `git diff --check`.
