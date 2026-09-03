# Software Development Protocol

Software Development Protocol 5 is an engineering-fitness-first workflow for AI-assisted software engineering.

## Governing doctrine

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Protocol 5.12 preserves the complete two-role lifecycle and every material Protocol 5.4-5.11 engineering safeguard while adding explicit development-convergence and cycle-economy controls:

```text
software-design -> software-implementation
```

The durable stakeholder product is the objective; workplans, tests, gates, metrics, reviews, and reports are constraints or evidence. Requirements are interpreted according to their protected engineering purpose, not gamed for an easier green result.

`software-design` diagnoses and chooses the product design, preserves task-specific intent in a lossless implementation contract, designs acceptance, and independently reviews when warranted. `software-implementation` realizes that contract adaptively, closes coherent material stages semantically and functionally, and completes final accepted-contract reconciliation plus affected-surface regression/integration.

Protocol 5.12 preserves Protocol 5.11 optional tool-assisted methodology, Protocol 5.10 snapshot-complete handoffs, and Protocol 5.9 **canonical detailed ownership + deterministic progressive-disclosure routing** unchanged. Role-critical task triggers still require exact linked references before the corresponding decision or closure, while domain references remain conditional. Final accepted handoffs still carry every binding task-specific semantic in the supplied current artifact set rather than depending on hidden history or conversation state.

The 5.11 addition is a single canonical tool-assisted engineering reference, conditionally routed from both lifecycle roles. Serena can provide semantic repository navigation and bounded editing, Semgrep can provide structural/variant analysis, and Hypothesis can provide property/stateful testing when those capabilities materially improve the task. They are optional environment capabilities and evidence instruments—not generic skill dependencies, lifecycle gates, normative task authority, or substitutes for affected regression and real-boundary integration.

Executable changes still require focused checks, stage-local affected regression for every material behavior-changing stage, final affected-surface re-derivation/regression, integration through real product/consumer boundaries, and repository/project-required checks. A local coherent behavior change is normally one stage; proportionality reduces ceremony, never coverage. Production qualification remains separate from functional acceptance.

Independent review remains Software Design mode, not a third lifecycle role. Optional specialists are supporting capabilities, not approval gates.

## Convergent development

The 5.12 convergence control keeps a first clean local defect local, but material sibling recurrence changes the unit of work to a bounded semantic defect family. Implementation establishes a family closure basis, repairs the canonical owner/mechanism, and proves family-level real-owner plus affected-regression/integration behavior. Genuine same-family recurrence after adequate family closure triggers bounded Design reconsideration before another ordinary sibling patch; reconsideration may preserve frozen design and require consolidation/refactoring rather than automatically creating a new normative revision.

Review readiness, acceptance liveness, proportionate blocker-family saturation, conditional finite-surface census, closure horizons, and revision-number economy reduce repeated rediscovery without making exhaustive scans, matrices, new roles, or fixed review counts universal. Independent review remains able to find material new issues, and genuinely new binding task semantics still enter canonical current authority before the next handoff.

## Build and repository acceptance

`source/` is canonical. `dist/skills/<skill-name>/` contains first-class ready-to-install directory bundles and the existing top-level ZIPs remain backward-compatible transport artifacts generated from the same bundle tree. See `PORTABILITY.md` for installation and real-harness routing qualification. Before a protocol revision is complete:

```bash
python -m pip install -r source/requirements-validation.txt
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```
