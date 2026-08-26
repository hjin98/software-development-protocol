# Software Development Protocol

Software Development Protocol 5 is an engineering-fitness-first workflow for AI-assisted software engineering.

## Governing doctrine

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Protocol 5.8 preserves the complete two-role lifecycle and the material engineering guarantees accumulated through Protocols 5.4-5.7 while reducing always-loaded instruction duplication:

```text
software-design -> software-implementation
```

The durable stakeholder product is the objective; workplans, tests, gates, metrics, reviews, and reports are constraints or evidence. Requirements are interpreted according to their protected engineering purpose, not gamed for an easier green result.

`software-design` diagnoses and chooses the product design, preserves task-specific intent in a lossless implementation contract, designs acceptance, and independently reviews when warranted. `software-implementation` realizes that contract adaptively, closes coherent material stages semantically and functionally, and completes final accepted-contract reconciliation plus affected-surface regression/integration.

Protocol 5.8 uses **canonical detailed ownership + progressive disclosure**: lifecycle skills retain high-salience invariants and loading triggers, while detailed generic workflow/testing/architecture/intake/version rules live in their canonical references and are loaded when their material surface becomes relevant. This preserves Protocol 5.4 development economy without weakening Protocol 5.5 lossless handoff, Protocol 5.6 proxy-proof semantic-owner acceptance, or Protocol 5.7 engineering stewardship and acceptance integrity.

Executable changes still require focused checks, stage-local affected regression for every material behavior-changing stage, final affected-surface re-derivation/regression, integration through real product/consumer boundaries, and repository/project-required checks. A local coherent behavior change is normally one stage; proportionality reduces ceremony, never coverage. Production qualification remains separate from functional acceptance.

Independent review remains Software Design mode, not a third lifecycle role. Optional specialists are supporting capabilities, not approval gates.

## Build and repository acceptance

`source/` is canonical and `dist/` contains committed generated skill packages. Before a protocol revision is complete:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```
