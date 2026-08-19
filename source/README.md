# Software Development Protocol v3

This directory is the **canonical source library**, not an installable Agent Skill.

Protocol v3 separates software-development authority into four generated role skills while keeping cross-cutting engineering doctrine in one shared source:

- `software-design`: diagnosis, algorithm/architecture selection, invariant/acceptance design, and Implementation Workplan ownership.
- `software-implementation`: bounded workplan execution, code/test/harness construction, available light validation, candidate closeout/content identity, and Qualification Handoff creation.
- `software-qualification`: candidate-content-bound target-environment execution and evidence capture; product source and tracked candidate outputs are read-only.
- `software-verification`: independent final conformance/evidence/reuse review and merge-readiness decision.

Formal lifecycle artifacts:

```text
Implementation Workplan
  -> Qualification Handoff
  -> Qualification Report
  -> Verification Report
```

Protocol v3 distinguishes `candidate_commit`, `candidate_content_identity`, and later evidence/coordination commits. Qualification preflight/postflight must establish a clean unambiguous candidate surface; evidence-only commits do not invalidate the qualification when they preserve candidate content identity under the declared policy.

See:

- `shared/references/workplans-and-agent-handoff.md`
- `shared/references/testing-and-qualification.md`
- `shared/references/protocol-versioning-and-compatibility.md`
- `shared/references/protocol-v3-freeze-checklist.md`

Do not hand-edit generated role packages. Edit this canonical source and run:

```bash
python build_skills.py --output ../dist
```

Before committing/freeze, verify semantic and generated parity:

```bash
python check_protocol_semantics.py
python build_skills.py --output ../dist --check
```

The builder packages only role-relevant shared references/scripts/templates, emits content-hash manifests, builds deterministic ZIPs, and checks role/template/source drift. `check_protocol_semantics.py` enforces critical v3 authority/identity/immutability fields that ordinary package generation cannot infer from prose.
