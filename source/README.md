# Software Development Protocol v3

This directory is the **canonical source library**, not an installable Agent Skill.

Protocol v3 separates software-development authority into four generated role skills while keeping cross-cutting engineering doctrine in one shared source:

- `software-design`: diagnosis, algorithm/architecture selection, invariant/acceptance design, and Implementation Workplan ownership.
- `software-implementation`: bounded workplan execution, code/test/harness construction, available light validation, candidate closeout, and Qualification Handoff creation.
- `software-qualification`: source-bound target-environment execution and evidence capture; product source is read-only by default.
- `software-verification`: independent final conformance/evidence review and merge-readiness decision.

Formal lifecycle artifacts:

```text
Implementation Workplan
  -> Qualification Handoff
  -> Qualification Report
  -> Verification Report
```

See:

- `shared/references/workplans-and-agent-handoff.md`
- `shared/references/testing-and-qualification.md`
- `shared/references/protocol-versioning-and-compatibility.md`

Do not hand-edit generated role packages. Edit this canonical source and run:

```bash
python build_skills.py --output ../dist
```

Before committing/freeze, verify the committed generated distributions are exact:

```bash
python build_skills.py --output ../dist --check
```

The builder packages only role-relevant shared references/scripts/templates, emits content-hash manifests, builds deterministic ZIPs, and checks role/template/source drift.
