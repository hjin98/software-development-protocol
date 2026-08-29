# Software Development Protocol

Software Development Protocol 5 is an engineering-fitness-first workflow for AI-assisted software engineering.

## Governing doctrine

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Protocol 5.9 preserves the complete two-role lifecycle and every material Protocol 5.4-5.8 engineering safeguard while making Protocol 5.8 progressive disclosure deterministic and portable across Agent-Skills-style harnesses:

```text
software-design -> software-implementation
```

The durable stakeholder product is the objective; workplans, tests, gates, metrics, reviews, and reports are constraints or evidence. Requirements are interpreted according to their protected engineering purpose, not gamed for an easier green result.

`software-design` diagnoses and chooses the product design, preserves task-specific intent in a lossless implementation contract, designs acceptance, and independently reviews when warranted. `software-implementation` realizes that contract adaptively, closes coherent material stages semantically and functionally, and completes final accepted-contract reconciliation plus affected-surface regression/integration.

Protocol 5.9 keeps Protocol 5.8 **canonical detailed ownership + progressive disclosure** unchanged, but makes routing explicit: role-critical task triggers require exact linked references before the corresponding decision or closure, while domain references remain conditional. This changes how reliably agents reach the doctrine, not what the doctrine means.

Executable changes still require focused checks, stage-local affected regression for every material behavior-changing stage, final affected-surface re-derivation/regression, integration through real product/consumer boundaries, and repository/project-required checks. A local coherent behavior change is normally one stage; proportionality reduces ceremony, never coverage. Production qualification remains separate from functional acceptance.

Independent review remains Software Design mode, not a third lifecycle role. Optional specialists are supporting capabilities, not approval gates.

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
