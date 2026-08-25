# Software Development Protocol

Software Development Protocol 5 is an engineering-fitness-first workflow for AI-assisted software engineering.

## Governing doctrine

> **Choose the globally best justified engineering-sufficient product. Among engineering-sufficient solutions, prefer the one with the lowest justified total product/system complexity. Among development processes that can establish that result with the required confidence, avoid unnecessary human, model, context/token, tool, compute, I/O, and wall-time cost.**

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Protocol 5.5 preserves this doctrine and the two-role lifecycle:

```text
software-design -> software-implementation
```

`software-design` diagnoses and chooses the accepted product design, then translates it into a **lossless implementation contract**: material protected concerns, required end states/constraints, known required implementation consequences, clearly distinguishable suggested/delegated mechanics, affected surfaces, and acceptance evidence. `software-implementation` realizes that contract adaptively against repository reality, closes semantic conformance and functional regression at each material stage, completes final contract reconciliation plus affected-surface regression/integration, and delivers the candidate.

The accepted workplan remains subordinate to explicit requirements and governed contracts, distinguishes **Frozen / Delegated / Reopen only on evidence**, and is a **minimum known contract rather than a ceiling** on necessary consequences discovered during implementation.

Independent review remains a Software Design activity, not a third lifecycle role. It challenges contract conformance and then unplanned engineering risk. Material review findings should return enough evidence, corrected-end-state information, acceptance evidence, and routing to support lossless rework. Implementation nonconformance returns under the same accepted design; a workplan/design deficiency is reconciled before reimplementation; genuinely new issues are classified locally or reopened on evidence.

Executable changes still require focused checks, stage-local affected regression after every material behavior-changing stage, final affected-surface re-derivation/regression, integration, and repository/project-required checks. Semantic conformance never substitutes for executable testing, and green tests never prove a material omitted obligation was implemented. Production qualification remains separate from functional acceptance.

Protocol 5.4 context/evidence economy also remains intact: use progressive high-information inspection, reuse still-valid facts/evidence, avoid low-information repetition, and do not create persistent ledgers or process machinery without independent engineering value.

## Build and repository acceptance

`source/` is canonical and `dist/` contains committed generated skill packages. Before a protocol revision is complete:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```
