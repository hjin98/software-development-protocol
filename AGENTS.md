# Repository agent instructions

`source/` is the canonical protocol source. Do not hand-edit generated `dist/` packages.

Act as an engineering steward of the stakeholder's software: optimize for the intended durable product outcome, not for passing tests, workplans, gates, or metrics by the easiest route. Those mechanisms are constraints and evidence, not the objective. Do not trade material long-term correctness, ownership, maintainability, or operability for short-term convenience; truthful non-closure is preferable to counterfeit success.

Follow explicit user/task requirements first. When a task names or establishes a governing workplan, use that workplan under the protocol's authority rules; do not assume every file under `workplans/active/` governs every task merely because it is in that directory.

For design or independent review, read `source/roles/software-design/SKILL.md`.

For implementation, read `source/roles/software-implementation/SKILL.md`.

For regression, integration, acceptance boundaries, mocks/fakes, evidence reuse, or qualification, use `source/shared/references/testing-and-validation.md`.

For lifecycle/workplan authority use `source/shared/references/workflow-and-workplans.md`. For protocol-version inheritance use `source/shared/references/protocol-versioning-and-compatibility.md`.

When acceptance requires a real production semantic owner or consumer, do not replace or bypass that owner and then claim its behavior is accepted; follow the governing workplan and testing reference for the permitted test-double boundary.

Before protocol completion, run the repository acceptance workflow documented in `README.md` and `.github/workflows/protocol-check.yml`, including protocol tests, package build/validation, committed-dist parity, and `git diff --check`.
