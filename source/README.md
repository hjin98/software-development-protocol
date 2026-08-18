# Software Development Protocol v2

This directory is the **canonical source library**, not an installable Agent Skill.

Protocol v2 separates software-development responsibilities into two generated, self-contained role skills while keeping engineering doctrine in one shared source:

- `software-design-review`: repository inspection, diagnosis, algorithm/architecture design, workplan creation/revision, and post-implementation conformance review.
- `software-implementation`: bounded workplan revalidation, implementation, focused-to-broad testing, benchmarking/evidence, and normative documentation/version/release closeout.

The formal interface between the roles is an **Implementation Workplan**. See `shared/references/workplans-and-agent-handoff.md` and `shared/templates/implementation_workplan_template.md`.

Do not hand-edit generated role packages. Edit this canonical source and run:

```bash
python build_skills.py --output dist
```

The builder copies only the role-relevant shared references/scripts/templates and emits a content-hash manifest in each skill so generated packages can be checked for source drift.
